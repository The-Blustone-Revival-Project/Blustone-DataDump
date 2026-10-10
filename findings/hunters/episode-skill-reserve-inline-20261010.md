# Inline Episode pending skill serial

Root-only Ghidra readOnly/noanalysis export from preserved original program:
ghidra-skill-reserve-pause-contract.txt, plus existing original instruction
export ghidra-complete-22-insn-groupinfo.txt. Headless session exited0; no saved
project/original changes. Native runtime field validation is pending.

IsSkillReserve G9e6dc8 loads both words game+3d8/3dc, ORs them and returns true
if nonzero. ReserveSkill G9e6910 passes actor serial halves to Group.UseSkill;
after returned effect vector is nonempty (9e6a96..9c), 9e6ab0 stores those halves
inline at3d8. Effect vector storage is separate at3e0..3e8. This is an actor
serial, not a pointer requiring unknown reservation-record ownership.

InspectNativeInput's qualified Episode input snapshot now reads/rechecks both
inline words and prints high/low serial and reconstructed IsSkillReserve.
There is no effect-vector dereference or purchase/application inference.
Java compilation and independent source audit passed. New fields have not yet
been observed on a native paused battle or active DOWN.

IsBGPaused(unsigned) G9dfb1e instead follows game+284 then tests object+278
against the supplied mask; no-argument G9dfb0e tests that member nonzero.
The background object/control concrete ownership remains unclosed, so neither
reader dereferences it. Opposite-front viewport getter/ownership also remains
unproved. Do not conflate game pause140 with background reason8, or this inline
pending predicate with every other input/Buy/cooldown gate.
