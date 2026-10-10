# Native skill types3/5: rank admission, aura registration and refresh

Read retained Hunter MakeBackEndActor G9ac2ac in
`ghidra-enemycamp-decomp-02.txt`, native symbols and existing skill/source
reports. Narrow original Thumb checks used ELF PT_LOAD address translation
(G address minus0x10000), not a flat-file pointer guess. No Ghidra, ADB,
runtime read, balance change, owned-card grant or server/client source edit.

## Constructor admission is independent of the active button's enabled byte

The Hunter constructor obtains actual Analyzer.GetRank and GetAwake, then
FindSkillInfo(awake,type3) and FindSkillInfo(awake,type5). Each passive/aura
branch requires a non-null reference and its target_rank <= actual actor rank.
Type number is not intrinsically the rank: compare the recovered reference's
target_rank rather than assume every type3/5 requires rank3/5 universally.
The original instruction branches G9ada16..28 and G9adbdc..ee corroborate the
two reference/rank tests.

Once admitted, it searches the instance skill-level map for the exact key3 or5.
A missing key reaches the retained assertion path, so dropping locked slot
keys is unsafe. Original GetSkillLV G86f404 simply loads Analyzer's instance
pointer and returns instance+34; it performs no level filtering. The selected
map node's uint level at+14 is converted to float and used to scale copied
effect values. Nonempty effects call AddAura. Empty lists register nothing.

There is no selected-level>0 test between these branches and AddAura. A
rank-admitted nonempty type3/5 reference at level0 still registers its base
effect (base + up*0), not automatically nothing. Missing keys and existing
zero-valued keys are different cases. Do not use zero levels as an invented
passive-disable switch without an independently proved earlier admission rule.
The constructor copies coefficients as base+up*level, and analogous nested
subeffect scalars; it does not use level-1 here. Complete target-stat meanings,
unit conversion and parser arithmetic must remain tied to their own evidence.

These branches do not read actor+a7d (IsSkillEnabled) or the skill-icon opacity
byte. Those are the active-button listener contract. Active skill availability
must not be promoted into aura readiness or used to disable passive effects.
The constructor's ACTOR_INFO/ref overrides and Episode runtime skill selection
can influence actual Analyzer rank/reference/levels, so read those actual
inputs rather than infer them from a portrait level or an enabled button.

## Registration is an aura record, not immediate damage or a UI tap

AddAura G97ed04 appends to actor's vector begin/end/capacity at9cc/9d0/9d4,
with AURA stride0xe8. It copies the BUF_DATA/result fields and its descriptive
strings, and assigns a generated64-bit aura serial at row+e0/+e4. This unique
identity is consumed later; it is not an owned inventory serial or skill type.
The constructor's type3 AddAura call is corroborated at G9adb94; the type5
branch is retained in the decompilation. No tap, Rage debit, active icon or
manual exchange belongs to this registration step.

## Native refresh/target application

Retained TestCollision G9d1c44 calls UpdateAura before consuming its collision
worker result (`ghidra-complete-26-deadgroup-producer.txt`). Original OnRefresh
calls TestCollision under its started/unpaused-background branch. This proves
a refresh path for registered auras during gameplay; it is not a claim that
every paused/startup state refreshes them or that each frame adds another buff.

Narrow Thumb UpdateAura G9e871c shows a source CanRunning gate, traversal of
source aura9cc..9d0 by0xe8, and an extra IsRunning gate when aura target_type==1.
It resolves recipients through FindSkillTargetActors(sourceSerial,targetType),
also resolves type1 actors for context, requires recipient CanRunning and calls
recipient AddAuraEffect(aura,source,context). Precise membership/role/camp and
all target enum semantics are not reconstructed from these names alone.

AddAuraEffect G98241c scans the recipient's buff list for the aura's serial.
The existing-match branch at G9827dc calls Recharge, with subsequent binding/
status comparison and UpdateStat handling. Thus repeated aura refresh is not
proved unconditional new stacking. Complete Recharge expiration/interval and
new-buff binding rules need their own parser/handler proof before predicting
tick counts, additive stacking or removal after a source dies/exchanges.
The retained signatures and calls establish registration→targeted buff refresh,
not a successful live passive activation or original numerical parity.

## Ordinary owned fixtures versus fixed Episode actors

Current fixtureSkillSlots publishes all five keys with target_rank=index+1,
but only active type1 has effects. Types3/5 remain empty. Current starter owned
projection sets skill3 level1 at rank>=3 and skill5 level1 at rank>=5; otherwise
it retains their keys with0. Therefore ordinary fixture rank1 skips both by
rank, rank3 admits the type3 reference but its empty effect list adds no aura,
and rank3 skips type5. These are current local reference/projection policies,
not proof of original passive magnitudes or universal thresholds.

Fixed Episode descriptors have separate explicit skill selections. Original
CB0602 Karl uses `[1,1,0,1,0]`, while first-selected STAT row143 contains only
types1/2/4: absent type3/5 references, rather than their zero levels alone,
explain no aura registration from those rows. Original Bibi STAT includes
type3 target_rank3 and type5 target_rank5; its COMBAT thumb rank4 differs from
STAT rank5. Determine actual constructed Analyzer rank before saying type5
is admitted or suppressed. A five-entry selection with all1 likewise does
not override the constructor's reference/rank tests.

Original numeric effect rows are preserved in episode06-entry-materials.md;
do not map their target_stat15/4 or signed base values to invented labels or
change parameters to make a result pass. Root should close FindSkillInfo/parser
field semantics, actual fixed actor rank/selection, AddAuraEffect/Recharge
duration and source-removal behavior before implementing or claiming complete
passive mechanics. A future bounded observer can report qualified vector/count/
aura serial and actual rank/level facts; finite output alone is not runtime
effect proof. No such reader or new gameplay test was added here.
