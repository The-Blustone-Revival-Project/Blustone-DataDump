# ItemDetail null card lookup and item classification

2026-10-06. Original ELF static inspection only; no device, Ghidra, source,
account reads/writes or fixes. Addresses use Ghidra coordinates.

Fault G86c328 is CSRCard.SetRefID's first LDRB from r1. The containing caller
is **ItemDetail.InitCard Gcc32c4**. It calls CardInfoContainer.GetCardData87ce64
atcc32e6 with **popup+ac string**, retains its result in sb atcc32ec, then
passes sb as SetRefID's r1 atcc33b8/cc33bc. Nullr1 therefore proves this
card-data lookup returned null, before the following sb+44 dereferencecc33c0.

**ItemDetail.Init Gcc31d8** copies two incoming strings into popup+a0/+ac.
Nonempty+ac selects InitCard atcc322e; only empty+ac and nonempty+a0 selects
GetItemDataaf109c atcc3270, then ordinary InitItemcc3cf8 (or random-box
branch for use_type30). This establishes descriptor classification, not actual
clicked identity or stale-scene causation. No RP1 wallet parser occurs here.

**CSRItemInfo.IsItemData Gaf1088 / ELFae1088** calls its
map<string,INFO>.find **af2740 ataf108e**, compares returned node with
container end **this+4 ataf1092..94**, and returns1 for non-end ataf1098,
otherwise0. It does not inspect use_type, effect, rank, resource or quantity.
Thus a genuinely registered local use_type0 display row counts as item data.
This does not prove the detail producer consulted that method or that the
clicked row was RP1; both need producer/caller evidence.

**InitItem Gcc3cf8** calls GetItemData with popup+a0 atcc3d24, immediately
copies INFO+20 as a string atcc3d2a..30, and loads ordinary
INVENTORY/INVEN_INFO atcc3f28. Separate fishing-specific layout/quantity paths
exist; their semantics are not generalized to gold. Existing item parser
contract requires strict string id/name/desc/thumbnail_id/effect and numeric
rank/use_type/sell_price/collect_qty. Membership alone is not proof all popup
resources/fields are valid. No complete InitItem decomp was available in this
bounded lane; no original RP1 definition was recovered.

Parent targets: Initcc31d8, InitCardcc32c4, InitItemcc3cf8 and IsItemDataaf1088.
For the producer, CSRItemThumb.OnProcessCursorPressaf80a4 calls its thumb+824
event pool ataf81fe; follow the registered callback from Initaf6f58/LoadView
af70a0 or actual Init callers. Do not infer an automatic server receipt defect
from a null card lookup or silently add original currency metadata claims.
