# Skill magnitude estimates — 2026-10-11

Lane: `findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/`.
Deliverable: `skill-magnitude-estimates-2026-10-11.tsv` — one row per skill slot
(113 cards x 5 slots = **565 rows**), each carrying a per-row class
(`[DERIVED-ESTIMATE]` vs `[INFERRED-FIXTURE]`) and confidence. `coverage.md`
was not touched.

## 1. What the server ships vs what this lane synthesises

`SKILL_REF_RO` (1070 records) ships the *formula* but never `value`,
`value_up` or `duration`. The three live formulas:

| formula | slots using it | meaning |
|---|---|---|
| `-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000` | 124 dmg sub-effects (x5 variant: 37) | direct / bleed damage off ATK (or DEF for reverse) |
| `-1*(value+value_up*skill_level)` | 40 sub-effects | debuff percent |
| `value+value_up*skill_level` | 300+ sub-effects | buff percent / flat |
| `nan` (no formula) | rest | chance gates, rage costs, stuns, immunity, cleanse, switches |

Skill max level = 10x hero grade (1★ -> 10 ... 5★ -> 50), consistent with the
ten 特技-단련 material bands (1~4 ... 45~50) recovered in
`namu-browser-pass-2026-10-10.md` §3.2. Grade per card is
[COMMUNITY-SOURCED] wiki rarity (see `catalog/INDEX.md` §2); the ten
unknown-grade costume rows default to 3★ and carry that assumption in `method`
via their `Lmax=30` tag.

## 2. Anchor ledger (all bounds, no assumed skill level)

**A1. Beckhen 051 active, 피해량 ~9046 [COMMUNITY-SOURCED namu].**
Lv.30 nude ATK 1471, rank 3★ [OCR-CONFIDENT]. Base multiplier
1471 x (8+2x3) = 20,594. Observed V\* = (value+value_up x L\*) = 9046/20594
x 10000 ≈ **4390 at unknown skill level L\* in [1, 30]** (3★ -> Lmax 30).
With slope prior value_up ≈ 0.15 x value (INDEX.md §7.2 convention):
Vmax = V(30) lies in **[4390, ~21000]**; the low end (screenshot at max
level) is judged likelier — wiki showcases maxed hunters. Central fit:
value **800** + value_up **120**/level -> V(30)=4400, V(1)=920.

**A2. Beckhen slot-4 DEF weaken ~30.00% [COMMUNITY-SOURCED namu].**
Same level-unknown bound: V(30) in [30, higher]. Central: 12 + 0.6/level ->
V(30)=30, V(1)=12.6. Percent debuffs must stay < 100 at all levels; this fit
peaks at 30 (3★), 54 at 5★/L50 — sane.

**A3. Beckhen slot-5 opponent block decrease ~30.00% [COMMUNITY-SOURCED namu].**
Same treatment: 12 + 0.6/level. Duration 0 (the EN text carries no
[duration]; aura-style until-deactivation reading).

**A4. Gullveig 039 team attack speed +7.5% (narrative) [COMMUNITY-SOURCED].**
Team-wide, battle-start, permanent: 3 + 0.15/level -> V(30)=7.5. Single
observation, level unknown — same bounding logic, central fit reported.

**A5. Hermes 023 self attack speed +15% (narrative) [COMMUNITY-SOURCED].**
Self, battle-start: 6 + 0.3/level -> V(30)=15. Note the 2x self:team ratio
(15 vs 7.5) is *observed*, not assumed, and matches the self>team ordering
used in the analogy fits below.

**A6. Beckhen slot-2 frontline-mate attack speed ~20.00%, timed
[COMMUNITY-SOURCED namu].** Timed buffs run hotter than permanents: 8 +
0.4/level -> V(30)=20, duration 4.0 s (INDEX.md §7.2 bleed/debuff-template
convention).

**A7. Every-3-s immunity duration 0.51~1.00 s (051 + Mowgli 002)
[COMMUNITY-SOURCED namu].** Duration 0.75 s (range midpoint); the range is
preserved here because no generator should pretend it is a point value.

No anchor exists for: heals (46 slots), crit buffs (32), DR/elem/block buffs,
ATK debuffs, stuns, bleed totals, or anything on the 5★/1★ curves. Those are
[INFERRED-FIXTURE] by analogy, all LOW.

## 3. Per-archetype confidence

`n` = slots. Class rule: `[DERIVED-ESTIMATE]` = archetype fit informed by at
least one numeric anchor (A1–A7) or read literally from recovered text;
`[INFERRED-FIXTURE]` = analogy or convention, no direct evidence.

| archetype | n | value / up | dur | class | conf | basis |
|---|---|---|---|---|---|---|
| active-direct | 62 | 800 / 120 | 0 | DERIVED | MEDIUM | A1 central; level-unknown bound [4390,~21000] |
| active-pen | 47 | 800 / 120 | 0 | DERIVED | MEDIUM | A1 + parity-with-direct assumption |
| active-bleed4 | 33 | 160 / 24 | 4 | FIXTURE | LOW | analogy: 4 s total ~= 1x direct hit; V(30)=880 |
| active-bleed4-all | 4 | 100 / 15 | 4 | FIXTURE | LOW | analogy: AoE total < single-target |
| active-dot-maint | 15 | 200 / 30 | 0=indef | FIXTURE | LOW | analogy; indefinite per recovered text |
| active-fixed2000 | 4 | 2000 / 0 | 0 | DERIVED | HIGH | recovered literal, no free parameter |
| active-reverse | 3 | 0 / 0 | 0 | FIXTURE | LOW | magnitude uses opponent ATK; nothing to fit |
| debuff-def | 19 | 12 / 0.6 | 4 | DERIVED | MEDIUM | A2; V(30)=30 |
| debuff-block | 5 | 12 / 0.6 | 0 | DERIVED | MEDIUM | A3; V(30)=30 |
| debuff-atk | 4 | 10 / 0.5 | 4 | FIXTURE | LOW | analogy-to-debuff-def |
| debuff-misc | 5 | 8 / 0.4 | 4 | FIXTURE | LOW | analogy (aspd/crit/elemres/dr) |
| debuff-stack | 7 | 4 / 0.2 | 0 | FIXTURE | LOW | analogy: per-stack, x5 cap |
| debuff-perm | 3 | 10 / 0.5 | 0=indef | FIXTURE | LOW | analogy; indefinite per text |
| buff-team-aspd | 1 | 3 / 0.15 | 0=perm | DERIVED | MEDIUM | A4; V(30)=7.5 |
| buff-self-aspd | 11 | 6 / 0.3 | 0=perm | DERIVED | MEDIUM | A5; V(30)=15 |
| buff-mate-aspd | 7 | 8 / 0.4 | 4 | DERIVED | MEDIUM | A6; V(30)=20 timed |
| buff-self-atk | 42 | 8 / 0.4 | 0=perm | FIXTURE | LOW | analogy (JOB_ATT role buff) |
| buff-self-def | 32 | 8 / 0.4 | 0=perm | FIXTURE | LOW | analogy (JOB_DEF role buff) |
| buff-team-atk | 25 | 4 / 0.2 | 0=perm | FIXTURE | LOW | analogy; team < self, order of fightclub +10% |
| buff-team-hp | 26 | 4 / 0.2 | 0=perm | FIXTURE | LOW | analogy (JOB_SUP role buff) |
| buff-mate-atkdef | 8 | 6 / 0.3 | 4 | FIXTURE | LOW | analogy: timed frontline buff |
| buff-crit | 21 | 2 / 0.1 | 0=perm | FIXTURE | LOW | analogy: base crit 33, V(30)=5 |
| buff-block | 18 | 6 / 0.3 | 0=perm | FIXTURE | LOW | analogy: base block 14, V(30)=15 |
| buff-dr | 15 | 4 / 0.2 | 0=perm | FIXTURE | LOW | analogy |
| buff-elem | 14 | 2 / 0.1 | 0=perm | FIXTURE | LOW | analogy: base elem 5.0, V(30)=5 |
| buff-hp-misc | 13 | 4 / 0.2 | 0=perm | FIXTURE | LOW | analogy (maxhp/regen/arpen) |
| buff-healpct | 4 | 8 / 0.4 | 0 | FIXTURE | LOW | analogy: instant %HP recovery |
| buff-critdmg | 11 | 0.2 / 0.01 | 0=perm | FIXTURE | LOW | analogy: formula x100 -> V(30)=50% |
| buff-regen4s | 5 | 0.8 / 0.04 | 4 | FIXTURE | LOW | analogy: 4 s %HP recovery |
| buff-tick3s | 2 | 2 / 0.1 | 0 | FIXTURE | LOW | analogy: every-3-s recovery |
| buff-perm | 11 | 6 / 0.3 | 0=indef | FIXTURE | LOW | analogy; indefinite per text |
| heal-instant | 25 | 20 / 1.0 | 0 | FIXTURE | LOW | analogy: DEFxV/100, V(30)=50 ~= 20% HP |
| heal-dot4 | 21 | 8 / 0.4 | 4 | FIXTURE | LOW | analogy: 4 s total |
| stun-timed | 14 | — | 2.0 | FIXTURE | LOW | convention; no anchor |
| invuln-repeat | 3 | — | 0.75 | DERIVED | MEDIUM | A7 range midpoint (range kept in §2) |
| invuln-timed | 9 | — | 2.0 | FIXTURE | LOW | analogy |
| control-misc | 9 | — | 2.0 | FIXTURE | LOW | disable/switch/cleanse; no magnitude |
| control-perm | 3 | — | 0 | DERIVED | HIGH | permanent per recovered text |
| rage-delta | 4 | 1 / 0 | 0 | DERIVED | HIGH | recovered literal +/-1 rage |

Totals: 565 rows, 0 unclassified; 166 [DERIVED-ESTIMATE] (11 HIGH, 155
MEDIUM) vs 399 [INFERRED-FIXTURE] (all LOW).

## 6. Propagation pass 2026-10-11 — analogy-depth promotion (166 -> 379 derived)

Per-archetype `value`/`value_up` of the 166 derived rows was propagated to
fixture rows **only inside the same shipped-formula + scope family**.
`value_est`/`value_up_est`/`duration_est` are unchanged everywhere — only
`class`, `confidence` and `method` move, with the new `analogy_depth`
column recording the chain length (0 = direct anchor / recovered literal,
1 = same formula + same scope/timing, 2 = same formula with timing/scope
extrapolation, NA = residual fixture). All promoted rows enter at LOW
(widened vs the MEDIUM anchors). Tag signal: `SKILL_TAG.json` (565 rows)
confirms the family grouping — HARD_HIT vs BLEED/BLEED_REPEAT/DEEP_WOUND,
DEBUFF(+_CON/_REPEAT)/TEAM_WEAKEN/ENERMY_WEAKEN, SELF_ENHAN/TEAM_ENHAN +
JOB_ATT/JOB_DEF/JOB_GUN/JOB_SUP, INVIN/INVIN_REPEAT/INVIN_TEAM.

| archetype | n | promoted | depth | confidence | anchor chain |
|---|---|---|---|---|---|
| active-bleed4 | 33 | 33 | 1 | DERIVED LOW | A1, same dmg formula; 4 s total ~= 0.2x direct, V(30)=880 |
| active-bleed4-all | 4 | 4 | 1 | DERIVED LOW | A1, same dmg formula; AoE total < single, V(30)=550 |
| active-dot-maint | 15 | 15 | 2 | DERIVED LOW | A1, same dmg formula; maintained every-2-s extrapolated |
| debuff-atk | 4 | 4 | 1 | DERIVED LOW | A2/A3, same pct formula; frontline timed 4 s, V(30)=25 < 100 |
| debuff-misc | 5 | 5 | 1 | DERIVED LOW | A2/A3, same pct formula; heterogeneous targets, V(30)=20 |
| debuff-stack | 7 | 7 | 2 | DERIVED LOW | A2/A3, same pct formula; per-stack x5 cap (5xV(30)=50 < 100) |
| debuff-perm | 3 | 3 | 2 | DERIVED LOW | A2/A3, same pct formula; indefinite timing extrapolated |
| buff-self-atk | 42 | 42 | 1 | DERIVED LOW | A5, same scope (self perm) + formula; stat atk-vs-aspd, V(30)=20 |
| buff-self-def | 32 | 32 | 1 | DERIVED LOW | A5, same scope (self perm) + formula; stat def-vs-aspd, V(30)=20 |
| buff-team-atk | 25 | 25 | 1 | DERIVED LOW | A4, same scope (team perm) + formula, V(30)=10 |
| buff-team-hp | 26 | 26 | 1 | DERIVED LOW | A4, same scope (team perm) + formula, V(30)=10 |
| buff-mate-atkdef | 8 | 8 | 1 | DERIVED LOW | A6, same scope (mate timed 4 s) + formula, V(30)=15 |
| invuln-timed | 9 | 9 | 2 | DERIVED LOW | A7 duration analogy (repeat 0.75 s vs timed 2.0 s); no magnitude |

Deliberately NOT promoted (zero-anchor families — cross-archetype analogy
would be dishonest): heal-instant (25) + heal-dot4 (21) — DEFxV/100 formula
has no anchor; buff-crit (21) / buff-block (18) / buff-dr (15) / buff-elem
(14) / buff-hp-misc (13) / buff-critdmg (11) / buff-perm (11) /
buff-regen4s (5) / buff-healpct (4) / buff-tick3s (2) — stat-specific scales
set by base-stat plausibility (crit 33 / block 14 / DR-block 42 / elem 5.0 /
critdmg 200 from 051.md), not by the aspd anchors; stun-timed (14) —
duration 2.0 s is pure convention; control-misc (9) — no magnitude;
active-reverse (3) — magnitude uses opponent ATK, nothing to fit.

New class split: **379 [DERIVED-ESTIMATE]** (11 HIGH depth-0, 155 MEDIUM
depth-0, 179 LOW depth-1, 34 LOW depth-2) vs **186 [INFERRED-FIXTURE]**
(all LOW, depth NA). Percent-cap recheck: every promoted debuff/buff row
stays < 100 at its grade's Lmax (hottest: debuff V(50)=42, buff V(50)=28).

## 4. Classification method and known limitations

- Primary-effect rule: one row per slot reports the first numeric sub-effect
  in priority damage > debuff > buff/heal > timed-control. Secondaries are
  NOT parametrised (e.g. 023|4's block-weaken alongside its damage roll;
  051|5's +10% Fight Club aura alongside its block aura; 017_1|5's
  every-3-s immunity alongside its self-aspd buff; 010|5's rage trickle).
  The `primary_effect_en` column records which sub-effect the numbers belong
  to, so no row silently mixes two magnitudes.
- Names: `SKILL_EFFECT_RO` (230 records) names only slots 2 and 4, so 339
  rows fall back to `TAG_REF` titles suffixed `[tag-fallback]` (slots 1/3/5).
  Slot-1 rows are additionally identifiable by their `primary_effect_en`.
- Chance gates (30/40/50%), rage costs (3/4) and rage trickles never own a
  slot alone — they always pair with the effect they gate — so they appear
  as documented secondaries, not archetypes. Fixed-2000 actives (4 slots)
  need no fit.
- Percent fits are capped by construction: the hottest debuff (30 at L30)
  reaches 54 at the 5★ L50 cap; no buff/debuff crosses 100 within its
  grade's level range.
- Era caveat: anchors A1–A7 are live-wiki (post-2019-rebalance) readings
  while the 051 stat anchor is a 2018-era screenshot; cross-era fits inherit
  that mismatch. Flagged, not resolved.

## 5. Single most valuable missing observation

**One skill-level reading for any anchored hunter — ideally Beckhen's
특기 레벨 on the same panel that shows 피해량 ~9046.**
Every anchor in §2 is a value-at-unknown-level V\* = value + value_up x L\*,
one equation in two unknowns per archetype family. A single observed L\*
(e.g. "Beckhen active at skill level 27 shows 9046") collapses the
value/value_up degeneracy for the entire 109-slot direct-damage family at
once, and the same screenshot class (skill panel with level + effect value)
generalises to the debuff/buff families. No other single observation —
not even a second damage number at another unknown level — buys as much:
two unknowns need exactly this kind of level tag, and the namu per-role
pages already display the effect values, so only the level readout is
missing. Failing that, the same panel for Gullveig (7.5%) or Hermes (15%)
would pin the buff family instead.
