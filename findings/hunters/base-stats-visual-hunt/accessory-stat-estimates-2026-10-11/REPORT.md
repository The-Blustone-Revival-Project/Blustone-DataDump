# Accessory main-stat estimates — verification report (2026-10-11)

Lane folder: `findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/`
Artefacts: `accessory-stat-estimates-2026-10-11.tsv` (100 data rows), `per-level-curve.tsv` (L1–L50)
Builder: `tools/build_accessory_estimates.py` (read-only outside lane)
Status: verified, read-only check. `coverage.md` not edited.

## 1. Row / tier verification (executed)

- Data rows in TSV: **100** (header + 100, lines 2–101).
- Distinct `item_name_en`: **100/100**, no duplicates.
- Tier counts: **T1 = 1, T2 = 96, T3 = 3**.
- Class counts: `[RECOVERED] = 1` (Jack), `[DERIVED-ESTIMATE] = 99`.
- Point-confidence distribution: `100 x1 / 85 x96 / 80 x3`.
- Band check: all T2 Lv50 bands `(208, 312)` = ±20% of 260; all T3 bands `(195, 325)` = ±25% of 260; T1 band `(260, 260)`.
- `max_hp_lv1` set = `{135}`; `max_hp_lv50` set = `{260}` for all 100 rows.

## 2. CHAR_STR coverage — correction to "100 distinct names" wording

`charstr-items-2026-10-06.tsv` has 105 rows total:

- 98 rows with a non-empty `accessory_en` cell.
- **97 distinct** `accessory_en` values (only duplicate: `Hybrid Gloves` on nums 068 and 098).
- 7 empty rows (nums 901/902/903/904/912/913/914, TITLE/VICTORY only).

Estimate-TSV coverage:

- All **97/97** distinct shipped CHAR_STR accessory names are present — zero missing.
- The estimate TSV has **100** distinct names = 97 shipped + 3 awakened-form extras absent from shipped CHAR_STR:
  `Damaged Union Epaulet` (010_1), `Heat Resistant Railgun Gloves` (020_1), `Union Epaulet` (009_1).
- So the lane covers 100/100 distinct **catalogue** accessory names, not 100 distinct CHAR_STR names. The prompt wording conflates the two; the corrected statement is above.

## 3. Anchors

- **A1 — Accessory cap (T1):** `Jack` (Beckhen 051 accessory), Lv.50/50, **Max HP 260**, from `datasets/hunters/observed-stats/found/faq-image21-gear-accessory-jack.png`. Cross-checked inside the same build: 260 + jewel HP 58+21+58+18+21 = 436 vs observed equipment delta +437 (1-point rounding residual). Class `[RECOVERED]`, point 100, band 0.
- **A2 — Armour slope pair:** `Chicken Wings` DEF **102 @ Lv.50** (`faq-image20`) + `Purple Combat Coat` (Vincent 010) upgrade preview **DEF 101 @ Lv.49 → 102 @ Lv.50** (`faq-image07`). Same-item two-point fit gives `DEF(L) = 52 + L` exactly (up = 1/level).
- **A3 — Rarity invariance:** Chicken Wings is on 3-star Beckhen (051); Purple Combat Coat is on 4-star Vincent (010). Same Lv.50 value (102) across rarities is the only evidence for applying a slot-level (not per-item, not per-rarity) model to accessories.
- **A4 — Slope bound:** `faq-image08` accessory at Lv.20, whole-HP-equipment delta +221, bounds the accessory's own contribution: `acc(20) <= 221`, hence slope 1.300–5.200 and base 0–195 (computed in builder; the adopted slope 2.549 sits inside the bound).

## 4. Model (M1–M4, per builder docstring)

- **M1 shape:** `main_stat(L) = base + up * L` (linear in item level; shape-identical to the native card-stat helper `uint32(base + up*level) * multiplier`).
- **M2 scope:** main stat is a function of SLOT × ITEM LEVEL, not of the item or owner rarity (evidence: A3 pair).
- **M3 armour:** `DEF(L) = 52 + L` from A2.
- **M4 transfer:** keep the armour's normalised increments (`base/MAX = 52/102`, `up/MAX = 1/102`) and apply to accessory cap MAX = 260 (A1):
  `Max HP(L) = round(260 * (0.509804 + 0.009804 * L))`.

`per-level-curve.tsv` validation (executed): **50/50 rows match** the formula exactly; endpoints L1 = 135 / L50 = 260, consistent with every estimate row. The same normalised fractions also generate the `def_armour` (cap 102) and `atk_weapon` (cap 134) columns.

## 5. Tier definitions

| Tier | N | Meaning | Point / band |
|---|---|---|---|
| T1 `[RECOVERED]` | 1 (Jack) | Printed Lv.50 panel value, no model applied | 100 / 0% |
| T2 `[DERIVED-ESTIMATE]` | 96 | Shipped CHAR_STR num present; Lv.50 = Jack cap, levels 1–49 from M1–M4 curve | 85 / ±20% |
| T3 `[DERIVED-ESTIMATE]` | 3 | Same curve; identity from live-wiki crosswalk + card catalogue only (`in_shipped_2_8_0_1_CHARSTR=NO`) | 80 / ±25% (T2 minus 5 for identity provenance) |

## 6. Coverage under the >= 60%-point rule

- All 100 rows have `confidence_point_pct >= 60` (min = 80): **100/100 (100%)**.
- By tier: T1 1/1, T2 96/96, T3 3/3 pass.
- No row falls below the threshold; nothing is excluded under this rule.

## 7. Residual uncertainty (do not over-claim)

1. Single-item anchor: only one printed accessory Lv.50 value (Jack 260). All other Lv.50 = 260 values are transferred, not observed.
2. Lv.1 = 135 is pure model output (`round(260 × 0.519608)`), not a printed reading.
3. Linearity between L1–L50 is inherited from a two-point armour fit (49→50); curvature or per-item slopes would break M4.
4. Rarity invariance is proved for one armour value (102 on 3-star and 4-star heroes), only asserted for accessories (several T2 rows span rarities 1/5, 2/5, 4/5).
5. Bands (±20% T2, ±25% T3) are judgement margins, not measured dispersions; the only hard slope bound is the wide 1.3–5.2 interval from faq-image08.
6. The +1 residual in the Jack jewel cross-check (436 vs +437) is consistent with rounding but leaves the exact jewel-stacking rule unproved.
7. T3 identity rests on wiki + catalogue, not shipped CHAR_STR; a catalogue/wikiname mismatch would orphan those 3 rows.
8. Main stat is uniformly `Max HP`; any accessory with a non-HP main stat would invalidate its row (none observed, but only one panel transcribed).
