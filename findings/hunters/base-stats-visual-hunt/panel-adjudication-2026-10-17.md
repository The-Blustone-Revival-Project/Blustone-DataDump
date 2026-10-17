# Stat-panel adjudication — 2026-10-17 (owner decision)

**Input lane:** [`manual-scrapes-2026-10-14/`](manual-scrapes-2026-10-14/scrape-consolidation-2026-10-14.md)
(3,626-screenshot manual transcription lane: 73 batches, 119 stat-panel hits,
22 full HP/ATK/DEF triples). The consolidation was recorded evidence-only on
2026-10-14 with promotion decisions deferred. This file records the owner's
adjudication of those deferred decisions on 2026-10-17.

**Superseding table:** [`hero-at-draw-estimates-2026-10-17.tsv`](hero-at-draw-estimates-2026-10-17.tsv)
(carries the adjudication annotations; the 2026-10-11 file is retained as history).

## Decision

No numeric at-draw estimate changed. The panels either **confirm** existing
estimates, or **conflict** with them without enough evidence to compute a
replacement value. Every affected row now carries an explicit, dated annotation
in its `method` field. Per the 2026-10-11 adjudication rules, ledger edits name
the lane and date; the confirming/conflicting evidence is auditable back to
`scrape-hits-consolidated.tsv` and the `hits/` crops.

Back-calculation model (from the consolidation, unchanged): `stat(L) = at_draw x
(1+r)^(L-1)`, HP r=1.879%, ATK r=1.852%, DEF r=1.930%; confirm bar ±15% on all
three legs, conflict bar beyond ±30%.

## Per-row verdicts

| Catalog | Tier | Verdict | Evidence (panel, deviation % HP/ATK/DEF) |
|---|---|---|---|
| 023 Hermes | A `[RECOVERED]` | CONFIRM (model gold standard) | Hermes-3031 naked-base jewel decomposition, L30 5-star: +3.4/+3.9/+5.2 — validates the ~100% archive row and the growth model simultaneously |
| 010_1 Vincent (Awakened) | D | CONFIRM (strong) | Vincent-3436, L30 5-star: −4.3/+0.7/+1.4 |
| 017_1 Lapis (Awakened) | D | CONFIRM | Lapis-1603, L30 5-star: −10.9/−8.6/−9.8; implied awakened factor ~1.29–1.33, retires the top of the old 1.30–1.93 gear-polluted band |
| 005_1 Gerard (Awakened) | D | PARTIAL CONFIRM | Gerard-831, L8: +3.1/−0.6/+25.3; HP/ATK confirm, DEF leg carries a fate-material caveat |
| 009_1 Captain (Awakened) | D | WEAK SUPPORT | Whiteheart-3417, L28 5-star: −16.5/−15.7/−10.7; provisional DEF, nickname display |
| 020_1 Sienna (Awakened) | D | BORDERLINE (keep D-pending) | Sienna-123, L30: −14.0/+1.8/−16.0; gear state unknown, DEF 1 point outside the bar |
| 071 Anemone | B | CONFIRM with DEF-method flag | Anemone-996, L30: +4.1/+9.3 confirm; DEF +29.4 high — shared B-ladder DEF leg (1053) flagged ~25–30% light |
| 069 Celine | B | BORDERLINE (B stands) | Celine-3281, L30 5-star: −14.9/−11.7/−18.0; HP/ATK confirm the dual-method B point |
| 095 Lawrence (Swim) | B | BORDERLINE (B stands) | Lawrence-3302, L18 5-star: +7.7/+16.3/+17.7; consistent with B, not promotion-grade alone |
| 089 Clara | C | CONFLICT — value retained with flag | Clara-1601, L30: +32.4/+30.4/+50.4 on all legs; unreconcilable at every measured gear quantum; keep C only until a naked-base decomposition |
| 065 Teresa | C | CONFLICT on DEF leg | Teresa-713, L30: HP +17.4 / ATK +10.8 confirm-ish; DEF +33.1 conflict; DEF leg (821) is the disputed leg |
| 068 Selene | C | CAVEAT (not refutation) | Selene-3280, L24 4-star: −53.6/−40.0/−40.0; panel is not in the 5-star state the C point assumes; needs a 5-star panel |
| 083 Kamala | B | CAVEAT (draw-state floor) | Kamala-3151/3290, two independent L1 4-star draws: −35/−27/−15 and −42/−35/−27; L1 draw-state is not at-draw units; pair mean 1248/580/828 is the floor |
| 067 Judith | C | CAVEAT (first direct panel) | Judith-3289, L1 4-star: −39.4/−27.1/−27.5; L1 draw-state caveat |

## Standing findings adopted with this adjudication

- **Growth model scope:** the 1.88%-class per-level model is valid only within a
  fixed star/transcendence state (validated by Hermes-3031-naked). Lv.1 draw-state
  panels are proven NOT to be in at-draw units (Hermes-3008 sits −64/−46/−45%
  under its own ~100% archive row) and must never be promoted without a
  star-state correction.
- **Gear noise floor:** same-hero same-level spreads reach 35–40% (Karl 506 vs
  3158; Hermes 507/642/3031); the ±15% confirm bar sits inside demonstrated gear
  noise. Promotion-grade evidence standard going forward: a naked-base triple
  (jewel/gear-off) + stated level + 5-star, as in Hermes-3031/idx-3033.
- **Promotion standard:** no tier promotion is granted on this lane's evidence
  alone; the confirms raise the standing of the existing D/B rows but exact
  values await naked-base decompositions.

## Remaining gaps

- **Katrina-090 (tier B): zero hits across all 3,626 screenshots** — highest-priority gap among the named task heroes.
- Tier-B/C/D heroes with hits but no triple (no back-calc possible): 056 Genovia, 064 Geranium, 066 Mary, 079 Lawrence (base), 081 Monica, 084 Lottery Mouse, 096 Estelle, 077 Blondie, 063 Erise; 095-swim needs an L30 mate for its L18 panel.
- Method upgrades wanted: naked-base decompositions for every section-4/5 hero of the consolidation; a 5-star Selene panel; a same-state level pair with documented equal gear to pin the growth rate.
- 13 blank-catalog hits await catalog-side resolution (costume variants; see consolidation §2).

No battle was started and no device was operated for this adjudication; all
input evidence was captured 2026-10-14.
