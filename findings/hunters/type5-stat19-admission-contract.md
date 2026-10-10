# Kind 5 / stat 19 native admission and debuff immunity

2026-10-09. Read-only research against retained original native exports. No Ghidra, ADB, native invocation, runtime, server, ownership or balance change in this lane. G addresses include the 0x10000 analysis image bias.

The selected ordinary Tyltyl slot 4 is loaded as kind 5 / target 4 / stat 19 / reference type 2 / reference stat 0 / coefficient 0.1 / duration 4 seconds / interval 0, followed by a separate positive HP/DEF result. This is proven by `analysis/testing/ordinary-skill-reference-001/native.txt`, not a combat application. Its rank requirement is 4; the current owned rank 1 does not establish eligibility or trigger execution.

## Source admission chain

`ghidra-effect-kind-admission.txt` retains CSRGameBase::ApplySkill G9e6dd4, target selection, and the recipient CanRunning gate before CSRGameActor::AddBuf. Exact selection/type-4 trigger admission upstream remains separate from these functions. Do not infer a newly restored ordinary slot activated merely because its reference row is present.

Single AddBuf G981f48 allocates/binds a CSRGameActorBuffInfo, copies the result through Load G99e64c and sends it to the recipient component's AddBuff G99e78c. Load asserts nonzero effect kind and target and rejects stat 0 or 3; stat 19 satisfies that check. It copies the normalized result and initializes elapsed F0=0, remaining F4=duration24, applied count FC=0. The list overload G97db14 merely forwards each BUF_DATA.

AddBuff G99e78c checks kind 2 through the aura immunity queries, kind 4 through IsImmuneDBf, and kind 3 through IsImmuneBf. **Kind 5 has no corresponding rejection branch.** It reaches list insertion/count increment, active recipient100/component104 assignment, and ApplyBuff(1). The special stat15 recheck does not apply to stat19. This establishes a valid downstream path for kind5 without relabeling it kind3. It does not prove this particular slot generated a BUF_DATA, selected a live target or passed its upstream conditional trigger.

## Stat 19 applies an integer immunity counter

ApplyBuff G99eb3c computes RefData*coefficient*application multiplier, records that float at F8, and skips Apply when the result is zero. No negative-HP attack/defense quotient applies to stat19. RefData selection and exact rawInteger30 production are not closed by this report.

Apply G99c450 dispatches stat19 (0x13) to AddBuffImmuneDbf G99b870. With no nested AC-list entries (countB4==0), it uses selector 0 and the signed **raw integer30**, rather than rounding coefficient1c or F8*100. For a positive applied float, it sends abs(rawInteger30); for a nonpositive applied float, it sends -abs(rawInteger30), subject to ordinary signed overflow behavior not characterized here. If rawInteger30 is positive and the applied float is positive, it first calls purge G99faf0 with selector0. A zero raw integer yields no positive counter even if F8 is nonzero. Therefore parsed base0.1 alone is insufficient to claim an immunity counter10 or any live immunity.

For a nonempty nested AC-list, each node supplies its selector at node10 (inline result stat8) and signed raw integer at node38 (inline result30), applying the same sign and purge rules. The selected native reference snapshot reports nested count0; no nested application has been observed.

`ghidra-debuff-immunity-kind5.txt` closes AddBuffImmuneDbf G99b870 and IsImmuneDBf G99babe. The counter map is inside the typed ACTOR_STATE at actor8bc: minimumB8/rootBC/countC0, node allocation18/key10/signed counter14. An existing key adds the supplied integer to its counter. A missing key allocates a node initialized to that integer and increments tree count; the insertion count increment is distinct from the stored counter. No clamp, automatic erase at zero or boolean-only storage is shown.

IsImmuneDBf returns false unconditionally for requested stat30 (0x1e). Otherwise a positive counter at key0 supplies global immunity; failing that, a positive counter at the exact requested stat supplies immunity. Zero/negative counters are not immune. Thus stat19's empty-list selector0 can block later **kind4** admission across requested stats except30, provided its counter becomes positive. It does not prove protection from kind2 aura debuffs, direct damage, every negative effect or all game statuses; those use different paths.

## Purge and lifetime

Purge G99faf0 walks the same recipient BuffInfo list and selects **kind4 only**, excluding stat30. Selector0 matches all those eligible rows; a nonzero selector matches that exact stat. For selected rows it un-applies existing applied counts, clears active100, emits removal event, removes the node and decrements list count. This can remove previously admitted debuffs when a positive raw counter is applied; it does not purge kind2 aura debuffs or kind5 itself.

Refresh G99eeb8 consumes recipient active deltaTime22c, delay18, elapsedF0, remainingF4 and interval2c. With selected interval0 it decreases remaining without periodic ApplyBuff calls. Deactivate G99f006 and OnUpdate G99f400 call UnapplyBuff for non-kind1 records with positive applied count, then clear active100; expiry removes the node. Four native seconds of recipient active time is not four host wall-clock seconds while paused.

UnapplyBuff G99ea54 uses stored F8 and the removal count, negates the product, calls Apply and clears F8. The decompiler omitted the sign inversion, but `ghidra-buff-unapply-instructions.txt` proves it: G99ea74 converts r1 to float; ea7c multiplies F8; ea84 EORs the float bits with 0x80000000 into r2; ea8a calls Apply G99c450. Thus a positive application with positive raw integer has an inverse negative counter operation on removal. Exact baseline restoration still depends on stacking, number of applications and concurrent counter changes, and has not been observed live.

## Verification boundary and next evidence

Source closes kind5 downstream admission, stat19 counter recipient/key semantics, kind4 purge/exclusion and timer/removal path. Live reference parsing closes kind5/stat19/base0.1/duration4; root's new `analysis/testing/type5-immunity-001/reference.txt` additionally directly prints rawInteger30=10 with both nested counts0. This is a native reference payload, not a recipient counter. No live eligible Tyltyl trigger, recipient counter delta, successful rejection of a later debuff, purge or expiration is claimed. Ordinary adaptation of this Episode row remains local policy; final ordinary skill balance is unrecovered.

A useful next observation would correlate an eligible original source's conditional result and recipient BuffInfo with the typed immunity map key0/value, taking before/after snapshots while normally paused. Record rawInteger30 separately from normalized coefficient and F8. Do not call native getters that insert map entries or mutate expiration; do not raise owned ranks to manufacture admission.
