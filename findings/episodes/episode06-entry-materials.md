# E06 original entry and complete material audit

2026-10-08. Read-only PAD/JSON audit; only this report written. Native E06 entry/residency/combat/progress/reward pending. Compare root-stated full E05 profile (132 groups, all88 E04 assets plus nine original E05 packs).

Continuation evidence (2026-10-09): AGENTS sections173..177 verify nativeentry/
S01..03clears, CB0601WIN andCB0602body/cut-in/nativeLOSS. Pausedobserver177 verifies
actualCB0602enemyserials6..9M024 and10C040camp1/sameSource, fixedKarl5camp0.
Dino portrait/S04win/remainingstories/reward stillpending; originaldata unchanged.

## Original progression

Reward `{"item": [{"ref_id": "OV1", "qty": 10}], "free_iap": 0}`. OV1×10 identity/quantity recovered; metadata/native settlement unknown. No grant.
- E06_S01: EP_1201B, battle=False, {"localname": "local_GREYWOOD", "x": 860, "y": 1130}; portrait C003_DIALOG.
- E06_S02: EP_1201C, battle=True, {"localname": "local_3BEAR", "x": 790, "y": 1050}; portrait C003_DIALOG.
- E06_S03: EP_1203A, battle=False, {"localname": "local_3BEAR", "x": 790, "y": 1050}; portrait C003_DIALOG.
- E06_S04: EP_1204A, battle=True, {"localname": "local_GREYWOOD", "x": 860, "y": 1130}; portrait C005_DIALOG.
- E06_S05: EP_1301A, battle=False, {"localname": "local_CAMP", "x": 900, "y": 1210}; portrait C005_DIALOG.
- E06_S06: EP_1302A, battle=False, {"localname": "local_CAMP", "x": 900, "y": 1210}; portrait C005_DIALOG.
- E06_S07: EP_1303A, battle=False, {"localname": "local_REDHILL", "x": 1080, "y": 1140}; portrait C005_DIALOG.

CB0601 stage_name E06_S05_TITLE disagrees with actual S02 link; CB0602 E05_S05_TITLE disagrees with actual S04. Follow original links.

## Full dialogue paths

### EP_1201B

Header2521435/packed2396/RW33059 SHA256 `85d7d68dfb2ad48ba3de90a073f9e0e78e93b24abb1f3ac29874e569c9a8cdcd`. 22 nodes/19 texts. Path 0→1→2→21→3→4→5→6→7→8→9→10→11→12→13→14→22→15→16→17→23→20.
First node2 %user_name%: Karl, I have a question for you...
**Final node23 %user_name%: Three... bears?**
Terminal20: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
`.
Speakers %user_name%/Char009, Karl Steiner/Char012, Tyltyl/Char004, Bear/Char036.
Dependencies BG007_1.

### EP_1201C

Header2523855/packed2787/RW42400 SHA256 `1ca8267165d455a93757111874f909d71255f2f32eabe8606ef3b0948f99d4df`. 29 nodes/25 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→14→17→18→19→20→21→22→24→25→26→27→28→29→30→23.
First node2 Karl Steiner: This is the cave where the three bears live together.
**Final node30 Karl Steiner: I will fight with you guys.**
Terminal23: `scr-fade duration:0.6 color:(0,0,0,0)
wait duration:0.6
combat_goto id:CB0601`.
Speakers %user_name%/Char009, Tyltyl/Char004, Karl Steiner/Char012, Bear/Char036.
Dependencies BG900_1, BGM_COMIC1, BGM_TRAIN.

### EP_1203A

Header2528157/packed2452/RW35994 SHA256 `52cceb6b7912b38045136683612d0f831d1e3c5e61dcb92bc5cebb2f7a5aa0dd`. 24 nodes/21 texts. Path 0→1→2→3→15→16→17→24→25→26→27→28→29→30→31→32→33→34→35→37→38→39→36→23.
First node2 %user_name%: Phew... I never expected the supply delivery mission would last this long...
**Final node36 %user_name%: We can't let that happen. I think we should fight them off here.**
Terminal23: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
`.
Speakers %user_name%/Char009, Tyltyl/Char004, Karl Steiner/Char012, Bibi/Char040, Bear/Char036.
Dependencies BG001_1.

### EP_1204A

Header2530633/packed1636/RW17476 SHA256 `7751914fbc82ac084f3e4ad74e7515546ecb5b98debd2ded0eaf665ebced2f25`. 10 nodes/6 texts. Path 0→1→2→3→15→17→26→24→25→23.
First node2 %user_name%: Now, if we are fighting against the wolves, waiting in ambush makes no sense.
**Final node25 : I will never forgive you!**
Terminal23: `scr-fade duration:0.6 color:(0,0,0,0)
wait duration:0.6
combat_goto id:CB0602`.
Speakers %user_name%/Char009, Tyltyl/Char004, Karl Steiner/Char012, Bibi/Char040, Bear/Char036.
Dependencies BG001_1, BGM_BATTLE2.

### EP_1301A

Header2534220/packed2023/RW27474 SHA256 `63a43594c737e2e27a46441fcf7728ae63d91327eaad1933d3745bff29d5d71b`. 18 nodes/15 texts. Path 0→1→2→3→5→6→7→8→9→10→11→12→13→14→15→16→17→18.
First node2 %user_name%: We are back, Acerola. We brought the anti-fever herbs too.
**Final node17 %user_name%: Where the truth was hidden...?**
Terminal18: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6`.
Speakers %user_name%/Char009, Acerola/Char030, Tyltyl/Char004, Karl Steiner/Char012.
Dependencies BG007_1.

### EP_1302A

Header2536267/packed2408/RW34379 SHA256 `2fef14f7736d0dac43f81e374b65aa055761c218a67fc4cb43ed70514f5bbb8e`. 23 nodes/18 texts. Path 0→1→3→4→5→6→24→8→9→10→11→12→13→14→16→17→19→25→20→21→22→23→18.
First node3 Acerola: Oh my! I need to leave now. The kids are waiting for me!
**Final node23 : Ugh! I can't breathe!**
Terminal18: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6`.
Speakers %user_name%/Char009, Acerola/Char030, Tyltyl/Char004, Karl Steiner/Char012.
Dependencies BG006_2, BG007_1.

### EP_1303A

Header2538699/packed2386/RW33746 SHA256 `c3c19b8b3f46572a6ae0e8e35ce6cda449c052ff952e17c3fa9ca207fa164df8`. 23 nodes/19 texts. Path 0→1→2→3→4→5→6→23→7→8→9→10→11→13→21→22→14→15→16→17→18→19→20.
First node2 Dino: Ugh! I almost suffocated to death under your luggage. Thanks for helping me out!
**Final node19 %user_name%: Do I smell more trouble in Midgard...?**
Terminal20: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6`.
Speakers %user_name%/Char009, Dino/Char054, Tyltyl/Char004.
Dependencies BG006_2.

### EP_1202A

Header2526666/packed1467/RW14608 SHA256 `fbceed7c0292cc706581f2557b5f66ed0e32a76361f84e6bf864ee9532180b25`. 8 nodes/5 texts. Path 0→1→2→3→15→16→17→23.
First node2 %user_name%: Phew... That was a tough fight.
**Final node17 %user_name%: Great! Let's return to Acerola now.**
Terminal23: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
ctrl-scene-back cnt:2`.
Speakers %user_name%/Char009, Tyltyl/Char004, Karl Steiner/Char012, Bibi/Char040, Bear/Char036.
Dependencies BG005_1.

### EP_1204B

Header2532293/packed1903/RW22916 SHA256 `4fe7d4b415762bbc53d55401576c0813445de029c45e476ca39e3d5356f2f083`. 14 nodes/9 texts. Path 0→1→2→3→28→16→17→26→31→24→25→29→30→23.
First node2 : Hey, I think there is a misunderstanding here. I never harmed any wolves!
**Final node30 %user_name%: Well... I think I'm in trouble...**
Terminal23: `episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
ctrl-scene-back cnt:2`.
Speakers %user_name%/Char009, Tyltyl/Char004, Karl Steiner/Char012, Bibi/Char040, Bear/Char036.
Dependencies BG007_1, BGM_BATTLE3.

## Original combat and STAT

- CB0601: `{"id":"CB0601","title":"E06_TITLE","stage_name":"E06_S05_TITLE","bgm":"BGM_TRAIN","power":"20000","game_res_id":"7","field_bg_res":"BG_RES","win_dialog":"EP_1202A","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{},{"type":"hunter","actor_id":"CB0601_012_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,1,1,0]}]],"right":[[{"type":"hunter","actor_id":"CB0601_036_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,1,1,0]},{"type":"hunter","actor_id":"CB0601_036_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,1,1,0]},{"type":"hunter","actor_id":"CB0601_036_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,1,1,0]}]]}`.
- CB0602: `{"id":"CB0602","title":"E06_TITLE","stage_name":"E05_S05_TITLE","bgm":"BGM_BATTLE2","power":"26000","game_res_id":"7","field_bg_res":"BG_RES","win_dialog":"EP_1204B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{},{"type":"hunter","actor_id":"CB0601_012_1","thumb":{"level":1,"rank":4,"hyper":0,"attr":3},"skill":[1,1,0,1,0]}]],"right":[[{"type":"monster","actor_id":"CB0602_M1","thumb":{"level":1,"rank":4,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0602_M1","thumb":{"level":1,"rank":4,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0602_M1","thumb":{"level":1,"rank":4,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0602_M1","thumb":{"level":1,"rank":4,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"hunter","actor_id":"CB0602_040_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,1,1,1]}]]}`.
- STAT array index68: `{"id":"CB0601_036_1","ref_id":"036","res_id":"C036","attr":3,"role":2,"cool_time":5000,"stat":{"rank":"4","hp":"2800","atk":"850","def":"200","spd":"5.00","crt_chance":"30.00","crt_dmg":"200","penetration":"0.00","block_chance":"30.00","block_dec_dmg":"30","attr_resist":"0","hp_regen":"0"},"skill":[{"type":1,"target_rank":1,"cool_time":8000,"cost":4,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1800,"duration":0,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":4,"target_type":1,"target_stat":4,"refer_target_type":1,"refer_target_stat":0,"base_number":-20,"duration":4000,"interval":0}]},{"type":3,"target_rank":3,"effect":[{"effect_type":2,"target_type":2,"target_stat":1,"refer_target_type":2,"refer_target_stat":4,"base_number":2,"duration":3000,"interval":3000}]},{"type":4,"target_rank":4,"effect":[{"effect_type":1,"target_type":2,"target_stat":1,"refer_target_type":2,"refer_target_stat":4,"base_number":6,"duration":0,"interval":0}]}]}`.
- STAT array index69: `{"id":"CB0602_040_1","ref_id":"040","res_id":"C040","attr":3,"role":1,"cool_time":5000,"stat":{"rank":"5","hp":"4000","atk":"900","def":"240","spd":"5.00","crt_chance":"30.00","crt_dmg":"200","penetration":"0.00","block_chance":"30.00","block_dec_dmg":"40","attr_resist":"0","hp_regen":"120"},"skill":[{"type":1,"target_rank":1,"cool_time":12000,"cost":4,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-500,"duration":4000,"interval":1000}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":2,"target_stat":14,"refer_target_type":1,"refer_target_stat":0,"base_number":20,"duration":4000,"interval":0}]},{"type":3,"target_rank":3,"effect":[{"effect_type":2,"target_type":2,"target_stat":15,"refer_target_type":2,"refer_target_stat":0,"base_number":-3,"duration":500,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1600,"duration":0,"interval":0}]},{"type":5,"target_rank":5,"effect":[{"effect_type":2,"target_type":1,"target_stat":4,"refer_target_type":2,"refer_target_stat":0,"base_number":-15,"duration":500,"interval":0}]}]}`.
- STAT array index72: `{"id":"CB0602_M1","res_id":"M024","attr":3,"role":1,"cool_time":5000,"stat":{"rank":"4","hp":"2500","atk":"1800","def":"200","spd":"0","crt_chance":"30.00","crt_dmg":"200","penetration":"0.00","attr_enhance":"0","block_chance":"30.00","block_dec_dmg":"30","attr_resist":"0","hp_regen":"20"},"skill":[]}`.
- STAT array index143: `{"id":"CB0601_012_1","ref_id":"012","res_id":"C012","attr":3,"role":1,"cool_time":5000,"stat":{"rank":"4","hp":"1150","atk":"750","def":"550","spd":"7.00","crt_chance":"33.00","crt_dmg":"200","penetration":"0","block_chance":"13.00","block_dec_dmg":"40","attr_resist":"0","hp_regen":"30"},"skill":[{"type":1,"target_rank":1,"cool_time":5000,"cost":3,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-2000,"duration":0,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":2,"target_stat":5,"refer_target_type":2,"refer_target_stat":0,"base_number":40,"duration":4000,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":2,"target_stat":7,"refer_target_type":2,"refer_target_stat":0,"base_number":1.0,"duration":4000,"interval":0}]}]}`.
- STAT array index144: `{"id":"CB0601_012_1","ref_id":"012","res_id":"C012","attr":3,"role":1,"cool_time":5000,"stat":{"rank":"4","hp":"1150","atk":"750","def":"533","spd":"7.00","crt_chance":"31.00","crt_dmg":"210","penetration":"0","block_chance":"13.00","block_dec_dmg":"40","attr_resist":"0","hp_regen":"26"},"skill":[{"type":1,"target_rank":1,"cool_time":6000,"cost":3,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-2000,"duration":0,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":2,"target_stat":5,"refer_target_type":2,"refer_target_stat":0,"base_number":40,"duration":4000,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":2,"target_stat":7,"refer_target_type":2,"refer_target_stat":0,"base_number":1.2,"duration":4000,"interval":0}]}]}`.

Both combats four owned placeholders plus fixed Karl/camp0 expected serial5. CB0601 has THREE original Bear/C036 entries, camp1 expected distinct instances serial6–8. CB0602 four repeated CB0602_M1/M024 references expected distinct camp1 instances serial6–9 then C040 serial10. These are expected bindings, not live native observations.

**Duplicate CB0601_012_1 native semantics now closed (2026-10-09):** see episode06-stat-duplicate-contract.md. ActorParser unique insertion retains first index; FindActorRef selects original row143 (DEF550/crit33/regen30/cooldown5000), retaining row144 unchanged in source. Scope is fresh index populated from preserved original array; earlier cache/reimport semantics require separate proof. Direct live fields remain pending. E05 CB0502_012_1 is distinct. No ordinary stats/owned grants changed.

## Original owners and additional packs

- BG001_1: DIAL_BG.jet header809877/packed61.
- BG005_1: DIAL_BG2.jet header2972816/packed32.
- BG006_2: DIAL_BG2.jet header2972927/packed31.
- BG007_1: DIAL_BG2.jet header2973092/packed32.
- BG900_1: DIAL_BG9.jet header2665708/packed31.
- BGM_BATTLE2: SND1.jet header1358916/packed479408.
- BGM_BATTLE3: SND1.jet header1838348/packed377426.
- BGM_COMIC1: SND_CDN.jet header4074657/packed682118.
- BGM_TRAIN: SND_CDN.jet header6514908/packed929968.
- M024_TH: M008.jet header223615/packed30.
- M024_H1: M008.jet header223138/packed47.
- M024_S: M008.jet header223491/packed46.

All 774 PAD packs walked exactly to EOF. Same-ID fragments concatenate to +0 total; each +4 part and +8 packed length checked; uint64+12/base38 names. No single-fragment image shortcut.
**Additional candidate complete packs beyond E05: C040.jet, C040_EFT.jet, C040_Q.jet, C040_SND.jet, C054.jet.** Documentary selection comparison, not native residency.

- C004.jet: 1246194 bytes/6 logical records; SHA256 `403634344564e6e6c889607ee4fa202b5b4d2b4ef066d52d2e611139ede743df`; previously selected.
- C009.jet: 3101288 bytes/9 logical records; SHA256 `98dc7e66efc1f3b4453966cf6ed09f1cab20af12b158eed1b51355b8cec798c5`; previously selected.
- C012.jet: 1795342 bytes/6 logical records; SHA256 `308bd36707873b09fb750baf3fe1c1830458521b01cd90eb5f838b3a4cce7f57`; previously selected.
- C012_EFT.jet: 3592464 bytes/7 logical records; SHA256 `d6cbe39b9da296f5ba6271e08a89d87d945eb0d9e3833563ad7d26f59a019bd2`; previously selected.
- C012_Q.jet: 54305 bytes/39 logical records; SHA256 `37b022a9949b6a2ec16df563522e416cfe0f90652aae47ceb21c2f81d389fa4b`; previously selected.
- C012_SND.jet: 109636 bytes/4 logical records; SHA256 `9f660ea0374ce7423c70c3924a583d6f0ee1ae4aac6899ef0bdac8a335629add`; previously selected.
- C030.jet: 587812 bytes/6 logical records; SHA256 `f997f429d8fce9ac8631cb9208e12da6eb6c19541e545fd840a69d05866d94fb`; previously selected.
- C036.jet: 1567284 bytes/6 logical records; SHA256 `e4f7cb46ab924b75f173752a0696e72c8288534273ca8f6104529b08c656b360`; previously selected.
- C036_EFT.jet: 1320814 bytes/8 logical records; SHA256 `b3a0a27dfdb4f79b1119cc27591ec768303a0209a85c1b0f66247d5fe38ddb83`; previously selected.
- C036_Q.jet: 53949 bytes/39 logical records; SHA256 `73002b5ee10b3dd49e5647531b142fb4fff410ab11cf8a99f6386d031e4baa25`; previously selected.
- C036_SND.jet: 192144 bytes/4 logical records; SHA256 `d4f8ff00e412c6f0515ba8caf61351b88e20769deebf882fff9ff7ca13f9ce02`; previously selected.
- C040.jet: 1184156 bytes/7 logical records; SHA256 `34c15d85a1ada674be94cb9a7a29906765f3029da6191512f2a5ee951ebd7df4`; ADDITIONAL.
- C040_EFT.jet: 3435626 bytes/12 logical records; SHA256 `7fcfc6a40dd56b8ddd8301838d0fce989cff1747b705c5937824a438ea61425e`; ADDITIONAL.
- C040_Q.jet: 53962 bytes/39 logical records; SHA256 `029b991a93eb6f3d9d7aea668bdf75006218957de09211378a4013306126718b`; ADDITIONAL.
- C040_SND.jet: 455854 bytes/7 logical records; SHA256 `707e9a8e20b66432f48cd6ce6a4bd06265e9f88cc2dfeee7b40db52fa1c25de0`; ADDITIONAL.
- C054.jet: 992404 bytes/6 logical records; SHA256 `540341367e541025f3a8bdf8679aade97b13f9a5c3d65cd01f96afa639536ab8`; ADDITIONAL.
- DIAL_BG.jet: 810132 bytes/9 logical records; SHA256 `b12aa44631bceb6da1d20870b8f84476b5922108dfe48c4248637a466148043e`; previously selected.
- DIAL_BG2.jet: 2973203 bytes/30 logical records; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; previously selected.
- DIAL_BG9.jet: 2665981 bytes/15 logical records; SHA256 `f085326e3139884fce5e1e2332312885c6aa15bf5dc6d4edf66cda4dc1c85b03`; previously selected.
- M008.jet: 223669 bytes/134 logical records; SHA256 `04b37480c31248de3a2a23f09901961923441a9ba7524abae037a0eb805074f5`; previously selected.
- SND1.jet: 7173961 bytes/68 logical records; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; previously selected.
- SND_CDN.jet: 10911430 bytes/105 logical records; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; previously selected.
- ST001.jet: 1733825 bytes/42 logical records; SHA256 `9948876a679a9cfce6a88233c7985e82b641137f639fae2aff8167e614e32cd7`; previously selected.

All nine dialogue paths exhaust all nodes, no conditional/nonlinear edge. Fades/waits may ignore taps; inspect displayed final text before terminal advancement. Binary Spine attachments/skin/timelines unclosed; native rendering required. Image/atlas closure follows below. Enemy stats preserved. OV1 metadata/native reward settlement unknown. No runtime/profile/server/save/original edits/grants.

## Additional image/atlas closure

### C040.jet

- C040 header0: 1024×512, positive-alpha pixels165366.
- C040_D header351840: 1024×1024, positive-alpha pixels582970.
- C040_D2 header1172322: 256×256, positive-alpha pixels25976.
- C040_A pageC040.png resolves C040 1024×512.
- C040_A: 45 original regions; all rotated rectangle bounds valid; RW SHA256 `ce2bd6bf62d8180d546afdc54ab3b36f446ee8faa139ac4c63a965bb599ae2ba`.
- C040_B header299944/RW152446 SHA256 `12215d63b299e90fbdab521538a4db9e2538891bc555d705f6e4345cbb83947f` external symbols C040_E01, C040_E02, C040_E03, C040_E04, C040_E05, C040_EC, C040_SND01, C040_SND02, C040_SND03, C040_SND04, C040_SND05, C040_SND06, C040_SND07.
- C040_DA pageC040_d.png resolves C040_D 1024×1024.
- C040_DA pageC040_d2.png resolves C040_D2 256×256.
- C040_DA: 11 original regions; all rotated rectangle bounds valid; RW SHA256 `df34f04187d84c48aab2fecec9a47ee1837b3b102735b1cad30ebf8360a726d6`.
- C040_DB header1183693/RW1050 SHA256 `6b4f40e47db4937249a4479555498b279238c998d1568e7ea0e36b46cbfffed5` external symbols .
### C040_EFT.jet

### C040_Q.jet

- 4PUGXF header0: 77×78, positive-alpha pixels1414.
- N.0AZC header2411: 55×81, positive-alpha pixels3026.
- 1M3OX header5762: 82×44, positive-alpha pixels1581.
- VMIW88 header7914: 110×110, positive-alpha pixels9660.
- XZ1XX_ header9450: 115×121, positive-alpha pixels8947.
- PMO315 header19010: 96×97, positive-alpha pixels1879.
- MI8A_7 header20374: 175×210, positive-alpha pixels36738.
- 18NMPHA header21126: 175×210, positive-alpha pixels28564.
- 126T.D9 header44382: 64×64, positive-alpha pixels2067.
- 5_D3M0 header45902: 64×64, positive-alpha pixels1790.
- YJPL9Z header47142: 64×64, positive-alpha pixels2104.
- KNB9SO header48786: 64×64, positive-alpha pixels2017.
- 2RIJLA header50359: 64×64, positive-alpha pixels1826.
- .XGM_R header52053: 84×29, positive-alpha pixels1797.
### C040_SND.jet

### C054.jet

- C054 header0: 1024×1024, positive-alpha pixels325876.
- C054_D header636143: 1024×1024, positive-alpha pixels498095.
- C054_A pageC054.png resolves C054 1024×1024.
- C054_A: 83 original regions; all rotated rectangle bounds valid; RW SHA256 `521a4a97984c05852f85e1e012b4707bf371050bf3bfd5cc970e92bc562a4147`.
- C054_B header585584/RW132018 SHA256 `fa4d20233b930843c86ff316a954c120ed88611c812faad250424ee4da68b8f3` external symbols C054_E01, C054_E02, C054_E03, C054_E04, C054_EC, C054_SND01, C054_SND02, C054_SND03, C054_SND04, C054_SND05, C054_SND06.
- C054_DA pageC054_d.png resolves C054_D 1024×1024.
- C054_DA: 11 original regions; all rotated rectangle bounds valid; RW SHA256 `95cb6588d9649e6f0c9a41fc21be9e17ce5bd4b630b7a5926f8e5dddab572df5`.
- C054_DB header991946/RW1043 SHA256 `ba01877719cd3c88bd99b6c4d40c0a90aa86360d09cc850ec5a59193312e1ffd` external symbols .

19 complete added-pack I2/PNG images decoded with positive alpha; fragments reassembled before decode. Atlas region bounds are closed by this section. C054 Dino is portrait-only: its unused combat C054_B references C054_E01/E02/E03/E04/EC/SND01–06, but dialogue C054_DB contains no such symbols, so extra combat packs are not required by E06. C040 Bibi requires full base/Q/EFT/SND. C036 Bear/C012 Karl full materials and M024 in M008 are already selected. Both ENV7 use original STI001/ST001. Binary attachment/skin/timeline semantics and native rendering remain unverified.

C040_B external symbols C040_E01–E05/EC each exist in C040_EFT (12 logical RW effect/atlas records), and SND01–07 each exist in C040_SND (7 records). Symbol-name edges are closed; full binary effect/Spine attachment semantics remain unverified. Opaque I2 identifiers rendered in base38 above are numeric keys, not original human-readable sprite assignments.

## C040 equipment/thumbnail graph closure

- C040_WP → C040_WEP → imageIDs 370739605.
- C040_AM → C040_AMOR → imageIDs 1897489542.
- C040_AC → C040_ACCRY → imageIDs 3297597.
- C040_TH → C040_THN → imageIDs 2687844119.
- C040_STH → C040_STHN → imageIDs 3694019796.
- C040_SI1 → C040_SI01 → imageIDs 3183561311.
- C040_SI2 → C040_SI02 → imageIDs 474044376.
- C040_SI3 → C040_SI03 → imageIDs 2735015797.
- C040_SI4 → C040_SI04 → imageIDs 1633279164.
- C040_SI5 → C040_SI05 → imageIDs 215784948.
- C040_SHADOW → C040_SHA → imageIDs 2922186689.

11 AT / 14 S2 records consumed exactly; zero missing/type-mismatched target edges. Images decoded with positive alpha in prior section. AT count+43/frame+47/14-byte prefix plus event length+12; S2 imageID+46. No inferred aliases.
