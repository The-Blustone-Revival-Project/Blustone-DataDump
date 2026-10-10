# Free Fuel activity unlocks after stage8 achievement progress

2026-10-04. Original read-only ELF/RTTI/literal/Capstone evidence. No source/AGENTS/adb/Ghidra/client changes. **No actual stage8 achievement has yet been earned in this control.** Tester is progressing normally through stages5→8; don't report this unlock as live verified yet.

## Recovered condition

Village's initialization callback hides the activity footer when **GetStageAchieveCnt("n_01_08")==0**. Claimable Fuel reference/instance data do not bypass this campaign gate. The recovered predicate is any nonzero stage8 achievement count, not necessarily three stars or a tutorial state.

Actual callback instructions (Ghidra coordinates):

```text
0xdbb818  DataMgr.get
0xdbb81c  GetPlayData
0xdbb820  r1 = 44  // TU_TYPE REWARD_ACHIEVE
0xdbb822  GetStageAchieveCnt(TU_TYPE) at0x84e87c
0xdbb826  CBZ result ->0xdbb874
0xdbb874  r0 = captured Village
0xdbb876  DisableBadges at0xda1b20
```

DisableBadges loads **PA_ACTIVE** (LDR0xda1c14/slot0xda1f14/addPC0xda1c16), finds that actual panel through framed view lookup at0xda1c24, and calls **SetVisible(false)**0xda1c3c. It hides the parent panel, including BT_ACTIVE's rendering/hit subtree.

## Correct Thumb entry and exact callback owner

The containing anonymous callback's correct **Ghidra Thumb entry is0xdbb740**. ELF function pointer is **0xdab741**, including Thumb bit. Entry begins push r4/r5/r6/r7/lr and further callee saves, allocates0x20 stack; captured Village is closure+4 at0xdbb758. Mid-call0xdbb876 is not a valid new function entry; creating it or interpreting ARM mode produced bad decompilation and is discarded.

Exact hidden vtable **ELF0x216b32c**, addresspoint+8, has invoke slot **vtable+0x20 = ELF0xdab741**. The literal pair slot0xdbb720/addPC0xdbb714 resolves this vtable. Vtable+4 points to RTTI **ELF0x216b358**, whose actual type-name bytes are:

```text
NSt6__ndk110__function6__funcIZN15CSRPopUpVillage6OnInitEvE3$_1NS_9allocatorIS3_EEFvvEEE
```

This proves **CSRPopUpVillage::OnInit's $_1 callback**. OnInit constructs/registers the same function object: slot0xd9faa4/addPC0xd9f946 resolves ELF0x216b32c, captured this stored0xd9f948, vtable+8 stored0xd9f94c, registration into Village eventpool+0x58 at0xd9f954.

## End-to-end44→stage8 mapping

`CSRPlayData::GetStageAchieveCnt(TU_TYPE)`0x84e87c calls StaticData.GetStageID at0x84e8a4 with the supplied enum, then **GetStageAchieveCnt(string)**0xb6ce4c at0x84e8ac. It does not call Tutorial.GetState.

StaticData.GetStageID0xf42820 uses TBB at0xf4282a, tablebase **0xf4282e**. Byte **index44** selects **0xf428f8**. That arm loads string from literal slot **0xf42924**, matched addPC **0xf428fa**, resolving **0x1d8f4a5 = "n_01_08"**. Enum44 is independently named **REWARD_ACHIEVE** in `tutorial-clear-contract.md`. The enum label does not turn this string-based campaign counter into a cleared tutorial flag.

Thus the recovered chain is44→n_01_08→native stage achievement count→panel hiding. Sending tuto[{type:44,is_cleared:1}] does not establish this counter, and no fabricated server star grant is proposed.

## Nonzero branch and restoration limit

With nonzero count, the callback skips DisableBadges and schedules a0.3-second OnceImpl at0xdbb862. Nested closure vtable **ELF0x216b364**, RTTI0x216b390, invoke pointer **ELF0xdab9fb** (Ghidra Thumb entry0xdbb9fa), names the nested OnInit $_1 lambda and calls **PopUpBanners0xda8d30** at0xdbba1e. It does not itself show PA_ACTIVE.

Fresh selected EN/KO SR_MAIN/MAIN_ICON XML initializes PA_ACTIVE visible=true beneath screen-sized PA_ICON_AREA. Normal reconstruction of Village view after genuine stage8 progress therefore avoids the initialization hide. Explicitly restoring a previously hidden already-existing view is not proved; native return/reinitialization should be observed rather than forcing a byte.

OnReset0xda48e2 and minute-boundary CheckActiveNoti0xda8b60 use HasRewardActivity to set **MN_NC**, the notification child. These positive badge checks **do not show PA_ACTIVE itself**. Parent measured Fuel refcount1/instance1/AP10/status1; that establishes ready model data, not campaign permission or actual visible footer.

## What this disproves and what remains unverified

Earlier EN absence as the cause was disproved by recovered KO fallback. Header AP popup was measured as **ShopFuel** primary ELFvptr0x2166678, a separate BT_FUEL route; it did not test SupplyFuel's PA_CELL0 binding. Ready reference/instance1 disproves an empty Supply model in that native control. Proposed JSON alias, layout alias, missing PA_CELL0, or icon resource cause remains **unproved** and should not be used to bypass this legitimate gate.

After ordinary stage8 win earns actual achievement(s), return normally to Village. Observe PA_ACTIVE/BT_ACTIVE hidden bytes, press actual lower-right **BT_ACTIVE/ACT_RW_ICON**, and confirm **SupplyFuel primary vptr B+0x2167d04** before inspecting cells. CMUpdatable hiddenbyte+0x271 is inverted:0 visible,1 hidden. If a stable guarded tree remains hidden after nonzero stage8 counter, examine initialization/reload timing and ancestor state; don't label unlock verified from server data alone.

Cold-start reading order: this report; `supply-fuel-entry-actions.md`; `village-ui-live-root.md`; `supply-fuel-live-ui-reader.md`; `supply-village-active-visibility.md`. Parent decompile should use Thumbentry0xdbb740 and nested0xdbb9fa, preserving the original library. No AGENTS update is made before a live milestone.
