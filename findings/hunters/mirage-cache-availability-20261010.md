# Preserved Mirage cache availability audit

2026-10-10. Bounded offline, read-only audit of preserved phone evidence. No live phone, ADB, BlueStacks, Ghidra, Docker, server/account changes or application-value dump. Only this report was written. This is not another stat/visual hunt.

## Result and interpretation

No positive persisted Mirage floor/reference/run response was identified in the inspected indexes or six small active state containers. The 60 Mirage-containing CDN keys describe the original **MIRAGE** and **UI_MIRAGE** resource packages, rather than floor transactions or `ref_stair`/`ref_monster` rows. They are useful material provenance, not an encounter catalog.

This is a scoped negative: filename or key absence does **not** prove that original Mirage data is unrecoverable. Opaque/generated resources, unnamed/encrypted values, unindexed WebView objects, deleted historical LevelDB records, other snapshots and independent server captures are outside this audit. No guessed floor/balance/enemy/reward rows should be published from this result.

## Existing indexes checked first

Sources under `recovered-assets/phone-evidence-2026-09-19/`:

- `UserData.db.keys.json`: 497 rows, zero case-insensitive `MIRAGE`, `REF_STAIR`, `REF_MONSTER` or `GETNEXTFLOOR` key matches.
- `EtcData.db.keys.json`: 29 rows, the same zero-match results.
- `CDN.db.keys.json`: 23,656 rows; 60 keys contain `MIRAGE`, zero keys contain `/MIRAGE/`, `REF_STAIR`, `REF_MONSTER`, `GETNEXTFLOOR` or `REFEN/REFERENCE/`.
- `web-cache-manifest.json`: 497 metadata records; zero `mirage`, `/mirage/` or `getnextfloor` path matches. Only paths/counts were inspected; no host identity, query values, headers or cached bodies were printed.

The 60 CDN keys divide into 30 metadata keys plus 30 corresponding `type:` keys. They all fall under `CDN\\PVC\\MIRAGE`, `CDN\\PVC\\UI_MIRAGE`, `CDN\\RES\\MIRAGE.jet`, `CDN\\RES\\UI_MIRAGE.jet`, or the two matching `CDN\\header\\items` trees. Their fields are resource descriptors (`packs`, `filename`, `sign`, `size`, `stamp`, `name`, `pkg`, `step`), not response/floor member names. Descriptor values were not decoded or exported.

## Active database replay

Used the existing read-only `analysis/research/episode-ui-audit.py` reader: CURRENT-selected MANIFEST file adds/deletions, active SST restart/Snappy decoding, selected current/previous WAL replay, highest-sequence selection and deletion handling. No writable LevelDB library, locking or compaction was used. Raw values necessarily pass through block/replay parsing but no unmatched application value was interpreted or emitted.

- `phone-2026-09-18/private/files/local/UserData.db`: 497 live keys; MANIFEST-000380; SST 374/376; WAL 381, previous WAL 0.
- `phone-2026-09-18/private/files/local/EtcData.db`: 29 live keys; MANIFEST-000441; SST 437/439; WAL 442, previous WAL 0.
- `phone-evidence-2026-09-19/diagnostics/files/local/UserData.db`: 497 live keys; MANIFEST-000371; SST 374; WAL 373, previous WAL 0.
- `phone-evidence-2026-09-19/diagnostics/files/local/EtcData.db`: 29 live keys; MANIFEST-000434; SST 437; WAL 436, previous WAL 0.
- `phone-history-2026-09-20/private/files/local/UserData.db`: 497 live keys; MANIFEST-000371; SST 374; WAL 373, previous WAL 0.
- `phone-history-2026-09-20/private/files/local/EtcData.db`: 29 live keys; MANIFEST-000434; SST 437; WAL 436, previous WAL 0.

All six have zero case-insensitive `MIRAGE`, `REF_STAIR`, `REF_MONSTER` or `GETNEXTFLOOR` live key matches. This includes the nonempty older WALs, so the negative is not SST-only. SHA-256 maps of every file in each selected database directory matched before and after replay. No original snapshot bytes changed. No exact candidate existed to justify conditional application-value inspection.

## Storage-model limit and next useful work

`native-reference-offline-storage.md` establishes that generic `CSRSyncRef.RequestByPVJson` can load `REF` + locale + URI through the JET/resource map before HTTP. That is not proof of a write-through cache in UserData/EtcData, and this audit does not assume Mirage's dedicated `GetInfo` uses that generic fallback. Existing `native-reference-cache-candidates.md` and `native-getitem-cache-key-scan.md` explain the preserved directory/index provenance and why CDN descriptors must not be treated as gameplay responses.

Do not repeat broad private-cache or stat scans based solely on this negative. A stronger next lead is either an exact native Mirage persistence/resource key with a proved storage owner, or an authentic original response/source with floor rows and run semantics. Original help/video observations can constrain behavior and presentation, but cannot supply missing final floor transactions by themselves.
