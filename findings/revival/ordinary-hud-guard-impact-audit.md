# Ordinary HUD impact observation audit (2026-10-09)

Scope: `tools/verify-ordinary-hud.py` is a standalone pixel observer. It neither
drives input nor proves a stage, an outcome, a skill state, or native admission.
No Episode predicate, server, controller, APK, device, or original asset changed.

## Actual misses before the change

Visually reviewed retained native `campaign-receipt-001/11-hud.png` and
`14-hud.png`: both show ordinary fighting with bright cyan impact streaks,
crate/coin, mountain progress, AUTO/X1 and friendly green health bars. These are
positive HUD observations, not recognized menus or settled result screens.

The original observer returned `unconfirmed` for both. Its scores were:

- 11: crate 0.9083, coin 1.0, AUTO 0.7635, speed 0.9869, mountain 0.30.
- 14: crate 0.9083, coin 1.0, AUTO 0.5676, speed 0.9869, mountain 0.50.

Only mountain failed the 0.70 edge gate in 11; mountain and AUTO failed in 14.
Health geometry already passed: coherent >=24-pixel, three-row green fill with
nearby gray/dark track at (456,1030)/(375,1504) in 11, and
(267,1027)/(394,1517) in 14. Health thresholds and search regions are unchanged.

## Bounded alternative geometry

Bright impact pixels saturate AUTO's upper arc. All 76 existing foreground/
background edge pairs on its lower portion (foreground y >=1200) retain signed
contrast >5 in both captures. Mountain translucency reverses contrast against
the bright backdrop; the same 30 coordinate pairs retain absolute contrast >5
in 21/30 (11) and 27/30 (14). No mountain coordinates were resampled.

The original full signed-edge conjunction and thresholds remain unchanged.
An additional conjunction requires all of:

- Original crate and coin masks at >=0.88 each, original speed edges >=0.70.
- Lower AUTO arc signed edges >=0.95, a stricter visibility fraction than the
  original whole AUTO arc's 0.70 threshold.
- The same mountain edge pairs with absolute contrast >5 at >=0.70.
- The unchanged coherent friendly health stripe requirement.

The alternative does not recognize an impact state. It only accepts retained
HUD geometry across a contrast reversal and upper-arc saturation. Original
signed scores and new alternate scores are both returned for diagnosis. Both
captures now yield `ordinary_hud_observed` with reason
`lower_arc_and_mountain_geometry_with_friendly_health`.

## Validation and limits

`tools/python-venv/Scripts/python.exe -m unittest discover -s tools/tests -p
test_ordinary_hud.py -v` passed nine tests covering all 45 distinct retained
native screenshots. Existing positive/negative expectations are unchanged
except the two annotated impacts, now positively required. Missing/truncated
images still decline recognition. Twelve negative ablations, each removing
mountain, lower AUTO arc, crate, coin, speed, or friendly health from one of
the two native captures, each return `unconfirmed`. These modified images
exist only in temporary test directories; they are negative sensitivity checks,
not fabricated positive battle examples.

Every tested output remains `input_authorized:false`,
`stage_identity_verified:false`, `outcome:"unknown"`. The corpus does not
qualify ordinary pause, loss, active skill, or partial result/overlay handling.
Effects or unknown modals may preserve HUD geometry. The widened observation
therefore must not be used as an autonomous attack authorization or an outcome
classifier. A live expected-stage/foreground/native-state qualification and
explicit visual review remain separate requirements.
