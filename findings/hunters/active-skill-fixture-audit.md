# Active skill fixture audit

2026-10-04. Read-only audit ofserver-ts/src/skills.ts against recovered native
processing, source catalogue formulas and prior native reports. No runtime
control, source edits, adb/Ghidra or client changes.

## Conclusion

**No concrete selector, coefficient-sign or millisecond-conversion error was
found in the four slot1 effect rows.** They are coherent opt-in mechanics
fixtures. This is source/native-contract agreement, not a successful live
activation or original balance claim. Do not manufacture a bug merely because
original numeric parameters are missing.

## Proved agreement

- Slot keys are type1..5; active type1 andtarget_rank1 is usable for ordinary
  rank1+ cards. Keeping all five neutral slots avoids the earlier map::at fault.
- 001/003 direct damage uses effect_type1,target_type1(Enemy),target_stat1(HP
  change),source ref_type1/ref_stat1. LV1(-95 + -5*1)/100=-1.0, exactly a100%
  native source-attack coefficient before its defense/attribute/block processing.
- 002 uses **Debuff4 / periodic HP32**, Enemy1/sourceAtk1. LV1(-19 + -1)/100
  =-0.2 per application; duration4000/interval1000 are milliseconds, already
  divided by the native parser. Initial application plus boundaries1..4 gives
  nominal five applications. Debuff4 expiration avoids retaining an expired
  Activate1/stat32 record. Selecting33 instead would set a DOT counter, not
  schedule this HP damage; the source correctly uses32.
- 004 uses Activate1 / FrontAlly4 / HP1 with source DEF ref_stat3/type1.
  LV1(95+5)/100=+1.0; the native positive-value branch heals/caps at maxHP.
- Costs4/3/3/4 agree with shipped001/002/003/004 slot1 text.
- Damage/DOT formula text matches the shipped001/003 and002 definitions.
  Heal formula `stat*(value+value_up*skill_level)/100` is likewise the exact
  shipped004|1|1 formula, corroborated incatalogue/cards/004.md.
- Numeric base/up—not formula text—drive live combat after native skill-level
  adjustment. The source correctly supplies nonzero numeric coefficients and
  does not repeat the earlier formula-only/base0 diagnostic error.

## Inferred or intentionally incomplete

-100% direct/+100% DEF and20% DOT coefficients, their5%-per-level/1%-per-level
upgrades, names and special cooldown0 are local fixtures. Native arithmetic is
verified; those magnitudes/upgrades/cooldowns are not original recovered values.
The source's opening comment establishes this, but UI names/descriptions alone
must not later be cited as recovered proper skill names or balance evidence.

Enemy1 andFrontAlly4 enum meanings are recovered, but original wire selector
rows are absent. Matching the published frontline prose is a reconstruction,
not proof that an original server row used exactly that combination.

DOT interval1000 is consistent with the four-second prose and shipped *5
formula plus native immediate-tick schedule; its original interval parameter
was not recovered independently. Runtime clock/pause/overkill can affect
observed timing/number of visible HP changes; test the actor effects.

Original001 INVI_BREAK/Immunity penetration is absent. Effect1 skips
buff/debuff admission immunity filters but generic Damage still checks
Invincible. The source description appropriately omits the original penetration
claim; do not mark full Lantern fidelity after only ordinary HP loss.

Slots2..5 remain inert, so follow-ups/passives (Nene stun, Tyltyl team HP,
etc.) are not revived. Empty cut_in_id/icon_id resource bindings remain a
material native activation/cinematic completion uncertainty. That is a runtime
risk, not a proved crash or a reason to guess resource ids.

## Focused native validation

For the opt-in profile, verify fresh reference consumption, owned slot1 LV1,
matching costs and opaque ready skill icon. Use one normal tap—no hold/drag—on
front Mowgli or eligible airship Lantern/Tyltyl, after measuring actual group SP.
Require protocol10/ReserveSkill, nonempty effects, one cost deduction, real
HP/DOT/heal result and complete return to normal input. Also verify DOT
expiration and repeat activation. UI formula/runtime amount parity is still
unmeasured and must not be asserted merely because formula strings are original.

No source change is recommended by this audit before the bounded live test.
