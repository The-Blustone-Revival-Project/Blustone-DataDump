# Blustone APK analysis

Initial offline analysis of `BLUSTONE_2.8.0.1_APKPure.apk` performed on 2026-09-17.

## APK identity

- Package: `com.vshower.prd_sr`
- Version: `2.8.0.1` / version code `28010`
- Minimum SDK: 20
- Target SDK: 33
- Native ABI: `armeabi-v7a` only, loaded from `libnative_core.so`
- Signing certificate subject: `CN=Justin Hwang, OU=COSMOS, O=VisualShower Crop.`
- The manifest allows cleartext traffic and declares Internet, Firebase messaging, Google sign-in/auth, billing, storage, wake-lock, and boot permissions.

## Initial server shape

The Java wrapper is small. The native engine owns the server protocol and exposes retained C++ symbols.

1. Launcher/base-info service
   - `/launcher/GetBaseInfo`
   - Base information contains `pv_url`, `country_code`, `url_list`, `client_option`, `app_srv_list`, `app_srv_name_list`, `state`, and `recommend_server`.
   - URL records contain `url_key`, `address`, and `param_format`.
   - Other launcher-related paths include `/VERSION`, `/AUTHORIZATION_REQUEST`, and `/selected_server`.

2. Account/auth service
   - `/v2/account/RegisterGuest`
   - `/v2/account/Login`
   - `/v2/account/BindSNS`, `/account/Unbind`, `/account/Unregister`, `/account/ConfirmNickname`
   - `/pv_account/get_token` and `/pv_account/register_push_token`
   - Login results carry fields including `server_url`, `web_token`, `new_res_ver`, `profile_status`, and account data.

3. HTTP security layer
   - Shared-key exchange: `/shared_secret/Exchange`
   - Native code contains `CPVHTTPSharedSecret`, ECDH key agreement, HMAC-SHA384, Base64 encoding, and encrypted/decrypted response handling.
   - Relevant headers/constants include `X-PV-AccessToken`, `PV-AccessToken`, `PV-Signature`, and `x-pv2-secure-v3`/`x-pv2-secure-v2`/`x-pv2-secure-v1`.

4. Game API service
   - JSON/form HTTP requests cover lobby, reference data, account state, cards, items, stages, missions, gacha, shop, guilds, GvG, arena, fishing, episodes, mail, social, and rewards.
   - The complete string-derived endpoint inventory is in `native-all-strings.tsv`; representative examples are `/lobby/Enter`, `/lobby/GetCardInven`, `/reference/GetStage`, `/mission/Start`, `/shop/BuyItem`, `/gvg/CombatBegin`, and `/arena/BattleComplete`.

5. CDN/resource service
   - Native `CPVCDN2` code manages resource versions, headers/stamps, reslists, package files, checksums, and staged downloads.
   - The APK already bundles LevelDB stores such as `UI_JSON.db`, `UI_TEXT.db`, `UI_XML.db`, skills, episodes, and static text, plus many `.jet` asset packages. A replica still needs to answer resource/version checks consistently.

6. WebSocket/chat service
   - The native library includes `easywsclient`, `CPVWebSocketClient`, and chat payload/message types.
   - WebSocket URL parsing expects `ws://host[:port]/path`.

## Analysis artifacts

- `jadx/` — JADX Java/resource output.
- `extracted/` — selected APK contents, including native code and bundled assets.
- `ghidra-project/` — Ghidra project for the ARM native library.
- `native-evidence.tsv` — retained native function names and filtered printable strings.
- `native-all-strings.tsv` — all printable native strings, including the full endpoint vocabulary.
- `native-decomp.txt` — focused decompilation of server, launcher, and shared-secret functions.
- `native-network-decomp.txt` — focused decompilation of launcher/auth/request functions.
- `native-pointer-resolve.txt` — resolved native pointer-table values used while mapping launcher constants.

## Compatibility scaffold

`server/` contains a dependency-free local HTTP scaffold generated from the endpoint evidence. It implements launcher/base-info and guest-auth flows, exposes the discovered route catalog as mock handlers, and leaves native ECDH/HMAC body protection explicitly marked as a placeholder until an ARM-device capture confirms the wire format. Run it with `python -m server.app` and test it with `python -m unittest discover -s server/tests -v`.

`server-ts/` is the canonical TypeScript/Express implementation. It serves heavily documented Swagger UI at `/docs`, OpenAPI JSON at `/openapi.json`, and OpenAPI YAML at `/openapi.yaml`. Use `npm install`, `npm run openapi:export`, and `npm run dev` from that directory.

The first locally redirected launcher request confirmed one wire-level semantic: the JSON `result_code` value `1` is the native success value (`CPVDataMgr::ParseLauncherResp`), while `0` is not accepted as launcher success. The TypeScript envelope and generated OpenAPI contract use `1`.

Native `ParseAppServerList` also parses `app_srv_name_list` entries as `{srv_id, lang, name, desc}` objects; the TypeScript response now emits that array shape.

The first captured launcher form identified `app_code=_SR`; `ReqLaunchResCB` asserted `PV_LAUNCHER_INVALID_APP_REFERENCE` until the response advertised a matching `_SR` URL record.

## Runtime limitation

The host is x86_64. Android Studio 2026.1.4.7 and the official SDK emulator are installed, but both Google API and Google Play x86_64 images rejected the APK because it has no matching ABI; the ARM64 image cannot run on this x86_64 host. The official BlueStacks 5.22.166.1003 fallback was therefore installed with its Nougat32 image. It reports `x86,armeabi-v7a,armeabi`, installed `com.vshower.prd_sr`, and launched `com.vshower.sr.MainActivity` successfully.

The runtime evidence is in `capture/blustone-player-evidence.log` and `capture/blustone-peer-snapshot.json`. The peer snapshot is process-level BlueStacks traffic and is not an app-specific HTTP attribution. BlueStacks' legacy ADB bridge closed file-sync, shell, and logcat commands, and Windows `pktmon` required elevation, so decrypted HTTP bodies were not captured in this pass.
