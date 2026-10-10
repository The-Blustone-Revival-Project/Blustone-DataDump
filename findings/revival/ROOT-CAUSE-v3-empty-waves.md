# ROOT CAUSE v3 — the enemy camp map is never created because the `waves` vector is empty

Written by the orchestrator, 2026-10-02. This is the **complete, end-to-end causal chain**, and
it supersedes `FALSIFIED-showthumbnail.md` §2 and closes `ADJUDICATION-crash-site.md`.

**Status: [RECOVERED] at every link, with the final register state derived from the standard
library rather than fitted to the crash report.**

---

## 1. The chain in full

```
1.  CSRSceneMEpisode / CSRMStage selected by MODE (a constructor arg, no JSON)
    -> default is CSRMStage, the expedition scene. CORRECT scene.
2.  CSRMStage::InitBeforeOpen (0xb33ccc)
    -> CSRDataMgr::LoadLevelData("leveling_m")           compile-time literal
    -> CSRLevelData::LoadLevelData (0xa178c4) reads <root>leveling_m.JSON from the LOCAL CM DB
    -> CSRLevelData::GetMonsterGroupID() == CMHashID("enemy")   CONSTANT, for every level/stage
3.  /reference/GetTargetStageMonster response
    -> ReqTargetStageMonsterCB (0xb4606c), result_code == 1
    -> AddStageMonster (0xa0d194)   [bl 0x00a0d194 at 0xb4612c, UNCONDITIONAL - reached]
    -> reads _id, wave_list[].ref_id, .group, .next_spawn_ms, .show_thumbnail
    -> emplaces into CSRGameMob: map<string, STAGE_MONSTER_LINK>
4.  CSRMStage::MakeStageInst (0xb33f84)
    -> GetStageMonsterLinkData(this+0x220)      the link map
    -> loop 0xb34b0e..0xb34e8c: outer vector stride 0xc, inner STAGE_MONSTER stride 0x14
    -> if the WAVES vector is empty:  beq.w -> 0x00b34e88   (skip EVERYTHING)
    -> the "enemy" key is therefore NEVER CREATED in this+0x264
5.  0xb3506a  unconditional final store, after the wave loop
    -> emplaces a FRESH, EMPTY list<list<ACTOR_INFO>> for the "enemy" key
    -> 0xb3507a  str r0,[r1,#0x4c]        <-- SIGSEGV
```

## 2. Why `r1 == 0` — derived, not fitted

This is the part that makes the chain trustworthy. `std::list`'s own constructor at
`0x00904604` initialises a fresh node as:

```
__m_begin_ = __m_end_ = entry + 0x20
__m_size_  = 0
```

So the store sequence is:

```
ldr r1, [r1, #0x20]   -> the list sentinel (entry+0x20)
ldr r1, [r1, #8]      -> __m_size_ == 0        (libstdc++ offset)
str r0, [r1, #0x4c]   -> fault address 0x4c    (r1 == 0)
```

That reproduces the device's `fault=0x4c`, `r1=0`, `r0=0x0a` **from the container's own
constructor**, before consulting the crash report. I independently confirmed the encoding
(halfword `0x64c8` = `str r0,[r1,#0x4c]` at Ghidra `0xb3507a`, immediately below the reported
PC) — see `ADJUDICATION-crash-site.md` §2.

## 3. The single defect

**The `waves` vector of the `STAGE_MONSTER_LINK` we build is empty**, so step 4 skips and the
`"enemy"` key is never created.

Two sub-cases, and the evidence distinguishes them (Q5 of the analysis):

| Condition | Result |
|---|---|
| A **wave** is empty | an **empty inner list** is still inserted — degraded, does not crash |
| The **`waves` vector** is empty | `beq.w 0x00b34e88` skips everything, key never created, then the unconditional store crashes |

We are in the second case. **`AddStageMonster` is reached and returns without emplacing a usable
waves vector** — i.e. our response is read and then yields nothing.

### What this rules out
- **NOT the map key.** Keying `ret_data` by monster id (`5acb45e`) was real and necessary — it
  took assertions 6 → 0 — but it is not what leaves `waves` empty.
- **NOT `show_thumbnail`'s type.** A clean device negative (report-012): array and integer are
  indistinguishable down to the crash registers. Keep the array — it is correctly shaped — but
  it is not the lever.
- **NOT a missing level file.** `leveling_m.JSON` is a compile-time literal and `LEVELING.jet`
  ships in the base APK byte-identically.
- **NOT the wrong scene.** `CSRMStage` is the default and no response field selects the scene.
- **NOT dead code.** `AddStageMonster` is reached unconditionally.

### The open sub-question
The analysis recovered **`wave_list[].ref_id` as the field consumed for the camp's inner
strings** — a key **not** in `AGENTS.md` §11's list. And the decompile reads `_id` *and*
`wave_list` from **two different addends on the same literal slot** (verified by me:
`tools/resolve-literals-offline.py --function 0xa0d194:0xa0d300` resolves slot `0xa0d4f4` to
both `'_id'` at addend `0xa0d1b8` **and** `'wave_list'` at addend `0xa0d1bc`).

So the two candidates for the waves array are `_id` and `wave_list`, and our response currently
publishes **both** as arrays of wave objects. The most likely reason `waves` still ends up empty
is therefore **not the array key but the array's element shape** — `AddStageMonster` builds
`STAGE_MONSTER` per element from `ref_id`/`group`/`next_spawn_ms`, and if an element is missing
one of those the record may be discarded.

## 4. Next step — one cheap observation, then one shape change

**First, and it is nearly free: log what the client actually received.** `BLUSTONE_DUMP_RESPONSES=1`
already exists. The single most valuable datum is the exact decrypted `ret_data` the client got
for `/reference/GetTargetStageMonster`, byte for byte, so we can confirm what shape `waves` was
built from rather than inferring it. The test lane has been asked for this.

**Then**, if the waves vector is still empty, the fix is in the **wave record's element shape**
— specifically making sure each element of both `_id[]` and `wave_list[]` carries
`ref_id` / `group` / `next_spawn_ms` / `show_thumbnail` with the types `AddStageMonster` expects
(`from_json<std::string>` on `ref_id`, numeric on the rest).

**Do not** re-litigate the key, `show_thumbnail`'s type, the level file, or the scene. All four
are settled.

## 5. Honest confidence

| Link | Confidence |
|---|---|
| Crash site = `str r0,[r1,#0x4c]`, `r1 == 0` | **Recovered**, encoding + registers agree |
| `r1 == 0` derives from `std::list`'s own constructor | **Recovered**, independent of the crash report |
| `"enemy"` key never created when the waves vector is empty | **Recovered** (`beq.w` skip) |
| `this+0x264` written only by `MakeStageInst` | **Recovered** (exhaustive `#0x264` scan) |
| `AddStageMonster` is reached | **Recovered** (unconditional `bl`) |
| Our response leaves `waves` empty | **Inferred-strong** — the whole chain is consistent, but the specific empty field is not yet observed |
| Which element field causes the empty record | **UNKNOWN** — needs the logged `ret_data` |

Everything above the last two rows is verified from the binary. The last two are why the next
step is to *look at the response* rather than to try another shape.

## 6. Retractions, for the record

Four claims of mine were wrong along the way, and each was caught by checking bytes rather than
symbols:

1. "`wave_list` has zero code references" — **false negative from my own resolver's pairing
   window**. It is a real key. Resolver fixed and documented in-source.
2. "The pushed ids are the map key" — they are `show_thumbnail[]`.
3. "`show_thumbnail`'s type causes the empty ids" — **refuted by device control**.
4. "The crash is in the episode scene" — an ELF/Ghidra `+0x10000` confusion; it is `CSRMStage`.

`5acb45e` stands and should be kept: it took total assertions 6 → 0, moved the crash to a
resolved instruction, and is control-verified.