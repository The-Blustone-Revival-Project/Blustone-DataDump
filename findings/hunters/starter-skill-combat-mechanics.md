# Starter skill combat mechanics: direct HP, periodic damage, references

2026-10-04. Read-only offline original-library inspection. No adb, Ghidra,
client/server changes or original-file modifications. All code addresses below
use the Ghidra image coordinate (ELF VA +10000). Live behavior still requires
controlled validation; this report separates recovered processing from fixtures.

## Result

A nonempty effect needs a **numeric coefficient**, not merely value_calc.
The actual combat path copies parsed SRSKILL_RESULT_INFO, adjusts its base and
duration by the owned skill level, then multiplies a reference actor stat.
value_calc substitutions are used by the description/UI calculation path.
The prior constant formula with base_number0 is retracted as a damage-producing
example: its parser shape remains usable, but zero coefficient can produce no
combat result even when the UI formula says50.

Recovered distinctions:

- target_stat1: immediate signed HP change routed through DAMAGE_INFO.
- target_stat14: damage/attack **modifier**, AddBuffAtk; not immediate HP loss.
- target_stat32: periodic signed HP damage routed through DAMAGE_INFO.
- target_stat33: integer DOT state/counter modifier, AddBuffDOTdmg; not itself
  a periodic HP-damage effect.

Lantern's original immunity penetration is not implemented merely by choosing1.
The native effect1 avoids buff/debuff admission immunity tests, but the final
Damage function still suppresses positive damage when Invincible is active.
No original missing row/flag that reproduces Lantern's INVI_BREAK is recovered.

## Parser and runtime object bases

SRSKILL_INFO::parse uses effect scratch **sp+110**, proven by construction and
SRSKILL_RESULT_INFO destructor call f21bca..bcc. Relevant member offsets:

```text
+00 serial          +04 target_type       +08 target_stat
+0c refer_target_stat +10 refer_target_type +14 effect_type
+18 delay (zero in inspected parser scratch; no delay JSON key recovered)
+1c coefficient     +20 coefficient_up
+24 duration        +28 duration_up       +2c interval
```

The parser reads base_number twice: raw copies and base_number/100.0 at
f21f7c..84 -> sp12c, i.e.+1c. up_number has the same /100 normalization.
duration -> /1000 at f22064..6c -> sp134, i.e.+24.
interval -> /1000 at f22184..8c -> sp13c, i.e.+2c.
The float literal pool f21d1c/f21d20 is exactly100.0/1000.0.

The fields may be JSON numbers or decimal strings: this client's specialized
from_json<string>728b08 type-dispatches and calls to_string for signed integer,
unsigned integer and float arms (728b4e..70). The examples below use numbers.
value_calc is a string and effect_desc is array<string>.

Hunter MakeBackEndActor9ac2ac copies each active effect into scratchsp108
at9ad0d4. It loads +1c/+20 and +24/+28 at9ad0d8..e4 and does

```text
coefficient = base_number/100 + (up_number/100)*owned_skill_level
duration_seconds = duration/1000 + (duration_up/1000)*owned_skill_level
```

Stores9ad0f6..fa then copies the resulting structure into its runtime skill's
returned effect list at9ad128..13a. Skill level is read from the owned
CSRCardAnalyzer::GetSkillLV map, slot1 at9ad02a..74. It uses skill_level,
not skill_level-1. It also adjusts nested result-duration rows when present.
No value_calc evaluator is called in this inspected conversion or ApplyBuff.

## Source, destination, reference stat and rank

BuffInfo.Bind99e5ce stores source/destination/enemy at+108/+10c/+110.
CSRGameActor::AddBuf981f48 calls Bind with the actual effect source and target
before BuffInfo.Load copies the BUF_DATA into the base of BuffInfo.
Reference type1/default selects source+108;2 selects destination+10c;
3 selects enemy+110, falling back to destination if absent (99ed94..be).

BuffInfo.RefData99edc0 uses a TBB table beginning99edce. Exact branches:

```text
refer_stat1 -> 99ee4c -> source.GetAtk99aef0
refer_stat2 -> 99edf8 -> source.GetAtk /10000
refer_stat3 -> 99ee10 -> source.GetDef99b078
refer_stat4 -> 99ee1a -> source.GetHPMax99abea
refer_stat5 -> 99ee56 -> source.GetHP99abd6
```

Thus ref_stat1/type1 means the current source actor's calculated combat attack,
including its attack-buff multiplier, not a raw server card atk field.
GetAtk99aef0 multiplies actor default+38 by its clamped buff+38 multiplier and
floors the resulting attack to at least1.

Hunter default attack is assigned at9ac59c..5a6 from
CSRCardAnalyzer::CalcDmg86dbe0 -> CSRCard::CalcDmg86a278. The latter gathers
card/equipment/bonus contributions, then tail-calls
SRCalcInGameAttackValue10ac736:

```text
attack_in_game = final_card_attack * (8 + 2*rank)
```

The function's instructions are movs r2,#8; add r1,r2,r1,lsl#1;
unsigned-int-to-float conversion and multiplication. This establishes why the
shipped formula contains8+2*rank. Later stage/bonus adjustments can change the
actor's final default attack; do not double-apply this factor in server stats.

UI CSRCardSkillUtil::Substitution884528 resolves stat at884a32..38 using the
supplied card/stat and reference enum. It resolves rank at884b26..2c from
owning CSRCard+24. The UI reference-stat1 arm8851ee..f4 computes
CSRCardAnalyzer::CalcFinalAttackValue; it is not the same final runtime buffed
actor read as BuffInfo.RefData. Preserve the shipped UI formula but do not
use it as the runtime implementation of damage.

## Application and immunity boundaries

BuffInfo.ApplyBuff99eb3c selects reference actor via+10, gets RefData at99eb7e.
For negative coefficients and target_stat1 OR32, it first computes
SRCalcDamage(reference_value, destination.GetDef) at99eb88..c6.
It then multiplies that by coefficient+1c and applyCount at99ebc8..dc,
stores last applied value+f8 and calls Apply99c450 at99ed0e.
Therefore these skills include the recovered defense path; they are not
unmitigated raw-HP subtraction.

Apply's TBH base99c48c pins target_stat branches:

```text
1  ->99c8a4: DAMAGE_INFO, type1; negative value takes damage path99d508.
14 ->99cb4c: tail AddBuffAtk99b436; changes buff attack multiplier+38.
32 ->99cf80: DAMAGE_INFO, type32; positive value exits99de54.
33 ->99d118: float-to-integer; tail AddBuffDOTdmg99b644; counter+a8.
```

Stat1's negative damage processing includes attribute advantage and further
critical/block/skill processing. Stat32's processing at99cfd8..d0a8 includes
attribute advantage, BlockDmg, then Damage. Neither bypasses Damage's generic
Invincible check at99aa72..88: positive damage becomes0 when victim buff+9c>0.
The zero-check uses this actor's HP and clamps resulting HP to its current max.

CSRGameActorBuff::AddBuff admission99e79a..ee checks effect_type:
3 Buff -> IsImmuneBf;4 Debuff -> IsImmuneDBf;
2 Passive -> positive/negative aura immunity. Effect1 passes directly to the
insertion branch. This is a precise immunity-filter difference, **not proof
of Lantern's shipped Invincible penetration**.

The stat33 counter causes IsDotDmg99b18c=true. Direct stat1 code99ddfa..16
then halves its amount when that state is true. This confirms33 has observable
behavior different from32; its complete original intended pairing is unknown.
Do not add it to002 based solely on the BLEED text tag.

## DOT timing: immediate plus interval ticks

AddBuff increments tickCount+fc and calls ApplyBuff(1) immediately
at99e868..880. BuffInfo.Refresh99eeb8 reads actor delta-time+22c,
start-delay+18, remaining lifetime+f4, interval+2c and tickCount+fc.
The next boundary is delay + interval*tickCount (99ef1e..2a).
At a crossed boundary it increments tickCount and calls ApplyBuff(1)
at99ef30..3e, then advances the next boundary by interval.

For delay0, duration4000, interval1000, normal uninterrupted processing gives
applications at t=0,1,2,3,4 seconds: **five applications**. This is consistent
with the shipped002 formula's *5, but it does not recover the original interval
parameter from a preserved server response. interval1000 remains an inferred
mechanic fixture consistent with the published4 seconds and five multiplier.
The refresh loop supports catching up multiple boundaries after a larger delta.

Expired effect_type4 rows are removed via99f472..4a6. Unapply reverses the
stored amount, but stat32's now-positive application exits without healing.
Expired effect_type1/stat32 rows take99f458..46c (>29) and remain in the list;
remaining lifetime0 prevents further ticks, but the expired record is retained.
That is why4 is the preferred bounded DOT fixture. If1 is deliberately tested,
it needs this lifecycle limitation recorded, rather than calling it faithful002.

## Full candidate rows: local magnitudes, recovered mechanics

These are **nested skill.effect rows**, not the enclosing skill metadata.
They require the already-recovered enclosing type1 slot, source card ownership,
Rage cost4 for001 and3 for002, and appropriate native role/position eligibility.
Original coefficients and exact original effect_type/reference rows are absent.
The following -100 is a fixture100% coefficient; up_number0 is a fixture.
Descriptions/formulas do not determine the combat coefficient.

001 direct HP candidate (does NOT implement original Invincible penetration):

```json
{
  "serial": 1,
  "effect_type": 1,
  "target_type": 1,
  "target_stat": 1,
  "refer_target_stat": 1,
  "refer_target_type": 1,
  "base_number": -100,
  "up_number": 0,
  "duration": 0,
  "duration_up": 0,
  "interval": 0,
  "value_calc": "-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000",
  "effect_desc": []
}
```

002 periodic HP candidate (Debuff4 preferred for expiration):

```json
{
  "serial": 1,
  "effect_type": 4,
  "target_type": 1,
  "target_stat": 32,
  "refer_target_stat": 1,
  "refer_target_type": 1,
  "base_number": -100,
  "up_number": 0,
  "duration": 4000,
  "duration_up": 0,
  "interval": 1000,
  "value_calc": "(-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000)*5",
  "effect_desc": []
}
```

Both formula strings are shipped text. Negative coefficients make the native
HP operation damaging; formulas retain the original display convention. Their
numerical UI/runtime parity has not been measured for these replacement values.
If intentionally choosing effect_type1 for002, replace only4 with1 and retain
the documented expired-record limitation. Do not silently claim that1 is the
original002 effect_type or that the reconstructed coefficient is original.

A Tyltyl-style healing mechanic is structurally supported by HP1 positive
coefficient + source DEF reference3/type1 + FrontAlly target4. Apply stat1 sees
a positive amount, negates it into DAMAGE_INFO, and Damage subtracts a negative
amount (healing), capped at maxHP. A complete original Tyltyl row and magnitude
are not recovered here. A candidate100 coefficient corresponds to source DEF
before native healing/attribute processing, not100 flat HP.

Validation needed before promoting fixtures: real skill spends original Rage
once, generates nonzero returned effects, changes actual HP with defense and
attribute processing, runs five bounded002 applications, expires normally,
returns input after its cinematic, and survives repeat activation. Distinguish
these local mechanics from original-stat or Invincible-penetration fidelity.
