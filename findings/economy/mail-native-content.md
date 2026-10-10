# Native Mail notification content: plain string, no attachment receipt

2026-10-05. Read-only parent mail-contract dumps, existing mail-native-transport.md and original ELF Thumb/symbols. No source/native/VM/Ghidra/adb operations and no message sent.

## Distinguish notification body from attachment content_result

Fresh `ghidra-mail-contract.txt`/keys prove mailbox list parser only reads **ret_data.list[] and unread_count**. CPVMsg::ParseMsgInfo G7ffd2c reads each row's **content as strict JSON STRING**, storing it in PV_MSG_INSTANCE. A nonempty string field must exist; an object suchas{title,body} is not the recovered shape.

**content_result is not a list-row field.** Existing mail-native-transport.md pins it to the distinct **ProcessTakeAttachmentComplete G80101c** claim receipt. A system notification without attachment needs no content_result and must not create a fake reward/attachment claim response. No exact attachment content_result schema is recovered here; it is irrelevant to an honest no-reward notice.

Original **CSRMail::DATA(PV_MSG_INSTANCE const&) Gb4b4f8** real body endsGb4b688 (size0x190). Read-only Thumb inspection shows copying raw fields/string and noJSONparse call. Thus this constructor does not establish a nested JSON-text format inside content. Do not invent JSON-stringifiedtitle/body for it. Plaintext notification content is structurally supported; final body renderer requires the remaining consumer dump to confirm formatting/markup rules.

## Notification row fields already exact

ParseMsgInfo keys: id,sender_pvid,sender_nickname,receiver_pvid,receiver_nickname,from_admin,app_code,content,attachment,is_archived,is_read,is_attachment_taken,created_datetime. String fields sender/receivernickname,app_code,content are strictstrings. Numericids/flags accept normalnumericvalues. MessageTYPE is command-derivedcallbackargument, notproved JSONrowtype.

Attachment **null** is parser-guarded; omit reward content and attachment description/item_list/IAP fields entirely byusingnull. Do not pretend `attachment:"{}"` is an equivalent null or add zero-rewardrows toexerciseclaimcallbacks. Coherentunread_count andstablepositiveID are requiredforRead/cacheprojection; the currentauthoritativeaccount recipient mustmatch the mailboxowner. No arbitrarysender/recipient accounts created bythisresearch.

Candidate scalar shape (localmetadata placeholders, not a dispatchedmessage):

```
ret_data:{unread_count:1,list:[{
 id:notificationID,sender_pvid:0,sender_nickname:"Local replica",
 receiver_pvid:actualAccountPvid,receiver_nickname:actualAccountNickname,
 from_admin:1,app_code:"_SR",content:"Local revival status notification.",
 attachment:null,is_archived:0,is_read:0,is_attachment_taken:0,
 created_datetime:validatedNumericTimestamp
}]}
```

Systemsender0/adminprofile/UIflags require renderercontrol beforeproductionassertion; scalarscheme is parser-supported, not a verifiedrenderednotification. No sendingtool/endpoint action was performed.

## Date wire format and remaining unit proof

Created_datetime is read G800526, converted **unsigned32 scalar**, stored lowword+0x48 andhighword0 atG800572. NumericJSON or numericstrings work; ISOdatetime strings run throughstrtod and wouldnotproduceanISOdateparse. Therefore wireformat is numeric, not `%Y-%m-%d...` text. **Epoch and seconds/milliseconds units remain unresolved** until timeconsumer isread; no original timestampvalue was captured. Do not claim a dateformat fromfieldnamealone.

SortByReceivedTime Gb4d7f8 and UI dateconsumer are nextexacttargets. CellMailPost::LoadView G89e834 only loadsviewlayout/template; actualtextpopulation is **CellMailPost::Init G89e1c0..G89e834**. Original calls SetText atG89e46e/G89e4c8 andfurthercodeafterinlinepools needsvalidThumbdecomp. Parentfocused **CSRMailDATA ctorGb4b4f8**, **CellMailPost InitG89e1c0**, **SortByReceivedTimeGb4d7f8**, andmail-openpopupconsumer identifiedfromitsbuttoncallback willpin plaintextcontent/date andnoattachment actions. Currentprovidedmail-contract doesnotcontainthesegame-specificconsumers.

This closestransportnotificationfields andcorrectscontent_resultattribution whilekeepingdateunits/renderingunknown. No systemmessage, currency, attachment, readflag, privateaccount or gameplaystate changed.
