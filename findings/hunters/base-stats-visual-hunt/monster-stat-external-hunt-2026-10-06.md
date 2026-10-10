# Monster base-stat external hunt (2026-10-06)

**Brief.** Monster base stats are **0/22** — the weakest gap in the project. Monsters
were picked as the best target because they have no gear, no jewels and no skills,
so a monster Max-HP panel at a stated level would be close to a genuine base tuple.
APK diffing and VSFan media mining were ruled out as proven dead ends before this
pass and were **not** repeated.

**Result in one line: a controlled negative, plus one new local calibration datum
that upgrades the Episode `M*` readings from "unpurified" to "purified as
per-encounter combat values" — while correctly leaving coverage at 0/22.**

No monster tuple with identity + level basis + unscaled basis was found. Coverage
is unchanged. Every zero below is reported with a positive control.

---

## 1. PURE — measured facts, each with a control

### 1.1 The decisive structural finding: the game has NO monster stat screen

This is the single most important result of the pass, because it explains why
seven prior visual hunts all returned zero. It is a **read-only string-table
enumeration**, not an inference.

`analysis/native-all-strings.tsv` (515 613 lines) was searched for any class that
could render a monster information panel:

| probe | result |
|---|---|
| `CSRPopUp.*Mon` | only `CSRPopUpNoMoney::SetData` false positives (`Mon` inside `function`/`Money`) |
| `CSRTable.*Mon` | **0** |
| `CSRDialog.*Mon` | **0** |
| `CSRWindow.*Mon` | **0** |
| `CSRScene.*Mon` | 3, all `CSRSceneStageConfirm::RequestMonsterRef` |
| `MONSTER_INFO`, `MonsterInfo` (as an identifier) | **0** (only 3 `[AST]` format strings using the C++ local name `MonsterInfo`) |
| `MonsterDex`, `HunterDex`, `HunterZukan`, `Zukan`, `HunterList`, `図鑑` | **0** each |

**Positive control for this probe:** the same enumeration returns **179** hits for
`CardBook`, and the native `CSRCardAnalyzer::SetBonus` / `CSRInventory::GetCardbookBonus`
symbols are present. The heroes' encyclopedia (`カードブック`) is real and shipped;
the monsters' equivalent **does not exist in the client**.

**Positive control for the string table itself:** the table reliably resolves hero
UI (`NEW/SR_MISSION/...` layout keys, 36 hits) and 78 `MONSTER` data-path hits, so
the absence of a monster UI is a real absence and not a broken table.

**Consequence.** Unlike heroes — which have a full detail screen, a card book, and
a `/reference/GetCard` reference — **a monster info card could never be screenshotted
from the original game, because no such screen was ever implemented.** The monster
stats are consumed only as combat parameters by `CSRGameMob::AddMonster`. Every
external hunt itemised in this brief (an "info card / encyclopedia entry / max HP at
stated level") was therefore hunting for a screen that does not exist. This is why
the search kept returning the same nine HUD bar tokens: it is the only monster
number the game has ever shown a player.

This is a **stronger negative than "nobody photographed it"**: it is *nothing to
photograph*.

### 1.2 The one new local calibration: shipped Episode `stat.hp` **is** the on-screen max HP

`episode-monster-base-2026-10-06.md` §4 listed as falsifier #1: *"A level-formula
application stage — if native code multiplies the shipped STAT by a level/rank
factor at load time, the shipped literal would be a pre-scale value."* That
falsifier is now **closed, in the direction that makes the quarantine stronger.**

Evidence, three independent legs:

1. **Shipped literals.** `analysis/recovered-reference/EPISODE_COMBAT_CB0101.json`
   places `CB0101_009_1` (res `C009`, thumb L15/R2/H0) and `CB0101_003_1`
   (res `C003`, thumb L1/R3/H0).
2. **Shipped stats.** `EPISODE_STAT_ACTORS.json` gives `hp` = **323** and **514**
   for those two actor ids.
3. **Observed on device, by eye.** `analysis/testing/episode-010/29-cb0101-after8.png`
   shows the two battle HP bars reading **311** (green, left) and **514** (red,
   right). The right-hand bar is **completely full** and reads exactly the shipped
   literal 514; the left reads 311, i.e. 12 below its shipped 323 after taking
   damage.

I re-derived the bar geometry from the PNG myself rather than trusting the prior
report: at row y=1031 the green fill spans x=198–381 (184 px) inside a neutral
track, and the red fill spans x=712–901 (190 px). The red bar's track ends at
x≈905 with no unfilled remainder, i.e. 514/514 — **full**. Digits were legible
without interpolation at 3× crop.

**What this establishes.** `stat.hp` is a **literal, unscaled combat HP value**, not
a pre-scale constant that a hidden level/rank formula inflates. The observed 514 is
numerically identical to the shipped 514 on an untouched bar. So the parent file's
falsifier #1 does not fire.

**What it does not establish — and this is the part that must not be overstated.**
`res_id` is still not a monster identity (§2.1), the tuples are still per-encounter
tunings (§2.2), and the one number this unlocks is a **hero** actor (`C003`), not a
monster. It upgrades *interpretation*, not *identity*.

I report the calibration as **PURE** because it is arithmetic on shipped literals
cross-checked against a device capture. I do **not** report any monster tuple as a
base stat.

### 1.3 Two 22s — the denominator trap, independently re-confirmed

Re-derived from disk rather than quoted:

- Coverage denominator (`analysis/catalogue/data/monsters.json`): `M001`…`M021`
  plus `M100` — **22**.
- Episode `M*` `res_id` tokens in `EPISODE_STAT_ACTORS.json`: `M001, M022, M023,
  M024, M034, M035, M036, M040, M041, M042, M044, M046, M048, M049, M050, M051,
  M052, M054, M057, M058, M062, M100` — **22**.
- **Intersection = 2** (`M001`, `M100`).

Art check: only `M001.jet` and `M100.jet` exist in both
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets` (790 files)
and `analysis/extracted/assets` (787 files). The other 20 Episode tokens
(`M022`…`M062`) have **no** art file anywhere locally — a second, independent
confirmation that they are not the catalogue monsters.

**This agrees with `episode-monster-base-2026-10-06.md` §1.1 and
`m001-m100-insider-2026-10-05.md:3-7`.** Flagging it because a future brief saying
"the 22 monsters" about the Episode table will silently target the wrong set — at
most **2 of 22** were ever addressable there.

---

## 2. UNPURIFIED — quarantined, zero coverage credit

### 2.1 The 34 Episode `M*` rows: status upgraded, still not a base stat

The parent's §2 quarantine **stands**. My calibration (§1.2) changes the *reason*
it cannot be promoted, not the outcome:

| promotion clause (`coverage.md:13`) | status after this pass |
|---|---|
| unambiguous monster ID | **still fails** — 20/22 tokens are not catalogue monsters; `M001`/`M100` each contradict themselves across appearances |
| level/rank/difficulty context | **now satisfied as *literal combat context*** — `stat.hp` is unscaled (§1.2), so each row is a real per-encounter HP |
| tuple is a base stat | **still fails** — the value is hand-tuned per encounter, not a monster property |

So the honest reframing is: **these are now the monsters' real combat HP/ATK/DEF for
those specific encounters**, which is *better* material for a difficulty-curve
estimate and *still not* a base stat. Quoting e.g. `M001` = 150/130/100 as "M001's
stats" remains forbidden, exactly as §2.5 of the parent file requires.

### 2.2 Identity stays unresolved — the sharing clusters re-confirmed

Four distinct `res_id` tokens carry one identical tuple (`M046, M048, M052, M054` =
`1000/1200/180`), and `M035` alone appears in three different tuples. This is
mutually exclusive with `res_id` being a stat-bearing identity. Independently
re-derived here; consistent with the parent file's §1.5a.

### 2.3 Cross-check that must not be made: `M001` 150 vs the replica's 872

`analysis/catalogue/INDEX.md:623-628` records an observed level-1 `M001` at
**872** HP in the local replica battle, while the Episode table's `M001` row is
**150**. These are different corpora (campaign replica fixture vs shipped Episode
script) and **must not** be reconciled, differenced, or averaged. The replica value
is fixture data and is excluded from original evidence by `coverage.md:37`.

---

## 3. Controlled negatives — every avenue, with its positive control

The brief's archive trap: *a zero-row CDX result is not evidence until a known-good
namespace in the same query shape returns rows.* Every negative below has that.

### 3.1 Japanese official strategy site `blustone.jp` — **no monster encyclopedia**

- **Positive control first:** `cdx?url=blustone.jp&matchType=domain` returned HTTP
  **200** with **1 236** distinct URL rows. The archive is reachable and the site
  is well captured.
- Full URL inventory taken and decoded (1 236 rows). Top-level sections:
  `wp-content` 379, `archives` 215, **`hunter` 162**, `wp-json` 111, root 55,
  `facility` 41, **`育成論` 22**, `category` 12, `初心者のあるき方` 10,
  `釣り` 3, `glossary` 3, `news` 3.
- Regex sweep for `monster|Monster|mon_|mons|怪物|モンスター|敵|ボス|teki|boss|chaseb`
  over the **whole decoded inventory: 0 hits.** The 22 `育成論` ("development
  theory") URLs are entirely hero training (`トレーニング`, `ランクアップ`,
  `キャパ超越`, `結晶`, `キャラ編成例`).
- The site's own navigation (fetched from the archived `/hunter` page) lists the
  complete article set: ハンター図鑑 (hunter dex), 施設紹介, 育成論, 釣り,
  ファイトクラブ, and stage walkthroughs. **There is no monster encyclopedia entry
  in the site map.**
- `探検ステージに詰まったら` (archives/2193) and `地獄エリアについて` (archives/1561)
  were fetched and read in full. They contain the word モンスター only in passing
  prose ("出現する敵の属性" — the element of appearing enemies). No numbers.

**Verdict: the Japanese official site documented heroes exhaustively and monsters
not at all.** This mirrors §1.1 — the source had nothing to publish.

### 3.2 Korean — namu/seore mirror: **no monster page**

- **Positive control:** the same CDX query shape returned rows for
  `dark.namu.moe` (20+ rows) and `seore.org` (20+ rows), so their Blustone-filtered
  zeros are real.
- Live `seore.org` (a working namu.wiki mirror) was read directly:
  - `블루스톤/헌터` → **200**, 132 049 bytes, with sub-pages
    공격수/수비수/폭격수/도우미/이야기.
  - `블루스톤/아이템` → **200**, 101 869 bytes.
  - `블루스톤/몬스터` → **404**.
  - `블루스톤/적` → **404**.
- **The sibling-200 / target-404 pattern is the control:** the wiki demonstrably
  carries Blustone content and demonstrably has no monster article under either
  spelling. A 404 here is a real absence, not a fetch failure.
- `namu.wiki/w/블루스톤` itself returns 403 to non-browser clients; the mirror was
  used instead. `seore.org`'s search API is 404, so absence was established by
  direct slug probing rather than by search.

### 3.3 Fandom — **no Blustone wiki exists**

`blustone.fandom.com`, `blustone2.fandom.com`, `blustone.fandom.io` all return
**0 rows** for `matchType=domain`, while the same query shape returns rows for
other domains. Absence of the wiki itself.

### 3.4 Chinese — no monster database found

- `wiki.biligame.com/blustone/` returns 200 but is a **fallback page**
  (title `bilibili游戏中心 - WIKI`) whose only 怪物 occurrences are links to
  *other* games (怪物圣所, 怪物弹珠, 怪物猎人2dos). No Blustone wiki.
- Baidu Baike 蓝光石 / 蓝光石2: no monster-stat article. Baidu search and Tieba:
  403 / anti-bot, and the one 1 MB Baidu SERP contained no monster stat content.
- `so.4399.com` does not resolve from this environment (DNS), `www.9game.cn` timed
  out, `gamersky.com` 404. **Recorded as unreachable, NOT as a negative** — I
  could not test these, so I make no claim about them.

### 3.5 VisualShower official domains — no monster pages

- `bs.visualshower.com`: **positive control** returns 50 rows; the
  Blustone/monster-filtered query returns **0**. Real absence.
- `www.visualshower.com`: 8 Blustone-related URLs, all of which are the
  2018-05-02 blacklist notice and `blustone_event` locale stubs. The `zh-CN` and
  `jp` event pages were fetched; **no 怪物 and no モンスター.** The Chinese
  official event page contains no monster data either.

### 3.6 Web search engines — unusable for this title

Five separate queries (Japanese, Korean, Chinese; monster HP/ATK/DEF/dex
spellings) returned **only unrelated games**: Ragnarok Online, Monster Hunter
World/Kiranico, Final Fantasy X/VIII, Dragon Quest, Tibia, SaGa Frontier 2, Dark
 Souls. Not one Blustone monster result. Recorded as a negative about the
*tooling*, which is why the domain-targeted work above was done directly.

### 3.7 Local VSFan tree — art and payloads only, no stat files

- 8 551 files. **Zero filenames match** `monster|mon_|mons|MONS|monster`
  (case-insensitive) — a surprising result given the tree's size, re-verified.
- Monster-named directories exist only under `Extracted Assets (2026)/1441 (APK)/`:
  `M001` (35 PNG), `M002` (38), `M005` (35), `M006` (35), `M008` (35), `M009` (38),
  `M100` (6). **All PNG textures.** No CSV, JSON, or text stat file.
- `UI_CSV/*` (6 files, including the 187 KB help table) searched for
  `몬스터|モンスター|Monster|怪物`: **0 occurrences in all six.** The archived
  in-game help documents jewels and equipment in depth but never mentions monsters.
- `Research/Blustone/Extracted Updates/*/bs_parsed/M00*.pkg.txt` are **compressed CDN
  payload bytes**, not manifests with stat filenames — verified by reading
  `M003.pkg.txt` (first line `M003.jet`, remainder binary).
- `Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx` is hero-only and already
  quarantined upstream.

**Verdict: nothing in the VSFan tree was missed.** It contains monster *art* and
monster *payloads*, and no monster *numbers*.

---

## 4. What would actually move the needle

Ranked by expected value, given §1.1:

1. **A second corpus, not more photography.** The parent file's §4 falsifier #5 is
   correct: the lever is the campaign `GetStageMonster` / `STAGE_MONSTER_LINK`
   data, where one monster id *might* hold ratio-constant rows at two levels. That
   data is **server-side** in the original game (the `/reference/GetMonster`
   request is in the 2017 VSFan capture, `API Endpoints.md:29`), so it cannot be
   recovered from any client artifact. It would require an original-server capture,
   which no one has.
2. **Stop re-hunting monster screenshots.** §1.1 makes this a closed door. The nine
   HUD tokens in `monster-hud-observations.md` are the complete set of
   player-visible monster numbers in this game.
3. **Accept 0/22 as the honest ceiling** for hero-style base-stat recovery, and
   document *why* (§1.1) — a negative with a structural cause is a real result and
   is more useful than a low-yield search programme.

---

## 5. Compliance

- All reads via Python with `encoding='utf-8'`, plus the `read`/`write`/`grep` tools.
  **No PowerShell `Get-Content`/`Set-Content`/`WriteAllLines`.** Shell was used only
  to launch Python. Cropped images were written to
  `%LOCALAPPDATA%\Temp\opencode\`, outside the workspace.
- `polluted-observations.md` **not** appended to and **not** edited. Other lane files
  were **read** for consistency and **not** edited; §1.2 supersedes one falsifier in
  `episode-monster-base-2026-10-06.md` §4 and is reported here for the parent to
  apply.
- No `server-ts`, fixture, APK, seed, emulator, phone or Ghidra action. No network
  writes; archive requests were reads only.
- Verified after writing: **U+FFFD = 0**, **CRLF = 0**.
