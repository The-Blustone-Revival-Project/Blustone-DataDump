# Empty fuel activity rows: narrow native diagnosis

Read-only evidence, 2026-10-04. All addresses below are Ghidra addresses (ELF + 0x10000). No original, server, or client changes.

## Verified

- Fresh HTTP response arrival does not alone prove the reference vector was populated. However `CSRSyncRef::ReqSupplyCB` Gf84c10 forwards the full envelope directly to `CSRRefData::SetSupply`; there is no extra wrapper to invent. Source: `analysis/ghidra-supply-live-empty.txt`.
- Reference `GetActivitySupplyCnt` Gde4a5e and `GetActivitySupply` Gde4a72 both use the vector at reference object +0x2c0/+0x2c4 with stride 0x58. The actual SetSupply activity insertion uses this same vector, Gddf50c..ddf522. Sources: `ghidra-supply-live-empty.txt`, `ghidra-supply-parent-insn.txt`.
- `SetActivitySupplyThumb` Gde4146 fills reference-row thumb string +0x48 and quantity +0x54 from available group experience/gold/item/card reward. This is not a guard that suppresses fuel rows. `CSRCellSupplyFuel::Load` Gd7331c writes claim id, time window and xAP before its status switch; no thumb test gates those texts. Source: `ghidra-supply-fuel-ui.txt`.
- `CSRPopUpSupplyFuel::InitCell` Gd72f78 returns if the GetFuelSupply output vector is empty. Otherwise it builds `PA_CELL` + decimal ordinal starting at zero. If `FindCastByName<CMDrawable>` returns null, it silently skips that row (Gd7301e..d73020 branch to Gd7314e). With a container it creates the cell, initializes the view, loads the INFO and attaches it. Thus missing `PA_CELL0` alone can explain a completely empty first row. Source: `ghidra-supply-fuel-init.txt`, checked against read-only Capstone disassembly.
- `CSRPopUpSupplyFuel::OnInit` Gd71918 loads exactly `SR_REWARD/ACTIVE` via CSRFramedScene::LoadView Gf1cc4c. Original ELF literal at d61924 is 0x1014fb4; PC-relative sum with d61922 gives ELF1d768d6, whose bytes are `SR_REWARD/ACTIVE` followed by NUL. This matches the preserved UI record name.
- Preserved `analysis/recovered-data/leveldb-tables/all-tables.json`, UI_XML_RO, has `KO/SR_REWARD/ACTIVE` with actual `PA_CELL0`, `PA_CELL1`, `PA_CELL2`, `PA_CELL3`. It also has `KO/SR_REWARD/ACTIVE_CELL`. This snapshot has no corresponding EN key; the live instrumented seed may supply aliases, so absence from this snapshot is not proof of a live missing layout.
- Reload Gd719d0 always calls InitNoti, InitVIP, InitCell and InitPurchase. Periodic OnRefresh Gd71928 refreshes on the 60-second time boundary and HasRewardActivity()==1. Neither has a thumbnail condition.

## Smallest next observation

Verify the actual loaded fuel popup layout is the preserved `SR_REWARD/ACTIVE` with a discoverable `PA_CELL0`, and simultaneously read native reference activity begin/end (+0x2c0/+0x2c4) after its callback. These distinguish missing reference rows from silently missing container without guessing JSON aliases. If reference count is one and PA_CELL0 exists, observe InitCell execution/Load/attachment rather than changing the wire shape. The screenshot appearance alone does not prove which popup class or layout was opened.

## Follow-up: live model confirmed; EN absence is insufficient

Parent's fresh native probe confirms reference count 1, instance count 1, id `local_fuel_0`, AP10, status1. This excludes the empty reference vector hypothesis for that probe.

Read-only original Capstone/literal inspection proves cell template binding: Fuel make_shared Gd74dc4 passes `SR_REWARD/ACTIVE_CELL` to `CSRUICellBase(char*)` G1076f38 at Gd74dfa. Its constructor calls CMUIView::LoadViewCache G7840a4 at G1076f86. InitView G1077210 copies the existing template drawable at cell+0x830, clears current children and attaches the copy; it does not itself independently choose a locale.

**Do not infer EN lookup failure from missing EN records.** Derived game loader `CSRUIParser::LoadScript` G1087f08 explicitly has a KO retry. Normal database path obtains CGMLocalDB::GetLanguage at G1087f78, indexes a language table (ELF2186a80: 0=KO,1=EN,2=JA,3=SC,4=TC), joins `/` plus the supplied key, and calls CGMDataMgr::GetUIXML G793674 at G1088358. At G1088388..G10883a2, if the returned string is empty and language is nonzero, it resets language to zero and loops to G108826c. Consequently intact preserved KO records can service both ACTIVE and ACTIVE_CELL even without EN aliases. This supersedes any EN-absence-only hypothesis in the earlier note.

Remaining narrow observation: actual PA_CELL0 lookup result, template at cell+0x830, and whether InitView/CellLoad/attachment execute for the known nonempty row. Empty GetItemDataRefID warning is not itself a whole-row visibility guard; no ASSERT or root suppression has been proved from that warning.
