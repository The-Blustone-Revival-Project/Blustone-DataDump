# CDN.db decoded schema, and what the startup stall actually is

Date: 2026-10-02
Supersedes part of `2026-09-30-startup-stall-investigation.md`.

## TL;DR

The client is **not** deadlocked and **not** waiting on us. Its main thread is
parked in the HTTP event loop, the CDN step completes correctly and concludes
"nothing to download", and then **nothing calls the next step**. The launcher
never issues `/v2/account/RegisterGuest` or `/v2/account/Login`.

We also now know the exact on-disk schema the client uses to decide what to
download, which is the thing to instrument next.

## 1. The decisive measurement: thread blocking state

Added to `Telemetry`: a `thread_states` event on every heartbeat, sampling
`/proc/self/task/<tid>/{stat,wchan,comm}` for all threads. Reading the app's
own `/proc` needs no root.

On the stalled client:

```
main thread  tid 5309  state S  wchan SyS_epoll_wait

94 threads total:
  70  futex_wait_queue_me
  12  SyS_epoll_wait
   3  hrtimer_nanosleep
   3  running (wchan 0)
   1  unix_stream_read_generic
   1  do_sigtimedwait
   1  poll_schedule_timeout
```

Read this carefully, because it eliminates the obvious hypothesis:

- The main thread is **not** in `futex_wait_queue_me`, so it is **not** blocked
  on a mutex or condition variable. "Deadlock" is the wrong word.
- It is in `epoll_wait`, i.e. sitting in the curl event loop with no socket
  activity to service.
- 70 other threads are parked on futexes, which is the normal steady state for
  a 94-thread process (thread pools, Glide, OkHttp, Crashlytics).

Corroborating socket evidence: one `CLOSE_WAIT` socket to the replica and one
`ESTABLISHED` to BlueStacks' local ads service. **No pending outbound request.**
So the engine is waiting for an event/callback, not for bytes from us.

## 2. Assertions are not the cause

The shipped native patch set silences the game's own reporter:

| what | offset | default patch |
|---|---|---|
| `RMAssert` | `0x10B3ABC` | stubbed to `movs r0,#0; bx lr` |
| `CSRUIParser::ParseRes2` anim assert | `0x107FA10` | `beq` → `bne` (inverted) |
| `GMLevelDB` Put assert | `0x784CFE` | `beq` → `bne` (inverted) |

So a failing assertion is stepped over silently, which would make "we sent
something wrong" look identical to "the client hung".

Built a variant that leaves all three live (`--keep-asserts`) and ran it.
**Nothing fires.** The stall is not a silenced assertion. The flag is kept
because the *next* missing-response failure will be silent otherwise.

## 3. The engine's own CDN logging is compiled out

The binary contains `download reslist(%s) from server`, `DownloadHeader`,
`did you try to download?`, `Success that download the file(%s)`, the
`PV_CDN_*` error names, and the `[JET] ExtractJETInfo/The time-stamp is
miss-matching` message. **None of them ever print**, even at `RMDBG_LOG(FULL)`.

The `[FWK]`/`[ERR]`/`[ADS]`/`[JUC]`/`[RSM]` framework messages do print, so the
logger works; the CDN module's log statements are simply not in this build.
Consequence: **logging has to be added natively** - there is no existing log
line to un-suppress.

## 4. CDN.db schema (decoded from the collector's artifact)

Decoded with `tools/inspect-leveldb.py` against the `local__CDN.db` artifacts.
192 keys under two prefixes.

### Remote manifest (what the client parsed out of the reslist)

```
CDN/header/stamp            reslist version
CDN/header/cnt              package count           (int32, plaintext)
CDN/header/size             total size
CDN/header/items/<PKG>/name
CDN/header/items/<PKG>/stamp
CDN/header/items/<PKG>/size
CDN/header/items/<PKG>/step                           (int32, plaintext)
CDN/header/items/<PKG>/sign
CDN/header/items/<PKG>/md5
CDN/header/items/<PKG>/pkg
```

### Local unpacked state (what the client already has on disk)

```
CDN/PVC/<PKG>/stamp
CDN/PVC/<PKG>/packs
CDN/PVC/<PKG>/packs/[<packid>]/filename
CDN/PVC/<PKG>/packs/[<packid>]/sign
CDN/PVC/<PKG>/packs/[<packid>]/size
```

`<packid>` is a 64-bit hash of the unpacked content, e.g.
`[10862646430480732674]` for `E_NEW`.

### Value encoding

`int32` fields (`cnt`, `step`) are stored plaintext little-endian. The
string-ish fields (`name`, `stamp`, `size`, `sign`, `md5`) are **encrypted
blobs** - so the local database is not readable without the client's key. Only
the int fields and the key names are directly usable. Note `stamp` is a
variable-length encoding, not a fixed 4-byte int.

### What the current device state says

```
header items                 : 11  (E_NEW, E_MIDAGE, PK_LM2, PK_LM4, PK_LM5,
                                     PK_MO3, PK_MO5, PK_MT3, PK_MT5, PK_WK1,
                                     VD_MISSION)
PVC/<PKG>/stamp present      : 11
PVC/<PKG>/packs present      : 11
missing local state          : (none)
```

Two things follow, and both matter:

1. **The client parsed our reslist successfully.** `CDN/header/cnt = 11` and
   all 11 `items/<PKG>/*` subtrees exist, written from *our* manifest. The
   reslist wire format is therefore correct - which independently confirms the
   negative results from 2026-09-30 (a forced fresh stamp, and a 0-package
   manifest, both still stalled).
2. **Every package is already current locally**, so the CDN step has nothing to
   download and finishes immediately. Then the launcher does nothing at all.

## 5. Where the stall actually is

```
launcher/GetBaseInfo      -> 200
shared_secret/Exchange    -> 200
reslist_*.list            -> 200   (parsed, stored: header/cnt = 11)
<CDN step completes, no work to do>
<nothing>                  main thread in epoll_wait, no further request
```

The missing piece is the **completion callback of the resource-check
operation**: the CDN step finishes, but whatever should be signalled to proceed
to account registration never is. This is a client-side wait, not a missing or
malformed response, and it is consistent with every negative result so far.

## 6. What to instrument next

Now that the CDN state model is known, the native work is concrete rather than
guesswork. Build a `write(2)`-to-stderr trace stub (no imports, fully
relocatable; `-b stderr` is now captured by the app) and hook these addresses,
which come from the retained symbol table in `analysis/native-evidence.tsv`:

| address | symbol | why |
|---|---|---|
| `0x7d2f9c` | `CPVCDN2::DownloadHeader` | entry/exit of the reslist fetch |
| `0x7ccd80` | `CPVCDN2::PrepareDiff(unsigned)` | the decide-what-to-download step; the argument is the interesting one |
| `0x7d3940` | `CPVCDN2::DownloadStep(int,unsigned,...)` | per-item step |
| `0x7cd818` | `CPVCDN2::UnpackAll(unsigned,...)` | entry/exit |
| `0x7cfcf8` | `CPVCDN2::UnPacking(vector<unsigned char> const&)` | the unpack check |
| `0x7d0120` | `CPVCDN2::DownloadItem(...)` | per-item download |

Caveat found while preparing this: these symbol addresses are **not** clean
function entries. For example `DownloadStep` at `0x7d3940` begins
`2de9 000f` and `DownloadHeader` at `0x7d2f9c` begins `0134 01e0`, neither of
which is a recognisable prologue. Each hook site must be inspected and the
original instructions replicated in the stub, which is why it has not been done
blind. `tools/patch-native-ui-animation.py` is the existing precedent for
build-time patching with expected-byte verification, Thumb branch encoders and
code caves in bypassed function bodies.

Two supporting observations from the binary:

- `pv-prd.vshower.com` occurs **once** (`0x1D5EC56`, the literal we redirect).
  Every other `.com` / `http://` string is libcurl or PKCS internals
  (`ftp@example.com`, `http_proxy`, `CMS_ATTRIBUTES`, ...). So there is no
  second production host the client could be stuck contacting.
- libcurl resume support is compiled in: `Range: bytes=%lld-`,
  `Couldn't resume download`, `File already completely downloaded`,
  `partial download completed, closing connection`, and a `header_cb`
  `CURLOPT_HEADERFUNCTION`. `header/stamp` and `header\stamp` are literal
  strings and may name the record `CPVCDN2` writes after the reslist.
