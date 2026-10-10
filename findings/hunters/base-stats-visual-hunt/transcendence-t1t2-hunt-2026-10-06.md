# T1 / T2 hunt — a measured first transcendence rung (2026-10-06)

**Lane.** Find any single **T1** or **T2** reading of HP / ATK / DEF for an
identified hero, to break the degeneracy
[`transcendence-multiplier-2026-10-05.md`](transcendence-multiplier-2026-10-05.md)
§2.2 limit 1 recorded: *"`1.10` and `1.20` are **untested**, not confirmed. A
ladder with `1.10 / 1.20 / 1.30` and a ladder with `1.05 / 1.18 / 1.30` predict
identical T3 values and are **indistinguishable on the available evidence**."*

## Headline

**A T1 rung exists, is first-party, and is measured.**

> One capacity-transcendence step on **Bear `036`** (大自然の贈り物「クマ」,
> Lv.1, same grade both sides, same frame) takes
> **HP 619 → 681**, **攻撃力 365 → 401**, **防御力 423 → 465** —
> **×1.10016 / ×1.09863 / ×1.09929**, mean **×1.099361**, internal spread
> **0.139 %**.
>
> **The flat ladder `1.10 / 1.20 / 1.30` is confirmed on its first rung.
> `1.05 / 1.18 / 1.30` is excluded by 4.70 %.**

The step is labelled **T1 on an axis completely independent of the stat block**:
the frame's own cost panel reads **crystals 9/9, fragments 449/90, gold 9000**,
which is exactly the ★3 **T1** row of the vsfan
`Guide_to_Blustone` cost table — not T2 (30/300/30 000) and not T3
(80/800/80 000). So "T1" is *positively identified*, not inferred from "one step".

**Still zero T2 and zero T3 observations anywhere.** The step ladder is now
one-of-three confirmed, not three-of-three.

**Nothing was changed.** No `server-ts`, fixture, seed, APK, state file, emulator
or physical phone was touched. `polluted-observations.md` was **not** appended.
`coverage.md`, every TSV and the Ghidra project were **not** touched.
**Coverage does not move: heroes 1/113, accessories 1/100, monsters 0/22** —
per the project convention recorded in the brief, a stat block that sits
post-Transcendence is not a base stat, and this block is a *delta*, not a level
of a stat at all.

---

# 1. PURE

## 1.1 The artifact — full provenance

| field | value |
|---|---|
| Host | `blustone.jp` — 「ブルーストーン公式攻略サイト」, the **official** Japanese strategy site |
| Host page | `/育成論/キャパ超越/capa2` (page capture `20191216051555`, 26 826 B, HTTP 200) |
| Parent page | `/育成論/キャパ超越` (page capture `20190331201909`, 30 888 B, HTTP 200, in-page date `2018-11-16`) |
| Image URL | `https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg` |
| CDX row | `20190403161635  image/jpeg  200  68305` (compressed **WARC record** length) |
| Retrieved (`id_`) | **HTTP 200, 69 340 bytes** (decompressed payload), decoded **JPEG 1024 × 911** |
| sha256 | `709ed6d5eee606bc8501888df9d430e41a371f4d1a5c5abc20df3a7019eec0e9` |
| Companion frame | `capa1-1024x911.jpg` — capture `20190403142252`, 116 281 B, 1024 × 911, sha256 `aa90c79b4…` — the **pre-transcendence** state |

URLs were taken **verbatim from the CDX `original` field**, percent-encoded as the
archive stored them; no codepoint was hand-written (GUARD item 13). Local copies
are under `analysis/tmp-t1t2/img/`.

**The image is the only one of its kind in the corpus.** Of the 343 unique image
URLs archived under `blustone.jp/wp-content/uploads/`, `capa2-1024x911.jpg` is
the **only** file carrying a per-stat `攻撃力 / 防御力 / HP` before→after block.
`capa1` is the before-state panel; `capa.jpg` (both the 2018-11 and 2019-03
captures) and `capacity.png` are chibi-art procedure diagrams; `rank1`–`rank4`
are ★1→★2 … ★4→★5 **cost/selection** screens with no stat block (verified by
opening `rank3`); `0d40a5e4…-1-1024x904` is a Rank-Up **review** screen showing
`戦闘力 2554 → 3827` but **no** per-stat block (verified by opening it).

## 1.2 Verbatim reading of the frame

Two panes. **Left** = ハンターキャパ超越, the pre-transcend selection screen.
**Right** = キャバ超越, the success receipt (「キャバ超越に成功しました！」).

Target, **left and right panes, same hero, same level, same grade**:

- Name/epithet **大自然の贈り物「クマ」**, badge **Lv. 1**
- Rank title **ミドルハンター**
- **戦闘力 2326 → 2704**

Result block, zoom-verified at 3× on a 1024 × 911 source:

| label | before | after | ratio |
|---|---:|---:|---:|
| 戦闘力 (rating) | 2326 | 2704 | ×1.162511 |
| **攻撃力** (Attack) | **365** | **401** | **×1.098630** |
| **防御力** (Defense) | **423** | **465** | **×1.099291** |
| **HP** | **619** | **681** | **×1.100162** |

Material consumed: a second **Bear `036`**, Lv.1, 戦闘力 2326, selected `1/1`.
On-screen rule, read verbatim from the frame:

> 対象ハンターと同一の★3以上のハンターの素材として使用可能です。
> キャバ超越に使用したハンターはリストからいなくなります。

Cost panel, read verbatim:

| | value |
|---|---|
| キャバ超越必要アイテム, blue crystal | **9/9** |
| キャバ超越必要アイテム, blue shard | **449/90** |
| キャバ超越 button, gold | **9000** |

**Identity: exact, not inferred.** `大自然の贈り物「クマ」` is the verbatim
`profile_title` of catalogue `036` in
[`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv), and
`hero-panel-level-extraction-2026-10-06.md` §4.3 had already confirmed it from
the same frame by name-on-screen plus 守備手/電撃 icon agreement.

## 1.3 The mechanic name is first-party, not a translator's guess

The brief asked for a "Transcendence / Ascension / Awakening" reading; the frame
says 「キャバ超越」. These are **one localised string in the shipped client**, not
a translation:

```
헌터 자기극복,헌터 자기극복,Hunter Transcendence,ハンターキャパ超越,猎人自我超越,獵人自我超越
```

— `analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/e44ab8ed.txt`
**line 408**. One CSV row, six locales, EN `Hunter Transcendence` ≡ JA
`ハンターキャパ超越`.

Corroboration from the shipped EN help string (`…/UI_CSV/7adedb12.txt` line 7133,
key `ENH_TRC_INFO3`):

> `To transcend the hunter above| only identical hunters who are 3★ or above can be used as fodder.\nThe used hunter will disappear.`

which matches the frame's rule text clause-for-clause (same-hero ★3+ material;
the material leaves the list). **So the same mechanic is called Transcendence in
English and キャバ超越 in Japanese, in the client's own strings.**

## 1.4 The step is T1 — proven by cost, not assumed

vsfan `Guide_to_Blustone` (`oldid` **7465**, re-fetched 2019-11-14, 56 355 B,
sha256 `34b96c361497d90bbc3ac93c0da59d2370fc9b308e4b7ee8030f86b72c3afd27`),
Transcendence section, verbatim:

| | T1 | T2 | T3 |
|---|---|---|---|
| Natural 1-star | 5 crystals / 5 000 / 50 / 1 dup | 15 / 15 000 / 150 / 2 | 45 / 45 000 / 450 / 3 |
| Natural 2-stars | 7 / 7 000 / 70 / 1 | 25 / 25 000 / 250 / 2 | 60 / 60 000 / 600 / 3 |
| **Natural 3-stars** | **9 / 9 000 / 90 / 1** | 30 / 30 000 / 300 / 2 | 80 / 80 000 / 800 / 3 |

The frame's cost panel reads **9 crystals, 9 000 gold, 90 fragments, 1
duplicate** — the **★3 T1** row exactly. ★3 is the floor for the first
transcendence (the frame's own rule text says ★3以上; `ENH_TRC_INFO3` says
"3★ or above"; `[COST]`'s T1 floor is ★3).

**Therefore the measured step is T1, and the label rests on a quantity
(cost) that is independent of the quantity being measured (stats).** This is the
one thing the frame could have got wrong in a self-consistent way and cannot:
if the stat block were a T2 or T3 delta, the cost panel would read 30/300/30 000
or 80/800/80 000.

**This is also an independent triple corroboration of the vsfan cost table** —
a row that was previously `OPEN-2` for the ★3 T1 column.

## 1.5 The multiplier, and how tightly it is pinned

| selection | ratio | spread |
|---|---:|---:|
| 攻撃力 | ×1.098630 | |
| 防御力 | ×1.099291 | |
| HP | ×1.100162 | |
| **mean** | **×1.099361** | **0.001531 = 0.139 % of mean** |

Integer-exactness test. A single `M` satisfies all three readings when the
per-field intervals intersect:

| rounding | intersection | width | is `M = 1.100000` inside? |
|---|---|---:|---|
| `floor` | `[1.100162, 1.101370)` | 1.208 × 10⁻³ | no, by 1.62 × 10⁻⁴ |
| `round` | `[1.099354, 1.100000)` | 6.46 × 10⁻⁴ | no, by 6.46 × 10⁻⁴ |

**Both intersections are NON-EMPTY, and both bracket 1.10 to within 0.11 %.**
Exactly `1.100000` falls in neither because of two independent one-unit effects
at n = 1: `365 × 1.10 = 401.50` is an exact tie, and `619 × 1.10 = 680.90`
truncates to 680, not the displayed 681.

> **Stated honestly: T1 = 1.0994 ± 0.0012, i.e. ×1.10 to within 0.11 %.** The
> exact rounding/tie-break rule is **not** recoverable from a single sample, and
> no single rule makes exactly 1.100000 consistent. Do not quote this as
> "integer-exact at 1.30 the way Hermes is".

Context for the 0.139 % internal spread: it is the **second-tightest** in the
project after Hermes `023` (0.11 %), ahead of Riko `024` (0.20 %), and two
orders of magnitude tighter than Captain `009` (8.87 %).

## 1.6 The degeneracy is broken

| candidate ladder | T1 rung | error vs measured T1 | T3 | worst T3 err (9 fields) |
|---|---:|---:|---:|---:|
| **flat 1.10 / 1.20 / 1.30** | 1.10 | **−0.058 %** | 1.30 | 10.09 % |
| flat 1.05 / 1.18 / 1.30 | 1.05 | **+4.701 %** | 1.30 | 10.09 % |
| compounded ×1.10³ | 1.10 | −0.058 % | 1.331 | 12.19 % |
| cumulative 1.10 · 1.20 · 1.30 | 1.10 | −0.058 % | 1.716 | 31.89 % |

The two ladders that were **provably indistinguishable on T3 alone are now
separated by a measured 4.70 % at T1.** This is exactly the discriminator
`transcendence-multiplier-2026-10-05.md` §2.5 item 2 asked for ("A T1- or
T2-captioned page, which would break the `1.10/1.20/1.30` degeneracy
directly"). The caption is not needed — the game's own receipt supplies the same
discrimination, and better, because it is first-party.

**Standing prohibitions unchanged and re-affirmed.** `1.10 × 1.20 × 1.30 =
1.716` stays **refuted** (31.89 % worst error). Do not implement `×1.30`, do not
implement `×1.274`. Captain's ATK is **not** smoothed (§2.3).

## 1.7 Era matching — the largest existing confound is reduced

`stat-version-context-2026-10-06.md` dates the balance patch to **2019-09-05**.
`transcendence-multiplier-2026-10-05.md` §2 flags that `[WIKI-T3]` (the T3
numerators) is **PRE** while `[JP19]` (the denominators) is **POST**, as "the
single largest limitation on every number above".

- `capa2` image upload directory **`2018/11`**; parent page in-page date
  **`2018-11-16`** → **PRE** the patch.
- vsfan T3 table captures **2019-08-21 / 2019-08-26** → **PRE** the patch.

So **the T1 rung and the T3 rung are now measured on the same side of the
rebalance.** Stronger than that: the T1 ratio is **internal to a single frame** —
same hero, same level, same grade, same session, before and after one button —
so it carries **no era dependence whatsoever**. The confound survives only for
the T3 numbers, which still divide a PRE numerator by a POST denominator.

## 1.8 Falsifiable prediction for Bear `036` — recorded for a future test

Pre-transcendence values in the frame are HP 619 / ATK 365 / DEF 423. Under the
now-measured flat ladder:

| state | HP | 攻撃力 | 防御力 |
|---|---:|---:|---:|
| pre-T1 (in frame) | 619 | 365 | 423 |
| **T1** (×1.10) | 680.9 → **681 measured** | 401.5 → **401 measured** | 465.3 → **465 measured** |
| T2 (×1.20) | 742.8 | 438.0 | 507.6 |
| T3 (×1.30) | 804.7 | 474.5 | 549.9 |

**A T2 or T3 receipt for Bear `036` at Lv.1 would test 1.20 and 1.30 directly.**
None was found (§3).

---

# 2. UNPURIFIED

Everything in §2 is inference. Named unknowns, all of them:

| # | unknown | status |
|---|---|---|
| U1 | **Gear / equipment state** | **UNKNOWN.** The frame shows no equipment slots. Whether the ★3→★4 panel convention of §16-era gear-removal applies here is **unverified**. Does not affect the ratio (both sides identical state) but does mean the absolute values are not base values. |
| U2 | **Sub-stat state** | **UNKNOWN.** The receipt shows only 攻撃力/防御力/HP. Crit / crit-dmg / pen / block / block-resist / elem enhance / resist / hp-regen are **not displayed** and their T1 response is **unmeasured**. |
| U3 | **Jewels / set bonuses** | **UNKNOWN**, as U1. |
| U4 | **Buffs / temporary states** | Not a buff context (no buff icon row in the receipt); treated as absent but **not positively verified**. |
| U5 | **Star grade of the frame** | The badge is ~20 px on a 1024-wide source and **stars are not independently resolvable** at this resolution. Carried as **★3** from `hero-panel-level-extraction-2026-10-06.md` §4.3; **not re-read here and not contradicted here**. Immaterial: the before/after comparison is at identical state inside one frame, and the ★3 T1 cost row matches. |
| U6 | **Level** | **Lv. 1**, stated on the badge in both panes. High confidence. |
| U7 | **Absolute relation to `[JP19]`** | **UNRESOLVED and newly visible.** The frame's pre-transcendence Bear is 365/423/619; `[JP19]` Bear is 755/864/1923. Ratios 0.48344 / 0.48958 / **0.32189** — not a single level factor. `atk/hp` shape is 0.5897 in the frame vs **0.3926** in `[JP19]`. So `[JP19]`'s row is **not** a level-scaled copy of this hero at any level, which is an independent reason to keep the `[JP19]` denominator suspect. Recorded, not resolved. |
| U8 | **Whether the bonus is "+10 % of base" or "×1.10 on current"** | **STILL OPEN.** One rung cannot separate them; they diverge at T2 (1.20 flat vs 1.21 compounded). The T3 observations favour flat (1.30000 exact for Hermes vs 2.4 % off for compounded), but T3 is era-confounded. |
| U9 | **n = 1** | One hero, one frame, one step. No replication. |
| U10 | **2018-11 build vs the 2.8.0.1 shipped client** | The image is from an **unofficial-provenance screenshot placed on the official guide site**, uploaded `2018/11`, i.e. game version ≤ ~1.4.x. **Whether the 1.10 factor is unchanged in 2.8.0.1 is unverified.** |

## 2.1 What this licenses and what it does not

**Licensed:**

- **T1 = 1.10 (±0.11 %) on HP, ATK and DEF, first-party, era-independent.**
  This is now a *measured rung*, not a fitted one.
- The **flat** reading of the ladder is preferred over the compounded reading on
  the first rung (they are indistinguishable at T1), and the T3 corpus already
  prefers flat.
- The `1.05 / 1.18 / 1.30` alternative is **excluded**.
- The ★3 **T1** cost row of the vsfan table is **corroborated by the game's own
  receipt** — `OPEN-2`-class item closed on the cost side.

**NOT licensed:**

- **A single game-wide multiplier still does not follow.** `transcendence-multiplier`
  §2.1's two-cluster finding (Hermes 1.300 vs Riko/Captain 1.274, a 2.0 %
  unexplained gap) is untouched by a T1 rung on a *fourth* hero in a *different
  corpus* at a *different* level. **Do not implement `×1.10`, `×1.20` or `×1.30`.**
- **No base stat.** Per the project convention, and per U1/U3/U7, these are
  post-progression deltas at Lv.1 on a possibly-geared hero. **Heroes stay
  1/113.**
- **The per-step factors `1.20` and `1.30` remain UNTESTED.** One of three
  confirmed is not three of three. The fit still has two degrees of freedom.

## 2.2 Effect on the Bear `×1.162511` open item — cause now measured

The brief flagged: *"A 'capacity-transcendence' reading for Bear `036` at fixed
level+grade gives 戦闘力 2326 → 2704 = ×1.16251, which fits none of the clusters
in any step count. It may be a different mechanic."*

**It is a different mechanic, and the difference is now quantified.**

| quantity | factor |
|---|---:|
| 攻撃力 / 防御力 / HP (mean) | ×1.099361 |
| 戦闘力 rating | **×1.162511** |
| **excess** | **+5.744 %** |

Three stats that each scaled ×1.0994 produced a rating that scaled ×1.1625.
**Therefore 戦闘力 is a composite that is not a linear function of
HP/ATK/DEF** — it carries terms (level, rank, sub-stats, growth curve) that do
not share the ×1.0994 step response.

**This retires the item.** `hero-panel-level-extraction-2026-10-06.md` line 462
records `×1.162511` with confidence **high** as "Bear `036` capacity-transcendence
factor". That confidence is misplaced: it is a **rating** ratio, correctly read,
but it is **not a stat multiplier** and must never be entered in a stat column.
The same file's line 175 calls it "a same-state (level and grade both fixed)
change" — true, and still not a stat factor. **Proposed correction, not applied
(§4).**

## 2.3 Effect on the Captain `009` ATK anomaly — constrained, not explained

`atk/hp` **shape** ratio, `[JP19]` base → vsfan T3:

| hero | base | T3 | shape change |
|---|---:|---:|---:|
| `009` Captain | 0.3867 | 0.3548 | **−8.26 %** |
| `023` Hermes | 0.5354 | 0.5354 | −0.01 % |
| `024` Riko | 0.4200 | 0.4195 | −0.10 % |

The T1 step scales **ATK, DEF and HP identically to 0.139 %**. So a
field-specific ATK rule — the one hypothesis that would explain Captain — **is
not present at T1**, and if it exists at all it must appear only at T2/T3.

That is a genuine narrowing, and it is the opposite of a resolution: it moves the
anomaly from "possibly a field-specific rule anywhere" to "possibly a
field-specific rule that switches on after T1", which is a narrower but no more
likely place to look. **Captain's ATK stays the corpus's one large unexplained
field. Do not smooth it.** A single-digit `[JP19]` repair (628 → 576, the archive
minimum) still reconciles him and remains unproven.

## 2.4 What would close the rest

1. **Any second one-step receipt**, on any hero, any level. This is now the
   highest-value cheap target — the measurement is a two-number comparison and
   the corpus is known to be image-heavy (§1.1).
2. **A T2 or T3 receipt.** Would test 1.20 / 1.30 directly and settle U8.
   §3 records where these were searched for and not found.
3. **The stat block with a sub-stat row visible**, to answer U2 — if sub-stats
   also respond to T1, the "three stats only" reading of the vsfan tables
   (97/108 agreement on nine sub-stats) is a *display* artefact rather than a
   rule, and that is a materially different model.
4. **A `[JP19]` row that reconciles with U7.** The archive's `atk/hp` shape for
   `036` (0.3926) is 50 % off the in-game Lv.1 hero (0.5897). Whatever the
   archive's rows represent, it is not a level-scaled hunter stat line.

---

# 3. Controlled negatives

A controlled negative is a result. Each item below ran a **positive control
first** and is stated as a bounded negative, never as an absence.

## 3.1 vsfan wiki revision history — **no T1/T2 table exists in any revision**

This is the §2.5-item-1 probe ("`action=history` on e.g. `Bear` or `Lapis` is the
cheap probe"), done exhaustively instead of cheaply.

- CDX `url=vsfan.net/wiki/` + `matchType=prefix`, **no `collapse`** →
  **8 887 rows / 1 201 distinct plain content paths**. (The prior harvest used
  `collapse=urlkey`, which silently kept one capture per URL and hid the rest.)
- **BROKEN INSTRUMENT avoided:** `matchType=prefix` with a literal `*` in `url=`
  returned **0 bytes**, twice, and read as "no pages". The `*` form is only valid
  for `matchType=domain`. Control that caught it: the same query without `*`
  returned 9 rows immediately.
- Each of the 8 partial-table heroes has **2–3 real captures** once the
  2021-07-29 parking pages (2 2xx B) are excluded.
- **Fetched the later revisions of all 8** (Bear ×2, Diana, Joy ×2, Kain ×2,
  Lantern ×2, Pansy, Patrone, Scar ×2) — all HTTP 200, all 1024-scale HTML with
  real wiki text.
- **Result: every `Character Attributes` table is identical in every revision.**
  No `Life` cell, no `Attack`/`Defense` cell, **zero `<caption>` elements on the
  page**, same Attack Speed, same nine sub-stats. `table len = 1063` (Bear /
  Lantern / Patrone) and `1069` (Diana / Joy / Kain / Pansy / Scar) are stable
  across all revisions.

**Positive control for this negative** — the same fetch path re-fetched three
**ledger** captures and reproduced them **byte-exact and sha256-exact**:

| page | capture | bytes | expected | sha256 |
|---|---|---:|---:|---|
| Patrone | `20190826075547` | 122 245 | 122 245 | **MATCH** |
| Bear | `20190826070034` | 80 961 | 80 961 | **MATCH** |
| Hermes | `20190826081115` | 113 204 | 113 204 | **MATCH** |

So the instrument is proven good on this exact namespace before the zero is
believed.

**Verdict: the vsfan wiki holds exactly three `Life/Attack/Defense` tables in
its entire archived history, all captioned `Transcendence Level: 3`. The "absent
from the wikitext" reading in `vsfan-wiki-2026-10-05.md` §1.6 is confirmed
against every revision, not just the one the ledger happened to fetch.**

## 3.2 vsfan `Guide_to_Blustone` — a dedicated Transcendence section exists, and it is **costs only**

The brief's avenue 1 asked whether the wiki has a dedicated
Transcendence/Ascension/Awakening article with its own tables. **Yes, and the
answer is no for stats.**

`Guide_to_Blustone` (`oldid` 7465) has a § **2.3 Transcendence** with a full
3 × 3 cost matrix (natural 1★/2★/3★ × T1/T2/T3), plus the star-floor rule
("for the second and third transcendence, your base hunter needs to be at least
4-stars and 5-stars respectively"). **There is no stat multiplier anywhere in it**
— no HP/ATK/DEF figure, no percentage, for any level. I read the whole section.

Two by-products:

- The **★3 T1 row** (9 / 9 000 / 90 / 1) is what pinned my frame to T1 (§1.4),
  and is now independently corroborated by the game's own cost panel.
- **Correction to the project's own record:** this section was already inside
  the retrieved corpus — `vsfan-wiki-2026-10-05.md` §1.4 lists `Guide_to_Blustone`
  `oldid 7465` with 56 316 B, and my re-fetch of the **same revision** returned
  56 355 B (same `oldid`, different capture timestamp/rewriting). So this is
  **not** new material; it is a transcription gap in the existing note, which
  summarised the page's economy data (§1.10) without transcribing §2.3.

`Hunter_Gym` (`oldid` 3172) contains **no** Transcendence content at all — it is
a location stub. Not a lead.

## 3.3 The official Japanese guide — searched, one receipt found, no T2/T3

The `育成論` (growth) section of `blustone.jp` was enumerated in full from the
domain CDX (1 235 rows; the site's WordPress structure `wp-json` / `archives` /
`hunter` / `育成論` was mapped, 63 `/hunter` profile paths confirmed as the
already-harvested set). Pages fetched at HTTP 200: `/育成論`,
`/育成論/キャパ超越`, `/育成論/キャパ超越/capa2`, `/育成論/ランクアップ` and
`/d` `/rank1`–`/rank4`, `/育成論/トレーニング` + `/traning1` `/traning2`,
`/育成論/結晶`, `/育成論/キャラ編成例`, `/hunter/タイプ別`,
`/hunter/レアリティ別`.

Every image in `wp-content/uploads/` (343 unique URLs) was enumerated. **All
stat-bearing candidates were opened and read:**

| image | content | stat block? |
|---|---|---|
| `capa1-1024x911.jpg` | Hunter List + Member Training, pre-state | rating only |
| **`capa2-1024x911.jpg`** | **capacity-transcendence receipt** | **YES — the finding** |
| `capa.jpg` (2018-11, 2019-03) | chibi `+ + =` procedure art | no |
| `capacity.png` | 300×200 chibi diagram | no |
| `rank1`–`rank4-1024x911.jpg` | ★N→★N+1 **cost/selection** screens (`opened rank3`) | no |
| `rankup.jpg`, `traning.jpg`, `IMG_9719.jpg` | summary/child-page art | no |
| `0d40a5e4…-1-1024x904.jpg` | Rank-Up **review**, 2554→3827 (`opened`) | rating only |
| `0d40a5e4…-2-1024x904.jpg` | Abyss / Mirage excavation UI (`opened`) | no |
| `equip1-1024x911.jpg`, `fishing1`, `biginner1`, `1242x2208_04` | other articles | no |

**Positive control for the image namespace** (GUARD: *count actual decoded
pixels*, not HTTP 200): 9 of 10 images decoded to real JPEGs of the expected
**1024 × 911**; the one failure (`rank4`, a 234-byte transport error) was
re-fetched and decoded to 63 961 B / 1024 × 911. **Decoded-pixel controls: pass.**

**Verdict: exactly one per-stat transcendence receipt exists in the official
Japanese guide. There is no T2 or T3 receipt there, and the other four growth
screens are cost panels, not stat panels.**

## 3.4 A claim in the existing record that this pass **corrects**

`capa2-diff-2026-10-05.md` §1.3 records: *"There is no POST-era transcendence text
to diff against the PRE capture 2019-03-31."* **There is.** A second page,
`/育成論/キャパ超越/capa2`, is archived at **2019-12-16** — after the 2019-09-05
rebalance. It was found by reading the CDX `original` field rather than the
prior note's URL list.

**It does not change the conclusion, and honesty requires saying so:** the
2019-12-16 page's entire content is **one image**, `capa2-300x267.jpg`, and the
**same** 1024 × 911 asset already archived in 2019-04. So the "POST-era capture"
is a later *capture of a 2018-11 upload*, not later content. The diff is empty
because the content never changed, **not** because no POST-era page exists. The
prior note's negative was right in substance and wrong in its stated reason.
**Proposed correction, not applied (§4).**

---

# 4. Proposed corrections — NOT applied

This file changes nothing outside itself.

| file | proposed | why |
|---|---|---|
| `hero-panel-level-extraction-2026-10-06.md` §4.3 line 175 / ledger line 462 | demote `×1.162511` from a "capacity-transcendence **factor**", confidence **high**, to a **rating** ratio; add that the three measured stats scaled ×1.0994 in the same frame | §2.2 — a rating is not a stat multiplier; the +5.74 % excess is measured, not speculated |
| `hero-panel-level-extraction-2026-10-06.md` line 449 | replace "キャパ超越 … no stat block" with "the キャパ超越 article's `capa2` image **does** carry a per-stat block; it was not read" | §1.1 — the stat block was there and unrecorded |
| `capa2-diff-2026-10-05.md` §1.3 | amend "no POST-era transcendence text exists" → a 2019-12-16 page capture exists but its content is the same 2018-11 image, so the diff is empty for a different reason | §3.4 |
| `transcendence-multiplier-2026-10-05.md` §2.2 limit 1 / §2.4 | T1 is now **measured** (§1.5); `1.20` and `1.30` remain untested | §1.6 — the degeneracy statement is superseded, the ladder is not |
| `vsfan-wiki-2026-10-05.md` §1.6 | the "rows absent from the wikitext" reading now rests on **all revisions**, not one capture | §3.1 |
| `transcendence-skill-cost-2026-10-05.md` cost matrix | ★3 **T1** row corroborated by the game's own receipt panel | §1.4 |

**Not appended:** `polluted-observations.md` (parent mirrors).
**Not touched:** `coverage.md`, any TSV, `README.md`, `server-ts`, fixtures,
seeds, the APK, the emulator, the physical phone, Ghidra.

---

# 5. Files

- **New:** this file only, under
  `analysis/research/base-stats-visual-hunt/`.
- **Scratch, gitignored-by-convention working set:** `analysis/tmp-t1t2/`
  (`cdx-wiki-all.txt` 8 887 rows, `cdx-blustonejp.txt` 1 235 rows,
  `cdx-jp-uploads.txt` 344 rows, `jp/` 16 pages, `img/` 20 images, `crops/` 9
  zoom crops, `ctl/` 3 positive-control pages, the analysis scripts and their
  logs). Retained for auditability; **delete when the parent is satisfied.**
- **Read:** `GUARD-encoding-and-archive-traps.md`,
  `transcendence-multiplier-2026-10-05.md`, `vsfan-wiki-2026-10-05.md`,
  `hero-panel-level-extraction-2026-10-06.md`, `bahamut-remaining-2026-10-05.md`,
  `archived-hunter-database-2019.tsv`, `…/UI_CSV/e44ab8ed.txt`,
  `…/UI_CSV/7adedb12.txt`.
- **Fetched (read-only, Wayback `id_`):** 1 image family + 8 vsfan hero revisions
  + 16 `blustone.jp` pages + 3 positive controls.
