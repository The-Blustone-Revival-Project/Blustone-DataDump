# Fishing materials and local content evidence

2026-10-05. Bounded read-only final public PAD JET headers/payloads, exported localization/help and retained native symbols/original field-string candidates. No VM, Ghidra, source/original changes, fish/items/rod grants or guessed economy. G addresses are ELF+0x10000.

## Original local fishing configuration is recovered

Public **LEVELING.jet** contains native-named **FISHING**, header**7497**, packed**425bytes**, zlib-inflated**1300bytes**. Body is RW+length+UTF8 JSON. Exact top-level keys are **common1,PLC001,TUTO**. This is gameplay timing/placement configuration, not a fish catalog or reward table.

Original **PLC001.NPC1** is `{res_id:"CHIR",pos_x:-150,pos_y:50,chance:100}`. TUTO has height1..height14 (mostly610, height5..9=680,height10=600). common1 includes touch_delay0.1,touch_dir_change1.0,rage_delay0.3,success_wait0.8,gage_hide_interval0.1/count6/start0.6/speed10.0,low_speed3/high_speed3,add_speed_min35/max90,short/middle/long_ratio100,alert_time0.5,dir_same_ratio0.6/dir_not_same_ratio1.2,dir_time_min1/max4,wait_time{min1,max4},bite_time{min1,max4},escape_time{min5,max5}. Numeric scalar strings are preserved as originally serialized; this report does not assign unproved units/formulas or server-random sampling rules.

Retained **CSRStaticData.LoadFishingSetting Gf3cb04** and original bounded field scan yield local loader name **fishing**, prefix **common**, place prefix **PLC00**, NPC prefix **NPC**, and keys res_id,pos_x,pos_y,chance. Parent must recover exact dynamic suffix construction before interpreting common1 or manufacturing aliases. GetLoadFishPlaceInfo Gf419b4/GetLoadFishNPCInfo Gf41af8 are actual local model consumers. **PLC001 is a genuine configuration key**, not a guessed API area record or proof of a presently accessible native spot.

## Fish/area art: exact resource names, not API IDs

All inspected packages walk exactly to EOF with native24-byte header/uint64 base38 naming:

- **FISH_LIST.jet**:562972bytes/90records. Named fish sprite families **FS001..FS011**; common variants _S,_V,_S_V exist but are not uniform (FS002 only FS002/FS002_V). **TS001..TS005** also exist. FS001 header560357, FS011 finalnamedrecord. These are resource descriptors, **not recovered /fishing fish_id values or item IDs**.
- **FISHING.jet**:1054020bytes/181records. Named UI/art includes F_ANI_BG,F_WAIT_ANI,F_PICK_ANI,F_GA_RED_ANI,F_GA_FI_ANI,F_ALERT_ANI,F_GA_GRE_ANI,F_SHORT,F_NEWRE,F_ICON and gold/silver indicators. No JSON/text catalog was found among its decoded records.
- **MGM_FISH.jet**:4240113bytes/530records. Named **FMAN_BG,FMAM_BG,FMAN_FI,FMAN_THDW,FMAN_READY,FMAN_START,FMAN_SUC**, FMAN_LUSG*,FMAN_THBGS/M/L and **CHIR** withCHIR_01..07 sprites. These support original fishing actor/scene art. No JSON catalog/reward/recipe declaration was found among its decoded records. Names resembling fishing rods do not establish equippable rod item IDs.
- Original **CUT_FISH.jet** and **MP4_FISH.jet** also exist; existence alone is not a required binding or reward definition. No media extraction/preview was performed.

Preserved UI_TEXT_RO key **미드가드 얼음낚시터** has EN **Midgard Ice Fishing Area**. This is an exact original area label, but its binding to place_idPLC001 has not been traced. Neither the resource filenames nor the shared Midgard wording justify an invented area/ref row.

## Bait and rod identity limits

Final localization gives **일반 미끼 = Average Bait**, **고급 미끼 = High-quality Bait**; UI_JSON labels TX_FI_BA1/TX_FI_BA2 agree. Original ELF includes literals **BAIT1/BAIT2** and controls BT_BAIT1/BT_BAIT2, while UI_ITEM resource inventory contains **BAIT01_L/M/S and BAIT02_L/M/S**. These are distinct namespaces/spellings: **do not identify BAIT1 or BAIT01 as a /reference/GetItem.id without its native lookup/row proof**.

Actual native purchase seam is **CSRSceneMFishing.RequestBuyGlobalItem(LURE) Ge6e724**, entered by its normal controls; UpdateBait Ge6ea48 and CSRMFishing.GetBait Gb2efd0 are precise parent-only targets. The current evidence does not recover original item use_type/effect/collect_qty or bait prices/quantity. There is no published full original ITEM_REF in the13-table export, and no original rod item/upgrade/recipe declaration was recovered in this bounded unit. Do not invent a rod reference or claim rods absent from all historical game versions.

## Primary gameplay/reward declarations, with version separation

Original final **UI_CSV.jet namedHELP_DATA** (header516,packed85055) contains **CONTENTS10_1..10_8**. It says fish can be sold, Average/High-quality bait are immediately purchasable at fishing areas, throw distance changes possible fish, bites need hook timing, tapping during fish fury snaps the line, and gold/silver crowns indicate larger/more valuable catches. **CONTENTS10_8** explicitly says bait is consumed if failing/canceling **after a bite**, but may be withdrawn before then. These are primary original gameplay rules; they contain no exact price, fishID, bait consumption quantity, numeric size/rarity threshold or catch-pool probabilities.

VSFan archived1.4.4.1 help has analogous10_1..8 text, but its throw action description differs from the final help (older charge/click versus final press/release). Use final original instruction wording for final-client behavior, not a blanket historical merge. The community FAQ's targeted human-text fishing hit is an event mention; base64 picture rows were not read or used as numeric evidence.

The recovered fishing schema vocabulary includes **place_id,fish_id,/fishing/Begin,/fishing/EndWithSell,/fishing/GetRecord,/fishing/GetInven,/fishing/SellFish,/fishing/GetPriceRef** and exact retained string `fishing/GetFishingPool`. Those literals locate protocol; they are not a complete response or an invented leading-slash correction. **CSRMFishing.ParsePrice Gb2e438** reads fish_id and b_price/s_price/g_price through original candidates, suggesting grade-specific sale price rows but not any amounts. **ParseBegin Gb27d34** reads log_id/init_val/max_val/dec_val/inc_val/dec_val_on_burn and burn/timing ranges; this is server-provided gameplay state, not a recovered fish definition. Parent's exact containing callback/parent decomp is required before publishing a minimum schema.

## Finite next proof

A usable original local FISHING configuration and substantial exact art are present. **Actual fish IDs, original bait/rod item definitions, full pool/price rows and recipe/reward quantities remain unrecovered.** Narrow native parent targets are LoadFishingSetting Gf3cb04, RequestBuyGlobalItem Ge6e724, ParseBegin Gb27d34 and ParsePrice Gb2e438 plus the actual GetFishingPool/Record/Inven callbacks. Preserve separate resource/API/item identities and the original bite-dependent bait-loss rule. No grant, recipe, price, fish stat or runtime fishing acceptance was fabricated.
