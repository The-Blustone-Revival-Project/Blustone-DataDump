# Fixed Episode actor skill scalar: reference, units and damage boundary

Read original skill-construction/actor exports, `ghidra-aura-apply-value.txt`,
starter-skill-combat-mechanics.md and original Karl STAT provenance. Narrow
Thumb checks used PT_LOAD mapping with G=ELF+0x10000. No Ghidra, ADB, new visual
stat hunt, state/source edits or balance retune. The observed enemy HP1581 after
one activation plus intervening attacks is not an isolated damage measurement.

## The coefficient is-20; wire ATK750 is not the reference scalar

Original first-selected CB0601_012_1 STAT row143 supplies main effect
effect_type1/target_type1/target_stat1/refer_type1/refer_stat1/base_number-2000.
The shared parser divides base_number by100, giving runtime coefficient-20.
It does not interpret that wire number as flat HP damage. Ordinary per-level
growth is not supplied by this fixed row; exact selected copied effect and
skill-level arithmetic still belong to the constructor/readback contract.

BuffInfo.ApplyBuff G99eb3c chooses the bound source actor at+108 for ref_type1,
destination+10c for2, and context+110 for3 (falling back to destination if null).
RefData G99edc0 dispatches ref_stat1 to actual actor GetAtk G99aef0. Ref_stat2
uses GetAtk/10000; that is a different selector and must not be substituted
because its scale would make a guessed calculation convenient.

Fresh GetAtk Thumb proves:
`max(1.0f, defaultStat[+38] * clamp(buffState[+38],0.4f,3.0f))`.
Actor default/buff pointers are+8b4/+8bc. The0.4 lower multiplier literal is at
G99af2c; the upper3 and final minimum1 are instruction constants. This function
is a float calculation, not simply the server JSON atk string or card-panel
number. It does not apply the skill coefficient itself.

## Defense precedes the skill coefficient

For a negative coefficient with target_stat1 or32, ApplyBuff converts RefData
and destination GetDef into signed64-bit inputs and calls SRCalcDamage G10ac7c0.
Then it multiplies the returned float by coefficient and applyCount, records
the signed result at BuffInfo+f8 and calls Apply. Fresh GetDef G99b078 reads
destination default+40 and buff+40 with the same0.4..3 multiplier clamp; it has
no additional final minimum1 in the inspected body.

SRCalcDamage itself is a small native wrapper, not an unproved smooth-defense
formula. It loads both64-bit operands, calls G1be343c, then G1be2fa8. Narrow
helper instructions establish the signed division/remainder wrapper: the
denominator-zero branch is distinct; its normal G1be3598 calls the quotient
helper G1be3840 and computes numerator-minus-denominator-times-quotient for the
remainder. G1be2fa8 converts the signed64-bit result to float. For ordinary
positive attack/defense inputs this is integer quotient behavior before the
skill coefficient, with the input conversion/truncation boundary retained.
Do not describe it as raw ATK*20 HP subtraction, or silently substitute a
different defense formula. The unobserved zero-defense case is not a reason
to set enemy defense to an invented value.

Apply's target_stat1 branch then enters DAMAGE_INFO/native damage processing:
attribute advantage, critical/block/skill modifiers, immunity/Invincible,
HP clamp and concurrent events can change the final HP movement. The scalar
before that boundary is not a promised observed HP delta. Type2 follow-ups
and conditional type4 effects can share an activation; an enemy HP snapshot
after ordinary bursts mixes those paths with normal attacks/regeneration.

## Fixed construction differs from ordinary card arithmetic

Hunter MakeBackEndActor G9ac2ac stores Analyzer.CalcDmg into defaultStat+38.
Ordinary Analyzer.CalcDmg G86dbe0 delegates to CSRCard::CalcDmg G86a278. The
recovered SRCalcInGameAttackValue G10ac736 multiplies its float input by
`8+2*rank`. That factor is a native construction consumer; do not pre-multiply
wire stats and then apply it again. Even proving that generic helper does not
prove which scalar the fixed Episode actor supplies on this run.

ACTOR_INFO+5c controls distinct construction routes. Bit0x100 selects LoadForGVG;
the ordinary path loads a card but bit0x08 then invokes Analyzer.Load(ACTOR_INFO)
and can use the explicit CardInfo at ACTOR_INFO+3c for reference role/attribute.
This fixed-data Load G86cc60 is distinct from Load(sharedCard) G86cf68.
After construction, ACTOR_INFO multiplier+0 modifies default attack+38, and
multiplier+4 modifies default defense+40. Episode overrides, bonuses/equipment,
actual selected rank/reference and these multipliers cannot be guessed from
portrait thumb level1 or the STAT atk750 string alone.

Neither `750*20=15000` nor a rank-adjusted variant is established final damage.
The original effect coefficient-20 is known; actual source GetAtk, converted
destination GetDef, copied effect, bound target and downstream modifiers need
runtime evidence. Preserve original row143 and its duplicate-selection rule;
do not change Karl/enemy stats to make the screenshot agree with a prediction.

## Most direct bounded read to validate the scalar

Root can add diagnostic fields to its already owned actor/body/state path:
actual source default+38 and buff+38, destination default+40 and buff+40,
actual constructor rank at default+14, and the selected active result's typed
coefficient/reference/target tuple. Qualify the ACTOR_STAT/ACTOR_STATE owner
and range before reading data through+8b4/+8bc; a mapped pointer alone is not
complete allocation proof. Capture/recheck source/destination serial/camp,
BuffInfo bound source/destination/context+108/+10c/+110 and effect bytes.

Reconstruct only the audited float getters/conversion/division from those
samples without invoking native lazy/game getters. If an active recipient
BuffInfo is captured, its last applied+f8 and appliedCount+fc provide a more
direct scalar observation, but still require the exact bound source and effect
identity. A short before/after HP interval without ordinary bursts, after
qualified native pause handling, can separately constrain HP application;
do not claim simultaneous enemy hits or regeneration were absent without
evidence. Current observed M024HP1581 remains a mixed-event screenshot, not
proof of14k/15k damage or a reconstruction defect.
