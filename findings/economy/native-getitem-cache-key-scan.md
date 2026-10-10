# Exact original GetItem cache-key scan

2026-10-07. Authorized narrow keys-only audit of the three preserved phone snapshots' **UserData.db/EtcData.db** containers, based on parent-proved native key **REFEN/REFERENCE/GETITEM**. No live phone/adb/VM/Ghidra, LevelDB open/compaction, account body dump, private body export, grant or source mutation.

**Result: no matching cache record.** Existing9/19 UserData.db.keys.json497rows and EtcData.db.keys.json29rows contain zero case-insensitive exact/contained GetItem key matches. Both also contain zero REFEN/REFERENCE/ prefix matches.

The same result was independently checked against active database storage using existing **analysis/research/episode-ui-audit.py**: CURRENT-selected MANIFEST add/delete file state, SST restart/Snappy decoding, current/previous WAL replay and latest-sequence deletion handling. No writable database library was opened; no unmatched value was decoded as application data or printed. Raw block bytes necessarily passed through the reader, but only keys/counts/storage metadata were evaluated.

Exact snapshot/container coverage:

- **phone-2026-09-18/private/files/local/UserData.db**:497live keys, MANIFEST-000380, SST374/376, WAL381. EtcData.db:29keys, MANIFEST-000441, SST437/439, WAL442.
- **phone-evidence-2026-09-19/diagnostics/files/local/UserData.db**:497keys, MANIFEST-000371, SST374, WAL373. EtcData.db:29keys, MANIFEST-000434, SST437, WAL436.
- **phone-history-2026-09-20/private/files/local/UserData.db**:497keys, MANIFEST-000371, SST374, WAL373. EtcData.db:29keys, MANIFEST-000434, SST437, WAL436.

All six containers have **zero REFEN/REFERENCE/GETITEM** and **zero REFEN/REFERENCE/** live keys. Nonempty older373/436 WALs were included, so this is not an SST-only negative. Before/after SHA256 maps for every source file were compared and unchanged. No exact match existed to authorize the conditional reference-record body inspection, so **no body was inspected/exported**.

Machine-readable scoped evidence: **analysis/research/native-getitem-cache-key-scan.json** records the exact key, live counts, active manifests/tables/WALs, empty match lists, namespace counts and source-unchanged outcomes. It contains no account keys/values or private response body.

This exhausts the two previously proposed small state-container candidates within these three snapshots. It does not establish that CMJetLoader uses those containers for the native reference resource, nor that every other resource/cache location lacks GetItem. Storage ownership remains a separate native question. No genuine fish catalog was recovered and no fish ID/item metadata was invented from this negative.
