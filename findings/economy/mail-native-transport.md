# Native Mail transport and DTOs

2026-10-05. Read-only original ELF Thumb and native-evidence.tsv, mail-social.md and current game-routes.ts. No messaging, grants, adb, VM control, Ghidra, phone actions or source changes. Addresses are Ghidra coordinates: original ELF VA plus10000hex. PC-relative keys were resolved from matching LDR-register/ADD-PC pairs, with control-flow/clobber resets; raw instructions corroborate structural claims below.

## Request fields

All examined CPVMsg request maps include app_code, app_ver, market, pvid, otp. The following additional fields are proved:

- **GetReceivedList G7f89c8** and **GetSentList G7f9338**: start, length, after, before. Received key ADDs7f8b38/7f8b60/7f8b8a/7f8bb4; sent7f94a8/7f94d0/7f94fa/7f9524. Each map has9 entries (Received initializer7f8bd8). The signature is `(uint64 start,uint32 length,uint64 after,uint64 before)` and values are decimal form strings. after/before's exact ID-versus-time cursor interpretation is not recovered; do not invent timestamp units.
- **Read G7f9ca8**: target_list, ADD7f9e1e. The single uint64 argument is converted with to_string(uint64) at7f9e18 and placed directly in that field; map size6 at7f9e40. This is a decimal string request value, not a JSON array request body.
- **Archive G7fa604**: target_list, ADD7fa77a; same single-ID request pattern. Neither requester posts is_read/is_archived flags.
- **GetUnreadCount G7fe750**: only the5 authentication fields (initializer count5 at7fe8aa). Its uint8 method parameter does not produce a sixth named form key in the examined builder. Response parser independently reads unread_count.
- **Send G7fb8bc**: receiver_pvid, sender_pvid, content, item_code, item_quantity are named in its builder. This is protocol evidence only, not authorization to send messages.

The routes resolve atReceived ADD7f8c88, Sent7f95f8, Read7f9f40, Archive7fa89c, Unread7fe984. ClearReceivedList G7fd5e0 and ClearSentList G7fde98 both resolve `/message/RemoveSent` in the original builder (ADD7fd810/7fe0c8). This surprising original evidence must not be normalized into invented ClearReceived/ClearSent URLs. Its caller behavior needs a fresh parent decompile before implementing bulk removal.

## Response envelope and empty entry

**ProcessCommonGetListComplete G800690** checks CPVHTTPResponse.GetResultCode()==1 at8006c6..cc. It receives the full parsed JSON asr3, indexes **ret_data** at8006d6, then **unread_count** at8006e0 and **list** at800734. unread_count is unsigned32 and stored CPVMsg+30 at80072a. The list is indexed numerically (8008a8), with each element passed to **ParseMsgInfo G7ffd2c**; it is not a bare ret_data array or an object keyed by message ID.

The minimal honest empty mailbox response is:

```json
{"result_code":1,"ret_data":{"unread_count":0,"list":[]}}
```

**ProcessGetTotalUnreadCountComplete G801b20** indexes ret_data at801b4c and unread_count at801b54. Its minimum response is the same envelope with just unread_count. Current game-routes.ts already returns that. Current list fixture returns onlylist[]; the parser defaults missing unread_count to0, so it is viable only for an empty mailbox and would reset a future nonzero badge. A real list must publish coherent unread_count too.

## Message row schema

**CPVMsg.ParseMsgInfo G7ffd2c** consumes one row directly. Exact key ADD locations:

```text
id                    7ffd6a   scalar uint64, stored instance+18 at7ffdea
sender_pvid           7ffdee   scalar numeric
sender_nickname       7ffe44   string conversion7ffe58
receiver_pvid         7ffe9a   scalar numeric
receiver_nickname     7ffee8   string conversion7ffefc
from_admin            7fff32   scalar numeric flag
app_code              7fff7e   string conversion7fff90
content               7fffc4   string conversion7fffdc
attachment            800012  optional; null skips at80002c
is_archived           80043e  scalar flag
is_read               80048a  scalar flag
is_attachment_taken   8004da  scalar flag
created_datetime      800526  unsigned32 conversion; high word0 at800572
```

Use real JSON strings for string fields and numeric0/1 flags. Missing string fields are not a proved safe nonempty row. Message TYPE comes from the callback's command-derived argument, not a proven JSON `type` field. List pagination/last-page policy and created_datetime's epoch/unit remain unresolved. Its unsigned32 storage is proved; an ISO string is not proved accepted (scalar strings go through strtod).

For optional attachment, its **description** string is indexed at80006c (LDR80003e/ADD80005a). Additional nested fields are **iap_quantity** (ADD8000f0), **free_iap_quantity** (800144), and **item_list[]** (8001a4); each attachment item reads **code** (800226) and **quantity** (80022e). Do not substitute game inventory's ref_id/qty fields for these platform attachment fields. Attachment claims and application to game inventory are a separate CSRSyncMail seam; this report does not authorize or implement rewards.

## Read/Archive receipt and native mutation

**ProcessCommonComplete G800c30** checks result1 at800c56..5e, indexes ret_data at800c68, unread_count at800c72 and **target_list** at800cbc. Response target_list is indexed numerically at800d16 and each scalar is converted to a uint64 message ID, then searched in the local CPVMsg message map. Therefore request target_list is a decimal form string, while response target_list is an array of numeric IDs.

```text
ret_data:{unread_count:REMAINING_UNREAD,target_list:[MESSAGE_ID]}
```

Its command5 branch writes instance+41=1 at800de4; command6 writes instance+40=1 at800e3c. ParseMsgInfo assigns those slots to is_read and is_archived respectively. Command9/10 erases matched entries. The mapping of each request closure's captured command to these branches has not yet been independently attributed through RTTI in this report; the exact flags/slots are proved, but do not claim a fully audited Archive storage policy. Unknown IDs do not create messages through this completion path.

**ProcessTakeAttachmentComplete G80101c** additionally indexes ret_data.content_result at801094, unread_count at8010ce, message_id at80111c, iap_quantity at80116c and free_iap_quantity at8011c0. This is a distinct receipt; a generic Read target_list response is not a recovered claim receipt. content_result hierarchy and game-side item/card/reward synchronization are unresolved.

## Narrow next parent dumps

For genuine Mail entry, decompile **ProcessCommonGetListComplete800690**, **ParseMsgInfo7ffd2c**, **ProcessCommonComplete800c30**, and **ProcessGetTotalUnreadCountComplete801b20**. This will close cache replacement/pagination and flag-command attribution without any mailbox mutation. For attachment support later, use **ProcessTakeAttachmentComplete80101c** and **CSRSyncMail ReqRead/ReqEnter callbacks** from native-evidence.tsv; their platform PV_MSG_RESULT wrapper is not itself the wire JSON schema.

Empty lists/unread counts are a legitimate initial seam. A locally authored research mailbox, reward policy or bulk removal needs explicit fixture labeling and durable per-account state; the original sender/content/economics have not been recovered. No mail was sent or claimed by this lane.
