# The expedition map's black backdrop — `resource_id` is ART, not an environment id

**Status 2026-10-03 · resource-serving agent · supersedes nothing, but corrects
the working assumption in AGENTS.md §16.6 item 3.**

## 1. The symptom

On the expedition map ("Snowfield") the snow particle layer draws and
**everything beneath it is pure black**. Once per session, ~40 s before the
battle:

```
[ERR] [RES] Can't find 'ST001' in ResMap.
[ERR] [RES] LoadAnim2 'ST001' failure
[ERR] [LoadAnim] Cannot find the resource(ST001)
[WRN] [OnPlay] Cannot play the node,itrdon't have A resource of image
```

`analysis/r015/logcat-all.txt`, lines **20620, 65586, 109593, 157904, 206015** —
**5 of 5 legs**, byte-identical.

## 2. The hypothesis I was given, and why it is WRONG

The brief was: this is the same namespace confusion that crashed the battle.
`starterAreas` published `resource_id: FIXTURE_STAGE_ASSET_PREFIX = "ST001"`,
`CSRGameBase::InitBackground` reads a `res_prefix`/`resource_id` and uses it as the
key into the `environments.csv` table, `find()`'s `end()` is never tested, so
publish an environment id (`"99"`). Four independent lines of evidence refute
that, and **publishing `99` here would have produced
`[ERR] [RES] Can't find '99' in ResMap.` instead** — the same black screen from
the opposite direction.

### 2.1 The environment table has exactly three callers and `SetArea` is not one

`CSRGameBase::OnInitBackground` (**0x9cbf34**) is the *single* reader of the
`std::map<string, CSRStaticData::ENV_INFO>` at `CSRStaticData+0x150`
(`analysis/ghidra-scrollbg-16-decomp-initbackground.txt`, `find<basic_string>`
at `iVar7+0x150`, then reads `node+0x34` = `ENV_INFO.PreFix`). Its callers:

| caller | where the key comes from |
|---|---|
| `CSRGameBase::InitBackground` (**0x9cbe8c**) | `GetStageData(this+0x220)` → `stage+0x70` = the **stage's** `res_prefix`, else the stage id |
| `CSRSceneMEpisode::InitBackground` (**0xb23e80**) | `*(std::string*)(X + 0x24)` where `X` is `CSRMEpisode::GetCombat()`'s `COMBAT` — a **local JSON resource**, not a server route |
| `CSRExploreMirage::InitBackground` (**0x926778**) | the mirage override; the only one that *does* test `end()` and log `Cannot find environment Information(ID:%s)` |

`CSRGameStage::SetArea` (**0xa28108**) appears in none of them. Its recovered
field set is 27 literals (`analysis/ghidra-setstage-exact.txt`, lines 30–57) and
**contains no environment field at all** — `id, type, serial, level_limit, title,
desc, dialog_id, resource_id, explore_id, stage[]`, `achieve_reward[]`. So does
`SetStage`'s 22 (`res_prefix` is the selector there).

### 2.2 The log signature is an ART miss, and it is a *different* signature from the environment miss

| | environment miss | this miss |
|---|---|---|
| format string | `CMFormat("%s_%s", PreFix, suffix)` with `PreFix == ""` | `Can't find '%s' in ResMap.` |
| literal | — | `0x01d999cb`, `CRMResMap::GetResInfo` (0x0011d126) |
| names produced | **prefixless**: `_A0.._A9`, `_D0.._D9`, `_E0.._E9` | the string as published: `ST001` |
| when | the **battle**, ~40 s later | the **map**, 40 s earlier |

Both appear in the same r015 leg, and they are 34–40 s apart. The prefixless
burst (`_D0` at 23:30:26.997, `_A0`, `_E0`) is the defect that commit `8dc5bfd`
fixed with `res_prefix: "99"`. **That fix is correct and complete for the stage.
It has nothing to do with `ST001`.**

### 2.3 The consumer is `CSRSceneMStageMap::CreateArea`, and the load lands in the right slot

`CSRSceneMStageMap` is the expedition-map scene (`analysis/native-evidence.tsv`
lines 20697–20742: `OnInit` 0xe912ac, `LoadView` 0xe91694, **`CreateArea`
0xe91f0c**, `SetGauge` 0xe993f0, `ShowReward` 0xe9413c, `SetRewardVisible`
0xe95eb8, `SetClearRewardThumb` 0xe95f00, `PopUpClearReward` 0xe964e0,
`SelectStage` 0xe98db8, `ChangeMap` 0xe9a75c).

`tools/resolve-literals-offline.py --function e91f0c:e93980`:

```
ldr@0x00e9205e -> 'PA_MAP_RD_%d'      ldr@0x00e92490 -> 'SR_SNOW'
ldr@0x00e920ca -> 'PA_MAP_SP_%d'      ldr@0x00e924d0 -> 'SR_SNOW'
ldr@0x00e92136 -> 'PA_MAP_EV_%d'      ldr@0x00e9268e -> 'PA_SHADOW'
ldr@0x00e921d6 -> 'PA_MAP%d'          ldr@0x00e92698 -> 'SHADOW_ANI1'
ldr@0x00e9222c -> 'PA_BG'             ldr@0x00e926be -> 'SHADOW_ANI2'
```

`PA_MAP%d` and `PA_BG` are **UI node names, not art names**. The recovered
layout record `KO/NEW/SR_MISSION/2_SR_UI_MS_ST/1_MS_ST_MAP` (83 432 bytes,
`analysis/recovered-data/leveldb-tables/all-tables.json`) is the proof:

* 51 panels `PA_MAP0 … PA_MAP50`, each wrapping an **empty**
  `<relative-coord><panel name="PA_BG" size="screen, screen"/></relative-coord>`;
* `RE_MK0 … RE_MK9` marker rects per panel (positions differ per map — the
  chapter layout);
* `PA_MAP_EV_%d`, `PA_MAP_RD_%d`, `PA_MAP_SP_%d` panels;
* `PA_SHADOW` with a 25 s pan `trans trl="-1050, 1500/2, 0"` — the map scroll;
* **exactly one** `res-name` in the whole document: `ST_SHADOW`.

So the backdrop image is filled in **by code**, into an empty panel, and the
only data-driven string on an `AREA_INFO` is `resource_id`.

**The timing pins it.** r015 leg 5:

```
23:47:43.294  [ERR] [RES] Can't find 'ST001' in ResMap.
23:47:43.307  [RSM] 'SR_SNOW01'(0x9de69a00), type:10 is registered.
```

13 ms apart, and `SR_SNOW` (0xe92490) is the *only* function in the library
that loads it — `CreateArea`. So the miss sits between `FindByName("PA_BG")`
(0xe9222c) and the snow load (0xe92490), which is exactly where the backdrop
image load must be.

### 2.4 One miss, not seventeen — so it is not the stage `thumb`

`thumb` is a **per-stage** field; the fixture publishes 17 stages
(`PAD_NODE_IDS` N001–N013 + N500–N502, plus `n_01_01`), all with
`thumb: "ST001"`. `resource_id` is **per-area** and exactly one area (`n_01`)
is on screen. The log shows **one** miss per session. A per-stage field would
have produced up to 17 (or 3 visible nodes). This is the cleanest single
discriminator, and it is also why the bug was never attributed: **the fixture
published the same constant `"ST001"` into both fields**, so the log could not
say which one missed.

## 3. **Explicit answer: does `resource_id` do double duty as an art name?**

**It does double duty — but both duties are ART, not environment.** Concretely:

* `resource_id` = the mission-map backdrop **art name**. ✔ (this report)
* It is **not** an `environments.csv` key. ✘ (refuted, §2.1–2.2)
* It is **not** a `PreFix` value (`STI000`/`STI099`/…). ✘ — those are the
  battle-backdrop layer prefixes and belong to the `res_prefix` path.
* The **battle** `res_prefix` is the environment id. It and `resource_id` are
  **two different fields in two different tables** (`STAGE_INFO` vs `AREA_INFO`),
  read by two different functions, feeding two different maps.

So the risk is the reverse of what the brief feared: changing `resource_id` to an
environment id would have **broken the art**, not fixed it. That is why the fix
is `MAP_ZONE_1` and why `assertAreaBackdropArt` refuses both wrong shapes at
boot.

## 4. The fix

### 4.1 The value: `MAP_ZONE_1`

**[FIXTURE]** `MAP_ZONE_1.jet` — 6 129 328 bytes, a **real** file in
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets` *and* in
`analysis/extracted/assets`, and the **only** `MAP*` pack in that 790-file
corpus. `n_00` already published it before this change.

**It is NOT proven to resolve, and I am not claiming it does.** See §6.

### 4.2 Three namespaces, three named constants

`server-ts/src/bootstrap.ts`:

| constant | field | value | status |
|---|---|---|---|
| `FIXTURE_STAGE_ENVIRONMENT_IDS` | `STAGE_INFO.res_prefix` | `"99"` | **[RECOVERED]** role, **[FIXTURE]** value (`8dc5bfd`) |
| `FIXTURE_AREA_BACKDROP_ART` | `AREA_INFO.resource_id` | `"MAP_ZONE_1"` | **[RECOVERED]** role, **[FIXTURE]** value |
| `FIXTURE_STAGE_THUMB_ART` | `STAGE_INFO.thumb` | `"ST001"` | **[RECOVERED]** role (art, not a selector), value **UNPROVEN** |

One string can no longer be published into two namespaces, which is precisely
what made the r015 log unattributable.

### 4.3 `assertAreaBackdropArt` — refuse to publish a guaranteed miss

Refuses, at module load:

1. an **empty** name;
2. an **`environments.csv` `#ID`** (`/^\d+$/`) — the inverse of the stage bug;
3. an **`ST<n>` prefix** — the measured-bad value, and the `thumb` namespace.

Cross-check against the actual CSV lives in `tests/area-backdrop.ts` (the same
split the existing stage guard uses, so `server-ts` needs no `analysis/` access
at runtime).

### 4.4 The regression test, and proof it fails without the change

`server-ts/tests/area-backdrop.ts`, added to the `npm test` chain. It asserts,
for every published area `resource_id`:

* **not** an `environments.csv` row id (re-read from the CSV, 50 rows);
* **not** `/^ST\d+$/`;
* **not** byte-identical to any published stage `thumb`;
* **is** an existing `<name>.jet` in the recovered PAD pack;
* **is not** an `environments.csv` `PreFix` value;
* plus in-file control legs: `assertAreaBackdropArt("ST001")`,
  `("99")`, `("1000")` and `("   ")` all **throw**.

**Proof it fails on the pre-change value.** Two independent legs:

**(a) the fixture's literal reverted to `"ST001"`:**

```
$ npx tsx tests/area-backdrop.ts
AssertionError [ERR_ASSERTION]: area "n_00" resource_id "ST001" is an ST<n> stage/episode
art prefix - the stage `thumb` namespace, and MEASURED to miss here:
analysis/r015/logcat-all.txt logs "[ERR] [RES] Can't find 'ST001' in ResMap." + ...
This value shipped until 2026-10-03.
  actual: false, expected: true
```

**(b) the same value through the env dial, which is refused at boot:**

```
$ $env:BLUSTONE_AREA_BACKDROP_ART='ST001'; npx tsx tests/area-backdrop.ts
Error: BLUSTONE_AREA_BACKDROP_ART="ST001" is an ST<n> stage/episode art prefix, which is the
stage `thumb` namespace, not the map backdrop. It is MEASURED to miss: ...
    at assertAreaBackdropArt (src/bootstrap.ts:270:11)
```

**After the change:**

```
$ npx tsx tests/area-backdrop.ts
Area backdrop art guard passed: 1 distinct resource_id value(s) (MAP_ZONE_1) across
2 area record(s); ST001 and 99 both refused.
```

`npm test` — all five suites pass. `npx tsc --noEmit` — exit 0.

## 5. Chest sprites (REPORT ONLY — deliberately not touched)

### 5.1 The art family is recovered

`MS_RW_*`, three states × three variants, read straight out of three recovered
layout records:

| record | names |
|---|---|
| `KO/NEW/SR_MISSION/2_SR_UI_MS_ST/0_MS_ST_EX` | `MS_RW_B1`, `MS_RW_B` (`<Animation>`), `MS_RW_B8`, and the same `_S` and `_G` triples, repeated per node slot |
| `KO/NEW/SR_MISSION/2_SR_UI_MS_ST/4_MS_ST_FT` | `MS_RW_B1`/`MS_RW_B`/`MS_RW_B8`, `MS_RW_S1`/`MS_RW_S`/`MS_RW_S8`, `MS_RW_G1`/`MS_RW_G`/`MS_RW_G8` |
| `KO/NEW/SR_MISSION/2_SR_UI_MS_ST/STAGE_POP` | `<sprite res-name="MS_RW_G1" rpos="249,547">` + `<Animation res-name="MS_RW_G" rpos="250,510">` |

So: `B` / `S` / `G` are **three** states, each with a leading still (`_1`), an
animation (bare) and a trailing still (`_8`). "Two states at once" is the UI
declaring all three in one document and code choosing which to show — which is
`CSRSceneMStageMap::SetRewardVisible(int, REWARD_STATE)` (0xe95eb8) and
`ShowReward` (0xe9413c) territory, not a resource problem. **`MS_RW_` is also a
native literal** at `0x01d730a0`, loaded in `ShowReward` next to
`PA_THUMB2`, `UI_MS_ST_BOX%s`, `RE_ITEM`, `MS_RW_`+`B`/`S`/`G` and `MN_NC`.

### 5.2 Which package? **UNKNOWN.** Candidates, all real files:

| candidate | size | why |
|---|---|---|
| `REWARD.jet` | 1 279 866 | the only pack in either tree whose name denotes rewards |
| `STAGE.jet` | 2 186 837 | the mission-stage family |
| `N_M_ICON.jet` | 270 592 | the `MS_*` node-icon family |
| `UI_MAIN.jet` | 9 321 947 | main UI art |
| `VD_MISSION.jet` | 5 841 421 | **ruled out**: it is an `MP4 payload` container (the mission cutscene video), not art |

`MS_RW_*` is **not** in `VD_MISSION.jet`, `UI_MAIN.jet`, `REWARD.jet`,
`STAGE.jet`, `MISSION2.jet`, `N_M_ICON.jet` by any readable index (§6), and it is
**not** in `E_NEW.jet` or `E_MIDAGE.jet` either — which are the two packages the
original phone definitely had.

### 5.3 The empty popup above the third chest

`CSRSceneMStageMap::PopUpClearReward(const string&, const string&, …)`
(0xe964e0) logs `'ClearRewardInfo Not Found'` when its lookup misses, and
`SetClearRewardThumb` (0xe95f00) logs `'SetClearRewardThumb Not Found'` and uses
UI nodes `RE_ITEM_THUMB` / `RE_HUNT_THUMB`. **Neither string appears in
`analysis/r015/logcat-all.txt`**, so that popup's data contract was never
reached in r015 — a different gap from the backdrop, and the one another agent
is already recovering. **Not touched here.**

### 5.4 A concrete, real gap on the popup path: `N00x` / `N00x_BG`

The recovered layout names the popup backdrop and sprite explicitly:

* `STAGE_POP`: `<Animation res-name="N003_BG">`
* `0_MS_ST_EX`: `N002_BG`, `N001_BG`, `N003_BG`, `N010_BG`, `N010_DLG01`
* `4_MS_ST_FT`, `1_UI_MS_AS`, `MS_C_SELECT`: further `N00x_BG` uses

Real files present: `N001.jet` 869 436, `N002.jet` 1 522 723, `N003.jet` 1 547 587,
`N001_BG.jet` 2 282 467, `N003_BG.jet` 322 254, `N008_BG.jet` 2 134 891.
**`N002_BG.jet` and `N010_BG.jet` are NOT in either recovered tree** — the
original server's CDN still holds those two. **None of the `N*` packs are
currently served.** They are wired up behind
`BLUSTONE_RESOURCE_ASSET_NAMES_EXTRA` (empty by default) in
`tools/start-server.ps1`.

## 6. What is NOT proven, and one correction to the record

**Entry names are not uniformly unreadable.** `analysis/research/environments-recovery.md`
§4 row 7 recorded "entry names are not plaintext in any package in this corpus".
That is **too strong**, and the distinction matters:

| pack | plaintext `<stem>*` entry index? |
|---|---|
| `C001.jet` | **yes** — `C001`, `C001_A1..A3`, `C001_AT1..AT3`, `C001_C`, `C001_DIE`, `C001_E01..`, `C001_EC`, `C001_H1..H3`, `C001_I`, `C001_I2`, `C001_R1/R2`, `C001_SK1/SK2`, plus atlas parts (`body`, `head`, `r_arm`, `T0_idle`, `T1_angry`, …) |
| `N001.jet`, `N003.jet` | **yes** — the bare stem `N001` / `N003` |
| `M001.jet` | **no** — and yet the client registered `M001_R01..R04` from it |
| `ST001.jet`, `MAP_ZONE_1.jet`, `SNOW.jet`, `UI_MAIN.jet`, `N003_BG.jet`, `MAIN_BG01.jet`, `REWARD.jet`, `STAGE.jet`, `E_NEW.jet`, `E_MIDAGE.jet`, `LEVELING.jet` | **no** |

So a **plaintext index is sufficient but not necessary** for an entry to exist,
and `M001.jet` is the counterexample that proves the obfuscated packs are fine.
Absence of a plaintext index therefore proves **nothing** about whether
`ST001` or `MAP_ZONE_1` resolves. That is exactly why §4.1 does not claim
`MAP_ZONE_1` works — only that it is the sole real candidate.

**The oracle is the log, and it is cheap.** On device:
* a **hit** produces no line at all, so *absence of* `Can't find 'MAP_ZONE_1' in
  ResMap.` is the success signal;
* a **miss** produces `[ERR] [RES] Can't find 'MAP_ZONE_1' in ResMap.` and the
  screen stays black;
* `[WRN] [OnPlay] Cannot play the node,itrdon't have A resource of image`
  immediately after any `LoadAnim2 '<X>' failure` is the "empty panel" tell.

**A free, evidence-backed A/B for the *next* defect** (not taken, out of scope
here): `ST001.jet` is the `thumb` value and it is measured to miss. `N001.jet`,
`N002.jet` and `N003.jet` carry a **provable bare entry named exactly the node
id**, and `starterAreas` already links `N001`/`N002`/`N003` as stage ids. So
`BLUSTONE_STAGE_THUMB_ART=N003` is a one-line, no-new-asset dial (the `N*` packs
would need serving first). The `thumb` consumer has never been isolated, so this
is left as the recommended next probe rather than applied.

## 7. Asset-serving state and the `.env.example` disagreement

### 7.1 What the map needs, and what is served

| need | name | served? | evidence |
|---|---|---|---|
| map backdrop | `resource_id` = `MAP_ZONE_1` | **yes** (`MAP_ZONE_1.jet`) | §2–4 |
| snow particles | `SR_SNOW` → `SR_SNOW01..03` | **yes — PROVEN WORKING** | `SNOW.jet`; `23:47:43.307/320/335` registrations |
| node markers, chapter shield, up/down buttons | `MS_ST1..3`, `MS_MK_ON/OFF`, `MS_UP`, `MS_DWN`, `MS_UP_COVER`, `MS_DW_COVER`, `MN_NC`, `ST_SHADOW` | **yes** (UI packages) | registered throughout `23:47:43.2xx` |
| stage thumbnail | `thumb` = `ST001` | yes (the pack), **but the name misses** | §6 |
| stage-select popup sprite + backdrop | `N00x`, `N00x_BG` | **NO** | §5.4 |
| chest sprites | `MS_RW_B/S/G` (+`_1`/`_8`) | **owner UNKNOWN** | §5.2 |
| battle HUD | `UI_BATTLE`, `UI_BATTLE2` | yes | working (r016/r017) |
| monster | `M001` | yes — **proven working** (`M001_R01..R04`) | — |
| card art | `C001` family | yes — **proven working** (`C001`, `C001_TH`, `C001_THN`) | — |

So the served set was **already sufficient** for the backdrop. The defect was
never a missing package: it was a wrong *name*.

### 7.2 `.env.example` (3 packages) vs `start-server.ps1` (11) — RESOLVED, documented

They disagreed silently: `.env.example` advertised
`E_NEW,E_MIDAGE,UI_XML_RO.db` against `analysis/reconstructed-resources`, while
`start-server.ps1` set eleven packages against `analysis/runtime-package-full`
plus an 8-pack art set. Nothing on the client distinguishes the two — it simply
renders a different amount of the game, which is the worst kind of config
divergence.

Resolved by naming them, not by unifying them (they are genuinely different
jobs and unifying either breaks something):

* `.env.example` now opens with a **PROFILES** section: this file is the
  **reconstructed-resources smoke profile**, used by `npm test` and
  `tests/resources.ts`; it serves **no stage art at all**, so the expedition map
  draws nothing on it. Documented: do not copy its list into a device run.
* `tools/start-server.ps1` now prints the disagreement on **every start**, plus
  the asset directory and the full folded asset list.
* `README.md` gained the two-profile table and the asset-state table.

### 7.3 A silent-failure hazard found and closed

`packageTreeEntries` (`src/server.ts`) does
`if (!existsSync(assetPath) || !isFile()) continue;` — **a name that does not
exist is dropped from the PKGI tree with no error at all**, so a typo or an
unrecovered pack ships a *shortened* package whose only symptom is missing art on
the device. `start-server.ps1` now walks
`BLUSTONE_RESOURCE_ASSET_NAMES` against `BLUSTONE_RESOURCE_ASSET_DIR` and
**throws before starting** if any file is absent. Both candidate asset
directories were checked: `analysis/extracted/assets` and the recovered PAD pack
each contain all eight base names plus the whole `C001*` family, so the check
does not misfire.

### 7.4 Not my lane, but recorded

`$card = Get-ChildItem -Filter 'C001*.jet'` serves only card 001's family and
**will not scale** as the parallel agent grows the roster in `bootstrap.ts` — a
card added there silently gets no art and no warning. It is now a dial,
`BLUSTONE_CARD_ART_GLOB` (default unchanged at `C001*.jet`; `C00*.jet` is ~570
packages / 587 MB and forces a full re-download, so it is deliberately not the
default), plus a warning if the glob matches nothing. **This does not block the
resource lane**; it only needs whoever grows the roster to widen the glob.

Widening the package/asset list is **not** done implicitly anywhere. The new
`BLUSTONE_RESOURCE_ASSET_NAMES_EXTRA` defaults to empty.

## 8. Files touched

| file | change |
|---|---|
| `server-ts/src/bootstrap.ts` | three namespace-separated constants; `FIXTURE_AREA_BACKDROP_ART` + `assertAreaBackdropArt`; areas fixture `resource_id`; `thumb` comment. **Areas/thumb only** — the monster/card fixtures were not touched. |
| `server-ts/tests/area-backdrop.ts` | **new.** The regression guard + control legs. |
| `server-ts/package.json` | added the new test to the `test` chain. |
| `server-ts/src/openapi.ts` | `AreaCatalog.resource_id` rewritten; `/reference/GetArea` operation + `x-evidence` / `x-runtime-confidence`. |
| `server-ts/README.md` | two-profile table, the `.env.example` disagreement, the map art-family table, the `resource_id`-is-art section, three new env knobs. |
| `server-ts/.env.example` | PROFILES section, asset/glob/extra dials, the `resource_id` and `thumb` sections. |
| `tools/start-server.ps1` | per-name asset documentation, `..._EXTRA`, `BLUSTONE_CARD_ART_GLOB`, missing-asset refusal, profile-disagreement banner. **The served package list is unchanged.** |

## 9. Honest bottom line

`resource_id` is the mission-map backdrop **art name** — recovered, with the
consumer, the instruction slot and the log timing all pinned. `ST001` was
provably the wrong value and is now refused at boot; `MAP_ZONE_1` is the only
real candidate in the recovered corpus and is a labelled **[FIXTURE]** choice.
**That the backdrop now renders is not claimed** — a pack existing does not
prove a resolvable entry, and §6 documents exactly why. The next run's logcat
answers it in one line: `Can't find 'MAP_ZONE_1' in ResMap.` present ⇒ wrong,
absent ⇒ right.
