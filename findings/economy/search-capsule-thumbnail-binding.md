# Search capsule thumbnail binding

2026-10-08. Read-only original UI database, PAD UI_ITEM and retained native exports. Only this report written. No ADB/Ghidra/runtime/server/profile/save edits or grants.

## Finding and implementation candidate

The original Search header explicitly draws **IT_TK_SE_S**. This closes the capsule artwork identity through the same header panel whose native counter reads **AIRSHIP_TICKET**. It does not recover the original server GetItem row or prove which size that row used.

An evidence-backed **local display reconstruction** is to set only existing AIRSHIP_TICKET fixture thumbnail_id to **IT_TK_SE**, the original 150×150 member of that exact Search ticket family. The native item-thumb resolver accepts the resource name directly; no invented alias, texture substitution or UI XML edit is needed. Preserve the fixture labels on rank/use_type/effect/prices and call the size selection local until original metadata/native validation proves it. IT_TK_SE_S is the independently proved header variant; IT_TK_SE is the suitable full-size candidate, not a recovered server metadata assignment.

Root observations: analysis/testing/episode05-005/51-reward-current.png shows earned20 with blank reward icon, while 56-search-counter.png shows count36 with actual header capsule glyph. Those are supplied root observations, not this lane's live inspection. Native residency of the full-size variant is still unproved; small header residency alone is insufficient.

## Exact preserved UI binding

Read-only active MANIFEST/SST/Snappy/current+previous WAL parsing using episode-ui-audit.py.read_database; no LevelDB open, lock or compaction. Source recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db.

**KO/SEARCH/SE_MAIN**, 2884 bytes, SHA256 fa55996bc2261e855c69dbf0367898f2daddf50877b8bd5428bdeb76ac54cf7b. Original XML:

- panel name PA_TK_SE, pos -12,12, size200,40, align right,top.
- button name BT_TK_SE, normal-spr BT_GS_L.
- sprite res-name **IT_TK_SE_S**, pos25,0, align left,center, render-option alphablend.

These are explicit literal resources, not a blanket KO→EN alias proposal. Retained search-entry-reference-contract.md pins OnInit LoadView to SEARCH/SE_MAIN and PA_TK_SE. search-capsule-content.md and ghidra-find-shard-entry-contract.txt establish SceneFindShard counter's Inventory.GetInstItemCnt("AIRSHIP_TICKET"); exact literal Ge23f36/Ge23f38 resolves G1d7f0b5. search-capsule-purchase-contract.md pins the same BT_TK_SE branch Ge248e2..ec to ItemDetail("AIRSHIP_TICKET") at Ge24b02..0a. Thus the header icon/counter/item-detail identity crosswalk uses original UI plus native consumers, not ordinal/name resemblance alone.

## Complete original image graph

Original recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/UI_ITEM.jet: 1655400 bytes, SHA256 **4b4350559330947254764f795902b2f66ea48826290316b9eb2bd295bd446eda**. Fresh 24-byte header walk reaches exact EOF with391 records; every inspected part length matches total and inflation. Name uint64+12/native base38; packed length+8. Four names are S2 descriptors, count1/imageID+46. Referenced I2s exist in this same genuine package and decode read-only with jet_decoder.decode_i2_texture; alpha counted in memory.

- **IT_TK_SE** ID0x1f48986d8ba: S2 header1653179/packed34, SHA256 c8d392060c91d84fe187ffda75eb09e393a1d7cea9bddc51c45f238178384fff → I2 **0xf16730e5**, header1150020/packed8050, **150×150**, positive-alpha pixels2757.
- **IT_TK_SE_M** ID0xb0757bc9e7ebc: S2 header1653237/packed35, SHA256 afe7a44fafd2c9d74977e8c84e204d2b3f192e7bdbb2b4b98383c227867c5af4 → I2 **0x13d2854e**, header1160116/packed3660, **54×53**, positive-alpha pixels1079.
- **IT_TK_SE_S** ID0xb0757bc9e7ec2: S2 header1653296/packed35, SHA256 a82f35d34fd4f6858abcee5491320fbee3782f17608e60500cade2f4e8adef21 → I2 **0x6d274682**, header1158667/packed1425, **32×32**, positive-alpha pixels354. This is the literal header binding.
- **IT_TK_SEXS** ID0xb0757bc9e7e2a: S2 header1653355/packed34, SHA256 3bb624dc02e84340fe3738dfe2cbecfe8bc88250de4b258527436f80b07a5c1d → I2 **0x74912397**, header1158094/packed549, **18×18**, positive-alpha pixels108.

No missing/type-mismatched edge or zero-alpha texture in these four graphs. No runtime/CDN selection modified here.

## Native metadata-to-thumb resolver

Retained ghidra-shop-fuel-contract.txt and exact keys ghidra-shop-fuel-strings.txt prove CSRItemInfo.SetItem **Gaefe10** consumes full envelope ret_data.item[]. Required base identity id; string thumbnail_id is explicitly read via LDR **Gaf00c8** / ADD **Gaf00cc**, resolved **G1d7a112**. Other metadata and trace/global collections remain separate.

Retained ghidra-episode-reward-display.txt: CSRPopupEpisodeReward.SetItemData **Gcfb30c** calls CSRItemThumb.factory(ref_id), SetOwnedCount(quantity), and enables detail opening. ghidra-item-thumb-factory.txt/ghidra-item-thumb-display.txt: Init **Gaf6f58** copies CREATE_INFO reference string to thumb+0x840; when character mode+0x865 is false it invokes normal LoadRes **Gaf7404**. Normal LoadRes calls CSRItemInfo.GetItemData(thumb+0x840), then **CMHashID.Set(returned INFO+0x38)** and **CSRUIImageNode.LoadSprite** (retained display lines399–407). Rank background separately comes from the item row.

This resolver passes the supplied thumbnail resource directly. No hard-coded AIRSHIP_TICKET override, automatic IT_TK_SE suffix selection or header-glyph fallback is present in this exercised normal path. Current server-ts/src/search-capsules.ts supplies an empty thumbnail_id, consistent with the blank reward art. Runtime success after changing that one fixture field still needs a genuine native thumb display; do not grant/replay E05 merely to manufacture that proof. Item-detail access from the already-owned capsule stack is a prospective display path, and existing earned reward marker remains preserved.

## Limits

Original full GetItem row for AIRSHIP_TICKET remains absent from the bounded previously audited exports. Original rank/use_type/effect/collect_qty/sell_price/name/desc and full-size thumbnail assignment are not recovered by artwork. This evidence closes genuine Search capsule artwork and normal resolver behavior; a one-field local display choice improves the revival without claiming original metadata fidelity. No blanket aliases, duplicate reward grants or economy changes follow.
