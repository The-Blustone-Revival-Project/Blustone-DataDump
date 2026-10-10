# Village free-fuel icon: panel hiding versus reward badge

2026-10-04. Read-only original Capstone/literals and selected UI XML. Parent's live fuel model is refcount1/instance1/status1; no UI visibility was measured by this task. No adb/Ghidra/source/client changes.

## Actual panel hider

**CSRPopUpVillage::DisableBadges0xda1b20 explicitly hides PA_ACTIVE itself.** Matched LDR0xda1c14, slot0xda1f14, addPC0xda1c16 resolves PA_ACTIVE0x1d87cca. It constructs the name, calls framed FindCast0x93cf88 at0xda1c24, reads resulting drawable at0xda1c36, and if nonnull calls **SetVisible(false)** at0xda1c3c (r1=0 at0xda1c3a). This removes the activity icon's rendering/hit subtree, independently of whether a claimable fuel model exists.

A direct-BL offline call scan found **0xdbb876** calling DisableBadges. This is inside an anonymous/stripped callback, not a named standalone method in the retained original symbol table. The callback also schedules a CMTaskStream OnceImpl at0xdbb862 and PopWaiting(300)0xdbb88a. The surrounding condition choosing DisableBadges versus scheduling needs parent decompilation; do not label it a particular tutorial or blindly clear flags.

**Exact next parent operation:** GetFunctionContaining(0xdbb876), dump that complete function with resolved PC-relative strings and record its registered caller/closure owner. Start with the0xdbb700..0xdbb8ac neighborhood if needed. Also dump DisableBadges0xda1b20..0xda1f20 and OnReset containing0xda48e2. These target actual panel state rather than the unrelated NPC CheckSupplyNoti.

## Reward checks change MN_NC, not PA_ACTIVE visibility

At the end of Village **OnReset0xda1f20**,0xda48e2 calls Supply.get and0xda48e6 calls HasRewardActivity. Only if it returns1 (0xda48ea..ec), code finds PA_ACTIVE0xda48fe, then finds its child **MN_NC**0xda4914, and calls **SetVisible(true) on MN_NC**0xda491c. Matched second literal slot0xda4c38/addPC0xda4906 resolves MN_NC. This code does **not** show the PA_ACTIVE panel itself.

**CheckActiveNoti0xda8b60** first computes local time modulo60 and skips unless the remainder is0 at0xda8bce..d0. It finds PA_ACTIVE then MN_NC (slots0xda8d28/0xda8d2c, actual matched adds0xda8bd6/0xda8bec), calls HasRewardActivity0xda8c04 and passes that result to **MN_NC.SetVisible**0xda8c0c. Its direct caller0xda7b5a is in OnRefresh. A claimable row therefore enables the notification child, not every ancestor; a minute boundary does not repair a hidden parent.

Another anonymous callback containing **0xdc10ac** tests HasRewardActivity at0xdc10dc. If false, it looks up PA_ACTIVE then MN_NC and hides **MN_NC** at0xdc1112; if reward exists it returns without that hide. This likewise cannot restore PA_ACTIVE hidden earlier.

Thus status1/model presence and a positive HasRewardActivity prove reward eligibility only. The earlier inference that positive eligibility guarantees a visible clickable footer icon is too strong. **DisableBadges is a concrete panel-hide path**, but its occurrence in the actual healthy Village is not yet measured.

## Safe bounded UI discriminator

CMUpdatable::SetVisible0x7882a0 reads/stores **object+0x271**, using an **inverted hidden flag**: inputtrue1 maps to byte0; inputfalse0 maps to byte1. Evidence CLZ/shift0x7882ac..b4 and STRB0x7882c8. The existing reader's object bound through0x270 must include0x271 when observing this one byte. Do not write it.

Under an independently guarded actual Village view/root and the161 CMUpdatable-derived primary guards, read name metadata and hidden flag for **PA_ICON_AREA, PA_ACTIVE, BT_ACTIVE, MN_NC** and their ancestors. Unknown/secondary pointers or unstable tree means inconclusive, not absence. Report:

- PA_ACTIVE exists, hidden1 => actual panel hide, next attribute its caller/condition.
- PA_ACTIVE visible0 but ancestor hidden1 => ancestor gating; resolve the ancestor setter.
- PA_ACTIVE and BT_ACTIVE visible0, valid drawable tree => wrong tap coordinate/hit geometry or icon asset rendering remains; don't mutate flags.
- PA_ACTIVE absent => actual view/XML binding issue; positive Supply model does not resolve it.

Selected EN/SR_MAIN/MAIN_ICON XML has PA_ACTIVE directly beneath **PA_ICON_AREA**, a screen-sized fixed panel with no explicit hidden attribute. PA_ACTIVE itself has visible=t and position(-128,-20), alignright,bottom,size90x90; BT_ACTIVE is centered90x90, pressed/release, using ACT_RW_ICON. There are no additional static hidden ancestors between these nodes in that record. Runtime ancestor transforms and screen coordinate conversion remain unmeasured; the one unsuccessful810,1835 tap is not proof of hidden state or hit bounds.

## Asset question remains separate

ACT_RW_ICON is the exact XML sprite reference; this task did not establish its actual runtime sprite/texture resolution or inspect its package pixels. Missing icon art would not by itself prove BT_ACTIVE's panel hidden/hit-disabled. Inspect the guarded node tree/hidden flag first, then bounded drawable/resource state if visible. No icon-resource replacement, JSON aliases, tutorial sweep, locale alias, or UI forcing is justified by this evidence.

Earlier exact action attribution remains valid: Village BT_ACTIVE hash0x18b8c16a constructs SupplyFuel0xdad340, Init0xdad34e, Reload0xdad352. Header BT_FUEL constructs separate ShopFuel. Confirm actual SupplyFuel vptr B+0x2167d04 before claiming the free fuel scene was tested.

## Exact anonymous callback attribution and actual campaign gate

Later offline recovery pins the correct **Thumb entry0xdbb740**, containing the call0xdbb876. It starts with `push {r4,r5,r6,r7,lr}` at0xdbb740, then saves r8/sb/sl, allocates0x20 stack, and obtains captured Village pointer closure+4 at0xdbb758. **Do not decompile a new function at mid-call0xdbb876 or in ARM mode.** Original ELF callable address is0xdab741 (Thumb bit), equivalent Ghidra code entry0xdbb740.

The closure's hidden function vtable is **ELF0x216b32c**, address point+8. Exact literal slot0xdbb720/addPC0xdbb714 yields that vtable; its invoke slot vtable+0x20 stores ELF0xdab741. Typeinfo pointer vtable+4 is ELF0x216b358; its actual type-name string is:

```text
NSt6__ndk110__function6__funcIZN15CSRPopUpVillage6OnInitEvE3$_1NS_9allocatorIS3_EEFvvEEE
```

This proves **CSRPopUpVillage::OnInit's $_1 callback**, not a speculative nearest-symbol owner. OnInit registers exactly this closure: literal slot0xd9faa4/addPC0xd9f946 resolves the same ELF0x216b32c; it stores captured this at0xd9f948, adds vtable+8 at0xd9f94a and registers in Village eventpool+0x58 at0xd9f954 (`CMEventPool<>::operator<<`).

Actual hide condition is **campaign achievement progress**, not a missing claimable Fuel row and not Tutorial.GetState:

```text
0xdbb818 DataMgr.get
0xdbb81c GetPlayData
0xdbb820 r1 = 44 (TU_TYPE REWARD_ACHIEVE)
0xdbb822 PlayData.GetStageAchieveCnt(TU_TYPE) (0x84e87c)
0xdbb826 if count==0 ->0xdbb874
0xdbb876 Village.DisableBadges
```

GetStageAchieveCnt(TU_TYPE)0x84e87c calls StaticData.GetStageID at0x84e8a4, then **GetStageAchieveCnt(string)**0xb6ce4c at0x84e8ac. The type enum44 name REWARD_ACHIEVE is independently recovered in `tutorial-clear-contract.md`. The Static.GetStageID TBB at0xf4282a uses tablebase0xf4282e: byte index44 selects **0xf428f8**. Its matched LDR slot0xf42924/addPC0xf428fa resolves **n_01_08** at0x1d8f4a5. Therefore zero native stage8 achievement count causes the footer panel to be hidden on this Village initialization callback.

If the count is nonzero, this callback **does not hide the panel**; instead0xdbb862 schedules a0.3-second OnceImpl. Its hidden vtable ELF0x216b364/typeinfo0x216b390 names the nested OnInit $_1 callback lambda; invoke slot+0x20 stores ELF0xdab9fb (Ghidra Thumbentry0xdbb9fa). That nested callback calls **Village.PopUpBanners0xda8d30** at0xdbba1e. It does not itself SetVisible(true) on PA_ACTIVE. A freshly loaded XML starts PA_ACTIVE visible=true and the nonzero stage8 path leaves it alone; exact restoration of a previously hidden already-existing view remains unproved.

This provides an intended progression hypothesis with exact writer/condition: **earn actual stage8 achievement(s), then return through normal Village initialization**, rather than clear type44 tutorial flags or fabricate stage8 rewards. Count>0, not necessarily three stars, is the recovered predicate. Parent's pending live hidden-byte probe still determines whether this callback explains the observed icon in the actual session.

Correct parent decompile targets:0xdbb740..0xdbb924 **in Thumb context**, nested callback0xdbb9fa..0xdbba88, and OnInit registration0xd9f942..0xd9f958; the original f42820 TU-type jump-table mapping and84e87c wrapper independently corroborate stage8. No UI forcing, tutorial sweep, server star grant or APK change is proposed.
