# E07 original entry and complete material audit

2026-10-09. Read-only PAD/JSON audit. Only this report and requested E06 correction written. Native E07 entry/residency/combat/progress/reward pending. Compare complete original selection through E06.

## Progression

Original reward `{"item": [{"ref_id": "CERUM01", "qty": 20}], "free_iap": 0}`. CERUM01×20 identity/quantity recovered; GetItem metadata/native settlement unknown. No grant.
- E07_S01: EP_1401A, battle=False, {"localname": "local_MIDGARD", "x": 1235, "y": 1150}; portraitC003_DIALOG.
- E07_S02: EP_1402A, battle=True, {"localname": "local_BRUCE", "x": 1255, "y": 1155}; portraitC003_DIALOG.
- E07_S03: EP_1403A, battle=False, {"localname": "local_???", "x": 1255, "y": 1155}; portraitC003_DIALOG.
- E07_S04: EP_1404A, battle=True, {"localname": "local_???", "x": 1255, "y": 1155}; portraitC005_DIALOG.
- E07_S05: EP_1405A, battle=False, {"localname": "local_BRUCE", "x": 1255, "y": 1155}; portraitC005_DIALOG.

Combat labels agree with actual S02/S04. Original local_??? retained.

## Complete paths

### EP_1401A

Header2541109/packed2257/RW32198 SHA256 `b3dac4c872207d9af41d174ee460e1e3097448da812aaf9458b753eec8c09fe0`. 22 nodes/18 texts. Path 0→1→2→3→23→4→5→6→7→8→9→10→13→14→15→16→17→18→19→20→21→22.
First node2 Lana: I heard you're doing pretty well these days. It seems you were meant to be a hunter.
**Final node21 %user_name%: Oh man...**
Terminal22: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers Lana/NPC001, %user_name%/Char009, Schumann/NPC007.
Dependencies BGM_GULLVEIG, N001_BG.

### EP_1402A

Header2543390/packed1767/RW20783 SHA256 `d8541900677af22eff49a25841874ded4f13f1e3af6861d3a909fcb60ede5562`. 13 nodes/9 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→19.
First node2 Schumann: This is it. This is his room.
**Final node11 %user_name%: No!! We have to stop him! Take his guitar away from him!**
Terminal19: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0701`.
Speakers Schumann/NPC007, Lana/NPC001, %user_name%/Char009, Bruce Bang/Char016.
Dependencies BG002_1, BGM_COMIC1, N007_BG.

### EP_1403A

Header2546949/packed1915/RW22979 SHA256 `92c604b106b31fe2a939bd907de73a52295b2dfc5613713ff9f303f676f05888`. 15 nodes/11 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→15.
First node2 %user_name%: He has the power to make people go unconscious...
**Final node13 %user_name%: I told you last time! I was starving so I went to eat!**
Terminal15: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Bruce Bang/Char016, Vincent/Char010.
Dependencies BGM_BATTLE3, BGM_D_START, N004_BG.

### EP_1404A

Header2548888/packed1768/RW19006 SHA256 `ccb2b69fd0397d0dbf1947192ac2896944377d0ec2ce37b9b255701484552fa3`. 12 nodes/9 texts. Path 0→1→2→3→4→6→7→16→8→10→11→15.
First node2 Vincent: How hard are you trying to disappoint me?
**Final node11 Vincent: ... Shut up and take out your sword.**
Terminal15: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0702`.
Speakers %user_name%/Char009, Bruce Bang/Char016, Vincent/Char010.
Dependencies BGM_BATTLE3, N004_BG.

### EP_1405A

Header2552296/packed2242/RW33874 SHA256 `eaf7da96d91899c5d192557ed354ad16a13be90801fe80fe37e331294eecef0b`. 23 nodes/20 texts. Path 0→1→2→22→3→4→5→6→7→8→9→10→11→12→13→14→15→16→17→18→19→20→21.
First node2 %user_name%: Ugh... Where is this? Is the world of the unconscious finally over...?
**Final node20 %user_name%: Everyone, run!**
Terminal21: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Lana/NPC001, Schumann/NPC007, Bruce Bang/Char016.
Dependencies BG002_1, BGM_COMIC1.

### EP_1402B

Header2545181/packed1744/RW19656 SHA256 `c43ca6509ce8615bc3ec5e98c726e8e4385503b6bef7b793c1546280986ae38d`. 12 nodes/8 texts. Path 0→1→21→20→12→13→14→15→16→17→18→19.
First node21 %user_name%: Give up now. Give me the guitar!
**Final node18 %user_name%: Wha- This is... terrifying...**
Terminal19: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers Schumann/NPC007, Lana/NPC001, %user_name%/Char009, Bruce Bang/Char016.
Dependencies BG002_1, BGM_COMIC1, BGM_D_START, N004_BG, N007_BG.

### EP_1404B

Header2550680/packed1592/RW16960 SHA256 `10743da25aa2e64817166075db29068386a4d0be406f08d1c41b311f9ff72132`. 11 nodes/8 texts. Path 0→1→2→3→10→11→9→4→5→8→7.
First node2 Vincent: Ugh... You have improved. More than I expected...
**Final node8 Vincent: In this freezing hell...**
Terminal7: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers Vincent/Char010, %user_name%/Char009.
Dependencies BGM_D_START, N004_BG.

## Combat and original stats

- CB0701: `{"id":"CB0701","title":"E07_TITLE","stage_name":"E07_S02_TITLE","bgm":"BGM_COMIC1","power":"25000","game_res_id":"99","field_bg_res":"BG_RES","win_dialog":"EP_1402B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{}]],"right":[[{"type":"hunter","actor_id":"CB0701_011_1","thumb":{"level":20,"rank":4,"hyper":0,"attr":1},"skill":[1,1,0,1,0]},{"type":"hunter","actor_id":"CB0701_018_1","thumb":{"level":20,"rank":4,"hyper":0,"attr":2},"skill":[1,1,0,1,0]},{"type":"hunter","actor_id":"CB0701_007_1","thumb":{"level":20,"rank":4,"hyper":0,"attr":1},"skill":[1,1,0,1,0]},{"type":"hunter","actor_id":"CB0701_016_1","thumb":{"level":20,"rank":4,"hyper":0,"attr":2},"skill":[1,1,0,1,0]}]]}`.
- CB0702: `{"id":"CB0702","title":"E07_TITLE","stage_name":"E07_S04_TITLE","bgm":"BGM_BATTLE3","power":"33000","game_res_id":"901","field_bg_res":"BG_RES","win_dialog":"EP_1404B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{}]],"right":[[{"type":"monster","actor_id":"CB0702_M1","thumb":{"level":30,"rank":4,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0702_M1","thumb":{"level":30,"rank":4,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0702_M1","thumb":{"level":30,"rank":4,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0702_M1","thumb":{"level":30,"rank":4,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"hunter","actor_id":"CB0702_010_1","thumb":{"level":30,"rank":5,"hyper":0,"attr":3},"skill":[1,1,1,1,1]}]]}`.
- STAT array index74: `{"id":"CB0701_011_1","ref_id":"011","res_id":"C011","attr":1,"role":2,"cool_time":5000,"stat":{"rank":"4","hp":"3300","atk":"900","def":"250","spd":"5","crt_chance":"20","crt_dmg":"200","penetration":"0","block_chance":"30","block_dec_dmg":"40","attr_resist":"0","hp_regen":"80"},"skill":[{"type":1,"target_rank":1,"cool_time":8000,"cost":3,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1500,"duration":0,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":2,"target_stat":16,"refer_target_type":2,"refer_target_stat":0,"base_number":1,"duration":2000,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":2,"target_stat":14,"refer_target_type":2,"refer_target_stat":0,"base_number":40,"duration":4000,"interval":0}]}]}`.
- STAT array index89: `{"id":"CB0701_018_1","ref_id":"018","res_id":"C018","attr":2,"role":2,"cool_time":5000,"stat":{"rank":"4","hp":"3100","atk":"1000","def":"240","spd":"5","crt_chance":"30","crt_dmg":"200","penetration":"0","block_chance":"30","block_dec_dmg":"40","attr_resist":"0","hp_regen":"80"},"skill":[{"type":1,"target_rank":1,"cool_time":8000,"cost":3,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-300,"duration":4000,"interval":1000}]},{"type":2,"target_rank":2,"effect":[{"effect_type":1,"target_type":2,"target_stat":1,"refer_target_type":2,"refer_target_stat":4,"base_number":6,"duration":4000,"interval":1000}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":2,"target_stat":6,"refer_target_type":2,"refer_target_stat":0,"base_number":25,"duration":4000,"interval":0}]}]}`.
- STAT array index90: `{"id":"CB0701_007_1","ref_id":"007","res_id":"C007","attr":1,"role":3,"cool_time":5000,"stat":{"rank":"4","hp":"2300","atk":"1400","def":"200","spd":"5","crt_chance":"20","crt_dmg":"200","penetration":"0","block_chance":"20","block_dec_dmg":"30","attr_resist":"0","hp_regen":"80"},"skill":[{"type":1,"target_rank":1,"cool_time":8000,"cost":3,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1500,"duration":0,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-300,"duration":4100,"interval":1000},{"effect_type":4,"target_type":1,"target_stat":16,"refer_target_type":2,"refer_target_stat":0,"base_number":-3,"duration":300,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1000,"duration":0,"interval":0}]}]}`.
- STAT array index91: `{"id":"CB0701_016_1","ref_id":"016","res_id":"C016","attr":2,"role":4,"cool_time":5000,"stat":{"rank":"4","hp":"2400","atk":"1000","def":"220","spd":"5","crt_chance":"20","crt_dmg":"200","penetration":"0","block_chance":"20","block_dec_dmg":"30","attr_resist":"0","hp_regen":"80"},"skill":[{"type":1,"target_rank":1,"cool_time":8000,"cost":4,"crt_chance":50,"effect":[{"effect_type":1,"target_type":4,"target_stat":1,"refer_target_type":2,"refer_target_stat":4,"base_number":9,"duration":4100,"interval":1000}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":4,"target_stat":9,"refer_target_type":2,"refer_target_stat":0,"base_number":30,"duration":5000,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":4,"target_stat":9,"refer_target_type":2,"refer_target_stat":0,"base_number":30,"duration":5000,"interval":0}]}]}`.
- STAT array index103: `{"id":"CB0702_M1","res_id":"M058","attr":2,"role":2,"cool_time":5000,"stat":{"rank":"4","hp":"2400","atk":"2600","def":"200","spd":"0","crt_chance":"30.00","crt_dmg":"200","penetration":"0.00","attr_enhance":"0","block_chance":"30.00","block_dec_dmg":"30","attr_resist":"0","hp_regen":"50"},"skill":[]}`.
- STAT array index131: `{"id":"CB0702_010_1","ref_id":"010","res_id":"C010","attr":3,"role":1,"cool_time":5000,"stat":{"rank":"5","hp":"3700","atk":"1800","def":"260","spd":"5.00","crt_chance":"30.00","crt_dmg":"200","penetration":"5.00","block_chance":"30.00","block_dec_dmg":"40","attr_resist":"0","hp_regen":"50"},"skill":[{"type":1,"target_rank":1,"cool_time":10000,"cost":4,"crt_chance":50,"effect":[{"effect_type":1,"target_type":1,"target_stat":1,"refer_target_type":1,"refer_target_stat":1,"base_number":-1800,"duration":0,"interval":0},{"effect_type":4,"target_type":1,"target_stat":16,"refer_target_type":2,"refer_target_stat":0,"base_number":-3,"duration":10000,"interval":0}]},{"type":2,"target_rank":2,"effect":[{"effect_type":3,"target_type":2,"target_stat":16,"refer_target_type":2,"refer_target_stat":0,"base_number":1,"duration":2000,"interval":0}]},{"type":4,"target_rank":4,"effect":[{"effect_type":3,"target_type":2,"target_stat":5,"refer_target_type":2,"refer_target_stat":0,"base_number":20,"duration":3000,"interval":0}]}]}`.

Four owned placeholders, no fixed ally in both. Expected camp1 CB0701 serial5C011/6C018/7C007/8C016. CB0702 distinct M058 instances serial5–8 then C010 serial9. Construction expectations only, not native observations. No owned grant/ordinary stat promotion.

## Original owner closure

- BG002_1: DIAL_BG2.jet header2972650/packed31.
- BGM_BATTLE3: SND1.jet header1838348/packed377426.
- BGM_COMIC1: SND_CDN.jet header4074657/packed682118.
- BGM_D_START: SND1.jet header2990616/packed479826.
- BGM_GULLVEIG: SND1.jet header3470466/packed646624.
- N001_BG: N001_BG.jet header2282340/packed49.
- N004_BG: N004.jet header1640181/packed271.
- N007_BG: N007.jet header3267619/packed215.
- M058_TH: M020.jet header922961/packed61.
- M058_H1: M020.jet header922072/packed117.
- M058_S: M020.jet header922749/packed103.
- STI099_A1: ST099.jet header1252007/packed32.
- STI901_A1: ST901.jet header663289/packed33.

774 original PAD packs walked exactly to EOF; same-ID fragments concatenate to +0 total, +4 part/+8 packed lengths checked, uint64+12/base38 names.
**Complete additional selection beyond E06: C007.jet, C007_EFT.jet, C007_Q.jet, C011.jet, C011_EFT.jet, C011_Q.jet, C011_SND.jet, C016.jet, C016_EFT.jet, C016_Q.jet, C016_SND.jet, C018.jet, C018_EFT.jet, C018_Q.jet, M020.jet, N007.jet, ST901.jet.** Compared saved base and overlay hash inventories, without sourcing/mutating profile. Native residency not inferred.

- C007.jet: 753975 bytes/6 logical records; SHA256 `949be5dbd4d6451f4f50fc862a1a0f5071f591fda73e95da3a5d727690930e73`; ADDITIONAL.
- C007_EFT.jet: 2137495 bytes/8 logical records; SHA256 `8bb0c0971a56491cb3e41cd9b4279e077e295d9f1fd33919a6bbb537e9e0af3e`; ADDITIONAL.
- C007_Q.jet: 57482 bytes/39 logical records; SHA256 `8395cc442c9a41a4381766e5c8b959e6d89f8cc86ba6146efc024ceeb07192b8`; ADDITIONAL.
- C007_SND.jet: 81150 bytes/2 logical records; SHA256 `5e794d5014e333b74927bb508d259cd2b1f78653248379f8e3ca839f4560248c`; previously selected.
- C009.jet: 3101288 bytes/9 logical records; SHA256 `98dc7e66efc1f3b4453966cf6ed09f1cab20af12b158eed1b51355b8cec798c5`; previously selected.
- C010.jet: 2759458 bytes/9 logical records; SHA256 `3592c448aca8b7096f4adde8420e2ef19988cc6e452c23ef513f0e4fc6c59067`; previously selected.
- C010_EFT.jet: 3818579 bytes/13 logical records; SHA256 `692d3a46d7eddf39fb9b526b713d171c9e79d1b250e6408aa231bf62d87eb797`; previously selected.
- C010_Q.jet: 53683 bytes/45 logical records; SHA256 `f2a19358c627047df72baa8329428147e70f8a0d36960b1e0a3996301985955d`; previously selected.
- C010_SND.jet: 175008 bytes/9 logical records; SHA256 `e32a4e85807a49e2961ebc5de7b178295c9c818c20816df92f85528ba1879df9`; previously selected.
- C011.jet: 1189575 bytes/6 logical records; SHA256 `e2aea670ac617df79be05ad2c860074997efbd5201c1a8724e179d8bca1be944`; ADDITIONAL.
- C011_EFT.jet: 1944752 bytes/8 logical records; SHA256 `268de72b2d4e405009a7345f9c0a536d131b154194b03e9f029497e7880c88ed`; ADDITIONAL.
- C011_Q.jet: 53700 bytes/39 logical records; SHA256 `6abe741c5b180e20d6a96d171320294e978e4780d6d1cd69504ed94a978f3a41`; ADDITIONAL.
- C011_SND.jet: 86588 bytes/4 logical records; SHA256 `0cb28a36f329a90661c41bc0619258b1d03c0cfff3956187ea670dead89c5ac5`; ADDITIONAL.
- C016.jet: 757670 bytes/7 logical records; SHA256 `c35c525e4eb65a7ded346aa7baac2aacdafbc40d51c38a746debebf3d2c2436f`; ADDITIONAL.
- C016_EFT.jet: 7335026 bytes/6 logical records; SHA256 `f1347d403ac57aa855841b2307d0f596754a5c6b8dd198fc1a1abf601228c41f`; ADDITIONAL.
- C016_Q.jet: 120442 bytes/39 logical records; SHA256 `33b1e5a313ad84c990a0bbb5335304fe84bf64aaed8e12db72fb94060e073eb4`; ADDITIONAL.
- C016_SND.jet: 135066 bytes/2 logical records; SHA256 `f578b51dbf267d304a34963ec906b0eaa372486c1f2fad0c55dd68e5f4ff6f6a`; ADDITIONAL.
- C018.jet: 900296 bytes/7 logical records; SHA256 `7ab656845ab2e37448c48e073ec34301fe5d5e9dd505c384d200a4c25d95e82a`; ADDITIONAL.
- C018_EFT.jet: 1147675 bytes/12 logical records; SHA256 `a19f6f9e06468eb1c2f5ecf6b861d1e9e78c57bee6f2fef5831c7f8a1ac29181`; ADDITIONAL.
- C018_Q.jet: 42481 bytes/39 logical records; SHA256 `9eae7a673078dc1baf46c66ea935ad94f13fc48507e155197b39744a1ea57fba`; ADDITIONAL.
- C018_SND.jet: 95425 bytes/4 logical records; SHA256 `e1b1ffaeb0dd44c9a01a87c1f225097ab99cef553b3bfb496d6643d244c1bf3d`; previously selected.
- DIAL_BG2.jet: 2973203 bytes/30 logical records; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; previously selected (single-pack final-background overlay).
- M020.jet: 925674 bytes/135 logical records; SHA256 `f0acad2194ab843a3fb722176c51c93a916fab8238be19aa42ac379097e62dbb`; ADDITIONAL.
- N001.jet: 869436 bytes/4 logical records; SHA256 `a54b3997bf8f2b60f4a0ae787d9a926c2a9188f0fb6661f1e153e3b4cc9cb6e8`; previously selected.
- N001_BG.jet: 2282467 bytes/21 logical records; SHA256 `4d09c9eaf150befb7adc3a32919bdba6247ceb2097d5cac069de5da48fcb3d40`; previously selected.
- N004.jet: 1651492 bytes/47 logical records; SHA256 `dac953f788f16936f95c664cb9fd28e628f24b3325a7dc241a19b658e86935bb`; previously selected.
- N007.jet: 3327702 bytes/33 logical records; SHA256 `48633922e7091be83983fdff41416725f14c1631a09fac03986d17b31f9a45c7`; ADDITIONAL.
- SND1.jet: 7173961 bytes/68 logical records; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; previously selected.
- SND_CDN.jet: 10911430 bytes/105 logical records; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; previously selected.
- ST099.jet: 1252287 bytes/25 logical records; SHA256 `e99d2c7df04f4c32f539d4b79d44791a69f97046dd61b48d4a89211a72f50e81`; previously selected.
- ST901.jet: 663573 bytes/20 logical records; SHA256 `5036d6f3490eb011a0b7fc3bcb30bd56e897dc776657e11d9543f995f9725128`; ADDITIONAL.
- Original ENV_INFO `99,배틀,STI099,111,-5,160,11,-10,273,111,20,648,111,30,840,111,-5,1000`. Exact prefix owners above; no invented numeric/suffix aliases.
- Original ENV_INFO `901,극전압 무저갱,STI901,111,-5,0,111,-20,40,111,-40,210,111,-60,580,111,-20,850`. Exact prefix owners above; no invented numeric/suffix aliases.

All seven paths exhaust every node, with one outgoing edge per nonterminal/no ConditionsString. Fades may ignore taps: fresh final-text UI controls terminal advancement. Original stats unchanged. Binary Spine attachment/skin/timeline/native render remain unverified. CERUM01 metadata/native settlement unknown. No runtime/server/profile/save/original edits/grants.

## Original images and atlas edges

### C007.jet

- C007 header0: 1024×512, positive-alpha pixels181824.
- C007_D header379308: 1024×1024, positive-alpha pixels575328.
- C007_A pageC007.png resolves C007 1024×512.
- C007_A: 38 regions verified; RW SHA256 `2b585e633719ed58301f3ba516237e55ce7a9ba07a289274d5a39ecb0186d3de`; all pages/rotated rectangle bounds valid.
- C007_B header327820/RW158087 SHA256 `8bce194e09ad758f0ca809a30adc4421bb2eea20422817147c286ba2f11e7728` external symbols C007_E01, C007_E02, C007_EC, C007_SND01, C007_SND02.
- C007_DA pageC007_d.png resolves C007_D 1024×1024.
- C007_DA: 7 regions verified; RW SHA256 `0ef8b5aa670e4ceb99428ce7e3bb825914bfb5376a5ee3eeaf2538712f5c8449`; all pages/rotated rectangle bounds valid.
- C007_DB header753589/RW814 SHA256 `d1f96cb297643542776801d659197d967121926f9074ecfb507064620462ca11` external symbols .
### C007_EFT.jet

### C007_Q.jet

- 11S19I7 header0: 110×110, positive-alpha pixels9662.
- 10J46UG header1547: 83×46, positive-alpha pixels2454.
- 19UVFB5 header3968: 55×92, positive-alpha pixels3977.
- A6C4O header7679: 74×60, positive-alpha pixels1897.
- 2DAUO6 header9926: 175×210, positive-alpha pixels36738.
- 14NPST header10680: 175×210, positive-alpha pixels30304.
- 13OQD6I header37183: 102×126, positive-alpha pixels9066.
- QL1FCA header47089: 96×97, positive-alpha pixels1899.
- 152F9NT header48538: 64×64, positive-alpha pixels2315.
- BKE61D header50121: 64×64, positive-alpha pixels1483.
- 1T8ZGD header51366: 64×64, positive-alpha pixels1728.
- YXYOIL header52539: 64×64, positive-alpha pixels1955.
- STC_2U header53719: 64×64, positive-alpha pixels2274.
- 10ALQ.V header55534: 84×29, positive-alpha pixels1817.
### C007_SND.jet

### C011.jet

- C011 header0: 512×512, positive-alpha pixels150205.
- C011_D header362673: 1024×1024, positive-alpha pixels611411.
- C011_A pageC011.png resolves C011 512×512.
- C011_A: 36 regions verified; RW SHA256 `3c52a51d31e73d74283aca665b2553b8e08336b8095a2fbf55e2b9e8cdaddcbd`; all pages/rotated rectangle bounds valid.
- C011_B header331204/RW115379 SHA256 `9587cea72c34e9bf23dbd03621e1a2bfa5b33f57a75aa4aa3fe792ab0111128e` external symbols C011_E01, C011_E02, C011_E03, C011_EC, C011_SND01, C011_SND02, C011_SND03, C011_SND04.
- C011_DA pageC011_d.png resolves C011_D 1024×1024.
- C011_DA: 12 regions verified; RW SHA256 `090230bab773140bab75cb4ef3cdbf9a0c665fe4f598e8c0ef6daaa28d2ed094`; all pages/rotated rectangle bounds valid.
- C011_DB header1189035/RW1149 SHA256 `1bced5947163ed00df46256699d7a958923155f59d5ee3889fd34093a3bb4a58` external symbols .
### C011_EFT.jet

### C011_Q.jet

- 112GJSJ header0: 110×110, positive-alpha pixels9660.
- EUBEPJ header1565: 75×75, positive-alpha pixels1802.
- QR.IHO header4084: 71×93, positive-alpha pixels4215.
- 16NQJJU header7963: 85×43, positive-alpha pixels2267.
- 15G8K.1 header10418: 175×210, positive-alpha pixels36730.
- 1BRCJUE header11153: 175×210, positive-alpha pixels30244.
- _7KRKR header35072: 92×123, positive-alpha pixels8049.
- 1CYD22K header43229: 96×97, positive-alpha pixels1871.
- 1BJ3FYW header44566: 64×64, positive-alpha pixels2325.
- HEJXEB header46477: 64×64, positive-alpha pixels1413.
- 1DZZ8HL header47816: 64×64, positive-alpha pixels2235.
- F.RQOP header48977: 64×64, positive-alpha pixels2163.
- UC1L39 header50348: 64×64, positive-alpha pixels1789.
- P3SZG7 header51806: 84×29, positive-alpha pixels1755.
### C011_SND.jet

### C016.jet

- C016 header0: 1024×512, positive-alpha pixels150958.
- C016_D header400645: 1024×1024, positive-alpha pixels404989.
- C016_D2 header685339: 512×1024, positive-alpha pixels146044.
- C016_A pageC016.png resolves C016 1024×512.
- C016_A: 48 regions verified; RW SHA256 `4641dcfbb577c5dc28593f67e237648941092f315249e6b9e804a5663dd3dd13`; all pages/rotated rectangle bounds valid.
- C016_B header365823/RW147197 SHA256 `dc03f79868fa83fe652d9c6113965b38097dcf0b0011c057ed850ea97e295be7` external symbols C016_E01, C016_E02, C016_EC, C016_SND01, C016_SND02.
- C016_DA pageC016_d.png resolves C016_D 1024×1024.
- C016_DA pageC016_d2.png resolves C016_D2 512×1024.
- C016_DA: 5 regions verified; RW SHA256 `c0fda99f7855b5f8ceec5161c4f84fbc8796019193d7324bba3cd00bd6e4d548`; all pages/rotated rectangle bounds valid.
- C016_DB header757303/RW2094 SHA256 `17aef3d89b3175f95c1ead5edfcce33f1fa8cda4545b003f32e3517c933eeb3d` external symbols .
### C016_EFT.jet

### C016_Q.jet

- VJH97 header0: 110×110, positive-alpha pixels9668.
- 1AZR1LP header1935: 90×71, positive-alpha pixels2182.
- 648.GA header9644: 55×94, positive-alpha pixels3677.
- 2FX9VI header18160: 53×85, positive-alpha pixels2418.
- X6.6WN header23324: 175×210, positive-alpha pixels36738.
- 11_ZM81 header24111: 175×210, positive-alpha pixels23750.
- W5BAEO header77572: 98×133, positive-alpha pixels8334.
- DN4U9D header100580: 96×97, positive-alpha pixels1919.
- T59K0Y header102359: 64×64, positive-alpha pixels1701.
- OB54MP header105478: 64×64, positive-alpha pixels2127.
- 6O43K4 header108457: 64×64, positive-alpha pixels2157.
- 5U_6PO header110845: 64×64, positive-alpha pixels2586.
- 16X1MBE header114889: 64×64, positive-alpha pixels2204.
- P2WDPS header118077: 84×29, positive-alpha pixels1928.
### C016_SND.jet

### C018.jet

- C018 header0: 1024×256, positive-alpha pixels130681.
- C018_D header338915: 1024×1024, positive-alpha pixels340411.
- C018_D2 header747563: 1024×1024, positive-alpha pixels178921.
- C018_A pageC018.png resolves C018 1024×256.
- C018_A: 37 regions verified; RW SHA256 `fd5699977430c08deb2942ca1076043e4afd144405a83e8db6e59061545dcce6`; all pages/rotated rectangle bounds valid.
- C018_B header306984/RW112287 SHA256 `83fb34febce3560b134eca9f1f2041f5a9b5b2f78d72cbab822edf1de0f5fd7d` external symbols C018_E01, C018_E02, C018_E03, C018_E04, C018_E05, C018_EC, C018_SND01, C018_SND02, C018_SND03, C018_SND04.
- C018_DA pageC018_d.png resolves C018_D 1024×1024.
- C018_DA pageC018_d2.png resolves C018_D2 1024×1024.
- C018_DA: 2 regions verified; RW SHA256 `6ce218d91a7d027a8289d44b26c4d7f67d1010f681e35f3cf1f86408e94e3282`; all pages/rotated rectangle bounds valid.
- C018_DB header900022/RW1213 SHA256 `93f9c3702dcd96dfdb5c6b3ca5fc741b38956d8d53118ebf58ad3342f575ab24` external symbols .
### C018_EFT.jet

### C018_Q.jet

- 3UT0EA header0: 110×110, positive-alpha pixels9661.
- 34XBQP header1645: 77×56, positive-alpha pixels1395.
- 1CXKOUA header3659: 66×70, positive-alpha pixels3587.
- 1G1_ZLB header6217: 82×36, positive-alpha pixels1754.
- ZPM0H4 header7854: 175×210, positive-alpha pixels36738.
- N76_96 header8608: 175×210, positive-alpha pixels24334.
- _BFHA8 header25956: 89×113, positive-alpha pixels7197.
- 1ELIAS2 header32256: 96×97, positive-alpha pixels1879.
- 166111W header33667: 64×64, positive-alpha pixels2177.
- O8LL1 header35133: 64×64, positive-alpha pixels1674.
- 372R7Q header36457: 64×64, positive-alpha pixels2207.
- L.BMS7 header37681: 64×64, positive-alpha pixels1813.
- AY0CBF header39376: 64×64, positive-alpha pixels1079.
- P64P6M header40540: 84×29, positive-alpha pixels1782.
### C018_SND.jet

### M020.jet

- X49IK_ header0: 91×91, positive-alpha pixels6481.
- Z8SL55 header2813: 157×31, positive-alpha pixels3886.
- 9_CVAB header5239: 171×171, positive-alpha pixels16932.
- 18F305U header29763: 165×166, positive-alpha pixels16316.
- 471PCH header53293: 167×171, positive-alpha pixels16001.
- 11XE22_ header79032: 164×165, positive-alpha pixels15953.
- 9RJ_DB header105292: 172×166, positive-alpha pixels17476.
- N.0H3G header139830: 162×166, positive-alpha pixels15542.
- 94SJR. header166492: 187×169, positive-alpha pixels18128.
- CPH_KI header205815: 180×171, positive-alpha pixels15950.
- 5Q4N76 header232741: 134×169, positive-alpha pixels17496.
- Y6XLT6 header267537: 134×159, positive-alpha pixels15666.
- NH84L0 header292387: 116×94, positive-alpha pixels7904.
- _GZDC header305420: 171×171, positive-alpha pixels16812.
- K43UXG header331716: 165×166, positive-alpha pixels16210.
- HFIQH4 header357550: 167×171, positive-alpha pixels16001.
- JD223U header382430: 164×165, positive-alpha pixels15953.
- BOMYYU header407790: 172×166, positive-alpha pixels17469.
- I.SA15 header440503: 162×166, positive-alpha pixels15540.
- 19M7573 header466151: 187×169, positive-alpha pixels18137.
- 10QNLV6 header503786: 180×171, positive-alpha pixels15950.
- 6NZVCO header529717: 134×169, positive-alpha pixels17496.
- 123ZV2K header562899: 134×159, positive-alpha pixels15666.
- N7_BD2 header586761: 115×93, positive-alpha pixels7866.
- OVPI55 header599005: 171×171, positive-alpha pixels16812.
- M14PJO header627433: 165×166, positive-alpha pixels16210.
- 147NHI3 header655043: 167×171, positive-alpha pixels16001.
- NT3VZJ header681734: 164×165, positive-alpha pixels15953.
- 13XJ8WZ header709043: 172×166, positive-alpha pixels17469.
- PBP954 header744577: 162×166, positive-alpha pixels15540.
- BXKMUV header772427: 187×169, positive-alpha pixels18138.
- 44JWFR header812718: 180×171, positive-alpha pixels15945.
- 187SWBX header840696: 134×169, positive-alpha pixels17519.
- .VNGE7 header876445: 135×159, positive-alpha pixels15687.
- 961G2D header902425: 116×93, positive-alpha pixels7885.
### N007.jet

- 1FDFQ7O header0: 852×1136, positive-alpha pixels967872.
- 1A58C48 header721195: 96×143, positive-alpha pixels7646.
- DLOJIP header738318: 844×1136, positive-alpha pixels462336.
- VAP_Q0 header1395909: 178×491, positive-alpha pixels87398.
- BDLQGC header1487257: 178×491, positive-alpha pixels87398.
- VQOBWO header1578611: 178×491, positive-alpha pixels87398.
- 15DTEF1 header1670431: 178×491, positive-alpha pixels87398.
- M5L16G header1762500: 178×491, positive-alpha pixels87398.
- 19AGPF_ header1854831: 178×491, positive-alpha pixels87398.
- C0ERQF header1946021: 178×491, positive-alpha pixels87398.
- F037QU header2036239: 178×491, positive-alpha pixels87398.
- WAYDUF header2127350: 178×491, positive-alpha pixels87398.
- 140CWON header2217882: 178×491, positive-alpha pixels87398.
- 1BW28E2 header2308494: 178×491, positive-alpha pixels87398.
- 18.G4.2 header2399763: 1024×1024, positive-alpha pixels506149.
- N007_A: 45 regions validate through original N007_ST S2→I2 graph; see closure below.
- N007_B header3272414/RW156472 SHA256 `c0e9562bfb437a75a95c58deffb7723e4413120fa45a56547f2788437be2d3b3` external symbols .
### ST901.jet

- VKNCUG header0: 852×1136, positive-alpha pixels967872.
- 18YPIEC header501045: 480×568, positive-alpha pixels272640.
- _4.76. header576851: 500×280, positive-alpha pixels124855.
- 1139ZCW header595260: 445×280, positive-alpha pixels88257.
- OLK50X header623913: 395×230, positive-alpha pixels44375.
- 19NY._L header644736: 314×230, positive-alpha pixels72220.

122 complete PNG/I2 images decoded with positive alpha. C007_SND/C018_SND already selected E02/E03. All candidate packages preserved in full; binary attachment/skin/timeline/native render unverified. Exact atlas-key/bounds exceptions below must be resolved before claiming full graph closure; do not create aliases from this report.

- N007 atlas direct-image-key exception resolved through original S2 descriptor below.

## N007 atlas sprite page closure

Original N007_A names N007_ST.png. N007_ST is an original **S2 descriptor**, not an absent image: header3267529/packed66/SHA256 `293fadee3c7fd1ff73ba8a3967e49bd00a77bc864d9f88fde3adcafb72bd1003`, imageID3720767722→same-pack I2 header2399763/packed213731, 1024×1024, positive-alpha pixels506149. All 45 original atlas rotated rectangles validate against that image. No invented alias added. This closes the original descriptor/image graph; native Spine page-loading consumer semantics/render remain unverified. Earlier direct-PNG-key absence is superseded by this source-backed S2 edge.
