# FMD1 display metadata and original artwork closure

2026-10-08. Read-only retained native dumps, original Episode declarations and
original final PAD UI_ITEM.jet. Only this report written. No ADB, Ghidra,
source/save/profile edits, web hunts or reward grants.

## Decision

**A fully recovered FMD1 GetItem metadata row is not established.** Original
FMD artwork has a complete positive-pixel graph, and native free-currency
display identity FMD1 is proved, but neither supplies the missing item's
thumbnail_id binding and remaining required fields. A guessed use_type0 row
would be a new local display fixture. It must not be described as recovered
metadata merely because the chapter's x30 label already renders.

Original E02 declares item[{ref_id:FMD1,qty:30}], free_iap0. Native
LoginBonus.ParseLoginBonusRef Gf4ae7c synthesizes FMD1 from separate
free_iap (literal LDRf4b5ec/ADDf4b5ee, retained login-bonus keys). The current
replica wallet policy uses the proved Episode SyncUser free_iap{prev,cur}
receipt; no FMD1 inventory stack is necessary for that policy. Display metadata
and historical settlement semantics remain separate from this currency parser.

## Exact native reference schema

Retained `shop-fuel-contract.md`, `ghidra-shop-fuel-contract.txt` and
`ghidra-shop-fuel-strings.txt` close CSRSyncRef.ReqItemCB Gf83a14 →
CSRItemInfo.SetItem Gaefe10, which receives the full envelope, indexes
ret_data at Gaefe36 and item at Gaefe58, clears/rebuilds its reference map and
iterates item **array** rows. Base identity is id, not ref_id.

- Required strings: **id,name,desc,thumbnail_id,effect**. String conversions
  are strict; effect must be a string even when numeric in meaning.
- Numeric fields: **rank,use_type,sell_price,collect_qty**. Numeric strings
  may be accepted by native conversions, but this is not original-field proof.
- Separate ret_data.trace[] and global_item[] collections do not supply base
  item metadata. Preserve other existing item rows because SetItem rebuilds
  the whole table; a FMD1-only replacement would regress those references.

No original final GetItem idFMD1 row was found in the already scoped original
13-table LevelDB export, recovered-reference exports or retained exact cache
key audit. The 13 exported tables have no ITEM_REF. This is a bounded absence,
not proof that every possible archive/snapshot lacks the original row.
Native IsItemData Gaf1088 tests map membership alone, so a fabricated row can
hide the missing reference without proving original semantics. See
`item-detail-null-card-classification.md` for original consumer distinctions.

## Exact original candidate artwork graphs

Source:
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/UI_ITEM.jet`.
Size **1655400**, SHA256
**4b4350559330947254764f795902b2f66ea48826290316b9eb2bd295bd446eda**.
Fresh complete24-byte-header walk reaches exact EOF with391 unique records.
Headers use uint32 packed size at+8, uint64 native base38 name at+12;
zlib body decoded read-only. No image artifacts or original mutations.

These four FMD names are **S2 sprite descriptors**, not AT animations. Each
has one image layer: count1 at S2+42, imageID uint64 at+46. Each referenced
I2 exists in the same genuine pack and decodes using established
tools/jet-viewer/jet_decoder.py decode_i2_texture; positive-alpha pixels
counted from its decoded PNG in memory.

- **IT_FMD** S2 header1649485/packed34, ID0x58bc9835 → I2
  **0x7d757213**, header1124316, **150×150**, positive alpha4652.
  Decoded S2 SHA256
  85c1fcdbd32d292b1b31902347adba5c222efb4d2fcbce271a92e9bbb9af4e0c.
- **IT_FMDXS** S2 header1649543/packed35, ID0x1f487ca8ff6 → I2
  **0x9b624342**, header1212931, **19×21**, positive alpha316.
  Decoded S2 SHA256
  85b943709336ba77893843029c6310de0077b0cc0225f9a5c7e8067cd6ca5e00.
- **IT_FMD_M** S2 header1649602/packed35, ID0x1f487ca9088 → I2
  **0x1f521fa9**, header1138451, **59×65**, positive alpha2853.
  Decoded S2 SHA256
  b9816cee3427b76f3779e94d66e96b53563981fcf55bcf50ba065b0f704b17f3.
- **IT_FMD_S** S2 header1649661/packed35, ID0x1f487ca908e → I2
  **0xf3d68775**, header1147254, **31×33**, positive alpha805.
  Decoded S2 SHA256
  822d1bc2758a7ddd36dbb815fc845201bd100e9a27ea7f88862af9d47b0fc4cc.

Original native string corpus includes IT_FMD at G1d7de96 and IT_FMD_S at
G1d83a31, in addition to FMD1 at G1d6f02c. Resource/name existence does not
prove a direct FMD1→thumbnail_id crosswalk, a preferred variant in Episode
thumbs, native CDN residency or current render. No binding is inferred from
name resemblance. No alias or texture replacement is warranted.

## Evidence needed to complete the display contract

An original final GetItem item[] row idFMD1 would directly settle all required
metadata, including the real thumbnail variant. Alternatively a bounded
original native special-case thumb producer that explicitly selects IT_FMD
for FMD1 could close the **display mapping only**; it would still not recover
unknown rank/use_type/effect/sell_price/collect_qty. No such complete producer
binding was present in the retained dumps examined by this lane.

Root can separately assess native claim receipt and free-wallet persistence
through the existing replica policy. Successful wallet credit would not turn
a locally invented display row into original metadata or demonstrate the
original server's E02 economic settlement.

## Root native producer follow-up, 2026-10-08

Read-only original Ghidra decomp retained in ghidra-episode-reward-display.txt,
ghidra-item-thumb-factory.txt and ghidra-item-thumb-display.txt. Episode popup
SetItemData Gcfb30c invokes CSRItemThumb.factory Gafa900 with the reference ID,
then SetOwnedCount(quantity), scales/shows the thumb and enables detail opening.
Factory copies that ID into CREATE_INFO, Init Gaf6f58 copies it to object+840,
loads its view, then normal LoadRes Gaf7404 (character branch only when+865).
LoadRes calls CSRItemInfo.GetItemData(object+840), then CMHashID.Set from
returned item+0x38 (puVar8+0xe) and CSRUIImageNode.LoadSprite; rank background
also comes from that returned row. This exercised producer depends on the
item reference table; no direct FMD1→IT_FMD substitution is present here.
It narrows the blank artwork cause without inventing the missing metadata.
Other independent native currency widgets are outside this bounded conclusion.
