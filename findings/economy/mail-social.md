# Mail, Friends and Social — recovered subsystem notes

**Author:** research subagent (read-only). **Date:** 2026-10-02.
**Sources:** `analysis/native-all-strings.tsv` (printable native string table,
cited by offset), `analysis/native-evidence.tsv`, `server-ts/src/catalog.ts`,
`server-ts/src/game-routes.ts` (cited by line), `server-ts/src/openapi.ts`.

**Search method:** `python tools/native-grep.py -p <term> ...` (one streaming pass
over both tables) plus a small `python -c` offset-window dump of the strings
table. No Ghidra, no adb, no writes outside this file.

Evidence labels used throughout:

- **recovered** — the literal appears verbatim in a native table.
- **inferred** — derived from recovered names/shapes/signatures, not literal.
- **unknown** — nothing found; what was searched is listed.

---

## 1. Routes in the subsystem

### 1a. `/message/*` — the in-game mailbox (recovered)

The mail subsystem is **not** under `/mail`; it is `/message`. There is **no
`/mail/...` HTTP route at all** (searched `-p "/mail"` and dumped every string in
the table starting with `/`: the only `/mail` hits are UI/resource keys such as
`SR_MAIL/MAIL_RECEIVE`, `UI_MAIlBOX_U`, `BT_MAIL`, `MAIL_SLOT`).

| Path | Offset | Owning native code |
|---|---|---|
| `/message/GetReceivedList` | `0x1d6a743` | `CPVMsg::ReqGetReceivedList` (`_ZN6CPVMsg18ReqGetReceivedListEyjyy`) |
| `/message/GetSentList` | `0x1d6a75c` | `CPVMsg::ReqGetSentList` (`_ZN6CPVMsg14ReqGetSentListEyjyy`) |
| `/message/Read` | `0x1d6a77d` | `CPVMsg::ReqRead` (`_ZN6CPVMsg7ReqReadEy`) |
| `/message/Archive` | `0x1d6a78b` | `CPVMsg::ReqArchive` (`_ZN6CPVMsg10ReqArchiveEy`) |
| `/message/TakeAttachment` | `0x1d6a7a7` | `CPVMsg::ReqTakeAttachment` (`_ZN6CPVMsg17ReqTakeAttachmentEy`) |
| `/message/Send` | `0x1d6a7f9` | `CPVMsg::ReqSend` (`_ZN6CPVMsg7ReqSendEjPKcS1_j`) |
| `/message/RemoveReceived` | `0x1d6a807` | `CPVMsg::ReqRemoveReceived` (`_ZN6CPVMsg17ReqRemoveReceivedEPKc`) |
| `/message/RemoveSent` | `0x1d6a81f` | `CPVMsg::ReqRemoveSent` (`_ZN6CPVMsg13ReqRemoveSentEPKc`) |
| `/message/GetUnreadCount` | `0x1d6a833` | `CPVMsg::ReqGetTotalUnreadCount` (`_ZN6CPVMsg22ReqGetTotalUnreadCountEh`) |

All ten are grouped contiguously in `.rodata` at `0x1d6a743..0x1d6a848`, i.e. they
were emitted by one translation unit — `PV2/PVMsg.cpp` (the file-name literal for
that region is not adjacent, but `CPVMsg`'s symbol block is at `0x1606xx..0x1618xx`).

**confidence: high** (routes), **medium** (the PVMsg.cpp attribution — inferred
from contiguous layout + symbol adjacency, the file-name string is not adjacent).

There are also `CPVMsg` operations with **no literal path next to them**, which
means the path is built or lives elsewhere:
`CPVMsg::ReqClearSentList` (`0x1612f43`-block), `CPVMsg::ReqClearReceivedList`,
`CPVMsg::ProcessClearSentComplete`, `CPVMsg::ProcessClearComplete`,
`CPVMsg::ProcessCommonGetListComplete`, `CPVMsg::ProcessTakeAttachmentComplete`,
`CPVMsg::ProcessGetTotalUnreadCountComplete`. **Likely** `/message/ClearSent`,
`/message/ClearReceived` — **unknown, not recovered.** They may reuse
`/message/RemoveSent` / `/message/RemoveReceived` with a sentinel id, or take a
command enum instead of a path. Next step in §6.

### 1b. `/relation/*` — friends, blocks, likes, recommendations (recovered)

All 23 paths are contiguous at `0x1d6af43..0x1d6b4fa`, emitted by
`PV2/PVRelation.cpp` (`CPVRelation` symbols at `0x173b1c..0x17550a`).

| Path | Offset | Callback symbol (recovered) |
|---|---|---|
| `/relation/GetList` | `0x1d6af43` | `CPVRelation::ReqFriendListCB` |
| `/relation/Block` | `0x1d6b01d` | `ReqBlockCB` |
| `/relation/Unblock` | `0x1d6b048` | `ReqUnBlockCB` |
| `/relation/BlockList` | `0x1d6b067` | `ReqBlockListCB` |
| `/relation/RequestUserReport` | `0x1d6b091` | `ReqUserReportCB` |
| `/relation/FriendRequest` | `0x1d6b0bd` | `ReqFriendCB` |
| `/relation/FriendReqAccept` | `0x1d6b120` | `ReqAcceptFriendCB` |
| `/relation/FriendReqCancel` | `0x1d6b17c` | `ReqCancelFriendListCB` |
| `/relation/FriendReqReject` | `0x1d6b1bb` | `ReqRejectFriendListCB` |
| `/relation/Unfriend` | `0x1d6b1eb` | `ReqUnfriendListCB` |
| `/relation/GetFriendReceivedCount` | `0x1d6b210` | `ReqReceivedFriendCountCB` |
| `/relation/GetSuggestedFriendList` | `0x1d6b27a` | `ReqSuggestedListCB` |
| `/relation/FriendSearch` | `0x1d6b2c7` | `ReqSearchFriendCB` |
| `/relation/SendFriendInviteMsg` | `0x1d6b2f0` | `ReqSendInvitationCB` |
| `/relation/GetRecommendRewardRefList` | `0x1d6b322` | `ReqRecommendRewardRefCB` |
| `/relation/RequestRecommend` | `0x1d6b35e` | `ReqRecommendCB` |
| `/relation/GetRecommendInfo` | `0x1d6b388` | `ReqRecommendInfoCB` |
| `/relation/GetTargetUserInfo` | `0x1d6b3d5` | `ReqUserInfoCB` |
| `/relation/GetTargetUserInfoWithAI` | `0x1d6b3ff` | `ReqUserInfoIncludeAICB` |
| `/relation/GetLikeCnt` | `0x1d6b438` | `ReqLikeCntCB` |
| `/relation/ToggleLike` | `0x1d6b45a` | `ReqToggleLikeCB` |
| `/relation/RequestInvite` | `0x1d6b47f` | `ReqInviteCB` |
| `/relation/RequestAcceptInvitation` | `0x1d6b4a7` | `ReqAcceptInvitationCB` |
| `/relation/GetInvitationCnt` | `0x1d6b4df` | `ReqInvitationCntCB` |

**confidence: high.** Every path has a matching `…CB` completion callback in the
symbol table, and the two orderings agree.

### 1c. Adjacent social routes outside `/relation` (recovered)

| Path | Offset | Owner |
|---|---|---|
| `/friend/received` | `0x1d880fa` | SNS invite webview handler (see `PV_SNS_INVITE_*` errors) |
| `/webview/sns_invite/app` | `0x1d80b60` | SNS invite webview |
| `/world/GetFriendMissionRecord` | `0x1d7b40c` | `CSRPlayData::FRIEND_MISSION_RECORD` |
| `/world/GetFriendlyBattleInfo` | `0x1d8fa2c` | social battle |
| `/arena/GetFriendRankList` | `0x1d8f955` | arena social |
| `/mirage/GetFriendInfo` | `0x1d72fab` | `CSRExploreMirageInfo::RequestFriend` / `ParseFriendInfo` |
| `/guild/GetRecommendations` | `0x1d78dc2` | guild-side recommend (distinct from `/relation/GetRecommendRewardRefList`) |
| `/guild/GetChattingLog` | `0x1d78d1f` | guild chat history |
| `/world/ReportCombatAbusing` | `0x1d78348` | combat-abuse report |
| `/webview/...` `/RELATION_STORY/` | `0x1d93ee3` | UI resource prefix for relation-story dialogs, **not** a route |

`/guild/*` and `/world/*` overlap with the guild/economy research agents; only
the friend/social-facing ones are listed here.

**confidence: high** for the paths, **medium** for the ownership claims (offset
adjacency only).

### 1d. What is in the catalog vs. what exists natively

`server-ts/src/catalog.ts` builds its endpoint list by scanning the same
`native-all-strings.tsv` (`discoverEndpoints`) and filtering on a
`servicePrefixes` allow-list (line 7-13). Both `message` and `relation` and
`friend` are in that allow-list, so all of the above are already registered
routes. `/webview/…` and `/RELATION_STORY/` are not in the allow-list for the
first (`webview` **is** in the list; `RELATION_STORY` is not a route).

**Honest negative:** no `/mail/*`, `/chat/*`, `/social/*`, `/sns/*` HTTP route
exists in the table. Searched patterns: `/mail`, `/friend`, `/relation`, `/msg`,
`Msg/`, plus a full dump of every `/`-prefixed string (1360 of them).

---

## 2. Native types and classes (recovered, demangled)

### Platform/transport layer (`CPV*` — PV2 SDK, platform-agnostic)

```
CPVMsg                 0x1606xx-0x1618xx   singleton; all /message/* transport
CPVRelation            0x173b1c-0x17550a   singleton; all /relation/* transport
CPVAccount             0x13b27d-0x13bd50   login / SNS / bound-mail address
CPVChatClient          0x1670f5            websocket chat client
CPVChatRequestMessage  0x1481df-0x148eaa   encrypt() / to_json(); has a
                                             `uitagSeq` field and a conversion
                                             operator to std::string
CPVChatClientImpl      0x16710e            Poll() / Send(vector<unsigned>)
CPVCDN2 / PVC          —                   (not this subsystem)
```

Wire structs (recovered names, with RTTI typeinfo symbols present so these are
genuine class types, not typedefs):

```
PV_MSG_RESULT        shared_ptr used in every CSRSyncMail::Req* callback
PV_MSG_INSTANCE      CTAD from (const json&, PV_MSG_INSTANCE::TYPE)
                       -> CTAD from (const CSRGuild::MSG&)
PV_MSG_ATTACHMENT
PV_MSG_ATTACHMENT_ITEM
PV_MSG_COMMAND       passed to ProcessClearComplete / ProcessCommonComplete /
                     ProcessCommonGetListComplete
PV_FRIEND_INFO       RTTI at 0x20869d / 0x2087b7
PV_TARGET_INFO       RTTI at 0x2086b2 / 0x2087cc ; copy ctor from `const _`
```

`PV_FRIEND_INFO` and `PV_TARGET_INFO` are distinct types: friend list rows and
"user profile you are looking at" rows are **not** the same shape.

### Game layer (`CSR*`)

```
CSRSyncMail      0x2888a7-0x288a12 + ReqRemoveAll at 0x35fa0e
                 ReqEnter(cb, unsigned, unsigned, unsigned)
                 ReqRead(cb, unsigned)
                 ReqSend(cb, unsigned, char const*)
                 ReqRemove(cb, list<unsigned>)
                 ReqRemoveAll(cb)
                 ReqUnreadRecvedCnt(cb)
CSRMail          0x288c3e-0x2890a7  singleton
                 DATA (CTAD from PV_MSG_INSTANCE, and from CSRGuild::MSG)
                 GetMsgList(unsigned,unsigned) / GetMsgList()
                 IsLastPage(unsigned,unsigned)
                 SortByReceivedTime(DATA const&, DATA const&)
                 FindMsg(CMHashID const&) / ReadMsg(CMHashID const&)
                 GetUnreadCount() const
                 RequestList(unsigned, unsigned, char, cb)
                 RequestRead(CMHashID const&, vector<DATA>, cb)
                 RequestSend(unsigned, std::string const&, cb)
                 RequestAppend(unsigned, cb)
                 RequestRemove(list<CMHashID>, cb)
                 RequestUnreadMsg(cb)
                 MailMessageTypeToText(DATA const&) static
                 MailMessageTypeToText(CSRGuild::MSG::NOTI_TYPE) static
CSRMail::DATA::TYPE          nested enum
CSRTableMail    0x381514-0x3819ed  the list view; _DATA(const CSRMail::DATA&, TYPE)
CSRCellMailPost / CSRCellMailGuild  0x13b22fb / 0x13b2232
                 Init(const CSRMail::DATA&, bool); factory(...) same signature
CSRPopUpMailRead       0x2dd3af   OnRemoveMail(), OnButtonClick, OnInit
CSRPopUpMailReadGuild  0x2dd693   + CreateRegistCancelPopup()
CSRPopUpMailSend       0x2dd87c   ChangeState(STATE), ResultCB(void*, string&)
CSRPopUpMailWrite      0x2de69b   AddSlot(const SRTARGET_USER&), _DATA struct
CSRPopUpFriend         0x2b4731   IsRecommender(), RecommenderCnt(),
                                 SetRecommender(int,int,vector<RECOMMENDER_DATA>),
                                 RecommendFriend(string const&),
                                 RecommendFriendRewardInfo(),
                                 RecommendFriendRewardItemList(int,int),
                                 SetRecommenderMessage(int)
CSRFriendMgr      0x204f67
                 RequestFriendList(PV_FRIEND_INFO::TYPE, cb<int,vector<unsigned>>)
                 RequestSearch(string const&, cb<int,vector<unsigned>,int,int,list<PV_FRIEND_INFO>,int,int>)
                 RequestSuggest(cb<int,vector<unsigned>,int,int,list<PV_FRIEND_INFO>,int,int>)
CSRExploreMirageInfo    RequestFriend(cb) / ParseFriendInfo(json)   0x1f58b6
CSRUserPool      0x204c28   Update(const PV_TARGET_INFO&, shared_ptr<SRTARGET_USER>)
CSRRefData::HELPER_INFO::FRIEND   0x1ba7f4  static ref-data friend list
CSRRefData::GetVirtualFriendList  0x1ec381
CSRPlayData::FRIEND_MISSION_RECORD 0x1bdc82  std::map<unsigned, ...>
CSRRefData11HELPER_INFO6FRIEND     map<basic_string, FRIEND>
```

`CMRelationRect` (0xee1bc+) is **layout, not social** — it is a UI rect helper.
`CMRelationRect` is a false friend for this subsystem; worth noting so a future
agent does not chase it.

`RECOMMENDER_DATA` and `SRTARGET_USER` are recovered as type names but their
member layouts are not in the string table (no keys recovered for them).

**confidence: high** for every name above (verbatim mangled symbol demangled by
me); **medium** for the CSRFriendMgr callback signature decoding, which is read
off the `std::function` template arguments.

---

## 3. JSON key vocabulary

All keys below are **recovered**: they appear as standalone literals in
`native-all-strings.tsv` in the `0x1d6a743..0x1d6b513` window, which is the
string pool of `PV2/PVMsg.cpp` + `PV2/PVRelation.cpp` and is therefore exactly
the set of keys those two parsers read (plus their request builders). Keys are
listed in table order so the grouping mirrors the source layout.

### 3a. Mail / message keys

| Key | Offset | Attributed to | Notes |
|---|---|---|---|
| `target_list` | `0x1d6a771` | `ReqGetSentList` / `ReqGetReceivedList` request | vector of receiver pvid |
| `message_id` | `0x1d6a79c` | `/message/Read`, `/message/Archive`, `/message/RemoveReceived`, `/message/RemoveSent` | **unsigned** — `ReqRead(unsigned)`, `ReqRemove(list<unsigned>)`, and `CSRMail` keys by `CMHashID` |
| `receiver_pvid` | `0x1d6a7bf` | `/message/Send` request | |
| `sender_pvid` | `0x1d6a7cd` | `/message/Send` request | |
| `content` | `0x1d6a7d9` | `/message/Send` request | the mail body |
| `item_code` | `0x1d6a7e1` | `/message/Send` request | singular; mirrors `PV_MSG_ATTACHMENT_ITEM` |
| `item_quantity` | `0x1d6a7eb` | `/message/Send` request | |
| `sender_nickname` | `0x1d6a84b` | `PV_MSG_INSTANCE` parse | response |
| `receiver_nickname` | `0x1d6a85b` | `PV_MSG_INSTANCE` parse | response |
| `from_admin` | `0x1d6a86d` | `PV_MSG_INSTANCE` parse | GM mail flag |
| `attachment` | `0x1d6a878` | `PV_MSG_INSTANCE` parse | container for `PV_MSG_ATTACHMENT` |
| `description` | `0x1d6a883` | `PV_MSG_INSTANCE` parse | mail text |
| `free_iap_quantity` | `0x1d6a88f` | `PV_MSG_INSTANCE` parse | attachment iap value |
| `item_list` | `0x1d6a8a1` | `PV_MSG_INSTANCE` parse | array of `{code, quantity}` |
| `code` | `0x1d6a8ab` | `item_list[]` element | |
| `quantity` | `0x1d6a8b0` | `item_list[]` element | |
| `is_archived` | `0x1d6a8b9` | `PV_MSG_INSTANCE` parse | |
| `is_read` | `0x1d6a8c5` | `PV_MSG_INSTANCE` parse | the "read" flag |
| `is_attachment_taken` | `0x1d6a8cd` | `PV_MSG_INSTANCE` parse | |
| `created_datetime` | `0x1d6a8e1` | `PV_MSG_INSTANCE` parse | `SortByReceivedTime` sorts on this |
| `unread_count` | `0x1d6a8f2` | `/message/GetUnreadCount` response | |
| `list` | `0x1d6a8ff` | `ProcessCommonGetListComplete` | the array wrapper for Get{Received,Sent}List |
| `content_result` | `0x1d6a904` | mail list response | **the one genuinely surprising key** — see §5 |

**confidence: high** for presence; **medium** for the precise request-vs-response
split of each key (attribution is by adjacency to the nearest path literal, which
is how this pool is laid out, and is consistent across all 23 `/relation` paths).

### 3b. Friend / relation keys

| Key | Offset | Attributed to | Notes |
|---|---|---|---|
| `friend` | `0x1d6af95` | `GetList` response | **container key**, see §5 |
| `candidate` | `0x1d6af9c` | `GetList` response | second container key |
| `request` | `0x1d6afa6` | `GetList` response | third container key |
| `received` | `0x1d6afae` | `GetList` response | fourth container key |
| `friend_id` | `0x1d6afb7` | `GetList` / `FriendReqCancel` | |
| `target_pvid` | `0x1d6afc1` | `FriendRequest`, `Block`, `Unblock`, `Unfriend`, `ToggleLike` | |
| `reg_utc` | `0x1d6aff2` | `PV_FRIEND_INFO` parse | friend-since |
| `tick` | `0x1d6affa` | `PV_FRIEND_INFO` parse | |
| `received_dtm` | `0x1d6afff` | `PV_FRIEND_INFO` parse | request-received time |
| `like_cnt` | `0x1d6b00c` | `PV_FRIEND_INFO` parse | |
| `is_like` | `0x1d6b015` | `PV_FRIEND_INFO` parse | |
| `target_nickname` | `0x1d6b02d` | `Block` / `Unblock` request | |
| `report` | `0x1d6b08a` | `RequestUserReport` request | |
| `target_friend_id` | `0x1d6b10f` | `FriendReqAccept` request | |
| `target_friend_id_list` | `0x1d6b166` | `FriendReqAccept` request | **note: the `_list` variant** |
| `friend_id_list` | `0x1d6b196` | `FriendReqCancel` / `FriendReqReject` request | **different name from the accept key** — a real asymmetry in the protocol |
| `target_nick_name` | `0x1d6b2b6` | `FriendSearch` request | **note: `nick_name`, not `nickname`** — differs from `target_nickname` on Block |
| `recommend_info` | `0x1d6b3b6` | `GetRecommendInfo` response | |
| `recommender_cnt` | `0x1d6b3c5` | `GetRecommendInfo` response | matches `CSRPopUpFriend::RecommenderCnt()` |
| `msg` | `0x1d6b4a3` | `RequestAcceptInvitation` request | invitation body |
| `is_ai` | `0x1d6b50d` | `GetTargetUserInfoWithAI` response | the "WithAI" variant adds an AI-player flag |
| `pvid` | `0x1d686aa` | account layer | `PVAccount.cpp`, `uiOrgPVID == uiPVID` |
| `nickname` | `0x1d69740` | account/popup layer | `PV2/PVDataMgr.cpp` region, not relation |
| `nick_name` | `0x1d68b22` | account layer | `ConfirmNickname` response |
| `message` | `0x1d69749` | push/local-noti layer | `PVPush.cpp` `!sTitle.empty() \|\| !sMsg.empty()` |

**confidence: high** for the key literals. **Important honesty note:** there is
**no** `title`, `body`, `sender`, `read`, `unread` bare key in this subsystem —
they are prefixed (`sender_pvid`, `is_read`, `unread_count`) or named differently
(`content`/`description`, not `body`). `title` exists only in the local-push
string (`sTitle`, `0x1d6af12`), not in the mail protocol.

### 3c. Error codes for this subsystem (recovered, 0x1d6c2a8-0x1d6c528)

```
PV_MSG_INVALID_SENDER / _INVALID_RECEIVER / _INVALID_APP_CODE / _INVALID_INSTANCE
PV_MSG_ALREADY_GET_ITEM / _INVALID_ITEM_CODE / _UPDATE_ITEM_FAIL
PV_MSG_TAKE_FROM_TARGET_APP / PV_MSG_BE_BLOCKED
PV_RELATION_ALREADY_REQUEST / _TARGET_ALREADY_REQUEST / _INVALID_REQUEST
PV_RELATION_ALREADY_CONFIRMED / _IS_NOT_CONFIRMED / _NEED_TO_LOGIN
PV_RELATION_ALREADY_RECOMMEND / _OVER_RECOMMEND_DUEDATE
PV_RELATION_LIKE_TO_COND / _CANNOT_LIKE_SELF
PV_RELATION_TARGET_OVER_MAX_CNT / _OVER_MAX_CNT
PV_RELATION_ALREADY_BLOCK / _OVER_BLOCK / _INVALID_BLOCK
PV_SNS_INVITE_LOADING_LIST_FAIL / _CANCEL / _FAIL
```

These are the strings behind the numeric `result_code`; the client prints
`PV ErrorCode %s(%d)` (0x1d6b6d1) and `Protocol Result Code : %d` (0x1d68e95).

**confidence: high.**

---

## 4. Mock-fallback backlog — which routes are NOT implemented

`server-ts/src/game-routes.ts` is 120 lines. Its named branches are lines
16-106; everything else falls through to the generic mock at lines 108-119,
which returns `{ mock: true, route, request_keys: [...] }` plus, for
`/relation/*`, `{ list: [], users: [] }` (line 118).

**Only two routes in this entire subsystem have a real handler:**

| Route | Handler | Line | Shape returned |
|---|---|---|---|
| `/relation/GetSuggestedFriendList` | `state.envelope([])` | 30 | bare empty array |
| `/relation/BlockList` | `state.envelope([])` | 105 | bare empty array |

Both are **empty-array stubs, not reconstructions** — they exist only to stop the
`mock: true` marker. `/relation/BlockList` as an empty array is consistent with
`CPVRelation::ReqBlockListCB`'s callback type
`function<void(int, map<unsigned, basic_string>&)>` (recovered from the mangled
symbol at `0x001742ba`) — but the stub sends `[]`, not a **map keyed by pvid**,
which is a shape mismatch that will bite the first real BlockList response.

### The backlog, in priority order

**Tier 0 — REORDERED BY WIRE EVIDENCE (§6b). These five are on the village boot
path and are called today, every session:**

1. **`/message/GetUnreadCount`** → `{ unread_count: 0 }`. One line. Feeds the
   village Mail badge via `CSRMail::GetUnreadCount()`. **Cheapest, highest-value
   fix in the subsystem.**
2. **`/relation/GetList`** → called with `{"type":"1"}` then `{"type":"3"}`.
   Needs the bucket container for each type (§5c/§6b.2). Currently mocked.
3. **`/relation/GetTargetUserInfo`** → sends `list`; needs a `PV_TARGET_INFO`
   row shape (§6b.4). Currently mocked.
4. `/relation/GetSuggestedFriendList` — has a stub, but the stub returns `[]`
   with no `start`/`length` paging contract. Partially wrong, not unmocked.
5. `/relation/BlockList` — has a stub, but the stub is a JSON array where the
   parser wants `map<pvid, nickname>`. **Actively wrong.**

**Tier 1 — mail list UI, 100% unmocked and never yet exercised (8 routes):**

6. `/message/GetReceivedList` 7. `/message/GetSentList` 8. `/message/Read`
9. `/message/Archive` 10. `/message/TakeAttachment` 11. `/message/Send`
12. `/message/RemoveReceived` 13. `/message/RemoveSent`
(plus the two unknown clear-list routes, §6.3 — **do not implement until
identified**, see §1a)

**Tier 2 — friend/relation, 21 of 23 falling through (GetList and
GetTargetUserInfo promoted to Tier 0 by §6b):**

14. `/relation/FriendRequest` 15. `/relation/FriendReqAccept`
16. `/relation/FriendReqCancel` 17. `/relation/FriendReqReject`
18. `/relation/Unfriend` 19. `/relation/GetFriendReceivedCount`
20. `/relation/FriendSearch` 21. `/relation/SendFriendInviteMsg`
22. `/relation/RequestInvite` 23. `/relation/RequestAcceptInvitation`
24. `/relation/GetInvitationCnt`
25. `/relation/Block` 26. `/relation/Unblock`
27. `/relation/RequestUserReport`
28. `/relation/GetTargetUserInfoWithAI` — never observed on the wire, **not on
    the exercised path**; lowest value in the tier.
29. `/relation/GetLikeCnt` 30. `/relation/ToggleLike`
31. `/relation/GetRecommendRewardRefList` 32. `/relation/RequestRecommend`
33. `/relation/GetRecommendInfo`

**Tier 3 — adjacent social, unmocked, never observed on the wire:**

34. `/mirage/GetFriendInfo` 35. `/world/GetFriendMissionRecord`
36. `/arena/GetFriendRankList` 37. `/world/GetFriendlyBattleInfo`
38. `/guild/GetRecommendations` 39. `/guild/GetChattingLog`
40. `/webview/sns_invite/app` 41. `/friend/received`

**confidence: high** for the mock-fallback status — direct read of
`game-routes.ts` lines 16-119, nothing else in the file mentions `message` or
`relation`. **confidence: high** for the boot-path membership in Tier 0 —
decrypted bodies in `server-ts/logs/server.stdout.log` lines 261-270, 423-425.

---

## 5. Response SHAPE evidence

### 5a. `/message/GetReceivedList` and `/message/GetSentList`

Recovered: `CPVMsg::ProcessCommonGetListComplete(request, response, json,
PV_MSG_COMMAND)` at `0x1614a0`, and `CSRMail::RequestList(unsigned,unsigned,char,cb)`
whose completion lambda is
`[](unsigned, shared_ptr<PV_MSG_RESULT>, list<CSRGuild::MSG>)`
(fully recovered in the mangled name at `0x01e26724`). So:

- the **top level** is an object with `ret_data` containing `list`
  (`list` at `0x1d6a8ff`, immediately before `content_result`);
- the **rows** are an array of objects parsed by
  `CPVMsg::ParseMsgInfo(const json&, PV_MSG_INSTANCE::TYPE)` (`0x00160d72`),
  which in turn feeds `CSRMail::DATA`'s converting constructor from
  `PV_MSG_INSTANCE`.

**Array, not object, for the rows — confidence: medium-high.** The row parser is
*named* `ParseMsgInfo` and is given a single json value; but I have **not**
decompiled it (Ghidra is owned by the parent), so whether it indexes an array
positionally or looks up by key is **unverified**. This is the exact same class
of bug that cost the project the `/reference/GetStage` and `/reference/GetCard`
incidents (see AGENTS.md §11): the array-vs-object choice must be read out of
`ParseMsgInfo`'s decompile, not guessed. **Do not ship a fixture until it is read.**

### 5b. `content_result` — the highest-risk unknown key

`content_result` at `0x1d6a904` sits *after* `list` and *before* the PVPurchase
string pool begins. Nothing in the recovered symbol table explains it. Two live
hypotheses:

- **(a)** it is the **name of the field that holds the message bodies**, i.e.
  `ret_data.list[]` is a list of ids and `ret_data.content_result` is a parallel
  array of contents. This would explain why `content` (`0x1d6a7d9`) exists as a
  *request* key for Send and why `description` also exists.
- **(b)** it belongs to `PVPurchase2.cpp` (whose pool starts at `0x1d6a95f`) and
  is simply the last message-pool string before it.

**confidence: low.** Distinguishing (a) from (b) is the single highest-value
open question for the mail subsystem and is cheap to answer (§6.1).

### 5c. `/relation/GetList`

Recovered from the string pool, in order (`0x1d6af95..0x1d6afae`):
`friend`, `candidate`, `request`, `received`, followed by the row keys
`friend_id`, `target_pvid`, `reg_utc`, `tick`, `received_dtm`, `like_cnt`,
`is_like`, then the log lines `PVID is NULL. (%llu)` and `ParseFriendInfo`.

Four container names appearing back-to-back immediately after the route literal
is strong evidence that `ret_data` is an **object with four array members**:
`friend[]`, `candidate[]`, `request[]`, `received[]` — one per bucket of the
friend state machine (confirmed friends / recommendable candidates / outbound
requests / inbound requests). `CPVRelation::ReqFriendListCB`'s recovered
signature is `function<void(int, list<PV_FRIEND_INFO>&)>`
(symbol `0x00174554`), i.e. the callback receives **one list per request**, which
is consistent with the client issuing `GetList` four times with different filter
args and receiving one bucket per call — which would make the four names a
**union of four separate responses**, not four members of one response.

- "object with four array members": **confidence: medium**
- "one bucket per call, four possible key names": **confidence: medium**
- Which one is right: **unknown.** Both readings are compatible with the string
  pool; only `CPVRelation::ReqFriendListCB`'s decompile settles it.

Note the parallel with `PV_FRIEND_INFO::TYPE` (an enum, recovered from
`RequestFriendList(PV_FRIEND_INFO::TYPE, cb)` at `0x001749fc` and
`CSRFriendMgr::RequestFriendList(PV_FRIEND_INFO::TYPE, cb)` at `0x00204f67`).
**The enum exists**, so the "one call per bucket" reading is the more likely
one — the client asks for a `TYPE` and gets that bucket. **confidence: medium.**

### 5d. `/relation/BlockList` — array vs map (a live bug)

`CPVRelation::ReqBlockListCB` is
`function<void(int, map<unsigned, basic_string>&)>` (symbol `0x001742ba`):
a `std::map<pvid, string>` — block list rows keyed by pvid with the blocked
nickname as the value. `RequestBlockList(vector<unsigned>&, cb)` at
`0x00174742`. The current stub at `game-routes.ts:105` returns `[]`.

**confidence: high** on the map; the stub is wrong and should be
`{ "<pvid>": "<nickname>" }`.

### 5e. `/relation/BlockList` reading array directly

AGENTS.md §6 records that `BlockList` was previously noted as a "parser that
consumes an array directly and iterates numerically". This contradicts 5d.
The recovered symbol is unambiguous (`map<unsigned, basic_string>`), so 5d
stands and the AGENTS.md note should be corrected. **Confidence: high** — a
`std::map` in the callback signature cannot be produced by numeric iteration
over an array.

### 5f. `/relation/GetTargetUserInfo` vs `…WithAI`

`GetTargetUserInfo` → `ReqUserInfoCB(int, list<PV_TARGET_INFO>&)`
(`0x001740c4`); `GetTargetUserInfoWithAI` → `ReqUserInfoIncludeAICB(int,
list<PV_TARGET_INFO>&)` (`0x00175144`), taking `vector<pair<unsigned,unsigned>>`
(`0x0017541e`). The `WithAI` variant adds `is_ai` per row (`0x1d6b50d`).
`CSRUserPool::Update(const PV_TARGET_INFO&, shared_ptr<SRTARGET_USER>)`
(`0x00204c28`) consumes it. `SRTARGET_USER` is the same type
`CSRPopUpMailWrite::AddSlot(const SRTARGET_USER&)` (`0x002de799`) takes —
**mail composition and friend lookups share one user-projection type.**
**confidence: high.**

---

## 6. Open questions, each with the exact next step

**6.1 What is `content_result`? (blocks mail list shape)**
Searched: `-p "content_result"`, the whole `0x1d6a800-0x1d6b000` pool window,
and every `PV_MSG*`/`CSRMail*` symbol. Next step: run
`analysis/ghidra-scripts/ResolvePcRelativeStrings.java` (the parent owns Ghidra;
it was used for `analysis/ghidra-setstage-exact.txt`) over
`CPVMsg::ProcessCommonGetListComplete` at `0x1614a0` and
`CPVMsg::ParseMsgInfo` at `0x160d72`. The answer decides whether `ret_data` is
`{list:[…], content_result:…}` or something else. Until then **do not build a
mail-list fixture.**

**6.2 ~~Is `/relation/GetList` one-bucket-per-call or four members of one
object?~~ ANSWERED: one bucket per call (§6b.2).**
**Residual question — what do `type=1` and `type=3` mean?**
Next step (cheap, no Ghidra): have the tester open the Friends screen; new
`type` values on the wire name their own buckets. Next step (definitive):
decompile `CPVRelation::ReqFriendListCB` (symbol `0x00174554`) and
`ParseFriendInfo` (`0x00174492`) with `ResolvePcRelativeStrings.java`, and read
`PV_FRIEND_INFO::TYPE`'s enumerators — they come out of the same decompile.
This is what tells the server which bucket name (`friend` / `candidate` /
`request` / `received`) to send for each `type`.

**6.3 What are the clear-list endpoints?**
`CPVMsg::ReqClearSentList` / `ReqClearReceivedList` exist as symbols
(`0x00161243`, `0x0016f6d`) but no `/message/Clear*` literal was found — I
searched `/msg`, `Msg/`, `Unread`, `ReqRemove`, and dumped all 1360 `/`-prefixed
strings. Next step: resolve the string operand inside `CPVMsg::ReqClearSentList`
(`0x0016f6d`) — it may be assembled at runtime or may reuse `/message/RemoveSent`
with a sentinel.

**6.4 What are the members of `PV_MSG_INSTANCE`, `PV_FRIEND_INFO`,
`PV_TARGET_INFO`, `RECOMMENDER_DATA` and `SRTARGET_USER`?**
Only their *names* are recoverable from the string/symbol tables; the layouts are
not. Next step: `RequestRecommendRewardRefCB` / `CSRPopUpFriend::
RecommendFriendRewardItemList(int,int)` give the reward-ref shape, and
`CSRMail::DATA`'s converting constructor `DATA::DATA(PV_MSG_INSTANCE const&)`
(`0x00288f16`) is the single best target: it copies every field and will
enumerate the whole mail row. Decompile that one constructor first.

**6.5 Is `CSRMail::MailMessageTypeToText` a client-side localisation hook?**
Two overloads exist: `(DATA const&)` (`0x0023b23f`-block, `0x00288ec7`) and
`(CSRGuild::MSG::NOTI_TYPE)` (`0x00288ec7`). If the client maps mail rows to
display text itself from a numeric type field, the server must supply that type
and **no** localised text. Next step: read the `CSRMail::DATA::TYPE` enum values
and check `CSRTableMail::GetTableViewItemType` (`0x00381650`) for a switch.

**6.6 Which social routes does the client actually call at village boot?**
**ANSWERED — see §6b.** Five routes, in order, on every boot:
`/relation/GetSuggestedFriendList`, `/relation/BlockList`, `/relation/GetList`
(type=1), `/message/GetUnreadCount`, `/relation/GetList` (type=3), plus
`/relation/GetTargetUserInfo` on demand. Remaining question, for the tester:
open the **Mail** and **Friends** screens and report which additional routes
appear (expect `/message/GetReceivedList` and `/relation/GetList` with
`type=2`/`type=4`).

**6.7 `/webview/sns_invite/app` and `/friend/received` are HTML, not JSON.**
`PV_SNS_INVITE_*` error codes exist. Next step: check whether the replica's
generic handler serves these; if the client WebView expects HTML, a JSON envelope
will render a blank page. Same class of problem as the already-fixed
`ad_unit_id_1` HTML handoff noted in AGENTS.md §13.

---

## 6b. WIRE EVIDENCE — the client actually calls this subsystem today

This supersedes the guesswork in §6.6. Decrypted request bodies were recovered
from `server-ts/logs/server.stdout.log` (lines 261-270, 423-425 etc.,
session `2026-10-02T11:15:36Z`), which logs decrypted `body_keys` and, under
`BLUSTONE_LOG_GAME_VALUES=1`, the game fields. Corroborated by
`server-ts/data/live-requests-state2.log` and `live-requests-skip.log`, which
show the **same request sequence repeating 5+ times across sessions on
2026-09-21** — this is not a one-off.

### 6b.1 The observed boot sequence (recovered)

Village boot fires exactly five routes from this subsystem, in this order:

```
1  POST /relation/GetSuggestedFriendList   body_keys=app_code,app_ver,length,market,otp,platform,pvid,start
                                          game-values {}            (has `start`/`length` -> PAGED)
2  POST /relation/BlockList                body_keys=app_code,app_ver,market,otp,pvid
                                          game-values {}
3  POST /relation/GetList                  body_keys=app_code,app_ver,market,otp,platform,pvid,type
                                          game-values {"type":"1"}
4  POST /message/GetUnreadCount            body_keys=app_code,app_ver,market,otp,pvid
                                          game-values {}
5  POST /relation/GetList                  game-values {"type":"3"}
6  POST /relation/GetTargetUserInfo        body_keys=app_code,app_ver,list,market,otp,platform,pvid
                                          game-values {}
```

`live-requests-state2.log` lines 315-325 show the same, interleaved with
`/fishing/*`, `/explore/GetRef`, `/gvg/GetRef`, `/guild/GetNotifications`,
`/mirage/GetInfo`, `/lobby/GetNotiInfo`, `/v2/purchase/ReqIAPRef`,
`/world/GetIapMainIcon`, `/shop/GetHotDealSummaryList` — i.e. **this is part of
the standard village/UI hydrate burst**, not a screen the tester has to open.
`/relation/GetTargetUserInfo` is also called standalone at `04:35:14` and
`05:11:35`, i.e. on demand when a profile is opened.

### 6b.2 `/relation/GetList` takes a `type` — and is called TWICE with different values

**This settles §5c in favour of the "one bucket per call" reading.**
`GetList {"type":"1"}` then `GetList {"type":"3"}` are two separate HTTP calls,
so the client is asking for bucket 1 then bucket 3 by numeric type. The four
container names in the string pool (`friend`, `candidate`, `request`, `received`)
are therefore the **names of the four possible bucket payloads**, selected by
`type` — not four members of one object.

This aligns exactly with the recovered signatures:
`CPVRelation::RequestFriendList(PV_FRIEND_INFO::TYPE, cb)` (`0x001749fc`) and
`CSRFriendMgr::RequestFriendList(PV_FRIEND_INFO::TYPE, cb)` (`0x00204f67`).

**confidence: high** — two distinct requests with two distinct `type` values are
in the log; the four-name interpretation is now the only consistent one.

The **numeric meaning of `type` 1 and 3 is still unknown**. From the string-pool
order (`friend`, `candidate`, `request`, `received`) a plausible mapping is
`1=friend, 2=candidate, 3=request, 4=received`, i.e. the client asks for the
confirmed-friend list and the outbound-request list on boot (which is exactly
what a friends screen needs to show two tabs). **That mapping is inferred, not
recovered — confidence: low.** Next step: read the `PV_FRIEND_INFO::TYPE`
enumerators out of `CPVRelation::RequestFriendList`'s decompile; or, cheaper,
have the tester open the Friends screen and watch whether `type=2`/`type=4`
appear.

Note: `type` arrives as a **JSON string** (`"1"`, `"3"`), not a number. The
replica must echo the same type or at least accept both; a numeric `1` may or may
not parse, and this is worth matching exactly since the value comes from a
`basic_string`-typed comparison in most of this SDK's parsers. **confidence:
medium** (observed in the log; the parser's acceptance of a number is untested).

### 6b.3 `/relation/GetSuggestedFriendList` is PAGED (`start` + `length`)

It is the only route in the subsystem whose request carries `start` and `length`
alongside the usual envelope keys. Those two names are the same ones
`CPVLauncher` uses for its own paging (`length`/`after`/`before` at
`0x1d6a72f`-`0x1d6a73c`). The current stub returns `[]`, which is
*shape-plausible* for page 0 but means the client can never advance past it.
**confidence: high** (the keys are in the decrypted body).

### 6b.4 `/relation/GetTargetUserInfo` sends `list`, not `target_pvid`

The request key is **`list`** — the generic list name, not the
`target_pvid`/`target_friend_id` vocabulary used by the mutation routes. The
signature `CPVRelation::RequestUserInfo(vector<unsigned>&, unsigned,
cb<int,list<PV_TARGET_INFO>>)` (`0x001746b7`) is a **vector of pvid**, so
`list` is almost certainly an array of pvid integers. `RequestUserInfo` takes a
second `unsigned` — **unknown what it is** (possibly a page index or an
`include_ai` flag; the `WithAI` variant at `0x0017541e` takes
`vector<pair<unsigned,unsigned>>` instead, which suggests the scalar is a
**companion/second id**, e.g. `list` of `[pvid, guild_id]` pairs).
**confidence: medium** for "array of pvid"; **low** for the second scalar.

Note the sibling route `/relation/GetTargetUserInfoWithAI` and the key `is_ai`
(`0x1d6b50d`) were never observed on the wire — only `GetTargetUserInfo` was.
**So the `WithAI` variant is not on the exercised path.**

### 6b.5 `/message/*` — exactly one route is exercised

Only `/message/GetUnreadCount` was ever observed. The mail-list, read, send and
remove routes (`GetReceivedList`, `GetSentList`, `Read`, `Archive`,
`TakeAttachment`, `Send`, `RemoveReceived`, `RemoveSent`) **never appear** in any
of the three trace files. That is consistent with the mail list screen never
being opened during the expedition runs — it does **not** mean the routes are
wrong.

Consequence for the backlog: **`/message/GetUnreadCount` is the one mail route
that matters for the current goal**, because it is on the village boot path. It
currently falls through to the mock and returns
`{mock:true, route, request_keys:[…]}`. If the client reads `unread_count`
(`0x1d6a8f2`) as an integer out of that it gets a type mismatch — the village
Mail badge (`CSRPopUpVillage::SetVisibleMailNotiBadge`, `0x002f4591`) is fed from
`CSRMail::GetUnreadCount()` (`0x00289084`). **This is the single cheapest,
highest-value fix in this entire subsystem**: `{ unread_count: 0 }`.

The 332-byte plaintext for `/relation/GetList` in the current server log
(`plaintext_bytes=332`) is the **mock** response, not the original server's —
do not mistake it for recovered data.

---

## 7. Confidence summary

| Finding | Confidence |
|---|---|
| 9 `/message/*` paths and 23 `/relation/*` paths, verbatim with offsets | **high** |
| Adjacent `/friend/`, `/world/`, `/arena/`, `/mirage/`, `/guild/` social paths | **high** (path), medium (ownership) |
| All key names in §3a/§3b, with offsets | **high** (present), medium (request-vs-response attribution) |
| `PV_MSG_*` / `PV_RELATION_*` / `PV_SNS_INVITE_*` error vocabulary | **high** |
| All demangled class/struct names in §2 | **high** |
| **Every mail route (9/9) falls through to the mock** | **high** |
| **21 of 23 `/relation/*` routes fall through; 2 are empty stubs** | **high** |
| `/relation/BlockList` is a `map<pvid,nickname>`, stub is wrong | **high** |
| `/relation/GetList` has four buckets (`friend`/`candidate`/`request`/`received`) | **high** |
| `/relation/GetList` is one bucket per call keyed by `PV_FRIEND_INFO::TYPE` | **high** — settled by §6b.2: two calls, `type=1` then `type=3` |
| Numeric meaning of `type` 1 and 3 | **low** (inferred mapping, §6b.2) |
| `/relation/GetSuggestedFriendList` is paged via `start`+`length` | **high** |
| `/relation/GetTargetUserInfo` sends `list` (array of pvid), not `target_pvid` | **medium** |
| Boot-path routes: 5 from this subsystem, order in §6b.1 | **high** (repeated across 5+ sessions) |
| `/message/GetUnreadCount` is the only mail route ever exercised | **high** |
| Mail list rows are a JSON array | **medium-high**, unverified — see 6.1 |
| `content_result` is a body/payload field | **low** — see 5b |
| Struct layouts for `PV_MSG_INSTANCE`, `PV_FRIEND_INFO`, `PV_TARGET_INFO` | **unknown** — see 6.4 |
| `/message/ClearSent` / `/message/ClearReceived` paths | **unknown** — see 6.3 |

**Not recovered, searched and empty:** `/mail/*`, `/chat/*`, `/social/*`,
`/sns/*` HTTP routes; a bare `title`, `body`, `sender`, `read`, `unread` JSON key
in this subsystem; any member name for `PV_MSG_INSTANCE`, `PV_FRIEND_INFO`,
`PV_TARGET_INFO`, `RECOMMENDER_DATA`, `SRTARGET_USER`.

**Out of scope for this file:** the exact values behind `PV_FRIEND_INFO::TYPE`,
`CSRMail::DATA::TYPE` and `CSRGuild::MSG::NOTI_TYPE`; chat/WebSocket framing
(`CPVChatClient` exists but the message list UI is a separate concern).
