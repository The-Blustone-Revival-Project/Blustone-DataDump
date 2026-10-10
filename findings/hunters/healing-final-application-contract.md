# Positive HP skill healing: final modifiers and observation limits

Read original `ghidra-aura-apply-value.txt`, `ghidra-aura-signed-counter.txt`,
LevelData exports and narrow original Damage/GetDef Thumb. PT_LOAD mapping and
G=ELF+0x10000 were used; no Ghidra, ADB, live test, visual-stat hunt, source/state
edit or retune. Nene37.876→397 during concurrent combat is not an isolated heal.

## Positive amount starts with actual reference DEF

The selected Tyltyl main row uses effect_type1/target_type4/target_stat1,
refer_type1/refer_stat3/base_number150. The parser produces coefficient1.5.
ApplyBuff G99eb3c binds the actual source at+108 for ref_type1 and RefData
G99edc0 dispatches ref_stat3 to source GetDef. That getter uses qualified source
default defense+40 times buff defense+40 clamped0.4..3. A baseline DEF688 is
not necessarily the effective source GetDef at the instant of application.

ApplyBuff multiplies RefData by coefficient and applyCount, saves the float
value at+f8 and calls Apply G99c450. Its SRCalcDamage branch is restricted to
negative coefficients with HP target_stat1/32. Positive HP healing therefore
does not divide source DEF by the recipient's defense through that branch.
Do not apply the fixed damage integer quotient formula to positive healing.

## Stat1 positive branch has its own final modifiers

The positive stat1 branch in Apply negates the signed healing value into the
DAMAGE_INFO amount. If source and bound destination GetAttr words are equal,
it multiplies by selected LevelData+1f8. If the recipient (active binding at
BuffInfo+100) IsDotDmg returns true, it then multiplies that amount by0.5.
Both checks must be read at the actual application; a graphical BLEEDING label
or main skill description alone does not establish the separate DOT counter.

Exact narrow Thumb getters close the read fields: IsDotDmg G99b18c loads
actor+8bc then signed counter+ a8 and returns counter>0 (G99b190..19a).
Zero or negative values are false. GetAttr G99aee0 returns the address
defaultState+7c after loading actor+8b4; native callers dereference that enum
word. Thus same-attribute comparison is the source/destination default+7c
u32 values, not role+80, camp+988 or a skin/portrait label. Root's existing
qualified0xdc default/buff snapshots include both offsets: read/recheck the
owned pairs/bytes and derive the predicate without invoking either getter.

The recovered positive branch does not call GetCriticalChance/GetCriticalBonus,
GetBlockChance/GetBlockDmg or SRCalcAdvantage. Those appear in negative HP/
other damage branches and must not automatically be imposed on this positive
healing path. DAMAGE_INFO's initialized critical/block flags remain distinct
from active skill metadata crt_chance and conditional type4 follow-ups.

Naming correction: actual LoadLevelData G a178c4's field+1f8 is populated from
resolved JSON `elem_def_bonus`, normalized `(raw+100)/100`. The hardened resolver
passed23 self-tests and matched the literal at Ga1916e/addGa19170 to the original
readonly string; decomp Ga191b2..d2 confirms the addition/normalization/store.
No `heal_camp` key or camp-equality check was established here. This branch
compares attributes through GetAttr, not GetCamp. An earlier shorthand
"same-camp healing bonus" would be misleading. Preserve the original reused
field name/offset and distinguish target-camp selection elsewhere in the skill
pipeline from this same-attribute scalar.

## DamageInfo receiving path and presentation

Narrow Damage G99a9b4 checks target HP+8b0==0 and rejects that target before
the ordinary application path. This is not resurrection. G99aa6a onward reads
the float DAMAGE_INFO amount+c. Invincible at buff+9c only zeroes positive
incoming damage; a negative healing amount passes that suppression condition.
It subtracts the signed amount from float HP, so subtracting a negative heals.
It clamps against native maxHP (default+28 times buff+28), retaining the raw
state-dependent lower-bound flag behavior rather than an invented death rule.

The audited receiving body adds no new critical/block/attribute random roll or
natural-recovery multiplier to the positive path. It emits the resulting
damage/HP event after clamp. The native amount and HP remain floats; a green
integer font or rounded HP label is a separate presentation observation, not
an exact float read. This review does not claim its rounding mode. Natural
RecoveryNatual and its delay/clock are separate actors' events, so concurrent
regeneration/damage can still change net HP between screenshots.

## Stat4 is defense, not attack

Apply's exact case4 reads recipient buff state through actor+8bc and adds the
applied value to member+40. GetDef consumes+40; GetAtk consumes+38. Attack
modifier case14 uses+38. Thus target_stat4 is a defense-multiplier effect in
this inspected pipeline, and any prior stat4-as-attack wording is incorrect.
The observed player defenseMultiplier40=0.85 with attackMultiplier38=1 agrees
with Bibi's original stat4/coefficient-0.15 aura payload. This agreement does
not prove every recipient or all lifetime/Unapply behavior. No such mistaken
label was found in this lane's earlier retained scalar/payload reports.

## Direct evidence needed for an exact heal

Read/recheck the qualified source GetDef inputs, copied coefficient/ref tuple,
applyCount and BuffInfo+f8, bound source/destination/active-recipient identities,
their actual attributes, selected LevelData+1f8, recipient DOT counter/state
and maxHP. Separately observe the emitted signed DAMAGE_INFO amount and
resulting HP event, or tightly bound the interval and identify concurrent
damage/regeneration. Do not invoke game-native getters or write flags to
manufacture a clean sample. Until these match at the same application,
688*1.5 is an intermediate candidate, not a guaranteed HP gain, and the mixed
37.876→397 observation must remain qualified.
