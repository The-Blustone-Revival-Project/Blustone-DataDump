# Ordinary campaign HUD observer implementation

2026-10-09. Offline only; no emulator input, Ghidra use, server mutation,
APK rebuild, or Episode-controller change. Root retains exclusive BlueStacks.

`tools/verify-ordinary-hud.py IMAGE` is a standalone PIL-based observer.
`inspect(path)` returns one of `ordinary_hud_observed`, `known_nonbattle`, or
`unconfirmed`. Every response explicitly leaves `input_authorized=false`,
`stage_identity_verified=false`, and `outcome=unknown`. An ordinary positive
means only that the retained ordinary visual conjunction is present. It never
means WIN, loss, pause-flag absence, successful Start, or unchanged stage.

## Native evidence and implementation

Sparse foreground masks were sampled from the actual 1080x1920 native image
`analysis/testing/campaign-exp-001/fight/013.png`; encoded coordinates and RGB
values are bundled in the module. There is no runtime dependency on that PNG.
The crate/coin comparison preserves static colored icon geometry and excludes
counter digits. At least 88% of their samples must match within 35 RGB units.

AUTO/X1 and the distance mountain are translucent over the scene. Direct RGB
matching incorrectly rejected actual impact images, so these anchors use paired
foreground/background coordinates derived from the same native sample. Their
ring arcs and mountain upper edge require local luminance contrast >5 in at
least 70% of pairs, rather than brightness across an arbitrary rectangular box.
The observed minimum in the retained positive corpus is AUTO 74.32% and distance
76.67% on `11-current.png`; the corpus does not establish general accuracy.
No cyan/speed-line rejection is used: `07-fight`, `08-paused`, and `11-current`
are legitimate ordinary impact views with visible front health.

All five anchor conditions must hold together with a geometry-qualified friendly
health stripe: >=24 contiguous green pixels across three rows, plus four nearby
gray/dark border samples. Front search is x100..599/y1018..1050 and rear search
x100..1059/y1500..1679. Rear search excludes the green exit panel. Subpixel/very
low health, moved bars, changed resolution, unfamiliar UI, or unreadable captures
may conservatively become unconfirmed. No threshold was lowered to accept the
Episode HUD.

Recognized retained nonbattle states are sparse text conjunctions: actual r017
Victory-word pixels; actual preparation heading **and** Begin Battle pixels;
actual Episode Paused **and** Resume pixels. These classify recognized visual
text only, not battle outcomes or native flags. Other menus and unidentified
frames are unconfirmed. Recognition runs before positive HUD admission.

## Regression result

`python -m unittest discover -s tools/tests -p test_ordinary_hud.py -v`:
**7 tests passed, 38 real native screenshot cases**, plus missing/truncated-image
checks. Inputs and expectations are annotated actual screenshots, not generated
battle images or predicates repeated as expected results.

Retained positives cover ordinary active fighting, impact streaks, enemy
absence, variable distance pin/counters, front/rear health, and historical locked
AUTO/X1. Historical filenames `09-paused`, `10-result`, and `12-pause` are
visually ordinary battle without pause/result overlays and therefore positive.
Retained negatives cover village, area/map, preparation, native entry warning,
uninitialized scene, actual historical Victory, Episode fighting, actual Episode
pause overlay, and Episode hunter/enemy skill views. Root's current
`campaign-receipt-001/01-current`, `03-areas-settled`, `05-aurora-settled`, and
`07-preparation-settled` are included as negatives.

## Boundaries and missing coverage

No actual **ordinary** pause modal, ordinary loss screen, natural-win transition,
partial result overlay, hunter skill cut-in, or enemy skill cut-in was available
in this corpus. Episode versions do not close those ordinary gaps. A future
ordinary overlay may retain enough anchors to be observed positive. Accordingly
this observer is **not qualified as an autonomous input guard** and does not
expand `attack-battle-visual.ps1`.

Root must verify each fresh frame visually, confirm foreground/client PID and a
fresh expected-stage preparation/Start contract independently, and keep attack
bursts bounded. A screenshot does not carry a unique stage ID. On unfamiliar
states root must promptly resolve an already-active fight instead of leaving it
idle for research. Do not spam menus/results/exit door; do not use the unresolved
top-right arrow as a pause action. Native Start/Complete receipts and persisted
progress remain separate evidence. Broad calibrated robustness needs actual
ordinary terminal/modal/skill captures, not synthetic substitutions.

## Subsequent live corpus (root, same turn)

Aurora33..38 now produced native Start/Complete receipts and natural WIN screens
without active-battle exit input. New first-HUD/tinted ordinary frames10/17 are
observed; actual WIN12/15/38-20 are known nonbattle. Bright impacts11/14 remain
unconfirmed, demonstrating a conservative miss; they are not menus/losses.
Root added a regression separating this uncertainty from known nonbattle.
Eight tests now cover45 actual screenshot cases. This does not qualify autonomous
input: ordinary pause/loss/skill/partial-overlay coverage still remains incomplete.
Private stage-scoped prototypes used native reservations plus root-armed HUD
observation and exact result words, and are not promoted to a general controller.
Back at WIN36 and X at WIN37 did not stop later automatic starts. Settled WIN38
was therefore followed by force-stop of only the instrumented client; no state
clear or rollback. See campaign-receipt-001/receipt-audit.md for exact provenance.
