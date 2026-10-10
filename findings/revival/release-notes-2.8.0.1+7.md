Adds a bounded read-only native Gym observer to the side-by-side instrumented package. It reports scene class, selected target, candidate IDs and selected source IDs through local `native_gym_state` telemetry, sampled on the background heartbeat when the snapshot changes.

The observer checks package/version, exact native application/manager/scene vtables, readable mappings, vector bounds and repeated ownership/header/content consistency. It reads this process only and does not suspend the debugger, invoke native functions or write game memory. Double-reading does not make a snapshot atomic; changes or unsupported scenes are reported as unavailable/unsupported.

Build verification passed Java/D8 compilation, existing native patch checks and APK signature verification. Runtime observer passed on ordinary Raise: target5, expected candidate IDs and empty selection, with responsive Back navigation after sampling. Interrupted tutorial resume remains pending. Existing local routing, resource seeds and assertion logging profile are preserved. Game statistics, rewards and several server systems remain local fixtures or incomplete.

Also fixes Windows packaging of LevelDB `CURRENT`: manifest filenames are validated and written with exactly one LF. Git attributes prevent CRLF conversion of the copied seed files. All18 packaged CURRENT/manifest pairs passed byte-level verification. The initial candidate's UI_XML load assertion exposed this packaging defect; that candidate was held in draft and replaced.

Android package: `com.vshower.prd_sr.instrumented`, base version/code `2.8.0.1` / `28010`. Local replica and collector are required. Replacing the instrumented package preserves its data; the original package is separate.
