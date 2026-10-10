# Visible skill-button gate

`tools/battle-skill-button-guard.py` is a fail-closed visual aid for an explicitly
approved physical point on a fresh 1080x1920 frame. It first calls the existing
battle HUD gate with the expected enemy count. It does not establish actor
identity, native admission, cooldown, stun, rank, or available Rage.

CLI: `python tools/battle-skill-button-guard.py image_path x y expected_cost expected_enemies`.
JSON `visible_button` is the controller-facing result; `visible_skill_button`
is an equivalent descriptive alias. Costs other than 3 and 4 are unsupported.
Optional `--rage` uses only the caller's explicitly supplied number; no Rage
is inferred from elapsed attacks, a milestone, or the screenshot.

## Retained template provenance

The three 137x137 RGB PNGs in `tools/skill-button-templates` are lossless crops
from existing native screenshots. They contain UI pixels only, not account
identifiers. Center coordinates use the original frame coordinate system:

- `shield3.png`: `analysis/testing/episode6-complete-001/fight/015.png`,
  center (294,514), crop (226,446)-(363,583).
- `sword3.png`: `analysis/testing/episode6-complete-001/fight/020.png`,
  center (953,1395), crop (885,1327)-(1022,1464).
- `heart4.png`: `analysis/testing/episode6-complete-001/fight/015.png`,
  center (342,1410), crop (274,1342)-(411,1479).

These names describe retained graphics, not a stable actor assignment. A sword
bubble may belong to different actors. The function only checks whether a
supported button appearance with the requested visible cost surrounds the
caller-approved point.

The search is limited to centers within 32 pixels per axis of that point.
Matches require all three calibrated measurements: cost-fill overlap >=0.90,
whole icon-fill overlap >=0.88, and circle-annulus luminance difference <=18
against the retained crop. Fill masks threshold luminance at 235. The annulus
spans radii approximately 55-65 pixels. Distant or different-template matches
are rejected as ambiguous. These are conservative retained-frame thresholds,
not measured classifier accuracy or native hitbox bounds.

## Verification and limits

Six regression tests pass, covering twelve annotated combat points; story,
map, cut-in and loss rejection; wrong cost; invalid requests; explicit
insufficient Rage; and deliberate removal of cost/circle context. Frame 021's
Karl bubble is an independent later image and passes despite its center moving
seven pixels vertically from frame 020. Template-source positives are calibration
checks, not independent detection evidence.

Missing, faded, occluded or unfamiliar graphics may be denied even when a native
skill would work. The gate deliberately supports only the three retained
appearances. It is not OCR, a general circle detector, or an actor tracker.
A true result permits a planned *attempt*, not a claim of accepted skill use.
Without explicitly supplied fresh Rage, funding stays `unproved`. Callers must
keep ordinary attacks prompt during bounded visual deferral and must not idle
combat for analysis. No emulator, server, saved state, original package or
instrumented APK was changed while developing this helper.
