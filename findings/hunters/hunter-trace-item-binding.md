# Hunter trace item identity is assigned by item post-processing

2026-10-04. Read-only original Thumb and existing native-card/bootstrap/item schema evidence. No original/server/client/adb/Ghidra edits.

`SearchStuff::SetCardBook` reads CSRCardInfo+0x18 as the argument to Inventory.GetInstItemCnt. This is **not base.id/char_id automatically**. SetCard allocates0xc4 bytes including shared control; actual info object is allocation+0xc. The queried member is allocation+0x24. SetCard initializes that member empty and does not derive an item-ID alias from the hunter ID.

The writer is **CSRCardInfoContainer::PostProcess G87d348**:

- G87d360/G87d364 gets CSRItemInfo/GetItems and traverses item map nodes.
- G87d382..386 tests node+0x20==3, the item INFO.use_type field (value starts node+0x1c).
- G87d388 copies node+0x60, which is INFO.effect at+0x44, then G87d396 looks up the hunter reference map with that string.
- On a matching reference, G87d3a0 retrieves node's shared CSRCardInfo pointer. G87d3a2 source=node+0x10 (the item's own map key/base.id); G87d3a6 destination=cardInfo+0x18; string assign G87d3c2 copies the genuine item ID.
- G87d3c8/G87d3ca copies node+0x28 (INFO.collect_qty) to cardInfo+0x4c.

Thus the structurally required original row for hunter005/006 is a `/reference/GetItem` base record with **use_type3**, **effect string equal to hunter reference base.id**, and its **own original base.id as trace item ID**. The map compares the effect to card reference identity, not char_id. Explicit original ID is required before describing trace metadata as recovered.

Existing shop-fuel-contract.md proves base.effect is string and native INFO.effect+0x44 (short-string bytes+45 or heap pointer+4c); this independently corroborates node+0x60 arithmetic. SetCard's base id/char_id/res_prefix literal stores in native-card-bootstrap.txt are separate fields, not this trace binding.

Original trace item IDs for005/006 are **unresolved**. `analysis/recovered-data/leveldb-tables/all-tables.json` and recovered-reference manifest expose skill/tag/char/UI data but no ITEM_REF table; no item row was found in these bounded preserved sources. Do not publish005/006 themselves as assumed trace item IDs. Source catalog hunters can remain without original trace metadata; any deliberately local trace-ID fixture must be explicitly labeled local and should not be confused with recovered original collection identities.

Small parent proof dump if needed: PostProcess **G87d348..G87d3da** (first trace-binding loop). SetItem **Gaefe10** exact base schema already documented; no broad Ghidra run is needed to establish the writer.
