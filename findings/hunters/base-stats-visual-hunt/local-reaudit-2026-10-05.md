# Local evidence re-audit — 2026-10-05

Lane: re-audit local BLUSTONE evidence for missed stat tables.
Scope per task: `analysis/VSFan/` (workbook, 220 images, 3 resource sets incl. APK 1.4.4.1, 5 pcaps),
`analysis/extracted/assets/EQUIP.jet`, `LEVELING.jet`, phone snapshot reference manifest,
catalog JSONs, 774-package JET scan.

Method: read-only. JET checks used the repo decoder (`tools/jet-viewer/jet_decoder.py`,
`inspect_bytes`) with summary-only output (counts/mime kinds/short text heads, no binary dumps,
no writes to sources). Workbook recount used `openpyxl` read-only against the original xlsx.
Prior reports were re-read, not re-derived: `vsfan-material-index.md`, `vsfan-research-material.md`,
`vsfan-extracted-assets.md`, `vsfan-packet-capture-findings.md`, `vsfan-visual-audio-material.md`,
`base-stats-visual-hunt/README.md`, `coverage.md`, `environments-recovery.md`.
No server/APK/state changes. (Note: `openpyxl` was installed into `tools/python-venv` to run the
read-only recount; that is gitignored tooling, not repo content.)

## 1. VSFan workbook — independent recount, still polluted

File: `analysis/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx` (untouched).
Raw TSV already kept at `analysis/research/vsfan-hunter-stats-raw.tsv` (36,691 B) plus
`vsfan-hunter-details-raw.tsv` (6,129 B).

Recount from the original (this lane, read-only):
- Sheets: `Details`, `Stats`. `Stats` header: Hunter/Strength/Life/Attack/Defense/Att Spd/
  CD Chance/Crit Dmg/Arm. Pen/Block Chance/Block Res/Str Elem Attr/Elem Att Res/Life Regen.
- 208 data rows = 19 hero-name rows + 189 rank-label rows. Names in order: Lapis, Denali,
  Rebecca, Metis, Locke, Balian, Hecate, Sienna, Bruce Bang, Sylvester, Sunny, Robin,
  Lantern, Captain, Gerard, Karl Steiner, Levi, Riko, Acerola.
- Rank rows: **67 fully numeric / 22 all-`N/A` / 100 fully blank** — matches the prior report exactly.
- `- Base Bronze` per hero: **10 numeric** (Lapis, Metis, Locke, Balian, Hecate, Sienna,
  Bruce Bang, Sylvester, Robin, Captain) and **9 all-`N/A`**
  (Denali, Rebecca, Sunny, Lantern, Gerard, Karl Steiner, Levi, Riko, Acerola).
- `Details`: 31 rows (header + 30 named heroes with title/role/type/skills); metadata only.
- The archive has no `docProps/core.xml` (KeyError on read); no author/timestamp harvested
  from that path. The prior report's `openpyxl`-dated-metadata caution stands regardless.

Verdict: counts confirmed, **zero strict coverage**. No source, capture date/build, level
definition, equipment/enhancement state, or rank-label semantics. The 10 numeric Base Bronze
tuples remain polluted rebalance candidates only. Do NOT promote the 67 numeric rows.

## 2. VSFan 220 curated images — no stat panels

`analysis/VSFan/Images` contains exactly **220 files** (recount matches manifest).
Manifest: `analysis/research/vsfan-image-manifest.tsv` (30,558 B), including two exact
duplicate-file pairs (metron_fragment, lana). Per `vsfan-visual-audio-material.md`:
portraits/emoji/items/locations/NPCs are art/identity assets; the six full-screen captures
are UI/economy snapshots (energy/fuel/balances/progress/recruit labels), not HP/ATK/DEF
tuples or item-instance values. No new rows; identity-only value preserved.

## 3. VSFan three resource sets + APK 1.4.4.1 — no stat tables

- Trees: `1.1.2.0 (blustone.pcap, 2017-09-04)`, `1.1.3.0 (bs_transcendence.pcap, 2017-09-08)`,
  `1441 (APK)`; root APK `com-vshower-prd-sr-1441-*.apk` (1.4.4.1, per prior SHA record).
- `1441 (APK)/` top-level dirs: character art/effect/sound families, DIALTU-EN/JP/KO/ZH/ZT
  (17 files each — TalkerMaker dialogue, identity leads only), MOTION (2 JSONs), UI_CSV
  (help/navigation/strings/sound/filter), monster art M001/M002/M005/M006/M008/M009/M100,
  stage/background/UI packages.
- Text-bearing files under `1441 (APK)/` are dialogue JSONs, 2 motion JSONs, and UI_CSV
  help/strings — **no file with a card/stat/item/monster/level/equip/gem/jewel name match**
  in JSON/CSV/TXT across the extracted tree (bounded filename sweep, zero hits).
- `UI_CSV/3d98d128.json` help: stat-field *definitions* and the 12-family jewel set-bonus
  table (`CONTENTS11_8`) — historical mechanics, one locale conflict (Super Block 9% KO vs
  5% elsewhere). No per-hero tuples, no per-item rows. Stays as historical set-bonus
  evidence, not instance stats.
- `LEVELING/6a434cb8.bin` (39 B) and `6c1781a5.bin` (195 B): opaque binary sidecars in the
  extracted view; not decoded in any pass (names/bytes only, no stat claim).
- `M001/` directory: PNG art frames only (35 files sampled); no stat records.

## 4. Five PCAPs — protocol map only, bodies encrypted

`analysis/VSFan/Packet Captures/`: `blustone.pcap` (128,731,909 B), `bs_transcendence.pcap`
(54,929,150 B), `btba_install.pcap` (21,496,355 B), `btba.pcap` (1,102,501 B),
`whiteisland.pcap` (96,353,113 B). Per `vsfan-packet-capture-findings.md`: the two Blustone
captures expose reference/lobby/mission *route names* (`GetCard`, `GetLevel`, `GetItem`,
`GetMonster`, `GetStageMonster`, etc.) with encrypted `application/octet-stream` bodies;
BTBA-install is a separate product flow; `btba.pcap`/`whiteisland.pcap` are TLS-only.
No readable card/item/monster values; no session keys. Zero coverage credit.

## 5. EQUIP.jet — re-verified texture-only

`analysis/extracted/assets/EQUIP.jet` (165,028 B), `inspect_bytes` this lane:
- 24 media resources, **all `image/png`**; `textResources: []`; concatenated text length 0.
- 609 printable strings are short texture/atlas noise (e.g. `a0rL`, `Gk}V`), not a table.
Negative result confirmed: no `textResources`, no readable equipment-stat table.

## 6. LEVELING.jet — shared tuning only, no per-entity rows

`analysis/extracted/assets/LEVELING.jet` (18,524 B), `inspect_bytes` this lane:
- kind `multi-resource JET`, `resourceCount: 21`, media 0, **20 textResources**.
- Payload heads (first 150 chars each): scene/init key table (`BeforeAppInit…pv` IDs);
  Korean upgrade curve (`2,100.0,10.0…`); skill/battle tuning JSONs; `#ID,Name,PreFix,…`
  environment CSV; position/mouse/packet/elem-bonus configs; `power,rank,hyper,level`
  threshold curve; death-box layout. Generic HP/ATK/DEF appear as shared parameters,
  never as per-hero or per-monster tuples; no per-item equipment/jewel/accessory rows.
Consistent with the prior audit and the 774-package scan (§8).

## 7. Phone snapshot reference manifest — 8 tables, none is card/item/monster

`analysis/recovered-reference/manifest.json` exports exactly: CHAR_STR (1,033 records),
INGAME_TALK (231), SKILL_DESC (5), SKILL_EFFECT (230), SKILL_REF (1,070), SKILL_TAG (565),
TAG_REF (142), UI_EPISODE (297). Character strings, skill/effect/tag tables, talk, episode UI.
No card, item, or monster reference table. Negative result stands.

## 8. Catalog JSONs — descriptive/art inventory, not stats

- `analysis/catalogue/data/cards.json`: 121 rows; sampled rows (`001` Lantern, `002` Mowgli)
  carry title/name/rarity/role/element/gender/race/VA/portrait/summary/weapon prose —
  descriptive metadata, no HP/ATK/DEF battle rows.
- `analysis/catalogue/data/monsters.json`: 22 rows; sampled `M001` is `{monster_id, art,
  bytes_total}` — art/byte inventory, no HP/ATK/DEF.
- `card-catalogue.tsv` supplies the 113-real-hero denominator (121 rows minus 8 non-card rows).

## 9. 774-package JET scan — one shared CSV, no per-card/item rows

Per `environments-recovery.md` §§4/7: an independent chunk walker over all 774 base-APK
jets (and the byte-identical phone tree, 0 unique filenames either way) found exactly one
18-column CSV — `LEVELING.jet` chunk 5 (`environments.csv`, environment/scroll-speed table)
— plus small config curves (`LEVELING` c1/c19, UI_CSV IAP/ISO/sound) and binary false
positives. No per-card or per-item rows in either tree. This lane did not re-run the full
774-file walk (prior byte-identical result stands); EQUIP/LEVELING spot decodes above are
consistent with it.

## Outcome

- **New strict rows: none.** No missed card/item/monster table found in any lane asset.
- **New polluted rows: none** — the recount confirms (not extends) the already-ledgered
  workbook material (10 numeric Base Bronze candidates + 9 N/A rows, 67 numeric rank rows
  total, Details skill index) and existing HUD/archive observations.
- Coverage unchanged: heroes **1/113**, jewel set bonuses **12/12 historical families**
  (Super Block locale dispute preserved), mounted-jewel samples 6/6, accessories **1/100**,
  monsters **0/22**.
- All sources left untouched; only reads performed. Prior quarantines hold: never promote
  VSFan xlsx rows, never derive hero HP/ATK/DEF from LEVELING shared multipliers, never
  count cross-title MON BLAST! cards or HUD tokens as base stats.
