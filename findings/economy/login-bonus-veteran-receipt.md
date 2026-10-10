# Calendar claim: captured Veteran20 and absolute VIP state

2026-10-07. Read-only retained login-bonus decomp/keys, original ELF and current
source. No Ghidra/device/source/account actions, grants or reward retuning.

## Empty20 is a native captured display reward

RequestLoginReward **Gf49410** builds SRREWARD_INFO at stack+40: base setup
f4949a and zero stores f494a8..f494c8. It unconditionally loads **20** at
**f49624** and stores it in the struct's **first field atf49626**. This value
comes from the original client, not a ret_data.item row or backend quantity.

Its callback **Gf4e43c** parses ret_data through ParseLoginBonusRewardf4a438
and Achieve.ParseLobbyEnter, then copies **captured closure+30 SRREWARD_INFO**
to the UI callback (retained callback lines33..42). Parsing additional arbitrary
reward rows is not the way to remove this captured display value.

**CSRItemThumb.GetItemThumbList Gafa584** synthesizes exact identity **VIP1**
(LDRafa5d0/ADDafa5d2), loads the SRREWARD_INFO first field at**afa5da**,
and calls AddThumbListafa420 at**afa5e0**. Shared SyncUser's vip_exp branch
also uses the first SRREWARD_INFO field for the VIP delta. Thus the observed
EMPTY icon20 has a concrete **VIP1 display-reference dependency**. It is not
evidence for an arbitrary inventory item20 reward. Actual gold100 remains the
separate RP1 display field.

## Exact claim parser and omitted-VIP behavior

Callback extracts fullJSON.ret_data, which ParseLoginBonusReward receives.
That parser extracts **ret_data.reward**, then **reward.user** atADDf4a622.
Optional item grants are reward.item[] with inst_id/ref_id/added. Wallet parent
for calendar parsing is reward.user; gold uses **gold.cur**. Its IAP grammar
is **iap.paid{prev,cur}** and **iap.free{prev,cur}**, not the unrelated Shop
scalar names or shared SyncUser pair names.

Calendar VIP grammar is **ret_data.reward.user.vip_exp{cur}**
(vip_exp ADDf4aaee/f4ab06, cur ADDf4ab0e). Original **f4aaf4/f4aaf6**
checks the vip_exp child and skips to f4ab5a ifnull. Omission therefore does
**not directly zero VIP EXP**. When supplied, cur converts to uint32 and writes
absolute **PlayData+150 atf4ab56**. There is no inferred automatic+20 native
wallet increment in this parser. A prev field can document a transaction but
is not consumed by this VIP branch.

Current claimLoginBonus returns only reward.user.gold.cur and instance/neutral
achievement fields. Current reload profile/lobby emits vip_exp0, with no durable
VIP EXP field in the game model. This is a state/receipt completeness seam:
the original captured20 display must be reconciled with authoritative absolute
VIP state and reload, rather than silently changing gold or crediting a normal
VIP1 inventory stack. The native constant establishes a20 Veteran reward
expectation for this requester; historical already-earned VIP totals remain
unrecovered and must not be guessed from one label transition.

## Veteran3→1: remaining UI proof

A possible explanation is reward UI calculating its prior level from current
VIP EXP minus the captured20, while currentEXP remains0, causing unsigned
underflow. This is **a hypothesis**, not a recovered assignment in the calendar
parser. It cannot justify asserting the actual account lost Veteran EXP.
Precise parent decompile targets for that transition:
**CSRPopUpGetReward.SetData(CREATE_INFO) Gc5239c**, wrapper
**SetData(SRREWARD_INFO) Gc59cdc**, and GetUserVIPLevel **Gb6cc2c**;
GetItemThumbList **Gafa584** closes icon identity. Source-backed VIP1 thumbnail
mapping and native successful claim/reload remain separate validations.

No extra gold/AP/item award, historical VIP backfill or source fix was performed
in this lane. A narrowly recovered VIP absolute receipt plus persistent earned
state and a display-only reference is the concrete next implementation seam;
the root owns its policy, migration and tests.
