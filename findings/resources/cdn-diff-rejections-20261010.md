# CDN PrepareDiff rejection audit — 2026-10-10

Read-only source audit. No client, server, profile, account or device mutation was performed. Root owns live validation and Ghidra. This closes the meanings of the per-item checks; it does not identify which check failed on either current 139-package restart.

## Evidence and scope

`analysis/native-cdn-callers-new.txt`, PrepareDiff G `007ccd80` (lines 1–720), supplies control flow. `analysis/ghidra-cdn-version-persistence-strings.txt` supplies relocated literals for that exact function. Historical disk-key names come from `analysis/2026-10-02-cdn-stall-findings.md`; its 11-package snapshot and stall conclusion are not current runtime evidence. Function targets below use Ghidra addresses, not ELF offsets (ELF = G − `0x10000`).

The controlled matched-header restarts still requested all 139 package endpoints. Those requests do not establish response byte counts, outer-file deletion, PVC absence, MD5 mismatch, or output-size mismatch. Matching uppercase server MD5 is useful static evidence, but does not prove which bytes the native reader opened.

## Exact decision chain

1. Read current header `items` from the cached header JSON at `**(this+0x34)+0x18`. Consider only rows whose numeric `step` equals the requested step. A step mismatch skips the row rather than requesting it.
2. Read row `pkg`; call `RMFileExist(2, pkg)`. Missing outer package proceeds to PVC fallback, not directly to enqueue.
3. For an existing outer package, call `RMGetFileSize(2, pkg)` and compare the full 64-bit size to row `size`. A mismatch reaches G `007cd148`, emits the invalid-file trace, deletes that outer path with `RMFileDelete(2, pkg)`, then proceeds to PVC fallback.
4. If sizes match and row has `md5`, load the complete outer package with `CMLoadBufferFromFile(pkg, 2)`, compute `Signing`, and compare the resulting string to row `md5`. Comparison is exact length and bytes, with no case normalization. Equality sets the enqueue flag false and jumps directly to G `007cd2d0`: **it does not consult PVC or unpacked output files**. Inequality deletes the outer package and falls through PVC fallback. This fallback can still avoid a request.
5. If sizes match but row lacks `md5`, an alternate legacy check opens the package with `RMFileOpen(..., IO=0, DIR=0)` and reads its first eight bytes. Open failure sets enqueue true. Otherwise compare those bytes to row `stamp`: unequal sets enqueue true, equal false. This alternate branch bypasses PVC. The numeric DIR `0` here differs from DIR `2` in the existence/size/hash checks; directory semantics need their own proof. Current generated rows carrying `md5` should not take this branch, but that must be confirmed on the parsed native row.
6. PVC fallback at G `007cd1bc` reads row `name`, invokes `GetPVCInfo(name)`, and rejects a null JSON result. A non-null PVC result has its `stamp` compared numerically to row `stamp`; unequal stamps enqueue.
7. Equal PVC stamps lead to traversal of PVC `packs`. For each entry, read `filename` and `size`, then compare `RMGetFileSize(2, filename)` to the stored 64-bit size. The first mismatch emits the real/expected-size trace and enqueues. If all entries match, enqueue false. **No `sign` or content hash is checked in this fallback.** An empty iterable has no failing size check and therefore passes this loop; this is source behavior, not a recommendation to seed empty metadata.
8. Only enqueue true at G `007cd2d0` causes the row to be copied into the returned download vector.

The important causal distinction is that outer package absence/deletion alone is insufficient to explain repeat requests. The PVC fallback must also fail. Conversely, a valid cached outer package with exact MD5 suppresses download even when unpacked metadata is missing.

## Reader, producer and persistence targets

- `GetPVCInfo`: G `007ceeb4`, exact symbol `_ZN7CPVCDN210GetPVCInfoERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE`. This is the first export to close the PVC namespace construction, database instance, returned JSON and normalization.
- `Init`: G `007cb964`. Close resource database open path/mode and its adapter; distinguish the in-memory header holder from durable database contents.
- `UnpackAsynTask`: G `007d121c`. It loads the outer package from DIR `2`, conditionally verifies `md5`, calls `UnPacking`, and queues a main-thread task carrying the unpacked JSON and manifest row. The producer's body does **not** prove that the queued callback wrote PVC successfully. Resolve the callback registered near G `007d1862` and the completion chain, rather than assigning persistence to this parent solely from its name.
- `UnPacking`: G `007cfcf8`. The current dump calls `CMSaveBufferToFile(..., DIR=2, ...)` around lines 1360 onward in `native-cdn-decomp-new.txt`; inspect exact filenames, sizes, save-result handling and returned pack metadata. `ExportPKGIver1(buffer)` G `007cf6a0` and `ExportPKGIver1(path)` G `007d1108` are metadata producers, not automatically durable PVC writers.
- `CleanOld`: G `007ce834`, called by `UnpackAll` G `007cd818` after its worker chain. Close whether it removes outdated output paths, alters metadata, or writes the final header/PVC root. Do not infer it erases current files from the name.
- `CMLocalDB::Get(key)` G `007202a4`; `Get(key, PROPERTY)` G `007203a8`; JSON `Put(key, JSON)` G `0071d3a4`; string `Put` G `0071d2cc`; `PutDir` G `0071f65c`; `Delete` G `0071e748`. These targets distinguish JSON path normalization and adapter dispatch from concrete disk operations. Resolve caller and adapter before treating a Put as durable write.
- `GetResVer` G `007cf584` reads literal `header/stamp`; `DownloadHeader` G `007d2f9c` reads literal `header\\stamp`. Literal spelling is now proved, but separator normalization remains unproved. Header callback/cache writes and root `header` loading belong to root's persistence audit.

Historical decoded keys identify an evidence target: `CDN/PVC/<name>/stamp`, `CDN/PVC/<name>/packs/[<packid>]/filename`, `.../size`, and `.../sign`. Current snapshots must establish their presence and values after unpack completion and after a fresh boot. Historical encrypted/string encodings must not be treated as plaintext integer values merely because key names are visible.

## Minimum discriminating live evidence

For one representative package, preserve a post-Village snapshot and compare it to the next pre-download state. Record only necessary local diagnostic fields: parsed `name/pkg/stamp/size/md5` and step; actual resolved DIR `2` outer path, existence, byte count and native Signing result; PVC null/non-null and stamp; first differing output filename and expected/actual byte count if any. Keep private app snapshots local.

The strongest attribution records the native enqueue reason for that row. A filesystem snapshot without proof of directory/path resolution can miss an alternate storage root. A 139-request server trace without native reason cannot choose among PVC null, stale stamp, output size failure, or valid outer-package suppression failure. A completed Village bootstrap does not by itself prove queued PVC persistence or disk durability.

No server/header/MD5 change is justified by this audit. Next action is to close `GetPVCInfo`, queued unpack metadata writer and local-DB normalization, then compare those precise values across the already authorized fresh-boot sequence.
