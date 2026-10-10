# E05 original entry and material audit

2026-10-08. Reads original PAD/recovered JSON; only report written. No ADB/Ghidra/runtime/server/profile/save edits. Native residency/playback pending.

## Progression and reward

Original reward `{"item": [{"ref_id": "AIRSHIP_TICKET", "qty": 20}], "free_iap": 0}`. AIRSHIP_TICKET×20 is original identity/quantity. Existing replica credits20 Search Capsules through additive item receipts and durable reward marker; all-descendant gate, idempotency and transaction policy are local reconstruction, not recovered original settlement. No grant performed.
- E05_S01: EP_1001A, battle=False, {"localname": "local_MIDGARD", "x": 1235, "y": 1150}, portrait C003_DIALOG.
- E05_S02: EP_1002B, battle=False, {"localname": "local_MISSINGTOWN", "x": 840, "y": 1260}, portrait C003_DIALOG.
- E05_S03: EP_1003A, battle=False, {"localname": "local_MISSINGTOWN", "x": 840, "y": 1260}, portrait C003_DIALOG.
- E05_S04: EP_1004A, battle=True, {"localname": "local_CAMP", "x": 900, "y": 1210}, portrait C005_DIALOG.
- E05_S05: EP_1005A, battle=False, {"localname": "local_CAMP", "x": 900, "y": 1210}, portrait C005_DIALOG.
- E05_S06: EP_1102A, battle=True, {"localname": "local_GREYWOOD", "x": 860, "y": 1130}, portrait C005_DIALOG.
- E05_S07: EP_1103A, battle=False, {"localname": "local_GREYWOOD", "x": 860, "y": 1130}, portrait C005_DIALOG.
- E05_S08: EP_1201A, battle=False, {"localname": "local_GREYWOOD", "x": 860, "y": 1130}, portrait C005_DIALOG.

S02 usesEP_1002B. Both combat stage_name strings E05_S05_TITLE conflict with actual linksS04/S06. Follow original SEASON1 andcombat_goto, not display label. Literal RES1 unchanged.

## Dialogue paths

Every IsRoot/outgoing path visits all nodes; no branch/nonempty condition. Text counts include narration. Fades ignore taps; inspect final displayed line before terminal.

### EP_1001A

Header2499569/packed2166/RW27834; SHA256 `c9bf60acbb37b53997be124e66fe62fa17968618b3611de554368595d5833b37`. 19 nodes/16 texts. Path 0→1→2→3→4→24→5→6→7→8→9→10→12→14→15→20→21→22→23.
First node2 Lana: %user_name%, did you enjoy your holiday?
**Final node22 Lana: Ok. Always put safety first. Never let your guard down in the outskirts.**
Terminal23: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Lana/NPC001.
Dependencies N001_BG.

### EP_1002B

Header2501759/packed2243/RW30981; SHA256 `16a68ef59343e7d9e01fe637612d2ae2be50f62edd0e2e2d7e7d56426199482c`. 21 nodes/18 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→14→15→16→17→18→19→20.
First node2 %user_name%: Hmm... According to the map, we should be really close to our destination.
**Final node19 Acerola: The village no longer exists.**
Terminal20: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Acerola/Char030, Tyltyl/Char004.
Dependencies BG007_1, BGM_COMIC1.

### EP_1003A

Header2504026/packed1802/RW20300; SHA256 `7cd4cbdea99c1b083eabc11c9c7fa003b9111e61b96621622403d18c8ab52176`. 13 nodes/10 texts. Path 0→1→2→3→4→19→20→21→22→23→5→24→18.
First node2 %user_name%: What do you mean it no longer exists?
**Final node24 Acerola: Hmm... Follow me if you'd like to find out.**
Terminal18: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Acerola/Char030, Tyltyl/Char004.
Dependencies BG007_1, BGM_GULLVEIG.

### EP_1004A

Header2505852/packed2290/RW32210; SHA256 `84c03ecd6fe27f7653d2b403ba3765867de1c92139280bc13d58aa22961bf6cb`. 21 nodes/17 texts. Path 0→1→2→3→4→6→7→8→9→10→32→11→12→13→33→34→35→36→37→38→25.
First node2 : ...!!!
**Final node38 Looter Gang Boss: Don’t you underestimate us. We are much tougher than last time!**
Terminal25: `scr-fade duration:0.6 color:(0,0,0,0) ; wait duration:0.6 ; combat_goto id:CB0501`.
Speakers %user_name%/Char009, Tyltyl/Char004, Acerola/Char030, Looter Gang Boss/NPC500, Looter Gang Henchmen/NPC501.
Dependencies BG005_1, BGM_BATTLE2, BGM_D_START, BGM_LANA, CUTIN_E0401.

### EP_1005A

Header2510029/packed1964/RW23078; SHA256 `cc58e8869c1145a27cc1048e202f8bbd7e3684141215b9c2ec46d8f84bb22f19`. 15 nodes/12 texts. Path 0→1→28→32→29→30→31→14→16→22→23→24→26→27→25.
First node28 %user_name%: Acerola, have you been taking care of all the refugees just by yourself?
**Final node27 %user_name%: Sure. We love helping others in need.**
Terminal25: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,0) ; wait duration:0.6`.
Speakers %user_name%/Char009, Tyltyl/Char004, Acerola/Char030.
Dependencies BG007_1.

### EP_1102A

Header2513434/packed1949/RW25532; SHA256 `a0bdb206b75e174601a9eb85e018cb9dca8d202240fa17c5ee8ab8470469e110`. 17 nodes/14 texts. Path 0→1→2→3→4→5→6→7→9→10→11→12→13→14→17→15→16.
First node2 Tyltyl: I think we are supposed to be near the path Acerola told us about...
**Final node15 Narration: CLASH-!**
Terminal16: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0502`.
Speakers %user_name%/Char009, Karl Steiner/Char012, Tyltyl/Char004.
Dependencies BG007_1, BGM_BATTLE2, BGM_LANA.

### EP_1103A

Header2517194/packed2361/RW32441; SHA256 `353a170a132908c0d4044aaa326758db765d34167e8d8e41696ce7a965f7d229`. 22 nodes/19 texts. Path 0→1→2→3→6→7→8→9→10→11→12→14→15→17→19→25→20→21→22→23→24→16.
First node2 %user_name%: Vincent used to be a captain in Midgard?
**Final node24 %user_name%: Tyltyl. I'm so confused. Can you give me a minute?**
Terminal16: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Karl Steiner/Char012, Tyltyl/Char004.
Dependencies BG007_1, BGM_GULLVEIG.

### EP_1201A

Header2519579/packed1832/RW21566; SHA256 `cbfe63008088a24cd95efd28ea05ef80124657c862504fc0fe284b6c17447e1e`. 14 nodes/11 texts. Path 0→1→2→3→4→5→6→14→7→8→9→10→11→13.
First node2 : ZZZZ- ZZZ...
**Final node11 Tyltyl: I knew this guy was the type to hold grudges. You are not cool at all!**
Terminal13: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers %user_name%/Char009, Karl Steiner/Char012, Tyltyl/Char004.
Dependencies BG007_1, BGM_COMIC1.

### EP_1004B

Header2508166/packed1839/RW21378; SHA256 `5b82c73fb9dcfb92a8934b99cd6c5fd073c1c5361dbd599150001e426c0ddf8f`. 13 nodes/10 texts. Path 0→1→33→34→35→36→37→38→39→40→41→42→25.
First node33 Looter Gang Boss: Ugh... We lost. There's no other option now...
**Final node42 Acerola: We built this place to save lives.**
Terminal25: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,0) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers %user_name%/Char009, Tyltyl/Char004, Acerola/Char030, Looter Gang Boss/NPC500, Looter Gang Henchmen/NPC501.
Dependencies BG005_1, BGM_BATTLE2, BGM_GULLVEIG.

### EP_1102B

Header2515407/packed1763/RW19010; SHA256 `19faa63120eea3a185ed2350603c46736c73652e03f958433248c7e1d1c52e84`. 12 nodes/9 texts. Path 0→1→2→3→4→5→6→11→7→8→10→9.
First node2 Karl Steiner: From this fight, I can tell. You are not Vincent. At least, not now...
**Final node10 %user_name%: Tyltyl...? You know something about this too?**
Terminal9: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers %user_name%/Char009, Karl Steiner/Char012, Tyltyl/Char004.
Dependencies BG007_1, BGM_TRAIN.

## Combat

Original CB0501: `{"id":"CB0501","title":"E05_TITLE","stage_name":"E05_S05_TITLE","power":"9000","game_res_id":"7","bgm":"BGM_BATTLE2","field_bg_res":"BG_RES","win_dialog":"EP_1004B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{}]],"right":[[{"type":"monster","actor_id":"CB0501_M1","thumb":{"level":20,"rank":3,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0501_M2","thumb":{"level":20,"rank":3,"hyper":0,"attr":2},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0501_M3","thumb":{"level":20,"rank":3,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0501_M4","thumb":{"level":20,"rank":3,"hyper":0,"attr":3},"skill":[0,0,0,0,0]},{"type":"monster","actor_id":"CB0501_BOSS","thumb":{"level":1,"rank":4,"hyper":0,"attr":1},"skill":[0,0,0,0,0]}]]}`.
Original CB0502: `{"id":"CB0502","title":"E05_TITLE","stage_name":"E05_S05_TITLE","power":"11000","game_res_id":"7","bgm":"BGM_BATTLE2","field_bg_res":"BG_RES","win_dialog":"EP_1102B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{}]],"right":[[{"type":"hunter","actor_id":"CB0502_012_1","thumb":{"level":10,"rank":4,"hyper":0,"attr":3},"skill":[1,1,0,1,0]}]]}`.
- CB0501_M1 resM046/role2/attr2/cool_time5000: `{"rank": "3", "hp": "1000", "atk": "1200", "def": "180", "spd": "0", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "attr_enhance": "0", "block_chance": "20.00", "block_dec_dmg": "20", "attr_resist": "0", "hp_regen": "20"}`; skill type/target_rank [].
- CB0501_M2 resM052/role2/attr2/cool_time5000: `{"rank": "3", "hp": "1000", "atk": "1200", "def": "180", "spd": "0", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "attr_enhance": "0", "block_chance": "20.00", "block_dec_dmg": "20", "attr_resist": "0", "hp_regen": "20"}`; skill type/target_rank [].
- CB0501_M3 resM048/role2/attr3/cool_time5000: `{"rank": "3", "hp": "1000", "atk": "1200", "def": "180", "spd": "0", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "attr_enhance": "0", "block_chance": "20.00", "block_dec_dmg": "20", "attr_resist": "0", "hp_regen": "20"}`; skill type/target_rank [].
- CB0501_M4 resM054/role2/attr3/cool_time5000: `{"rank": "3", "hp": "1000", "atk": "1200", "def": "180", "spd": "0", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "attr_enhance": "0", "block_chance": "20.00", "block_dec_dmg": "20", "attr_resist": "0", "hp_regen": "20"}`; skill type/target_rank [].
- CB0501_BOSS resM062/role2/attr1/cool_time5000: `{"rank": "4", "hp": "2000", "atk": "1500", "def": "210", "spd": "0", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "attr_enhance": "0", "block_chance": "20.00", "block_dec_dmg": "30", "attr_resist": "0", "hp_regen": "30"}`; skill type/target_rank [].
- CB0502_012_1 resC012/role1/attr3/cool_time5000: `{"rank": "4", "hp": "2500", "atk": "850", "def": "220", "spd": "5.00", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0", "block_chance": "30.00", "block_dec_dmg": "40", "attr_resist": "0", "hp_regen": "0"}`; skill type/target_rank [[1, 1], [2, 2], [4, 4]].

Four owned left placeholders in both. Expected CB0501 serial5–9/camp1 in listed order; CB0502 Karl serial5/camp1. Native corroboration pending. JSONmonster alone does not prove nativeMob. No globalmonster fixture, ownedKarl/Acerola or stat promotion follows.

## Owner inventory

774 PAD packs walked to exact EOF; +8 packed size/+12ID, total+0/part+4. Split image chunks reassemble sameID to total length. Texture IDs may be opaque numeric keys; base38 rendering is not a semantic texture name. Selection compared saved base plus explicit overlays throughE04, never sourced. Embedded base-pack duplicate coverage not exhaustive.
- BG005_1: DIAL_BG2.jet header2972816/packed32.
- BG007_1: DIAL_BG2.jet header2973092/packed32.
- BGM_BATTLE2: SND1.jet header1358916/packed479408.
- BGM_COMIC1: SND_CDN.jet header4074657/packed682118.
- BGM_D_START: SND1.jet header2990616/packed479826.
- BGM_GULLVEIG: SND1.jet header3470466/packed646624.
- BGM_LANA: SND1.jet header4117114/packed585184.
- BGM_TRAIN: SND_CDN.jet header6514908/packed929968.
- CUTIN_E0401: CUT_E0401.jet header659614/packed61.
- N001_BG: N001_BG.jet header2282340/packed49.
- M046_: M016.jet.
- M052_: M018.jet.
- M048_: M016.jet.
- M054_: M018.jet.
- M062_: M021.jet.

Original ENV_INFO row7 `7,하얀숲,STI001,111,-5,0,11,-20,160,111,-40,210,111,-60,580,111,-20,850`. PrefixSTI001 ownerST001.jet. No ST007 inference or numeric suffix aliases.

**Additive minimum 9 packs: C012.jet, C012_EFT.jet, C012_Q.jet, C012_SND.jet, C030.jet, CUT_E0401.jet, M016.jet, M018.jet, N001.jet.**
C030 base coversAcerola portrait only; C012fullbase/Q/EFT/SND forKarl. No numbered voice references; no newVOICE_CDN justified.

- C004.jet: 1246194 bytes; SHA256 `403634344564e6e6c889607ee4fa202b5b4d2b4ef066d52d2e611139ede743df`; selected.
- C009.jet: 3101288 bytes; SHA256 `98dc7e66efc1f3b4453966cf6ed09f1cab20af12b158eed1b51355b8cec798c5`; selected.
- C012.jet: 1795342 bytes; SHA256 `308bd36707873b09fb750baf3fe1c1830458521b01cd90eb5f838b3a4cce7f57`; **missing**.
- C012_EFT.jet: 3592464 bytes; SHA256 `d6cbe39b9da296f5ba6271e08a89d87d945eb0d9e3833563ad7d26f59a019bd2`; **missing**.
- C012_Q.jet: 54305 bytes; SHA256 `37b022a9949b6a2ec16df563522e416cfe0f90652aae47ceb21c2f81d389fa4b`; **missing**.
- C012_SND.jet: 109636 bytes; SHA256 `9f660ea0374ce7423c70c3924a583d6f0ee1ae4aac6899ef0bdac8a335629add`; **missing**.
- C030.jet: 587812 bytes; SHA256 `f997f429d8fce9ac8631cb9208e12da6eb6c19541e545fd840a69d05866d94fb`; **missing**.
- CUT_E0401.jet: 659699 bytes; SHA256 `9b1d133c8562c446d799c85a45eb73f9a338a42fa75eb9bff746db6dfb5e4ee6`; **missing**.
- DIAL_BG2.jet: 2973203 bytes; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; selected.
- M016.jet: 1597837 bytes; SHA256 `ab40de921dec9d9f5fcb292870534dc3c37f88443067dccd5d6b4de2c38061f2`; **missing**.
- M018.jet: 837454 bytes; SHA256 `6c77291f4918548fb777c982e86d9bd67b4b3c920622271782693d76da0490ae`; **missing**.
- M021.jet: 1015930 bytes; SHA256 `3c623ebdcfc2db86b66ddabcd09be8d08c008335286e1494dbbfdd8ef78dd328`; selected.
- N001.jet: 869436 bytes; SHA256 `a54b3997bf8f2b60f4a0ae787d9a926c2a9188f0fb6661f1e153e3b4cc9cb6e8`; **missing**.
- N001_BG.jet: 2282467 bytes; SHA256 `4d09c9eaf150befb7adc3a32919bdba6247ceb2097d5cac069de5da48fcb3d40`; selected.
- N500.jet: 220037 bytes; SHA256 `a362f88ce48fb503dc035de13f446854282d43e75478cff6def375a2998d7f5c`; selected.
- N501.jet: 222917 bytes; SHA256 `fb76b2c0a27cde2d257dc493c4603049bbae49436ab21c8028a25d8c4ffd4053`; selected.
- SND1.jet: 7173961 bytes; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; selected.
- SND_CDN.jet: 10911430 bytes; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; selected.
- ST001.jet: 1733825 bytes; SHA256 `9948876a679a9cfce6a88233c7985e82b641137f639fae2aff8167e614e32cd7`; selected.

## Closed original material edges

AT count+43/frames+47 with14-byte prefix plus variable uint16 event length+12. S2 textureID+46. Every cursor consumes exact body; image fragments reassembled and decoded with positive alpha. Opaque texture IDs retained as numeric.

### C012_Q.jet

- C012_WP → C012_WEP → imageIDs 742910289.
- C012_AM → C012_AMOR → imageIDs 1939206917.
- C012_AC → C012_ACCRY → imageIDs 3870518965.
- C012_TH → C012_THN → imageIDs 4093732542.
- C012_STH → C012_STHN → imageIDs 910776506.
- C012_SI1 → C012_SI01 → imageIDs 905183120.
- C012_SI2 → C012_SI02 → imageIDs 2962310142.
- C012_SI3 → C012_SI03 → imageIDs 876696030.
- C012_SI4 → C012_SI04 → imageIDs 3096304446.
- C012_SI5 → C012_SI05 → imageIDs 2944414770.
- C012_SHADOW → C012_SHA → imageIDs 4013766782.

### C012_EFT.jet


### M016.jet

- M046_AS1 → M046_SHA → imageIDs 3769080934.
- M046_AS2 → M046_SHA → imageIDs 3769080934.
- M046_AS3 → M046_SHA → imageIDs 3769080934.
- M046_DIE → M046_H10 → imageIDs 1783974635.
- M046_H1 → M046_H01,M046_H02,M046_H03,M046_H04,M046_H05 → imageIDs 446417401,1124991248.
- M046_H2 → M046_H06,M046_H07,M046_H08,M046_H09,M046_H10 → imageIDs 2799990288,1783974635.
- M046_H3 → M046_H11,M046_H12,M046_H13,M046_H14,M046_H15 → imageIDs 2389914419,3573182038.
- M046_R1 → M046_R01,M046_R02,M046_R03,M046_R04 → imageIDs 601385463,308052371,1805205046,4215620929.
- M046_R2 → M046_R01,M046_R02,M046_R03,M046_R04 → imageIDs 601385463,308052371,1805205046,4215620929.
- M046_S → M046_R01,M046_R02,M046_R03,M046_R04 → imageIDs 601385463,308052371,1805205046,4215620929.
- M046_SHADOW → M046_SHA → imageIDs 3769080934.
- M046_TH → M046_THN → imageIDs 1169659811.
- M048_AS1 → M046_SHA → imageIDs 3769080934.
- M048_AS2 → M046_SHA → imageIDs 3769080934.
- M048_AS3 → M046_SHA → imageIDs 3769080934.
- M048_DIE → M048_H10 → imageIDs 205783739.
- M048_H1 → M048_H01,M048_H02,M048_H03,M048_H04,M048_H05 → imageIDs 3231760957,3603554789.
- M048_H2 → M048_H06,M048_H07,M048_H08,M048_H09,M048_H10 → imageIDs 4021134233,205783739.
- M048_H3 → M048_H11,M048_H12,M048_H13,M048_H14,M048_H15 → imageIDs 4008388516,1423417888.
- M048_R1 → M048_R01,M048_R02,M048_R03,M048_R04 → imageIDs 435911950,1262117387,2850166098,3996276104.
- M048_R2 → M048_R01,M048_R02,M048_R03,M048_R04 → imageIDs 435911950,1262117387,2850166098,3996276104.
- M048_S → M048_R01,M048_R02,M048_R03,M048_R04 → imageIDs 435911950,1262117387,2850166098,3996276104.
- M048_SHADOW → M046_SHA → imageIDs 3769080934.
- M048_TH → M048_THN → imageIDs 2298889524.

### M018.jet

- M052_AS1 → M052_SHA → imageIDs 2713260599.
- M052_AS2 → M052_SHA → imageIDs 2713260599.
- M052_AS3 → M052_SHA → imageIDs 2713260599.
- M052_DIE → M052_H10 → imageIDs 1008973402.
- M052_H1 → M052_H01,M052_H02,M052_H03,M052_H04,M052_H05 → imageIDs 3718586919,4103345285.
- M052_H2 → M052_H06,M052_H07,M052_H08,M052_H09,M052_H10 → imageIDs 2991718431,1008973402.
- M052_H3 → M052_H11,M052_H12,M052_H13,M052_H14,M052_H15 → imageIDs 1339604905,3612369167.
- M052_R1 → M052_R01,M052_R02,M052_R03,M052_R04 → imageIDs 353768306,397813193,1239908804,775004379.
- M052_R2 → M052_R01,M052_R02,M052_R03,M052_R04 → imageIDs 353768306,397813193,1239908804,775004379.
- M052_S → M052_R01,M052_R02,M052_R03,M052_R04 → imageIDs 353768306,397813193,1239908804,775004379.
- M052_SHADOW → M052_SHA → imageIDs 2713260599.
- M052_TH → M052_THN → imageIDs 3546341723.
- M054_AS1 → M054_SHA → imageIDs 2713260599.
- M054_AS2 → M054_SHA → imageIDs 2713260599.
- M054_AS3 → M054_SHA → imageIDs 2713260599.
- M054_DIE → M054_H10 → imageIDs 9979693.
- M054_H1 → M054_H01,M054_H02,M054_H03,M054_H04,M054_H05 → imageIDs 369164555,1785964337.
- M054_H2 → M054_H06,M054_H07,M054_H08,M054_H09,M054_H10 → imageIDs 3397884670,9979693.
- M054_H3 → M054_H11,M054_H12,M054_H13,M054_H14,M054_H15 → imageIDs 667664542,680859963.
- M054_R1 → M054_R01,M054_R02,M054_R03,M054_R04 → imageIDs 524488407,3812438156,922516679,1535648427.
- M054_R2 → M054_R01,M054_R02,M054_R03,M054_R04 → imageIDs 524488407,3812438156,922516679,1535648427.
- M054_S → M054_R01,M054_R02,M054_R03,M054_R04 → imageIDs 524488407,3812438156,922516679,1535648427.
- M054_SHADOW → M054_SHA → imageIDs 2713260599.
- M054_TH → M054_THN → imageIDs 3854561281.

### M021.jet

- M062_AS1 → M062_SHA → imageIDs 4216754979.
- M062_AS2 → M062_SHA → imageIDs 4216754979.
- M062_AS3 → M062_SHA → imageIDs 4216754979.
- M062_DIE → M062_H10 → imageIDs 619403929.
- M062_H1 → M062_H01,M062_H02,M062_H03,M062_H04,M062_H05 → imageIDs 1965177616,3770708396.
- M062_H2 → M062_H06,M062_H07,M062_H08,M062_H09,M062_H10 → imageIDs 971289935,619403929.
- M062_H3 → M062_H11,M062_H12,M062_H13,M062_H14,M062_H15 → imageIDs 417778287,921861798.
- M062_R1 → M062_R01,M062_R02,M062_R03,M062_R04 → imageIDs 1186265042,733726149,2150893338,2128790451.
- M062_R2 → M062_R01,M062_R02,M062_R03,M062_R04 → imageIDs 1186265042,733726149,2150893338,2128790451.
- M062_S → M062_R01,M062_R02,M062_R03,M062_R04 → imageIDs 1186265042,733726149,2150893338,2128790451.
- M062_SHADOW → M062_SHA → imageIDs 4216754979.
- M062_TH → M062_THN → imageIDs 3145834786.

### ST001.jet

- ST000BG → ST000_BG1,ST000_BG2,ST000_BG3,ST000_BG4,ST000_BG5,ST000_BG6,ST000_BG7 → imageIDs 1602541050.
- ST001BG → ST001_BG → imageIDs 617658326.
- STI000B → STI001B_01 → imageIDs 4164470819.
- STI000_A1 → STI001_A01 → imageIDs 4206206551.
- STI000_B1 → STI001_B01 → imageIDs 337455804.
- STI000_C1 → STI001_C01 → imageIDs 773052973.
- STI000_D1 → STI001_D01 → imageIDs 78091620.
- STI001B → STI001B_01 → imageIDs 4164470819.
- STI001_A1 → STI001_A01 → imageIDs 4206206551.
- STI001_B1 → STI001_B01 → imageIDs 337455804.
- STI001_C1 → STI001_C01 → imageIDs 773052973.
- STI001_D1 → STI001_D01 → imageIDs 78091620.
- STI000_E1 → STI001_E01 → imageIDs 78091620.
- STI001_E1 → STI001_E01 → imageIDs 78091620.

### CUT_E0401.jet

- CUTIN_E0401 → CUTIN_E0401S → imageIDs 2918130229.
- ImageID9979693: 148×168, positive-alpha pixels12921 [M018.jet].
- ImageID78091620: 424×230, positive-alpha pixels97520 [ST001.jet].
- ImageID205783739: 202×189, positive-alpha pixels16806 [M016.jet].
- ImageID211339070: 110×110, positive-alpha pixels9661 [C012_Q.jet].
- ImageID308052371: 198×173, positive-alpha pixels17407 [M016.jet].
- ImageID337455804: 453×280, positive-alpha pixels111633 [ST001.jet].
- ImageID353768306: 139×179, positive-alpha pixels14677 [M018.jet].
- ImageID369164555: 134×180, positive-alpha pixels15720 [M018.jet].
- ImageID397813193: 144×175, positive-alpha pixels14236 [M018.jet].
- ImageID417778287: 167×193, positive-alpha pixels20246 [M021.jet].
- ImageID435911950: 220×177, positive-alpha pixels18112 [M016.jet].
- ImageID446417401: 192×176, positive-alpha pixels18748 [M016.jet].
- ImageID524488407: 139×179, positive-alpha pixels14677 [M018.jet].
- ImageID601385463: 220×177, positive-alpha pixels18106 [M016.jet].
- ImageID617658326: 852×1136, positive-alpha pixels967872 [ST001.jet].
- ImageID619403929: 229×177, positive-alpha pixels18156 [M021.jet].
- ImageID667664542: 122×175, positive-alpha pixels14649 [M018.jet].
- ImageID680859963: 122×170, positive-alpha pixels13770 [M018.jet].
- ImageID733726149: 161×188, positive-alpha pixels18263 [M021.jet].
- ImageID742910289: 71×81, positive-alpha pixels1626 [C012_Q.jet].
- ImageID773052973: 892×230, positive-alpha pixels164432 [ST001.jet].
- ImageID775004379: 136×174, positive-alpha pixels14065 [M018.jet].
- ImageID807860344: 91×91, positive-alpha pixels6481 [M016.jet].
- ImageID876696030: 64×64, positive-alpha pixels2293 [C012_Q.jet].
- ImageID905183120: 64×64, positive-alpha pixels2472 [C012_Q.jet].
- ImageID910776506: 175×208, positive-alpha pixels31817 [C012_Q.jet].
- ImageID921861798: 167×183, positive-alpha pixels18169 [M021.jet].
- ImageID922516679: 118×179, positive-alpha pixels13305 [M018.jet].
- ImageID971289935: 236×185, positive-alpha pixels20644 [M021.jet].
- ImageID1008973402: 148×168, positive-alpha pixels12921 [M018.jet].
- ImageID1124991248: 185×172, positive-alpha pixels17216 [M016.jet].
- ImageID1169659811: 124×102, positive-alpha pixels8161 [M016.jet].
- ImageID1186265042: 153×192, positive-alpha pixels16842 [M021.jet].
- ImageID1239908804: 118×179, positive-alpha pixels13305 [M018.jet].
- ImageID1262117387: 198×173, positive-alpha pixels17357 [M016.jet].
- ImageID1339604905: 122×175, positive-alpha pixels14649 [M018.jet].
- ImageID1423417888: 209×158, positive-alpha pixels17598 [M016.jet].
- ImageID1535648427: 136×174, positive-alpha pixels14065 [M018.jet].
- ImageID1602541050: 852×1136, positive-alpha pixels967872 [ST001.jet].
- ImageID1783974635: 199×192, positive-alpha pixels16811 [M016.jet].
- ImageID1785964337: 129×180, positive-alpha pixels14493 [M018.jet].
- ImageID1805205046: 191×177, positive-alpha pixels16520 [M016.jet].
- ImageID1939206917: 67×86, positive-alpha pixels4143 [C012_Q.jet].
- ImageID1965177616: 154×193, positive-alpha pixels18943 [M021.jet].
- ImageID2128790451: 152×186, positive-alpha pixels17716 [M021.jet].
- ImageID2150893338: 142×192, positive-alpha pixels17852 [M021.jet].
- ImageID2298889524: 124×102, positive-alpha pixels8130 [M016.jet].
- ImageID2389914419: 209×165, positive-alpha pixels19754 [M016.jet].
- ImageID2713260599: 157×31, positive-alpha pixels3886 [M018.jet].
- ImageID2799990288: 204×197, positive-alpha pixels18983 [M016.jet].
- ImageID2850166098: 191×177, positive-alpha pixels16476 [M016.jet].
- ImageID2918130229: 852×1136, positive-alpha pixels967872 [CUT_E0401.jet].
- ImageID2944414770: 64×64, positive-alpha pixels1652 [C012_Q.jet].
- ImageID2962310142: 64×64, positive-alpha pixels2007 [C012_Q.jet].
- ImageID2991718431: 152×173, positive-alpha pixels13849 [M018.jet].
- ImageID3096304446: 64×64, positive-alpha pixels1969 [C012_Q.jet].
- ImageID3145834786: 121×113, positive-alpha pixels10078 [M021.jet].
- ImageID3231760957: 209×170, positive-alpha pixels18806 [M016.jet].
- ImageID3397884670: 152×173, positive-alpha pixels13847 [M018.jet].
- ImageID3546341723: 104×107, positive-alpha pixels8265 [M018.jet].
- ImageID3573182038: 210×158, positive-alpha pixels17687 [M016.jet].
- ImageID3603554789: 202×170, positive-alpha pixels17242 [M016.jet].
- ImageID3612369167: 122×170, positive-alpha pixels13770 [M018.jet].
- ImageID3718586919: 134×180, positive-alpha pixels15720 [M018.jet].
- ImageID3769080934: 157×31, positive-alpha pixels3886 [M016.jet].
- ImageID3770708396: 144×193, positive-alpha pixels16902 [M021.jet].
- ImageID3812438156: 144×175, positive-alpha pixels14236 [M018.jet].
- ImageID3854561281: 102×106, positive-alpha pixels8184 [M018.jet].
- ImageID3870518965: 49×51, positive-alpha pixels1864 [C012_Q.jet].
- ImageID3906126428: 91×91, positive-alpha pixels6481 [M018.jet].
- ImageID3996276104: 195×172, positive-alpha pixels17294 [M016.jet].
- ImageID4006529217: 96×97, positive-alpha pixels1887 [C012_Q.jet].
- ImageID4008388516: 209×165, positive-alpha pixels19772 [M016.jet].
- ImageID4013766782: 84×29, positive-alpha pixels1791 [C012_Q.jet].
- ImageID4021134233: 207×191, positive-alpha pixels18945 [M016.jet].
- ImageID4088639591: 175×210, positive-alpha pixels36738 [C012_Q.jet].
- ImageID4093732542: 90×114, positive-alpha pixels7970 [C012_Q.jet].
- ImageID4103345285: 129×180, positive-alpha pixels14493 [M018.jet].
- ImageID4164470819: 480×568, positive-alpha pixels272640 [ST001.jet].
- ImageID4206206551: 441×280, positive-alpha pixels115202 [ST001.jet].
- ImageID4215620929: 195×172, positive-alpha pixels17336 [M016.jet].
- ImageID4216754979: 157×31, positive-alpha pixels3886 [M021.jet].

## Karl external skeleton symbols and original portraits

- C012_B RW135940/SHA256 `c2a77f92b6932b507479e2c1b2eae8ac3508ec6479f84bc7c8269f25e0cd780a`; C012_E01 [C012_EFT.jet],C012_E02 [C012_EFT.jet],C012_E03 [C012_EFT.jet],C012_EC [C012_EFT.jet],C012_SND01 [C012_SND.jet],C012_SND02 [C012_SND.jet],C012_SND03 [C012_SND.jet],C012_SND04 [C012_SND.jet].
- C012_DB RW834/SHA256 `f3a80348b4f15e4ebdd6d9516ec9e8fd516482cc22469937648e7e6c5a7f80ac`; no matching EFT/SND symbols.
- C012_A pageC012.png → C012 1024×1024, positive-alpha pixels286165.
- C012_DA pageC012_d.png → C012_D 1024×1024, positive-alpha pixels593302.
- C030_A pageC030.png → C030 1024×256, positive-alpha pixels140742.
- C030_DA pageC030_d.png → C030_D 1024×1024, positive-alpha pixels485419.
- N001_A pageN001.png → N001 1024×1024, positive-alpha pixels576835.
- N001_A pageN0012.png → N0012 512×256, positive-alpha pixels68116.

Atlas pages/symbol scan do not prove complete binary attachment/skin/timeline semantics. No native gameplay validation or owned grants. Current ordinary Hunter stats/levels are preserved, original enemystats may require meaningful skill/party play; do not weaken them to make a test pass. Native chapter reward20 remains pending.

### Atlas region rectangle validation

- C012_A: 68 original regions; every page exists and rotated rectangle lies within decoded texture dimensions.
- C012_DA: 8 original regions; every page exists and rotated rectangle lies within decoded texture dimensions.
- C030_A: 70 original regions; every page exists and rotated rectangle lies within decoded texture dimensions.
- C030_DA: 6 original regions; every page exists and rotated rectangle lies within decoded texture dimensions.
- N001_A: 31 original regions; every page exists and rotated rectangle lies within decoded texture dimensions.
