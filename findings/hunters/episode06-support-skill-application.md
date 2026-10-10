# E06 support application: fixed Karl versus owned Tyltyl

2026-10-09. Supplemental read-only original STAT/COMBAT exports, current skill publication and existing native reports. No runtime/Ghidra/source/save actions or balancing.

**Karl is an original fixed Episode actor, not the owned healer.** CB0602 left slot5 uses `CB0601_012_1`, camp0/resC012/role1 Offense/rank4 with flags `[1,1,0,1,0]`. `episode06-stat-duplicate-contract.md` proves first duplicate STAT row143 wins for a fresh original index: HP1150/ATK750/DEF550/regen30; skill1 cooldown5000/cost3/crit_chance50. Its effect is Activate1 -> Enemy1 -> HP1, sourceAtk reference1, base_number-2000 (coefficient **-20**, before native defense/attribute processing). No up_number is exported; do not apply owned Tyltyl's per-level fixture increment. Original skill2 supplies self-target stat5 buff40/4000ms; skill4 self-target stat7 buff1.0/4000ms. Their numeric rows remain original; this supplemental review does not reassign stat5/7 enum meanings.

**Tyltyl1000005 is the ordinary owned support.** Current ref004/rank1/skill1LV2 is reconstructed fixture Activate1 -> FrontAlly4 -> HP1, sourceDEF reference3/type1, coefficient `(95+5*2)/100=1.05`, cost4. Slots2..5 have no effects. This is positive healing, not Karl's negative attack or an original recovered Tyltyl magnitude. Use actual source combat GetDef, which can include buffs; do not substitute target Karl's DEF550 as the healing reference merely because Karl receives the heal.

Existing native effect review establishes positive HP1 becomes negative DAMAGE_INFO, then HP subtraction restores health and caps at destination maxHP. Thus an accepted heal of a full-HP ally can show zero net HP; a heavily damaged front should restore at most its deficit, not display an unbounded 1.05*DEF gain. Actual processing/rounding, concurrent damage and passive recovery can alter a screenshot delta. Pair one cost4 debit/accepted effect with target HP before/after and finish/resume; HP rise alone is insufficient.

FrontAlly4 identifies a friendly frontline target relative to the source's camp, rather than Tyltyl herself or a named owned ref003. The current fixture does not request AllAlly or fixed Karl. **No Karl exchange is necessary to heal whichever camp0 actor is already front.** To heal Karl specifically, Karl must be the live front target when native target resolution selects that front. Exact reserve-versus-application selection timing is not closed by the existing reports; do not race exchange against a pending heal and assume the earlier target stays bound.

Role4 Tyltyl uses eligible rear/airship input and skips the role1/2 automatic-front-exchange branch documented in `active-skill-gesture-rage.md`. Activating her support should not itself swap her into the frontline. Role1 Karl's normal skill may exchange him with the current front first; `battle-skill-plan-validation.md` already records Karl skill transition, native front Karl/rear Nene afterward and subsequent combat. Keep the support heal and Karl skill/exchange as distinct native actions so attribution is possible.

Regeneration is a separate confound: selected Karl has original hp_regen30, projected ordinary Tyltyl37 and Nene48. Those source values alone do not establish actual regeneration per wall-clock second or battle state. Do not claim every upward HP transition is Tyltyl's heal, or that Karl's listed30 means +30HP/s. Observe real source/target HP and cost/animation evidence; no rewrite of regeneration is justified.

Actionable test distinction: an accepted Tyltyl heal costs4 and should benefit the current damaged friendly front without changing support role; a Karl skill costs3 and can automatically exchange the original fixed Offense actor into front before applying his original damaging result. A missed fixed-point press, full-HP destination, target changed during exchange, or regeneration are different explanations and need separate evidence.

## Corrected role-dependent admission predicate, next diagnostic

2026-10-10 correction: the earlier supporter-only explanation below reversed
the branch. Root's original Thumb export corroborates CBNZ G9f78ac→9f78ba:
IsSupporter=true skips the extra same-camp front-stun check. IsSupporter is
SRCanUseSkillAirShip(GetRole), returning true for roles3/4. Karl/offense checks
the matched same-camp front; Tyltyl/support does not. The clicked source's own
stun check remains unconditional. See ghidra-episode-supporter-stun-thumb-asm.txt
and ghidra-episode-supporter-predicate.txt. No original game behavior was changed.

Supplement after root's heal002: reported owned Tyltyl enabled/visible, SP4.410961 and opacity factors1 plus a point inside its reconstructed bound still produced no observed cost4 debit. Root's Karl activation works. These are root observations, not actions by this review.

Listener G9f7604 first finds an opposite-camp input actor whose GetFrontBound intersects the viewport and a same-camp actor in the bounded input list. G9f7816..1c rejects game state13c bit **0x4**; G9f781e..32 rejects source IsFrontStun or missing camp matches. Then **G9f78a6..b8** performs the additional same-camp front-stun check only when IsSupporter is false. Karl role1 takes it; Tyltyl role4 skips it.

`IsFrontStun` G97e6c4 tailcalls `IsStun` G99b168. Exact getter: actor+8bc is state pointer; **signed int state+94 >0** means stunned. A bright support icon does not prove its source is unstunned or that all other gates pass. Same-camp frontline stun alone does not explain Tyltyl's failed activation through this branch. No event-time cause of the reported failure has been established.

Next read-only diagnostic should retain the actual matched same-camp input actor's serial/camp/HP and buff+94, source Tyltyl buff+94, game state13c bit4, and the opposite-camp GetFrontBound/viewport intersection. Do not hardcode the previously saved Nene pointer or infer stun from appearance; selection may change after death/exchange. Guard owners and repeated fields as with the existing native reader. No stun/cooldown/enable field should be written or cleared. If those predicates pass, continue to distinguish actual dispatched byte255, current reservation/background pause8 and nonempty returned effects rather than attributing failure to coordinates alone.

## Buff state type and ownership for a bounded reader

Original symbols plus read-only original Thumb establish actor+8bc/+8c0 as a shared pair for **CSRGameActorBaseDraw::ACTOR_STATE**, not CSRGameActorBuff and not an inline polymorphic actor. Base constructor G999c9c zeroes the pair (G999dda..dde). Load G99a438 calls typed CMPoolMgr.get G99a5e0 and CMPool<ACTOR_STATE>::Alloc G99a7e0, then moves the returned pair into actor+8bc/+8c0 at G99a4c6..d6, releasing the previous control if present. Base destructor G97c848 releases control+8c0 at G97c850..884.

Pool Alloc's fresh branch allocates **0xdc** bytes at G99a816..81c; it zeroes the first16 bytes rather than installing a vptr, and zeroes 90..9f (including stun94) at G99a88e..892. Recycled states follow the typed pool path and its callback; do not require fresh-zero contents. This is a plain field-bearing state object with string/container members, not an arbitrary readable pointer.

The returned shared pointer uses custom pool deleter constructor **G99be7c**: separate control allocation0x18, control+c=raw ACTOR_STATE pointer, control+10/+14=weak pool pair. Original ELF dynsym `_ZTV...__shared_ptr_pointer<ACTOR_STATE*,CMPool<ACTOR_STATE>::Alloc lambda,...>` is0x2149d3c; its primary address point is **B+0x2149d44**. Do not mistake raw state for control+c inline allocation: **u32(control+c)==state**, not state==control+c. On_zero_shared G99c050 loads that stored pointer and invokes the pool deleter G99bef0 with control+10; eventual weak release is separate. No ACTOR_STATE primary vptr check belongs on the object itself.

Minimum diagnostic qualification: already validated current Episode actor owner/camp/serial; repeated nonzero pair8bc/8c0; exact control primary B+2149d44; nonexpired signed control+4>=0; stored pointer control+c equal state; mapped readable state range0xdc; repeated pair and counter bytes. Read signed int state+94, with predicate >0. CopyActorStat G99ac80 reads default+8b4 and buff+8bc to calculate numeric values into a supplied state; it is not a distinct allocation-owner path. If another control branch appears, refuse it until independently recovered rather than accepting any mapped pointer. No observer changes were made by this lane.
