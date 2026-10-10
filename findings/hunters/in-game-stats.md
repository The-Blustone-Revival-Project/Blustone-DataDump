# In-game stat oracle — what the running game actually displays

**Date:** 2026-10-03. **Lane:** in-game stat oracle (sub-agent).
**Device:** BlueStacks 5, `adb -s 127.0.0.1:5555`. Phone `RR8M60E30GW` never contacted.
**Owns:** adb, BlueStacks, the collector, the `:8080` dev-server process,
`analysis/in-game-stats/*`, this file.
**Did not touch:** `server-ts/` (read only), `tools/`, `instrumentation/`,
`analysis/ghidra-*`, `analysis/testing/*`, `analysis/catalogue/*`, other
`analysis/research/*`. No git. No Ghidra. No `pm install`, no data clear, no hand-edit of
`server-ts/data/state.json`.

Artefact index: **`analysis/in-game-stats/README.md`**.

---

## 0. Blunt answers first

| # | Question | Answer |
|---|---|---|
| 1 | Card stat screen? Exact tap sequence? | **It exists and is reachable — long-press a card. It aborts the process.** Sequence in §2. Crash is `CSRPopUpCardInfo::SetStatPanel` → `std::out_of_range: map::at: key not found`, reproduced **3/3**. |
| 2 | Numbers on card `001`? At what level/rank? | **The stat screen never renders, so no HP/ATK/DEF were read.** What *is* readable: `LV.1`, rank 1 (from the fixture), and a **`50`** under the portrait on both *Prepare for Battle* and the result screen — which I show is a **derived stat, not a stat field**. §3. |
| 3 | **872 vs 100?** | **The discrepancy does not exist. 872 was the PLAYER's HP.** The monster's HP is displayed **byte-for-byte as sent**. §4. This is a misattribution in `report-016` §1 and in `AGENTS.md` §16.1. |
| 4 | Other cards' stats? | **No.** The replica publishes one card, and the two routes to more (gacha, village roster) are dead ends for now — §5 documents exactly what each needs. |
| 5 | Other numbers | *Ally Teammates* / *Opponent Teammates* strengths, `enemy_total_hp_max`, `player_total_hp_max`, AP, gold, `Enemy HP` bar on the result screen, gacha costs. §6. |
| 6 | Screenshots | `analysis/in-game-stats/` — the load-bearing one is **`b1-06.png`**. |

---

## 1. Provenance and method

### 1.1 I did not edit `server-ts/`, so I ran a copy of it

Every A/B experiment needs the fixture to change, and `server-ts/` belongs to another agent.
Instead of editing it I copied the replica **outside the repo**:

```
C:\Users\shaha\AppData\Local\Temp\opencode\statprobe\
    src/           copy of server-ts/src   (EDITED freely, here only)
    data/          its own state.json copy (state-probe.json)
    node_modules/  a JUNCTION into the real server-ts/node_modules, read-only
```

`analysis/in-game-stats/start-statprobe.ps1` launches it on `:8080` with an env block copied
from `tools/start-server.ps1` (same 11 packages, same asset dir, same
`BLUSTONE_RESOURCE_VERSION=1634661`, `BLUSTONE_MISSION_START_IDEMPOTENCY_SECONDS=0`). Two
dials it does **not** inherit, both of which cost me one round each and are worth recording:

* **`BLUSTONE_CATALOG_PATH` must be set explicitly.** `catalog.ts` resolves it relative to
  `process.cwd()`, so with the copy as cwd it found nothing and served **9 routes instead of
  285**; the client then rendered the village with dead buttons and a `...` on the loading
  bar. **A "partially working client" that is really a 9-route server is a new failure mode
  worth naming.**
* **`NODE_OPTIONS=--require <tap.cjs>` must be built with forward slashes.** The
  PowerShell-quoted backslash form collapsed to `C:Usersshaha...` and node died in preload.
  (r017's tap does survive a plain backslash form; this is about `--require` specifically.)

The real `server-ts/data/state.json` was **never written by me** and never hand-edited; the
probe used its own copy. At the end of the round I ran `tools/stop-server.ps1` and
`tools/start-server.ps1`, and verified `/healthz` → 200 on the real replica.

### 1.1a One thing I broke and repaired — read this before using `ui-keys.py`

`plyvel.DB(path)` **opens LevelDB read/write and compacts on open.** Pointing it at
`instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db` — which is
outside my lane — silently **deleted seven `.ldb` files, rewrote `CURRENT`/`LOG`, and
wrote a new `MANIFEST-000114` + `000113.ldb`** in a tracked asset directory.

Repaired with `git checkout --` on that path plus removal of the two new files;
`git status --porcelain -- instrumentation` now shows **no tracked modification** (only a
pre-existing untracked `instrumented-seed-battle-en-delta-v1/`). The on-device copy the app
actually uses was never touched — the seed is unpacked at install time, not read at runtime.

`ui-keys.py` is now fixed to copy the DB to `%TEMP%` first and **must not be pointed at a
tracked directory**. It is presently *safe but not working*: with the pinned plyvel 1.5.1 it
now fails to open even the copy ("IO error: …/MANIFEST-000047"), although the same build
opened the in-repo directory directly. The 684/13 counts in §2.4 therefore come from a
**direct read of the pristine in-repo directory**, not from the copy path — anyone
re-deriving them must confirm their plyvel opens the copy before trusting a number.

### 1.2 Log slicing

Per `AGENTS.md` §16.7.5 every log claim here is sliced on a launch marker. The two crash
reports were taken with `adb logcat -c` immediately before the triggering gesture and the
`abort_message` line was read from that window only (`logcat-longpress-crash.txt`,
`35-longpress-plainname` round).

### 1.3 AP budget

Spent **3 AP total** (server `ap` 39 → 36), all on the enemy-HP leg and its control.
Everything else was free UI. **No `AP_EMPTY`.** No data clear, no state hand-edit.

---

## 2. The card stat screen: found, and it aborts

### 2.1 Exact tap sequence (0 AP, reproducible)

```
village
  tap (400, 660)     Airport building            -> Airport
  tap (540, 1450)    advance Isla's greeting
  tap (490, 1345)    "Well, to cruise, of course!"
  tap (635, 1035)    Snowfield area node
  # if you land on the chapter-shield map instead of the area map:
  tap (960, 550)     "Select Area"
  tap (640, 350)     Snowfield
  tap (490, 1620)    stage node                  -> "Prepare for Battle"
  tap (130, 720)     the ally card portrait      -> "Build Team"
  # OR, straight from Prepare for Battle:
  input swipe 131 721 131 721 900   # LONG-PRESS the ally card -> CSRPopUpCardInfo
```

`analysis/in-game-stats/battle-probe.ps1` runs everything up to *Prepare for Battle* in one
command. **0 AP.**

### 2.2 What happens: a reproducible process abort

```
F/libc : abort_message: assertion "terminating with uncaught exception of type
         std::out_of_range: map::at:  key not found" failed
E/BLUSTONE_ARM: candidate pc=0x4b85dc3 libnative_core.so
                symbol=_ZN16CSRPopUpCardInfo12SetStatPanelERK11CSRCardStat
I/ActivityManager: Process com.vshower.prd_sr.instrumented (pid …) has died
```

* **Crash site [recovered]:** `CSRPopUpCardInfo::SetStatPanel(CSRCardStat const&)` —
  ELF `0xb85dc3`, **Ghidra `0xb95dc3`** (ELF + `0x10000`, per §16.7.3).
* **Exception type [recovered], verbatim from libc++:** `std::out_of_range`,
  `map::at`, key not found. `_ZTISt12out_of_range` is on the candidate chain.
* **Signal:** `signal=6` (SIGABRT) with `ARM-PC`/`ARM-LR` both in `libc` — i.e.
  `std::terminate`, **an uncaught exception with no handler**, exactly the
  `type_error` class of failure §16.2 attributed to `wave_list`. There is **no
  `ASSERTION Failed` line** before it.
* **Reproduced 3/3**, on three different fixtures (§3.2).
* **The popup does open** — [inferred-strong]. `SetStatPanel` is a `CSRPopUpCardInfo` member,
  and the stack-scan candidate chain is heuristic (§16.7.4), so I am not claiming a true
  backtrace. But a long press on a card is the canonical "show card info" gesture and the
  symbol is unambiguous about which class of object was being populated.

**This is the answer to "where are the numbers *not* on screen": the game's own stat panel
is unreachable because it kills the process on open.**

### 2.3 Three server-side causes, falsified

I could not fix it, but I can say what it is **not**:

| # | Hypothesis | Probe | Result |
|---|---|---|---|
| A | `stat` is indexed by `(rank, level)` and our single row only covers rank 1 / no `level` | published **250 rows**, rank 1–5 × level 1–50, each with an explicit `level` field | **still aborts, identical exception** |
| B | the structure itself upset `SetCard` | **control:** 250 rows but rank1/level1 restored to the shipped baseline values | **no change** — card still loads, BP still `50` (§3.1). So A/B are cleanly separated |
| C | `base.name` is the token `"%user_name%"` and the panel does `map::at(name)` | `name: "Card One"` | **still aborts, identical exception** |

`_ZNK20CSRCardInfoContainer15GetCardStatDataERKNSt…EE jj` and
`_ZNK11CSRCardInfo7GetStatEjj` (both `unsigned, unsigned` = rank, level) are in the symbol
table, so hypothesis A was well founded — it is simply not the cause.

### 2.4 The likely cause is a **missing EN UI record**, not server data

Offline, free, read-only (`analysis/in-game-stats/ui-keys.py`, plyvel over the
`UI_XML_RO.db` *directory*):

```
instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db
    684 keys total
    13 keys match CARD / STAT / HUNTER / CHAR
    12 of those 13 are KO/ prefixed.  Exactly ONE has an EN alias:
        EN/NEW/SR_MISSION/3_SR_UI_MS_CF/1_SP_HUNTER
```

The KO-only records include what look like the stat-panel documents:

```
KO/SR_ENHANCE/3_SR_EN_CH/TR_STAT_POP          9882 bytes   <-- "stat pop-up"
KO/MIRAGE/MIRAGE_STAT                          6001
KO/SR_SHOP/HUNTER_SHOP                         4710
KO/SR_SHOP/HUNTER_SALE                         4983
KO/SR_SELECT/10GACHA_CARD                       6624
KO/SKIN/HUNTER_C / HUNTER_T                 555 / 1697
KO/SR_CHANGE/BOOK_CARD                          1707
```

**[inferred-strong]** A `map::at` inside a UI panel, failing on a database whose EN alias set
covers 1 of 13 relevant documents, is much better explained by a **missing UI document than
by missing card data** — and three server-side probes failing is consistent with that.

**Caveat, stated plainly:** this is correlation, not proof. It is falsifiable in one
Ghidra session by reading the `map::at` key in `SetStatPanel`, and that is the single
cheapest next step for whoever has the decompiler. Note also §7's hard-won lesson: a
wholesale KO→EN alias of this table reproduces the `DEFINE_COLOR` / `BuildColorTable`
assertion, so the fix is a **selective** EN copy of the card-popup records via
`tools/patch-ui-leveldb-selective.py`, and `EN/…/1_SP_HUNTER` proves selective aliasing of
this table *does* work today.

---

## 3. Numbers I actually read

### 3.1 Card `001` — what the UI shows today

`analysis/in-game-stats/b0-prep.png` (*Prepare for Battle*) and the r017 result screen:

| Readout | Value | Where |
|---|---|---|
| Card name/portrait | art `C001`, blonde rifleman in a blue cap | prep + battle |
| Level | **`LV.1`** | prep, result screen |
| Number under the portrait | **`50`** | prep, result screen |
| *Ally Teammates* | **`50`** | prep, *Build Team* ("Team Strength") |
| *Opponent Teammates* | **`1`** | prep |
| Team level | `Team Level 1` | result screen |
| AP | `38/50` | village, prep |

**The `50` is NOT a stat field — it is derived, and it moved when I changed the fixture.**
`analysis/in-game-stats/compare-prep.png` is the A/B:

| Fixture `stat[rank 1]` | Displayed |
|---|---|
| `hp 1000, atk 100, def 50, spd 100, hp_up 10` (shipped) | **`50`** |
| `hp 1001, atk 100, def 10, spd 100, hp_up 7` | **`0`** |
| `hp 1000, atk 100, def 50, spd 100, hp_up 10`, but 250 rows + explicit `level` (control) | **`50`** |

`50` with the shipped fixture is **`atk/2` and `def` and `hp/20` simultaneously** — one data
point cannot separate them, and the `0` in round 1 is non-monotonic in `def`
(`50→50` but `10→0`), which fits neither. **[UNKNOWN]** what the number is; it is *not*
worth more device time until someone decompiles the consumer. Two extra constraints worth
banking:

* it is a **client-side derivation**, not a server field (nothing we send is a plain `50`),
* it survives a 250-row `stat` table unchanged, so it reads **one** row, not an aggregate.

*Opponent Teammates = 1* for a monster with `hp 100, atk 10, def 5`: **[UNKNOWN]**, same
reason.

### 3.2 The monster — HP is displayed verbatim

This is the cleanest measurement in the round, and it is negative for the interesting
hypothesis. Full frame: **`analysis/in-game-stats/b1-06.png`**. Two bars, two different
quantities, routinely confused:

```
        ┌──────────────────────── wide top bar, bunny icon ─────────────────────────┐
        │                    250   x 10     (blue→yellow→red as it drops)          │
        └───────────────────────────────────────────────────────────────────────────┘
                                    ... fighters ...
              ┌── small green bar, bunny icon ──┐
              │              858                │
              └─────────────────────────────────┘
```

I changed only the monster fixture — `hp: "100"→"250"`, `atk: "10"→"44"`, `def: "5"→"33"`,
`hp_page: "100"→"777"` — and the **top bar tracked `hp` exactly**:

| Fixture `hp` | Top bar reads | `play_info.enemy_total_hp_max` |
|---|---|---|
| `"100"` (shipped) | **`100`** | `100.0` (r017) |
| `"250"` (probe) | **`250`** | **`250.0`** |

`analysis/in-game-stats/compare-enemybar.png` is the 2× zoom of both bars side by side.

**⇒ There is no level scaling, no rank multiplier, no party multiplication and no ×10 on
monster HP. `AddMonster`'s `hp` is the whole story. [recovered, 2/2 with a 2.5× change]**

I also confirmed the recovered multiplier tables are **not** applied on this path —
`analysis/in-game-stats/leveling-chunk09.json` (`LEVELING.jet` chunk 9):

```
rank_1 hp 2.6 atk 1.4 def 1.4 | rank_2 2.2 | rank_3 1.8 | rank_4 1.4 | rank_5 1.0
bomber  hp 0.85 atk 0.95 def 0.95 | support 0.80/0.95/1.00
atk_camp hp 2.0 atk 2.6 def 1.0 | def_camp hp 2.0 atk 2.6 def 1.0
```

Monster `M001` is `rank: 1, role: 1`, and `hp 100 × 2.6 = 260`, not the 250 on screen. So
either `rank`/`role` are not being applied (the catalogue's standing worry, §Monsters), or
they do not feed HP. **`LEVELING.jet` chunks 0 and 9–19 verified by extraction, as
instructed** — chunk 9 is the multiplier table above, chunk 19 is the 66-row
`power,rank,hyper,level` table, and chunk 1 (`leveling-chunk001.csv`, `2,100.0,10.0` …
`15,5.5,0.6`) is a *decreasing* level→cost table, **checked and rejected** as a stat
multiplier.

### 3.3 `play_info` from a real LOSS (first capture of a losing battle)

`analysis/in-game-stats/play-info-statprobe.txt`, probe fixture, `/mission/Complete` fired
**once**, 79 s in, on a loss:

```json
{"atk_cnt":0,"atk_total":0,"clear":0,"clear_time":79,"dead_cnt":1,
 "enemy_total_hp":250.0,"enemy_total_hp_max":250.0,"item_use":[],
 "player_total_hp":0.0,"player_total_hp_max":1010.0}
```

Three things this settles:

* **`/mission/Complete` fires on a loss too**, `clear: 0`, `dead_cnt: 1` — r017 only ever
  saw the win path (it used the exit door). `[recovered]`
* **`enemy_total_hp_max` = our `hp` verbatim.** r017 §4 flagged `enemy_total_hp: 0.0`
  against a visibly alive monster as unexplained; with `clear: 0` and a dead player it is
  simply correct, and `enemy_total_hp` reaching `0.0` is consistent with the *player* being
  the one at zero. The remaining oddity is only the r017 win case.
* **`player_total_hp_max` = `hp + hp_up`, additive, no multiplier.** Card `hp 1000 +
  hp_up 10 = 1010.0`. Now confirmed on **three** independent captures
  (r017 ×2 at 1010.0, this one at 1010.0). `[recovered]`

---

## 4. THE 872 QUESTION — answered

**`analysis/r016-02-BATTLE-SCENE-RENDERED.png` (the `872` frame) and r017's `935/892/870/138`
series are the small green bar with the bunny icon: the PLAYER's HP. The monster's HP is
the wide top bar.** `report-016` §1's "enemy HUD showing HP 872 for monster M001" and
`AGENTS.md` §16.1's framing of it as a 4× discrepancy are **wrong on both counts** — 872 is
a player HP reading, and the fixture's `hp: 100` is displayed as `100`.

Four independent lines of evidence, all on screen:

1. **The player's HP starts at the player's maximum.** Baseline series reads
   **1008** at the first sample (`series-enemyhp.png`) against a
   `player_total_hp_max` of `1010.0` — i.e. 2 points of damage already taken. The monster's
   bar read a flat `100`.
2. **The rate scales with the MONSTER's `atk`, not the player's.** Baseline
   (`monster atk 10`): 1008 → 782 over ~120 s ≈ **1.9 HP/s**. Probe
   (`monster atk 44`): 994 → 522 over ~110 s ≈ **6.2 HP/s**. Ratio **3.3×** for a 4.4×
   `atk` change. Damage *to the player* scaling with the enemy's attack is the only
   consistent reading; enemy HP draining because I raised the enemy's attack is nonsense.
3. **It matches the client's own telemetry exactly.** r017 leg 3 recorded the green bar at
   **138** at t+540 s and `play_info.player_total_hp: 136.0` at `clear_time 548`. Same
   quantity, 8 s apart. r017 leg 2's `player_total_hp: 916.0` at 59 s sits on the baseline
   curve.
4. **It is symmetric with `enemy_total_hp`.** In the probe the green bar ran down to **250**
   and the next frame is the **defeat screen** (`b1-120.png`,
   `analysis/in-game-stats/probe-recruit.png`'s predecessor): *the green bar is the thing
   that hit zero.*

**Consequences for the project, please action:**

* Strike the "872 vs 100, 4× discrepancy" line from `AGENTS.md` §16 and `report-016` §1.
  It is a misattribution, not an open question.
* **`enemy_total_hp_max` is not a mystery** — it is `AddMonster.hp` verbatim (§3.3).
* r017's remaining `enemy_total_hp: 0.0` on a *win* is the only live item, and it is much
  smaller than it looked: on a loss the same field is `250.0` and correct.
* **The result screen has a separate, explicitly labelled `Enemy HP` bar**
  (`b1-120.png`) that was full at the moment of the loss — so the game's own defeat screen
  agrees that the monster was untouched. The "enemy HP" that everyone has been reading is
  the player's.

### 4.1 One loose end I did not resolve

The top bar carries a right-hand `x NN` that reads **`x 100`** on the shipped fixture and
**`x 10`** on the probe (`compare-enemybar.png`). It is **not** `hp_page` (100→777), **not**
`atk` (10→44) and **not** `def` (5→33), and in the probe the glyphs stop short of the bar's
right edge, so it is not merely clipped. In the baseline run it never changed across 19
frames, and `atk_cnt`/`atk_total` were `0` in both battles, so a live counter is unlikely.
**[UNKNOWN]** — recorded rather than guessed.

**Correction, 2026-10-05:** The observations above are preserved, but the
historical exclusion of hp_page is retracted. Original native instructions
`0x9afeb2: strb.w r0,[r2,#0x8c]` and `0x99b396: ldrb r0,[r0,#0x8c]`
establish unsigned byte narrowing:777 becomes9. Consequently not displaying777
does not exclude hp_page. The probe changed four fields together; no suffix
equation, page/death lifecycle or original page distribution is proved. See
`stage-multipliers.md` §2 for the reconciled evidence. A choice of hp_page1
would be a local diagnostic fixture, not an original balance recovery.

---

## 5. Getting to the other 120 cards

Not achieved. What I established, precisely:

### 5.1 The roster has exactly one card, and that is the binding constraint

`CHAR_STR_RO.db` carries **121** card ids and the recovered pack **155** `C*` art packages
(`analysis/recovered-data/native-key-vocabulary/deck-and-arity.tsv`). *Build Team*
(`probe-rostercard.png`) lists exactly one card, so the client is showing us everything the
replica publishes. **The other 120 are a server-publication question, not a UI question.**

### 5.2 What would have to be published

For each card id `NNN`:

| Route | Keys | Status |
|---|---|---|
| `/reference/GetCard` | `ret_data[] = { base:{id, char_id, name, attr, role, res_prefix, cool_time, …}, thumb, stat:[…], equipment:[], skill:[], dialog:[] }`, one entry per card | shape **[recovered]**; values fixture |
| `/lobby/GetCardInven` | an **instance** per card: `inst_id, ref_id, rank, rank_up_cnt, exp, lock, weapon_rank/level, armor_rank/level, accessory_rank/level, skill_1..5_level, skin_ref_id` | shape **[recovered]** |
| `/lobby/Enter` | `ref_id_1..4` + `ref_id_leader`, `inst_id_*`, `rank_*`, `exp_*` in `partyProfile` | shape **[recovered]** |
| art | `res_prefix: "Cnnn"` **and** the package tree | `BLUSTONE_CARD_ART_GLOB='C0*.jet'` in `tools/start-server.ps1` already does the art side (~570 packs / 587 MB) |

`stat` needs one row per `(rank, level)` with `level` present — see §2.3 hypothesis A. That
is the one structural change I would insist on regardless of the `SetStatPanel` crash: the
250-row table changed nothing observable, which means the client is not iterating it, but a
real panel will have to index it.

**Caveat:** the stat panel aborts (§2), so publishing more cards today yields more portraits
in *Build Team* and **no new numbers**. Fixing §2.4 comes first.

### 5.3 Two dead ends, measured

* **The gacha screen is reachable and runs, but awards nothing.** Free path:
  defeat screen → **"Recruit New Hunter"** → *Recruit Hunters* (gacha). `Recruit 300`
  confirms, and the client issues a real
  `POST /shop/GachaPremium {"pvid":"1000001","cnt":"11"}` with the recovered key set
  `app_code, app_ver, bonus_level, cnt, gacha_type, item_inst_id, market, otp, pvid`,
  then `/gacha_period/GetInst` and `/shop/GetGachaEventRef2`. Response 398 B, gems stayed
  at **60K**, no card appeared. **[recovered] the request contract; [UNKNOWN] the result
  contract.** This is the cheapest route to more cards once someone shapes the response.
  (It also gave us the screen art for free — `probe-recruit.png`.)
* **The village HUD is inert.** `SHOP` (90,195), `EVENT` (90,375), the hamburger
  (117,1805), the chevron (537,1848), the **Mail** sprite (170,1390) and the **Supply**
  sprite were each tapped 2–3× with screenshots between, and **none produced any change or
  any HTTP request** (`probe-shop2.png`, `probe-mailgirl.png`, `probe-event.png`). The
  3D Airport works, and the mission map's 2D UI works fine (*Select Area*, *Preset*, the
  `+`). So it is **not** a coordinate problem and **not** a general 2D-UI problem — the
  village's own interactivity is missing data, most likely the building/NPC list in
  `/lobby/Enter`. **[recovered] as a behaviour; [UNKNOWN] as a cause.**

---

## 6. Other numbers the UI exposes

| Number | Value | Screen | Note |
|---|---|---|---|
| Player max HP | `1010` | `play_info` | = card `hp 1000 + hp_up 10`, additive, 3 captures |
| Player HP, live | `1008 → 782` (baseline), `994 → 250` (probe) | battle, green bar | the number `report-016` called enemy HP |
| Monster HP, live | `100` / `250` | battle, top bar | **verbatim `hp`** |
| `atk_total` | `0` on a loss | `play_info` | the player attacked **zero** times in 79 s |
| `clear` / `dead_cnt` | `0` / `1` | `play_info` | a loss completes normally |
| Gacha | `Recruit 30` (×10), `Recruit 300` (10+1, "at least ★3"), currencies `30000` + `30000`, holdings `0 / 0 / 60K` | Recruit Hunters | `Collect Hunter Traces` costs 1 magnifier, we hold 0 |
| `Enemy HP` bar | **full** at the moment of defeat | defeat screen | labelled explicitly; contradicts the "enemy was at 138" reading |
| Village AP / BP | `38/50`, `10/10` | village | |
| Team Level | `1` | result screen | |

---

## 7. Honest status table

| Claim | Status |
|---|---|
| A card stat screen exists and is opened by long-pressing a card | **[inferred-strong]** — `CSRPopUpCardInfo::SetStatPanel` is on the crash chain; the chain itself is a heuristic scan (§16.7.4) |
| It aborts, 3/3, with `std::out_of_range: map::at: key not found` | **[recovered]** — verbatim libc++ `abort_message` |
| Crash site `CSRPopUpCardInfo::SetStatPanel(CSRCardStat const&)`, ELF `0xb85dc3`, Ghidra `0xb95dc3` | **[recovered]** from `BLUSTONE_ARM` |
| `stat` coverage / `level` field / `base.name` token are **not** the cause | **[recovered]** — 3 falsifying probes |
| The likely cause is a missing EN UI document | **[inferred-strong]** — 12 of 13 relevant `UI_XML_RO` records are KO-only; falsifiable in one Ghidra session |
| **The monster's HP is displayed exactly as `AddMonster.hp` sends it** | **[recovered]** — 2/2 with a 2.5× change; `enemy_total_hp_max` agrees |
| **872 was the player's HP; there is no 872-vs-100 discrepancy** | **[recovered-strong]** — 4 independent lines, §4 |
| `LEVELING.jet` rank/role multipliers are **not** applied to M001's HP | **[recovered]** — 250 shown, 260 predicted |
| Player max HP = `hp + hp_up`, additive | **[recovered]** — 3 captures |
| `/mission/Complete` fires on a loss (`clear: 0`, `dead_cnt: 1`), once | **[recovered]** |
| Card `001` HP / ATK / DEF | **NOT OBTAINED** — the panel aborts |
| The `50` under the card portrait | **[recovered] as an observation, [UNKNOWN] as a quantity** |
| `x NN` on the enemy bar | **[UNKNOWN]** |
| *Opponent Teammates* = 1 | **[UNKNOWN]** |
| Village HUD inert | **[recovered] as behaviour, [UNKNOWN] as cause** |
| `/shop/GachaPremium` request contract | **[recovered]** — 9 keys, `cnt: "11"` |
| Gacha result contract | **[UNKNOWN]** — 398 B response, nothing granted |
| Everything in `compare-prep.png` round 1 vs 2 | **[local fixture]** by construction |

---

## 8. Recommended next steps, cheapest first

1. **Decompile `CSRPopUpCardInfo::SetStatPanel` (Ghidra `0xb95dc3`) and read the `map::at`
   key.** One function settles §2.4, and with it the largest remaining "where are the
   numbers" question in the project. If the key is a `KO/…` UI document, the fix is a
   selective EN copy via `tools/patch-ui-leveldb-selective.py` — and
   `EN/NEW/SR_MISSION/3_SR_UI_MS_CF/1_SP_HUNTER` proves selective aliasing of that table
   already works.
2. **Correct `AGENTS.md` §16.1 and `report-016` §1.** The 872-vs-100 framing should be
   replaced with §4. It is actively misleading: it invites someone to go hunting for a
   monster-HP scaling rule that does not exist.
3. **Shape `/shop/GachaPremium`'s response** so a recruit actually awards a card. That is
   the only in-game route to a second card id, and the request contract is already recovered.
4. **Find why `/lobby/Enter`'s village data yields no clickable buildings or NPCs.** It
   costs nothing to fix and it is the difference between a village and a screenshot.
5. Only then publish the roster. Publishing 121 cards before (1) buys portraits, not numbers.

## 9. What I did **not** do

* No `server-ts/` edit. The A/B rig is a copy outside the repo (§1.1); the real tree is
  byte-unchanged and the real replica is back up on `:8080` (verified `/healthz` 200).
* No hand-edit of `server-ts/data/state.json`; the probe used its own copy. Final state:
  server `ap = 36`, client HUD **`37/50`** (`99-final-rig-state.png`) — i.e. a **+1**
  client-over-server offset. r017 §8 measured **+2** twice, so the offset is **not stable**
  and r017's "reproducible +2" should be softened. I did not investigate it further.
* No data clear, no reinstall, no `pm install -r`, no `pm install` at all.
* No Ghidra, no git, no `analysis/testing/*`, no `analysis/catalogue/*`, no other
  `analysis/research/*`.
* Phone `RR8M60E30GW` never contacted. Every adb call carried `-s 127.0.0.1:5555`.
* I did **not** press `Retry` (costs AP, teaches little), did not chase `x NN`, and did not
  try to make the monster die.
* I did not confirm the popup actually *paints* before it aborts — the candidate chain is a
  stack scan, not a backtrace, and I am not claiming more than the symbol supports.
