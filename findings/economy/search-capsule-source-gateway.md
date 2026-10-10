# Capsule source type3 is a generic campaign-stage gateway

2026-10-05. Read-only `ghidra-training-trace-gateway.txt`, item/reference reports and original ELF Thumb. No source/adb/Ghidra/runtime operations.

## Candidate row fits recovered native semantics

Reference trace row `{item_id:"AIRSHIP_TICKET",type:3,source_id:"n_01_07",order:1,thumb_id:""}` is a structurally supported **local stage acquisition link**. It is not an original captured AIRSHIP trace row, purchase offer or inventorygrant. Capsule base use_type0 stays a localgenericitemmetadatafixture; source type3 is independent of baseuse_type3 (hunter trace items).

ItemDetail::OnButtonClick Gcc6630 **source-type3 case** reads source_id and calls GetStageLinksDataToStageID. It does not resolve a hunter/card reference. This is a generic stage-navigation branch, applicable to any item whose source metadata points to a campaignstage. IsActivatedTrace Gcc7b88 case3 reads GetStageAchieveCnt(source_id); a positive actualstageachievement supplies activation. Since parent reports actualn_01_07 cleared, this predicate is supported without manufacturedflags.

CreateTraceList Gcc6044 has a non-card-mode stage-link pruning pass: it groups type3 rows by cleared/uncleared stage counts and removes excess rows, preserving representative entries. A single type3 row is not eliminated as a hunter-onlyunsupportedsource. Multiple rows andordering should not be invented until intendedrepresentative behavior is validated.

## Exact click prerequisites/navigation

- Rejects current AutoCombat CheckShortcutsScene==0x1c withtoast, leaving normalbattle/auto restrictions intact.
- Otherwise closesItemDetail, requires nonempty source_id and existing stage→area link; invalidlink doesnotproduceavalidmaptransition.
- Gets linked area, writes native currentarea/currentstage through UserLocalDB.
- Normal type1 campaign area transitions to map SceneTYPE0x86; alternativearea branch uses0x84; missing/defaultarea handling is separate. This is navigationonly—no Search capsule debit, reward, purchase, native battle start or tutorialclear is generated here.

The current stagecatalog already includes actualn_01_07→area nestedlinks; beforeliveuseconfirmreference rows stillcontainthatlink ratherthanlegacyN007 artfilename. Targetsource_id must be realstageid, not anassetname or hunterid.

## Empty thumbnail is explicitly safe

Original SetThumbnail Gcc8b3c reads TRACE.thumb_id string+0x14 and computeslength. **Gcc8b66/68 zero→Gcc8cc4 normalcleanup/return.** Therefore `thumb_id:""` skips thumbnailrendering; it does not attempt LoadThumbnail(empty) and requires no guessedfallbackart. Nonempty calls CSRThumb.LoadThumbnail Gcc8b86. This leaves thetext/sourcebutton independent anddoesnotprovecapsuleheaderitemthumbmetadataoriginal.

## Remaining UI/ref metadata checks

GetItem trace parser needs actual item_id, numericorder/type, source_id andthumb_idstrings. ItemDetail CreateTraceList looksuptrace rowsbycurrentitemreference; item_id must be AIRSHIP_TICKET, matchingbaseid andownedcapsuleID. Baseitemname/description/effect/rank/sell/collect fields remain required evenwhenordinaryuse_type0 isunusedbythegateway. No originalthreshold/purchaseprice/grant rate canbeinferredfromthistype3link.

SetTrace Gcc7fdc invokes SetTitle Gcc85d8 and SetThumbnail Gcc8b3c, and queries source-stageachievement for type3; no directCardInfo lookup is needed by the provedclick path. ParentcanpreservefocusedvalidThumbdecompofSetTrace/SetTitle if text/titlelayout differs; existingclick andemptythumbguards are concreteenoughforaboundednativegatewaycontrol. Nocontrolperformedbythislane.
