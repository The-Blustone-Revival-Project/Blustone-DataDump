# HANDOFF — base-stat / fixture research → the server agent

**Written:** 2026-10-06. **Audience:** whoever owns `server-ts`, Ghidra and the
emulator. **Provenance:** a parallel research effort that was read-only with
respect to all of those. **Nothing in this document has been applied.**

**Revised later the same day** to carry four post-writing findings: the Episode
STAT namespace filter (§6.1, plus a pointer in §0), the adjudicated transcendence
verdict and its standing prohibitions (§1, §8), the trace-value
non-commensurability (§5), and the shipped `skill-tag.tsv` `JOB_*` role
attestation (§3). Corrections made in place, nothing added merely to pad.

**Companion:** `SYNTHESIS-2026-10-05.md` is the navigation layer for ~95
supporting files in this folder. This file is the short version.

---

## 0. Read this first — the honest state

| Dataset | Count | Note |
|---|---|---|
| Hero base stats | **1 / 113** | only `051` Beckhen |
| Monsters | **0 / 22** | no identified full-HP tuple exists anywhere yet |
| Accessories | **1 / 100** | Jack, Max HP 260 @ Lv.50 |

**No new base stat tuple was recovered.** Everything below is either a
**proven shape/scale error you can act on**, a **native contract you no longer
need to re-derive**, or a **proven negative so you stop retrying it**.

The single most important structural fact: **the replica's protocol *shapes*
are overwhelmingly corroborated (29 rows, mostly native-parsed) while its
*numbers* are overwhelmingly unrecovered (~78 rows).** Most economy fixtures are
**unconstrained, not wrong**. Please do not read "~78 unsupported" as "78 bugs".

**One data trap before you compute any statistic.** Rows of
`analysis/recovered-reference/EPISODE_STAT_ACTORS.json` are **not** a
homogeneous hero table: a `res_id`-namespace filter alone admits 8 rows that
are tuned and placed as **enemies**. The full rule is in **§6.1** — the correct
partition is **109** hero rows over **54** identities, not 117 over 55. Nothing
in `server-ts` reads that file today, so this is a research-data rule, not a
live bug — but any number in this folder derived from Episode rows is wrong
without it.

---

> ## ⚠ READ FIRST — §1 IS **STALE**. Acting on it would REGRESS a landed fix.
>
> An adversarial audit (`handoff-adversarial-audit-2026-10-09.md`) found that §1
> was written against a `server-ts` that **no longer exists**, and I verified it at
> source. **This is the single most damaging item in this document.**
>
> - **`cardOneReference.stat[0]` now has ZERO occurrences in `server-ts/src/`.**
>   The code §1 tells you to replace **is gone**.
> - **`bootstrap.ts:201` is a `base:` line**, not the stat copy §1 cites.
> - The current line is `stat: ordinaryRankStats(projectOrdinaryStats(card.id,
>   cardOneLegacyStat))` — a **per-hero** projection with growth
>   (`hp_up 10 / atk_up 1 / def_up 1`).
> - **The defect §1 describes has already been fixed.** The default
>   `BLUSTONE_CARD_STAT_PROFILE=archive-2019-projection` publishes `001` at
>   **1521/1058/653**, giving `s = (ATK+DEF)/HP = 1.1249` — **inside** the archive
>   band `0.8419–1.2171`. The headline "**5.61× below the minimum**" error **no
>   longer exists** for the deployed profile.
> - "No test pins a hero stat value" is **false** as of this writing.
>
> **⇒ DO NOT APPLY §1.** It is retained below as the record of how the defect was
> found and what the archive says, not as a work item. The `@ hp 1000` table in
> particular is **harmful now**: publishing it would move HP back to 1000 and
> **re-open work that is already correct**. If you want to verify for yourself,
> read `bootstrap.ts` around the `projectOrdinaryStats` calls rather than trusting
> any line number in this document.
>
> Remaining live use of §1: the **"do NOT wire `LEVELING.jet` `bonus.*`"** warning
> and the **`active-skill` "do not fix"** warning, both of which still stand and are
> about things that were never deployed.


## 1. ACTIONABLE — the combat stat shape error

### What is wrong

There are exactly **three** stat-literal sites in the whole server. The defect
is one line:

```
server-ts/src/bootstrap.ts:201
  stat: ordinaryRankStats({ ...cardOneReference.stat[0] })
```

`additionalReferences` (heroes `003` `004` `005` `006`) maps every hero to
card **001's** rank-1 row verbatim. `ordinaryRankStats` only stamps a rank
label — it does not differentiate.

**Measured against the 62-row recovered archive:**

| axis | replica | archive range | error |
|---|---|---|---|
| HP | 1000 | 1277 – 2033 | **1.28× BELOW the minimum** |
| ATK | 100 / 120 | — | **5.76× below minimum** |
| DEF | 50 / 40 | — | **10.80× below minimum** |
| `s` = (ATK+DEF)/HP | **0.150** | 0.8419 – 1.2171 | **5.61× BELOW minimum** |

Note the direction: HP is **low**, not high. An earlier note in this research
said "HP 1.5× high" — that was wrong and is retracted.

**`s` is the biggest error, not `ATK/DEF`.** Any fix aimed only at `ATK/DEF`
leaves the larger error untouched. Fixing the substitution set below fixes both.

**Gear cannot explain this.** Controlled n=1: Beckhen `051` archive
`1678/864/660` vs its gear-removed Lv.30 panel `2879/1471/1149` = an **≈1.72×**
magnitude change **with ratios agreeing to ≤2.2%**. Gear is the variable held
constant. The replica also ships `equipment: []`, so there is no gear to apply.

Two precision notes, from `transcendence-multiplier-2026-10-05.md` §2.3. The
argument itself is **ratio invariance**, and that part is unaffected — but
(i) the scalar is **≈1.72, not `1.716`** (the three fields span a 2.25% band),
and (ii) **it is a LEVEL factor, not a transcendence factor** — the archive's
`level` column is `not shown` on all 62 rows while the panel is Lv.30, so the
pair differs in level and grade as well as gear. Do not reuse `1.716` for
anything; §8. The gear-removed derivation is *not* an assumption: `24068 + 6291
gear = 30359` reproduces a separately captured fully-geared panel exactly.

### 2026-10-08 — FIRST-PARTY KOREAN SOURCE: 4 fixtures CONTRADICTED, 5 CONFIRMED

`namu.wiki/w/블루스톤`, browser-rendered, last modified **2026-10-01** (so
post-2019-09-05 rebalance). Plain HTTP 403s and the mirrors render an empty shell —
**a browser is required**. Full detail, provenance and limits:
`namu-first-party-mechanics-2026-10-08.md`. **These are options with evidence,
not instructions, and none has been applied.**

**CONTRADICTED — act on these:**

| # | Replica has | Original says |
|---|---|---|
| C1 | Arena rating **±10** | **win +15, loss −8 points** — **BUT see the refusal below; do not implement this** |
| C2 | Arena week bucket **Thursday** | league **and** ranking settle/reset **Sunday** |
| C3 | one point event | **defence loss −5~6; revenge loss *or giving up* −8** |
| C4 | Search costs **1 capsule** | **per grade: 1★ 5 entries × 2 = 10; 2★ 4 × 8 = 32; 3★ 2 × 15 = 30** |

**CONFIRMED — you were right, independently:**
6 wins per league regardless of losses; **6 tiers = Bronze / Silver / Gold /
Emerald / Metron / Mandaring**; 10 sub-areas per upper area at 3 stars each and
**30 stars** for the upper-area reward; **50 dungeons** (2019); and — importantly —
**equipment and the Jewel Mine both gate on owning a 4★ hunter**, which
first-party-confirms the archive-derived "gear unlocks at ★4" I used to bound
gear-contamination risk on 57 of 62 archive rows.

**NEW and directly usable:**

- **Elemental cycle [RECOVERED]: Fire > Lightning > Ice > Fire.** Stated outright.
- **Role positional rule:** Offense/Defense **front-line only**, Bomber/Support
  **in-ship only**.
- **Rage:** fills from *touching/attacking*, never idling; **kills fill it faster**;
  **cap 10**. First-party confirmation of your measured SP behaviour.
- **Mirage Ruins:** daily entry limits; floor stage count **3 → 6** deeper; an
  uncleared floor resets at **midnight**; **only your strongest hero may be used on
  a floor**; floors can be **skipped**; difficulty is **auto-computed from the
  player's total combat power**; and *even when your power exceeds the monsters',
  team composition can still lose*. Your `mirage.ts` weekly/rotation policy now has
  a documented shape to conform to.
- **Mirage ruin types carry an element→material map:** Cryo→water/shell,
  Heat→**fire**/flame stone, High-voltage→**lightning**/metal scraps,
  Gold→varies/**Rupees**, Metron→shards.
- **Hunter Search consumes helium capsules, explicitly NOT fuel** — confirms the
  `AIRSHIP_TICKET` separation, and gives the original per-grade cost ladder (C4).

**FISHING — the first original fish data in the project.** Six named species in a
**price ordering** (cheapest → most valuable): bonefish anchovy · white-beard eel ·
**Metron sweetfish** · blade conger eel · bipedal freshwater crab · silver-warbler
octopus. Plus **silver-crown / gold-crown** size variants, the smallest unmarked,
and non-fish drops of shell / metal scraps. This is an **ordering, not values** —
but it is enough to make any invented fish table honest rather than arbitrary.

**MY "HERMES CONFLICT" WAS WRONG — RETRACTED. Do not go looking for it.**
I wrote that namu calls Hermes 3★ Fire while the archive says cold/ice. **I never
checked `023`; I had Beckhen `051`'s element in context and attributed it to the
wrong hero.** Verified directly: archive `023` = `火炎` (**Fire**), which **agrees
with namu and the catalogue**. There is no conflict and nothing to adjudicate. This
was my fourth unverified assertion this session, caught by a lane.

**The one REAL element conflict is Pansy `057`** (`動物愛好家「パンジー」`):
namu **화염 / Fire** vs archive **`冷気` / Ice** vs community catalogue **Ice** —
**2-vs-1, so namu does not overwrite.** Recorded, not applied.

**Also solved: the `Jack` identity puzzle.** Jack is a *separate character* who
interprets for Beckhen ("Beckhen is the real body") — the accessory named `Jack`
is named for the interpretor, not the rooster. That is why `051`'s accessory
looked anomalous.


### 2026-10-08 (2) — namu `블루스톤/아이템`: arena reward ladder + Raise/Forge costs

Browser-rendered `https://namu.wiki/w/블루스톤/아이템`, modified **2026-08-27**,
**16 tables**. Full detail: `namu-item-economy-tables-2026-10-08.md`. Options with
evidence; none applied. **Method note worth keeping: `innerText` collapses these
tables and reorders footnotes — a text-only pass misses them entirely. I walked
`table.rows` in the DOM.**

**NEW — arena ranking reward ladder, COMPLETE (28 rows), `순위 → 파이트칩`:**

```
1→2500  2→2400  3→2300  4-10→2200  11-20→2100  21-30→2000  31-50→1900
51-70→1800  71-100→1700  101-130→1600  131-180→1500  181-240→1400
241-320→1300  321-420→1200  421-550→1100  551-720→1000  721-950→900
951-1250→800  1251-1620→700  1621-2120→650  2121-2750→600  2751-3600→550
3601-4700→500  4701-6100→450  6101-8000→400  8001-10300→350  10301-13500→300
13501-17500→250  17501-23000→200  23001-30000→150  30000+→100
```

Two clean step regimes (−100 to rank 100, then −50), and the `1621-2120→650`
sits exactly on the midpoint, so it is consistent rather than a typo. **Arena tier
rewards are Silver 100 / Emerald 150 / Mandaring 200 chips, with Gold and Metron
BLANK — editorial gaps, not zeros. Do not publish 0 for them.**

**NEW — Raise (강화) costs are material-based and free early.** Four material
families, three grades each (금속 조각 rusty/sharp/wondrous · 등껍질
broken/intact/immutable · 화염석 cold/hot/blazing · 약초 wilted/fresh/fruiting).
By level band `1~4 … 45~`: `0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1,
0/4/2, 0/5/3, 0/0/4`. **Levels 1–4 cost no material at all**, then the grade
shifts up roughly every 10 levels. Your flat "Raise 100 gold" fixture has a real
shape to conform to.

> **HONESTY FLAG — all four material tables are byte-identical.** Genuine symmetry
> and editorial copy-paste are indistinguishable from one page, and copy-paste is
> a pattern already proven in this project's corpora. Treat "four materials cost
> the same" as **UNVERIFIED**; do not build per-material differentiation on it.

**NEW — Forge/equipment upgrade is capped at level 50** and splits into two tiers:
the row label changes from `개조 재료` (modification, lv1–20) to `강화 재료`
(enhancement, lv21–50) — mirroring your own naive-vs-Lv20+ growth split. Gold
costs exist at 500 / 1000 / 5000 / 1500 (lv11) but **only lv1–11 is populated and
the cell alignment is ambiguous**; take the existence and the cap, not a schedule.
Per-element mod materials: 번개 막대 lightning rod / 냉각수 coolant /
인화성 물질 flammable substance.

**NEW — Market corner prices:** Rupee corner 20000 gold · Fight-chip corner 500
gold **or 1500 chips** · Mirage corner 1000 gold **or 3000 chips** · Secret corner
**5 gold or 20 chips**. The gold/chip corners **rotate listings on a timer**. A
5-gold secret corner is far below everything else — sanity-check that against your
shop fixtures.

**NEW — traces are grade-gated, and that axis is separate from worth.** This page
organises 흔적 as `5.1 1★ / 5.2 2★ / 5.3 3★ / 5.4 4★`, the Mirage shop sells
specifically **3성 헌터 흔적**, and recruitment needs "등급에 따라 다른 일정 개수".
So `trace-rarity-vote-2026-10-05.md`'s non-commensurability verdict stands, but
the reason sharpens: **grade and worth are two different axes — do not merge
them.**

**FISHING — namu gives names and an order, but NOT the ids you need.** Its fish
tables are **empty** (editorial gap, same as the other wikis) and a namu site
search for a fishing page returns **0 results** (and the search UI itself works, so
that zero is real). Your `ParsePrice` contract wants `fish_id/b_price/s_price/
g_price`; **namu cannot supply `fish_id`** and this avenue is closed for ids.
What it *does* add, and what matters more than prices: **fish used to be caught
and stored then sold on demand, and are now sold immediately on capture** — so a
catch-inventory model is not original behaviour. Metron crystals drop from fishing
at "극악" (extremely low) odds.


### 2026-10-08 (3) — fixture audit against namu: 4 CONTRADICTED, incl. two HIGH

`fixture-audit-namu-2026-10-08.md`. 520 numeric literals swept across 28 files.
Read-only; `server-ts` verified **0 dirty lines** before and after. I re-verified
N1/N2/N4 at source.

**N1 (HIGH) — `shop-fuel.ts:5` `FUEL_SHOP_AP = 10`.** Prices are right
(`{1: 5 Manda, 2: 100 gold}`), the **quantity is 6× too small**: the original sells
**60** fuel for 5 Manda. Corroborated by **four** corpora, **two of which are
shipped client help text** (a 60-fuel ticket and a 60-fuel guild cap) — a stronger
evidence class than the forum post usually cited. Every original observation
brackets **8–12 fuel per Manda**; the server ships **2.0**.

**N2 (HIGH) — `game.ts:450`.** AP refills every **300 s** under a **50** cap. The
original is **1 fuel / 6 min** below a **60** cap. **These two errors partially mask
each other in play**, which is likely why both survived so long. Fixing one alone
will make the other more visible — treat them as one change.

**N4 — the highest-value structural finding.** `skill-training.ts` publishes the
`source_1..4` keys but assigns **zero materials in all 200 rows** (verified: no
non-empty `source_N_ref_id` assignment exists). namu §3 gives **four** material
families (금속 조각 / 등껍질 / 화염석 / 약초) against those **four native slots** —
a match no lane had connected. Blast radius: **184 of 200 rows wrong**; levels 1–4
happen to be correct because they cost nothing.

**N3 — a corpus-integrity defect, and a correction to my own synthesis.** The
material ladder's **final band differs between two reads of the same table**:
`0/6/4` (SYNTHESIS §A3) vs `0/0/4` (namu-item). That makes SYNTHESIS's headline
**"agree cell for cell (30/30)" actually 29/30**, and the band edges differ too
(1–4 vs 1–5). **This needs an owner decision, not a silent pick.**

**Four items the audit correctly UPGRADED from finding to non-finding** — worth
recording so nobody re-raises them: namu's blank arena tiers are **editorial gaps
(unknown, not zero)**; the 5-gold secret corner contradicts nothing; "fish sold on
capture" constrains a future implementation that does not exist; and
"equipment capped at 50" cannot contradict an empty `equipment: []`.

**Also from the namu hunter page** (`namu-hunter-page-2026-10-08.md`): 56 heroes
with **element + grade**, agreeing with the 2019 archive **50/51 on element and
51/51 on grade**; per-hero **HP/ATK/DEF is a structural negative** (the role tables
are `grade | element | name | description` with **zero images**, so nothing is an
unread stat panel). It covers **1 of the 51** uncovered ids — **`065` Teresa**
(Fire, 4★, Support). And **"등급에 상관없이 30레벨이 최대"** independently attests
the **Lv.30 cap** in Korean, though it still does not explain the 2017 "max 20"
source. A **browser on the canonical host refutes** the hope that per-role pages
hide stats the mirrors dropped: 275 slots, 4 filled, all in one hero's block.

**T2 is cost, not multiplier.** namu calls it `자기극복` and its ★3 row reads
**9/90, 30/300, 80/800** — an independent match with vsfan *and* with the game's own
T1 receipt. So T2/T3 material costs are doubly sourced, but **the
×1.2087-vs-×1.2000 discriminator is still untouched.**


### 2026-10-08 (4) — trace `collect_qty` 10/20 is CONTRADICTED by exactly 2.0×, and it has a load-time hazard

`trace-cost-adjudication-2026-10-08.md`. Read-only; `server-ts` verified untouched.

**Three axes were being conflated, which is why this looked like a four-way
disagreement:**

| axis | unit | values | source |
|---|---|---|---|
| **requirement** (divisor) | traces per hero | **20 / 40 / 80 / 160** `(2^n)×10` | namu |
| **shop price** | chips per trace | **75** (exact cross-check: "150 for 2" ≡ "375개로 5개") | `199711` + namu |
| **worth** (estimate) | valuation | 20 / 100 / 300 | vsfan `Value` column |

**Two of my own framing premises were wrong and are corrected here:** `share_en/199711`
never stated 20/100/300 (its only trace numeral is "Golden Hunter Traces **150 for
2**") — that is the *vsfan* `Value` column, so this is **three** corpora, not four.
And the shop is **신기루 (Sin-gi-ru) / 라피스의 마켓**, not Mirage —
`미라주` occurs **0** times across all 67 namu dumps.

**The verdict:** `collect_qty` 10/20 is contradicted **by exactly 2.0×** (spread
`0.00e+00`). This is **stronger than the older "factor-2 NOT UPHELD"** because
namu now also supplies the worked example **`floor(owned / collect_qty)`**
(100 traces ÷ 20 = 5), which matches native `Gce125c`. But it remains **one
community source, post-2019-09-05** — *contradicted as best evidence, not proven
wrong*. **Grade-gating is real**, appearing in three places: the requirement, the
shop price, and the Search capsule cost.

> ### ⚠ THE HAZARD, IF YOU ACT ON IT
> This is **not** a one-line constant change:
> - **`search-battle.ts:57` would THROW ON STATE LOAD.** Settled guided receipts
>   carrying `added = 10` become inconsistent the moment the divisor changes.
> - **Four tests pin the literals** — `guided-search-recruitment.ts:34,43` and
>   `trace-exchange.ts:35,65` — plus two loop trip counts.
> - **Do not strand the tutorial.** Both sides read the *same* constant
>   (`GUIDE_TRACE_QTY`), so there is no deadlock — but that was only established
>   by reading the call sites, not by inference.
> **What would settle it:** one in-game 확정 섭외 screenshot showing the rendered
> trace requirement converts this to `[ORIGDATA]`. Nothing else in the corpus can.

**And a negative worth having:** the 4,208-trace closed system is **supply**, not
the cost pool — it is a scroll-yield sample, `4208 = 2⁴×263`, no ladder rung divides
it, and `mean_drops × collect_qty` spans **3.98×** running the *wrong direction*
(supply falls 67.8 → 6.6 % as grade rises while the requirement rises 1:2:4:8).
**Per-hero `collect_qty` is NOT derivable.** Stop trying to derive it.

### 2026-10-08 (5) — the game had a DIFFERENT Chinese name; searching the obvious one finds nothing

`chinese-source-hunt-2026-10-08.md`. If you or a future lane goes looking for
Chinese sources, **do not search 蓝色石** — that is only the Korean-title
transliteration and Chinese distribution never used it as the product name.

**The game shipped in China as `疾风小侠` / `青石之战` / `青石`.** The corpus was
found by mining uploaders' own tags, not by title search.

Results: **equipment/accessory stats — negative** (no Chinese source transcribes
them; stays 1/100). **T2 panel — negative** (none exists in any language now).
**Per-hero base stats — negative** (stays 1/113). But **partial positive** — real
dated pre-rebalance CN numbers, including a purchase-bonus magnitude of
**▲1600 % / ×80000 coins** that no other corpus carries, ★4 bundles
**×100 / ×600 / ×1**, an arena zone name **`超電壓深淵-8區`**, and an expedition
countdown rendered in three fields (**44:56:70**).

**Two attractive leads were rejected on evidence, and both rejections are worth
copying:** a video titled 【疾风小侠】超越极限 *looks* like the T2 lead but is promo
copy with an art-only cover — a marketing use of 超越 is not a panel. And a
2025-26 batch of "T0阵容/礼包兑换码" posts turned out to be **a different game
entirely** (a three-role wuxia meta; Blustone has four roles).

**Left open, not closed:** QooApp (HTTP 500 to our control, but named as the CN
distribution route) and a **fully downloaded and hashed 1796 s CN-server beta
playthrough that was only sampled at 4 s**. That video is the single most promising
unfinished artifact found today.

**Instrument traps recorded:** seven tool families **failed their positive
controls** and their zeros are recorded as **void, not negatives** (Bing returned
zero for 明日方舟). `wiki.biligame.com` is a **soft-404 catch-all** returning an
identical sha256 for a nonsense path — a 1.4 MB "rich wiki" false positive. And
bilibili's CDN **truncates at exactly 1 MiB**, which mimics a rate limit.


### 2026-10-09 — the CN beta video was TRUNCATED; and Blustone shares NO engine with its sister games

**Read this if you ever touch the CN beta artefact — it was silently incomplete.**
`cn-beta-video-2026-10-09.md`. A previous lane recorded a 1796 s "decoded"
Chinese-server playthrough; it was a **40.96 % truncated download** (its own log
said `ok:false, bytes:0`, and the `mdat` header demands **518,316,881 B** against
**212,205,568** on disk). `ffprobe` reported the full 1796.1 s from a *complete
`moov`*, which is exactly why it read as "complete". **A container's metadata can
be intact while its payload is missing — that is not a completeness check.**
Now completed: 518,316,881 B, sha256 `779e7347…`, 1797 s, 53,831 frames verified,
**every second swept**. **1,070 s of footage had never been seen.**

**A real CN-beta balance reading:** one hero's 战力 reads **293 / 300 / 314 / 342** at
Lv **1 / 2 / 4 / 8** — an **exact linear fit `293 + 7×(level−1)`, zero residual**,
and the game itself prints **`▲7`**. **But do not turn this into a base tuple:**
across heroes, power is *not* a function of level (one frame shows Lv.8→342,
Lv.5→226, **Lv.2→713**). The per-hero slope is real; the cross-hero law is not.

**One balance difference you should know about:** the CN beta's **third star
condition is 全体生存 ("all survive")**, where the 2.8-era capture shows
**"1 Straggler or Less"**. Your `achieve[].order` fixtures were transcribed from
the later era, so this is most likely an era change rather than a bug — but it is
the first *evidence* that the star conditions moved, and nothing else in the
project has that.

**The headline target is a controlled negative:** across all 1796 s there is **no
HP/ATK/DEF panel and no equipment screen**. The only stat-panel-titled screen
(`详情信息`, t=538) carries just **战斗力 210 / Lv. 1** — there is **no equipment
widget to be "visibly empty"**, so it fails the gear classifier outright rather
than ambiguously. Coverage stays **1/113 · 1/100 · 0/22**.

**Sister games: the premise is closed, and first-party documentation closed it.**
`sister-game-stat-conventions-2026-10-09.md`. BTB (비욘드 더 바운즈) and White Island
(하얀섬) are **narrative adventure games with no stat system**. Better still,
`White Island/Overview.docx` states outright that BTB and White Island share the
**White Scripting Engine with each other**, while **Blustone is named separately and
runs PV**, VisualShower's platform released **2015-11**, *after* BTB's titles. So
**there is no shared engine either** — a shared developer here means a shared
*world*, not a shared formula. Corroborated by census-negative results across two
complete Fandom wikis (26/26 and 24/24 pages) and an 18,105-record audit of the
shipped client that found **zero** sister-title stat content — while also finding
the client **ships 9 sister-title strings** in all five locales, a first-party
survey panel. **Lantern/Nene agreement: full, zero new conflicts.** Side-find: the
cross-title cast is larger than the headline two — **Mowgli `002`, Chichir `004`
and Leonardo** also appear.

**Two instrument warnings, both cost real time here:**
- **bilibili's search no longer filters.** A gibberish query (`qqzzxx99887`)
  returns 20 plausible rows. A naive re-run surfaced 173 "new" videos, **all
  content-farm noise** (疾风小侠 as a ship name, 青石 as a gemstone). **Any future
  bilibili search needs a gibberish control**; the earlier Chinese hunt lacked one.
- **The video is pillarboxed** — 68 % black bar, active region 818×720. Reading raw
  frame halves effective resolution: contact sheets reported `296/1181` digit hits
  where zoom reported **536/860**, and contact sheets read `A410` where the frame
  said `450×2`. **Contact sheets triage; they do not read digits.**


> ### 🛑 STANDING REFUSAL — C1/C2/C3 are NOT approved for implementation
> `fc-native` **§1.4 forbids setting honor values from the arena reward tables**,
> and `exp-ladder` **§4 forbids conflating RankUp gold with the star-advancement
> ladder**. The "CONTRADICTED — act on these" framing above **overrides a recorded
> refusal and must not be followed.** The source documents are right; this handoff
> should have restated their refusals and did not. Treat C1–C3 as **evidence to
> keep**, not instructions. An earlier audit caught this same overreach.


### The candidate fix — 6 rows, zero migration risk

Source: `candidate-hero-bases-2026-10-05.md` §6.2. Each archive hero's
`ATK/HP` and `DEF/HP` applied to the **existing** `hp = 1000`, so **HP does not
move** — keeping this independent of the coupled monster-HP decision, which is
progression-visible and therefore yours.

| id | name | role | candidate @ hp 1000 | archive raw |
|---|---|---|---|---|
| `001` | Lantern | Bomber | **1000 / 696 / 429** | 1521/1058/653 |
| `002` | Mowgli | Offense | **1000 / 517 / 420** | 1624/839/682 |
| `003` | Nene | Defense | **1000 / 415 / 494** | 1750/726/864 |
| `004` | Tyltyl | Support | **1000 / 463 / 463** | 1467/679/679 |
| `005` | Gerard | Defense | **1000 / 387 / 550** | 1624/628/893 |
| `006` | Sylvester | Offense | **1000 / 532 / 375** | 1537/817/576 |

Properties, all checked: 6 distinct triples from 2; all six `ATK/DEF` mutually
distinct; all six land **inside their own archive role band** (the current
`2.000` and `3.000` land outside the *entire* 62-row range); `s` moves to
0.906–1.125, inside the archive band, **removing the 5.6× error**. Role ordering
is reproduced by the data, not imposed.

**Safety, verified:** `grep '\bhp\b'` over `state.ts` / `game.ts` returns **no
matches** — no derived stat is persisted. No test pins a hero stat value. The
`minRank` filter at `:202` is untouched. So this is a **reference-table-only**
change: **zero state migration, zero test breakage.**

### 2026-10-06 UPDATE — the archive's BLOCK is identified, but "base" is **REFUTED**

**Read before using the archive rows. An earlier version of this section told you
they were client-attested base stats. That was wrong and is withdrawn. The §1
substitution advice above still stands unchanged and remains safe.**

**What is [RECOVERED] and durable:**

1. The client ships the heading — `UI_TEXT_RO[329]`/`[567]`, key
   `TR_캐릭터 기본 능력치`, EN **"Base Stat"**, JA `基本能力値` — rendered as a
   stat-block title widget, `UI_JSON_RO[10756]`, key
   `캐릭터 기본 능력치|TX_ST_TL1`, SIZE 28. `TX_ST_TL1` occurs **exactly 5 times
   with exactly one label**.
2. The archive uses **both** of the game's headings byte-identically
   (`基本能力値` and `詳細能力値` = the client's `TR_능력치 상세 정보` → EN "Stat
   Details"), so the portal transcribed the game's own block structure rather
   than inventing a label.
3. The block's contents are **exactly HP / DEF / ATK / Attack-Speed** —
   `RE_CH_DI1` under `TX_ST_TL1` in `UI_XML_RO[275]`. Four for four against the
   archive's `基本能力値` block.

**What is REFUTED — do not repeat it.** The inference "therefore these are
gear-free *base* values" does **not** follow, on three independent grounds:

- **The same block is used on the equipment screens.** `TX_ST_TL1` + `RE_CH_DI1`
  appears in **four** layouts: `UI_XML_RO[275]` `SR_COMMON/1_UI_CM_CH` (character
  screen) and **[367] `SR_ENHANCE/3_SR_EN_CH`**, **[376]
  `SR_ENHANCE/3_SR_EN_CH/TR_TEAMMATE`**, **[402] `SR_EQUIP/EQUIP_MAIN`** — three
  of the four are gear screens. `[376]` additionally carries `RE_LEVEL_GAUGE`, so
  the block is **level-bearing** and certifies nothing about level.
- **`기본 능력치` is a live, buffable combat pool, not a frozen column.**
  `SKILL_REF_RO[554]` (`051|5|0`) "Increases the basic ability of self by 10%
  during a Fight Club battle"; `SKILL_REF_RO[784]` the same for all teammates in
  Guild Blitz; `TAG_REF_RO[14]` `BLITZ_TEAM_BONUS` and `[54]` `FIGHTCLUB_BOUNS`
  both "+10 % basic stat"; `UI_TEXT_RO[418]` (Awakening) "Your basic stats will
  increase". A column combat modifies by +10 % is not a static reference.
- **EN "Base" is only a dictionary rendering of a generic adjective** —
  `UI_TEXT_RO[68]` renders bare `기본` as EN "Base" for a *skill tag*. Gear-
  exclusion vocabulary is **0** across KO/EN/JA, positive-controlled.

**So `gear_state` remains `not established` on 63/63 rows.** Do not publish the
archive triple as a settled base stat on the strength of the heading. One bound
that does survive: equipment unlocks at ★4, so gear contamination is
*structurally impossible* for **57 of 62** rows and *live* only for the 5
four-star rows.

### Level: one anchor, weaker than first reported

`051`'s verified Lv.30 gear-free panel matches the archive row on **all nine
sub-stats byte-identically**, core triple at ×1.7157 / 1.7025 / 1.7409. Over 29
levels that implies:

| | HP | ATK | DEF |
|---|---:|---:|---:|
| implied `g` | 1.018790 | 1.018519 | 1.019301 |

**There is no single exact factor** — the three span 0.0008 and the DEF value sits
marginally *outside* the project's expected 1.0185–1.0193 band. Read it as
"≈1.0189 per level, with per-stat variation". **n = 1 hero.**

### Two corrections to my own earlier claims

- **RESOLVED — and my own "defect" premise was false.** I claimed `009`
  Captain's row was a copy-paste defect and that its `atk 628` was not its own
  value. **Both are refuted.** Direct exact-URL re-fetch of the primary
  `blustone.jp` pages (`settle-005-009-2026-10-06.md`) shows `009` really does
  publish **HP 1624 / ATK 628 / DEF 893** at **★1**, and `005` publishes the
  **identical block** at **★2**. All 13 TSV fields match on both. The two are
  **distinct cards** (different names, epithets, elements, rarities, all five
  skills, all three items) that the site simply gives one shared base row — the
  method discriminates, since `024`/`034` share a hero name *and all five skills
  while `005`/`009` share neither. `628` is correct; the `628 → 576`
  substitution is **withdrawn**.
  **Consequence: rarity does NOT determine the row** — the site itself gives a
  ★1 and a ★2 hero the same block, which kills the "keyed on (hero, rarity)"
  reading outright and matches the separate finding that `(rarity, role)` leaves
  all 14 cells ambiguous.
  **So the vsfan T3 non-uniformity is a REAL, UNEXPLAINED anomaly, not a data
  defect:** `009`'s ATK ratio is `1.1688` while its own HP/DEF give `1.2740` /
  `1.2788`, with the archive cell now verified correct. n = 3 heroes.
- **A real defect did surface, in a different column.** `capture_timestamp` /
  `source_url` are wrong for **31 rows**: `20191015065805` is the October *index*
  capture copied into rows that individually resolve elsewhere (`009` →
  `20191211113041`, `011` → `20191211104440`, `024` → `20191209002151`, `034` →
  `20191211104503`). Harmless for the stat values; it means **do not cite that
  timestamp as the provenance of a specific row.**
- **Level and gear stay unestablished — now confirmed at the primary source.**
  `レベル` = 0, no `Lv<digit>`, `装備中` = 0 across six sampled pages, and
  `基本能力値` appears once per page as an interpolated `<h3>`. So `level = not
  shown` and `gear_state = not established` are correct and are not extraction
  failures.

### Before you publish archive triples: 38.7 % of them are SHARED between unrelated heroes

Measured over the 62 numeric rows: **50 distinct core triples** serve 62 heroes,
so **24 heroes (38.7 %) share an HP/ATK/DEF block with another hero.** Split by
cause:

| kind | pairs | meaning |
|---|---:|---|
| identical across **all 12** stat fields | **3** | genuine costume variants — `004`/`026` Tyltyl, `001`/`059` Lantern, `024`/`034` Riko. Expected. |
| **core triple shared, substats DIFFER** | **9** | **unrelated cards** with identical HP/ATK/DEF: `007`/`014`, `039`/`031`, `019`/`006`, `022`/`030`, `005`/`009`, `032`/`002`, `060`/`035`, `048`/`027`, `037`/`040` |

So the source uses a **pool of core stat blocks** assigned across cards, with
per-card sub-stats — it is not a per-hero base table. Two consequences:

1. **Publishing the archive verbatim gives 9 pairs of unrelated heroes identical
   HP/ATK/DEF** (18 heroes). That is a visible artifact in any stat panel. If you
   publish, either accept it as evidence the original does the same, or
   differentiate deliberately and say so.
2. **It is a second, independent reason the archive is not a drop-in base table**
   — alongside the retracted gear-exclusion inference. The `replica-shape-error`
   fix in §1 remains the right one: 6 distinct rows for 6 published heroes.

Most of the unrelated sharers are same-rarity pairs (★1 ×2, ★2 ×2, ★3 ×4) with
one cross-rarity (`005` ★2 / `009` ★1), so rarity does not explain the sharing
either.


### `combat_power` is NOT a usable validator

Two heroes sharing identical core stats *and* identical `crit_damage` /
`block_damage_reduction` have `cp` differing by **+21** (`037`/`040`) and **+16**
(`019`/`006`), while `cp` is an integer. No `Σ fᵢ(statᵢ)` law — integer, real, or
`floor()` — can return different numbers for identical inputs. 0 of 511 substat
subsets are exactly consistent; `max|residual| ≥ RMSE = 80.80 cp` for any linear
law. Best fit is `R² = 0.99639`, worst row `052` at +226.9 cp. Critically,
**four of the eight rows implicated in this folder's contradictions pass the
residual test cleanly** — the same false-positive class that produced the
Captain-009 episode. Use coarse ±5 % band checks only; do not build a validator.
`combat-power-law-2026-10-06.md`.


### DO NOT "fix" the active-skill magnitudes — the wrong number is the dead one

`server-ts/src/skills.ts:21-27`. A second audit flagged this HIGH as
"magnitude declared twice, disagreeing 10× and in sign." **That reading inverts
which one is live.** The two declarations are:

| path | direct | bleed | heal | matches the comment? |
|---|---|---|---|---|
| `base_number`/`up_number` → `(base + up×level)/100` | `(-95-5)/100` = **−1.000** | `(-19-1)/100` = **−0.200** | `(95+5)/100` = **+1.000** | **YES — 100 % ATK, 20 %/tick ×5, 100 % DEF** |
| the `value_calc` **string** | **+0.100** | +0.050/tick | +0.100 | no |

`value_calc` occurs **exactly once** in the whole source tree, as a string literal
being written into the response, and the only test asserts
`typeof effect.value_calc === "string"` — it is never parsed or evaluated. Native
likewise does not evaluate it on the live path (`ApplyBuff` computes from the
`RefData` scalar before `Apply`). **So the live path is the one that matches the
documented intent, and `value_calc` is a misleading dead string.**

**Consequence: "correcting" `base_number`/`up_number` to agree with `value_calc`
would break working balance by 10×.** The only warranted change is deleting or
annotating the dead string. This is the same hazard class as
`LEVELING.jet` `bonus.*` below — a shipped-looking artifact that is not on the
live path.

### Please do NOT wire `LEVELING.jet` chunk-9 `bonus.*`

It is shipped, it looks authoritative, and it is a **regression**:

- It yields 20 distinct triples over 30 cells — heroes `003`/`005`/`006` stay
  byte-identical at every rank.
- Its expressible `ATK/DEF` spread is **5%** against a measured **2.65×** role
  spread.
- `bomber` is **strictly dominated** by `offense`, inverting the measured
  archetype. `bonus.rank_*` *worsens* the shape (ATK/HP 0.100 → 0.054).
- Only the bomber HP penalty is corroborated (0.85 vs measured 0.869); support
  0.80 is **not** (measured 0.977).
- No `server-ts/src` file currently consumes any `bonus.*` value.

### Coupled decision you own — and monster difficulty currently has NO axis

`enemy_total_hp_max` is the published monster `hp` **verbatim**, and every
recorded native win is one tap at ~181–272 damage against 100 HP. If you change
hero ATK/DEF, consider whether monster HP must move in the same change.

A second audit (`fixture-audit-pass2-2026-10-06.md`, finding F1) makes the
coupling concrete and rates it HIGH:

- **Exactly one monster is published.** `bootstrap.ts` references `M001` 24
  times and `M021` once; there is no second real monster row.
- **Every stage is one wave of that one monster** — `bootstrap.ts:1670` returns
  `{ _id: waves, wave_list: waves, ... }` from a single fixture list.
- **The schema has no per-rank growth columns**, so monster difficulty cannot
  vary even if you wanted it to. A `rank`/`level` growth column is a schema
  addition, not a data edit.

So hero ATK and monster HP are **one decision across two files**, and the monster
side currently has no dial to turn. Note the asymmetry: §1's update gives you
~~**62 hero base triples**~~ **WITHDRAWN 2026-10-09 — this re-promotes rows this same document says are NOT base stats (see the retracted gear-exclusion inference and the 38.7 % shared-block finding). Hero base coverage is **1/113**, not 62/113.~~
stat has been recovered from any source. Do not assume the hero fix transfers.

### Monsters are a STRUCTURAL gap, not a search gap — stop spending effort there

This is now a **structural** negative, established with positive controls, and it
should change how you treat any monster number in this replica:

**The game has no monster stat screen.** Monster stats are consumed *only* as
combat parameters by `CSRGameMob::AddMonster`. There is no monster encyclopedia,
no info card, no monster detail panel — **none was ever implemented.** The heroes'
equivalent is real and shipped (`CardBook` 143 string-table lines,
`CSRCardAnalyzer` 71, `SetBonus` 8).

The nine enemy-bar tokens already logged in
`monster-hud-observations.md` are therefore not an unlucky sample — they are
essentially **the complete set of monster numbers this game ever showed a
player**. Nothing can be photographed because there is no screen to photograph.

Controlled external negatives, each with a positive control: `blustone.jp` CDX
returns **1,236 rows** and **0** monster URLs; Korean `블루스톤/헌터` **200** and
`블루스톤/아이템` **200** while `블루스톤/몬스터` **404** (sibling-200 /
target-404); Fandom never existed; `bs.visualshower.com` returns **50 rows**
unfiltered with **0** Blustone hits; VSFan's **8,551 files** contain **0** monster
filenames and `몬스터` **0** hits across all 6 help files.

**What this means for you, stated plainly:** per-entity monster stats existed only
on the original server, which is gone. Any monster `hp`/`atk`/`def` in the replica
is a **design choice, not a recovery** — and it is honest as long as it is labelled
that way. Do not let a future session present a tuned monster number as recovered.
Full evidence: `monster-stat-external-hunt-2026-10-06.md`.

---

## 2. ACTIONABLE — the XP curve has the same class of error

Community sources (2 independent boards + 1 wiki ladder) agree the **MAX EXP to
cap, by grade** is `200 / 400 / 1200 / 4800 / 24000`. The local fixture is a
**rank-flat** `100*(level-1)`, totalling 2900 at every grade.

- At 1★ that is **14.5× too high**.
- At 5★ it is **8.3× too LOW**.

The direction **reverses**, so this is not a scaling error — **grade-dependence
of the total is missing entirely**. The rung ratio is 1 : 2 : 6 : 24 : 120.

Commensurability was proven in four steps (one EXP pool with two inflows; same
axis; same L1–30 span; and it is a total not a per-level step — a per-level
reading gives 29×200 = 528 cruises against three sources' 19). So the verdict
moved from UNSUPPORTED to **CONTRADICTED**. The `min_exp` **step** function is
still unrecovered, so only the endpoint and the grade-dependence are in question.

**Caution:** these community rungs are `MAX EXP`, not a per-level curve. Do not
read them as a curve. Also note `23265` (2017-05-22) says "Max level before
advance is 20", which contradicts the Lv30 cap used elsewhere — unresolved.

---

## 3. Native contracts and shipped sources recovered — do not re-derive these

All read-only. The route contracts below are native decomp; the last
subsection is a **shipped** LevelDB table, not decomp. Addresses are **ELF VA**;
Ghidra = **ELF + 0x10000**.

### `/gym/RankUpBundle` — batch rank-up (previously unknown, now closed)
- Request: `app_code app_ver market pvid otp` + `src_rank` `src_cnt`
  `target_rank` `target_cnt` **`price`**.
- Response: `ret_data.achievement` (optional), `ret_data.user.gold.cur`
  (**absolute, no `prev`**), and nested under `ret_data.card`:
  `removed_inst_id_list[]` → `RemoveCard`, and
  `target_list[]{inst_id, rank.cur, rank_up_cnt.cur, exp.cur}` → `SetCardRank`.
- `rank`/`rank_up_cnt`/`exp` are **`{cur}` objects, not numbers** —
  structurally different from single `/gym/RankUp`'s prev/cur pairs.
- Callback sink is **`void(int)`** — the int is the result code. `gym.md` and
  `batch-rankup-chucoin-2026-10-05.md` both previously said `void(int,int,int)`
  and are now corrected.
- The archive guide's "★1–★2 batch without max level" rule has **no mapped
  native eligibility predicate** yet — that gap is still open.

### `/shop/SellCard` — hunter release
- Request: **`inst_id_list`**, a JSON array serialised into **one** form field.
- Response: `user.gold.cur` (absolute) + `item[]{inst_id, ref_id, added}`.
- The removal list comes from the caller's own vector, not the response.
- **Native NEGATIVE: there is no coin/currency key.** The Chu-coin hypothesis is
  dead — the client cannot display a coin total. Do not implement a Chu-coin credit.

### `/gem/LevelUp` — jewel polish
- Request keys recovered: `app_code app_ver market pvid otp` **`inst_id`**
  **`max_tries`** (`max_tries` is the constant `7`).
- **`price_type` is positively falsified** on this path — absent from the wire,
  and `FindGemLevelUpPrice` is not called here.
- `ParseGemLevelUp` **response** fields remain unrecovered.
- Reference table row schema (no values recovered): `level price_type price
  possibility failed_compensation add_sub_ability`.

### Guild Blitz is the native **GVG** system
- 19 `/gvg/*` routes. `/gvg/GetRef` → `ret_data.gvg` with **eight absolute
  datetimes** (teaser/register/matching/deploy/combat/calc/result/finish +
  `next_gvg_dtm`), plus `min_cp` `max_cp` on both `gvg` and `camp[]`,
  `point[]`, `camp[]`.
- `min_entry_cnt` is a **field**, value server-side.
- A point row is `{point_id, val, multi}`, and **`multi` is a proved multiplier**
  on `val` (`mul r5, r0, r6` at ELF `0x00aafc76`, `r0`=multi, `r6`=val).
  **A missing or non-numeric `multi` silently zeroes the row** — all three
  conversions default to `movs rX, #0` with no default-1 path, so a malformed
  row renders as 0 points with no assertion and no log. Highest-risk item here
  for any future `/gvg/*` implementation.
- **But `/gvg/GetRef`'s `point[]` is `{id, val}` only** — no `multi`, no
  `point_id` anywhere in `BATTLE_INFO::parse`. The reference is a flat magnitude
  table; the multiplier lives only in the per-camp log.
- **2026-10-06 CORRECTION — there is no "eight datetimes vs five enumerators"
  gap. The premise was false.** `/gvg/GetRef` returns **nine** absolute datetimes
  (`next_gvg_dtm` is the ninth, not a rounding of the eighth), and
  `GetCurGVGPhase` (`0x00a9b938`) has **ten** phase values `0–9`, with the
  dtm→offset ladder confirmed from two independent sides. Decisively:
  **the phase clock is never joined to a point id** — `RefreshPoint`
  (`0x00c7838c`) resolves seven literals and *none* is `point`/`val`/`id`. A
  datetime is a boundary; it awards nothing. So do **not** invent extra point
  rows to satisfy an event/enumerator ratio.
- What a `/gvg/*` implementation actually needs: `GetRef` may safely carry
  **8** `point[]` rows (id is unclamped); **`GetCampClearPointLog` must carry
  `multi` on every row** (omitted `multi` = hard zero, see above); and
  **`GetResult` needs no itemisation at all** — it is one scalar `point` plus a
  newly recovered `contribution_multi` (`0x01d71ff8`).
- Also closed: `point_limit` is **not** a standalone key (its one occurrence at
  `0x01d68c62` is `+3` inside `fc_point_limit`), and
  `to_string<POINT_INFO_TYPE>` is libc++'s **numeric** formatter, so the
  enumerator-name route is permanently dead rather than merely relocation-blocked.
- **Known client bug, do not copy it:** `POINT_INFO_TYPE` 2 and 3 both write
  display row 1 (4 rows at stride 0x30), and phase 9's countdown reads one `int`
  past the dtm array.
- `ReqGVGRefCB` is **ELF `0x00f7525c`**, not `0x003600f0` (that is the `.dynstr`
  address of the mangled name).
- **There is no client weekday logic.** Shipped UI says Blitz registration opens
  Wednesday, but GVG runs on absolute server datetimes. **Do not implement a
  Wednesday gate.** Your `arena.ts` week bucket is **Thursday**-anchored
  (1970-01-01 was a Thursday), and its counters are inert anyway
  (`season_no: 1`, `weekly_no: 1`, `is_weekly_reward: 0`).

### A **shipped** role attestation — `skill-tag.tsv` `JOB_*`

`analysis/recovered-data/leveldb-tables/skill-tag.tsv` carries a job tag in
**slot 3** on **112 of 113** cards (`051` Beckhen has none; `036` and `043`
carry theirs in slot 5).

**The mapping is shipped TEXT, not an inference.** A second shipped table,
`TAG_REF_RO.db` (`tag-ref.tsv`, columns `tag`/`TITLE`/`DESC`), names all four
roles verbatim in its `TITLE` column — `tag-ref.tsv:55-59`:

| tag | shipped TITLE | shipped DESC (abridged) |
|---|---|---|
| `JOB` | Role | "common effect granted according to the hunter's role" |
| `JOB_ATT` | **Offense** | attack increases when the battle starts |
| `JOB_DEF` | **Defense** | defense increases when the battle starts |
| `JOB_GUN` | **Bomber** | the **whole team's** attack increases |
| `JOB_SUP` | **Support** | the **whole team's** HP increases |

This is an in-game tag dictionary, so the earlier caveat in this folder
("established empirically, not asserted") was **over-cautious and is retracted**.
Two further confirmations: the tag marks the **role-ability passive**, and a
card cannot be `JOB_GUN` without shipping the Bomber role ability (112/112, one
distinct text per role); and the mapping cross-checks **62/62 against the 2019 JP
archive** (`攻撃手/守備手/爆撃手/ヘルパー`), zero mismatches.

The independent cross-tabulation that first surfaced it still holds:

| shipped tag | role | rows | catalogue exceptions |
|---|---|---:|---:|
| `JOB_ATT` | Offense | 33 | **0** |
| `JOB_DEF` | Defense | 26 | **0** |
| `JOB_GUN` | Bomber | 21 | **0** |
| `JOB_SUP` | Support | 22 | **0** |

This is **game-authored and shipped**, and independent of the community wiki, of
the Episode actor table and of the description prose — i.e. a *second* shipped
role source, and the better one. If `bootstrap.ts` publishes `role`, this column
outranks the community catalogue. A third column agrees: `char-str.tsv`'s
`SUMMARY` prose names one archetype word on 110 rows and matches `JOB_*`
**110 / 110**.

**`JOB_*` is NEVER the wrong one.** Direct test: of 52 heroes carrying tag +
catalogue + prose, **0** dissents. Reverse test: exactly **1** (`071` Anemone)
where all three non-Episode sources agree and Episode never does. Where Episode
disagrees it is a **per-encounter override, not a card role** — `005`'s own file
contradicts its row three lines later on the same art pack and tier. So Episode's
`role` column is unusable as identity, which is the same class of error as §6.1.

**Coverage it newly attests:** the **51-ID uncovered-archive roster is 51/51
tagged** (43/43 previously agreeing; the 8 blank-role rows now filled from
shipped values), and the **11 Episode-only heroes are 11/11 tagged** —
`056 064 068 069 070 071 072 078 080 082 085`. `085` is therefore **no longer
Episode-only for role** (`JOB_SUP`), which corrects an earlier note claiming
Episode was its only source. `056` Genovia is now triple-attested Offense.
All 15 `_1` awakened rows are tagged and **all 15 agree with their base** — role
never changes across awakening.

**Only role is covered.** None of the 67 `TAG_KEY` values or 71 `TAG_REF` tags
carries element, rarity, gender or race.

**What it does not give you, and three ways to misuse it.**

- **No element, anywhere.** There is **no shipped element tag in any of the
  five LevelDB tables.** The only shipped element assignment in the workspace is
  the Episode STAT table's per-encounter `attr` — a *scripted actor* table,
  which needs the §6.1 filter and is not a card reference table.
- **Element is a per-`(card, tier)` property, not a per-card one.** Over 85
  `(ref_id, hyper)` cells `attr` is single-valued with **zero** conflicts (`role`
  likewise, except one `005` cell). Only `009` and `010` change, both at the
  top tier, and both land on the value the catalogue independently records for
  their awakened row. The `C5xx` costume packs are a **correlation, not the
  cause** — `CB1604` flips `009` on the **plain `C009` pack**. "Element varies
  by costume pack" was a true observation of the wrong mechanism; do not encode
  it.
- **The COMBAT `thumb.attr` is not read.** `MakeStageInst` copies `rank`,
  `awake_step`, `hyper`/`awake_hyper`, `init_hpratio` and `skill` off the thumb
  and **never reads `thumb.attr` at +0x24**; the in-battle element comes from
  the STAT row's `attr` via `GetRefAttr`. Three of `085`'s thumbs are
  **byte-identical copies of `070`'s own thumb**, sharing the actor-id prefix,
  while the two STAT rows are independently authored — so the thumbs are
  copy-propagated dead data.

Resolved with it, so you do not have to: `071` Anemone is **Defense**, 3-to-1
over one Episode row, and `005` proves per-encounter role overrides exist —
`CB1502_071.role = 1` is encounter scripting, not identity. `085` is a Lunar
New Year costume of `070` Alia carrying its **own Fire** element. `038_1`'s
`owner = 038` is **correct — do not "fix" it** (the same rule clears `034_1` and
`086_1`). `059` Jack O' Lantern's **card** element is deliberately left open:
44 of 45 Episode heroes agree with the archive at ≥1 tier and `059` never does,
archive + catalogue say Fire, its one Episode row says Lightning — but that row
is *independently authored* (12 of 14 stat fields differ from `001`), so neither
answer is licensed. **Do not pick one.**

---

## 4. ACTIONABLE — two Search divergences

1. **Traces are awarded only on full clear.** `search-battle.ts:207` enforces
   `won === (clearedWave === wave_count)`; the award site is `:210` with a flat
   scalar (`:214`), no per-wave term. Shipped `CONTENTS12_2` says a reward box
   per **completed** battle with partial credit on defeat. This is **already
   divergent on the win path** (1 box vs a documented 2) and becomes structurally
   unavoidable at `wave_count = 4`.
   Also: partial defeat (`cleared_wave: 1`) has **no test coverage**, and
   `cleared_wave === max_wave` is coupled at three sites (`:207`, `:65`,
   `state.ts:1238`) where `:65`/`:62` would make `normalizeSearch` **throw on
   load** — so partial credit is currently impossible to *persist*, not merely
   withheld.
2. **4 waves is the original.** `InitEffect` registers wave totals **2, 3 and 4
   only** — no total-1 family. So `SEARCH_WAVE_COUNT = 2` is native-legal, **4 is
   the documented original**, and 1 is native-illegal. Raising it to 4 would
   yield four *identical* clones of `n_01_01` wave 0 unless waves differ.

---

## 5. PROVEN NEGATIVES — do not retry these

- **The `vsfan` 20/100/300 trace table is NOT commensurable with
  `collect_qty`, and must never be compared to it.** Its numeral column is
  literally headed **`Value`** and means *what one trace is worth* — the same
  page prices `Metron Crystal` at `Value 1000`, which is exactly its Fight Club
  shop price, and skill levels consume 1–5 fragments against a `Value 10`.
  `collect_qty` is the opposite kind of quantity: **traces required per hunter**,
  a divisor — native `floor(owned_qty / collect_qty)` yields the max exchange
  count. So `hunter-traces.ts`'s `10`/`20` and NAMU's `20/40/80/160` are
  *counts*; `20/100/300` is a *per-unit price*. **The shared numeral `20` at
  1★ is a coincidence of the digit**, and any lane that greps `20` near "trace"
  must say which of the two quantities it found. Even under the counterfactual
  that they were the same quantity, the wiki breaks NAMU's *constant* ratio
  against the fixture (1.00× / 2.50× / 3.75× vs NAMU-vs-local 2.00× / 2.00×),
  which would destroy NAMU's authority rather than confirm the fixture.
  **The factor-2 claim therefore stays NOT UPHELD — leave `collect_qty` at
  10/20.** For the record: `20/100/300` is `×5` then `×3`, i.e. `20 × (1,5,15)`,
  not geometric and not `2^n`, and one row of 27 (`Locke`, ★ priced 100)
  violates the page's own rule — which is what an editorial price column looks
  like. The trace table's **rarity** column is a separate, valid axis reading
  (it agrees with the infobox / catalogue / archive on 26 of 27) and says
  nothing about counts or magnitudes.
- **The 2019 `blustone.jp/hunter` archive is a closed set.** Exactly two index
  captures, 163 urlkeys = 63 profile URLs, ★5 section empty, CDX census finds
  **no page for any `064`–`098` and no awakened `_1` variant ever existed.**
  The 62 rows you have are all it contains. Also: the availability API returns
  false negatives for `?`-query URLs — always confirm with exact-URL CDX.
- **The episode `res` → art filename rule is FALSE.** Measured: `C*` tokens match
  `<res_id>.jet` **64/64**; `M*` tokens match **2/22**. There is no `M034.jet` and
  no `M0xx` pack for 20 of 22 tokens. `ref_id` cannot substitute — it is a
  **hunter-card** namespace (120/120 to cards, 0 to monsters). The `M*` token is
  an opaque per-appearance script token. **A live false version of this claim was
  removed from two files** — if you read an older copy of
  `episode-stat-adjudication-2026-10-05.md` or `m001-m100-insider`, ignore it.
- **Chu-coin**: no native currency key exists (§3).
- **`/gem/LevelUp` price_type**: falsified (§3).
- **server-side stat data**: every audited APK build ships art/audio/dialogue/
  help/shared tuning only. 1.4.4.1 and 2.8.0.1 both audited; per-entity numbers
  are always behind `/reference/*`. **Do not spend effort diffing APKs for stat
  tables.** The only numeric change between those builds is the jewel set-bonus
  help text (see §7).
- **`share_en` / `event_en` attachment namespaces have ZERO archived bytes** —
  proven with positive controls, not merely unretrievable.
- **Audio carries no stats**: of 172 MP3s and 257 videos in the VSFan archive,
  only **one file contains speech** (a launch ceremony). Do not mine it.
- **`LEVELING.jet` chunks 1/9/19 are not hero growth curves** — they are
  upgrade costs, monster-rank multipliers, and a power threshold table.

---

## 6. TOOLING — two traps that have misled this work repeatedly

### 6.1 `EPISODE_STAT_ACTORS.json` is NOT a hero table — both clauses or nothing

> **A row is a hero row if and only if `res_id` starts with `C` AND the row's
> `id`, looked up in the matching `EPISODE_COMBAT_<id>.json` `left`/`right`
> wave lists, has `"type": "hunter"`.** The second clause is **not optional**,
> and the corpus omits it everywhere.

Measured partition of the 152-entry file (entry index 80 is a literal `{}`):

| filter | rows | distinct `ref_id` | distinct `res_id` |
|---|---:|---:|---:|
| all identifiable entries | 151 | 56 | 86 |
| `res_id` starts `M` — monsters | 34 | 4 | 22 |
| **`res_id` starts `C` — what the corpus used** | **117** | **55** | **64** |
| **`res_id` starts `C` AND `type == "hunter"` — SAFE** | **109** | **54** | **62** |

Three ways to get it wrong, all of which were live in shipped notes:

1. **`res_id` alone admits 8 rows that are tuned and placed as enemies** —
   `CB0002/0003/0004_BOSS` (all on `res_id C010`) and
   `CB1102_006/008/011/018/019`, which are the entire right side of
   `EPISODE_COMBAT_CB1102.json`. One of them was published as a hero Offense
   `ATK/DEF` of `22.500`.
2. **`ref_id` alone is worse.** Three `M*` monster rows carry a 3-digit hero
   `ref_id` (`CB0001_M01`→`001`, `CB0001_BOSS`→`040`, `CB0002_M01`→`034`), so a
   `ref_id`-only filter *inflates* a hero statistic by three.
3. **The id prefix is a red herring.** `EVCB*`/`CB*` partitions *actor ids*, not
   `res_id`s — `EVCB0301_M057` is `EVCB*` with an `M*` `res_id`, `CB1102_018`
   is `CB*` with a `C*` one. Never filter Episode STAT rows by id prefix.

This was swept corpus-wide: **12 contaminated statistics corrected, across nine
markdown files**, including a false "*median 1.263 unaffected*" claim that is now
retracted — the median **is** affected (`1.250` hero-only). Any Episode-derived
role / element / HP-median figure in this folder now carries its corrected value
inline. Use **109 / 54**, not 117 / 55. Distinct `res_id` (64) exceeds distinct
`ref_id` (55) because nine `ref_id`s carry two art packs (costume / awakened) —
say which you are counting.

**These are per-encounter scripted tuning, not ordinary hunter base stats** —
`EPISODE_COMBAT_STAT.manifest.json` says so verbatim. Never feed them into
`/reference/GetCard`. Note again that `server-ts` does not read this file today.

### 6.2 Address space — both TSVs are Ghidra image space

**`analysis/native-all-strings.tsv` and `analysis/native-evidence.tsv` are both
in Ghidra/IDA IMAGE address space (`IMAGE_BASE 0x10000` + ELF VA).**
`native-evidence.tsv` declares this at line 2; **`native-all-strings.tsv` does
NOT, and its header claims otherwise** — which misled three separate lanes.
Eleven convention statements across this folder were wrong and are now corrected.

- Subtract `0x10000` to get an ELF VA. `ghidra-*.txt` dumps (`ldr@`, `slot=`,
  `add@`, `->`) are Ghidra too; `BLUSTONE_ARM` logs are **ELF VA**.
- **A uniform `−0x10000` file mapping is wrong for the second `PT_LOAD`**
  (there `p_offset == p_vaddr − 0x1000`). That single bug produced a false
  string literal. But **every string literal in this corpus lives in
  `.rodata` / `.dynstr`, both in segment 0**, so for *string* work the uniform
  mapping is harmless — it bites only on `.got` / `.data*` byte reads. Do not
  generalise it into "all addresses are suspect".
- **The silent one: writable data is relocated.** There are **128 620
  `R_ARM_RELATIVE`** words. Reading one from the on-disk `.so` returns a value
  `0x10000` short **with no error at all** — the mapping was right, the content
  wrong. Use `word = LE32(file_off) + 0x10000`, and only where `.rel.dyn` says
  `R_ARM_RELATIVE` at that VA; `.rodata` / `.text` / `.dynstr` / `.plt` have
  **zero** such entries. Do not infer "there are no relocations" from a bare
  count — this project did, and got a right answer with a wrong reason.
- `native-evidence.tsv`'s `undefined` column is **broken, not a convention**:
  **91.2%** of `[FUNCTIONS]` rows carry it, only **735** are real imports.
- **42 rows across the two tables are section-relative byte offsets** — a third
  address space. Add the named section's `sh_offset`. The evidence file's 6
  rows are a **truncated subset** of the strings file's 36, not a disjoint set.
- `llvm-objdump` in this workspace decodes the library as **ARM, not Thumb**
  (`--triple=thumbv7-linux-gnueabihf` fixes decoding) **and its labels are ELF
  VAs with no bias — so its agreement is *not* evidence for a Ghidra-space
  claim.** Agreeing with objdump means the other side is wrong, not right.
- **Mask bit 0 of `.dynsym` `st_value`** before comparing it to a Ghidra
  address, or every Thumb symbol silently fails and the test reports ~24%
  instead of 90%.
- Both string tables are now **byte-verified 100.0000%** (`515 576/515 576`
  and `8 642/8 642`) once relocations are applied; the earlier
  "escape-encoding residue" limit is retracted.
- A byte-level `.text` literal scan produces **false positives** by decoding
  misaligned instruction streams. A non-decoding literal scan is a hypothesis,
  not evidence.

Also: **never round-trip a UTF-8 file through PowerShell 5.1**
(`Get-Content`/`Set-Content`). It cp1252-double-encodes and this has destroyed
Hangul content in this workspace three times. Use Python. See
`GUARD-encoding-and-archive-traps.md`.

---

## 7. One more real finding — the jewel set-bonus rebalance

Diffing 1.4.4.1 → 2.8.0.1 `UI_CSV` help gives **exact** per-locale deltas for
the 2019-09-05 rebalance that the TapTap announcement only described in prose:
`5%→6%`, `4.5%→6%/5%`, `50%→60%`, `23→35`, `12→16`, and **"Super Block Jewel
5%" was renamed "Reduction Jewel 10%"**.

**Warning for any rebalance model:** the reduction jewel reads **×2.00 from the
EN locale but ×1.111 from KO**. A model fitted to one locale mis-predicts
another. Also the **SC (Simplified Chinese) locale still carries the OLD table
including 9%** — the client disagrees with itself. Preserve all five locales.

---

## 8. What is genuinely NEW data, and how strong it is

The biggest acquisition was the **vsfan.net wiki**, dead live (NXDOMAIN) but
**archived in bulk**: 299 content pages retrieved, including **57 hero pages and
11 hero `Character Attributes` stat tables, 3 of them complete** and captioned
`Transcendence Level: 3`.

- **97 of 108** overlapping sub-stat fields match the 2019 JP database exactly —
  which *proves* both corpora measure the same thing. (One transcribed cell was
  wrong in the source note — `Patrone 033` reads `5/5`, not `0/0`; with it
  corrected the 97/108 result stands on re-fetched primary bytes.)
- The three complete tables imply a **candidate transcendence multiplier of
  ≈1.27–1.30**, but an integer interval test shows the intersection is **empty**:
  Hermes is exactly ×1.30000, Riko/Captain ≈×1.274, and the 2.0% gap between
  clusters is unexplained. **There is no single game-wide value.** That split
  tracks **role, not rank** (`009` ★ and `024` ★★ both read 1.274; `023` ★★★
  reads 1.300) — but n=2 vs n=1, so it is a **hypothesis, not a finding**.
- **There are zero T1 and zero T2 observations** — the other 8 tables have no
  Life/Attack/Defense row at all. So the per-step factors 1.10 and 1.20 are
  **untested, not confirmed**; a ladder of `1.05 / 1.18 / 1.30` predicts an
  identical T3 and is indistinguishable on this evidence.
- **2026-10-08 UPDATE 2 — THE MODEL IS NOW RESOLVED: rungs scale FROM BASE, not
  cumulatively.** Parent re-derived the discriminator. Three independent grounds
  now favour **(B) from-base** (`T1 x1.10`, `T2 x1.20`, `T3 x1.30`, each applied
  to the **base** value, not to the previous rung):

  | test | compounding | from-base | observed | winner |
  |---|---|---|---|---|
  | player: "akasha heals increase by **9 %** from T1 to T2" (`forum_en/421630`) | +9.94 % → a player says **10** | +9.09 % → a player says **9** | **9** | **from-base** |
  | Hermes `023` T3 ratio | 1.32868, err **2.16 %** | 1.30000, err **0.00 %** | **1.30000 exactly** | **from-base** |
  | Riko `024` T3 ratio | 1.32868, err **4.12 %** | 1.30000, err **2.00 %** | 1.2740 | from-base |

  **So `1.10 / 1.20 / 1.30` are per-level multipliers of the base stat, NOT
  successive multipliers of one another.** That is the real reason the old
  `1.716` never fitted anything: a compounding ladder predicts T3 = 1.7160,
  which matches no measurement. **This is the most implementable balance finding
  in the handoff.**

  **Caveats you must honour:**
  - The 9 % leg is **community testimony, not a measurement** — one rounded
    heal value on one hunter. It cannot resolve a 0.73 % gap on its own; it
    corroborates the two T3 legs, which are measurements.
  - **Captain `009` is off-model entirely**, not merely in ATK: its HP 1.2740 and
    DEF 1.2788 also miss 1.30000 (they match *Riko's* 1.274), and its ATK
    1.1688 matches neither model. Its archive cell is verified correct at the
    primary source, so this is a genuine unexplained outlier.
  - **No T2 panel exists in any reachable avenue.** The `blustone.jp` image
    corpus is now closed exhaustively — 343 of 344 archived images pixel-decoded,
    exactly **one** transcendence receipt (the T1 `capa2`). The shipped `TRC*` UI
    keys hold only four numeric rows (ATK/DEF/HP/Strength, before/after) and every
    numeral is the placeholder `10000`, which **proves the factors are
    server-side** — string archaeology can never recover 1.20 / 1.30.
  - **Why no clean per-level pair exists in the wild**, now explained: the
    in-game `!` panel "is really the full stats you get from added Dorm bonus,
    Jewels and Equips altogether" (`1361746`). Players never see a bare stat.
    **Do not keep hunting for one.**
  - `戦闘力` is a **composite**, rising +5.74 % where its inputs rose +9.94 %...


- **2026-10-08 UPDATE — T1 IS NOW MEASURED, and it settles the old `1.716` question
  by eliminating it.** Two lanes independently read the same previously-unread
  official-guide frame (`capa2-1024x911.jpg`, 2018-11, **pre**-2019-09-05
  rebalance) and got identical numbers: the キャパ超越 (Capacity Transcendence)
  receipt shows ATK `365 → 401`, DEF `423 → 465`, HP `619 → 681`.

  | | before | after | ratio |
  |---|---:|---:|---:|
  | ATK | 365 | 401 | **1.098630** |
  | DEF | 423 | 465 | **1.099291** |
  | HP | 619 | 681 | **1.100162** |

  **T1 = 1.0994 ± 0.0012**, internal spread **0.139 %** (parent re-derived). It is
  **positively labelled T1**, not inferred: the same frame's cost panel reads
  crystals **9/9**, fragments **449/90**, gold **9000** — the ★3 T1 row
  (9 / 90 / 9 000) exactly, and not T2 (30/300/30 000) or T3 (80/800/80 000).
  **Gear-free** (equipment unlocks at ★4; hero is ★3). So the `1.05/1.18/1.30`
  degeneracy is **excluded** (4.70 % off) and the `1.10` rung is **measured**,
  not assumed.

  **How the rungs combine is still OPEN, and this is the actionable part:**

  | model | rule | T1 | T2 | T3 |
  |---|---|---:|---:|---:|
  | **(A) compounding** | each rank-up scales the *current* value | 1.0994 | **1.2087** | **1.3287** |
  | **(B) from base** | each level scales the *base* value | 1.0994 | **1.2000** | **1.3000** |

  (B) fits the numbers — Hermes' T3 reads **×1.30000 exactly**. (A) fits the
  article's prose ("once per rank-up, max 3×"), giving the ×1.3287 ceiling.
  Measured T1 cannot separate them. **A single T2 panel decides it.**

  **Do not implement a compounding ladder.** `1.10 × 1.20 × 1.30 = 1.7160` matches
  no measured T3 (1.274 / 1.300 / 1.3287) — the rungs are **not** cumulative
  multipliers of one another. That is why `1.716` never fit, and it is now
  explained rather than merely refuted.

- **`戦闘力` is a COMPOSITE, not a linear function of HP/ATK/DEF — now proven, not
  inferred.** Under the same single operation that moved all three stats by
  ×1.0994, `戦闘力` moved `2326 → 2704` = **×1.162511**, i.e. **+5.74 % faster**
  than the stats it must derive from. Read that figure as a **rating ratio**, not
  a stat factor; the "high confidence factor" reading in
  `hero-panel-level-extraction-2026-10-06.md` is demoted. This also explains why
  the archive's `戦闘力` column and the in-game one will not reconcile.
- **The archive's 62 rows may be on a DIFFERENT BASIS from the in-game panel.**
  Archive `036` Bear vs this in-game ★3/Lv.1 reading gives HP **3.1066**, ATK
  **2.0685**, DEF **2.0426** — implied per-level factors spanning **1.0249–1.0399**.
  **No single per-level scalar maps all three, whatever the grade does.** That is
  a third independent reason not to drop the archive in as a base table (with the
  refuted gear-exclusion inference and the 38.7 % shared blocks). It does not make
  the archive worthless — it is still the only per-hero numeric corpus — but any
  use must state the basis mapping.
- **Still missing, precisely:** `戦闘力` of the blonde-child hero at **★4/Lv.MAX**
  (T3's left-hand value) would give `g²⁹ = 1.4820296 × 3311 / B` with no
  assumption about the T3 grade factor. The un-cropped ★4→★5 screen **does not
  exist** — all three uploads of `IMG_5729` are crops of one phone photo, cut at
  the badge row where `戦闘力` begins. Second priority: any **T2** panel.


- **2026-10-06: a THIRD, independent measurement that fits none of them.** 180
  official-guide screenshots (2018-11 → 2019-03, all **pre**-2019-09-05
  rebalance — the era control that had never been mined) contain a
  **capacity-transcendence** reading for Bear `036` at **fixed level and grade**:
  `戦闘力 2326 → 2704`, a factor of **×1.16251**. That is a genuine
  same-conditions observation the wiki could not supply. It does **not** compound
  into the T3 clusters in any step count — `1.1625¹/²/³` = `1.1625 / 1.3514 /
  1.5711`, against measured T3 values of `1.2740` and `1.3000`. Treating it as one
  rung of the same ladder would need a next rung of `1.096`–`1.118`, which is
  neither `1.10` nor `1.20`. **So either capacity-transcendence is a different
  mechanic from stat-transcendence, or the ladder is not per-step multiplicative.**
  Do not implement `1.1625` as a stat factor either — it is measured on
  `戦闘力`, not on a stat. `hero-panel-level-extraction-2026-10-06.md`.
- **The same lane produced the first measurement that actively FIGHTS the
  `1.7157` reading.** Two independent ★3/Lv.MAX → ★4/Lv.1 rank-ups move
  `戦闘力` by **1.48203** (`029` Kain) and **1.49843** (unidentified) — agreeing
  to **1.10 %**. Because a grade-up cannot lower power, that bounds Lv.1→Lv.30
  growth of `戦闘力` at **≤1.482**, i.e. per-level **≤1.0137**, against
  Beckhen's core-stat **1.7157** — **1.16× above the bound.** It does **not**
  close the question, because the two `戦闘力` columns are provably not the same
  quantity: in-game Lv.1 ÷ archive gives **0.2323 / 0.3237 / 0.6379** for three
  same-rarity heroes, varying **2.7×**, so no level factor reconciles them.
  **Prefer leaving this open.** A tempting next step — reading it as a hard bound
  and discarding `1.7157` — is exactly the defect of §5.5 item 13.
- A tempting 1.10 × 1.20 × 1.30 = **1.716** link to a Beckhen panel was tested
  and **refuted three ways** (the panel is labelled "Lv.30, no equipment";
  Beckhen is 3★ so it can reach at most T1; and the max measured T3 is 1.30000).
  **Do not resurrect this.**
- **What `1.716` most plausibly is: a LEVEL factor, not a transcendence factor.**
  The archive's `level` column is `not shown` on all 62 rows while the panel is
  Lv.30, so that pair differs in level as well as grade and gear. The same three
  fields give a per-level compound of **1.0185–1.0193** over 29 steps — three
  independent fields agreeing to 0.4% — and the panel's HP 2879 sits **above
  the archive's entire 62-row band of 1277–2033**, exactly where a levelled-up
  card belongs. Read that as a **candidate per-level growth rate only** (one
  panel, 2018 era, gear-removed), not a recovered curve — and it is a different
  axis from §2's MAX-EXP endpoint, so do not merge the two.
- **One anomaly survives and should not be smoothed away:** Captain `009` atk is
  734/628 = **1.16879**, 8.2% below the cluster. A single-digit JP repair
  (628 → 576, the archive's minimum ATK) would reconcile him, so it may be a
  transcription slip — but it is the only evidence that a field-specific rule
  might exist.

**Standing prohibitions — adjudicated, not open questions.** Do not implement
`×1.30`. Do not implement `×1.274`. Do not implement `1.10 / 1.20 / 1.30` as
per-step factors (only the T3 endpoint is measured; the fit has one degree of
freedom). **Never write `1.10 × 1.20 × 1.30 = 1.716` as a transcendence figure** —
it is refuted by ~26–32% against the corpus's own T3 captions. A per-hero or
per-role table is the only shape this evidence tolerates; no single scalar is
licensed by any arithmetic performed here.

Every number in this research is **IMPURE** — identity, level, gear, rank and
era are mostly unknown. `polluted-observations.md` is the full ledger. Nothing
here should be promoted to a "recovered base stat" without level + gear context.

---

## 9. Suggested reading order

1. this file
2. `SYNTHESIS-2026-10-05.md` — index, 15 live contradictions, 32 retractions,
   31 proven negatives
3. `replica-shape-error-2026-10-05.md` + `candidate-hero-bases-2026-10-05.md` §6
4. `fixture-conflict-audit-2026-10-05.md` — 82 rows, 9 systems, 4 CONTRADICTED
5. `GUARD-encoding-and-archive-traps.md` — 2 minutes, read before editing any file
6. `address-convention-2026-10-05.md` — before trusting any address
7. `episode-stat-namespace-filter-2026-10-06.md` — **the filter rule you need
   before computing any statistic from `EPISODE_STAT_ACTORS.json`**
8. `identity-contradictions-2026-10-05.md` — the shipped `JOB_*` role source and
   the element-per-tier rule (§3)
9. `transcendence-multiplier-2026-10-05.md` and
   `trace-rarity-vote-2026-10-05.md` — the two adjudicated negatives (§1, §5, §8)
10. `grouprankup-sellcard-bodies-2026-10-05.md`, `gvg-reference-2026-10-05.md`,
    `gem-popup-bindings-2026-10-05.md` — the native contracts

---

## 10. Decisions that are yours, not ours

1. **The `bootstrap.ts:201` substitution** (§1). It is safe and it is proven, but
   it changes combat balance. We did not apply it.
2. **Monster HP coupling** — hero ATK/DEF changes are entangled with the
   progression-visible `enemy_total_hp_max`. We deliberately left HP untouched
   to keep that separable.
3. **Role, if you publish it** (§3). `skill-tag.tsv`'s `JOB_*` column is
   shipped, game-authored and agrees with the community catalogue 102/102, so
   it is a strictly better source than the one the current reference tables
   lean on. Swapping it in is a one-column change to the reference data; we did
   not make it. `051` has no tag, so that cell stays as it is.

Everything in §1–§4 is offered as **options with evidence**, not instructions.
---

## 11. CORRECTIONS LOGGED 2026-10-09 (adversarial audit) — read before quoting §1–§10

From `handoff-adversarial-audit-2026-10-09.md`. I verified the §1 staleness claim
at source myself. **Reproduces exactly and needs no change:** §3, §5, §6.1, §6.2,
§7; the `JOB_*` attestation (112/113, 102/102, and the 51/51 · 11/11 · 15/15
coverage claims); the §6.1 partition `151/34/117/109 · 56/54 · 86/62`; the 38.7 %
shared-block finding; **all four prior retractions are genuinely retracted in
place**; and coverage counters never moved.

**Corrections a reader must apply:**

| # | As written | Correct |
|---|---|---|
| 1 | §1 defect + "act on this" | **STALE — already fixed.** See the banner. |
| 2 | arena ladder "28 rows" | **31 bands**; `fc-native §1.5` already said 31. The step regime ends at **rank 2120**, not rank 100. |
| 3 | C1 under "act on these" | **Violates `fc-native §1.4`.** See the refusal banner. |
| 4 | §5 trace factor-2 "NOT UPHELD" | **Stale** — §1(4) later upgraded it to contradicted-by-2.0×. |
| 5 | §8 "MODEL IS NOW RESOLVED… most implementable" | **Self-contradictory** — the same section also says "still OPEN" and "do not implement". The defensible statement: **from-base is favoured on three grounds, two of which are measurements; T2 is untested.** |
| 6 | `2326→2704` as a "third **independent** measurement" | **Not independent** — it is the **same `capa2` frame** as the T1 reading. |
| 7 | `1.3287` | **1.3288** |
| 8 | `29×200 = 528` | **5800**, then `⌈/11⌉` — the arithmetic as printed does not reproduce |
| 9 | "ratios agreeing to **≤2.2 %**" | the same document says **2.25 %** elsewhere |
| 10 | Beckhen excess **1.16×** | the source note explicitly corrected this to **1.15×** |
| 11 | `± 0.0012` on T1 | **error bar is undefined** — the measured spread is 0.139 %; quote the factor, not an invented interval |
| 12 | `state.ts:1238` | **1278** |
| 13 | "flat scalar `:214`" for trace award | that site **now awards 10 for guided wins** |
| 14 | "§1's update gives you **62 hero base triples**" | **re-promotes withdrawn rows** — this same document says they are not base stats. The one live mention is now **struck in place** with an explicit `1/113, not 62/113` marker. |

The audit also caught **two of its own** apparent misses as bad probes (an
unsorted-list min, and a bare-`clearedWave` grep that missed
`receipt.wave.cleared_wave`) and documented both so nobody re-chases them. That is
the standard this folder holds: a control failure and a real finding look the same
until you check.

**Live hazard re-confirmed at audit time:** `collect_qty` is still `10`/`20`, and
the **`search-battle.ts:57` load-time throw is still reachable** — so the §1(4)
trace migration hazard is not theoretical.

---

## 12. The third star condition DID change — proven from both clients' own bytes

`star-conditions-era-2026-10-09.md`. This closes the CN-beta thread and it is a
genuine era finding, not a regional difference.

The star labels are **client-side strings selected by a fixed index**, carrying
stable on-screen ids `TX_RS_M` / `TX_RS_C` / `TX_RS_T`. The **1.4.4.1 APK** (found
in the VSFan archive) and **2.8.0.1** carry the same ids:

| slot | id | 1.4.4.1 | 2.8.0.1 | changed |
|---|---|---|---|---|
| 1 | `TX_RS_M` | Mission Complete | identical, all 5 locales | **no** |
| 2 | `TX_RS_C` | Under 60s | identical, all 5 locales | **no** |
| 3 | `TX_RS_T` | **All Survived** / 全体生存 | **1 Straggler or Less** / 落伍1名以下 | **YES**, all 5 |

**The decisive detail:** the record key **`동료 전원 생존`** and the layout ORI
**`팀 전원 생존`** survive *verbatim* into 2.8.0.1 — both still say "whole team
survives" while the rendered value says "1 straggler or less". **A balance change
was applied without touching the localisation keys.** No new key was added, so it
is neither a new condition nor a re-translation.

**Dating:** vsfan's `Expedition_Area` still reads *"All hunters on your team have
survived"* across captures **2019-08-26, 2019-10-20 and 2019-12-14** — while that
page itself grew 11,142 → 11,189 B, so it was actively maintained, not stale.
**Bracket: after 2019-12-14, before 2.8.0.1.** The **2019-09-05 rebalance did not
do it** — the old rule was still published 70 days later, and no patch note in any
recovered corpus announces the change. It was silent.

**The CN beta is a PRE-CHANGE client, not regional content** — it reads
`任务完成` / `60秒以内完成` / `全体生存`, i.e. 1.4.4.1 **verbatim, slot for slot**. So
no CN-specific treatment is warranted, and the apparent CN/global difference is
fully explained by build age.

**Party size:** the old rule was **party-size dependent** (`팀 전원 생존` = "all
hunters on your team survived", 0 deaths of N). The new rule is an **absolute**
threshold in every locale with no N. At 5 hunters, 5/5 became 4/5 — so the change
both relaxed the rule by one death *and* de-coupled it from party size.

**⇒ SERVER: change nothing.** The replica ships a 2.8.0.1 client whose `TX_RS_T`
string reads "1 Straggler or Less", so `dead_cnt <= 1` makes awarded stars agree
with the label the client is simultaneously drawing. Switching to `== 0` would
award a star the client then labels wrongly. Keep it labelled **local policy** —
the labels and the era bracket were recovered, **not** the native predicate.

**Two bonuses:** `Under 60s` is **hard-coded in the client string**, not a chosen
server number, so publishing 60 s matches the label the client draws. And the
client ships a five-threshold family (30/60/90/120/180 s) used by *other*
contexts — **not** the campaign star slot. `hp_page` is untouched and no HP
arithmetic appears anywhere in this.


---

## 13. ECONOMY LEDGER 2026-10-09 — the coupled-error finding, and one [R] number

Spine document: `ECONOMY-LEDGER-2026-10-09.md`, consolidating
`cost-ledger-2026-10-09.md` (every cost, 13 systems) and
`campaign-reward-ledger-2026-10-09.md` (every reward, 20 currencies, flow graph).

### 13.1 The framing fact

**Exactly one number in the entire economy is `[RECOVERED-native]`: the gacha price,
30 single / 300 bundle.** Everything else is first-party, community or a fixture.
That is why the classification labels below matter more than the values.

### 13.2 🔴 FUEL AND STAGE COST ARE **ONE** ERROR, NOT TWO

This is the finding most likely to be got wrong, so it is stated bluntly:

| | replica | original | error |
|---|---|---|---|
| fuel per 5 Manda | 10 | **60** | 6× cheap |
| **AP cost per stage** | **1** | **6–12** | **6–12× cheap** |
| fuel regen | 1 / 300 s | 1 / 360 s | 20 % faster |
| fuel cap | 50 | 60 | 17 % lower |

A full 50-stage campaign costs the replica **50 AP** versus **300–600** originally.
**Fixing N1 alone does not help** — the stage cost is still 6–12× cheap, so the
campaign stays ungated. **Fix N1, X3 and N5 together or not at all.** X3
(`shop-fuel.ts:7`, gold tier 100 vs **5000**) compounds N1: fuel is cheap on *both*
currencies simultaneously. The interval/cap pair partly **masks** itself — 50 fuel
at 1/300 s and 60 at 1/360 s are close in *time to full* (4.2 h vs 6 h) — which is
why they read as "roughly right".

**60 is corroborated in three independent places**: the 60-fuel ticket, the 60-fuel
guild support cap, and the 60-fuel bundle.

### 13.3 🔴 X1 RankUp gold is a SHAPE error — no scale factor fixes it

`training.ts:5` charges a flat **1000/source**. Original per-source is
**1000 / 1500 / 4000 / 15000** — **not constant**, so a multiplier cannot fix it.
At 3★→4★ the replica is **4×**. A `[FIRSTPARTY]` image frame shows **8000 for 2
fodder** and **12000 for 3 fodder** on the same target, and
`8000/2 = 12000/3 = 4000` — two different counts yielding the same per-source
figure is what licenses the division. **The fodder counts in the same file are
already correct; the defect is confined to gold.** Per `exp-ladder` §4, fodder
counts / per-grade ladder / derived per-source price remain **three separate rows**.

### 13.4 🔴 FOUR FABRICATED-SUCCESS ROUTES — the only silent state corruption

**27 of 33 native cost-bearing routes are absent.** That is mostly benign: *not
implemented* means *nothing to fix*. But **four answer `result_code: 1` on a
state-changing verb**, which is not absence — it is a **fabricated success**:
`/shop/SellCard`, `/reference/GetPaidGemGacha`, `...Mileage`, `...DailyFree`,
`/lobby/GetGachaMileage`, plus the unlisted gacha banners
(`/shop/GachaGeneral`, `GachaEvent`, `GachaSpecificList`, `GetGachaEventRef2`).
AGENTS §26 proved a mock on a shop route renders a **popup that is empty**, so the
harm is invisible. **This needs no number to fix — just refuse them.**

### 13.5 ⚠️ THE 30-STAR CHEST — two credible sources, two answers. DO NOT PICK ONE

Agreed by **two independent classes** that each region has **three chests at
10 / 20 / 30 total stars**: the English `vsfan Expedition_Area` (byte-identical
paragraph across **three** Wayback captures, 46 and 116 days apart, three digests)
and the client's own `ShowReward` arithmetic gating on `S * (i + 1)` with `S = 10`.
**This is the first external confirmation of the `achieve_cnt = stageCount*(index+1)`
derivation**, which until now rested on native decomp alone.

But the **30-star payout** is disputed: vsfan says **the region's hunter**; namu
says **만다나 의뢰서** (Mandaring commission); vsfan's own Guide says the hunter
comes from **beating the boss** — a different trigger. Three readings survive.
**All 15 payout cells (5 areas × 3 thresholds) are `[UNKNOWN]`.**

⇒ **Leave them labelled. Do not choose.** Under the likelier readings the replica
pays gold where a hunter and/or a commission belongs — and if the hunter reading
holds, there is a **gacha-free path to region hunters** the replica deletes.

### 13.6 The other wrong constants, in one place

`N2` AP interval/cap 300 s/50 vs **360 s/60** · `N4` skill materials **184/200 rows**
zero where the original goes non-zero at level 5 · `N2`/`X2` skill gold 100×level
vs **800 at Lv35** (**4.5×**) · `N9` trace requirement 10/20 vs **20/40**
(**exactly 2.0×**; note `collect_qty` 10/20 is the *other* half of that same
relationship, and `search-battle.ts:57` **throws at load** so it is not dormant) ·
`N6` EXP/stage 10 flat vs 7–32 · `X6` XP endpoint **2900 for all grades** where the
ladder is **200·R!** — a **shape** error (grade 1 correct, 2–5 under-paid), so fix
per-grade, not the 2900 · `N8` weekly anchors **Thursday and Monday** vs
**Sunday** (arena) and **daily** (Mirage) — two systems, two different wrong days,
so there is no single constant to correct.

### 13.7 ⚪ Two things that are CORRECT and must not be "fixed"

- **`user.gold` IS the Rupee wallet and `IT_CO` IS the Rupee icon.** There is **no
  separate "Gold" currency**: the namu and English wikis use the same word for the
  soft currency, and "골드" is either loose player synonym or a **Market corner
  name** (비밀 코너 at 5, 루피 코너 at 20 000). The arena ladder's third column is
  **녹색 만다** (green Manda), not 골드.
- **`dead_cnt <= 1`** stays — see §12. The 30-star string change does not apply to
  the replica's client.

---

## 14. LOGIN BONUS RECOVERED — 9 of 28 cells known, replica matches NONE

`login-bonus-calendar-2026-10-09.md`. **G1 was not unrecoverable.** The prior
ledger called `Hunter_Supply_Office` "a navigation stub with no reward content at
all" — that was a **retrieval artefact** (the page exists; it was merged with
`Hunter_Supply_Station`).

**Week 1 of the cycle — [COMM] ×3 byte-identical captures** (2019-08-21 / 10-15 /
2020-08-08, all `oldid=6016`), post-patch 1.0.8.0 (2017-08-03):

| day | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| reward | **Rupee 3000** | **Evaluation Request ×5** | **Rupee 5000** | **Fuel Ticket ×2** | **Challenge Invitation ×2** | **Elite Request ×1** | **Metron Crystal ×1** |

**+20 Veteran points on every claim.** A **second, separate** cumulative ladder
(**[COMM] ×3**): **5/10/15/20 days** → Rupee Lottery Ticket ×2, Elite Request ×1,
2-3★ Request ×1, 3★ Request ×1.

**The 28-day cycle is REAL** — three independent sources **plus two players
reading "I am on day 28" off the UI**. That **reconciles** the old weekly-vs-
monthly dispute: the 7-day week is week 1 of a 4-week cycle. Weeks 2–4 `[?]`.

### 🔴 Replica impact — the largest correctable reward block found

| | replica | evidence |
|---|---|---|
| day 1 / day 3 | 100 gold | **3000 / 5000** |
| days 2, 4, 5, 6 | 100 gold | **no gold at all** — requests/tickets |
| day 7 | 100 gold | **Metron Crystal ×1** (contested) |
| Veteran | +20 ✅ | **+20** — already right |
| boundary | **UTC midnight** | **contradicted** (per-player 16:00 vs 10:00) |
| cumulative | absent | the four rewards above |

**Gold appears on no recovered day except days 1 and 3, and at 3000/5000 — not
100.** Wrong in magnitude, composition *and* day boundary. **Do not simply
multiply 100 → a constant:** five of the seven recovered days pay **no currency at
all**, so the correct fix changes the reward *type* per day, not just the number.

**G9 half-solved:** the wiki's "40 Veteran/day" is **20 attendance + 20 daily
goals**, not a rival figure. The 20 is confirmed by three separate live native
claims. The Guru-3 threshold conflict (40 960 = 20·2¹¹, self-consistent, vs
67 520, not) remains a likely era change.

**Contested — do not smooth:** day 7 is Metron Crystal ×1 in the recovered table
vs a 4★ Selection in one *unanswered 2022 question*; and **miss-day reset is
`[UNKNOWN]`** with sources actively disagreeing (1 069 sign-ins over ~3 years
argues against a strict streak).

**Not done:** no `[FIRSTPARTY]` image frame; Korean and Chinese sources were
genuinely unreachable (namu 403, no browser attached, web search returned nothing
even for its own control query). **The namu attendance page is still unread**, so
this is English-only.
