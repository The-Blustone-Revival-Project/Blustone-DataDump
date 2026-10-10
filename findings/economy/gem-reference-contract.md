# Final28010 Gem/Jewel parser contract

2026-10-05. Read-only original ELF Thumb/branch tables and parent's completed ghidra-gem-reference.txt/-keys.txt. No Ghidra, VM, source edits, inventory grants or historical balance imports. Code coordinates are Ghidra addresses (ELF VA plus10000hex).

## Five reference responses are direct ret_data collections

The original routes and parser/callback identities are:

- **/reference/GetGem**: ReqGemCB **f84e54** passes the full parsed envelope into **CSRGem.ParseGemRefs a535e8**; it extracts ret_data at a5360e and iterates reference rows.
- **/reference/GetGemCombinationEffect**: ReqGemCombiEffectCB **f84e76** passes the full envelope into **ParseGemCombineEffects a53a90**, which extracts ret_data at a53ab6 and iterates rows.
- **/reference/GetGemSellPrice**: ReqGemSellPriceCB **f84e98** -> **ParseGemSellPrices a53e50**, ret_data ADDa53e7a.
- **/reference/GetGemLevelUpPrice**: ReqGemLevelUpPriceCB **f84eba** -> **ParseGemLevelUpPrices a54108**, ret_data ADDa5412c.
- **/reference/GetGemDisassemblePrice**: ReqGemDisassemblePriceCB **f84edc** -> **ParseGemDisassemblePrices a54528**, ret_data ADDa54546.

An honest empty reference reply for each is **{result_code:1,ret_data:[]}**. Do not add gem[], stat[], price[] wrappers or pass only ret_data into a helper whose native callback actually passes the full envelope. Successful GetGem and Combination callbacks check GetResultCode1, then tail-call their parsers. These routes are part of the generic reference dispatcher; a distinct per-route requester/extra form-key schema was not recovered in this bounded task, so do not invent a gem-specific request payload beyond actual captured/common reference evidence.

## Gem definition fields and types

ParseGemRefs reads each row directly:

```text
id            STRING  ADDa536b6
name          STRING  ADDa536c0
desc          STRING  ADDa536c6
res_id        STRING  ADDa536cc
set_effect_id NUMERIC ADDa536d2
rank          NUMERIC ADDa536d8
target        NUMERIC ADDa536de
```

id/name/desc/res_id use from_json<string>. set_effect_id and rank use unsigned scalar conversion; set_effect_id is **not a string** (a preliminary message incorrectly grouped it with the4 strings; this report corrects that). target numeric values below4 map to internal target-1:1..3 become0..2,0 becomes-1. Do not claim the named equipment-slot meaning of all3 values without its consumer evidence. Rows are stored as INFO vector entries; ref_id is not the reference identity key here.

No exported **CSRGem.ParseGemStats** symbol or /reference/GetGemStats route was found. The relevant set-stat helper is **CSRCardStat.parse886fc0**, while individual owned gem abilities are parsed by **CSRGem.parse a5d3dc**. This distinction prevents inventing a missing stats endpoint.

## Combination effects: percentage processing and actual application

ParseGemCombineEffects rows have **numeric id** (ADDa53b78) and **numeric count** (ADDa53bf6), then pass the **same row object** to **CSRCardStat.parse at a53c46 withmode1**. Stat fields are direct siblings, not nested stat. Shared CardStat keys include rank,awk_step,hp,atk,def,spd,crt_chance,crt_dmg,penetration,block_chance,block_dec_dmg,attr_enhance,attr_resist,hp_regen,hp_up,atk_up,def_up; the shared parser's numeric-stat values are read as **strings** into floating_point values, e.g. def from_json<string>88710e/create887120. Publishing numbers instead of numeric strings for these fields is not proven compatible.

The combination parser explicitly creates floating_point100 repeatedly and **divides8 selected stat components by100** at a53c70,a53c9a,a53cc4,a53cee,a53d18,a53d42,a53d6c,a53d98. At least hp/atk/def normalization is pinned by destination layout: CardStat.def+38 is the normalized effect stored in the card's set-effect stat. Do not treat every stat component as an unscaled flat increase merely because it shares CardStat's parser. Conversely the exact percentage-point versus multiplicative treatment of every chance/resistance component was not fully audited here.

**Actual DEF multiplication is proved**, not inferred from UI labels. GetAddedStatGemSetEffect **86bfe0** copies Card+178 stat. Its DEF component+38 is therefore Card+1b0; **GetDef869fd4** loads its decimal floating value at86a00e..86a036, computes the fraction into **s22 at86a09e**, loads baseDEF from Card+660 at86a0f0, and applies **baseDEF*s22 through VMLA at86a100** before adding other contributions. Thus a combination row def:"100" becomes1.0 and adds100% of baseDEF; it is not a flat+100DEF. Ordinary gem stats copied from Card+270 are separate additive components. Avoid generalizing this confirmed DEF arithmetic to every other field without its exact getter.

**CSRCardAnalyzer.SetEquipGem86efd0** collects ordinary gem stats, calls CalcSetEffect **a5f5c0 at86f07e**, sums returned set-effect stat records at86f098 and stores them with SetAddedStatGemSetEffect at86f0a6. CalcSetEffect's exact duplicate-set/count-tier stacking policy still needs complete consumer review; count is a required pieces threshold, but original final set sizes/bonuses are not recovered from a2017 guide.

## Gem effect-stat IDs: independent vocabulary

**GetGemEffectName a600b0** subtracts1, bounds12, and uses its original TBB table. The12 branches resolve Korean localized gem effect names. Their exact numeric meanings are:

```text
1 HP                 2 ATK                 3 DEF
4 Critical chance    5 Critical damage     6 Block chance
7 Block damage reduction
8 Attribute enhancement                   9 Attribute resistance
10 Attack speed      11 Natural HP regeneration
12 Penetration chance
```

Branch arms are a600cc,a600d8,a600e4,a600f0,a600fc,a60108,a60114,a60120,a6012c,a60138,a60144,a60150. Values0/>12 take the blank/error display branch. This mapping is **not SRSKILL.target_stat**, whose1/2/3 meanings differ. No original2017 percentage values or drop tables were imported.

## Price-row fields

The completed reference dumps prove direct rows:

```text
SellPrice: rank,level,price_type,price
LevelUpPrice: level,price_type,price,possibility,failed_compensation,add_sub_ability
DisassemblePrice: level,price_type,price
```

These are recovered numeric field identities, not original fees, probability units or charge-currency policy. Their complete enum values/tier fallbacks remain unproved here. Keep price rows empty until implementing those mechanisms with explicit local fixtures; an empty reference does not authorize fake successful Sell/LevelUp/Equip responses.

## Owned inventory is an array, not a currency counter

**/lobby/GetGemInven** completion **CSRInstanceSync.ReqGemInstCB ae619c** checks success and passes the **full envelope** to **CSRGem.ParseGemInsts a5c090**. That helper extracts ret_data at a5c0ae and iterates gem-instance rows into **CSRGem.parse a5d3dc**. Therefore an account with no actual jewels must receive **envelope([])**. Legacy local game.gem numeric balance and gem_free/gem_paid are not gem-instance records; publishing their object as this response is a schema error and may pass primitive values into the instance parser.

The nonempty instance parser reads ref_id:string, inst_id:uint64, rank,level,position,target_inst_id,ability,abilities,level_up_failed,main,sub. Full ability nesting/value types and equipment attachment semantics remain unresolved; no owned instance should be synthesized just to make the page nonempty. Empty inventory and empty5 reference arrays are an honest minimal initial seam until references/stat/equipment contracts and earned acquisition are implemented.

Original final28010 set magnitudes, owned jewel catalogue, tier probabilities and reward economy remain missing. Native jewel UI/reward application was not tested by this lane. Remaining narrow parent targets: CSRCardStat.parse886fc0, CalcSetEffecta5f5c0, CSRGem.parsea5d3dc and GetAffectedEffecta5f400 to close every ability/unit/stacking rule before populated data.

## Source review of empty baseline

The inspected game-routes.ts now returns empty arrays for all5 reference routes. state.gemInventory authenticates and returns envelope([]), leaving legacy scalar game.gem intact rather than fabricating owned instances. unavailableGemAction authenticates and returns non-success2001 for /gem/*; no grants/economy/mutation were added. These changes match the minimal parser shapes. Fresh ghidra-gem-inventory.txt/-keys.txt independently corroborate ParseGemInsts ret_data and the per-instance key names. No native page/test was run by this review lane.

One concrete refusal-coverage gap was reported: **CSRGem.RequestGemEquip a557cc** uses **card_handler/EquipGem** (LDRa55e0c/ADDa55e0e), not /gem/Equip. Its request fields include target_inst_id, combination, price_type and weapon/armor/accessory collections. The initial new /gem/* refusal does not catch canonical **/card_handler/EquipGem**, which still reaches the generic mock in the inspected source. Add an explicit authenticated refusal for that actual unreconstructed mutation route; do not invent an equip success just because inventory is empty. Fix status was not assumed at this audit point.
