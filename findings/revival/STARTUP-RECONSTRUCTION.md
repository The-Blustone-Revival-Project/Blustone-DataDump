# Startup reconstruction checkpoint

## Verified, 2026-09-19

**Village screen reached and interactive on 2026-09-19.** Evidence: `capture/lana-skip2.png` (village), `capture/airport-main.png` (expedition map). Dialogue, artwork and choices work; airport opens. Expedition map is empty and village progress denominator is invalid because stage/area references remain placeholders. Combat, progression and full functionality remain unverified.

- Nonempty `ret_data.otp` is required by `CPVDataMgr::ParseLoginResult` before it assigns `server_url`. Missing OTP produced `http:///reference/...` and curl 6. Local login now unlocks encrypted reference/lobby requests.
- `GetCardInven` consumes an array directly. Metadata objects created blank card IDs and the `Cannot find Ref Data` assertion.
- `GetCard` consumes an array of `{base,stat,equipment,skill,dialog}`. Current starter fixture is provisional, not recovered balance data.
- `BlockList` consumes an array (`target_pvid`, `target_nickname`). Metadata produced a native callback exception.
- `GetStage` consumes an array indexed numerically. Its metadata-object exception disappeared after returning `[]`. Empty stages are not playable stages.
- Manifest sixth column is MD5 of the entire downloaded package. Tests cover HTTP bytes, header, directory record and range responses. Native unpack completion is NOT yet established.
- With stage fixed the process still exits (191). An empty-inventory diagnostic also exits after retry; it does not isolate the starter as the sole cause. Crashpad itself fails loading its handler and obscures the original crash.

## APK diagnostics

- Known working base: `patched/blustone-local-replica-debug-copy-signed.apk`.
- Do NOT install a full rebuild of `patched/debug-smali`: its native library differs from the working base and caused `Cannot Load Default Fonts`.
- `tools/assemble-logging-apk.py` preserves the known working archive and replaces only `classes.dex` from the rebuilt logging source; it asserts no other entry CRC changes.
- MainActivity's diagnostic `dispatchTouchEvent` calls existing `JNISetDebugLevel(0)` before forwarding the event. Confirmed FULL logs without JDWP.
- Diagnostic `CrashlyticsNdkRegistrar.getComponents` returns an empty list to let Android report native faults; no gameplay/assertion logic is bypassed.
- Latest diagnostic APK: `patched/blustone-local-native-debug.apk`, installed on BlueStacks. Normal fonts/login verified before the crash-reporter change; next run tests native stack reporting.
- Sign with `patched/debug.keystore`, alias androiddebugkey, standard local debug password android. This is not a production signing key.
- BlueStacks shared folder: host `C:/ProgramData/BlueStacks_nxt/Engine/UserData/SharedFolder`, guest `/mnt/windows/BstSharedFolder`. Copy APK there, then `adb -s 127.0.0.1:5555 shell pm install -r /mnt/windows/BstSharedFolder/<name>.apk`. Avoid slow/hanging streaming installs.
- JDWP sometimes freezes app/ADB. Emulator-only disconnect/reconnect recovers it. Logging hook avoids repeated debugger attaches.

## Phone preservation and reference data

- User permits phone inspection but no longer requests advisor assistance. Use preserved data before any live private-access procedure.
- Verified recovery already exists under `recovered-assets/phone-2026-09-18`; see its README. Private archive includes sensitive account/cache data and must remain local.
- `tools/export-recovered-reference.py` reads eight allowlisted reference databases from the preserved copy, refuses nonempty WALs/multiple tables, and exports 3,573 records into `analysis/recovered-reference` with source/export hashes.
- These records include localized character text, skill formulas/effects, and episode text. They are NOT recovered HTTP response bodies. Account databases are excluded.
- Physical phone serial `RR8M60E30GW`; emulator `127.0.0.1:5555`. Always select explicitly. Never clear/reinstall the phone app.

## Remaining work

- Disabling Crashlytics NDK registration successfully exposed SIGSEGV in libhoudini. Spacing generic response dispatches 500ms apart consistently narrowed the fault to after `/episode/GetLog` and before `/achievement/GetInstList`, long after CDN downloads.
- Episode log now returns `{read_log: [], reward_log: []}` based on `CSRMEpisode::ParseLog`.
- `/lobby/Enter` now supplies a provisional returning-player user/battle profile and `tuto:[{type:0,step:5,is_cleared:1}]`; Parse maps this to native state 3. Intended to avoid unchecked `TUTORIAL` lookup, but it did NOT eliminate the crash. Starter inventory restored for this run.
- Official NDK r29 installed through SDK Manager at `tools/android-sdk/ndk/29.0.14206865`. `tools/arm-crash-probe.c` builds `patched/libblustone_trace.so` with armv7a-linux-androideabi21-clang.cmd, `-shared -fPIC -g -O0 -llog -ldl`.
- `assemble-logging-apk.py --probe` adds that diagnostic library and new dex while preserving all original game native/assets. MainActivity loads it and installs ARM signal handler on first tap. Probe APK being tested: `patched/blustone-local-probe.apk`. Look for tag `BLUSTONE_ARM`.
- Temporary diagnostics: `BLUSTONE_DIAGNOSTIC_EMPTY_INVENTORY=1` removes starter; default restores it. `BLUSTONE_DIAGNOSTIC_RESPONSE_SPACING_MS=500` queues generic responses with timestamped `response-dispatch` logs. Neither is proof of functionality.
- ARM probe WORKS under Houdini. First identified `CSRRefData::FindCardBook` offset `0xdd491b`. Fixed GetCardBook reference with role-keyed rows and JSON-string `effect`, plus owned `{ref_id,rank}` array. Next fault moved to `CSRSupply::CalcVipBonusAP` (missing VIP record). Supplying named `GetLevel` arrays cleared that fault; current next fault is SIGFPE in libc raise. Probe stack-candidate scan was added to recover its caller, pending runtime test.
- Current canonical bootstrap fields are in `server-ts/src/bootstrap.ts`, persistent local game state is in `server-ts/src/game.ts`/`state.ts`, and explicit handlers are near `genericResponse` in server.ts. Village, opening dialogue/choices and airport navigation have been verified. The server now exposes persistent inventory/mission/gem/session contracts and deterministic mission start/complete actions; combat simulation remains incomplete.
- Later update: stack candidates located the arithmetic fault in `CSRPlayData::CalcTotalBP` called by `CSRPopUpVillage::OnRefresh`. `GetExtra` now supplies max_ap 50, max_bp 10, ap_refresh_interval 300, bp_refresh_interval 1800. This cleared the fault and exposed functioning opening dialogue and village. GetExtra documentation/test additions still pending at this checkpoint.
- Enhanced probe must NOT use dl_iterate_phdr: that bridge crashed on first tap in Houdini. Current source uses dlopen/dlsym/dladdr (verified) and scans current stack page for candidate game addresses. These are candidates, not a true backtrace. Current `blustone-local-probe.apk` is installed and working.
- Current emulator state: Expedition Area screen with no destinations (`capture/airport-main.png`), tutorial hand points to an absent destination. Next: reconstruct `CSRGameStage::SetArea`, stage links, first playable stage. Do not clear the app casually now that the village is reachable; first support server state persistence/hot configuration or preserve live-session keys before restart if possible.

Recover the first native fault; reconstruct reference/session dependency contracts; restore real inventory after the diagnostic; reach and exercise actual gameplay. Most of the 285 routes still return placeholders. Swagger explicitly marks the reconstructed array contracts and their limits. Do not claim 100% functionality.
