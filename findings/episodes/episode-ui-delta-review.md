# Episode delta candidate: independent LevelDB format review

2026-10-05. Read-only review of `tools/build-episode-ui-delta.py` and `analysis/episode-ui-delta-candidate-v2/UI_XML_RO.db`. No VM, instrumented assets, originals or candidate mutation. Only an explicitly authorized throwaway copy was opened with LevelDB.

## Result

**No actionable findings.** The builder's six-key append-only SST/MANIFEST delta loads successfully in an independent native LevelDB implementation, beyond agreement with its own raw reader.

Pinned **plyvel1.5.1** was imported from `analysis/leveldb-tooling-ci/plyvel/__init__.py`. Candidate-v2 was copied to **analysis/ui-episode-native-reader-check/UI_XML_RO.db**. Only that copy was opened, with **create_if_missing=False, paranoid_checks=True**. Full native iteration produced **688 keys**, identical in all key/value bytes to the separate raw MANIFEST/SST/Snappy/WAL reader. A second reopen with **iterator(verify_checksums=True)** also succeeded and confirmed the six alias hashes.

The added keys are exactly:

- EN/EPISODE/E_T_EPISODE
- EN/EPISODE/E_T_STAGE
- EN/EPISODE/E_C_EPISODE
- EN/EPISODE/E_C_STAGE
- EN/EPISODE/E_C_MAPMARK
- EN/EPISODE/E_T_STAGEMAP

Each value is byte-identical to its original KO counterpart. All682 source keys/values are unchanged. No EN/DEFINE_COLOR alias is added. Before/after SHA256 of **every file** in both the current source seed and candidate-v2 are unchanged, including original base000005.ldb and both manifests. Independent LevelDB recovery/compaction may alter the throwaway copy; that does not promote or modify the candidate.

## Reviewed logic

SST writer encodes internal sequence/value tags, sorted keys, restart blocks, block handles, LevelDB footer magic and CRC32C trailers. MANIFEST writer preserves existing bytes, appends a NewFile level0 edit plus advanced file/sequence counters, and writes a new LF-terminated CURRENT. It selects a fresh file number beyond current counters and physically existing numbers; existing source files remain preserved. Native loading and checksum verification establish this specific generated candidate's format compatibility, not a proof for every arbitrary input database.

The builder refuses existing destinations/targets and missing original KO records, copies only the six selected records, checks destination logical contents against source-plus-aliases, and verifies source preservation. No silent deletion/whole-table rewrite or palette alias was found. Its raw-reader import is a report companion; no LevelDB writable open occurs inside the builder.

## Evidence and limits

**analysis/research/episode-ui-native-reader-check.json** records the exact library location/version, copied/opened path, counts, all six full value hashes, checksum flags, original-content equality and full source/candidate SHA256 maps. This review proves an independently readable compatible delta while preserving sources. It does not prove Android's engine rendered Episode, confirm live installed DB contents, publish a resource version or rebuild/install an APK. Native UI validation and the standing required release remain parent/tester work.
