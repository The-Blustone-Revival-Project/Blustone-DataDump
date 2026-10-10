# QEMU API-30 mission blocker evidence

Capture date: 2026-09-19  
Target: official Android Emulator API-30 Google APIs x86_64 AVD, serial
`emulator-5564`, ARM native bridge enabled, `adbd` running as root.

## Reproduced path

1. The original ARMv7 APK reaches guest login, story, Airport, Expedition Area,
   and the Snowfield node.
2. The Airport flow reaches the flight animation and then starts mission-map
   initialization.
3. The native client logs these missing records immediately before the failure:

   - `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/1_MS_ST_MAP`
   - `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/6_UPDOWNBTN`
   - `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/5_MS_ST_GL`

4. The native trace then reports `CSRTutorialMStageMap::OnInit` followed by the
   assertion path in `__bGlobalAssert`; no native `/mission/Start` request is
   emitted before this point.

Evidence screenshots: `qemu-api30-airport-tutorial10.png`,
`qemu-api30-snowfield-after-flight.png`.

## Database experiments

- The preserved `UI_XML_RO.db` contains all three records under the `KO/NEW/...`
  prefix but not under `EN/NEW/...`.
- A full KO-to-EN rebuild added 569 aliases but caused an earlier
  `BuildColorTable` assertion, so it is not a safe client patch.
- A selective copy preserving the original SSTables and adding only the three
  mission aliases avoided that assertion but did not complete client startup in
  the clean replay. It remains an offline experiment, not the active emulator
  database.
- The emulator was restored to the original database after testing.

The reusable selective helper is
`tools/patch-ui-leveldb-selective.py`; it never edits the source directory and
does not compact by default.

## Server status

The replica serves the observed launcher, encrypted reference, lobby, and
WebView routes. The stateful `/mission/Start` and `/mission/Complete` seams are
implemented and documented, but the native client has not yet reached them in
this capture. Swagger explicitly records that limitation.
