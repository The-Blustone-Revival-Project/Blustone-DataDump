# Gem set evidence crosswalk: final-client names versus historical balance

2026-10-05. Read-only VSFan handoff/source documents, archived1.4.4.1 help JSON, preserved final-client UI_TEXT_RO/export and original final ARM helper. No VM, server/stat pipeline changes, grants, new strict coverage credit or source mutation.

## Sources and version limits

- Historical early asset captures: VSFan `Extracted Assets (2026)/1.1.2.0 (blustone.pcap, 2017-09-04)` and `1.1.3.0 (bs_transcendence.pcap, 2017-09-08)`. Those are2017 asset/protocol versions; they are not final2.8.0.1 balance references.
- Actual complete set-bonus text source: **analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/3d98d128.json**, article **CONTENTS11_8** (Set Effect). Archived APK is independently identified in vsfan-extracted-assets.md as **1.4.4.1/code1441**, hash0fbd1e08dc6e0dbdf9ecf972552c9de52fc4fd86b4b573af52935e8296199f4a. Do not label that article2017 merely because neighboring captures are2017. Its157-row JSON needs one in-memory removal of the final dangling comma; original untouched.
- Final-client vocabulary/parser evidence: original2.8.0.1 ARM GetGemEffectName plus preserved **analysis/recovered-data/leveldb-tables/all-tables.json**, UI_TEXT_RO. These support exact final localization keys/names and wire field semantics. They contain parameterized display templates, **not final numeric combine-effect rows**.
- FAQ images10/11 and mounted-jewel samples remain observation sources already documented in GEAR.md. The FAQ's Super Block5% is a separate author list/observation, not a recovered final server table. No new strict credit is assigned here.

## Exact native name-selector IDs and crosswalk

Original **CSRGem.GetGemEffectName Ga600b0** takes unsigned selector inr2, subtracts1 atGa600b6, checks<=11 atGa600b8, then TBB atGa600bc. Direct original12-byte branch table atELFa500c0 was decoded, followed through each exact LDR/ADD string sequence and matched to final UI_TEXT_RO records. This supplies a real native1..12 **effect-name selector** domain, not an inferred ordering from historical prose:

- **1**: key `체력의 보석` → EN **HP Jewel**, KO생명의 결정; historical2-piece HP+5%.
- **2**: key `공격의 보석` → **Offensive Jewel**, KO공격의 결정; historical2-piece AP+5% (raw archived abbreviation).
- **3**: key `방어의 보석` → **Defensive Jewel**, KO방어의 결정; historical2-piece DP+5% (raw archived abbreviation).
- **4**: key `치명타 확률 증가 보석` → **Critical Jewel**, KO치명의 결정; historical2-piece critical chance+4.5%.
- **5**: key `치명타 피해량 증가 보석` → **Fatal Jewel**, KO충격의 결정; historical4-piece critical damage+50%.
- **6**: key `막기 확률 증가 보석` → **Block Jewel**, KO막기의 결정; historical2-piece block chance+4.5%.
- **7**: key `막기 피해 감소량 보석` → **Reduction Jewel**, KO철벽의 결정; historical **Super Block Jewel**,4-piece KO9% versusEN/JP/SC/TC5% conflict.
- **8**: key `속성 강화의 보석` → **Element Jewel**, KO속성의 결정; historical4-piece elemental enhancement+23.
- **9**: key `속성 저항의 보석` → **Resistance Jewel**, KO저항의 결정; historical4-piece elemental resistance+23.
- **10**: key `공격 속도 증가 보석` → **Speed Jewel**, KO속도의 결정; historical4-piece attack speed+1.72.
- **11**: key `자연 회복 보석` → **Regeneration Jewel**, KO재생의 결정; historical4-piece HP regeneration+30.
- **12**: key `관통 확률 증가 보석` → **Penetration Jewel**, KO관통의 결정; historical4-piece armor penetration+12.

Native branch addresses for selectors1..12 respectively: **Ga600cc,d8,e4,f0,fc; Ga60108,14,20,2c,38,44,50**. Bounds-excluded inputs take the default string pathGa60162. Parent may inspect the helper/callers if promoting selector IDs into actual API data. **A name-selector ID is not itself proof of an original gem-reference string ID or rank/target/kind field.** No invented `GEM001`, `G01` or gem rank/slot is derived here. In particular historical help order puts Block before Fatal, but native selector IDs are **5Fatal/6Block**: historical list position is unsafe as an enum.

## Super Block discrepancy remains numeric, not identity

Archived1.4.4.1 CONTENTS11_8.desc2.ko literally uses `철벽의 결정 - 4개 장착 시, 막기 피해량 9% 증가`. EN names it Super Block Jewel and says Damage Reduction Rate Increase5%; Japanese and both Chinese descriptions also say5%. The final preserved native name is **Reduction Jewel** using the same Korean family철벽의 결정. Thus historical Super Block and final Reduction have a strong **identity/terminology** crosswalk, while the old localized numeric inconsistency remains unresolved.

Final UI_TEXT_RO key **[세트효과]막기피해%s%s** says EN `Mount Reduction Jewel %s, Damage Reduction %s%% ▲`; KO likewise inserts count and magnitude placeholders. Neither locale hardcodes9or5. The preserved final text therefore **does not choose a correct old translation, prove a final rebalance, or support current9%/5% backend logic**. Use recovered final numeric server reference rows when available, or label a deliberately chosen value as a local fixture; never claim majority-language voting establishes original balance.

The eleven consistent historical values also remain **historical** even though names/12-family structure match final UI. Values+23 in old help clarify that source's set text, but do not retroactively resolve ambiguous decimal placement in separate jewel-instance screenshots or final stat conversion units.

## Final native reference shape versus missing data

Parent's **ghidra-gem-reference.txt/-keys.txt** proves **ParseGemRefs Ga535e8** reads envelope.ret_data and reference fields **id,name,desc,res_id,set_effect_id,rank,target**. `id` is a string gem-reference identity; `set_effect_id` is a separate numeric selector/reference. **ParseGemCombineEffects Ga53a90** reads rows with **id,count** and passes the same row into **CSRCardStat.parse** (parent dump line547). Count/stat-effect fields, not the help text, determine live set magnitude.

No original full GetGemRefs/CombineEffects rows were present in the inspected recovered-reference export directory or13-table all-tables export. Existing helpers/localization are enough to restore labels/schema, not original per-rank gemID/resID mappings, mount targets, rolls, sell/upgrade prices, stack calculation or numeric bonuses. Full original final rows must be sourced independently before claiming a reconstructed balance table. `target` may encode slot eligibility; this report does not rename it `kind` or assign its numeric meanings without its consumer proof.

## Safe use in final-client revival

Use exact final names, localization keys,12selector domain and native parsed field names as final-client compatibility evidence. Keep historical1.4.4.1 bonus counts/magnitudes in a separate provenance layer with the Super Block conflict intact. Keep reference string IDs, effect-name selector IDs, set-effect IDs, rank and target/slot domain distinct until native caller/reference data closes them. This unit changes no stats, pipeline or strict-coverage ledger and grants no equipment.
