# Monster full-HP hunt lane log — 2026-10-05

**Lane:** Find full-to-empty bar sequences for ONE identified enemy (same
sprite/stage/wave), full-length bar openers, boss intro cards with names, and
`M001`–`M021`/`M100` mappings from stage data. Current-bar NEVER equals base;
a tuple needs identity + max-HP proof + ATK/DEF. MON BLAST! stays
cross-title. Monster strict coverage stays **0/22** — nothing below claims it.

## 1. Videos checked this pass

| # | Source | Method | Result |
|---|---|---|---|
| 1 | P J `Ot72M6h4OUI` (Giants' Shelter 46–50, 2017-05-16) | Direct visual re-read of all three saved local contact sheets (`Ot72M6h4OUI-contact-1/2/3.jpg`) by the lane agent, not relying on the prior transcription | All 16 previously logged bar tokens re-verified legible at their frames; three candidate depletion runs identified ( §2). No boss intro/name card; no `M`-ID mapping |
| 2 | Web search: EN gameplay/boss queries (`Blustone gameplay battle boss`, `Blustone 2 official promo battle`, `Blustone mid guard north garden boss`) | Search-result text/thumbnails | Surfaced only already-known clips (P J, CGPMobile, promo `i7IChnEylvk`), store listings, and unrelated-game collisions. No new attributable PvE boss video opened |
| 3 | Web search: KO queries (`거인의 쉼터 전투 영상 보스 공략`, `탐험 전투 보스 체력`, `헌터 수색 던전 영상`) | Search-result text | Namu mechanics text (10 stages/area, role/element descriptions) and unrelated-game guides; no enemy stat panel or new video |
| 4 | `Blustone 2 First Look!` / `My First Legendary Selection Request!` / `20+ Hunters Recruiting!` / `A Beyond The Bounds Story Part 1` (YouTube IDs `apR69H_bjXo`, `vOjXM4xcSiA`, `cnMBlXFd5W4`, `1ZUcs0HAnGc`) | Search metadata only; players not opened (YouTube page fetch returns chrome only, no inspectable frames in this lane) | Titles/descriptions indicate recruitment/progress content, not enemy-stat panels. Retained as uninspected leads, no values inferred |
| 5 | BLUSTONE Wiki (Fandom) monster/enemy list | Page fetch + targeted search | Page fetch 403; follow-up search returned only unrelated-game monster wikis. No Blustone monster HP/ATK source found |

Prior lanes already swept Korean/Japanese/English YouTube, Bilibili story/PvP
clips, and image search with negative results; those videos were NOT re-opened.

## 2. Candidate full-to-empty runs in the P J contact sheets (polluted track only)

All frames are 15 s samples — sampling alone cannot prove no wave change
between frames, and no frame shows a monster name or `M`-ID. Each run is
therefore a **candidate**, never max-HP proof.

### Run A (strongest): t=390 s → 405 s → 420 s → 435 s — 4,373 → 3,126 → 1,376 → 134

- Same icy Giants' Shelter backdrop, same brown-rifleman frontline, same
  red spiky/blob enemy sprite across t=390/405/420; bar monotonically
  decreases with consistent ~26/hit floating damage (26/21, 26/26, 26).
- t=390's bar renders full-length red, and the preceding t=330 frame shows an
  empty field (white-haired hunter, no enemy bar), so the t=390 enemy is plausibly
  near-full — but "plausibly near-full" is not a max-HP demonstration, and the
  t=435 frame goes dark with a different-looking blue spiky enemy (wave
  transition), breaking same-instance continuity at the tail.
- Identity, stage sub-wave, difficulty, ATK/DEF all unknown. No coverage credit.

### Run B: t=195 s → 210 s — 2,858 → 1,556

- Same darker-ice backdrop, same rifleman frontline, same green/yellow spiky
  enemy, decreasing bar. Same 15 s-continuity and identity caveats as Run A.
  No coverage credit.

### Run C: t=90 s → 105 s — 1,253 → 8

- Same backdrop/frontline, small fire enemy; t=105's bar is nearly empty (near-kill
  current reading). Consistent with one enemy dying, but the kill frame and any
  wave hand-off between samples are unobserved. No coverage credit.

### Negative results from the same sheets

- **No boss intro card with a name** appears in any of the 45 sampled frames.
  The t=675 dark-boss scene (2,685, red demon boss) follows a Captain skill
  cinematic at t=660, and the t=645 full-length bar (6,042) sits in a different
  backdrop — 6,042 → 2,685 is explicitly NOT one enemy (backdrop, party, and
  enemy all change).
- t=525 (5,321) → t=540 (3,682) changes the frontline hunter
  (rifleman → white-haired girl), so party exchange or a new wave breaks
  same-instance continuity.
- Wave dots sit atop most battle frames but are illegible at contact-sheet
  resolution and are not mapped per token.

## 3. Stage-data `M`-ID mapping (negative)

- `analysis/recovered-data/campaign-stages.csv` (50 recovered stages) has
  columns `stage,area,serial,global,cmge,pv` only — **no monster column**. There
  is no original stage→monster mapping in local evidence.
- `server-ts` serves fixture `FIXTURE_MONSTER_IDS` (default `["M001"]`) for every
  linked stage; `ref_id`/`show_thumbnail` are replica fixtures, not recovered
  per-stage enemy data. Do not cite them as original mappings.
- Catalog `analysis/catalogue/data/monsters.json` records art/byte inventory
  (`M001.jet`…`M021.jet`, `M100.jet`) with zero numeric stats.

## 4. Local-source scripted Episode monster STAT table (major caveat — parent to adjudicate)

`analysis/recovered-reference/EPISODE_STAT_ACTORS.json` (exported from original
`R_EPISODE.jet`, SHA `7f4362cd…`, see `EPISODE_COMBAT_STAT.manifest.json`)
contains **37 monster-like actor rows** with fixed HP/ATK/DEF + rank, joined to
per-appearance level/attr/skill context in `EPISODE_COMBAT_CB*.json`
(`thumb: {level, rank, hyper, attr}`, `skill: [...]`). **[2026-10-06: the `37` is
an incomplete monster partition — `34 M* + 3 C010` omits 5 more `C*`-namespace rows
that are `type: "monster"` (`CB1102_006/_008/_011/_018/_019`); exhaustive count is
**42**. Every row transcribed below is an `M*`/enemy-`C010` row, so no figure in
this file changes.]** Selected rows
(`id | res | hp | atk | def | rank`):

| Actor | res | HP | ATK | DEF | Rank |
|---|---|---:|---:|---:|---:|
| CB0001_M01 | M001 | 150 | 130 | 100 | 1 |
| CB0001_BOSS | M040 | 400 | 190 | 100 | 1 |
| CB0002_M01 | M034 | 100 | 100 | 100 | 1 |
| CB0102_M1 | M022 | 450 | 430 | 180 | 1 |
| CB0201_M1 | M023 | 700 | 400 | 130 | 2 |
| CB0301_M1 | M023 | 700 | 650 | 160 | 2 |
| CB0202_M1/M2/M3 | M050/M049/M051 | 800 | 680–700 | 160 | 2 |
| CB0202_BOSS | M062 | 1,800 | 750 | 160 | 3 |
| CB0501_M1..M4 | M046/M052/M048/M054 | 1,000 | 1,200 | 180 | 3 |
| CB0501_BOSS | M062 | 2,000 | 1,500 | 210 | 4 |
| CB0602_M1 | M024 | 2,500 | 1,800 | 200 | 4 |
| CB0702_M1 | M058 | 2,400 | 2,600 | 200 | 4 |
| EVCB0102_M1/M2 | M035/M036 | 3,000 | 3,500 | 200 | 4 |
| CB1002_M1/M2 | M035/M036 | 5,500 | 4,500 | 280 | 5 |
| CB1002_M3 | M034 | 13,000 | 5,500 | 280 | 5 |
| CB1501_M1/M2 | M034/M035 | 7,000 | 6,800 | 280 | 5 |
| CB1301_M1/M2/M3 | M035/M036/M034 | 7,000/7,000/16,000 | 6,000/6,000/7,000 | 300 | 5 |
| CB1201_M1/M2/M3 | M041/M040/M042 | 6,500 | 6,000 | 300 | 5 |
| CB1201_BOSS | M100 | 16,000 | 7,000 | 300 | 5 |
| CB1401_BOSS | M100 | 20,000 | 8,000 | 280 | 5 |
| EVCB0301_M044/M057 | M044/M057 | 5,000/4,000 | 4,000/4,500 | 250/200 | 5 |
| CB0002/0003/0004_BOSS | C010 (Vincent ref) | 1,000/2,000/2,000 | 100/140/120 | 250/200/160 | 4 |

Why this is **not** claimed as monster coverage:

1. The export manifest itself labels the table **"Episode-only actor STAT
   table; not ordinary hunter card-base stats"** — the same scoping applies to
   ordinary stage-enemy base stats (§91/97: scripted story context).
2. Values are **per-appearance scripted tuning, not one base tuple per
   monster**: M034 reads 100 (CB0002) / 7,000 (CB1501) / 13,000 (CB1002) /
   16,000 (CB1301); M035 reads 3,000 / 5,500 / 7,000; M100 reads
   16,000/7,000/300 vs 20,000/8,000/280. A base-stat claim would need to explain
   this variance, which currently reads as per-combat difficulty scripting.
3. Most `res` IDs (M022–M062) lie **outside the 22-catalog** (`M001`–`M021`,
   `M100`); only M001 and M100 intersect it, and M040 does not.
4. No battle video ties any of these fixed HP values to an observed full bar,
   and native Episode combat rendering remains unverified.

Preserved here as source-backed, identity-tied HP/ATK/DEF material for future
rebalance/scaling analysis — the first local evidence class that pairs enemy
identity with all three numbers — with **zero change to 0/22** pending parent
adjudication on whether scripted per-appearance rows can ever satisfy the
base-tuple definition.

## 5. MON BLAST! guardrail

Snowfox 17,370/790, Pandahawk 17,460/1,110, Moonwoof 18,080/850 (all Gold Card
Lv.10 MAX) remain in `cross-title-mon-blast.md` only. Nothing merged.

## 6. Files updated

- `analysis/research/base-stats-visual-hunt/monster-fullhp-2026-10-05.md`
  (this lane log — new file).
- `analysis/research/base-stats-visual-hunt/monster-hud-observations.md` —
  appended §"Candidate depletion runs" (Run A/B/C + negative results); no new
  numeric tokens (all 16 prior tokens re-verified, none added).

## 7. Coverage effect

None. Monster strict coverage remains **0/22**. The three runs are polluted
current-bar candidates; the Episode STAT table is scripted per-appearance data
awaiting a coverage-definition ruling. No server/APK changes were made.
