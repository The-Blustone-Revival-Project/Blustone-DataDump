# `environments-recovery.md` — `environments.csv` is **not** missing. The lookup key is.

Content-recovery agent, 2026-10-03.
Question from the brief: *recover `environments.csv`, or prove it unrecoverable.*
Mandated by `analysis/research/STATUS-2026-10-03.md` §2 and
`analysis/research/scrollbg-crash.md` §5-6, both of which assert the file does
not exist anywhere in this workspace.

**Both of those claims are wrong. The file is in `LEVELING.jet` in the base APK,
it is recovered, and it is at `analysis/recovered-data/environments.csv`.**

| | |
|---|---|
| Verdict | **[RECOVERED]** — content found, extracted, byte-verified. |
| The actual defect | **[RECOVERED-strong]** a `std::map::find()` **miss** (or an empty `ENV_INFO.PreFix`), *not* a missing file. |
| Fix | **[AUTHORABLE]** and small — one environment id string per stage/battle. Not a file recovery. |
| Placement | **[RECOVERED]** the file already ships in the APK the client installs. **No CDN change required.** |

---

## 1. Exact filename and format the client expects **[RECOVERED]**

**Filename: `environments.csv`.** Not a guess, not a `CMCSVReader` convention —
assembled from two adjacent Thumb literals and a 4-byte append inside
`CSRStaticData::LoadEnv`:

```
# tools/resolve-literals-offline.py --function 0xf3bab0:0xf3c2a0
ldr@0x00f3bb1e r6 slot=0x00f3be98 w=0x00e53655 add_pc=0x00f3bb24 -> 0x01d8f179  'environments'
ldr@0x00f3bb32 r2 slot=0x00f3be9c w=0x00e35729 add_pc=0x00f3bb3a -> 0x01d71263  '.csv'
ldr@0x00f3bbe4 r1 slot=0x00f3beac w=0x00e5358f add_pc=0x00f3bbea -> 0x01d8f179  'environments'
ldr@0x00f3bb96 r2 slot=0x00f3bea0 w=0x00e26da4 add_pc=0x00f3bb9c -> 0x01d62940  '[ERR] [%s] '
ldr@0x00f3bba0 r0 slot=0x00f3bea4 w=0x00e2b421 add_pc=0x00f3bba6 -> 0x01d66fc7  'Load failed %s'
ldr@0x00f3c008 r2 slot=0x00f3c294 w=0x00e26932 add_pc=0x00f3c00e -> 0x01d62940  '[ERR] [%s] '
ldr@0x00f3c012 r1 slot=0x00f3c298 w=0x00e53176 add_pc=0x00f3c018 -> 0x01d8f18e  'File Load failed(ENVIRONMENTS)'
```

`analysis/native-all-strings.tsv` independently lists `01d8f179 environments`,
`01d8f18e File Load failed(ENVIRONMENTS)`, `01d71263 .csv`. `Load failed %s` is
30 characters of format that the `[ERR] [%s] ` prefix wraps.

`LoadEnv` has **two** failure paths and both leave a distinctive
`[ERR] [%s] File Load failed(ENVIRONMENTS)` / `... Load failed %s` line
(`analysis/ghidra-leveldata-decomp-04.txt:118-133` and `:366-385`).

### Format — 18 columns, positional, read by `CMCSVReader::GetString(col,row)` **[RECOVERED]**

`analysis/ghidra-leveldata-decomp-04.txt:205-279` reads every row with exactly
18 positional `GetString` calls and an alternating type pattern:

```c
pbVar19 = CMCSVReader::GetString(&local_60, 0, row);      /* string */
pbVar8  = CMCSVReader::GetString(&local_60, 1, row);      /* string */
pbVar8  = CMCSVReader::GetString(&local_60, 2, row);      /* string */
for (col = 3; col <= 0x11; col += 3) {
    stol (GetString(col + 0, row));    /* 3, 6, 9, 12, 15  -> int  */
    stof (GetString(col + 1, row));    /* 4, 7, 10, 13, 16 -> float*/
    stof (GetString(col + 2, row));    /* 5, 8, 11, 14, 17 -> float*/
}
```

then `std::__ndk1::__tree<__value_type<basic_string, CSRStaticData::ENV_INFO>>::`
`__emplace_unique_key_args<...>(key, *(this + 0x150))`
(`decomp-04.txt:335-341`).

`CSRStaticData::ENV_INFO` therefore is **`{ std::string, std::string,
std::string, int, float, float × 5 }`** — 3 strings (36 B) + 15 numbers (60 B) =
**96 bytes**, and the map lives at `CSRStaticData + 0x150`.

---

## 2. The file **[RECOVERED]**

`LEVELING.jet`, chunk index 5. 18 columns, 50 data rows, 19 distinct `PreFix`
values. Full listing and provenance in `analysis/recovered-data/README.md`; the
file is `analysis/recovered-data/environments.csv`
(sha256 `0c9e214daae929e264083329dc8fdd7f0b02b4f438ec159080a82d6264da1b4c`,
4381 bytes).

### Why this *is* `environments.csv`, not some other 18-column table

1. **Column count and type pattern are an exact match** for `LoadEnv`'s 18
   positional reads (§1): 3 strings then 5×(`stol`,`stof`,`stof`).
   No other chunk in the 774-package corpus has this shape (§4).
2. **Content matches what the consumer needs.** The 15 numeric columns are five
   depth bands — `원거리`(long range) / `중거리` / `근거리` / `초근거리` /
   `비행선`(airship) — each with `구성`(arrangement row), `속도`(speed),
   `높이`(height). `CSRGameBase::MakeBackground` is called **exactly five
   times** per scene, once per band, and `CSRGameScrollBGDraw::Load` builds a
   **scrolling** parallax stack per band. Five bands in the table, five calls in
   the code.
3. **Row identity matches the scene taxonomy.** `99 배틀`(battle),
   `100 협회전`(guild battle), `200 레이드`(raid), and then per-map rows keyed by
   the map's numeric id (`515 레비`, `521 레베카`, `525 테디보머`, `900…907` the
   무저갱 boss stages). This is the environment table for battles, not a UI
   layout table.
4. **`PreFix` names a real asset family.** 18 of the 19 `PreFix` values minus
   the `I` are exactly the base-APK art packages: `STI000…STI007` ↔ `ST001.jet`
   … `ST007.jet`, `STI099` ↔ `ST099.jet`, `STI100` ↔ `ST100.jet`,
   `STI900…STI907` ↔ `ST900.jet` … `ST907.jet`. (Only `STI801`, row 801
   할로윈/Halloween, has no package in this APK.)

### The channel the file travels on **[RECOVERED]**

```
if (CGMDataMgr::get()->[+0x5814] == '\0') {          /* no data root       */
    std::string s("environments");                   /* decomp-04:102-106  */
    SRLoadRawDataStr(s);                             /* local asset tree   */
    if (!empty) { CMCSVReader::ParseAll(...); goto rows; }
    RMTrace("[ERR] [%s] File Load failed(ENVIRONMENTS)");
} else {                                             /* data root set      */
    CMCSVReader::Open(dataRoot + "environments" + ".csv");   /* CM database */
    if (ok) goto rows;
    RMTrace("[ERR] [%s] File Load failed(ENVIRONMENTS)", filename);
}
```

`LoadCommon` (`0xf39e54`) reads `common` + `.JSON` through the byte-identical
idiom. `analysis/research/leveldata-id-source.md:304-324` established that
`common.JSON` and the ten `leveling_*.JSON` files exist **only** in `LEVELING.jet`
and in **none** of the 11 served CDN packages, and that `common.JSON`
*demonstrably loads at runtime* (village / Supply / Mail work). `environments.csv`
is in the same chunk container in the same package.

⇒ **The client already has this file. There is nothing to serve.**

---

## 3. So the failure is a key miss, not a missing file **[RECOVERED-strong]**

### 3.1 `LoadEnv` did **not** fail at runtime

`analysis/r015/logcat-all.txt` (22.8 MB, 5 mission legs):

```
Select-String "environment" -CaseSensitive:$false   -> 0 hits
Select-String "ENV"        -CaseSensitive           -> 0 hits
Select-String "LoadEnv|CSV|SRLoad|RawData"          -> 0 hits
Select-String "\[ERR\]"                             -> 495 hits
```

495 `[ERR]` lines **do** reach logcat in the same file (`[ERR] [RES]`,
`[ERR] [DB]`, `[ERR] [ADS]`, `[ERR] [PV]`), and the sibling `[WRN] [Load]` line
that `CSRGameScrollBGDraw::Load` emits for each missing layer is present. So the
absence of `File Load failed(ENVIRONMENTS)` / `Load failed %s` is real evidence
that the file opened. Corroborated independently by the `common.JSON` control
experiment above. **[INFERRED-strong, not [RECOVERED]]** — a completely silent
success is the negative of an evidence set, not an observation.

### 3.2 `OnInitBackground` uses `find()` **without** testing `end()` **[RECOVERED]**

`CSRGameBase::OnInitBackground` (Ghidra `0x9cbf34` = ELF `0x9bbf34`). The
relevant block, verified instruction by instruction with
`llvm-objdump --triple=thumbv7-linux-gnueabihf` (note `Ghidra == ELF == file offset + 0x10000`):

```
009bbf50  bl    0x8a3390            ; CSRDataMgr::get
009bbf54  bl    0x8a26d4            ; CSRDataMgr::GetStaticData
009bbf58  add.w r0, r0, #0x150      ; &std::map<string,ENV_INFO>
009bbf5c  mov   r1, r5              ; param_1 = the environment key
009bbf5e  bl    0x9dbc10            ; std::map<string,ENV_INFO>::find
009bbf62  mov   r5, r0              ; <-- NO compare against end()
009bbf64  mov   r10, r0
009bbf66  ldrb  r0, [r5, #52]!      ; r5 = node+0x34 ; read ENV_INFO.PreFix[0]
009bbf6a  lsls  r0, r0, #0x1f      ; long-string bit (libc++ 12-byte string)
009bbf6e  addeq r6, r5, #0x1       ; short -> chars at node+0x35
009bbf70  ldrne.w r6, [r10, #0x3c]  ; long  -> ptr  at node+0x3c (= +8)
009bbf74  bl    0x8a3390            ; CSRDataMgr::get
009bbf78  bl    0x8a26d4            ; GetStaticData
009bbf7c  mov   r1, r0
009bbf82  ldrb  r2, [r1, #108]!     ; CSRStaticData + 0x6c, first suffix string
009bbf8c  ldrne r3, [r0, #0x74]
009bbf92  mov   r2, r6              ; arg1 = ENV_INFO.PreFix
009bbf94  add   r1, pc              ; format
009bbf96  bl    0x77cac4            ; CMFormat(buf, "%s_%s", PreFix, suffix)
```

The format string is recovered literally, four times, once per band:

```
# tools/resolve-literals-offline.py --function 0x9cbf34:0x9cc400
ldr@0x009cbfc8 ... -> 0x01d7583b  '%s_%s'
ldr@0x009cc000 ... -> 0x01d7583b  '%s_%s'
ldr@0x009cc038 ... -> 0x01d7583b  '%s_%s'
ldr@0x009cc070 ... -> 0x01d7583b  '%s_%s'
```

**The five suffixes are five consecutive `std::string`s at `CSRStaticData + 0x6c,
0x78, 0x84, 0x90, 0x9c`** (108/120/132/144/156 — confirmed by the
`ldrb rX,[rY,#imm]!` / `ldrne rX,[rY,#imm+8]` SSO pattern at each). Not
`LoadCommon` keys (`LoadCommon` reads only `skill_damage_spawn_interval`,
`gacha10_over_recruit_limit`, `coin_rwd_ratio_boss`, `coin_effect_gravity` —
`resolve-literals-offline.py --function 0xf39e54:0xf3a600`). **[UNKNOWN]** where
those five strings come from; observed values on device are `A`, `D`, `E`.

### 3.3 `ENV_INFO` layout — the string at `node+0x34` is `PreFix` **[RECOVERED]**

From `LoadEnv`'s own stack arithmetic (`analysis/ghidra-leveldata-decomp-04.txt`
+ ELF `0xf2bbfe-0xf2bf9c`), the `pair<const string, ENV_INFO>` it builds has, with
`r5 = sp+0x20`:

```
r5+0x00  key string   (12 B)      <- the map key
r5+0x0c  ENV_INFO string #1        = r5+0x0c
r5+0x18  ENV_INFO string #2        = r8
r5+0x24  ENV_INFO string #3        = r10
r5+0x30  first numeric field       = r9
```

With libc++ 32-bit `std::string` = 12 bytes and a 16-byte `__tree_node_base`
header, a node lays out as `0x10 header | 0x0C key | 0x1C ENV_INFO`, giving
`ENV_INFO+0x18 = node+0x34` — exactly where `OnInitBackground` reads the
`PreFix`. The 16-byte header is the only self-consistent choice: with a 12-byte
header the five `MakeBackground` arguments would land on the 16th of 15 numeric
fields, which does not exist.

Cross-check on the numeric fields: `MakeBackground(name, uint, float)` takes its
second argument from `node+0x44, 0x50, 0x5c, 0x68, 0x74` — stride `0x0C` — which
under that layout is the **second word of each `(int, float, float)` triple**,
i.e. the five `속도` (scroll-speed) floats `-5, -20, -40, -60, -20`. Five bands,
five calls, a scroll speed each. The layout is confirmed end to end.

### 3.4 What the device actually asked for **[RECOVERED]**

Whole of `analysis/r015/logcat-all.txt`, every distinct argument of
`Cannot find The resource(...)` (the message that is unique to
`CSRGameScrollBGDraw::Load`):

```
_A0 _A1 _A2 _A3 _A4 _A5 _A6 _A7 _A8 _A9
_D0 _D1 _D2 _D3 _D4 _D5 _D6 _D7 _D8 _D9
_E0        _E2 _E3 _E4 _E5 _E6 _E7 _E8 _E9
ST001
```

29 distinct names, **every one prefixless**. With a hit row the same code would
emit `STI099_A0`, `STI900_A0`, … — a `PreFix` is never empty in the table, so an
empty prefix can only come from the unchecked `find()` reading the tree's
end-node, or from `ENV_INFO.PreFix` never being populated at all. Both are the
same defect class; the logcat in §3.1 favours the former.

Corroborating detail: the same logcat shows
`[ERR] [RES] Can't find 'ST001' in ResMap.` once per leg. That is our fixture's
invented stage `res_prefix` (`analysis/r015/preflight-GetStage.json`), not a
`PreFix`, and it is a **separate** content gap — see §6.

---

## 4. Every place searched

| # | target | method | result |
|---|---|---|---|
| 1 | exact filename | `tools/native-grep.py -p environment -t both`; `-p csv`; `-p ENV` | `'environments'` `01d8f179`, `'.csv'` `01d71263`, `'File Load failed(ENVIRONMENTS)'` `01d8f18e`. Confirms the name; **no other candidate spelling exists in the binary**. |
| 2 | `recovered-assets/**` (5 snapshots) | streaming ASCII scan of every non-`.so/.dex/.png/.jpg` file for `environments` | **2 hits, both the `libnative_core.so` inside `split_config.arm64_v8a.apk`** at offset 36 698 160 — the literal pool. **Zero** content hits. |
| 3 | `recovered-assets/**` | `Get-ChildItem -Recurse -Filter *.csv` | **no `.csv` file anywhere** (confirms the brief's finding) |
| 4 | 5 tarballs (`game-data.tar`, `game-diagnostics.tar`, 3× `private-current.tar`, 1 638 / 649 / 289 / 1 726 entries) | `tar -tf`, filtered `csv\|env\|ENV` | **no matching entry** |
| 5 | base-APK asset corpus, **774 `.jet` files** (`analysis/extracted/assets`) | independent chunk walker (own parser, not `jet_decoder.py`): inflate every zlib chunk, report any chunk whose first 200 B contain ≥9 commas and no leading `{` | **exactly one 18-column CSV**: `LEVELING.jet` chunk 5. Others: `LEVELING` c1 (3 col), c19 (`power,rank,hyper,level`), `UI_CSV` c3/c4/c6 (IAP, ISO country, sound), plus binary false positives (`CUT_*`, `EQUIP`, `UI_TUTO`, `STAGE`, `N004`, `N010`, `C0xx`, `DIAL_BG9`, `FISHING`, `MIRAGE`). |
| 6 | phone snapshot's own package set, **774 `.jet` files** (`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`) | same scan | **byte-identical result.** Filename sets are identical to `analysis/extracted/assets` (0 files unique to either). So the phone snapshot does not hold a second or newer `environments.csv`. |
| 7 | all `.jet` chunks, both trees | needle scan for `_A0` | 16 hits, **all binary false positives** (PNG/ATLAS pixel data). The `_A0`/`_D0`/`_E0` resource names are **not stored as plaintext in any package** — entry names come from a PKGI1 index this workspace has not decoded, so "does `STI000_A0` exist as an entry" is **[UNKNOWN]** and cannot be answered offline. |
| 8 | `UI_JSON_RO.db`, `UI_TEXT_RO.db`, `UI_XML_RO.db`, `ADMIN_ID_RO.db`, `TAG_REF_RO.db`, `BADWORD_RO.db`, `CHAR_STR_RO.db`, `INGAME_TALK_RO.db`, `SKILL_*.db`, `UI_EPISODE_RO.db` (LevelDB, `recovered-assets/*/game-assets/`) and `working-db/{CDN,ETC,EtcData,PV,USER,UserData}.db` | streaming ASCII scan of the raw `.db` bytes (LevelDB values are snappy-compressed, so a plaintext scan can only miss them) **plus** the already-dumped tables in `analysis/recovered-data/leveldb-tables/*.tsv` searched for `environment` / `.csv` | **no plaintext `environments`; 0 hits in the dumped tables too.** A snappy-aware sweep of the raw `.db` files has **not** been done and is the one remaining hole — see §7. |
| 9 | `analysis/native-all-strings.tsv` | `native-grep.py -p csv` | `CMCSVReader` / `CSRCSVParser` symbols + `C:/Users/hkpark/.../CMCSVReader.cpp` + `01d71263 .csv`. `.csv` has **zero** literal-pool references outside `LoadEnv`, so no other file uses the extension. |

---

## 5. Where `ENV_INFO` must come from, and what the minimal fix is

### 5.1 The lookup key — generic path **[RECOVERED]**

`CSRExploreMirage::InitBackground` (Ghidra `0x926778` = ELF `0x916778`) is the
same scene setup done carefully — it walks the map and *checks* `end()`:

```
0091679e  add.w  r9, r4, #0x220        ; &this->stage_id   (std::string member)
009167a6  bl     0xa17f60              ; CSRGameStage::GetStageData(stage_id)
009167ac  ldrb   r5, [r4, #112]!       ; r4 = stage + 0x70  == res_prefix
009167b0  ldr    r6, [r4, #0x4]        ; res_prefix length
...
009167d8  cmp    r6, #0x0
009167dc  moveq  r4, r9                ; key = &this->stage_id   (empty res_prefix)
                                  ... ; key = stage->res_prefix  (non-empty)
009167ba  ldr.w  r1, [r0, #0x150]      ; manual std::map walk over CSRStaticData+0x150
```

and on a miss it logs the key:
`'Cannot find environment Information(ID:%s)'` (`0x01d72e06`, tag `InitBackground`,
`ldr@0x00926b9a` / `ldr@0x00926bd6 'InitBackground'`).

⇒ **The key is the stage's `res_prefix` (`/reference/GetStage` `ret_data[].res_prefix`),
falling back to the stage `id` when `res_prefix` is empty.** `node+0x70` of
`CSRGameStage::STAGE_DATA` is `res_prefix`, matching the offset used by
`SetStage` (`AGENTS.md` §11).

### 5.2 The lookup key — the path that actually crashes **[UNKNOWN]**

`CSRSceneMEpisode::InitBackground` (Ghidra `0xb23e80`) does **not** use
`res_prefix`:

```
00b23ec4  add.w  r1, r6, #0x24        ; key = *(std::string*)(X + 0x24)
00b23ec8  add    r2, sp, #0xc         ; CRMRenderParam
00b23eca  mov    r0, r4
00b23ecc  bl     0x009cbf34           ; CSRGameBase::OnInitBackground(this, X+0x24, rp)
```
(`analysis/ghidra-scrollbg-19-insn-mepisode-initbg.txt:31-34`)

`r6` is the result of `bl 0xb17712`, itself fed by `bl 0xb1dee0`. **`X+0x24`
is not yet characterised** — whether it is server-derived or local episode data
is the one question that decides whether `server-ts` can fix this. **This is the
single decompile still needed.**

### 5.3 Minimal record needed **[AUTHORABLE]**

The map has **50 rows and is already loaded**. Nothing needs to be added to it.
What is needed is that whatever string the client looks up must be one of:

```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
99 100 200
502 503 505 512 513 515 521 523 524 525 527 528 529 530 531 533 537
801 900 901 902 903 904 905 906 907 998
```

i.e. **one string per stage**, and the smallest candidate set for a Snowfield
mission battle is `"99"` (row 99 = 배틀 / *battle*, `PreFix STI099`) or `"0"`
(row 0 = 하얀숲 / *white forest*, `PreFix STI000`).

**Placement: none.** `PreFix` is consumed client-side; the environment key comes
from stage/combat data, not from a CDN package. Serving `LEVELING` over the CDN
would be fidelity work, not a fix (§2).

---

## 6. Not mine, but found and flagged

* **`[ERR] [RES] Can't find 'ST001' in ResMap.`** once per leg, same logcat, same
  second as the background failures (`23:29:47.335`). `ST001` is our fixture's
  invented `res_prefix`, and the client asked for it as a *resource entry name*.
  `BLUSTONE_RESOURCE_ASSET_NAMES` does fold `ST001` into the `E_NEW` tree, so this
  is a pkgi1 **entry-name registration** problem, not a missing file. Same log
  line also shows the replica resolves `res_prefix` art as a plain name — worth
  telling whoever owns `server-ts/src/bootstrap.ts`.
* **19th `PreFix` `STI801`** (row 801, Halloween) has no `ST801.jet` in this APK.
  Only relevant if a Halloween scene is ever reached.
* **`jet_decoder.py` is unreliable for enumeration**, as the tester reported
  (`analysis/r015/loadanim-diff.txt` and the brief both note it). My walker is
  committed as `tools/extract-jet-chunk.py` and validates each chunk's declared
  uncompressed size against the inflated length; all 21 `LEVELING.jet` chunks
  match. The u32 at chunk-header `+0x12` is **not** a plain CRC-32 of any
  variant I tested (`crc32(inflated)`, `crc32(compressed)`, `crc32(body)`,
  `adler32(inflated)`, `crc32c(inflated)` all differ) — recorded as unknown
  rather than used as a check.

## 7. Explicitly not resolved

* `[UNKNOWN]` the content of `*(std::string*)(X + 0x24)` on the episode path.
  **This is the blocking item.**
* `[UNKNOWN]` the values of the five suffix strings at `CSRStaticData+0x6c …
  +0x9c`. Device-observed values are `A`, `D`, `E`; two of the five
  `MakeBackground` calls produced no request at all in 5/5 legs, and I could not
  account for that from the disassembly.
* `[UNKNOWN]` whether entries named `STI000_A0`, `STI099_A0`, `STI900_A0` …
  exist in the PKGI1 name index. Entry names are not plaintext in any package, so
  a *hit* on a correct key has not been proven possible — only a miss has.
  **This is the risk that the fix may move the crash rather than remove it.**
* `[UNKNOWN]` how many layers `CSRGameScrollBGDraw::Load` should iterate. The
  observed per-letter iteration counts (~20 per leg) are **not** consistent with
  any real `ENV_INFO` row's `구성` values (111 / 11), which would give `_11` then
  `_1`. Do **not** read "a valid row was found" out of the iteration counts —
  they are part of the same garbage as the empty prefix.
* `[UNKNOWN]` whether the device took the `SRLoadRawDataStr` (asset tree) branch
  or the `CMCSVReader::Open` (CM database) branch of `LoadEnv`; the writer of
  `CGMDataMgr+0x5814` is still unknown, as `leveldata-id-source.md` records.
* `[INFERRED]` that the CM-database sweep was complete. LevelDB values are
  snappy-compressed; my scan of the `.db` files was plaintext-only (§4 row 8),
  so a CSV blob stored as a compressed LevelDB value in, say, `ETC.db` would
  not have been seen. The dumped tables in `analysis/recovered-data/leveldb-tables/`
  also show 0 hits. Given §2 and §3.1 — the file demonstrably loads — a hidden
  second copy is not needed to explain anything, but a hidden *newer* copy cannot
  be ruled out from here.

## 8. Raw evidence produced this session

| file | what |
|---|---|
| `tools/extract-jet-chunk.py` | new: verified `.jet` chunk walker / extractor (the `jet_decoder.py` replacement) |
| `analysis/recovered-data/environments.csv` | **[RECOVERED]** the file, byte-exact |
| `analysis/recovered-data/README.md` | provenance, format, placement answer. Also indexes the three pre-existing subdirectories (`cdn-manifest/`, `leveldb-tables/`, `native-key-vocabulary/`) and records that they contain 0 `environments`/`.csv` hits. |

Method notes for the next agent:

* `Ghidra address == ELF vaddr == file offset + 0x10000` re-verified here via
  `llvm-readelf -S` (`.text` at `0x612cc0`, `PT_LOAD#0` off=0 vaddr=0) and via
  `native-evidence.tsv` (`OnProcessMove` at `0x9dbe00`) vs `llvm-objdump`
  (`0x9cbe00`). To disassemble a Ghidra address with `llvm-objdump`, subtract
  `0x10000`. `llvm-objdump` is at
  `tools/android-sdk/ndk/29.0.14206865/toolchains/llvm/prebuilt/windows-x86_64/bin/llvm-objdump.exe`.
* `analysis/native-evidence.tsv` is in **Ghidra** address space;
  `llvm-objdump` and the `.so` file are in **ELF/file** space. Mixing them is how
  `scrollbg-crash.md` §0's `0xaaebd7` slip happened.
* Never attribute by nearest symbol: there are three `MakeStageInst`, two
  `LoadLevelData`, and `native-evidence.tsv` lists ~60 unimplemented stubs whose
  "addresses" are import slots.