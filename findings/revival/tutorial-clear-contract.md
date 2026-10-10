# Tutorial clear persistence and native tutorial identities

2026-10-03. Read-only native research with Capstone, existing network decompile,
original extracted library, and saved native test notes. No Ghidra, adb,
server/client changes or fresh runtime control.

## 1. Request and minimum acknowledgement

**[RECOVERED]** `CSRSyncTutorial::RequestClear` (`0xf9a0c4`) posts
**/tuto/Clear**. Its form map has seven fields:

```text
app_code, app_ver, market, pvid, otp, type, step
```

type and step are formatted with **to_string(unsigned int)** in the request
builder (`native-network-decomp.txt:10728-10741`); their native map keys are
unsigned32 enum values. The route literal is loaded at `0xf9a520`, type key at
`0xf9a340`, step at `0xf9a368`.

Successful acknowledgement must echo the requested pair in **ret_data**:

```json
{"result_code":1,"ret_data":{"type":8,"step":0}}
```

`ReqClearCB` (`0xf9ac40`) checks transport status and response result_code1
(`0xf9ac60..0xf9ac6c`), decrypts the body, indexes ret_data (`0xf9acdc`), reads
its type (`0xf9ad00`) and step (`0xf9ad46`) as scalar integers, and performs:

```text
00f9ad86 mov r0,this
00f9ad88 mov r1,parsedType
00f9ad8a movs r3,#3
00f9ad8c bl CSRSyncTutorial::SetState
```

Missing/non-numeric type or step defaults0. A generic mock success therefore
clears **FIRST0/step0**, not the guide that requested completion. An accepted
clear must persist the same pair before responding.

## 2. State and reload shape

`CSRSyncTutorial::Parse` (`0xf9b75c`) receives a tutorial **collection directly**
(the caller extracts tuto). Each row is:

```json
{"type":8,"step":0,"is_cleared":1}
```

The parser dereferences each row at `0xf9b802`, indexes type at `0xf9b80a`,
step at `0xf9b84c`, is_cleared at `0xf9b892`, and calls SetState at
`0xf9b8e2`. A truthy is_cleared maps to state3 (`0xf9b8ae`), false/missing
maps to state0 (`0xf9b8da`). Publish numeric0/1 rather than ambiguous strings.

GetState (`0xf9a956`) reads a nested map keyed by unsigned type and unsigned
step; missing either returns0 (`0xf9a9b6`). No step array or upper bound is
present in GetState/SetState. A nonnegative uint32 step validator is justified;
an invented max step5 is not. The named type table covers0..48.

**[RECOVERED / important correction] SetState is not monotonic.** Existing
step nodes directly overwrite their state at `0xf9abde`; false rows from a
later parse can turn previously completed3 back into0. Therefore merge
fixture gates and persisted account rows by exact (type,step), emit each once,
and never replace persisted completed truth with a stale false fixture row.
The old comment that SetState only raises state is incorrect.

RequestClear sees a current state3 and returns success callback1 without
network (`0xf9a136..0xf9a150`). Otherwise it sets state1 before submitting the
request (`native-network-decomp.txt:10654`). Thus state0 is uncompleted/missing,
state1 is at least used as pending, and state3 is acknowledged cleared. The
complete meaning of state2 remains unknown; many scene gates consider >1 done.

## 3. Safe repeat handling and optional side effects

Persist clear once under account identity and (type,step). Repeated requests
return the same pair without another mutation or reward. This matches the
native already-cleared short circuit and handles network retries. No native
idempotency nonce is constructed in this requester.

The callback has optional reward branches: achievement, card, item, deck, and
consume_result.item. achievement is null guarded (`0xf9acee`), card is null
guarded (`0xf9ad9e`), deck is null guarded (`0xf9b260`). Cards feed inventory
and tutorial-explore markers; item rewards include ref_id/added, and a deck
branch reads type plus inst_id_1..4 and calls SetDeckInfo at `0xf9b490`.
consume_result.item is forwarded to UseItem at `0xf9b222`, even when absent;
its item's semantics were not reconstructed here. **Do not fabricate rewards,
deck replacement, or item consumption for a pure completion acknowledgement.**
The original reward tables/condition identities are unknown. Verify a minimal
pair-only acknowledgement on the actual guide before claiming native usability.

## 4. Recovered TU_TYPE names, including gates outside the old sweep

`GetFlagStr` (`0xf9a9bc`) bounds-checks type<=48 and indexes a49-entry string
table. The table base is Ghidra `0x218e6d0` / ELF VA `0x217e6d0`. **ELF data
addresses require PT_LOAD mapping**, not raw `VA==file offset`: this ELF's
second load segment has VA0x210e550 and file offset0x210d550, a0x1000 gap.
Applying that mapping yields the following names:

```text
0 FIRST                    1 MISSION                 2 GACHA
3 BATTLE                   4 RAID                    5 SUPPLY
6 SHOP                     7 MAIL                    8 GYM
9 MISSION_ACHIEVE          10 GACHA_ACHIEVE           11 BATTLE_ACHIEVE
12 ABYSS_ACHIEVE           13 SUPPLY_ACHIEVE          14 SHOP_ACHIEVE
15 MAIL_ACHIEVE            16 GYM_ACHIEVE             17 HOTDEAL_ACHIEVE
18 ENTRUST                19 ENTRUST_ACHIEVE          20 GACHA_FIRST_ENTER
21 BATTLE_FIRST_ENTER      22 RAID_FIRST_ENTER        23 SHOP_FIRST_ENTER
24 GYM_FIRST_ENTER         25 MIRAGE                  26 MIRAGE_ACHIEVE
27 FISHING                 28 FISHING_ACHIEVE          29 EQUIP
30 EQUIP_ACHIEVE           31 AUTO_REMIND             32 BUY_STARTER_PACKAGE
33 GUILD                   34 SKIN                    35 EPISODE
36 LINEARQUEST             37 EXPLORE                 38 GVG
39 GVG_DEF                 40 GVG_ATK                 41 CHAT_ACHIEVE
42 CHAR2_SET               43 AUTOX2                  44 REWARD_ACHIEVE
45 FIRST_STAGE             46 NULL                    47 EXPLORE_ACHIEVE
48 ALL_FINISHED
```

The current sweep of types0..7 does not clear training8/16/24 or many later
guides. This is not a recommendation to automatically clear every named type:
honor the actual guide completion and persist its requested pair. A known enum
name is not proof that a player completed its guide.

## 5. n_01_03 and "Tap anywhere to attack!"

**[RECOVERED]** `CSRStaticData::GetStageID(TU_TYPE)` (`0xf42820`) uses a49-way
Thumb branch table. Its n_01_03 arm is `0xf4286a`, literal at `0x1d8ed76`.
That arm is selected by **types2,10,17** (GACHA, GACHA_ACHIEVE,
HOTDEAL_ACHIEVE). FIRST_STAGE45 instead selects arm `0xf42860`, n_01_01.
Therefore an automatic n_01_03 start is **not proof of FIRST_STAGE45**.

The saved native control `analysis/testing/revival-004.md` observed automatic
n_01_03 after stage2, showing "Tap anywhere to attack!". That text has a
recovered localization key `아무 곳이나 탭하여 적을 공격하세요` in
all-tables.json. It is shared gameplay/tutorial wording and alone cannot name
the active TU_TYPE.

The result-win pipeline `CSRMStage::PopUpResultWin` (`0xb3635c`) checks
GetState(2,0), GetState(8,0), GetState(37,0) at `0xb3655c`, `0xb365a6`,
`0xb365f0`; it has tutorial result paths when gates are incomplete. This
establishes that post-victory tutorial decisions consult GACHA/GYM/EXPLORE,
but the exact active guide step that produced the recorded n_01_03 start
remains **[UNKNOWN]**. Do not preemptively clear45 from this screen name.

A fresh /tuto/Clear request gives the actual completed type/step. Persisting it
and returning the same pair is stronger than trying to infer completion from
the combat instruction. Record guide interaction and subsequent wire events,
then relaunch and verify the cleared guide does not repeat.

## 6. Account merge and verification

Merge persisted account completed pairs into login/lobby tutorial arrays and
into launcher data when that account can be identified. Preserve existing
boot-gate fixture policy, but deduplicate rows and prioritize actual completed
pairs. Keep type/step numeric and is_cleared1. Do not reset tutorial state to
the static sweep on relaunch.

Test distinct type8/step0 and type24/step0, replay the same pair, reload from
disk and confirm exactly one completed row for each. Native control must
complete the active guide, receive the echoed pair, relaunch and confirm no
repeat without awarding another reward. This lane performed no live control.
