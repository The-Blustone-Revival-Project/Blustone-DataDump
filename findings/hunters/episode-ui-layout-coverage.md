# Episode UI layout locale coverage

2026-10-05. Read-only original phone snapshot, preserved table export and current instrumentation seed directories. No aliases, DB opens, compaction, source/VM/client edits. Report is the only written artifact.

## Exact inventory method

`analysis/in-game-stats/ui-xml-ro-keys.tsv` starts with a historical Python traceback; it is **not a usable key inventory**. Missing matches in that file prove nothing. The corresponding ui-ko-keys.tsv did not supply a trustworthy Episode inventory either; conclusions below use actual database bytes.

A lock-free reader reused `tools/inspect-leveldb.py`'s varint/SST restart-block routines and `tools/read-leveldb-log.py`'s physical/logical record and WriteBatch routines. It decoded Snappy literal/copy blocks in memory, validated decompressed lengths, parsed the active CURRENT-selected MANIFEST VersionEdit add/delete-file entries, read only active SST files, merged active/current and previous WAL operations by internal sequence, and applied deletion tombstones. No plyvel or writable LevelDB connection was opened. In particular physically present **000049.ldb is not active** in the inspected seed and was excluded.

Inspected sources:

- Original `recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db`: **584 live keys**, active SST file5.
- Current `instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db`: **682 live keys**, active SST5,12,25,28,31,34,37.
- `instrumentation/assets/instrumented-seed-battle-full-clean/UI_XML_RO.db`: **682 live keys**, same active SST numbers.

Telemetry.java's seed-copy source at line661 is complete-ui-delta-v2. This identifies the current source seed, **not proof of the live installed/emulator DB contents**. No device was inspected.

## Original Episode layouts survive unchanged, only under KO

All3 inspected sources have exactly the same17 **KO/EPISODE/** records, identical sizes and SHA256 prefixes. They have **zero EN/EPISODE/** keys. The preserved 13-table export corroborates the same17 original Korean records; no English counterpart was recovered there.

Exact original record inventory (path suffix, bytes, SHA256 prefix):

```text
E_ALL_CLEAR    3908   ace3cc8bdbeb
E_C_EPISODE    6899   1528dffc5600
E_C_MAPMARK    1017   9c14e87c98e6
E_C_STAGE      3208   68ec89994601
E_C_STORY       991   f44a83af0fb8
E_DECKSET     14204   7998206f5e70
E_DECKSET2     6419   db27aefa92e8
E_ICON         810   d24ccf6f1b06
E_MAP         1831   fd3dfbcae2b7
E_MS_CF       6349   5b017eb54082
E_MS_CF2      7539   beed03670b00
E_T_EPISODE   3957   66361b94ff4e
E_T_EPITEST   3718   96a40be8c34f
E_T_STAGE     3934   f0c688ac91a8
E_T_STAGEMAP   323   c04e45a5a9e4
E_T_STORY     1219   355f2fab0acc
E_T_STOTEST   1219   355f2fab0acc
```

Every suffix above is actually prefixed **KO/EPISODE/**. No new EN aliases or delta were produced.

## Actual native consumers and remaining top-root proof

Parent's fresh `ghidra-episode-ui-loaders-keys.txt` proves native loader names:

- Chapter CSRCellMEpisodeDraw.LoadView Ge58b58 requests **EPISODE/E_C_EPISODE**, exact literal LDR Ge58cd6/ADD Ge58cda.
- Story-list cell requests **EPISODE/E_C_STAGE**.
- Map marker requests **EPISODE/E_C_MAPMARK**.
- Stage-map presentation requests **EPISODE/E_T_STAGEMAP**.

These native relative identifiers have exact preserved Korean records, but no exact English counterparts in the inspected sources. How the engine chooses/falls back between locale prefixes is a separate native helper contract. **Do not conclude a crash or require an alias merely from zero EN keys**: earlier Supply behavior demonstrated the value of proving the actual loader/fallback path.

E_T_EPISODE, E_T_STAGE, E_T_STORY and other root-looking names are verified **existing XML records**, but filename resemblance does not prove which top OnInit requests each. Parent owns the exact top-scene loader recovery. E_T_STAGEMAP has LIST_SLOT/TEST_MAP_DRAWING and sprite SR_STAGE; E_C_MAPMARK has LIST_SLOT/ANI_PANEL/RE_SE_ON. These are XML-content facts, not a live layout render claim.

## Safe next action

Use the real native root/cell LoadView names and locale-fallback helper to select the smallest necessary compatibility action. If an EN alias is ultimately needed, preserve the original multi-SSTable base and append only proven records through the established selective delta procedure; never wholesale-copy KO, especially DEFINE_COLOR. That potential edit is deliberately outside this read-only unit. Current evidence proves preserved Korean layout availability and exact absence of English equivalents in source snapshots/seeds, while runtime fallback and actual Episode rendering remain unverified.

## Reproducible audit companion and literal dependency closure

The exact reader is saved as **analysis/research/episode-ui-audit.py**. Run `python analysis/research/episode-ui-audit.py` from the workspace root (its source paths resolve from the script, so other working directories also work). Its only output write is **analysis/research/episode-ui-layout-inventory.json**. This JSON preserves every exact Episode key, full SHA256, size, active MANIFEST/SST/WAL identifiers, and before/after SHA256 for **every file** in all3 source directories. All3 source-file maps were identical before/after; `source_unchanged:true` is confirmed for both seeds and the original snapshot. Source checksums were not inferred from Git status. The reader intentionally does not validate LevelDB CRC checks; it fails on unknown MANIFEST tags, unsupported compression or Snappy length mismatch.

Every original Episode XML record was parsed and every attribute value checked against exact source key, locale-prefixed key and same-directory key. **All17 records have zero direct XML child-layout dependency keys.** File attributes found are comp-motion/comp-sound resources (THUMB_INIT/SHOW/HIDE, UI_BT_PRE/REL variants, FX_OK_N/FX_BACK_N), not references to the other Episode layout keys. The JSON stores both `direct_dependency_keys` and `layout_like_attributes`, without relabeling resource IDs as UI layout links.

This establishes that the4 recovered cell/map loaders do **not acquire the other13 layout records through literal XML child includes**. It does not establish that4 aliases cover normal Episode entry: native top OnInit, map/root construction, dialogue/deck/result windows and dynamic loaders remain independent keys. Therefore neither4 nor17 is a proved complete alias closure yet. Parent's exact scene-root LoadView recovery must define the selective set. No aliases or instrumented rebuild were performed; a future APK rebuild still carries the standing required-release obligation.
