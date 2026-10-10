# Fishing tutorial EndWithSell settlement parser

2026-10-07. Parent's completed ghidra-fishing-end-settlement.txt, retained
tutorial transition/hook dumps and bounded original ELF Thumb/literal evidence.
No Ghidra/device/source/account actions or receipt implementation. G addresses
are Ghidra coordinates; ELF=G-0x10000.

## Tutorial transport and shared callback

Root observed original tutorial cast/wait/hook without ordinary Begin. Separate
native builder evidence proves RequestTutorialEnd's signed string
**log_id:"-1"**, plus is_win; no End request has yet been observed. Do not
normalize this into an ordinary positive-log attempt. RequestTutorialEnd
**Gb28864** and ordinary RequestEnd **Gb29624** both use /fishing/EndWithSell.
Retained hook decomp calls RequestTutorialEnd(1,callback,1). Neither a separate
tutorial success DTO nor a tutorial-only ParseEnd was identified.

**ReqEndCB Gb2a308** checks HTTP result1, removes the stored local consume record,
decrypts its response body and parses **the full JSON envelope**, then calls
**ParseEnd Gb2a560 atb2a468** with that full body. Its extra byte argument is
used for error-popup behavior (b2a3be); it does not choose a different success
parser. Failure does not enter the success settlement path. After ParseEnd,
it looks up **fullJSON.ret_data.sell** (ADDb2a46e/b2a47a); if nonnull, calls
**ParseSell Gb2b018 atb2a488** with that subtree. Empty/absent sell does not
justify a fabricated price or sale.

## Success hierarchy and mandatory no-op fields

ParseEnd first extracts **fullJSON.ret_data** (ADDb2a580). It does not parse a
nested reward or catch object. On that ret_data object:

- **fish_id is a mandatory STRING**: lookupADDb2acd2, unguarded
  from_json<string> **b2ace4**, moved into Fishing+68/+6c/+70. Omitting it or
  sending null/number is not a callback-safe success shape.
- **grade** (ADDb2ad2e) converts to uint32 and stores Fishing+78; **length**
  (ADDb2ad88) converts to signed32 and stores+7c. Their permissive default/
  conversion branches do not establish original grade enums or length units.
- **consumed_inst_list** is unconditionally passed to Inventory.UseItem
  at**b2ae90**. An empty array is the established no-consumption collection.
- ret_data is unconditionally passed to **Achieve.ParseLobbyEnter844918
  atb2aec4**. Neutral compatibility requires **dailyquest_min_stage:""**,
  **daily_quest:[]**, **linear_quest:[]** from the shared parser contract.
- Optional nonnull achievement is passed to ParseAchievementsElement atb2ae60.
  Omission avoids invented quest updates.

These are parser requirements, not proof that a tutorial actually caught a fish
or that the original server supplied an empty receipt.

## Catch mutation and replay boundary

After writing fish_id/grade/length, the parser compares fish_id with **NULL_STR**
(original GOT21ab04c resolves ELF21ce3d8, symbolNULL_STR). The empty-string
case skips both catch mutations. Otherwise it invokes **AddInvenb2e758
atb2ae3a** and **UpdateRecordb2e980 atb2ae46** using the returned identity,
grade and length. Thus an empty string is a structurally distinct no-catch
receipt; it must not be described as a recovered tutorial reward outcome.

Returning the same nonempty catch receipt again repeats native AddInven even
if the server transaction is idempotent. Lost-response retries therefore need
explicit additive-client replay handling; generic success replay is not safe.
An empty catch on a retry may avoid duplicate local count, but its effect on
the tutorial callback/result UI and refresh must be validated separately.

## Optional resource branches and unresolved values

Resource parent is **ret_data.user**. This parser handles optional
**user.iap {iap_qty,free_iap_qty}**, rather than shared SyncUser's pair fields.
When iap exists, omitted subfields can become zero and overwrite CPV wallet
components: provide actual authoritative values or omit that branch.
Other guarded user branches include gold.cur, exp.cur, AP/BP current/deadline
and capacity/level-related fields. Do not activate unknown branches with
zero-valued placeholders. No currency/resource change is necessary merely to
acknowledge a tutorial result if no actual earned grant is established.

Optional ret_data.item collection uses inst_id/ref_id/added with Inventory.AddItem;
optional card settlement is separate. Empty/absent collections do not grant
hunters/materials. This report does not generalize card shape from other routes.

Still unknown: whether the original tutorial End returned its locally bound
demo fish or an empty catch; real demo identity/grade/length; original sale
price/reward; successful tutorial-end guide ACK/UI transition and replays.
No arbitrary catch, gold or bait grant is justified. The parent decomp closes
the two requested callback/parser targets; **ParseSellb2b018** is the next
narrow target only if a real sale response must be implemented.
