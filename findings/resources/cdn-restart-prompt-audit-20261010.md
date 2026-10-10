# Repeated restart download prompt: source audit (2026-10-10)

Read-only source/evidence audit for root. Only this note written; no ADB, UI, Ghidra, Docker, original assets, runtime/profile/account or source edits. The supplied live condition is same +12 APK, 139 groups, resource/package stamp 1634683, header stamp 1634682. Live installed flags, cache contents and actual transferred bytes were not inspected by this agent.

## Findings supported by source

`Telemetry.install` (instrumentation/src/Telemetry.java:190..203) calls three restoration functions once per Java process:

- `restoreBundledJets` returns when local/UI_MAIN.jet exists. It is a missing-file seed, not an unconditional overwrite.
- `restoreSeededUiXml` unconditionally clears **only local/UI_XML_RO.db**, preserves its first backup, and copies `instrumented-seed-episode-ui-delta-v1/UI_XML_RO.db` before native LevelDB opens (lines 665..674). Therefore every new process returns this database to the APK's seed, irrespective of last session's download. This is an actual repeated overwrite in source.
- `restorePreRepairCdn` immediately returns when `BuildConfig.RESTORE_PRE_REPAIR_CDN` is false (lines740..743). Only when true does it overwrite CDN.db from the pre-repair snapshot or call `repairSeededCdn` when the backup is absent. The latter clean-rebuild is not independently called by install. Build script flag `--restore-pre-repair-cdn` is opt-in/default false; generated BuildConfig emits that explicit boolean (tools/build-instrumented-apk.py:108..116,203). Installed +12 must still be verified against its built artifact before ruling it out.

The source comment about an older every-launch CDN snapshot describes historical behavior; it does **not** prove current unconditional CDN.db repair. UI_XML overwrite remains separate.

`server-ts/src/server.ts:475..479` emits manifest first line from HEADER_STAMP, count, total outer payload size, then per-item name/stamp/size/step/sign/md5. `resourcePackages` uses RESLIST_STAMP for every package row (line230); native sign is MD5 of inner JET, md5 of outer payload. Both matter and are distinct. `state.ts:2246..2247` advertises res_ver/new_res_ver from RESOURCE_VERSION. Thus current supplied profile intentionally or accidentally exposes distinct header and resource/item stamps. The route accepts any numeric `/reslist_<n>.list` and returns the same current body, not a version-selected file. Runtime sequence/override/first-request bootstrap header can supersede generated manifest; inspect effective body rather than infer it from environment.

`analysis/native-cdn-callers-new.txt`, PrepareDiff G7ccd80, has actual per-item checks: requested step, cached package file existence, outer file size and optional Signing comparison; when package file is missing it consults GetPVCInfo, compares an item scalar to a PVC scalar and iterates cached unpacked-pack metadata. The exact key literals at these sites remain unresolved DAT operands in this dump. They must be recovered before labeling each scalar stamp or size. This is enough to reject the assumption that an old **root header stamp alone** demonstrates a full-package redownload. The native diff also examines package/unpacked state.

ParseHeader G7d22ec consumes newline-delimited header, strips CR. Existing curated evidence documents CDN/header plus CDN/PVC keys, and plaintext little-endian cnt/step versus encrypted/string-like stamp/sign/size values (`analysis/2026-10-02-cdn-stall-findings.md:80..117`). That document's 11-group state and stall conclusion are historical; not current 139-group proof.

## Causal candidates, not conclusions

1. **Root header version mismatch** may cause repeated reslist checks or resource-update prompt selection. Need DownloadHeader/current-header comparison and caller prompt selection to prove. A repeated 203 MB label may be manifest total even when actual transfer is smaller or zero.
2. **Every-process UI_XML seed overwrite** may invalidate one cached unpacked output's size/sign or restore old launch/progress records. It directly affects UI_XML content, not automatically all 139 packages. Prove membership and diff reason; do not infer whole-corpus invalidation from this write.
3. **Installed RESTORE_PRE_REPAIR_CDN true** would directly reset native accumulated cache metadata. Source default is false, so check installed/built +12 evidence first. Do not rebuild only to inspect a constant.
4. **Native cache persistence or unpack-completion failure**, missing/changed output filenames or signature/size mismatch, may cause repeated full or partial work. Successful Village entry alone does not prove every PVC update persisted.
5. **Different effective reslist per request** (debug sequence, first-request bootstrap, env drift or different material payload) can change diff unexpectedly. Root must record effective manifest and request sequence alongside private cache evidence.

## Exact safe verification plan for root

1. While freshly verified Village/no helper/battle, preserve current restoration profile and private state; inventory currently running listener/client. Do not clear/reinstall/cache-reseed.
2. Save effective reslist body and hash, VERSION/base-info resource fields, manifest count, row stamp and byte total. Record whether header override/sequence/bootstrap is active. No auth material in public evidence.
3. Check +12 packaged/generated BuildConfig or existing release build metadata for RESTORE_PRE_REPAIR_CDN, and process-start local logs for `cdn_repair` versus `ui_xml_repair`. This distinguishes overwrite lanes. Avoid collector/Docker; root can use bounded existing local artifacts/logs.
4. Before restart, capture private CDN.db metadata and relevant local output existence/length/signature, keeping copied evidence under recovered-assets. If live DB is open, treat a raw multi-file copy as non-atomic; prefer native read-only getters already demonstrated safe or a settled stopped-client snapshot. Do not decode/export USER/account fields. Capture UI_XML directory hashes separately.
5. Root-only native exports: DownloadHeader G7d2f9c and its callback, CSRPatchSystem::DownloadHeader Gb5fe6c plus literal resolver; PrepareDiff G7ccd80 key sites; GetPVCInfo exact symbol; unpack callback persistence; prompt caller that computes displayed download size. Close key/lifecycle branch before changing header policy.
6. Run one controlled same-profile restart, observe prompt, accept normally only after preserving evidence, measure actual package requests/count/Range/content bytes and completion; compare cache keys/metadata and UI_XML pre/post. A 203MB prompt screenshot alone proves only its display.
7. If root tests HEADER_STAMP=1634683, change that single profile field without bumping item stamps or altering material bytes. Preserve old profile as control, check effective body and full save equality. Only call fixed when repeated same-profile restart no longer requests unnecessary package data and native bootstrap still reaches Village.
8. If repair requires changing Java seed behavior, preserve original seed constraints, avoid removing startup UI blindly, and build a new side-by-side instrumented version **with mandatory GitHub release**. No client patch is proposed by this audit until attribution proves necessity.

No source/server/profile change is justified solely by this audit. Strongest newly isolated source fact is unconditional UI_XML reseeding versus conditional CDN reseeding; header mismatch remains independently testable.

## Root counter-test and revised attribution (2026-10-10)

Inspected `analysis/testing/cdn-header-001/counter-test.json` and `apk-identity.json` after root supplied its live results. The control changed only private profile HEADER_STAMP1634682→1634683; manifest rows1..end were identical. Root reports new wrapper/listener50232/25392 and fresh client8932, then9308. Both controlled restarts still displayed203MB, issued139 distinct package GET responses, all status206, and reached Village. Thus **header alignment alone is disproven as the prompt/repeated-request fix**. Exact transferred byte volume was not measured: endpoint count/status206 is stronger evidence than prompt text but does not prove203MB payload transfer, full-body ranges or successful persistence of every output. Root kept the aligned header as consistent with the requested version, not as a claimed fix.

Installed and local+12 APK SHA256 are equal, `b6189295b23f547d02514fbeeed7576aeeb1df5d0ae9120adc747aa1bbda0016`; matching host build metadata says RESTORE_PRE_REPAIR_CDN=false. This closes the conditional CDN reseeding candidate for this installed artifact. It does not remove the independent unconditional UI_XML reseed.

Root attempted private cache-copy access: run-as printed a capabilities error despite exit0; emulator su/tar returned empty. Neither yielded a CDN clone. Do not interpret exit0/empty output as successful acquisition, compare nonexistent cache snapshots or infer cache contents. No original-phone access, original/cache modifications or collector/Docker work occurred.

Native Signing export `analysis/ghidra-cdn-signing.txt` G7cbbc0 instantiates CryptoPP Weak1 MD5 and feeds its digest into CMToHex; `analysis/ghidra-cdn-tohex.txt` G78e46c constructs HexEncoder with uppercase=true. The current server already emits uppercase MD5 for inner sign and outer package md5, with matching tests reported by root. **A lowercase/uppercase MD5 server mismatch is not supported.** Decompiled call prototypes are incomplete; use the established digest/encoder flow rather than invent missing register arguments.

Root's new literal evidence distinguishes GetResVer's `header/stamp` from DownloadHeader's `header\\stamp`. Whether the packed-DB key path layer normalizes separators is still unclosed. A textual literal difference alone is **not** proof of two distinct keys or a defect; trace that normalization/call path before patching.

Root receipt audit shows unchanged gold12800/teamEXP1500 and earned progression; main changed fields only ap/ap_updated_at/bp_updated_at with natural AP46→50. Other two gameStates exactly unchanged; no active battle.

The next causal evidence should prioritize why all139 rows remain in native PrepareDiff after a successful prior Village bootstrap: exact key normalization, current-header read/write/persistence, PVC metadata production/completion and per-output signature checks. Keep UI_XML reseed as a separate candidate; it cannot explain all139 invalidations without a proved shared gate. No fix is claimed and no Java/native patch is proposed by this audit.
