# Bounded Search Partner snapshot: exact guards and layout

2026-10-05. Read-only original ELF symbols/RTTI, constructor stores, existing verified partner dump and raw Thumb. No VM/Ghidra/source/flag/native-call changes. Addresses labeled G are Ghidra; vptrs are **ELF VAs added to guest load bias**.

## Primary vptrs

```text
CSRSceneFindShardSelSupporter: ELF216f2ec
  _ZTV216f2e4+8; offset-to-top0; RTTI216f3c4
CSRPopUpTutorialBase: ELF21691d4
  _ZTV21691cc+8; offset-to-top0; RTTI2169254
CSRUIFocusDraw: ELF2185f4c
  _ZTV2185f44+8; offset-to-top0; RTTI218602c
```

TutorialBase constructor Gd85500 resolves its vtable via GOTELF21adcc8, adds8 atGd85546 and stores primary atobject+0 Gd85558. FocusDraw constructor G1077de0 resolves GOTELF21ae19c, adds8 G1077e6e and stores primary atobject+0 G1077e8a. These are actual constructor-correlated primary guards, not class-prefix guesses. Partner's supplied pointer converts to shared_ptr<CSRScene> without adjustment (Gec1600); its primary matches the existing original vtable and observer identity proof. Secondary listener/address points must not pass these guards.

Optional message object primary is **ELF218596c** (_ZTV23CSRTutorialGuideMsgDraw2185964+8), but this task did not independently reconstruct its full field layout. Do not cast an unknown derived modal/focus pointer merely because its RTTI sounds related.

## Guarded scene ownership and GROUP/THUMB vectors

Use the existing appELF2140cb0/managerELF21735a4 guards and ownership chain g_pAppELF21ef1e0→app+8→manager+34/+38. Require exact current Partner vptr above before any Partner fields. It is the current scene, not an inferred child modal. Do not read manager+44 history as a scene pointer.

After guard:

```text
Partner+678: GROUP begin
Partner+67c: GROUP end
GROUP stride =0x1c bytes =28 DECIMAL
  GROUP+00: numeric type
  GROUP+10: THUMB begin
  GROUP+14: THUMB end
THUMB stride=0x38 bytes=56 DECIMAL
  THUMB+28: availability BYTE
```

Raw SetTutorial proof: G e3008a/e3008e load scene begin/end; **e300b8 increments group by1c**; e300be/e300c0 load type and require2; e300c4 LDRDloads rowsbegin/end from+10/+14; **e300e0 increments row by38**; e300e8/e300ec loads byte+28 and requires exactly1. **Do not interpret GROUP stride28 as0x28**. The available-helper test is only GROUP.type2 AND byte1; other nonzero byte values are not proved available.

The standard vector capacity pointers are expected immediately after each begin/end, but this bounded task pins the actually consumed begin/end fields above rather than claiming separately measured capacity semantics. Reject reversed/unmapped/unaligned ranges, nonintegral stride and counts beyond chosen small diagnostic limits. Limits such as32 groups/32 rows per group are reader safety bounds, not original server capacity limits. If truncated, say so rather than reporting no eligible helper.

No THUMB names/nicknames/card/private user fields need be decoded to count type2/availability. Some row types include real friend data, so output only numeric group types/counts/availability bytes. Reading the selected guide row name or account strings is unnecessary for this initial discrimination.

## Tutorial and focus ownership chain

```text
Partner+6ac: shared TutorialBase object pointer
Partner+6b0: shared control block
TutorialBase+c4: shared FocusDraw object pointer
TutorialBase+c8: shared control block
FocusDraw+850: active input object pointer (nonnull test only)
Partner+2c: generic Scene input byte
```

SetTutorial constructs/stores the first pair and pushes it as a modal; e30192 reads Partner+6ac and **e30196 LDRDloads+c4/+c8** before focusing the selected row. The same fields are used in the later continuation at e37602..e3762c. Their control pointers must not be mistaken for object pointers.

**FocusDraw.OnProcessCursorPress G1079f52** loads+850 at1079f58; nonnull invokes its event pool when present and returns1 at1079f7e; null returns0 at1079f84. It is enough to report nonnull/zero for this field. Its target object's type/child layout and ownership semantics were not audited here, so do not follow it or infer a selected helper ID from it.

Generic **Scene.OnProcessBackKey Gdf4c90** reads byte+2c atdf4c94 and navigates only when it equals1 (df4c98..df4cba); otherwise returns1 without navigation. Report the raw byte and this exact comparison, not an invented broader input mask. TutorialBase's own+2c is a separate scene byte. Its back method additionally checks rawbyte+9d (d85e5c) before optional pause-popup creation; returned0 propagation is not fully pinned and should remain raw optional evidence.

## Race and privacy limits

The snapshot must remain read-only and make no C++ calls. Require mapped spans large enough for each field, exact primary guards and readable nonexpired control pairs. A shared control count of0 can represent one owner in libc++; do not invent a >0 requirement without the existing observer's proved ownership convention.

Repeat app→manager→current/control/vptr and tutorial/focus owner headers after reading bounded vector contents; ideally compare two row-content reads as in the existing Gym observer. Any changed owner/header/content is unstable. Stable equality is not a lifetime lock and cannot eliminate ABA or a stopped-versus-running difference. Unknown vptr or malformed/truncated vector means inconclusive, not zero candidates or missing popup.

The snapshot would distinguish no available type2 helper, active focus interception and ordinary scene input byte without clearing guide37/1 or usage. It cannot prove the e37420 guard executed, identify a precise Back-hand callback phase, restore navigation, or certify resource/controller correctness. New app diagnostic instrumentation/build/release remains parent-owned and required by project policy; none was performed here.
