# Mail attachment platform path: recovered, game use unproved

2026-10-05. Read-only original ELF Thumb plus parent's completed ghidra-mail-attachment.txt and -keys.txt. No device, VM, Ghidra, source edits, accounts, claims or grants. Code addresses are Ghidra coordinates (ELF VA plus10000hex).

## Request

**CPVMsg::ReqTakeAttachment G7faf60** builds6 decimal-form fields:

```text
app_code, app_ver, market, pvid, otp, message_id
```

message_id is the method's uint64 argument converted with to_string(uint64), rather than Read/Archive's target_list. Exact key LDR7fb0d4/ADD7fb0d6 and URL LDR7fb1f6/ADD7fb1f8 resolve **/message/TakeAttachment**. This request has no quantity, card ID, attachment item list or independent claim nonce.

## Exact response hierarchy

**ProcessTakeAttachmentComplete G80101c** checks GetResultCode1 at80107c..801082; indexes full JSON.ret_data at80108c and then reads these siblings from the same parent:

```text
ret_data.content_result     ADD801094
ret_data.unread_count       ADD8010ce
ret_data.message_id         ADD80111c
ret_data.iap_quantity       ADD80116c
ret_data.free_iap_quantity  ADD8011c0
```

The callback copies **content_result verbatim as JSON** into **PV_MSG_RESULT+28**: copy constructor80109e, JSON tag/body transfer8010ac/8010c0. It does not decode content_result.card/item/user, nor does this platform parser call AddCard, AddItem, UseItem or PlayData.SyncUser. This closes the old mail-social.md uncertainty: content_result is not a required list-row parallel wrapper in the examined list callback; it is opaque attachment-result payload in this callback. Its game-specific shape remains unproved.

unread_count is unsigned32 stored in CPVMsg+30 at80111e. message_id is uint64 and used to search the local message map. On a matching cached row, it sets **is_attachment_taken+43=1** at801258 and **is_read+41=1** through the halfword store80125c (which also writes the neighboring byte+42 to0; that byte's semantic name was not recovered). It does not erase the message or mark archived+40 here.

The IAP fields are unsigned32 **absolute scalar balances**, because they are stored directly into CPVDataMgr+9c/+a0 at80126e/80127c, not added. Each store is gated by nonzero at801264..268 and801272..276; a returned0 therefore leaves the native existing balance unchanged. Do not silently replace these with user.iap pairs or claim that0 synchronizes an empty wallet. Correct handling of a legitimately0 resulting balance would require a separately recovered game/account synchronization path.

Finally PV_MSG_RESULT receives response result_code and **command7** at80128c/80128e, its ID vector contains the parsed message_id, and the registered CPVMsg callback receives that result at8012da. A structural receipt therefore has an opaque content_result, the actual claimed ID, coherent unread_count and scalar IAP fields when applicable. No concrete item/card payload schema or original reward amount is recovered by this platform callback alone.

## Game caller audit: no proven attachment claim seam

**CSRSyncMail::ReqRead Gf7ef78** calls **CPVMsg::ReqRead G7f9ca8 atf7f060**, not ReqTakeAttachment. Its original callback closure **Gf7feb8**, selected by function vtableELF217d568, forwards the PV_MSG_RESULT to its captured function; no inventory reward application was found in that closure. **CSRMail::RequestRead Gb4c1a4** invokes the same CSRSyncMail adapter atb4c242 for its platform-message branch; its guild-message branch is distinct. Reading a message cannot be called an attachment claim solely because the DTO contains attachment metadata.

A bounded whole-code Thumb BL/B.W scan overG610000..1c00000 found **zero direct call sites targeting ReqTakeAttachment7faf60**. This is a negative direct-call result, not proof that an indirect call, exported external call or PLT-mediated call can never reach it. No exported CSRSyncMail claim method exists in the retained symbol catalog. The parent fresh decompile independently confirms the ReqRead adapter uses Read only. Consequently this may be an unused generic PV2 SDK path; that remains an inference until all reference/call mechanisms are audited.

**Do not implement a purported real card/item reward claim from this evidence.** An empty-content success would still set native claim/read flags without any recovered inventory application, which is precisely the fake-success risk. No data demonstrates an original game UI action requests TakeAttachment or consumes its opaque content_result.

## Narrow next evidence

Parent can inspect all Ghidra references to **7faf60**, its symbol's GOT/PLT references and address-taking sites, then the **CSRMail::RequestRead** callback closure for any command7/content_result branch. If those have no game consumer, document attachment delivery as unsupported legacy SDK protocol and pursue a real game reward seam already proved to mutate inventory. Do not infer card/item rewards from list attachment.item_list[{code,quantity}]—those are display metadata, not a proved claim settlement DTO.

No original balance, reward contents, claim eligibility or runtime success is claimed here. No attachment was taken.
