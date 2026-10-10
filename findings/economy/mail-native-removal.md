# Received/Sent Mail removal: exact native contract

2026-10-05. Read-only original ELF Capstone and RTTI attribution; companion mail-native-transport.md. No source/Ghidra/adb/VM/live mailbox actions. Code coordinates below are Ghidra addresses (ELF VA plus10000hex); vtables are ELF VAs.

## Actual UI adapter emits comma-separated IDs

**CSRSyncMail::ReqRemove Gf7f138** receives list<uint64> and serializes it into a string. The loop calls to_string(uint64) atf7f184, appends exactly one byte from the **comma** literal atf7f18e, then appends that ID-plus-comma string to the aggregate atf7f1ba. The comma is proved by LDRf7f16e / ADDf7f17c. The next list node is loaded atf7f1da and the loop ends atf7f1e0. There is no trimming before **CPVMsg::ReqRemoveReceived atf7f37a**.

For IDs123 and456 the native field is therefore **target_list="123,456,"**, including the trailing comma. It is not a JSON array request body. Empty-list behavior reaches the same adapter with an empty aggregate; it must not be interpreted as delete-all without separate proof.

**CPVMsg::ReqRemoveReceived G7fc380** copies the caller's char string into target_list (LDR7fc4d8 / ADD7fc4dc, string constructor7fc4ec). Its form initializer has6 fields at7fc4f4:

```text
app_code, app_ver, market, pvid, otp, target_list
```

The URL is **/message/RemoveReceived** atADD7fc5e6. **ReqRemoveSent G7fccb0** uses the same6-field pattern, target_list ADD7fce0c and route **/message/RemoveSent** ADD7fcf16. It accepts a string; the reviewed game adapter's received-removal serialization is the positive source for the comma-list format.

## Exact callback operation attribution

Original function-object RTTI supplies the request ownership, avoiding nearest-function-name inference:

- ELF vtable213e614 invoke+20 points **G804cd6**. Its deep RTTI explicitly names CPVMsg::ReqRemoveReceived $_6. It places **command9** on the stack at804cde/804ce2 and calls ProcessCommonComplete at804ce4.
- ELF vtable213e694 invoke+20 points **G8051aa**. RTTI explicitly names ReqRemoveSent $_7. It passes **command10** at8051b2/8051b6, call8051b8.
- For comparison, VT213e414 invokes **G80336a**, RTTI ReqRead $_2, command5 at803372. VT213e494 invokes **G80383e**, RTTI ReqArchive $_3, command6 at803846.

Thus Read/Archive merely set their local flags, while received/sent deletion is a separate9/10 erase operation. The earlier transport report's unresolved request-command attribution is closed by these exact callback identities.

## Receipt is an array, not the request string

**ProcessCommonComplete G800c30** first checks response GetResultCode()==1 at800c56..5e. It indexes full JSON.ret_data at800c68, ret_data.unread_count at800c72 and **ret_data.target_list** at800cbc. It numerically indexes that collection at800d16, converts each element to uint64, and looks up the corresponding existing local PV_MSG_INSTANCE.

```json
{"result_code":1,"ret_data":{"unread_count":0,"target_list":[123,456]}}
```

The example is a schema illustration, not a performed deletion or original reward fixture. unread_count must reflect the remaining account mailbox; it is an unsigned scalar, not an unread-ID list. Returning a comma string here does not match the request's response parser.

The shared command check subtracts9 and compares against2 at800dd2..800dd8. For commands9/10 it searches the local map and **erases the matched iterator at800e34**. The response IDs are also collected into vector<uint64> (800da6/800db6), assigned into PV_MSG_RESULT at800ebe, and delivered through the registered CPVMsg callback at800ee6. A successful receipt omitting an ID therefore does not erase that cached row. Unknown IDs cannot create rows and are skipped by the local lookup path.

For command5 it writes is_read byte+41 at800de4; command6 writes is_archived byte+40 at800e3c. Those offsets match ParseMsgInfo's flag stores. Delete is not equivalent to Archive and does not use is_archived as its receipt schema.

## Game/UI callback seam and safe scope

The game-facing exported method **CSRMail::RequestRemove Gb4bc80** receives list<CMHashID> and a callback `(int,const vector<CSRMail::DATA>&)`. The platform adapter above positively proves received deletion is the path supported by CSRSyncMail.ReqRemove; the UI/data-layer callback also includes guild-message handling, whose exact conversion and refresh path were not reconstructed in this bounded task. Parent decompile targets: **b4bc80**, **f7f138**, the RTTI-owned completion closure from CSRMail::RequestRemove $_2, and **800c30**.

The smallest sound server implementation would authenticate the mailbox owner, parse the actual comma-list (allowing its one terminal empty component), validate positive integral IDs, delete only that owner's matching received rows, persist once, and return numeric IDs actually settled plus coherent unread_count. Whether unread/unclaimed-attachment deletion is prohibited by original server policy remains unknown; the native transport does not prove its authorization rules. Do not invent refunds or reward claims during removal. Lost-response retries and already-removed IDs should be specified as local policy; the wire contains no independent deletion nonce.

**Do not add imagined ClearReceived/ClearSent routes.** The old no-ID Clear builders unexpectedly resolve RemoveSent in the original ELF, as mail-native-transport.md records. Single/batched received deletion is independently proved here; that odd bulk-clear behavior remains separate and unresolved. No messages were removed by this research.
