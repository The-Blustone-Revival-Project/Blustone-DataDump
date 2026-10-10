# Aura recipient identity, ownership and refresh

2026-10-09. Read-only existing original exports/symbols and bounded original Thumb. No Ghidra, ADB, observer/server changes, grants or retune. G addresses include10000 image bias; primary vptr constants below are original ELF offsets relative to loaded library baseB.

## Direct correlation is the generated aura serial

Source AddAura registration is documented in `skill-passive-registration-contract.md`: actor vector9cc/9d0/9d4 contains AURA stride0xe8, each row carrying generated64-bit serial at **+e0/+e4**. Skill type, inventory inst_id and vector position are not this identity.

Recipient **AddAuraEffect G98241c** obtains its CSRGameActorBuff at actor+9b0 and walks the buff list sentinel component+98/first+9c. At **G98246c..47a**, BuffInfo.GetSerial G99f04c returns **info+e0/+e4** and is compared with source aura+e0/+e4. Thus the most direct read-only correlation is equality of these full64-bit values, across a presently qualified source aura record and recipient buff node. Counting source auras or matching target_stat alone cannot show delivery.

New-recipient branch allocates a BuffInfo through its typed pool at G9826da..6e2, binds source/recipient/context at G9826ee and calls **Load(AURA,sourceSerial) G99ee9c** at G982702. Load's exact fields: **info+e0/e4 aura serial**, **info+e8/ec source actor serial**; original generic Load G99e64c copies BUF_DATA and initializes clockF0=0, remainingF4=duration24, countFC=0. **Bind G99e5ce** stores raw source actor pointer+108, recipient+10c and context actor+110. Those are raw bound references, not independently owning shared pairs.

## Qualified recipient list path

The concrete recipient component path is **actor+9b0/+9b4** -> `CSRGameActorBuff`. Original make_shared **G989b88** allocates0xb8 and constructs object atcontrol+10. Object primary **B+2149d6c**, emplace control primary **B+2149608**, nonexpired signed control+4>=0, object==control+10. These constants come from original ELF vtable symbols2149d64/2149600; they are not guessed adjacent actor-state types. This component is distinct from the numeric ACTOR_STATE at actor+8bc.

Buff list layout is confirmed by AddAuraEffect and AddBuff G99e78c/OnUpdate G99f400: sentinel **component+98**, first **+9c**, count **+a0**, node next+4, BuffInfo object/control **node+8/+c**. AddBuff allocates node0x10, stores this shared pair, updates list links/count, then activates the admitted object. Use finite list bounds/count match, cycle/null rejection, repeated list/node links and qualified actor owner; do not walk an unbounded list from source counts.

BuffInfo is a **plain pooled0x118 object**, not an inline polymorphic component. Alloc **G9822a0** fresh branch allocates0x118 at G9822d6..de and initializes data/timer/binding fields. Its custom pool-deleter shared constructor **G98cae4** allocates a separate control0x18, stores raw info atcontrol+c and weak pool pair atcontrol+10/+14. Exact control primary **B+21499b4** (symbol21499ac). Require stored pointer u32(control+c)==info, nonexpired control and readable info0x118, with repeated pair/control/type/raw fields; do not require info==control+c or an info primary vptr.

## Recharge does not create another stack

On existing serial match **G98281c** calls **Recharge G99ee94**. Exact implementation is two field operations: load duration **+24** and store it into remaining **+f4**. It does **not** reset elapsedF0, countFC, coefficient, source serial or add another list node. Refresh therefore normally extends this matched aura's lifetime rather than unconditionally stacking new buffs on every frame.

There is an additional context-change branch: when a supplied context exists and the reference selector atinfo+10 equals3, AddAuraEffect compares bound status identities and may delete/rebind/re-add the existing serial at G9828ae..8f2, followed by UpdateStat. Thus matching serial alone does not guarantee immutable context or that every refresh only changesF4. Repeat bindings as well as timer/value fields.

BuffInfo **Activate G99f02e** increments countFC, sets active target/base-draw pointer **+100**, owning Buff component reference **+104**, and calls ApplyBuff(1). **Deactivate G99f006** un-applies non-Activate effects when countFC>=1, decreases the count and clears active pointer100. List presence, active100 and countFC are stronger evidence of admission than source counts, but still do not prove a particular final numeric stat changed: immunity, selector/reference semantics and effect-specific application matter.

## Source death, exchange and natural expiration

UpdateAura **G9e871c** source CanRunning gate at G9e8ad8 uses **G99ac38**, whose exact implementation tests actorHP+8b0 !=0 (not merely a named liveness boolean). Source HP0 skips all its aura refresh work. For **target_type1** it additionally requires source IsRunning at G9e8b22; other target types do not take this extra branch. IsRunning G97d888 rejects IsUndead G99abdc (typed state+88 bit1) and requires actor byte+a50==1; it does not itself implement the separate HP0 death test. Accordingly exchange can stop a target1 source's refresh while other target selectors may continue from a live rear source, subject to actual source enumeration and FindSkillTargetActors. Do not claim all auras disappear when a Hunter moves rear.

Recipient CanRunning is checked at G9e8b68 before AddAuraEffect. BuffInfo.Refresh **G99eeb8** operates on active recipient100's deltaTime22c; it consumes delay18, elapsedF0, remainingF4 and interval2c/countFC. There is no sourceHP or source IsRunning read in this Refresh body. **Recharge alone leaves periodic tick progress intact**. A stopped source therefore need not synchronously erase a recipient record; without further Recharge, a finite-duration buff can expire through recipient active time.

Component.OnUpdate **G99f400** calls Refresh on each node (G99f438), checks max(remainingF4,0)==0, un-applies expired non-Activate effects and clears active100, removes their serial bookkeeping and list node/count, and releases the shared object. Activate-type effects have additional target-stat retention/removal handling; do not generalize the finite passive/buff rule to every one-shot effect. Paused recipient time need not correspond to wall-clock expiration. OnDetach G99f500 clears component's actor binding+a4; full source destruction/removal propagation outside these functions remains unclosed.

## Minimal useful native snapshot

For a fixed proven source and recipient actor in the current game:

1. Qualify source owner and repeat actual aura vector bounds/selected row bytes. Record source actor serial plus aura serial/type/target_stat/coefficient/duration/interval.
2. Qualify recipient Buff component and bounded list as above. Find exact aura serial and corroborate info sourceSerialE8/EC, bound source108 and recipient10c against those currently qualified actors. Never dereference raw bindings merely because they are mapped.
3. Record info active100, component104, elapsedF0, remainingF4, appliedCountFC, lastAppliedValueF8 and context110, with repeated owner/list/field checks. Also retain recipient typed numeric ACTOR_STATE before/after for the actual expected stat/counter change.
4. Report serial-matched admitted/refreshed record separately from measured application. Only an independently observed recipient stat/HP/counter delta, tied to that identity and excluding regeneration/concurrent effects, closes the stronger result claim.

No observer extension or live aura success is claimed here. This supplies a concrete owner-qualified recipient path for a future diagnostic, instead of assuming generated source records imply applied team effects.

## Recipient reader review and stat15 counter correlation

Root's subsequent exports `ghidra-aura-recipient-owner.txt`, `ghidra-aura-info-pool-refresh.txt` and `ghidra-aura-apply-value.txt` corroborate the typed owner/fields above. Source-only review of new `episodeRecipientBuffSnapshot` found no blocking owner/offset issue: list sentinel98 storeslast,9c first; previous0/next4/value8/controlc; empty and bounded64 counts checked; component emplace and Info pool qualifications correct; whole0x118 bytes and links/control/pair/count repeated; raw source/recipient/context pointers printed but not dereferenced. Application is explicitly labeled unproved.

**F8 is a float last applied value**, not an integer flag. ApplyBuff's new root export stores computed fVar10 (or0 on its nonapplication branch) at+f8 immediately before calling Apply. TimerF0/F4 and appliedCountFC are distinct fields.

Root reports the live read completed exit0/emptystderr: Bibi recipient seriala has exactly one matched aura1e1f, bound source/recipient self, active pointerself, appliedCount1, remaining0.5, coefficient/lastValue-0.03; all other nine recipient lists are empty and aura1e20 is not found. Those observations prove one identity-correlated admitted record, not team-wide delivery or isolated stat delta. Root's typed ACTOR_STATE snapshot already shows signedStun94=-3.

Original **Apply G99c450** reads target_stat at+8, subtracts1 and dispatches via TBH G99c488/tableG99c48c. For **stat15 (index14)** its exact branch is **G99c69c**. It reads a **signed integer at BuffInfo+30**, selects its sign using the applied float's sign and that raw integer, then calls **AddBuffStun G99b624 at G99c6d8**. AddBuffStun's implementation is actor+8bc -> state, signed counter+94 += supplied int. IsStun G99b168 returns only counter94>0; negative counts are not “negative HP” or a stunned actor.

Crucially, this branch is **not simply `lastValueF8*100`**. The raw integer30 is retained separately from normalized float coefficient1c/F8. If raw30=-3 and applied value is negative, the branch supplies-3; an existing zero counter would become-3 and IsStun remainsfalse. The observed matched buff plus state-3 is consistent with this mechanism, but an exact raw30 read from the already owner-qualified0x118 object is the direct next corroboration. Do not infer that integer solely by multiplying a rounded-0.03 display, and do not call the observed state an isolated before/after delta without its baseline.

No live reads or observer edits were performed by this research lane; root owns and validates that diagnostic.
