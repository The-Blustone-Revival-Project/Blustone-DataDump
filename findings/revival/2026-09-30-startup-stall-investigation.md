# 2026-09-30 session — startup stall investigation

## Environment restored

The workspace was dormant: the Docker collector and `server-ts` were both
stopped and no adb device was attached. Restored in this order:

```powershell
docker compose -f instrumentation/docker-compose.yml up -d          # collector :8099
. .\tools\stop-server.ps1 ; . .\tools\start-server.ps1               # replica   :8080
Start-Process "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Nougat32
adb connect 127.0.0.1:5555
adb -s 127.0.0.1:5555 shell am start -n com.vshower.prd_sr.instrumented/com.vshower.instrumented.InstrumentedActivity
```

`tools/start-server.ps1` and `tools/stop-server.ps1` are new. See
"Server process management" below for why the second one exists.

## Client-side fix: the telemetry stream was unusable

**Symptom.** Every session's event ring was 100% `RANN [RSM]` lines. Grouping
the last 2000 events by tag gave 1997/2000 `RANN`. No `BLUSTONE_*` line, no
native assertion, no LevelDB lookup survived — the diagnostic channel the whole
project depends on was blind.

**Cause.** The engine logs its resource manager at `*:V`, emitting
`[RSM] 'BATCHDRAW<n>'(0x...), type:18 is registered.` plus a matching
`Removing Res:` line ~17 ms apart while a loading animation plays. A title
screen alone produces thousands per minute. The collector's ring is bounded, so
the useful lines were evicted before anyone could read them.

**Fix** (`instrumentation/src/Telemetry.java`, released as `2.8.0.1+2`):

- drop `RANN    : [RSM]` lines at the source, before they are queued;
- repeat-suppress the remainder on a shape of `tag + first 4 message words`
  with digits collapsed, keeping the first 5 of each shape;
- emit periodic `android_log_filtered` events reporting `dropped_noise` /
  `dropped_repeat`, so the filter is never silently hiding evidence.

After the fix the same session yields the engine's real startup log:

```text
[FWK] RMGLSurfaceView has been created.
[JUC] [SetMarket] MarketType: 1
[FWK] Activity _onCreate ==============================
[FWK] RMUtilities/RMNetwork/RMFileSystem/RMModalDialog/RMSensor/RMEditBox/RMWebView has been created.
[FWK] [FS] Using internal storage. Path: /data/user/0/com.vshower.prd_sr.instrumented/files/local/
[FWK] Activity _onCreate finished 0.016s ===================
[FWK] OpenGL surface has been changed. (1080x1920)
[FWK] Debug Log Level: RMDBG_NONE
[ERR] [ADS] Ad loading was failure. http://10.0.2.2:8080/maintenance-replica-online { ... }
[FWK] MainThread has been created. / MainThread entered the loop.
```

Also confirmed and worth remembering: a single tap on the game window makes the
preserved `MainActivity` raise the engine to `RMDBG_LOG(FULL)`. Without a tap
the engine's own log level is `RMDBG_NONE`.

## The current blocker: startup stalls before login

The client is fully provisioned on the device — all 11 JET packages, all
reference LevelDB stores, and `cloud/v2pv.acct` with a guest `vs_token` are
present — but every launch stops on the title/loading screen at exactly this
point:

```text
POST /launcher/GetBaseInfo      -> 200
POST /shared_secret/Exchange    -> 200
GET  /reslist_1634661.list      -> 200
<nothing, indefinitely>
```

`/v2/account/RegisterGuest` or `/v2/account/Login` is never issued, and no
package is ever requested. In the last good run on 2026-09-21 the gap between
`reslist` and `RegisterGuest` was 23–40 s; here it is >8 min and the client
never gets there.

### What was ruled out

| Hypothesis | Test | Result |
|---|---|---|
| Manifest content is wrong | Forced a fresh stamp `1634662`; client re-requested `reslist_1634662.list` | no download attempt, still stalls — the stamp value is not the trigger |
| Manifest package list is wrong | `POST /debug/reslist` with a 0-package manifest (`1634662 / 0 / 0`) | still stalls — package count is not the trigger |
| Auto-login path is the blocker | `BLUSTONE_AUTO_LOGIN=0` to force the manual title/login UI | still stalls — never reaches the login decision |
| Launcher blocks on a WebView load of `pv_url` | `BLUSTONE_PV_URL=''` | still stalls |
| Ad unit URL is the blocker | `ad_unit_id_1` / `d_unit_id_1` now point at the 204 routes instead of the HTML handoff page | still stalls (kept anyway; it is more correct) |

### What is known about the client state

- Main thread is `S` (sleeping), not spinning; 95 threads exist.
- Sockets: one `CLOSE_WAIT` to `10.0.2.2:8080` and one `ESTABLISHED` to
  `127.0.0.1:37443` (the BlueStacks Google Ads service). **No pending outbound
  connection** — the client is not waiting on a reply from the replica.
- `dumpsys window windows` shows only the activity and its SurfaceView. No
  modal, no WebView window.
- The game is still rendering (the `[RSM]` stream continues); it is alive and
  idle, not crashed and not blocked on I/O.
- The engine's own CDN log lines (`download reslist(%s) from server`,
  `DownloadHeader`, `did you try to download?`, `Success that PatchList is
  download.`) **never appear at all**, even at `RMDBG_LOG(FULL)`. So the engine
  is not reaching the `CPVCDN2` body that would log them, despite having
  fetched the reslist.

### Where this points

The stall is inside `CPVCDN2` between `DownloadHeader` (the reslist fetch, which
succeeds) and `DownloadItem`/`UnpackAll`, and it happens with an empty package
list, which rules out the manifest and the download path. The most likely
remaining causes, in the order I would test them next:

1. **A post-reslist request the replica does not serve.** The native strings
   include a `header_cb` libcurl header callback and a separate
   `CSRPatchSystem`, and `DownloadHeader` may be a header-only probe whose
   *response* is required before the client proceeds. If the client issues it to
   a URL the replica does not route, the request may be retried without ever
   being logged. Worth logging every non-2xx and every unmatched path.
2. **`IsUnpacked` / local stamp mismatch.** `PV_CDN_FILE_ALREADY_UNPACKED` and
   the `IsUnpacked` PKGI error family suggest the client validates each local
   `.jet` against the manifest before deciding. A malformed or mismatched local
   JET could hang here. The next client-side lever is a native hook that logs
   the `CPVCDN2` return codes instead of guessing from the network side.
3. **The 2026-09-21 `/mission/Start` left client-side state that blocks
   bootstrap.** The last successful session ended with `/mission/Start` at
   09:12:51, and every launch after that stalls at the same point. A
   mission-resume check on startup is consistent with a stall that is
   independent of everything the server does. Clearing only the client's
   `USER.db` (keeping the CDN index and the UI seed) is the cheapest test.

## Server changes made this session

Both are behaviour-preserving for the paths that already worked and are
covered by `npm test` (285 routes):

- `state.ts` — `ad_unit_id_1` and `d_unit_id_1` now resolve to the bodyless
  204 routes rather than the HTML handoff page. The launcher hands
  `ad_unit_id_1` to the Google Ads SDK as an ad unit, and serving it an HTML
  document makes the SDK fail with `Error building request URL`. The
  human-readable handoff page stays reachable under its own `maintenance` key.
- `state.ts` — `pv_url` is overridable via `BLUSTONE_PV_URL` (default
  unchanged).

## Server process management

`npm run dev` spawns npm → node → tsx → node, so the PID written to
`server-ts/logs/server.pid` is only the npm wrapper. Killing it leaves an
orphaned grandchild still listening on 8080 and still serving the **old**
configuration. This cost real debugging time: a resource-version bump appeared
to have no effect because the old process was answering.

`tools/stop-server.ps1` kills the actual port owner, and `tools/start-server.ps1`
now refuses to start if 8080 is already held. `start-server.ps1` also no longer
clobbers env vars you set before dot-sourcing it, which is what makes
`BLUSTONE_RESOURCE_VERSION` usable as an A/B dial.

## Not achieved

The expedition/mission-map blocker is unchanged. The client does not currently
reach `/lobby/Enter` on this machine, so no new evidence about
`CSRGameStage::SetArea`, the stage/area link tables, or the missing
`EN/NEW/SR_MISSION/...` UI records was obtained. The concrete gain is that the
instrumentation channel works again, so that work is no longer blocked on
blindness.
