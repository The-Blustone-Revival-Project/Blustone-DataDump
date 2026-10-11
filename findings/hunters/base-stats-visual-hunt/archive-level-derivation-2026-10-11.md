# Archive-level derivation — the 2019 JP hunter DB shows the at-draw (Lv.1) state, gear-free (2026-10-11)

**Question.** `coverage.md` keeps hero base-stat coverage at **1/113** because the
62 numeric rows of the 2019 Japanese hunter database print no level and no gear
state. The 2026-10-06 note (`base-stat-heading-client-attested-2026-10-06.md` §5)
asked for an adjudication and got neither a proof nor a refutation. This note
closes the question with a derivation: **the archive rows are the heroes' at-draw
basic ability values — level 1, no equipment** — established from the page's own
labels plus three independent structural proofs.

**Coverage impact:** this changes the *classification* of the 62 rows from
"candidate, level/gear unknown" to "at-draw basic rows, gear proven, level
framed at-draw and bounded ≤ 17". Whether the ledger's "level documented" rule
accepts derivation-grade (rather than printed) documentation is the owner's
call — §6 states both outcomes. No counter was moved by this note.

## 1. The page's own labels (fetched 2026-10-11, verbatim)

`http://web.archive.org/web/20191216060610id_/https://blustone.jp/hunter/…/ファイトクラブの守護者「ベッケン」`
fetched and read in the browser (1,325 chars of body text). The stat block, verbatim:

```
ベッケンの基本情報
タイプ          攻撃手
属性            冷気
排出時の★       ★3
戦闘力          8709
ベッケンの基本能力値
HP              1678
攻撃力          864
防御力          660
攻撃スピード    8
ベッケンの詳細能力値：攻撃力
致命打率        33
致命打ダメージ量 200
貫通力          0
ベッケンの詳細能力値：防御力
ブロック率      14
ブロックダメージ減少量 42
属性強化        5
属性耐性        5
HP再生力        42
```

Three things follow directly from the labels, with no inference:

1. The stat section is **基本能力値 — "basic ability values"**. The site's own word
   for these numbers is *basic*, i.e. pre-training.
2. The rarity field is **排出時の★ — "★ at draw"**. The page frames the whole
   profile as the hero *at recruitment*. A hero at draw is at the level floor.
3. **There is no level field anywhere on the page** — confirming the prior lane's
   "level not printed", and simultaneously confirming the site never claimed a
   trained state.

The same page also lists **five skills** — `コケッ!コケコッコー!`, `攻撃スピードUP`,
`小柄で身軽な者`, `死の羽ばたき`, `ファイトクラブの守護者` — in the same order as the
five slots recovered from `SKILL_REF_RO`, and the same order the Korean wiki
(namu per-role page) lists them (`꼬꼬댁!! 꼬꼬!`, `공격 속도 증가`, `작고 가벼운 자`,
`죽음의 날개짓`, `파이트클럽의 수호자`). That is a third-language crosswalk for the
skill names and independently confirms the slot ordering. **Era caution:** the JP
text says Beckhen's evade fires `2秒間隔` (every 2 seconds) where the live Korean
wiki says `3초마다` (every 3) — the two sources are 7 years and one rebalance
apart; skill *text* is version-sensitive even though the stat schema is not.

## 2. Proof that the rows are gear-free

The FAQ's verified Lv.30 **nude** row for Beckhen (`datasets/hunters/observed-stats/051.md`)
and the archive row differ **only** in HP/ATK/DEF and the composite:

| field | archive | FAQ Lv.30 nude | |
|---|---|---|---|
| HP / ATK / DEF | 1678 / 864 / 660 | 2879 / 1471 / 1149 | ×1.716 / ×1.703 / ×1.741 |
| 戦闘力 | 8709 | 24068 | ×2.764 |
| speed | 8 | 8.00 | **identical** |
| crit / crit-dmg / pen | 33 / 200 / 0 | 33.00 / 200.00 / 0.00 | **identical** |
| block / block-red | 14 / 42 | 14.00 / 42.00 | **identical** |
| elem / elem-res / regen | 5 / 5 / 42 | 5.00 / 5.00 / 42.00 | **identical** |

All nine sub-stats are **exactly equal**. Beckhen's own gear delta is non-zero on
seven of those nine sub-stats (AS +1.72, crit +0.67, crit-dmg +10.86, block +4.69,
block-red +1.76, elem +1.65, elem-res +3.13). A geared archive row could not
reproduce the nude sub-stat line; therefore **the archive Beckhen row is
gear-free**. The database applies one schema to all 62 rows (§3 proves the schema
is uniform), so the argument generalizes: **all 62 rows are nude.**

## 3. Proof that the DB display carries no level/gear/rarity term

Least-squares fit of the DB composite against the three displayed core stats,
within role, over the 62 numeric rows:

| role | n | R² | max residual | fit `CP = c + w_h·HP + w_a·ATK + w_d·DEF` |
|---|---|---|---|---|
| Bomber | 12 | **0.9997** | 24 (0.3%) | −3907.7 + 2.5182·HP + 4.0519·ATK + 6.3365·DEF |
| Support | 13 | **0.9994** | 27.5 (0.4%) | −3921.3 + 2.2209·HP + 5.2626·ATK + 5.4994·DEF |
| Offense | 20 | 0.978 | 448 | −5512 + 3.856·HP + 4.473·ATK + 5.966·DEF |
| Defense | 17 | 0.956 | 620 | −5259 + 6.191·HP + 2.874·ATK + 2.040·DEF |

The Bomber and Support bands — which span ★1 through ★4 and include the three
identical costume-pair rows — are explained by **one linear formula to within
0.4%**. A level, gear, skill-level or rarity term in the DB display would break
that fit for some rows; none does. **The DB composite is a pure linear function of
the three basic abilities** (weights role-dependent), i.e. the archive's 戦闘力 is a
*basic rating*, not the trained on-screen value.

**Naming trap recorded:** the DB field and the on-screen field share the Japanese
label 戦闘力 (the FAQ translates it "Strength (Combined Power)"), but they are
different quantities. Beckhen: DB 8709 vs screen 24068 at Lv.30. Anyone joining the
archive to screen data on the label alone will silently mix schemas.

The trained display *does* carry the extra term: the Lv.30 stats fed through the
Offense fit predict 19,025 against the actual 24,068 — a **+5,043 residual**,
while every DB row sits within ±0.4% of its prediction. So the trained state adds
a term worth ~5,043 (level and/or skill-level and/or transcendence) that the DB
state lacks entirely. **The DB state is below any training.**

## 4. Bound on the level, and what the growth models say

Native formula (recovered, `findings/revival/…` §158 via
`STATS-ESTIMATE-2026-10-08.md`): `stat = uint32(base + up×level) × multiplier`.
For a fixed hero the multiplier cancels in ratios, so the analysis is
multiplier-independent.

- **Positive-base bound.** With `r = n(30)/n(L)`, a positive base requires
  `L < 30/r`. Beckhen: HP 17.49, ATK 17.62, DEF 17.23 → **L ≤ 17** for all three
  stats simultaneously. (At L=17 the implied DEF base is 20.5 — already nearly
  exhausted.)
- **Integer growth is impossible for every L.** `u = Δ/(30−L)` with
  Δ = 1201 (HP), 607 (ATK), 489 (DEF); 1201 and 607 are prime, and the only
  divisor of 489 in range gives L=27 with a negative base. No L yields positive
  integer growth, so growth increments are fractional (or the per-level map is
  multiplicative) — the replica's fixture `+10/+1/+1` is not the original curve.
- **Per-level rates if L=1:** core stats ≈ **1.89 %/level** (HP 1.879, ATK 1.852,
  DEF 1.930); the composite/Strength term ≈ 3.57 %/level. The core-stat rate is
  new; it does not collide with the 戦闘力 bound (`g²⁹ ≤ 1.498434`, itself a soft
  heuristic from rank-up transitions, and its own root does not reproduce —
  see `handoff-adversarial-audit-2026-10-09.md` A6) because that bound governs the
  on-screen 戦闘力, and §3 proved the DB composite is a different quantity.
- **Rarity structure at the DB state:** HP spans only 1277–2033 across ★1–★4
  (1.59× total) while the composite spans 6565–12725 (1.94×). At any trained level
  the rarity separation is far larger (`LEVELING.jet` chunk 19 power: 0 at ★1/Lv.1
  to 105,200 at ★5/Lv.1). Near-rarity-invariant core stats are the signature of
  the pre-growth floor — independent support for L=1.

## 5. What is proven, what is bounded, what remains open

| property of the 62 rows | status |
|---|---|
| gear state | **PROVEN nude** (exact sub-stat identity with the verified Lv.30 nude row; uniform schema) |
| rank / awakening | **printed** (排出時の★; awakened `_1` rows are absent from the DB by construction) |
| level | **framed at-draw by the site's own labels** (基本能力値 + 排出時の★, no level field) and **bounded L ≤ 17**; structural proofs (composite has no level term; rarity-invariant cores; at-draw framing) all point to the floor, L=1 |
| exact printed level | **not printed anywhere** — the one thing a screenshot of the page itself could still add |
| schema uniformity across all 62 rows | proven for Bomber/Support to 0.4%; Offense/Defense fits are looser (0.96–0.98) but still stat-dominated |

Residual risks, stated plainly: (a) the +5,043 trained-state term could include
skill level or transcendence rather than level alone — it bounds the DB state from
above but does not by itself name L=1; (b) the Offense/Defense composite fits are
weaker, so the "no level term" proof is tightest for Bomber/Support; (c) the DB is
a 2019-10…12 capture — pre-rebalance values, to be era-tagged like every other
2019 corpus.

## 6. Adjudication recommendation for the ledger owner

The 62 rows now satisfy two of the three `coverage.md` requirements with proof
(equipment state: proven nude; rank: printed) and the third (level) with
first-party framing plus bounding. Two defensible calls:

- **If derivation counts as documentation** — the level is documented as at-draw
  by the site's own section label and rarity field, corroborated by three
  independent structural proofs — then hero base-stat coverage moves
  **1/113 → 62/113 (54.9 %)**, with the rows labelled "at-draw basic (Lv.1)
  values, gear-proven, 2019 era". The 80-hero target is **not** met by this alone:
  18 more heroes are still required. The remaining 51 heroes have no archive row
  and are the archetype-guesstimation problem (see
  `archetype-guesstimate-2026-10-11.md`).
- **If the rule requires a printed level numeral**, the count stays 1/113, but the
  gap is now a single definitional call rather than an open research question —
  and the rows should be re-labelled from "candidate" to "at-draw basic, level
  bounded ≤ 17".

I have not edited `coverage.md` beyond the observation row; this is the same
restraint the 2026-10-06 note applied.

## 7. Reproduction

- Analysis script (stdlib only): run over
  `findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.tsv`,
  comparing against `datasets/hunters/observed-stats/051.md`; computations:
  sub-stat identity table, rarity-band spreads, per-role least-squares fits,
  positive-base bound, divisor test, per-level rates.
- Page fetch: `browser.tabs.open` on the `id_` Wayback URL above; positive control
  was the page's own known content (title, 戦闘力 8709, HP 1678 — all three matched
  the TSV row exactly before any conclusion was drawn).
- Note: archive.org served this fetch normally on 2026-10-11; the 429 window that
  blocked the OCR lane earlier the same day had passed. The vsfan 178-image census
  is therefore re-open when a lane is assigned to it.
