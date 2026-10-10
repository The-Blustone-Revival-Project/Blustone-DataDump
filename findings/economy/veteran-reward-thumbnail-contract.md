# Veteran EXP reward thumbnail: VIP1 metadata versus footer artwork

2026-10-09. Read-only retained native exports/original Thumb, current item/reference source and earlier material reports. No Ghidra, ADB, runtime, inventory, wallet, asset or server edits. Root's current login receipt shows blank quantity20 despite the original Shop footer glyph rendering.

## Reward identity is original, not an inventory grant

`login-bonus-veteran-receipt.md` closes RequestLoginReward Gf49410's captured SRREWARD_INFO first field20 and GetItemThumbList **Gafa584** synthesizing exact string **VIP1** at Gafa5d2, then passing captured quantity to AddThumbList. Absolute calendar settlement is `reward.user.vip_exp.cur`, independent of thumbnail metadata. Current server correctly treats it as persistent Veteran EXP; a VIP1 item stack or extra20 credit is not a display fix.

**AddThumbList Gafa420** creates a CSRItemThumb via make_shared Gaf6608 at Gafa448, builds its CREATE_INFO with the supplied ref string and otherwise zero/default fields, calls **Init Gaf6f58 at Gafa48e**, SetContents0x11 and displayed quantity. This inspected factory chain does not select a special numeric “VIP item type” or append an IT/VIP resource suffix. No new numeric resource/type ID is established by the synthetic name VIP1.

## Native metadata-to-resource seam

Init copies the ref string into thumb+840, calls LoadView Gaf70a0, then dispatches normal **LoadRes Gaf7404** or character LoadRes_Char according to thumb+865. The retained normal LoadRes obtains **CSRItemInfo.GetItemData(ref)** at its indexed ref string, then uses returned **INFO+38 thumbnail string** directly in CMHashID.Set -> CSRUIImageNode.LoadSprite (retained `ghidra-item-thumb-display.txt` lines399–407). Rank/background rendering is separate. This is the same normal item resolver already used successfully for the Search capsule.

Current `server-ts/src/hunter-traces.ts::itemReference()` publishes RP1 as an explicit local display reference, plus fuel/capsule/trace rows, but **no VIP1 row exists** in current source. CSRItemInfo.SetItem **Gaefe10** consumes full envelope `ret_data.item[]`; exact recovered fields include string id/name/desc/thumbnail_id/effect and numeric rank/use_type/sell_price/collect_qty. `thumbnail_id` literal is resolved at Gaf00c8/Gaf00cc in `ghidra-shop-fuel-strings.txt`.

GetItemData **Gaf109c** searches its native item map; a missing key enters a fallback-key lookup and then a statically initialized neutral INFO fallback if that also misses (Gaf10c4..1174). This supports a concrete metadata-miss hypothesis for blank VIP1; it does not establish the fallback's exact key/resource string without relocated literal resolution. Merely serving another UI_SHOP copy cannot populate this map.

The current source absence plus resolver is actionable evidence, but native cached VIP1 classification/returned INFO/thumbnail string should still be verified before claiming the exact observed blank's sole cause. Generic CSRThumb classification paths and this CSRItemThumb display class must not be conflated.

## Original ICON_VE is a footer binding, not proved receipt metadata

`vip1-original-icon-resources.md` establishes unchanged final **UI_SHOP.jet**,1236254bytes/SHA25689f3cc6750f01b3ca149ceece7c0798d963569bd8b6bb504c0c6be2b61162a09. Exact sprite **ICON_VE** S2 -> same-pack image0xd41fffca I2,14×17 RGBA with131 positive-alpha pixels. Earlier native Shop footer validation and preserved layout XML explicitly bind ICON_VE beside Veteran points.

No exact outer resource named VIP1/IMT_VIP1/IT_VIP1 was found in the earlier complete774-pack scan. That does not prove every possible full-size Veteran reward resource absent. More importantly, **footer ICON_VE residency/binding does not independently recover a VIP1 GetItem row's thumbnail_id**. The earlier material report says root selected this binding but supplies no exact receipt-map parser/source assignment; keep that stronger assignment unproved here.

A display-only local VIP1 metadata reconstruction could use an independently justified original resource through the normal resolver while preserving all EXP receipts and inventory. Such a choice must be labeled local display policy; no invented item behavior, source hunter, redemption/sale or numeric enum follows. This lane does not select new rank/use_type/effect values or claim the tiny footer sprite is the original full-size reward art.

## Size gate and next exact proof

Retained **CSRItemThumb.LoadRes Gaf7404** passes thumbnail_id directly to LoadSprite and attaches the image; no exact100×100 or150×150 equality gate appears in that exercised function's retained export. The Mail portrait's strict100×100 gate is a separate native class/contract and must not be applied to VIP1. Search capsule150×150 was an original full-size resource/local binding choice, not a universal reward-size requirement. Loader/layout/transitive sizing remains distinct; absence of a local gate is not proof every downstream size is accepted.

Focused root targets, if needed: GetItemData Gaf109c plus relocated fallback literal pairs; current VIP1 INFO/thumbnail string; CSRItemThumb.Init/LoadRes branch and attached sprite resource; actual CSRUIImageNode.LoadSprite transitive sizing only if native evidence reports a size/resource failure. Preserve original UI template size/render options and verify a native receipt/detail/reference-backed display without replaying an already claimed login reward or granting VIP1 inventory. Future eligible claim can validate the actual captured20 receipt after reference repair.

No wallet repair, extra package, alias, rebuilt client, reward replay or numeric item type is warranted solely by the blank icon. The concrete current gap is source item metadata coverage, with original full-size receipt-resource assignment still unrecovered.

## Owner-qualified items-only native read

Original ELF dynsym locates `CMSingleton<CSRItemInfo,DefaultAlloc,CMSpinLock>::get::wpRet` at **B+21d3ad4**, with control pointer at+4. Its companion guard symbol is21d3adc. This static weak pair points **directly to CSRItemInfo**, not to an intermediate CMSingleton Holder allocation. CSRItemInfo.get Gaf18bc calls template get Gaf1920; at Gaf196c..198a it copies the held object's pair from the typed pool Holder into wpRet, and at Gaf1a10..26 weak-locks that pair for the caller. A reader must not call get to instantiate or lock it.

Concrete object owner: **default_delete<CSRItemInfo> shared control** original vtable symbol2151cd4, primary **B+2151cdc**. Constructor Gaf3fd4 allocates control0x10 at Gaf3fe2..e4 and stores raw object at **control+c** (Gaf3ff6). Typed Holder pool's fresh branch allocates the **plain CSRItemInfo object0x30** at Gaf3b48..4e, initializes its trees/vectors, then calls this shared-pointer constructor at Gaf3b8c. Require static pointer/control nonzero, exact control primary, signed control+4>=0, u32(control+c)==object, readable object0x30 and repeated static pair/control/raw ownership. No object vptr or inline object==control+c predicate applies. An empty/expired weak pair is unavailable, not permission to run a native allocation.

CSRItemInfo's item tree has **minimum node+0, root+4 and count+8**; the tree end/sentinel address is **object+4**. This follows Gaf2740's native typed `tree<string,INFO>.find`: it loads root+4, compares byte strings at node+10 and traverses left0/right4. Header trace/global tables at+c/+18 are separate; do not search them as ordinary item rows.

Typed insert **Gaf1e44** allocates a **0x6c item node** at Gaf1e74..76. Layout: childleft+0/right+4, parent+8, colorbyte+c, lookup-key std::string+10, **inline INFO+1c, size0x50**. GetItemData Gaf10c6 returns node+1c for an exact map match. INFO copy Gaf1aa4 independently confirms strings at INFO+14/+20/+2c/+38/+44. The **thumbnail string is INFO+38**, as the normal item-thumb loader directly consumes it; numeric metadata occupies the first0x14 bytes. Do not assign meanings to other numeric/string offsets merely by this layout.

Minimal scoped lookup: read only target keys **VIP1, RP1, DUMMY** from the qualified ordinary item tree using a finite depth/cycle bound and bounded native std::string decoder. Keep comparisons byte-lexicographic as Gaf2740 does; the NDK short-string tag/length and long pointer/length must remain bounded and repeated. Read a matching node's thumbnail at node+1c+38 (node+54), plus desired raw metadata only inside the established INFO0x50 allocation. Record key+node/INFO provenance; do not emulate GetItemData's fallback and silently report DUMMY as VIP1. Missing VIP1 and present DUMMY are two distinct lookup observations.

Repeat all traversed links/keys/selected INFO bytes, tree root/min/count, static weak pair, owner type/nonexpired/raw object pointer before publishing. Do not dereference a key's arbitrary external string without mapped-range/bounded-length checks, call Find/GetItemData/LoadSprite natively, mutate cache, or expose unrelated item/account/auth records. Exact native VIP1 metadata presence/thumbnail can then be compared before/after normal server reference reload without claiming a future login reward.

## Root follow-up: exact fallback and deployment

Relocated literal export analysis/ghidra-veteran-item-lookup-keys.txt resolves the fallback key to DUMMY at Gaf1136. Checked native reads before/after are retained in analysis/testing/veteran-display-001: VIP1 missing/count6 became VIP1 thumbnail ICON_VE/count7; RP1 remains IT_CO and DUMMY remains missing. The new mapping is local display policy; actual receipt rendering is still unproved. All three persisted gameStates remained unchanged.
