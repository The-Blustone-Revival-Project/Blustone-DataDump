# Trace threshold scale — `collect_qty` adjudication (2026-10-05)

**Question put to this lane.** Audit row **E8** / register **X3**:
`local_sylvester_trace.collect_qty = 10` and `local_gerard_trace.collect_qty = 20`
against [NAMU §1.3] "Traces for fixed recruit: 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160 —
formula (2^n)×10". Both local values are exactly half; the audit calls this
**CONTRADICTED** and notes that `collect_qty` is *also* reused as the guided-Search
reward quantity, so one constant feeds two systems.

**The adjudication asked for.** Is the NAMU ladder a **per-STAR** ladder while
`collect_qty` is a **per-HUNTER** constant (i.e. one of the two readings must be
wrong), or not?

**Answer in one line.** The dichotomy is false: natively and in shipped copy
`collect_qty` *is* a per-hunter threshold that is **graded by the hunter's star**,
so NAMU's star ladder and the fixture's `collect_qty` are **the same quantity on
the same axis** and can differ only in value. The factor-2 arithmetic is real but
the "single scaling decision" inference is **not sound**: the NAMU corpus is
internally inconsistent, and the only external anchors (official 2018 ★3 trace
grants) fit the **local** ladder, not NAMU's.

**Verdict on the factor-2 claim: NOT UPHELD as a demonstrated error; the audit row
should be softened from CONTRADICTED to "shape corroborated, absolute value
unrecovered, one-index offset against one self-inconsistent wiki table".** No
doubling is warranted by anything in hand — and equally, **nothing in hand
recovers the original value.** See §2.6.

**[AMENDED 2026-10-05 — `trace-rarity-vote-2026-10-05.md`. Verdict unchanged:
still NOT UPHELD. Two bounds added so this header is not misread later.]**

1. **The "constant factor of 2" signature is specific to the NAMU-vs-local
   pair.** The constant-2 reading (2.00 / 2.00) exists **only** between
   `[NAMU] §1.3` and the local fixture. Under the counterfactual that the
   `vsfan` wiki's 20/100/300 *were* the same quantity, it would be
   **non-constant against NAMU (1.00× / 2.50× / 3.75×)** — i.e. it would attack
   **NAMU**, not the fixture. Do not quote the constant-2 observation as a
   general property of the trace scale. See vote §2.3.
2. **The `vsfan` 20/100/300 is NOT a second ladder and NOT commensurable.** It
   is a per-trace rarity **`Value`** (unit worth); `collect_qty` is traces
   **required per hunter** (a divisor). The corpus therefore still holds
   **exactly one** transcription of the 20/40/80/160 ladder. See vote
   §1.1–§1.5, §2.2, and the new ledger group in §2.8.

**Actions taken: none.** No fixture, server source, seed, state file, APK,
emulator or original asset was modified. **`polluted-observations.md` was
deliberately NOT appended this run** (parent mirrors).

**Coverage effect: zero.** Heroes 1/113, accessories 1/100, monsters 0/22 —
unchanged. Nothing below is a hero, accessory or monster base stat.

---

# 1. PURE — evidence bearing on the true `collect_qty` scale

Reproduced as stored/transcribed. No inference. Reasoning is §2.

## 1.1 What `collect_qty` natively **is** [NATIVE]

| Fact | Address / source |
|---|---|
| The threshold is a property of the **item reference row**, copied per hunter: `CSRCardInfoContainer::PostProcess` walks the item map, tests `node+0x20 == use_type 3`, resolves `node+0x60` (`INFO.effect`) against the hunter reference map, writes the item's own id into `cardInfo+0x18`, and **copies `node+0x28` (`INFO.collect_qty`) to `cardInfo+0x4c`** | `analysis/research/hunter-trace-item-binding.md:7-13` (`G87d348`, `G87d3c8/G87d3ca`) |
| The consumer reads it as a **per-hunter required-trace count** and divides by it: `Gce1252 r1 = CardInfo.collect_qty` / `Gce1256 r0 = owned qty` / `Gce125c divide` / `Gce1262 store max exchange count +DC`, i.e. **max hunters = floor(owned / collect_qty)**; the slider then initialises `1..max` and **debit = count × threshold** | `analysis/research/trace-recruitment-contract.md:44-46` |
| The exact request is an **owned trace item instance** + `cnt` = **number of hunters**, not traces | `trace-recruitment-contract.md:7-13,46`; `server-ts/src/trace-exchange.ts:29` |

So `collect_qty` is **per trace item / per hunter**, not a single global constant.
That is settled by native code and is not in dispute anywhere in this project.

## 1.2 The same item row carries **both** a grade and the quantity [NATIVE schema]

`CSRItemInfo::SetItem` (`Gaefe10`) parses, in one base record, strict strings
`id / name / desc / thumbnail_id / effect` and **numeric `rank`, `use_type`,
`sell_price`, `collect_qty`** (`analysis/research/shop-fuel-contract.md:20,31`;
schema cross-referenced from `shop-bp-contract.md:21`, `shop-fuel-implementation-audit.md:29`).
A per-item **grade** field sitting beside a per-item **required-quantity** field
is precisely the layout a **per-grade ladder** needs. (This is a schema fact; it
does **not** prove that `collect_qty` is a function of `rank`.)

## 1.3 Shipped 2.8.0.1 client help: per-hunter, grade-graded, **no numeral** [ORIGDATA, CURRENT]

Source: shipped 2.8.0.1 `UI_CSV.jet` `HELP_DATA`, Hunter-Search records. Offsets
and SHA-256 pinned in `analysis/research/base-stats-visual-hunt/help-2_8-sweep-2026-10-05.md:190-249`
(EN `desc1` value offset **151441**, 485 chars, SHA-256 `fbe368a6…`; KO offset
**151094**; JA **151953**; SC **152290**; TC offset **151048**).

| Locale | Verbatim (markup preserved as shipped) |
|---|---|
| **EN** | "• A hunter **can be recruited** after collecting the required **amount of its traces**." / "Hunter Searches involve **four consecutive battles** with the respective hunter." / "Based on your general stage clearance, new hunters can be searched." |
| **KO** | "• 일정 수량 이상 모으면 **해당 헌터를 확정적으로 획득**할 수 있는 헌터의 흔적을 수집하는 콘텐츠입니다." / "헌터 수색은 해당 헌터와의 **총 4회의 연속적인 전투**를 통해 이루어집니다." |
| **JA** | "一定数以上を集めると、**該当ハンターを100％獲得**できる、ハンターの痕跡(シュプール)を収集するコンテンツです。" |
| **SC** | "在收集一定数量的猎人痕迹后，**可确定获得该猎人**。" |

Three load-bearing facts, all first-party and current:

1. **The quantity is bound to the individual hunter** — "its traces", `해당 헌터`,
   `該獵人`, "that hunter". This is the shipped client stating the per-hunter
   semantics of the very quantity the fixture publishes.
2. **The system is a guaranteed/fixed recruit** once the amount is met —
   "확정적으로 획득", "100％獲得", "可確定獲得". This is the *same* semantic as
   NAMU's `확정 섭외` ("fixed recruit"), which is what identifies NAMU §1.3's row as
   being about **this** quantity and not some other trace price.
3. **No numeral is shipped.** The prose deliberately says "a certain amount" in
   all five locales. The full numeral census of the 22 new `CONTENTS12_*`…
   `CONTENTS15_*` records (`help-2_8-sweep-2026-10-05.md:2635-2649`) contains, for
   the Search records, only: `CONTENTS12_2` → **4** (four consecutive battles; max
   **4** reward boxes) and `CONTENTS12_4` → **1**, **10** (friend window **1 h**,
   at most **10** friends, **an extra trace for every two friends**).
   `CONTENTS12_1/3/5/6` carry **zero** prose numerals. There is **no trace
   requirement count anywhere in the shipped 2.8.0.1 help**, and §2.1 of that
   sweep states it outright: "no capsule cost, **no trace requirement count**, no
   drop rate, no Search cooldown, no daily cap number."

One more first-party grading statement from the same shipped corpus
(`help-2_8-sweep-2026-10-05.md:2658-2661`): **`CONTENTS12_3`** says the Search
**cost scales with the grade of the hunter being searched** — EN reads "The higher
the **Hunter Level** being searched", KO/JA read *grade*. The lane flags this as
an EN-vs-source divergence that must **not** be resolved by picking one; recorded
here as evidence that the Search economy is **grade-graded at all**, not as a
statement about traces specifically.

## 1.4 Official EN guide: the trace tiers are explicitly 2★ and 3★ [ORIGDATA, PRE]

`share_en/197745` "Guide to Blustone", transcribed verbatim, dated PRE-2019-09-05
(`share-en-guide-2026-10-05.md:29-35, 221-231`):

> "Hidden and Normal Ruins are used to obtain the traces of **natural 3-stars and
> 2-stars hunters** respectively. […] Right now, the only 3 star hunters for whom
> you can collect traces are **Hermes, Karl, Nene and Athena**."

> "The first is that there are **4 waves**, with each wave getting progressively
> more difficult. At the end of each wave, you will face off the hunter whose
> ruin you are doing. For wave 1 to 3, the hunter does not use his skill, but the
> final boss in wave 4 does."

The community FAQ adds (POST-2019-04-01, `L235`) that **4-star traces** are sold
in Mirage/Blitz shops and that the Fight Club shop stocks 4-star traces. So the
original trace ladder spans **2★ / 3★ / 4★** — consistent with §1.3's shipped
"grade-graded" statement. No threshold numeral in any of these texts.

## 1.5 Official event evidence — the four ★3 trace anchors [ORIGDATA, all PRE-2019-09-05]

All four are body-read captures of `bs.visualshower.com` `event_en` posts by the
official account (`Natara`). Full provenance, byte-level quotes and URLs are in
`event-board-bodies-2026-10-05.md` §1.1/§1.2, `event-board-bodies2-2026-10-05.md`
§1.1 and `official-posts-2026-10-05.md` §1.1. Nothing here is paraphrased.

### (a) Rice cakes — ★3 traces **sold**, 15 per box, jackpot 40

`document_srl` **989396**, posted **2018.09.20 14:34**, event **Sep 20th 15:00 ~
Sep 28th 15:00 (UTC+9)**, archive
[2018-10-25 17:57:40](http://web.archive.org/web/20181025175740/http://bs.visualshower.com/event_en/989396)
(also `20180925213940` in `index.php` form):

> "You can obtain rice cakes as you clear the general stages! The collected rice
> cakes are exchangeable for equipment modification materials and **★3 hunter
> traces**.
>
> You can exchange **15 rice cakes for 1 box**, and usually **3 ~ 5 traces** will be
> found in a box, but if you get lucky, you will find **40 traces** just in one box!"

| Box (verbatim name) | Contents (verbatim) |
|---|---|
| Scorching Rice Cake Box | 1 Flammable Material + **3~40** Fire type **★3** hunter traces |
| Frozen Rice Cake Box | 1 Coolant + **3~40** Ice type **★3** hunter traces |
| Glittering Rice Cake Box | 1 Lightning Box + **3~40** Lightning type **★3** hunter traces |

**Limit:** the body's 17-row `<Accumulation Rank Prizes>` ladder lists prizes per
accumulated *rank band*; it never states how many rice cakes a band costs, and no
rice-cake income rate appears anywhere. So the rice-cake economy has **no
recoverable scale anchor** beyond the 15-per-box price.

### (b) Walnuts — ★3 traces **sold**, 95/125 per box, jackpot 40

`document_srl` **1003633**, posted **2018.10.12 14:56**, event **Oct 12th 15:00 ~
Oct 26th 15:00 (UTC+9)**, archive
[2018-10-25 01:56:33](http://web.archive.org/web/20181025015633/http://bs.visualshower.com:80/?mid=event_en&document_srl=1003633&l=en):

- Walnut income (verbatim): clear **5** General Stages → **1** walnut
  (*dispatching counts*); clear **1** Hunter Search → **3**; clear **1** Abyss → **5**;
  **1** scroll recruit → **6** (excludes Evaluation Request); **Manda** recruit → **45**.
- Exchange (verbatim): **95 or 125 walnuts** per trace box; each box "normally holds
  **2~4 traces**, but a lucky person might get **40 traces** from one box!"
  - Box with **Crocus'** Traces — **125**
  - Box with **Apollon's** Traces — **95**
  - Box with **Dino's** Traces — **95**
  - Box with **Calibur's** Traces — **95**
  - Box with **Therapy's** Traces — **95**

**Limit (stated plainly):** the body attaches **no star label** to these five
hunters. Their ★3 status is **[COMMUNITY-SOURCED]** from the recovered catalogue
(`analysis/catalogue/INDEX.md` `R★` column: Crocus `058`=3, Apollon `055`=3, Dino
`054`=3, Calibur `053`=3, Therapy `050`=3), and `INDEX.md:503` marks the rarity
column "[COMMUNITY-SOURCED] — wiki only, not in any recovered table". The walnut
event therefore establishes a **trace unit price**, and a ★3 attribution that is
community-grade, not a first-party ★3↔quantity statement.

### (c) Halloween — ★3 traces **granted**, 10 per 10+1

`document_srl` **1008972**, board date **2018.10.19**, event **October 19th 18:00
~ November 2nd 15:00 (UTC+9)**, archive
[2018-10-25 01:57:03](http://web.archive.org/web/20181025015703/http://bs.visualshower.com/index.php?mid=event_en&document_srl=1008972&l=en):

> "- On 10+1 recruit, the following hunter traces will be given(UTC+9):
>   [Oct 19th 18:00 ~ Oct 26th 15:00] **10 traces of Jack-O'-Lantern**
>   [Oct 26th 15:00 ~ Nov 2nd 15:00] **10 traces of Broom Witch Denali**"

with, in the same body, the star labels
"Jack-O'-Lantern(**★3**), Broom Witch Denali(**★3**), Halloween Witch Riko(**★2**)".
**★3 and the quantity 10 are stated together in one first-party body.**

### (d) Halloween — ★3 traces **granted**, 40 as a weekly first-purchase bonus

Same body, same archive:

> "During the event, there will be a bonus gift with the **first purchase of each
> week(UTC+9)**!
>   - 1 Special Request, **40 Jack-O'-Lantern's Trace** (Oct 19th 18:00 ~ Oct 26th 15:00)
>   - 1 Special Request, **40 Broom Witch Denali's Trace** (Oct 26th 15:00 ~ Nov 2nd 15:00)"

**40 traces of a named ★3 hunter, from the official account, as a headline bonus.**
This is the single most directly relevant numeral in the whole corpus.

### (e) October Hot Time — ★3 traces **granted**, 10 per 10+1 (second, independent event)

`document_srl` **995273**, posted **2018.09.28 14:30**, event **Sep 28th 15:00 ~
Oct 2nd 15:00 (UTC+9)**, archive
[2018-10-21 13:44:17](http://web.archive.org/web/20181021134417/http://bs.visualshower.com/index.php?mid=event_en&document_srl=995273&l=en):

> "★3 Santa Clauster / ★3 Santa Girl Rebecca / ★2 Halloween Riko" … and
> "**10 Traces of Santa Girl + 10 Traces of Santa Clauster on 10+1 Recruit!**"

Again ★3 and the numeral 10 in one first-party body, from a **different** event.

### 1.6 Unit-price arithmetic on the transcribed official figures (arithmetic only)

| Event | Currency per box | Traces per box | Implied currency **per trace** |
|---|---|---|---|
| Walnuts, 95 boxes | 95 | 2 / 3 / 4 / 40 | **47.5 / 31.7 / 23.75 / 2.375** |
| Walnuts, 125 box (Crocus) | 125 | 2 / 3 / 4 / 40 | **62.5 / 41.7 / 31.25 / 3.125** |
| Rice cakes | 15 | 3 / 4 / 5 / 40 | **5 / 3.75 / 3 / 0.375** |

Walnut income reference points (official): **3** walnuts per Hunter Search, **1**
per five general stages, **45** per Manda recruit. These are the only official
trace *prices* anywhere in the corpus; there is **no official statement of a
required trace count** in any event body.

## 1.7 The only ladder-shaped source, and its internal contradictions [COMM, ERA-UNRESOLVED]

Source: `d.namu.moe/w/블루스톤/헌터` (mirror of `namu.wiki/w/블루스톤/헌터`;
namu.wiki direct = 403; mirror 200, 1475 text lines, fetched 2026-10-05; CC
BY-NC-SA 2.0 KR). Raw Korean preserved, translations the lane author's
(`namu-kr-blogs-2026-10-05.md:15-20, 64-99`).

| Where | Verbatim/recorded reading | Grade |
|---|---|---|
| **§1.3** | "**Traces for fixed recruit: 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160 — formula (2^n)×10.**" | the ladder under audit |
| **§1.3** | "**Self-overcoming (자기극복, 3★+): metron-crystal / fragment pairs per step:** 1★ 5/50, 15/150, 45/450; 2★ 7/70, 25/250; 3★ 9/90, 30/300, 80/800; 4★ 12/120, 40/400, 110/1100. Fragment = 10× crystal." | adjacent ladder, same page — **doubling does not hold here** |
| **§1.4** | "Harley (4★ defender) mirage-only: **300 mirage fragments → 3 traces/day → 160 traces ≈ 32 days** (≈2–3 months per wiki); achievement quest grants **5 traces per 10 mirage floors**" | the ladder **applied operationally** to a 4★ → 160, consistent with §1.3's 4★ row |
| **§2** (different page, `d.namu.moe/w/블루스톤`) | "**Helium capsules:** 1★ **2/search × 5 searches (10 total)**; 3★ **15/search × 2 searches (30 total)**; max **4 reward boxes per search, 2 traces per box** (≤8 traces/run)" | **inconsistent with §1.3** — 1★ 10 ≠ 20 and 3★ 30 ≠ 80, under any index shift; see §2.5 for the ambiguity |
| §2 (safest transcription) | "helium **2/8/15 per grade** with **5/4/2 searches**, 4 waves, 2 traces/box (**min 2, max 8**)" (`polluted-observations.md:700`) | raw triple; grading unverified |
| §1.4 | "Request (의뢰서) types: 초급 (**1–3★ traces**, ≤5 per ticket, usable 1–10 at once); 고급 (1–4★ recruit); **특급 (2–4★ fixed)**; 전설 (3–4★ fixed)" | the trace-recruit path is itself **star-graded** |
| §1.2 | "Beckhen (051) … obtained via **Fight Chip shop traces (375 chips per 5 traces**, shop restocks every 6h)" | purchase price, ★4 |
| §1.3 | "**Lily&Lala traces: 12 첨쥐 코인 → 5 traces**" | purchase price, ★4 pair |
| main page | "honor medals **700 medals per 8 traces (★4)**, **350 per 8 (★3)**" | purchase price, ★-graded |

**Net:** the corpus asserts, for the same quantity, ★1 = 20 and ★3 = 80 on one page
and ★1 = 10 and ★3 = 30 on another. Only the 4★ value (160) appears twice and is
consistent. **The source contradicts itself at exactly the two grades where the
local fixtures disagree with it.**

## 1.8 Negative evidence — the number is genuinely absent locally

| Search | Result |
|---|---|
| `collect_qty` / `collect_qt` / `TRACE_QTY` across `analysis/recovered-data/**` (incl. `leveldb-tables/all-tables.json`) | **0 matches** |
| `collect_qty` across `analysis/extracted/**` (base-APK assets) | **0 matches** |
| Shipped 2.8.0.1 `UI_CSV.jet` help, all 5 locales, all `CONTENTS*` | **no trace requirement count** (§1.3) |
| Native reference key index scan (`native-reference-key-index-scan.json`, `native-reference-cache-candidates.md`, AGENTS §124) | no separately named item/trace reference database; `UserData497`/`EtcData29`/`CDN23656` contain **zero** reference-route matches |

So the original `collect_qty` numeral is **unrecovered**, and the cheapest
remaining route to it is unchanged: a real `/reference/GetItem` row for a genuine
trace item id, or a native panel capture of the required count.

## 1.9 The local fixture, stated exactly as published [FIXTURE]

`server-ts/src/hunter-traces.ts:8-11`

```ts
{ id: "local_gerard_trace",   cardId: "005", rank: 2, name: "Gerard Traces",    collect_qty: 20 },
{ id: "local_sylvester_trace",cardId: "006", rank: 1, name: "Sylvester Traces", collect_qty: 10 },
```

Axis check (this matters for §2.1): the fixture's `rank` is **the catalogue's
`R★` draw-rarity**, not the training-whitelist stat rank —
`analysis/catalogue/INDEX.md` gives `005` Gerard `R★` = **2** and `006` Sylvester
`R★` = **1** (both `[COMMUNITY-SOURCED]`, `INDEX.md:503`). So the local ladder is
**already indexed on the same star axis NAMU uses**, one step lower.

Three consumers derive from the single `006` constant (the "one constant, two
systems" note in audit §2.3 is really one constant, **three** systems):

1. **Exchange threshold** — `HUNTER_TRACE_ITEMS[].collect_qty` → `/reference/GetItem`
   `item[].collect_qty` → native `CardInfo+0x4c` → slider max and per-request
   debit (`trace-exchange.ts:29`, `debit = count * trace.collect_qty`).
2. **Guided-Search victory award** — `search-battle.ts:8`
   `const GUIDE_TRACE_QTY = HUNTER_TRACE_ITEMS.find(row => row.cardId === "006")!.collect_qty`,
   used at `:57` and `:214` (guided wins award `GUIDE_TRACE_QTY`, ordinary wins 1).
3. **Tutorial `37/1` guided recruitment** — `state.ts:1231-1248` gates on a
   completed winning Search and then calls `exchangeHunterTraces({item_inst_id,
   cnt: 1})`, i.e. it **debits `collect_qty`** through consumer 1. So the tutorial
   gate's trace requirement *is* the exchange threshold.

---

# 2. UNPURE — reconciliation, adjudication, ledger

Inference only. Each item cites §1.

## 2.1 The key question: the per-STAR vs per-HUNTER dichotomy is **false**

The audit's §2.3 caveat — "the Namu row's exact semantics are not pinned (it may be
a generic 'fixed-recruit' ladder rather than a per-hunter recruit cost)" — is now
**closed**, and closed against the caveat rather than for it. Five facts, four of
them first-party or native:

1. `collect_qty` is a property of **one hunter's trace item**, consumed by that
   hunter's exchange (§1.1). It is not a global constant and cannot be.
2. The item row carries a **grade** next to the quantity (§1.2) — the layout a
   per-grade ladder requires.
3. The **shipped 2.8.0.1** help says the amount belongs to *that* hunter and that
   meeting it acquires *that* hunter ("its traces", `해당 헌터`, 100 % guaranteed)
   (§1.3), and separately that the Search **cost rises with the grade** of the
   hunter searched (§1.3, `CONTENTS12_3`).
4. The **official EN guide** says the trace tiers are the **2★ and 3★** hunters'
   (§1.4), with 4★ traces appearing later in shops.
5. NAMU's `확정 섭외` "fixed recruit" is the same "guaranteed acquisition on
   reaching an amount" mechanic the shipped help describes (§1.3), and NAMU's own
   request-type list grades that path by star: 초급 = *traces* at 1–3★, 특급 =
   *fixed* at 2–4★ (§1.7).

**Therefore** "NAMU's star ladder" and "`collect_qty`" are the **same quantity on
the same axis**: a per-hunter required-trace count tabulated by the hunter's star.
Neither reading is wrong; the only possible disagreement is the value, and the two
candidate ladders differ by exactly **one index step**:

| Star | local `10·2^(star−1)` | NAMU §1.3 `10·2^star` | ratio |
|---|---|---|---|
| 1★ | **10** (published, `006`) | 20 | 0.5× |
| 2★ | **20** (published, `005`) | 40 | 0.5× |
| 3★ | 40 (extrapolated, **not published**) | 80 | 0.5× |
| 4★ | 80 (extrapolated, **not published**) | 160 | 0.5× |
| 5★ | 160 (extrapolated) | — (NAMU stops at 4★; natural max is 4★ per NAMU §1.1) | — |

The audit's observation that "both local values are off by the same factor of 2 …
the signature of a single scaling decision" is **arithmetically correct and is
best explained as an exponent-convention offset (`n` vs `n−1`)**, not as two
independent errors and not as a demonstrated scale error. Only two of the four
local numbers are actually published; the 3★ row — the only grade with external
evidence — does not exist in the fixture at all.

## 2.2 What the official 2018 events actually pin down

Every official trace numeral recovered in this project concerns **★3** hunters.
That is a coincidence of corpus content, not a designed sample, but it happens to
land on the one grade where the two candidate ladders differ by a factor of 2 and
where one of them (80) is *published nowhere*:

| Official, body-read, ★3 | Numeral | Under local ladder (★3 = **40**) | Under NAMU §1.3 (★3 = **80**) |
|---|---|---|---|
| 10+1 recruit trace gift (Hot Time, Sep 2018) | **10** | ¼ of a recruit per bundle | ⅛ |
| 10+1 recruit trace gift (Halloween, Oct 2018) | **10** | ¼ | ⅛ |
| Weekly first-purchase bonus (Halloween, Oct 2018) | **40** | **exactly one recruit** | **exactly half** |
| Rice-cake box maximum ("if you get lucky", ★3 rows say 3~40) | **40** | **exactly one recruit** | **exactly half** |
| Walnuts box maximum ("a lucky person might get 40") | **40** | **exactly one recruit** (★3 is community-grade here) | exactly half |
| Typical box contents | 3–5 (cakes) / 2–4 (walnuts) | 6–13 boxes / 10–20 boxes | 16–27 / 20–40 boxes |

The strongest single item is the **weekly first-purchase bonus**: an official,
named, ★3-labelled **40**-trace grant. And it recurs — the maximum single box in
**two different** official events is also **40** for ★3 traces. Two independent
events using 40 as the "biggest sensible chunk of ★3 traces" is exactly what a
40-trace ★3 requirement predicts, and exactly what an 80-trace requirement does
not (it would make the largest number the game's own event copy could celebrate
be, twice running, precisely half of one recruit).

**This is design-plausibility inference, not proof.** No official body states a
required count. It is labelled as inference here and must stay labelled wherever
it is quoted.

The secondary inference — that the game's own **10**-trace quantum for ★3 (twice)
shows a base-of-10 quantum in the original ladder — is weaker but points the same
way, and coincides with the local 1★ value of 10.

## 2.3 Where the official boxes *cannot* discriminate (weak signals, kept explicit)

Using §1.6's per-trace prices and the official walnut income:

- A **40**-trace ★3 recruit costs **950–2,500 walnuts** (or **120–200 rice cakes**).
- An **80**-trace ★3 recruit costs **1,900–5,000 walnuts** (or **240–400 rice cakes**).

At 3 walnuts per Hunter Search, 80 traces is ~633–1,667 searches for one ★3
recruit — versus ~317–833 at 40. For scale, a paid 10+1 is 300 Manda and a single
is 30 Manda. **Both figures are event-scale sinks**, and the events plainly were
*not* the efficient route to a hunter (they were limited-time currency burns with
no rice-cake income rate recoverable at all, §1.5a). So the price data disfavours
80 only weakly and **cannot** settle it. Recording this so the §2.2 argument is not
over-read: §2.2 rests on the *roundness and recurrence* of 40, not on price.

## 2.4 NAMU §1.3's ladder is also weak on internal grounds

Two observations that reduce its authority as a *value* source, without touching
its authority as the only *shape* source:

- **Its stated formula is index-ambiguous.** "1★ 20 / 2★ 40 / 3★ 80 / 4★ 160"
  labelled by star, with formula "(2^n)×10", is only self-consistent if `n`
  starts at 1 for 1★. `10·2^(n−1)` fits the same four numbers with `n` starting at
  0. The wiki's own indexing convention is therefore not pinned by its own text.
- **Doubling is not this corpus's house style.** On the same page, the
  self-overcoming ladder (§1.7) is 5/15/45, 7/25, 9/30/80, 12/40/110 with
  fragment = 10× crystal — no geometric progression. A geometric `2^n` in one
  table and additive/mixed ladders in its neighbours is exactly the pattern one
  expects from an imprecise community summary.

## 2.5 The NAMU §2 "1★ = 10 / 3★ = 30" reading must **not** be used as proof

It would be convenient — it matches the local 1★ value exactly — but the
transcription is ambiguous in at least three ways, and the lane author himself
flags garbling in adjacent tables (`polluted-observations.md:701-702`):

1. **Safest raw form:** "helium **2/8/15 per grade** with **5/4/2 searches**, 4 waves,
   2 traces/box (**min 2, max 8**)". If 2/8/15 are *per-search yields* and 5/4/2 the
   searches, the grade totals are **10 / 32 / 30**. The middle value 32 is not on
   any ladder, which is itself a sign the triple is mistranscribed.
2. If "×N searches (N total)" is *capsule* arithmetic rather than trace counts —
   which is entirely plausible, since the sentence sits under the heading
   "Helium capsules" — then **no trace threshold is stated at all** in §2, and
   10/32/30 are capsule costs.
3. If the grade-3 figure 15 is a *total* rather than per-search, it exceeds the
   sentence's own stated per-search maximum of 8, so that reading is self-contradictory.

**Conclusion:** NAMU §2 cannot be cited as "the same wiki says 1★ = 10". It is
cited here only as *evidence of internal inconsistency* (§1.7, §2.4). Any future
lane that wants the raw line should re-fetch the mirror and transcribe the Korean
sentence verbatim rather than rely on the derived parenthetical.

## 2.6 Verdict

| Question | Verdict | Basis |
|---|---|---|
| Is `collect_qty` per-hunter or per-star? | **Neither/or — it is per-hunter, graded by star.** The dichotomy is false | §1.1, §1.2, §1.3, §1.4, §2.1 |
| Is the local ladder on the same axis as NAMU's? | **Yes** — indexed on catalogue `R★` (`006`=1, `005`=2) | §1.9, §2.1 |
| Is the local ladder's **shape** (doubling per star) corroborated? | **Yes, uniquely** — no other source states any ladder **[2026-10-05 re-counted per the `exp-ladder-corroboration-2026-10-05.md` retraction discipline, applied in `trace-rarity-vote-2026-10-05.md` §1.5: the `share-en` player-guide "fixed-recruit trace ladder" 20/40/80/160 is the **SAME `[NAMU] §1.3` numerals**, not an independent second ladder; `15672`/`69900` state no numeral; and `vsfan` 20/100/300 is a different quantity for a different reason. So "uniquely" still holds and the source count must stay at **ONE**, never "multi-source" / "independently corroborated".]** | §1.7 |
| Are the local **absolute values** corroborated? | **Rank 1 (10): partially.** No first-party source; 10 is the game's own ★3 grant quantum (§2.2) and the base of the local formula. **Rank 2 (20): no support and no contradiction** — NAMU is the only source and it says 40, while its sibling page says something else again | §1.7, §2.2, §2.5 |
| **Is the factor-2 claim upheld as an error?** | **NO.** It is an exponent-convention offset against a single ERA-UNRESOLVED source that contradicts itself at ★1 and ★3, and the only external anchors (two official 10-trace ★3 grants; two official 40-trace ★3 maxima/grants) fit the **local** ladder. **[2026-10-05, `trace-rarity-vote-2026-10-05.md` §2.2–§2.3 — two clauses added, verdict unchanged: (a) the only English-language wiki ladder in the corpus (`vsfan` 20/100/300) measures a **different quantity** (per-trace rarity VALUE), so it neither supports nor refutes; (b) under the counterfactual that it were the same quantity, it would contradict **[NAMU]** by a non-constant 1.00×/2.50×/3.75× rather than the fixture, so the constant-factor-2 signature remains specific to the NAMU-vs-local pair.]** | §2.1, §2.2, §2.4, §2.5 |
| Recommended audit change | **Soften row E8** from `CONTRADICTED` to *"shape CORROBORATED; absolute value UNRECOVERED; recorded as a one-index offset vs NAMU §1.3"* and re-file **X3** from `OPEN (contradiction)` to `OPEN (index ambiguity)`. Keep 10/20 as published fixtures — **no retune is recommended by this lane** | §2.1–§2.6 |
| Confidence | moderate on the axis and the shape; **low on every numeral**; the 40-vs-80 ★3 argument is plausible inference only | §2.2, §2.3 |

**Honesty boundary.** Nothing here recovers an original `collect_qty`. This lane's
contribution is negative and structural: it removes a false dichotomy, shows the
supposed contradiction is an index ambiguity inside a self-contradicting source,
and supplies the first *official* trace quantities that bear on the grade in
question. It does **not** license changing 10 or 20, and it does **not** license
asserting 10 or 20 as original.

## 2.7 Blast radius if the owner ever retunes (documentation only — no change made)

- Because consumers 2 and 3 **derive** from consumer 1 (`GUIDE_TRACE_QTY`), a
  doubling stays internally self-consistent for a **new** guided run: the guided
  award and the tutorial gate scale together, and "one guided victory = one
  recruit" survives.
- It would **not** retro-fit existing state, and by policy it must not: legacy
  guided receipts are retained exactly with no backfill (AGENTS §85), and the live
  account holds trace `qty = 2` against a threshold of 10. A retune creates a mixed
  population where pre-retune guided runs are worth half a post-retune recruit.
- Trace prices elsewhere in the corpus are **independent** of `collect_qty` and
  were computed against the local 10 only for plausibility: Fight Chip shop
  375 per 5 (Beckhen ★4), chu-coin 12 → 5 (Lily&Lala ★4), honor medals 700/8 (★4)
  and 350/8 (★3), Evaluation ticket ≤5 traces. At 8 traces per purchase, the
  official-looking honor-medal rate implies a **★3 threshold of ~8–16** and a **★4
  threshold of ~32–64** if the intent was "about one recruit per purchase" — which
  is *below* the local 40, not above it. Read as 8 traces being a bulk bundle
  rather than a recruit, it is neutral. **Recorded as a tension, not a finding.**

## 2.8 Complete trace-quantity token ledger (sources + era)

Era key: **PRE** = before 2019-09-05 · **POST** = after · **UNRES** = era
unresolved · **SHIPPED** = first-party text inside the 2.8.0.1 client.

### Required trace counts (the audited quantity)

| Token | Source | Class | Era |
|---|---|---|---|
| **1★ 20 / 2★ 40 / 3★ 80 / 4★ 160**, "(2^n)×10" | NAMU hunter page §1.3, `d.namu.moe/w/블루스톤/헌터` | COMM (1 source) | UNRES |
| **160** for 4★ Harley, worked example (300 mirage fragments → 3 traces/day; lane's own "≈32 days" figure does not reconcile with 3/day — **internally inconsistent arithmetic**) | NAMU §1.4 | COMM | UNRES |
| "1★ 2/search × 5 searches (10 total)" / "3★ 15/search × 2 searches (30 total)" | NAMU main page §2 — **ambiguous, see §2.5; may be capsules** | COMM | UNRES |
| **10** (rank 1, `006` Sylvester) | `server-ts/src/hunter-traces.ts:10` | FIXTURE | none |
| **20** (rank 2, `005` Gerard) | `hunter-traces.ts:9` | FIXTURE | none |
| no numeral at all | shipped 2.8.0.1 `UI_CSV` `CONTENTS12_*`/Hunter-Search help, 5 locales | ORIGDATA (negative) | SHIPPED |
| no numeral at all | preserved local data / extracted assets (0 matches for `collect_qty`) | ORIGDATA (negative) | — |

### Official first-party trace quantities (all ★3 unless noted)

| Token | What it is | Source | Era |
|---|---|---|---|
| **10** per 10+1, ★3 Santa Clauster + ★3 Santa Girl Rebecca | bundle gift | `document_srl` 995273, 2018-09-28, capture 2018-10-21 | PRE |
| **10** per 10+1, ★3 Jack-O'-Lantern (Oct 19–26) | bundle gift | `document_srl` 1008972, 2018-10-19, capture 2018-10-25 | PRE |
| **10** per 10+1, ★3 Broom Witch Denali (Oct 26–Nov 2) | bundle gift | same | PRE |
| **40** + 1 Special Request, ★3 Jack-O'-Lantern | weekly **first-purchase** bonus | same | PRE |
| **40** + 1 Special Request, ★3 Broom Witch Denali | weekly first-purchase bonus | same | PRE |
| **15** rice cakes → 1 box; **3~5** traces typical; **40** jackpot | ★3 traces **exchange price** | `document_srl` 989396, 2018-09-20, capture 2018-10-25 | PRE |
| **3~40** per box (Fire / Ice / Lightning ★3 traces + 1 element material) | box content range | same | PRE |
| **95** walnuts (Apollon, Dino, Calibur, Therapy) · **125** (Crocus) | trace box price; ★3 by **community** catalogue only | `document_srl` 1003633, 2018-10-12, capture 2018-10-25 | PRE |
| **2~4** per box typical · **40** lucky jackpot | box content range | same | PRE |
| walnut income **1** / 5 general stages · **3** / Hunter Search · **5** / Abyss · **6** / scroll recruit · **45** / Manda recruit | price denominator | same | PRE |
| **4** consecutive battles; max **4** reward boxes per Search | Search structure | shipped `CONTENTS12_2` | SHIPPED |
| **+1** trace per **2** friends, max **10** friends, **1**-hour window | trace reward scaling | shipped `CONTENTS12_4` | SHIPPED |
| grades **2★/3★** trace tiers; **4** waves; no time limit; **20** fuel per ruins | trace availability + structure | official EN guide `share_en/197745` | PRE |

### Community trace prices and rates (no threshold implied)

| Token | Source | Class | Era |
|---|---|---|---|
| **375** fight chips per **5** traces (Beckhen `051`, ★4), 6 h restock | NAMU §1.2 | COMM | UNRES |
| **12** chu-coins → **5** traces (Lily&Lala ★4) | NAMU §1.3 | COMM | UNRES |
| **700** honor medals per **8** traces (★4) · **350** per **8** (★3) | NAMU main page | COMM | UNRES |
| **3** traces/day from **300** mirage fragments; **5** traces per **10** mirage floors (quest) | NAMU §1.4 | COMM | UNRES |
| 초급/Evaluation ticket: **≤5** traces, usable 1–10 at once (1–3★) | NAMU §1.4 | COMM | UNRES |
| max **4** boxes/Search, **2** traces/box, min **2** max **8** per run | NAMU §2 | COMM | UNRES |
| stage drops carry traces (st. 40 fodder + old-man traces; 66–69 mid; 126–129 / 166–169 high) | Bahamut player text, unverified | COMM | UNRES |
| **1-** and **3-trace** exchange options, Lottery Mouse "Collect Hunter Traces" event, 2017-08-20 screenshot | VSFan 2017-08-20, UI only, no price | COMM/original-pixel | PRE |
| "**Teddy Bomber's Trace x30**" — Teddy Bomber `025` is `R★`=2 (community) | VSFan 2017-08-20 collectible description; **AMBIGUOUS**: `x30` may be a requirement, an owned quantity or an exchange price | COMM | PRE |
| since 2019-04-01 ruins pay **traces + Metron fragments only**; 4★ traces sold in Mirage/Blitz shops; FC shop stocks 4★ traces | Blustone Guide FAQ L235/L265 | COMM | POST |
| **1** trace per ordinary Search win; **10** per guided win | `search-battle.ts:214`; AGENTS §74/§85 | FIXTURE | none |
| live account: trace `qty = 2` against published threshold 10 | replica state | SELF | — |

### Rejected as trace-threshold evidence

- **MON BLAST!** figures (`com.vshower.prd_pf`) — different app, no crosswalk
  (`cross-title-mon-blast.md`).
- **2017 packet captures** — TLS-encrypted bodies; endpoint list only, no numeric
  payout (`vsfan-research-material.md`; `rewards-economy-2026-10-05.md:237-240`).
- **`Teddy Bomber's Trace x30`** as a *threshold* — see the AMBIGUOUS marker above.
- **Namu §2's "(10 total)"/"(30 total)"** as a threshold — see §2.5.

## 2.9 What would actually close this (cheapest first)

1. **A real `/reference/GetItem` row for a genuine trace item id** — `use_type 3`,
   `effect` = a hunter `base.id`, and its `collect_qty`. That single field closes
   E8 outright. The bounded local searches for it are already negative (§1.8), so
   this needs an authoritative archived `GetItem` response, a decrypted permitted
   capture, or an original-cache export — not more local grepping.
2. **One native panel capture** of the ShardExchange popup for any trace item
   (`ShardExchangeConfirm::Init` `Gce0e90` stores the threshold at popup+`E4`),
   ideally for a ★2 and a ★3 hunter, which would give two points on the ladder and
   settle the index question directly.
3. **Re-fetch the NAMU hunter page and transcribe the §1.3 ladder row verbatim in
   Korean**, plus the §2 helium sentence in full, to remove both the index
   ambiguity (§2.4) and the capsule/trace ambiguity (§2.5). Cheap, and it is the
   only source of any ladder at all.
4. **Mine `event_board` bodies further for a ★2 trace grant.** Every official trace
   numeral found so far is ★3; a single official ★2 grant would give the second
   ladder point directly. The board is a 23-page forum index with permalink
   captures already enumerated (`official-posts-2026-10-05.md` §1.3), and its
   declared purpose is player screenshot upload — its comment images are an
   unmined corpus that likely contains real exchange panels.

## 2.10 Limits of this lane

- **Nothing was changed.** No fixture, server source, seed, state file, APK,
  emulator, physical phone, original asset or Ghidra project was touched. This is a
  read-only evidence adjudication.
- **`polluted-observations.md` was deliberately not appended**; the parent mirrors
  this file.
- **No coverage change.** Heroes 1/113, accessories 1/100, monsters 0/22.
- **The §2.2 ★3 argument is inference** from event-design plausibility and the
  recurrence of the number 40 in two independent official events. It is not a
  recovered value and must always be quoted with that label.
- **§2.5 removes a tempting false corroboration.** Do not let "NAMU §2 says 1★ =
  10" back into circulation as settled; the sentence's own numbers may be capsule
  arithmetic.
- **The local `rank` values used for the axis check are community-sourced**
  (`INDEX.md:503`), as are the ★3 labels of the five walnut-event box hunters. The
  official ★3 labels used in §2.2 (Jack-O'-Lantern, Broom Witch Denali, Santa
  Clauster, Santa Girl Rebecca) *are* body-stated and need no catalogue inference.
- The 3★ and 4★ rows in the local ladder's shape table (§2.1) are **extrapolations
  for reasoning only** — the replica publishes rank 1 and rank 2 and nothing else.
