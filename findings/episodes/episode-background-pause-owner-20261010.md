# Episode background pause and corrected supporter admission

Original native source was exported with readOnly/noanalysis; transient Thumb
reclassification discarded. Original ELF, saved Ghidra project, APK and server
stats unchanged. Root exports and independent read-only review corroborate:

- GameBase constructor G9c11da allocates separate CMUpdatable0x280, named
  `Opp` (literal slot9c13b4/ADD9c11ea), stores it at game284. Control0x10,
  pointercontrol+c, shared owner at game288; initialized counts0.
- Control slot9c13b8 word17fa09c + ADD9c1204+4 → GOT21bb2a4, word214607c+8
  gives G2146084 / ELF2136084 primary. Concrete allocation evidence comes from
  this actual constructor, not the unrelated named CMDrawable factory9c0c2c.
- Object constructor785960 LDR7859d6 slot785cf0 word1a35e0c + ADD7859e4+4 →
  GOT21bb7f4 word214a86c+8 gives G214a874 / ELF213a874 CMUpdatable primary.
- IsBGPaused G9dfb1e reads game284→object278, tests supplied mask8. This is
  independent of GameBase.pause140. Do not equate the two or treat the `Opp`
  label as a recovered sprite/background resource.

InspectNativeInput now qualifies separate object/control/pointer/nonexpired
ownership, reads bounded0x280 object, repeats owned pair/control/count/link and
all object bytes, then prints pause278/IsBGPaused8. Unknown owner refuses. It
does not invoke getters or alter pause, reservation or effects. Inline skill
reservation remains game3d8/3dc serial nonzero, not a pending object pointer.

Material correction: earlier episode06-support-skill-application.md and §180
had the extra front-stun branch reversed. Original Thumb G9f78a8 calls
IsSupporter; CBNZ9f78ac jumps9f78ba, bypassing LDR samecampnode+8 / IsFrontStun
9f78b2 / reject1. IsSupporter97e6fc delegates to SRCanUseSkillAirShip10ae4b0,
true for roles3/4. SupporterTyltyl skips that extra same-front stun; offenseKarl
takes it. Source actor stun at9f781e remains unconditional. Neither source
closure establishes event-time stun or the cause of earlier failed heals.

Native paused CB0602 corroboration: owner-qualified mask1/IsBGPaused8=false,
pending serial0/IsSkillReserve=false, pause140=1/armed=no. Actual paused DOWN
1001200→logical60,722 captured same fields. This is a paused negative control,
not live skill acceptance. Coordinated reduced observer startup0.176s,
contact→terminal6.388s, observer49324 exit0/contact0/empty stderr. First
synchronous input wait took60.337s; retained as host orchestration counterexample.
Changing contact to an independent child handle while draining JDWP stdout
removed that delay. Still too slow to treat as a cheap unrestricted live probe.

Opposite-front viewport remains unresolved. Recovered listener uses
GetFrontBound986638→actor+a28 component virtual54, CMTestIntersection78c9b4
against a separate global-derived viewport. Current M024 image branch7040b0
updates CMRelationRect+b4 from drawable64c and returns+dc. Existing Spine67c
body cache cannot substitute. Next recover exact viewport global9f7954/ADD
9f76b0, component/drawable owner and relation arithmetic; never call lazy bounds.
