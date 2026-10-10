# CB0602 front skill input: bounded visual candidate, not eligibility proof

Original native evidence in `active-skill-gesture-rage.md` establishes one
ordinary press on the icon drawable. The icon must be enabled and its event
must deliver opacity byte exactly255. The actor listener additionally requires
IsSkillEnabled and encounter/camp/target predicates. Role-dependent placement,
stun, affordable Rage and exchange/global cooldown can hide or dim the icon.
Do not hold/drag or repeatedly press a skill bubble to bypass these checks.

Retained `episode06-cb0602-001/040.png` shows a white front sword/cost3 bubble
centered approximately `(294,516)`, with displayed Rage10, live enemy Bibi and
the accepted battle HUD. A single ordinary tap `(300,535)` falls inside this
observed bubble. Frame032 shows another white front sword at the same location.
Frame005 has Rage0 and no front bubble: it is not a skill candidate.

No automatic skill-eligibility field was added. Screenshot RGB does not expose
the native opacity byte or enabled/target flags. Counting near-white pixels is
particularly insufficient: the visually translucent front bomb bubble in
frame023 at `(451,519)` still contains1714 near-white pixels in its actual
glyph rectangle `(410,475)-(480,540)`. Frame040's sword rectangle
`(255,475)-(330,540)` contains1294. A fixed `(300,535)` test would exclude023
because its bubble moved, not because it proved the bomb unavailable. The
semi-transparent bubble background must not be equated with native alpha128.
Native eligibility of023 was not read and remains unknown.

For a bounded root-controlled skill observation, identify the actual front
hunter/role and freshly inspect its visible bubble plus displayed Rage. Use
one tap only after the active HUD gate passes, then inspect native debit,
animation/cut-in and outcome. Acceptance of a touch alone is not skill success.
No generic classifier can infer cost or current hunter from this calibration.

Actual Bibi cut-in frames024 and035, and loss dialogue048, all reject the
existing battle HUD gate. These negatives and active040 were added to the
regression suite. Root's retained controller logs, rather than these pixel
tests, establish whether it withheld inputs during the cut-ins. The retained
024/035/048 guard JSON reports `battle_hud:false`, and there are no matching
`.taps.txt` artifacts. Subsequent025/036 report `battle_hud:true` and each has
an associated taps artifact. This supports withheld controller bursts at the
sampled cut-ins and renewed bursts after recovery; it is not a proof about
unobserved inputs between screenshots. Recovery of the missing HUD later does
not authorize clicks on the earlier cut-in frames.

Validation: `python -m unittest discover -s tools/tests -p test_battle_hud_guard.py`
passes six tests. No ADB, runtime, controller, native state or APK changes.
