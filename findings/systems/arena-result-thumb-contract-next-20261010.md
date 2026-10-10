# Arena result blank circles: two independent resolver contracts

2026-10-10. Read-only native exports, existing Mail profile research and current
server source. Only this note written; no Ghidra/UI/runtime or image changes.

## Reward identity is FC1, not a guessed resource name

CSRPopUpFCResult.SetData **Gc21274** (ghidra-arena-result-thumbnails.txt
170–222) constructs CSRItemBoxDraw, then calls SetData with a literal item ID
and absolute difference of RESULT_LOG uint32 fields+20/+24. The shown10 is
consistent with the accepted honor10→20 receipt; this is presentation of the
existing reward, not an inventory grant or new original reward amount.

Bounded original-ELF PT_LOAD reads independently resolve:

- slotGc215ec word0x114db4c + decompiler ADD-PC baseGc214dc = G1d6f028,
  exact ASCII **FC1**.
- slotGc215e8 word0x115f376 + baseGc2145c = G1d807d2, **item_box** template.

Root's relocated literal export should corroborate these before implementation.
Current itemReference source has no FC1 row. Follow **CSRItemBoxDraw.SetData
Gaee914**, generic **CSRThumb.LoadThumbnail G1063dfc** and **CSRThumb.SetItem
G10648f2**, then **CSRItemThumb.LoadRes Gaf7404** as admitted by the actual
classification branch. GetItemData **Gaf109c** and the earlier Veteran receipt
reports explain how missing metadata can reach a neutral fallback; they do not
establish FC1's exact thumbnail_id or prove this is the sole runtime cause.

FC1 is a recovered **item ID**, not an explicit sprite ID. No guessed IT_FC,
HONOR, FC1 sprite alias, currency art substitution or new image is justified.
Scout original packs only after a native/static row or explicit consumer binds
a real resource name. Existing Waiting Room Fight Chip icon is a separate UI
binding, not automatically the full result-item thumbnail metadata.

## Profile circles use brief-user profile_url

SetWinnerInfo **Gc21838** and SetLoserInfo **Gc22194** create
CSRUserProfileDraw and call **SetPVID G10aa770** (new export527/1271). These
circles are not CSRThumbCard/ref002 portraits. Existing
mail-portrait-profile-contract.md already closes:

    SetPVID → CSRUserPool.Get G10a397c
    → SetPVID callback G10abd9a
    → SRTARGET_USER+40 profile_url
    → LoadImageFromURL G10ab404

Native CPVRelation.ReqUserInfoCB **G8227f0** consumes ret_data.list brief rows
with pvid/reg_utc/utc/nick_name/country_code/profile_url/profile_status/like_cnt/
is_like. Current game-routes.ts gives that shape and a URL only for reserved
LOCAL_MAIL_SENDER; own1000001 and rival9000001 fall through the historical
detailed-party response. A rival.thumbnail string"002" does not populate this
URL resolver. This is a concrete response coverage gap distinct from missing
Hunter combat art, ownership or economic balance.

The same CSRUserProfileDraw image callback's exact **100×100** size gate is
already documented in mail-avatar-size-gate.md. Preserve this existing contract
instead of serving an arbitrary150×150 reward/card sprite as a profile image.
Two explicitly local brief profiles with valid source-backed100×100 URLs can
repair presentation once exact actor-appropriate art is chosen and verified;
do not call the old Mail system icon an original Hunter avatar, or create
accounts/owned cards merely to render reserved fixture-rival9000001.

No new getter/profile/asset probe is needed merely to rediscover these shared
Mail contracts. Native result rendering after a narrowly scoped metadata/brief
profile repair remains a separate validation step; league/weekly/revenge rules
and original economics remain unrecovered.

## Exact FC1 ownership follow-up: metadata association still missing

Targeted existing recovered-reference JSON, native item display/factory exports
and retained literal-key indexes supply no positive FC1.thumbnail_id association.
This is a scoped evidence result, not a claim that all original assets lack
the art or that original metadata is unrecoverable.

The retained normal CSRItemThumb.LoadRes chain is explicit at
ghidra-item-thumb-display.txt399–407: GetItemData(ref) returns INFO, then
CMHashID.Set consumes the **INFO+38 string** directly before LoadSprite.
It does not invent a FC1-specific resource alias. Generic factory/Init evidence
does not override that metadata string. No new atlas/resource name can be
selected from the result quantity or item ID alone.

Two independent exact literal consumers corroborate currency identity only:
ghidra-village-input-button-keys.txt403–405 resolves BT_MY_CHIP at Gc0c964/
ADDGc0c96c and FC1 at Gc0c9ac/ADDGc0c9ae; special-supply-keys.txt89 also
resolves FC1 at Gf97fe6/ADDGf97fec. These are item/currency references, not
a recovered full-size thumbnail resource or server GetItem row.

There is therefore no explicit recovered resource ID for an additional
ownership scan. Do not turn nearby guessed IT_FC/ICON_FC names into evidence.
Root may separately recover the original Waiting Room currency node's resource
binding, then choose a clearly labeled local display mapping if appropriate;
that would remain distinct from recovering FC1's original GetItem metadata.
Profile brief-shape coverage can be repaired independently while FC1 art stays
an explicit missing association.
