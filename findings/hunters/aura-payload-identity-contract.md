# Typed AURA payload identity: parser, copy and normalized signatures

Read original AddAura/skill constructor exports, episode actor parsing,
starter-skill-combat-mechanics.md and the latest bounded reader/source capture.
Fresh original Thumb checks used PT_LOAD mapping and G=ELF+0x10000. The hardened
segment-aware literal resolver passed its23 self-tests and resolved29 literals
in SRSKILL_INFO::parse Gf219ac..f225d8. No Ghidra, ADB, native game calls,
balance/state mutation or server/client source edit by this lane.

## Typed numeric prefix is preserved into AURA row0

The parser's effect scratch starts at sp+110, corroborated by its destructor
call Gf21bca/bcc. Resolved JSON keys and corresponding stores establish:

```text
row+00 u32 definition serial   row+04 i32 target_type
row+08 i32 target_stat         row+0c i32 refer_target_stat
row+10 i32 refer_target_type   row+14 i32 effect_type
row+18 f32 delay               row+1c f32 coefficient
row+20 f32 coefficient_up      row+24 f32 duration seconds
row+28 f32 duration_up seconds row+2c f32 interval seconds
```

Integer stores include effect_type→sp124 Gf21cca, target_type→sp114 Gf21d7a,
target_stat→sp118 Gf21de2, refer_target_stat→sp11c Gf21e4a and
refer_target_type→sp120 Gf21e98. The0x18 scratch member is zero in this parser
path; no delay JSON key was recovered. Report its actual value rather than
invent a wire delay field.

SRSKILL_RESULT_INFO::operator= G988d5c directly copies the numeric prefix,
including blocks0..0f/10..1f/20..2f at G988d66..92. AddAura G97ed04 applies that
assignment to the new AURA row start, then separately copies its descriptive
strings. The typed vector stride is0xe8. Its generated64-bit aura identity is
row+e0/+e4 (AddAura end-8), distinct from definition serial at row+0. A generated
ID must not be used as a skill type, owned hunter ID or JSON definition serial.

## Normalization and construction arithmetic

Parser literal pool Gf21d1c/f21d20 contains float100.0 and1000.0. Direct division/
stores corroborate base_number/100→sp12c (Gf21f7c/84), up_number/100→sp130
(Gf21ff0/f8), duration/1000→sp134 (Gf22064/6c), duration_up/1000→sp138
(Gf22110/18), and interval/1000→sp13c (Gf22184/8c). These are relative to
scratch110 and therefore exactly the prefix offsets above. Numeric JSON or
decimal-string conversion does not change these units.

Hunter type3/5 admission copies each parsed result, then applies
coefficient += coefficient_up*selected_skill_level and
duration += duration_up*selected_skill_level before AddAura. Original type3
Thumb G9adb44..62 confirms the two multiply-add/store operations against scratch
sp108. It uses level, not level-1, and leaves a zero level capable of registering
base values when rank/reference admission passes. The prefix up fields remain
reportable; do not infer zero-level suppression or divide a second time.

The enums are raw numeric tags parsed from effect JSON, not the enclosing
SRSKILL_TYPE1..5. `effect_type=2` is not evidence that an aura came from skill2.
Do not assign user-facing stat names to target_stat15/4 merely from this identity
read. Runtime target selection, buff admission, Recharge, Apply/Unapply and
immunity/stat mappings are separate contracts.

## Original Bibi rows and the live registration match

Original CB0602_040_1 STAT in episode06-entry-materials.md supplies distinct
candidate signatures. Skill3: effect_type2, target_type2, target_stat15,
refer_type2/ref_stat0, base_number-3, duration500, interval0. Skill5:
effect_type2, target_type1, target_stat4, refer_type2/ref_stat0, base_number-15,
duration500, interval0. With absent up values normalized to0, their expected
core payloads are coefficients-0.03/-0.15, duration0.5 seconds, interval0.
The enclosing type/rank and actual actor rank/level still require their own
constructor provenance; matching a count of two was insufficient.

Root's paused `aura-identity-001/payload.txt` now reports generated1e1f with
target2/stat15/ref2/0/effect2/coefficient-0.030000/duration0.500000, and1e20 with
target1/stat4/ref2/0/effect2/coefficient-0.150000/duration0.500000. Both have
definitionSerial0, delay0, up fields0 and interval0. The recovered enum integers
and normalized values match the original skill3/5 core signatures at the
printed six-decimal precision. This identifies the registered payloads beyond
count-only evidence; it does not establish complete row byte identity or exact
floating-point bits from text output.

## Bounded read contract and claim limits

The latest reader guards owned actor and SkillMgr emplace allocation, vector
pointer alignment/order/stride/capacity<=64, mapped typed row extent and generated
serials. It reads a little-endian0x30 prefix, rejects nonfinite floats, repeats
prefix bytes/serials/vector/manager owner fields before output and calls no native
game getter or writer. This numeric-only read avoids strings, nested lists and
unproved per-row polymorphic casts. Unknown enum tags should stay raw/qualified,
not be relabeled into a convenient known mechanic.

Registration evidence is now concrete. Recipient binding, actual applied stat
change, duration/refresh/removal and all skill-type behavior remain outside this
prefix read. Preserve the distinction between an original payload registered
on Bibi and that payload successfully affecting a specific player actor.
