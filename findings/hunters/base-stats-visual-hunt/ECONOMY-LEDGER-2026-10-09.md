# MASTER ECONOMY LEDGER — Blustone, consolidated 2026-10-09

**This is the spine document for the economy.** Two source ledgers hold the detail:

| ledger | scope | size |
|---|---|---|
| [`campaign-reward-ledger-2026-10-09.md`](campaign-reward-ledger-2026-10-09.md) | everything that **flows IN** — every reward, every currency, the flow graph | 51.5 kB |
| [`cost-ledger-2026-10-09.md`](cost-ledger-2026-10-09.md) | everything that **flows OUT** — 13 systems, every cost, server-constant classifications | 37.3 kB |

Read those for line-level provenance. **This document answers the three questions
those two cannot answer alone:** what the whole economy's *shape* is, what
*interacts* with what, and what is still unknown in priority order.

## Evidence classes used throughout

| tag | meaning |
|---|---|
| **[R]** | **recovered** from the shipped client — native code, or a value the client itself prints |
| **[1P]** | **first-party** — official guide, or the game's own shipped help text |
| **[C]** | **community** — wiki, board, video; dated and sourced |
| **[F]** | **fixture** — a replica invention with no source |
| **[?]** | **unknown** — no source found; the source that would settle it is named |

**One number in this entire economy is [R]:** the gacha price, **30 single / 300
bundle**. Everything else is [1P], [C] or [F]. That is the single most important
sentence in this document — it is why the server's economy needs the labels below
rather than confidence.

---

# 1. THE SHAPE OF THE ECONOMY

Six real currencies carry the game. Everything else is a ticket, a fragment or a
shard that feeds one of them.

| # | currency | tier | its one structural job |
|---|---|---|---|
| 1 | **Rupee** (루피) | soft, universal | the sink on almost everything; 9 distinct documented price points from 1 000 to 80 000 |
| 2 | **Manda — paid** (만다) | premium, bought | gacha 30/300, fuel 5, abyss reset 30, high bait, dorm expansion |
| 3 | **Manda — free** (녹색 만다) | **earned only** | **4★ Transcendence Tickets are buyable with FREE Manda ONLY** — [C] forum 1140439 |
| 4 | **Fight Chip** (파이트칩) | FC-earned | the FC Shop, 7 rows, 12 h refresh |
| 5 | **Metron material** (메트론) | drop-gated | skill training **and** Transcendence; fragments cost exactly **10×** the crystal count |
| 6 | **Trace** (흔적) | drop-gated | hero recruitment through Exchange, at `(2^n)×10` = **20/40/80/160** by grade |

Plus three pure gates that are not currency but behave like it: **Fuel** (오르니톱터
연료), **Helium capsules** (헬륨 캡슐), **Mirage shards** (신기루 조각).

### 1.1 골드 vs 루피 — settled

**There is no separate "Gold" currency.** The namu wiki and the English wiki use
the *same word* for the soft currency. "골드" appears only as (a) loose player
synonym for 루피 in forum speech and (b) a **Market corner name** — 비밀 코너 at
**5 골드**, 루피 코너 at **20 000**. The arena ladder's third column is **녹색 만다**
— green Manda — *not* 골드.

⇒ The replica's `user.gold` **is** the Rupee wallet and `IT_CO` **is** the Rupee
icon. That is correct and should not be "fixed". *Caveat: rests on two corpora
(vsfan 2019, namu 2017–2021); no native string table could be checked, because
`native-all-strings.tsv` is printable-ASCII with zero Hangul.*

---

# 2. INTERACTIONS — what compounds, what cancels, what is a false friend

This section is **the synthesis**. It is mine, derived from the two ledgers, and
is labelled as such.

## 2.1 🔴 THE FUEL ERROR COMPOUNDS WITH THE STAGE-COST ERROR, in the same direction

Two independently confirmed defects, which reinforce rather than cancel:

| | replica | original | error |
|---|---|---|---|
| fuel per 5 Manda | **10** | **60** | **6× cheap** |
| AP cost per stage | **1** | **6–12** | **6–12× cheap** |
| fuel regeneration | 1 / 300 s | 1 / 360 s | **20 % faster** |
| fuel cap | 50 | 60 | 17 % lower |

**Neither error is visible alone.** A full 50-stage campaign run costs the
replica **50 AP**; the original costs **300–600 AP**. Even at the replica's
*higher* regen rate the campaign is effectively **ungated** — which is exactly what
has been observed: battles being lost to idleness rather than to fuel, and AP
sitting at 45–60/50 across whole sessions.

**The AP interval/cap errors partly mask each other**, which is why they read as
"roughly right": 50 fuel at 1/300 s and 60 fuel at 1/360 s are close in *time to
full* (4.2 h vs 6 h) while differing 20 % in rate. **Do not fix one and assume the
other improves.**

**Three independent places carry 60 as the fuel quantum**, which is strong:
the **60-fuel ticket**, the **60-fuel guild support cap**, and the **60-fuel
bundle**. The 60 is real; 10 is the replica's number.

## 2.2 🔴 TRACES ARE EXACTLY 2.0× TOO EXPENSIVE — a whole recruitment loop

Three axes, not one, and they must not be collapsed:

| axis | value | what it is |
|---|---|---|
| **requirement** | **20 / 40 / 80 / 160** by grade | traces needed to recruit — `(2^n)×10` |
| shop price | 75 chips | fight-chip price per trace |
| **worth** | 20 / 100 / 300 | stated trace value column |

The replica's `collect_qty` is **10 / 20**, i.e. **exactly half the requirement**.
The replica therefore grants half the intended traces, so a hero costs **twice as
many searches** as intended. Combined with capsule costs of **10 / 32 / 30** by
grade, the Search economy is uniformly ~2× too expensive to enter.

**A live hazard, not a hypothetical:** `search-battle.ts:57` **throws at load
time**, so this is not a dormant constant.

## 2.3 🔴 THE STAR CHEST MAY BE AN ENTIRE PROGRESSION PATH — and the replica deletes it

This is the most consequential *structural* finding, and it is unresolved.

**Agreed by two independent classes** that the per-region structure is
**three chests at 10 / 20 / 30 total stars**:
- **[C]** `vsfan Expedition_Area`, English wiki, paragraph **byte-identical across
  three Wayback captures** 46 and 116 days apart, three different digests (the page
  was edited in between) — a maintained statement, not one lucky revision.
- **[R]** the client's own arithmetic: `CSRGameStage::ShowReward` draws labels
  `S`, `2S`, `3S` with `S = GetStageCnt(area)`, and both the claimable test
  (`:3218`) and the request gate (`:1572-1574`) compare progress against
  **`S * (i + 1)`**. With `S = 10` that is **10 / 20 / 30**.

**⇒ This is the first external confirmation of the replica's own
`achieve_cnt = stageCount × (index+1)` derivation**, which until now rested on
native decomp alone.

**But the 30-star payout has two incompatible answers:**

| source | locale | date | says |
|---|---|---|---|
| `vsfan Expedition_Area` ×3 | EN | 2019-08 / 10 / 12 | **the region's own hunter** |
| namu main page | KO | spans 2017–2021 | **만다나 의뢰서** (Mandaring commission) |
| `vsfan Guide_to_Blustone` | EN | 2019-09-23 | the hunter comes from **beating the region boss** — a *different* trigger |

Three readings survive and the sources do not choose: (1) both true of different
things — hunter is the boss reward, chest pays a commission; (2) both true of the
same thing — stage 10 at 3★ *is* the boss clear and pays both; (3) one era changed
it.

**What is not in doubt:** the threshold exists, it is the last of three, and
**something is paid**. Its identity is **[?] — two sources, two answers.**

**⇒ Consequence:** if reading (1) or (2) holds, there is a **deterministic,
gacha-free path to region hunters** that the replica does not implement — it pays
**gold** at all three (`FIXTURE_CHEST_ITEMS` 300/200/100, `card_list: []`
deliberately). **Fifteen payout cells — 5 areas × 3 thresholds — are all [?].**
Not one payout in the entire campaign reward system is known.

**Do not resolve this by picking the likelier-sounding one.** The right move is to
leave it labelled and, if anything, publish *both* candidates in the notes field.

## 2.4 🟠 FREE MANDA IS A HARDER CONSTRAINT THAN THE REPLICA MODELS

The split is implemented (`iap_qty` / `free_iap_qty`, absolute receipts), which is
good. But the **sink constraint is not**:

- **4★ Transcendence Tickets are buyable with FREE Manda only** — [C].
- Free Manda comes from **only two places**: the FC rank ladder (**800 → 50**) and
  the FC tier ladder (**flat 2** per tier).
- Free Manda's documented sinks: gacha **300/bundle**, fuel 5, abyss reset 30.

⇒ A player who spends free Manda on bundles **cannot buy the 4★ ticket**, and the
replica has no notion of that competition. At 6 tiers that is ~12 free Manda per
week against a 300-Manda bundle — the tension is real, and it is the reason
"which Manda do I spend" is a genuine strategic question rather than a formality.

## 2.5 🟡 THE RAISE / SKILL LADDER HAS A FREE BAND THE REPLICA ZEROES EVERYWHERE

Both ledgers record a **free band**: Raise materials are **0 cost at levels 1–4**,
and skill-training materials go **non-zero from level 5**. The replica publishes
**0 materials in all 200 skill rows** — **184/200 rows wrong**.

⇒ This is the same structural fact seen twice: **the original gates materials
behind level, and the replica gates nothing.** Early progression was meant to be
gold-only so the material economy engages later. As shipped, the material axis does
not exist for the player at all.

## 2.6 🟡 TRANSCENDENCE IS THE ONLY SYSTEM WITH A COMPLETE COST LADDER

4 grades × 3 steps, crystals / fragments / gold — and **gold is exactly
`1000 × crystals` at every single rung**. That internal consistency is what makes
it trustworthy, and it corroborates the separately measured **T1 factor
×1.0994** (three stats agreeing to 0.139 %).

But **`awk_step` is pinned to 0** in the server and the server hard-refuses
`awk_step > 0` in three places, so **the whole ladder is unreachable**. Only the
chest Transcendence Tickets 912/913/914 exist as items.

⇒ This is the clearest *high-value, fully-specified, entirely unreachable* system
in the game: the data is known and the code forbids it.

## 2.7 ⚪ FALSE FRIEND — two XP endpoints that look like a contradiction

`hunter-levels.ts:8` publishes **2900 for all grades**; the community ladder says
**200·R!** = 200 / 400 / 1200 / 4800 / 24000. The 2900 is inside the 1★→2★ band,
so it is not "wrong by an order of magnitude" — it is **the 1★ endpoint applied to
every grade**, i.e. grades 2–5 are under-paid and grade 1 is right. The lane scored
this **8.3×–14.5× with opposite signs** because it compared against each grade's own
endpoint. Both readings are the same fact seen from different ends.

**⇒ Fix the shape (per-grade), not the number (2900).**

## 2.8 ⚪ A REAL WEEKDAY BUG IN TWO SYSTEMS

Replica weekly anchors: **Thursday** (arena) **and** Monday (mirage). Original:
**Sunday** for the arena reset; **daily** for Mirage. Two systems, two different
wrong days — so there is no single constant to correct, and fixing one leaves the
other.

---

# 3. THE ONE TABLE THAT MATTERS MOST — implemented wrongly vs not implemented

**27 of 33 native cost-bearing routes are absent from `server-ts/src`.**

That sounds alarming and is mostly not: **not implemented** means *there is nothing
to fix* — the number does not exist, and "not implemented" and "unknown" are the
same fact seen from two ends. Eleven of the twelve absent systems have **no original
value recovered either**.

| | count | meaning | action |
|---|---|---|---|
| **not implemented** | 12 systems | nothing to correct | recover the number, or leave absent |
| **implemented wrongly** | **11 constants** | the replica published a value and it is wrong | **fixable today — the original number is known** |
| **fabricated success** | **4 routes** | ⚠️ **corrupts state silently** | refuse, do not mock |

The third row is the dangerous one. **A state-changing verb answering
`result_code: 1` is not "absent" — it is a fabricated success.** Currently:
`/shop/SellCard`, the three gem-gacha references, and the four unlisted gacha
banners. AGENTS §26 already proved a mock on a shop route renders a **popup that
is empty** — the harm is invisible, which is exactly why it survives.

### The eleven wrong constants

| # | constant | replica | original | error |
|---|---|---|---|---|
| **X1** | RankUp gold | 1000/source flat | 1000/1500/**4000**/15000 per source | **4× at 3★→4★**, and wrong *shape* |
| **N1** | AP bundle | 10 fuel / 5 Manda | **60** | **6×** |
| **X3** | AP gold tier | 100 | **5000** | **50×**, 8.33× worse rate |
| **N2** | AP interval + cap | 300 s, cap 50 | **360 s, cap 60** | 1.20× + 4 smaller |
| **N4** | Skill materials | 0 in all 200 rows | non-zero from level 5 | **184/200 rows** |
| **X2** | Skill gold | 100 × level | 800 at Lv35 (one frame) | **4.5×** |
| **N9** | Trace requirement | 10 / 20 | **20 / 40** | exactly **2.0×** |
| **N5** | AP per stage | 1 | 6–12 | 6–12× |
| **N6** | EXP per stage | 10 flat | 7–32 | outside any band |
| **X6** | XP endpoint | 2900 all grades | 200·R! | shape, not magnitude |
| **N8** | Weekly anchors | Thu **and** Mon | **Sunday**; Mirage daily | two systems, two wrong days |

**X1 is the highest value and it is a *shape* error, not a scale error.** A first-party
image frame shows **8000 for 2 fodder** and **12000 for 3 fodder** on the same
target — `8000/2 = 12000/3 = 4000`. Two different counts yielding the same
per-source figure is what licenses the division. The original per-source price is
**not constant** (1000 / 1500 / 4000 / 15000), so **no single scale factor fixes
it**. Notably the *fodder counts* in the same file are already correct — the defect
is confined to gold.

**X3 compounds N1**: a 50× cheaper gold tier *and* a 6× cheaper Manda tier means the
replica's fuel is cheap on both currencies at once.

---

# 4. THE CAMPAIGN'S OWN DROP TABLE — what a stage actually gives

**[C]**, three independent sources. A stage's material is determined by its
**last digit**: units digit **1–5 and 7** → one material family; **6** → a
different one; **8** → another; **9** → the region's own hunter traces.

Material grades and shop values are dated **2019-08-21**. **Region unlock gates**
exist and they gate the star chests. The **190-stage** figure is a *scope fact*
about the live game, **not** a reward — the recovered campaign table is 50 stages
(5 areas × 10). That 50-vs-190 discrepancy is **[?]** and unresolved.

---

# 5. RANKED GAP LIST — what would most change the replica

| # | gap | why it matters | what would settle it |
|---|---|---|---|
| **G1** 🔴 | **Login Bonus / attendance calendar** | the largest untouched reward table; the replica's is a 28-entry local invention, no catch-up, no cycle | the original attendance table |
| **G2** 🔴 | **the 15 campaign star-chest payouts** | the only reward node in the entire flow graph with **no content at all**, and the one the replica invented | the original `achieve_reward[]` reference row |
| **G3** 🔴 | **30-star: hunter or commission?** | determines whether a gacha-free hunter path exists | boss-vs-chest ordering evidence |
| **G4** 🟠 | 50 vs 190 stages | the campaign's true extent | a dated stage list |
| **G5** 🟠 | every guild price | guild is structure-only; **no price recovered** | `GetGuildPrices` original |
| **G6** 🟠 | Mirage floor rewards + shop prices | Mirage is live in the replica but has no cost model | original Mirage shop table |
| **G7** 🟠 | fishing `fish_id` / prices / grades | `ParsePrice` wants all four; **no ID exists in any corpus** | an original `ParsePrice` capture |
| **G8** 🟡 | Special Supply contents and triggers | currently a local 10-gold rule | original supply table |
| **G9** 🟡 | Veteran ladder points (two irreconcilable figures) + arena entry cost | — | a dated ladder |
| **G10** 🟡 | the 4 fabricated-success routes | **corrupts state silently** | — *actionable now: refuse them* |
| **G11** 🟢 | Market corner contents | — | original corner table |
| **G12** 🟢 | gacha odds in the server | — | — |

### Still unknown, stated plainly

Interior per-level XP thresholds · awakening **heart** prices and heart *item
reference* · every guild price · Jewel Mine price · skin price · fish ids/prices/
grades · gem gacha prices · the 45– band of the skill ladder · **the four-material-
family identity question** (all four tables in the recovered extraction are
byte-identical, so "the four cost the same" is **UNVERIFIED**) · 20-vs-30 level cap ·
4★→5★ at 60 000 vs 15 000 · the 255-mandaring anomaly.

---

# 6. WHAT TO DO, IN ORDER

1. **Refuse the 4 fabricated-success routes.** They are the only defect that
   corrupts state silently and invisibly. No number is needed to fix this.
2. **Fix N1 + X3 + N5 together, not separately** — the fuel/AP economy is one
   coupled error (§2.1) and fixing one alone makes the system *look* improved
   while remaining wrong.
3. **Fix X1 as a shape**, using the 1000/1500/4000/15000 ladder. Do not apply a
   constant multiplier; there isn't one.
4. **Fix N9 and `collect_qty` together** — 20/40/80/160 versus 10/20 is a single
   2.0× relationship spanning three sites.
5. **Fix X6 as a shape** (per-grade `200·R!`), not by editing 2900.
6. **Leave the star chests labelled.** Do not pick a 30-star payout; two credible
   sources disagree and a wrong guess deletes or invents a progression path.
7. **Do not** "fix" `user.gold` to mean something other than Rupee — that is already
   correct (§1.1).

### Standing refusals, restated because they bind items above

- `fc-native` **§1.4 forbids setting honor values from the arena reward tables.**
  The arena data in the cost ledger is **evidence to keep**, not an instruction.
- `exp-ladder` **§4 forbids conflating RankUp gold with the star-advancement
  ladder.** The X1 row keeps fodder counts, the per-grade ladder and the derived
  per-source price as **three separate rows**; the pixel frame makes (b)→(c) a
  division *within one quantity*, not a conflation across two.


---

# 7. LOGIN BONUS — G1 PARTLY CLOSED, and the replica matches NONE of it

`login-bonus-calendar-2026-10-09.md`. The prior ledger called this "the largest
untouched reward table in the project" and recorded
`Hunter_Supply_Office` as "a navigation stub with no reward content at all."
**That was a retrieval artefact** — the page exists and carries both tables (it was
merged with `Hunter_Supply_Station`; the stub is the *other* page). Worth recording
because it is the second time this session a "no content here" verdict turned out
to be a fetch failure.

### 7.1 Daily Rewards — week 1 of the cycle

**[COMM] ×3 byte-identical captures** (2019-08-21 / 10-15 / 2020-08-08, all
`oldid=6016`), post-patch **1.0.8.0 (2017-08-03)** "New rewards for player
attendance have been added":

| day | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| reward | **Rupee 3000** | **Evaluation Request ×5** | **Rupee 5000** | **Fuel Ticket ×2** | **Challenge Invitation ×2** | **Elite Request ×1** | **Metron Crystal ×1** |

**Plus on every daily claim: +20 Veteran points.**

### 7.2 A SECOND, separate ladder — Cumulative Attendence Dates

**[COMM] ×3.** **5 / 10 / 15 / 20 days** → **Rupee Lottery Ticket ×2**, then
**Elite Request ×1**, **2-3★ Request ×1**, **3★ Request ×1**. The prior ledger
recorded "no amounts survive" for this — they do.

### 7.3 The 28-day cycle is REAL, not a fixture

Three independent sources (forum 292924 "28 checked in based on cumulative
attendance"; 1368000 "4★ Selection every 28 days"; 1393319 "4* selection scroll
monthly") **plus two players independently reading "I am on day 28" off the UI**.
This **reconciles** the old weekly-vs-monthly dispute rather than contradicting it:
**the 7-day week above is week 1 of a 4-week cycle.** Weeks 2–4 remain `[?]`.

### 7.4 🔴 What this means for the replica

**9 of 28 cells are now known and the replica matches none of them.**

| | replica | evidence |
|---|---|---|
| day 1 | 100 gold | **Rupee 3000** |
| day 3 | 100 gold | **Rupee 5000** |
| days 2, 4, 5, 6 | 100 gold | **no gold at all** — requests/tickets instead |
| day 7 | 100 gold | **Metron Crystal ×1** (contested, see below) |
| Veteran | — | **+20 every claim** (replica has this right) |
| day boundary | **UTC midnight** | **contradicted** — per-player 16:00-vs-10:00 and VS's own "under investigation" |
| cumulative ladder | absent | 5/10/15/20 → the four rewards above |

**Gold appears on NO recovered day except days 1 and 3, and at 3000/5000 — not
100.** The replica's flat 28 × 100 gold is wrong in *magnitude*, in *composition*
and in *day boundary*. This is the single largest correctable reward block found.

### 7.5 G9 is half-solved — and the conflict was a SUM, not a contradiction

The wiki's "**40 Veteran points/day**" is not a rival figure: it is
**20 (attendance) + 20 (daily goals)**. The **20** is confirmed by the wiki ×3
captures **and by three separate live native claims in this project** (+20 each).
The Guru-3 threshold conflict (**40 960 = 20·2¹¹**, self-consistent with that
page's own ladder, vs **67 520**, which is not) remains a likely era change.

### 7.6 Two things still contested — do not smooth them

- **Day 7 is contested across eras**: recovered **Metron Crystal ×1** vs a single
  *unanswered 2022 question* claiming a 4★ Selection. The prior ledger's
  "day-7 4★ Selection" row rested on that same question plus a thread about the
  rainbow-scroll *gate*, not the slot's contents.
- **Miss-day reset is `[UNKNOWN]`** and the sources actively disagree. One player
  reports 1069 sign-ins over ~3 years, which argues against a strict streak.

### 7.7 Honest negatives

**No `[FIRSTPARTY]` image frame.** Three named attendance screenshots attempted; 0
rows under exact-URL CDX **with a same-run passing control**; prefix queries 503.
Korean and Chinese sources were **genuinely unreachable this session** — namu 403,
CDX empty, no browser attached, and web search returned nothing even for its own
control query. **The namu attendance page G1 named is still unread**, so this is
English-only. The lane also caught four instrument faults of its own, including a
CDX false negative **reproducible within one session** and a codepoint self-check
that proved it had typed `이벤트` from memory instead of slicing it — recorded
rather than hidden, because all its namu results are negatives and a wrong term
can only produce a false negative.
