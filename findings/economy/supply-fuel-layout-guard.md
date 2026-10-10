# Supply fuel popup: resource and child-binding guard

2026-10-04. Read-only original native evidence and LevelDB snapshots. Databases were copied to disposable Windows TEMP directories before opening with plyvel; only the copies' CURRENT CRLF was normalized. No original/selected seed edits, adb, Ghidra, APK build, or server source changes.

## Verified popup resource identity

`CSRPopUpSupplyFuel::OnInit`0xd71918 loads r1 from PC-relative literal slot0xd71924; addPC0xd7191e yields **SR_REWARD/ACTIVE** at0x1d868d6. It passes this name to framed-scene loader0xf1cc4c, which calls CMUIView::LoadView0x783e64 at0xf1cc6c. LoadView calls LoadXML0x782b18 at0x783eb0. Existing independent output `ghidra-episode-strings-06.txt:792` agrees with the manually checked instruction pair.

The shipped native vocabulary also contains **SR_REWARD/ACTIVE_CELL** at0x1d86a45. Its KO XML matches every recovered Fuel cell child name (RW_DAY, RW_IT_NUM, BG_ACTIVE, BG_DISABLE, BT_GET, TX_GET, RW_STAMP). This audit has not independently pinned its virtual cell-resource getter; do not confuse that corroboration with the directly proved popup OnInit binding.

## Original and selected seed agree

Queried these exact keys, rather than assuming absence from a substring scan:

- Preserved source: `recovered-assets/phone-2026-09-18/game-assets/UI_XML_RO.db`.
- Selected build seed: `instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db` (build script identifies this as ui_xml_seed).

Both databases return **absent** for `EN/SR_REWARD/ACTIVE` and `EN/SR_REWARD/ACTIVE_CELL`. Both contain identical KO records:

- `KO/SR_REWARD/ACTIVE`:10162 bytes, SHA256 `940feed391a6b83da1808d1d6a5a5982998238c4bd2227bf59938747ff56251c`.
- `KO/SR_REWARD/ACTIVE_CELL`:2700 bytes, SHA256 `0af916e5da9d28d93a2447f17021441e3cf6e0d7a294edd27f7e95bf90af71f8`.

Read-only extracted values: `fuel-layout-phone-13b5561694b0.xml` (popup) and `fuel-layout-phone-5ff5951a9bf5.xml` (cell), with byte-identical seed counterparts. Other emitted fuel-layout XML files are neighboring reward layouts discovered by the bounded key/value scan, not proposed aliases.

**KO popup has all four real parent bindings**. At popup XML lines76..81, nested PA_CELL_LIST panels contain PA_CELL0/1/2/3, each130x164. PA_CELL0 is `pos="0,0" align="left,top"`, with zero-alpha red debug color; native attaches the cell artwork beneath it. Its parent PA_IMG is cropped, but the cell list resides inside the defined566x525 picture panel, not an absent record. Cell XML line4 also has its own root PA_CELL0, with item/button/day/active artwork below it.

Therefore the preserved/selected **KO layout does not explain a null PA_CELL0 by missing XML child**. EN absence is proved, but selecting or failing to select the EN prefix in the *live* view remains unobserved. A rendered fuel popup does not alone prove which XML bytes or fallback locale produced it. The selected seed also does not prove the runtime downloader never replaced its view/resource bytes.

## Native branches that distinguish the two failures

`Fuel::InitCell`0xd72f78 calls GetFuelSupply, obtaining begin/end in local_34/local_30. If equal, it creates no cells. If nonempty, ordinal starts0, builds **PA_CELL+decimal ordinal**, and looks up the popup child. If that lookup returns null, it silently skips construction/InitView/Load/AttachChild for that ordinal. A received row in an HTTP response does not prove this local vector is nonempty after parser/version/date filters.

For a present child, it clears that parent's current children, creates CSRCellSupplyFuel, initializes its view, loads the corresponding INFO, then attaches it. Thus three diagnostic cases exist:

1. Local supply vector empty: no child lookup at all; resolve model/reference synchronization/date eligibility.
2. Local vector nonempty but popup PA_CELL0 null: inspect actual loaded locale/view children; selective XML alias is a possible repair only after that binding is proved missing.
3. PA_CELL0 present and vector nonempty but cell remains invisible: inspect InitView/resource key, cell view children, load state/visibility and clip/position; changing fuel JSON aliases will not prove any of those.

No APK hook or guessed JSON is justified by the current screenshot. The discriminator is a bounded read of the **actual fuel supply vector** and **actual framed popup view/child lookup result**, or equivalent existing native logs. GetFuelSupply count and child lookup must be observed together; one does not substitute for the other.

## Exact selective candidates if live EN absence is established

These are narrow candidate aliases, not changes applied here:

```text
KO/SR_REWARD/ACTIVE=EN/SR_REWARD/ACTIVE
KO/SR_REWARD/ACTIVE_CELL=EN/SR_REWARD/ACTIVE_CELL
```

Reuse the existing selective delta procedure on a new destination; preserve base SSTables and do not compact or wholesale-copy locale records. The KO popup includes text-global labels and neutral resource bindings, but compare the complete actual locale-rendered view before adopting it. Never alias DEFINE_COLOR. Any instrumented APK rebuild still requires the project's mandated release publication; this audit does not request a rebuild while model-count versus child-binding remains unresolved.

Reference evidence: `ghidra-supply-fuel-init.txt`, `ghidra-supply-fuel-ui.txt`, `ghidra-supply-fuel-ui-strings.txt`, `ghidra-episode-strings-06.txt`, and exact disposable-copy database lookups. Original balance/timer/claim values remain outside this resource audit.

## Later discriminating evidence

Parent's bounded native probe confirmed refcount1, instancecount1, local_fuel_0/AP10/status1. Parent also recovered the loader's KO fallback. **EN absence therefore does not establish the missing-cell cause and is no longer a reason to build an alias.** Keep the original absence finding as provenance only. Follow `supply-fuel-live-ui-reader.md` to observe actual child/template roots; no JSON alias or APK rebuild is proposed.

The cell's resource identity is now directly proved: make_shared0xd74dc4 loads r1 from slot0xd74e8c at0xd74dda; matched addPC0xd74dea resolves0x1d86a45 **SR_REWARD/ACTIVE_CELL**, passed to CSRUICellBase constructor0x1076f38 at0xd74dfa. This supersedes the earlier resource-getter uncertainty.
