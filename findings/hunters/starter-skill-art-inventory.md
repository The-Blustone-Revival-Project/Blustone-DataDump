# Starter skill art: verified records and naming limit

**UPDATE2026-10-04:** resource-name inventory limitations below are superseded by `starter-skill-resource-bindings.md`. Native `RM10to38` decodes the uint64 header name id, exposing genuine Qpack skill-icon ATnames and CUTIN names; original cut_in_id/icon_id assignment remains unproved. Preserve the old failed approaches as method evidence, not current inventory conclusions.

2026-10-04. Read-only inspection using existing `jet_decoder.inflate_jet_resources`, `find_media`, `list-jet-entries.py`, and `extract-jet-chunk.py`. Originals, server, client and tools unchanged. No runtime actions. No guessed cut-in/icon bindings.

## Four requested packs

Source root: `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`.

**CUT_001.jet** (622980bytes): established logical-resource parser yields **6 I2 texture records**, at compressed payload offsets24,518254,568939,582201,595004,608769. Inflated sizes3981758,147658,33482,35018,35018,33482bytes. No readable `CUT`, `C001`, or skill-name resource identifiers were found in those records.

**CUT_002.jet** (1938440bytes): **18 logical I2 texture records**. No readable `CUT`/`C002`/skill-name identifiers found in their inflated bodies. Some records are assembled from multiple compressed chunks. The byte-faithful chunk helper's header-size comparison reports mismatches for continuation chunks because the header's first-size field describes a larger logical resource; it is not a valid per-chunk name extractor here.

**C001_EFT.jet** (1383938bytes) and **C002_EFT.jet** (5001859bytes): first payload is **SN-wrapped uncompressed MP4**, not a zlib resource. Raw prefix contains `SN` at20 and24; MP4 `ftyp` follows. The zlib/I2 logical parser therefore returns0 for these files. The established media recognizer identifies a first MP4 at offset34, sizes146374/639666bytes respectively. This media extraction result establishes video payload presence, **not an internal animation id** or complete multi-record SN inventory. No media was exported.

`list-jet-entries.py` prints placeholder/numeric identifiers for CUT records and no EFT entries. These are decoder limitations; do not use them as actual tree paths. The requested packs expose no verified resource-name tree through the current parser.

## Relevant names actually visible in base animation packs

The established inflater exposes readable RW animation data from **C001.jet**, logical payload offset315021, and **C002.jet**, offset214559. These contain exact names/references:

- Both prefixes: `_A1..A3`, `_AT1..AT3`, `_C`, `_DIE`, `_H1..H3`, `_I`, `_I2`, `_R1`, `_R2`, **`_SK1`, `_SK2`**, `_T`, `_W1`, `_W2`.
- C001 animation data additionally references **C001_E01**, **C001_E02**, **C001_E04**, **C001_EC**, and C001_SND01..04.
- C002 additionally references **C002_E01**, **C002_E02**, **C002_E03**, **C002_EC**, and C002_SND01..03.

[VERIFIED byte inventory] These are literal resource/animation references inside the base RW data. [INFERRED] E-prefixed names likely address effect resources, while SK names denote skill animations. This pass does not resolve which `_E*` record corresponds to active slot1, whether `_EC` is a combined effect, or the precise loader binding. **Neither SK1 nor E01 is proved to be `SRSKILL_INFO.cut_in_id` or `icon_id`.**

## Why filenames cannot close the binding

Existing `analysis/research/map-backdrop.md` §6 records the decisive counterexample: **M001.jet has no plaintext names yet native runtime registers M001_R01..R04**. The engine's resource-map naming/extraction contract therefore does more than expose printable package text. Absence of printable CUT names does not show the cut-in art is absent; filename equality does not prove a loadable id.

Native symbol inventory locates **CRMResMap::ExtractJETInfo at0x10e5f58** (Ghidra address), plus GetResNameList/GetResListinJET. Recovering that naming/decode contract or reading the runtime ResMap would be the appropriate next step if effect implementation requires art. This lane did neither.

**Conclusion:** texture and video art exists, and base animation references identify exact C001/C002 SK/E names. Exact `cut_in_id`/`icon_id` values remain **[UNKNOWN]**. Preserve blank explicitly provisional bindings until a native/resource-map match is proved; do not invent CUT_001, CUT_002, or a directory path from pack filenames.
