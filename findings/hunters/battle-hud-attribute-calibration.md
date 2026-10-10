# E06 battle HUD attribute calibration

The visual fallback is implemented in `tools/battle-hud-guard.py`;
`verify-control-pixels.py` only checks image decoding.

Retained native CB0601 frames `episode06-001/24-cb0601-current.png` and
`25-cb0601-current.png` show active combat with a red Lantern hand badge and
a yellow Karl hand badge respectively. The opposing bear has a yellow badge.
These frames must pass even when the old broad cyan test fails.

The new alternative counts red/yellow hand colours inside both front badge
interiors: left `(145,1010)-(200,1050)`, right `(665,1010)-(720,1050)`.
Both require at least 300 matching pixels. Red requires R>=180, G65..160,
B40..130, R-G>=65 and R-B>=85. Yellow requires R>=160, G>=135, B<=100,
R-B>=90, G-B>=75 and |R-G|<=85. Restricting both boxes avoids treating the
red HP stripe or warm character clothing alone as an attribute badge.
This calibration covers these captured colours and placements, not every
possible battle attribute or screen resolution.

The timer threshold, nonzero red enemy stripe, expected portrait defeat-X
rejection and 1080x1920 resolution guard remain required. The original cyan
branch remains available for previously verified frames. The full-screen bear
skill cut-in `episode06-cb0601-001/020.png` has zero warm pixels in both badge
boxes and remains rejected. A rejected frame does not authorize further input;
waiting through a cut-in is the controller's separate responsibility.

Regression: `python -m unittest discover -s tools/tests -p test_battle_hud_guard.py`
passes all five tests, including the original >=24 annotated frames, E05 low-HP
and result transitions, all-enemy-X controls, and the two E06 active frames plus
the E06 cut-in negative. No native identity, pause status, processed attacks or
victory is established by a pixel classification alone.

The subsequent native CB0601 retry captured 35 frames and delivered 30 bounded
bursts. Retained `episode06-cb0601-002/027.png` shows active Lantern combat and
passes; `035.png` contains all three bear portrait defeat crosses and rejects
with `all_expected_portraits_crossed`. Both are now regression cases with the
expected enemy count explicitly set to three. Root verified the original win
dialogue EP1202A and persisted Story02 clear separately from this classifier.
This retry did not sample a missing HUD during active combat; the controller's
new bounded wait branch remains unverified for a midbattle cut-in (only four
startup missing-HUD frames were observed).
