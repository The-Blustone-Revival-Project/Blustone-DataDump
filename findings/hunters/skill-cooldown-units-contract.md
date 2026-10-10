# Selected active skill cool_time: milliseconds on wire, seconds in native data

Read retained skill construction/Buy exports and narrow original Thumb; no
Ghidra, ADB, runtime or source/state edit. Addresses use G=ELF+0x10000 and raw
reads use PT_LOAD mapping. This resolves units, not every readiness condition.

## Parser conversion is explicit

The hardened literal resolver passed23 self-tests and resolves `cool_time`
at Gf2267e/addPC Gf22682 in SRSKILL_INFO::parse. Numeric/string branches produce
a float. At Gf226f6 the parser loads its divisor; Gf226fc divides that float;
Gf22704 stores the result into reference SRSKILL_INFO+50. The exact divisor
literal Gf22908 is1000.0f. Consequently raw original cool_time5000 becomes
native5.0 seconds. It is not5000 seconds, and publishing5 on the wire would
produce0.005 seconds instead.

Hunter MakeBackEndActor copies reference+50 into default state+4c, preserving
the already-normalized float bits. GetSkillCool G99b19e loads actor default
pointer+8b4 then returns member+4c in the ARM result register; that scalar is
float bits even when a weakly typed decompiler labels it integer. This copy
does not divide a second time. Actor's separate exchange cooldown is default
6c from CardAnalyzer.GetCoolTime/ACTOR_INFO flags; do not merge those mechanics
or substitute exchange readiness for active skill cooldown.

## Native clock/deadline consumers use the same seconds scale

SkillMgr.GetCoolTime G9b28a0 finds a stored deadline entry by registered skill
serial. G9b2a56..66 reads its float deadline and the attached owner's clock+228,
then computes deadline-minus-clock. Expired entries return the ready value and
can be removed by this non-const getter; do not invoke it as a pure diagnostic.
The const overload G9b2e5c is distinct and not automatically the same code.

MakeCoolTime G9b30cc uses the registered ITEM's float duration+30 and the same
attached clock+228; G9b3278..90 and G9b32ec..fc form/store clock+duration. This
corroborates float seconds for deadlines, not Unix milliseconds. The item's
exact registered metadata/owner and actual deadline still require typed proof
before a reader predicts readiness or says this particular actor has five
seconds remaining.

Retained Buy G9b23bc checks item availability/schedule, quantity, cost and
GetCoolTime; a nonzero remaining result returns the cooldown refusal branch.
Owning skill level/rank construction, usable targets, role/stun, icon visibility/
opacity, reserved skill/background pause and group Rage are additional gates.
A parsed5-second cooldown is not proof those gates pass or that a press caused
an activation. Cooldown creation/refresh timing must not be inferred solely
from a photographed icon or the server field.

## Ordinary adapter versus original fixed actor provenance

The episode-actives adapter selects raw5000 from original STAT rows49/47/18
for Lantern/Nene/Tyltyl, with original slot1 cost/crit/effect vectors. Their
ordinary adoption, zero per-level growth and presentation bindings remain
explicit local policies; this units proof does not recover final ordinary
balance or training progression. Existing fixture/neutral modes and saved
skill maps remain separate. Fixed Episode actors keep their original reference
and ACTOR_INFO/selection path; don't overwrite fixed flags to force readiness.

Useful next diagnostic is qualified default state+4c interpreted as f32, plus
the actual registered ITEM duration and deadline/clock under their own owner
contracts. Reconstruct remaining time from immutable reads without calling
lazy GetCoolTime or writing clocks. This report confirms5000ms→5s conversion,
not a successful activation, exact elapsed cooldown or gameplay parity.
