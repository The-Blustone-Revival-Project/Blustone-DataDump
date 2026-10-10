# First Episode combat CB0101: original actors and assets

2026-10-05. Read-only original R_EPISODE-derived exports, original PAD package header/payload inventory, preserved localization and existing native/environment reports. No server/client/VM/Ghidra/original mutation. These stats are **scripted Episode actor stats**, never ordinary hunter baselines.

## Original combat and participant identities

`analysis/recovered-reference/EPISODE_COMBAT_CB0101.json` defines idCB0101/titleE01_TITLE/stage_nameE01_S02_TITLE/power"1500", **game_res_id"99", bgmBGM_TRAIN, field_bg_resBG_RES**. Win/lose/lose2 all name **EP_0302B**. Left is CB0101_009_1 with thumblevel15/rank2/hyper0/attr3 and skill flags[1,0,0,0,0]. Right is CB0101_003_1 with thumblevel1/rank3/hyper0/attr2 and skill flags[1,1,0,1,0]. These are native script participants, not owned-card grants or a replacement saved deck.

**009 is Captain**, exact original CHAR_STR_RO key009|TITLE ENCaptain. Its original009|SUMMARY describes Defense with armor penetration. Do not substitute alternate009_1, whose separate original title is Eternal Flame. ActorSTAT ref009/resC009/attr3/role2 agrees with the original Defense role. Ref003 has original title Walking Disaster and a Defense summary (community hunter name Nene is a separate provenance).

Both exact actor IDs are present in `EPISODE_STAT_ACTORS.json`:

- CB0101_009_1: ref_id009/res_idC009/attr3/role2/cool_time5000. stat rank"2", hp"323", atk"229", def"320", spd"7.00", crt_chance"11.00", crt_dmg"183", penetration"1.00", attr_enhance"0", block_chance"27.00", block_dec_dmg"52", attr_resist"7", hp_regen"9".
- CB0101_003_1: ref_id003/res_idC003/attr2/role2/cool_time5000. stat rank"3", hp"514", atk"333", def"394", spd"7.00", crt_chance"12.00", crt_dmg"180", penetration"0.00", attr_enhance"0", block_chance"29.00", block_dec_dmg"50", attr_resist"8", hp_regen"17".

Use these only through the native Episode actor path; no global GetCard rank/stat rows were altered.

## Exact Episode skill payloads, not ordinary-level formulas

Captain's actor has one skill record: type1,target_rank1,cool_time5000,cost3. Its one effect has **effect_type1,target_type1,target_stat1,refer_target_type1,refer_target_stat1,base_number-1600,duration0,interval0**. Original actor JSON does not include icon_id/cut_in_id/value_up fields. Missing fields must follow the actual Episode parser's defaults rather than fabricated ordinary-skill records.

Opponent003 actor has:

- type1,target_rank1,cool_time5000,cost3,crt_chance100; effect_type1,target_type1,target_stat1,refer_target_type1,refer_target_stat1,base_number-1800,duration0,interval0.
- type2,target_rank2; effect_type4,target_type1,target_stat15,refer_target_type2,refer_target_stat0,base_number100,duration2500,interval0.
- type4,target_rank4; effect_type1,target_type2,target_stat1,refer_target_type1,refer_target_stat6,base_number100,duration3100,interval1000.

The scripted participant explicitly flags slot4 enabled despite thumb rank3. Do not enforce ordinary owned-card eligibility over this serialized Episode actor without inspecting the native script consumer. These are exact serialized values; this report does not invent damage scaling, cooldown units or an original training level.

Separately, preserved SKILL_REF_RO009|1|0 says active skill uses3Rage.009|1|1 says frontline damage penetrates Immunity and stores formula `-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000`;009|1|2 describes prohibiting immunity. These ordinary descriptive rows are useful corroboration of character mechanics, **not authorization to transplant all modern ordinary effects or substitute that formula into the simpler Episode base_number payload**.

## Positive original C009 resource coverage

Current opt-in `tools/episode-resource-profile.ps1` already selects C009.jet/C009_Q.jet/C009_EFT.jet/C009_SND.jet. Original files: base3101288bytes, Q50218, EFT1616214, SND142949. Base outer records are C009,C009_A,C009_B,C009_D,C009_D2,C009_D3,C009_D4,C009_DA,C009_DB; complete walk ends at EOF.

C009_B animation event text positively references **C009_E01/E02/E03/E04/EC** and **C009_SND01..09**. EFT package has all five exact video names plus their _A companions; SND contains all9 exact named sounds. This closes those original animation-event dependencies. Q thumbnail/icon records and C003 family assets exist; C003 is covered by the established starter-card profile rather than newly supplied actor statistics. Art availability is not proof an Episode actor was instantiated or activated a skill.

## Stage99, background and audio

Original **BGM_TRAIN** is a native named outer resource in **SND_CDN.jet** at header6514908, packed929968bytes. The opt-in Episode profile already includes SND_CDN. **EP_0302B** exists in DIAL-EN.jet at header2430912/packed1418, already selected by that profile.

Original `analysis/recovered-data/environments.csv` row99 is:

```text
99,배틀,STI099,111,-5,160,11,-10,273,111,20,648,111,30,840,111,-5,1000
```

Existing environments-recovery.md proves this LEVELING-derived environment table's native loader/three-string-plus-five-depth-band schema and STI099 art-family relationship. **ST099.jet** is1252287bytes, SHA256e99d2c7df04f4c32f539d4b79d44791a69f97046dd61b48d4a89211a72f50e81,25records with exact EOF walk. Named art includes ST099_BG, STI099B_01, STI099_A01..E01, UI_IG_FT_BG1/DR1 and AT **ST099BG, STI099B, STI099_A1..E1**. This is positive original stage99-family coverage. Current12-pack Episode profile does **not** explicitly select ST099; its native inclusion/loading is therefore a next opt-in profile check, not a runtime absence claim.

A bounded exact outer-name scan of all774 original public PAD JETs finds **no BG_RES** and no literal outer"99"/"ST099" resource. This does not invalidate the independently recovered STI099/ST099BG family or prove BG_RES an ignored sentinel. **Whether field_bg_res is parsed/used here and how game_res_id"99" selects UI/environment are native consumer questions still unresolved in this unit.** Do not create a resource alias named BG_RES or rename ST099BG to it from the shipped combat string alone. Existing UI_XML/UI_JSON export has no ST099/99 layout-key match in this bounded scan; stage art and layout namespaces are separate.

## Narrow next work

Preserve original CB0101 script/actor stats and all skill flags. Parent should verify Episode COMBAT parser's game_res_id/field_bg_res consumers and constructor/default fields, check opt-in ST099 inclusion through the normal CDN lifecycle, then use the original Episode participant path. No extra ordinary009 grant/reference expansion, stat merge, fictitious rewards or live battle was performed. Positive file/name coverage does not establish native CB0101 readiness or a complete Episode campaign.

## Follow-up: native background correction and exact LEVELING_E availability

Parent's fresh first-combat contract closes the earlier background uncertainty: original COMBAT constructor **does not read field_bg_res**. It reads game_res_id as a strict string at Gb14168/from_jsonGb14176 and stores COMBAT+24. SceneMEpisode.InitBackground Gb23e80 passes that string directly to **CSRGameBase.OnInitBackground G9cbf34 at Gb23ecc**. Thus **"99"→original ENV_INFO99→STI099** is the actual background path. The shipped unused field_bg_res:"BG_RES" is not an additional resource requirement or an alias to fabricate. This supersedes the unresolved field_bg_res paragraph above; outer BG_RES absence is immaterial to this proved path.

Original public **LEVELING.jet** (PAD assets) is **18524bytes**, SHA256 **ba73fff17002cc94f7f1a98bf657be1bef042283051a5b92c395347006d3c57e**. Exact24-byte header walk has21records and ends at18524. **LEVELING_E** is its **zero-based record11**, header offset**10309**, compressed body starts**10333**, packed size**930**. Header+12's uint64 decoded through the native base38 alphabet yields **LEVELING_E** itself, not a filename-derived guess. Zlib body inflates to **3987bytes**, starts RW + little-endian body length + UTF8 BOM JSON at+6; full inflated SHA256 **9286d223afc9d7c781544bd649cb8934efb200ef704fd4dd97caa5d6a00af8a8**.

The recovered JSON has38 top-level combat-mode keys and is **local Episode combat configuration**, not character EXP/level curves. Exact examples: play_time300, global_skill_cool1.0, sp_increase_spd_per_sec0.03, sp_increase_per_kill0.5, sp_increase_per_atk0.04, sp_increase_per_dmg0.04, sp_max10; left.first_sp2/right.first_sp1.8. It includes actor,left,right,waiting,bonus motion/camp/stat factors. No values were patched or substituted into a different mode. These are original serialized field values, not a claim that native runtime has loaded them.

Existing `leveldata-id-source.md` and parent's `episode-first-combat-contract.md` prove **InitBeforeOpen Gb23c38 loads local leveling_e through DataMgr.LoadLevelData at Gb23c5e**. The shared native resource lookup uppercases ASCII keys (episode-native-resource-loading.md), so original named **LEVELING_E** satisfies that spelling through existing native lookup; no duplicate lowercase descriptor needed. It is available inside original **LEVELING.jet**; the12-pack Episode-extra list itself does not explicitly add LEVELING. Whether the established battle profile already registers this original pack must be checked against the actual resource profile/native loader, rather than inferred from the curated JSON exports.
