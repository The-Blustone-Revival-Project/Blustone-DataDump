# Ordinary campaign HUD: observed markers and guard limits

2026-10-09. Read-only design audit; no controller implementation, emulator inputs,
runtime changes or Ghidra use. Root retains exclusive emulator control.

## Inspected evidence

At 1080x1920, inspected `testing/campaign-exp-001/fight/013.png`,
`07-fight.png`, `09-paused.png`, `10-result.png`, `11-current.png`,
`12-pause.png`, `06-prep.png` and `13-current.png`. Also inspected historical
`analysis/r016-02-BATTLE-SCENE-RENDERED.png` and
`analysis/r017-03-AFTER-EXIT-8s.png`, which exist locally even though the
default `rg --files` inventory excludes them.

`09-paused` and `12-pause` show ordinary battle without a visible pause modal.
`10-result` is still battle: its blue `100 x100` banner belongs to the enemy
HP/pages display. Filenames do not establish pause or result state. `12-pause`
has coins after enemy disappearance and a hunter speech bubble; neither proves
victory. The campaign report explicitly leaves intermediate transitions and
automatic advancement unattributed.

The historical r017 image visibly shows Victory, three star conditions, Team
Level and collected rewards. It is useful as a result-screen negative, but its
historical exit-input provenance is not proof of a current natural victory.

## Distinct ordinary HUD

Ordinary combat has top-left crate and gold counters, top-right mountain-shaped
distance progress, and a mid-height AUTO / distance bar / X1 footer. It does not
have the Episode timer/enemy portrait strip. The existing Episode guard correctly
rejects fight/013: timer pixels127, enemy-bar pixels0, friendly front2839 and
rear4319, but no qualifying front attribute badges. Lowering Episode timer/red
thresholds would erase the intended mode distinction.

Observed approximate anchor boxes, expressed as x0,y0,x1,y1:

- Crate icon: `(35,137,89,189)`.
- Gold coin icon: `(172,135,229,192)`.
- Mountain/distance line: `(695,137,960,192)`; the pin moves with progress.
- AUTO circular control: `(58,1168,158,1270)`.
- X1 circular arrows/control: `(923,1163,1019,1276)`.
- Front friendly HP stripe: broad search `(100,1015,600,1050)`.
- Rear friendly HP stripes: `(100,1450,1060,1680)`, excluding the central green
  exit-door panel. Use green fill together with dark horizontal track geometry.

These boxes are measured visual observations, not native hitboxes or final
matching thresholds. Header counters may change digits and footer X1 may change
speed. The historical r016 battle displays lock overlays on AUTO/X1. Thus exact
text or whole-box pixel equality would be needlessly brittle. Matching should
prefer distinctive static icon edges/foreground masks and allow known lock and
speed variants only after retaining real examples.

`07-fight` and `11-current` contain bright native impact streaks that cover much
of the scene and replace the rear cabin with dark staging. Friendly front HP and
the top currency icons remain visible. Requiring rear portraits/cabin/HP on every
frame would stop during legitimate attacks. Scene brightness or cyan streaks
alone are not safe ordinary cut-in rejection signals: ordinary impacts already
produce these features.

Enemy absence and absence of the blue enemy banner also occur in intermediate
ordinary battle frames. A red enemy stripe or persistent blue banner cannot be
mandatory. Conversely, friendly HP alone can survive a transition and does not
establish that another attack is allowed.

## Conservative design proposal

Keep a separate ordinary mode. A candidate frame needs all of: correct
resolution; both static currency icons in their header positions; both footer
control shapes in their observed positions; the distance-line shape; at least
one geometry-qualified friendly HP fill; and no recognized modal/result overlay.
The expected stage must already be verified by an independent preparation/start
contract. None of these pixels encode a unique stage ID.

Use explicit outcomes such as `ordinary_hud_observed`, `known_nonbattle`, and
`unconfirmed`; do not label a visual rejection death, loss or pause. The crate /
coin / footer conjunction rejects the inspected preparation, map and historical
Victory result, whereas any single gold/green predicate would be weak. The
Victory coin is relocated to x770/y1300 and its header/footer are absent.

An armed controller must stop at the first frame whose conjunction is absent or
whose stage changed; it must not click Next, map nodes, confirmation modals or
the top-right arrow to try to recover automatically. That arrow's action remains
unresolved in the campaign report. Clicking the central exit door is excluded.
An unconfirmed *already active* battle needs prompt human/root resolution, not
a prolonged research pause, because the user requires continuous attacks.

Preparation's stage identity/start authorization, bounded attack burst length,
fresh foreground/PID verification and fresh screenshot checks remain separate
requirements. A screenshot cannot establish mission reservation, successful
settlement, auto-confirm readiness or the absence of native pause flags.

## Missing validation before autonomous use

No current actual pause modal, loss screen, natural-win transition, partially
entering result overlay, ordinary hunter skill cut-in or enemy skill cut-in was
available in the inspected campaign set. Their retained currency/footer/HP
behavior is unknown. Therefore the proposed conjunction has **not** demonstrated
safe rejection of these states, and no accuracy or comprehensive regression
claim is justified. Existing Episode overlay heuristics cannot be copied without
ordinary examples: their speed-line predicate risks rejecting normal impact
frames here.

First close the root's source-qualified ordinary start/auto-confirm gate, then
retain a complete ordinary run with actual terminal and modal frames. Validate
the mode against those labeled frames and the inspected positives/negatives;
only then authorize automatic ordinary attack inputs. No synthetic screenshots,
renamed filenames or aggregate save progress can substitute for those missing
visual states.
