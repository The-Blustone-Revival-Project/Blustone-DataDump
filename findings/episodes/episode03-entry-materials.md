# E03 entry and original dialogue material audit

2026-10-08. Read-only original final PAD JETs, recovered local Episode JSON, and established resource-selection scripts. Only this report written. No ADB, Ghidra, server, state, profile or original-resource changes. Native E03 entry, combat and residency remain unverified.

## Sequence and exact progression identities

E03 has seven stories. Original reward is GC3 x3 plus GC4 x3, free_iap0. Coupon metadata, pool and redemption are not reconstructed; quantities alone do not justify grants. All seven `res1` values are literal RES1 in the preserved JSON; do not invent a resource alias.

- **E03_S01**: EP_0701A, battle=False, local_MIDGARD x1235/y1150, portrait C003_DIALOG.
- **E03_S02**: EP_0702A, battle=True, local_REDHILL x1040/y1150, portrait C003_DIALOG; combat CB0301.
- **E03_S03**: EP_0704A, battle=False, local_DENALI x1060/y1060, portrait C003_DIALOG.
- **E03_S04**: EP_0801A, battle=False, local_DENALI x1060/y1060, portrait C005_DIALOG.
- **E03_S05**: EP_0802A, battle=True, local_DENALI x1060/y1060, portrait C005_DIALOG; combat CB0302.
- **E03_S06**: EP_0803A, battle=False, local_REDHILL x1080/y1140, portrait C005_DIALOG.
- **E03_S07**: EP_0804A, battle=False, local_MIDGARD x1235/y1150, portrait C005_DIALOG.

**Original label mismatch:** CB0301.stage_name is E03_S03_TITLE, but SEASON1 links CB0301 to E03_S02, and EP_0702A terminal explicitly enters CB0301. Its win dialogue is EP_0703B. Do not use the combat stage_name to clear Story03. Story03 is nonbattle EP_0704A.

CB0301: four owned empty placeholders versus three CB0301_M1/M023 plus CB0301_013_1/C013 (Denali); game_res_id3/BGM_GULLVEIG. CB0302: four owned placeholders versus CB0302_010_1/C010 (Vincent); game_res_id7/BGM_BATTLE3. Both lose dialogs EP_0000A and EP_0000B. Fixed actors do not imply owned Denali/Vincent grants. Environment3→STI003/ST003 and environment7→STI001/ST001 are independently audited in the combat-material lane; never infer ST007 solely from game_res_id7.

## Dialogue traversal and exact terminal text

Every node is reached by following the outgoing graph from IsRoot=true; each route is linear, has at most one outgoing link per node, visits every declared node, and has no nonempty ConditionsString. Text includes narration. Source text counts bound observation; fades and auto-advancing narration can ignore taps or skip visible waits. Verify the final displayed line before a single terminal advance. Header+8 is packed length, +12 base38 uint64; inflated RW has XML at+6/UTF8 BOM. Hashes here are full inflated RW-record bytes, not only XML.

### EP_0701A

DIAL-EN header2467403, packed2205, RW29735, SHA256 `a5f45519be5ab1a7b88e3d238ce163cc7aaef86efd5ef4ecd1ee5c8e02762048`. 20 nodes/17 nonempty texts. Path 0→1→2→29→7→8→9→10→11→33→14→16→17→18→27→30→31→25→32→26.
First node2 Lana: Er... Can I ask you for a favor?
**Final node32 %user_name%: I will see you then.**
Terminal26: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Lana/NPC001.
Named script dependencies: C009_39_1, C009_39_2, C009_39_3, C009_39_4, C009_39_5, C009_39_6, N001_39_1, N001_39_10, N001_39_11, N001_39_2, N001_39_3, N001_39_4, N001_39_5, N001_39_6, N001_39_7, N001_39_8, N001_39_9, N001_BG.

### EP_0702A

DIAL-EN header2469632, packed2050, RW26133, SHA256 `bc5b753eb6dbd23f968644bcb7ba3877d328a84a40980d4267a39c0e05bb3b67`. 17 nodes/14 nonempty texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→14→22→21.
First node2 %user_name%: This place must be Crimson Chasm... I can't find anything special about it.
**Final node22 Denali: I am ready to fight with my full power this time, you'd better be ready for it...!**
Terminal21: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0301`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013.
Named script dependencies: BG004_1, BGM_TRAIN, C004_40_1, C004_40_2, C004_40_3, C004_40_4, C005_SND03, C009_40_1, C009_40_2, C009_40_3, C009_40_4, C013_40_1, C013_40_2, C013_40_3.

### EP_0704A

DIAL-EN header2474142, packed2260, RW31494, SHA256 `ad0bc17d4bad538f56c4d8166d800c21406d3833e6fa4d855fe622db395f9c86`. 21 nodes/18 nonempty texts. Path 0→1→2→3→5→6→9→10→11→12→13→14→15→16→17→27→28→29→22→23→24.
First node2 %user_name%: Denali, I've been thinking that you should be returning to the village with us.
**Final node23 %user_name%: Now, promise me you will come with us. Okay?**
Terminal24: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013.
Named script dependencies: C004_42, C009_42_1, C009_42_10, C009_42_2, C009_42_3, C009_42_4, C009_42_5, C009_42_6, C009_42_7, C009_42_8, C009_42_9, C013_42_1, C013_42_2, C013_42_3, C013_42_4, C013_42_5, C013_42_6, C013_42_7, N004_BG.

### EP_0801A

DIAL-EN header2476426, packed2276, RW29553, SHA256 `a388e036e24e3cd3ecc7ba4056cb5ed35466624c69249cf6b72a25cf2d857aee`. 19 nodes/15 nonempty texts. Path 0→1→2→3→4→23→5→6→8→9→10→12→13→15→24→16→25→21→22.
First node2 %user_name%: Ugh... I have so many things to report to Lana.
**Final node21 %user_name%: V-Vincent?!**
Terminal22: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013, Vincent/Char010.
Named script dependencies: BG001_2, BG006_2, BGM_BATTLE3, BGM_MOUSE, C004_43_1, C004_43_2, C005_SND03, C009_43_1, C009_43_2, C009_43_3, C009_43_4, C009_43_5, C009_43_6, C009_43_7, C010_43_1, C010_43_2, C010_43_3, C013_43_1, C013_43_2.

### EP_0802A

DIAL-EN header2478726, packed2586, RW34491, SHA256 `0568953a49d8f64a40dca3637a85c13c88331022912b3cdcd35a1c7e46e3d684`. 23 nodes/20 nonempty texts. Path 0→1→2→3→4→5→6→7→8→9→26→25→27→10→11→12→13→15→16→17→21→22→24.
First node2 %user_name%: Vincent... What are you trying to do?
**Final node22 %user_name%: Tyltyl, right now! Go!**
Terminal24: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0302`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Vincent/Char010.
Named script dependencies: BG001_2, BGM_BATTLE3, C004_44_1, C004_44_2, C004_44_3, C004_44_4, C009_44_1, C009_44_10, C009_44_11, C009_44_2, C009_44_3, C009_44_4, C009_44_5, C009_44_6, C009_44_7, C009_44_8, C009_44_9, C010_44_1, C010_44_2, C010_44_3, C010_44_4, FX_CLASH.

### EP_0803A

DIAL-EN header2483628, packed2093, RW25378, SHA256 `5a43b22e5f190968bc7672f5387dd8520e36a84da0e2a2841cdd3386a847207b`. 16 nodes/13 nonempty texts. Path 0→1→37→8→10→11→12→13→14→15→16→21→24→25→26→22.
First node37 %user_name%: Phew... That was scary. Why does that guy always bother me when I'm in a hurry?
**Final node26 %user_name%: If what you just said is true, Vincent will not stop looking for you.**
Terminal22: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013, Vincent/Char010.
Named script dependencies: BG006_2, C004_45_3, C009_45_10, C009_45_11, C009_45_12, C009_45_6, C009_45_7, C009_45_8, C009_45_9, C013_45_1, C013_45_2, C013_45_3, C013_45_4, C013_45_5.

### EP_0804A

DIAL-EN header2485745, packed2623, RW38886, SHA256 `c24583cea82c6ee4f59ae849644067d73857715c6b198e62c5659566e550f5d5`. 26 nodes/21 nonempty texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→30→27→29→26→12→24→23→13→14→15→16→25→28→22.
First node2 %user_name%: Lana... I'm back.
**Final node28 Lana: Last time, no one was ready for the disaster... We won't make the same mistake again.**
Terminal22: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Lana/NPC001, Denali/Char013, Beckhen & Jack/NPC003.
Named script dependencies: BGM_COMIC1, BGM_GULLVEIG, C009_46_1, C009_46_2, C009_46_3, C009_46_4, C009_46_5, C013_46, N001_46_1, N001_46_10, N001_46_11, N001_46_2, N001_46_3, N001_46_4, N001_46_5, N001_46_6, N001_46_7, N001_46_8, N001_46_9, N001_BG, N002_BG, N003_46_1, N003_46_2, N003_46_3, N003_46_4.

### EP_0703B

DIAL-EN header2471706, packed2412, RW31709, SHA256 `d68678ef2184db6fc145830b1e5b84314d706569a5cc7d39034fef681f47b4f3`. 21 nodes/18 nonempty texts. Path 0→1→2→3→5→6→8→9→26→27→28→11→12→13→14→15→17→21→22→23→24.
First node2 Tyltyl: Phew... Denali... How could you forget about me in just two years?
**Final node23 %user_name%: Vincent. He's creating so much trouble. What is he trying to do?**
Terminal24: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013.
Named script dependencies: BG004_1, BGM_LANA, C004_41_1, C004_41_2, C004_41_3, C009_41_1, C009_41_2, C009_41_3, C009_41_4, C009_41_5, C013_41_1, C013_41_10, C013_41_2, C013_41_3, C013_41_4, C013_41_5, C013_41_6, C013_41_7, C013_41_8, C013_41_9.

### EP_0802B

DIAL-EN header2481336, packed2268, RW29534, SHA256 `fdde75f34461d15d9a02884f0ffb3a3c24469e57df8ba5774b7634fa87efeb01`. 19 nodes/15 nonempty texts. Path 0→1→2→23→3→4→27→28→29→30→38→5→6→31→32→33→34→36→22.
First node2 Vincent: You have become much stronger. But you are still much weaker than your old self.
**Final node36 Narration: Getting rid of you is just a matter of time...**
Terminal22: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers: %user_name%/Char009, Tyltyl/Char004, Denali/Char013, Vincent/Char010.
Named script dependencies: BG001_2, BG004_1, BGM_BATTLE3, BGM_TRAIN, C004_45_1, C004_45_2, C009_45_1, C009_45_2, C009_45_3, C009_45_4, C009_45_5, C010_45_1, C010_45_2, C010_45_3, C010_45_4, C010_45_5, C010_45_6, C010_45_7, C010_45_8, CUTIN_E0301.

## Exact owner packs and additive missing selections

All 774 original top-level PAD .jet files were walked with 24-byte headers, seeking 24+packed-length per record and checking exact EOF. No nested/generated alias is inferred from absent outer names. Named dependency ownership below is exact original header evidence. Active comparison uses the saved replica activation selections plus existing Story04/Veteran/Bear/final-background/E02 overlays (root current 34 groups/70 folded assets, stamp1634672), without sourcing or changing environment.

**Missing explicit packs from dialogue headers plus fixed actor/environment candidates:** C010.jet, C010_EFT.jet, C010_Q.jet, C010_SND.jet, C013.jet, C013_EFT.jet, C013_Q.jet, C013_SND.jet, CUT_E0301.jet, N004.jet, ST003.jet, VOICE_CDN3.jet.

Independent combat-material inspection additionally found a **cross-family C018_SND01** request inside original C010_B skeleton bytes. Thus the complete additive set is **thirteen packs**, adding sound-only C018_SND.jet to the twelve header/candidate gaps above. No C018 owned/art/effect grant is implied. C018_SND.jet: 95425 bytes; SHA256 `e1b1ffaeb0dd44c9a01a87c1f225097ab99cef553b3bfb496d6643d244c1bf3d`. See episode03-combat-materials.md for that binary closure evidence.

No new pack is required by Story01 itself: N001_BG, voice9 Captain and voice8 Lana are already selected. Story02 needs original Denali C013 family; voices3 contain Denali and are newly required. Story03 additionally needs N004 for N004_BG. Later Vincent requires C010 family, and CB0302 win requires CUT_E0301. Other background/sound dependencies have existing selected owner packs. Q/EFT/SND candidate complete families are listed intentionally for fixed combat actors; generated portrait/Spine graph closure belongs to the separate combat audit. Do not add C010A/B or C013A/B variants from resemblance.

- C005_SND.jet: 211032 bytes/6 records; SHA256 `b5d7002b46e2fce102557866284df6ca424817c60d4788f120a40b942acfe5d7`; selected; exact names: C005_SND03.
- C010.jet: 2759458 bytes/9 records; SHA256 `3592c448aca8b7096f4adde8420e2ef19988cc6e452c23ef513f0e4fc6c59067`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C010_EFT.jet: 3818579 bytes/13 records; SHA256 `692d3a46d7eddf39fb9b526b713d171c9e79d1b250e6408aa231bf62d87eb797`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C010_Q.jet: 53683 bytes/45 records; SHA256 `f2a19358c627047df72baa8329428147e70f8a0d36960b1e0a3996301985955d`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C010_SND.jet: 175008 bytes/9 records; SHA256 `e32a4e85807a49e2961ebc5de7b178295c9c818c20816df92f85528ba1879df9`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C013.jet: 745049 bytes/6 records; SHA256 `be6a19cabdbecc1487fd2ba82588560c62de481012f398cbba78452862224733`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C013_EFT.jet: 3741764 bytes/6 records; SHA256 `4b673e0b3e3f84383629cb19d20ffcd04ada5bb25de6344714275c1dca662911`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C013_Q.jet: 47270 bytes/39 records; SHA256 `1a09892b4e9ac4809b83e9e60a54f768d790caf98024677e85726eba8dd8d583`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- C013_SND.jet: 115037 bytes/3 records; SHA256 `e46aa30fe6afc99b3ef9172a4aaa0fa3ebc3d1b499839e87a34f4cc2f6ba59ed`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- CUT_E0301.jet: 406759 bytes/6 records; SHA256 `e051215d2cf65bf1340279e175cce955020d7484af2188ae485b90c3583a63f8`; **missing**; exact names: CUTIN_E0301.
- DIAL_BG.jet: 810132 bytes/18 records; SHA256 `b12aa44631bceb6da1d20870b8f84476b5922108dfe48c4248637a466148043e`; selected; exact names: BG001_2.
- DIAL_BG2.jet: 2973203 bytes/30 records; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; selected; exact names: BG004_1, BG006_2.
- N001_BG.jet: 2282467 bytes/21 records; SHA256 `4d09c9eaf150befb7adc3a32919bdba6247ceb2097d5cac069de5da48fcb3d40`; selected; exact names: N001_BG.
- N002.jet: 1522723 bytes/38 records; SHA256 `cfd0b67b718d7ace8efa082b0fee9e1cc032aac5ca561aec32e6927ee3d88ae1`; selected; exact names: N002_BG.
- N004.jet: 1651492 bytes/54 records; SHA256 `dac953f788f16936f95c664cb9fd28e628f24b3325a7dc241a19b658e86935bb`; **missing**; exact names: N004_BG.
- SND1.jet: 7173961 bytes/68 records; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; selected; exact names: BGM_BATTLE3, BGM_GULLVEIG, BGM_LANA, FX_CLASH.
- SND_CDN.jet: 10911430 bytes/105 records; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; selected; exact names: BGM_COMIC1, BGM_MOUSE, BGM_TRAIN.
- ST003.jet: 1181521 bytes/20 records; SHA256 `a58c3a55a0b89c4beaf73bc46babac9b837874c5dabad88bc1b7c099fcd87e61`; **missing**; exact names: complete fixed-actor family or environment candidate; see combat audit.
- VOICE_CDN1.jet: 6023659 bytes/77 records; SHA256 `a04b9a3098d9142b09492089eb64e5e3475c32caaa5b299359cb25e31851f83b`; selected; exact names: N003_46_1, N003_46_2, N003_46_3, N003_46_4.
- VOICE_CDN3.jet: 5886922 bytes/76 records; SHA256 `3fd64cf3530ca00f74c04245e103c008f2c0fe385a992f11b3dfbf2072558ea0`; **missing**; exact names: C009_46_1, C009_46_2, C009_46_3, C009_46_4, C009_46_5, C013_40_1, C013_40_2, C013_40_3, C013_41_1, C013_41_10, C013_41_2, C013_41_3, C013_41_4, C013_41_5, C013_41_6, C013_41_7, C013_41_8, C013_41_9, C013_42_1, C013_42_2, C013_42_3, C013_42_4, C013_42_5, C013_42_6, C013_42_7, C013_43_1, C013_43_2, C013_45_1, C013_45_2, C013_45_3, C013_45_4, C013_45_5, C013_46.
- VOICE_CDN4.jet: 5193253 bytes/91 records; SHA256 `d1ea1fce10dbec7c8467980dd3be164f864c3717498c73e6d12c83f36443ef5d`; selected; exact names: C010_43_1, C010_43_2, C010_43_3, C010_44_1, C010_44_2, C010_44_3, C010_44_4, C010_45_1, C010_45_2, C010_45_3, C010_45_4, C010_45_5, C010_45_6, C010_45_7, C010_45_8.
- VOICE_CDN6.jet: 7338509 bytes/89 records; SHA256 `6e1fc70711557d03a2eec6b02fae393f52d510c408b0f732237b19ca794a1c2e`; selected; exact names: C004_40_1, C004_40_2, C004_40_3, C004_40_4, C004_41_1, C004_41_2, C004_41_3, C004_42, C004_43_1, C004_43_2, C004_44_1, C004_44_2, C004_44_3, C004_44_4, C004_45_1, C004_45_2, C004_45_3.
- VOICE_CDN8.jet: 6786890 bytes/84 records; SHA256 `e31df9f7ab1693d0350b967f48c4b93a67e82624e93770d00386540036092d8b`; selected; exact names: N001_39_1, N001_39_10, N001_39_11, N001_39_2, N001_39_3, N001_39_4, N001_39_5, N001_39_6, N001_39_7, N001_39_8, N001_39_9, N001_46_1, N001_46_10, N001_46_11, N001_46_2, N001_46_3, N001_46_4, N001_46_5, N001_46_6, N001_46_7, N001_46_8, N001_46_9.
- VOICE_CDN9.jet: 5198811 bytes/61 records; SHA256 `ecd78b8d0b317cc088d7b11920c0e5b18fc638b947f55c15134d3f1006beab6f`; selected; exact names: C009_39_1, C009_39_2, C009_39_3, C009_39_4, C009_39_5, C009_39_6, C009_40_1, C009_40_2, C009_40_3, C009_40_4, C009_41_1, C009_41_2, C009_41_3, C009_41_4, C009_41_5, C009_42_1, C009_42_10, C009_42_2, C009_42_3, C009_42_4, C009_42_5, C009_42_6, C009_42_7, C009_42_8, C009_42_9, C009_43_1, C009_43_2, C009_43_3, C009_43_4, C009_43_5, C009_43_6, C009_43_7, C009_44_1, C009_44_10, C009_44_11, C009_44_2, C009_44_3, C009_44_4, C009_44_5, C009_44_6, C009_44_7, C009_44_8, C009_44_9, C009_45_1, C009_45_10, C009_45_11, C009_45_12, C009_45_2, C009_45_3, C009_45_4, C009_45_5, C009_45_6, C009_45_7, C009_45_8, C009_45_9.

## Header locations for dialogue script dependencies

- BG001_2: DIAL_BG.jet header809962/packed61.
- BG004_1: DIAL_BG2.jet header2972761/packed31.
- BG006_2: DIAL_BG2.jet header2972927/packed31.
- BGM_BATTLE3: SND1.jet header1838348/packed377426.
- BGM_COMIC1: SND_CDN.jet header4074657/packed682118.
- BGM_GULLVEIG: SND1.jet header3470466/packed646624.
- BGM_LANA: SND1.jet header4117114/packed585184.
- BGM_MOUSE: SND_CDN.jet header5790970/packed723914.
- BGM_TRAIN: SND_CDN.jet header6514908/packed929968.
- C004_40_1: VOICE_CDN6.jet header3625359/packed148835.
- C004_40_2: VOICE_CDN6.jet header3774218/packed74020.
- C004_40_3: VOICE_CDN6.jet header3848262/packed79872.
- C004_40_4: VOICE_CDN6.jet header3928158/packed43091.
- C004_41_1: VOICE_CDN6.jet header3971273/packed145909.
- C004_41_2: VOICE_CDN6.jet header4117206/packed74856.
- C004_41_3: VOICE_CDN6.jet header4192086/packed65243.
- C004_42: VOICE_CDN6.jet header4257353/packed138804.
- C004_43_1: VOICE_CDN6.jet header4396181/packed158030.
- C004_43_2: VOICE_CDN6.jet header4554235/packed69423.
- C004_44_1: VOICE_CDN6.jet header4623682/packed129609.
- C004_44_2: VOICE_CDN6.jet header4753315/packed51033.
- C004_44_3: VOICE_CDN6.jet header4804372/packed148835.
- C004_44_4: VOICE_CDN6.jet header4953231/packed28045.
- C004_45_1: VOICE_CDN6.jet header4981300/packed48943.
- C004_45_2: VOICE_CDN6.jet header5030267/packed41002.
- C004_45_3: VOICE_CDN6.jet header5071293/packed112891.
- C005_SND03: C005_SND.jet header59208/packed51468.
- C009_39_1: VOICE_CDN9.jet header547083/packed73602.
- C009_39_2: VOICE_CDN9.jet header620709/packed89067.
- C009_39_3: VOICE_CDN9.jet header709800/packed29299.
- C009_39_4: VOICE_CDN9.jet header739123/packed74438.
- C009_39_5: VOICE_CDN9.jet header813585/packed120832.
- C009_39_6: VOICE_CDN9.jet header934441/packed44763.
- C009_40_1: VOICE_CDN9.jet header979228/packed96590.
- C009_40_2: VOICE_CDN9.jet header1075842/packed91157.
- C009_40_3: VOICE_CDN9.jet header1167023/packed62317.
- C009_40_4: VOICE_CDN9.jet header1229364/packed77782.
- C009_41_1: VOICE_CDN9.jet header1307170/packed79454.
- C009_41_2: VOICE_CDN9.jet header1386648/packed117906.
- C009_41_3: VOICE_CDN9.jet header1504578/packed87813.
- C009_41_4: VOICE_CDN9.jet header1592415/packed84051.
- C009_41_5: VOICE_CDN9.jet header1676490/packed119996.
- C009_42_1: VOICE_CDN9.jet header1796510/packed114980.
- C009_42_10: VOICE_CDN9.jet header1911514/packed44345.
- C009_42_2: VOICE_CDN9.jet header1955883/packed132117.
- C009_42_3: VOICE_CDN9.jet header2088024/packed84051.
- C009_42_4: VOICE_CDN9.jet header2172099/packed25119.
- C009_42_5: VOICE_CDN9.jet header2197242/packed118742.
- C009_42_6: VOICE_CDN9.jet header2316008/packed117488.
- C009_42_7: VOICE_CDN9.jet header2433520/packed94082.
- C009_42_8: VOICE_CDN9.jet header2527626/packed91993.
- C009_42_9: VOICE_CDN9.jet header2619643/packed130863.
- C009_43_1: VOICE_CDN9.jet header2750530/packed81962.
- C009_43_2: VOICE_CDN9.jet header2832516/packed82379.
- C009_43_3: VOICE_CDN9.jet header2914919/packed73602.
- C009_43_4: VOICE_CDN9.jet header2988545/packed57302.
- C009_43_5: VOICE_CDN9.jet header3045871/packed91575.
- C009_43_6: VOICE_CDN9.jet header3137470/packed15506.
- C009_43_7: VOICE_CDN9.jet header3153000/packed28463.
- C009_44_1: VOICE_CDN9.jet header3181487/packed56048.
- C009_44_10: VOICE_CDN9.jet header3237559/packed26791.
- C009_44_11: VOICE_CDN9.jet header3264374/packed35568.
- C009_44_2: VOICE_CDN9.jet header3299966/packed85305.
- C009_44_3: VOICE_CDN9.jet header3385295/packed119996.
- C009_44_4: VOICE_CDN9.jet header3505315/packed125847.
- C009_44_5: VOICE_CDN9.jet header3631186/packed107457.
- C009_44_6: VOICE_CDN9.jet header3738667/packed77364.
- C009_44_7: VOICE_CDN9.jet header3816055/packed81126.
- C009_44_8: VOICE_CDN9.jet header3897205/packed77364.
- C009_44_9: VOICE_CDN9.jet header3974593/packed48525.
- C009_45_1: VOICE_CDN9.jet header4023142/packed65661.
- C009_45_10: VOICE_CDN9.jet header4088827/packed93664.
- C009_45_11: VOICE_CDN9.jet header4182515/packed107875.
- C009_45_12: VOICE_CDN9.jet header4290414/packed101188.
- C009_45_2: VOICE_CDN9.jet header4391626/packed149671.
- C009_45_3: VOICE_CDN9.jet header4541321/packed92828.
- C009_45_4: VOICE_CDN9.jet header4634173/packed110801.
- C009_45_5: VOICE_CDN9.jet header4744998/packed83215.
- C009_45_6: VOICE_CDN9.jet header4828237/packed138386.
- C009_45_7: VOICE_CDN9.jet header4966647/packed81962.
- C009_45_8: VOICE_CDN9.jet header5048633/packed127937.
- C009_45_9: VOICE_CDN9.jet header5176594/packed22193.
- C009_46_1: VOICE_CDN3.jet header0/packed24701.
- C009_46_2: VOICE_CDN3.jet header24725/packed67751.
- C009_46_3: VOICE_CDN3.jet header92500/packed141312.
- C009_46_4: VOICE_CDN3.jet header233836/packed55212.
- C009_46_5: VOICE_CDN3.jet header289072/packed72348.
- C010_43_1: VOICE_CDN4.jet header0/packed62317.
- C010_43_2: VOICE_CDN4.jet header62341/packed82379.
- C010_43_3: VOICE_CDN4.jet header144744/packed90739.
- C010_44_1: VOICE_CDN4.jet header235507/packed97426.
- C010_44_2: VOICE_CDN4.jet header332957/packed117488.
- C010_44_3: VOICE_CDN4.jet header450469/packed62735.
- C010_44_4: VOICE_CDN4.jet header513228/packed105367.
- C010_45_1: VOICE_CDN4.jet header618619/packed179346.
- C010_45_2: VOICE_CDN4.jet header797989/packed160120.
- C010_45_3: VOICE_CDN4.jet header958133/packed126265.
- C010_45_4: VOICE_CDN4.jet header1084422/packed81126.
- C010_45_5: VOICE_CDN4.jet header1165572/packed6729.
- C010_45_6: VOICE_CDN4.jet header1172325/packed20104.
- C010_45_7: VOICE_CDN4.jet header1192453/packed50197.
- C010_45_8: VOICE_CDN4.jet header1242674/packed76110.
- C013_40_1: VOICE_CDN3.jet header3087578/packed20522.
- C013_40_2: VOICE_CDN3.jet header3108124/packed40584.
- C013_40_3: VOICE_CDN3.jet header3148732/packed69423.
- C013_41_1: VOICE_CDN3.jet header3218179/packed103695.
- C013_41_10: VOICE_CDN3.jet header3321898/packed77782.
- C013_41_2: VOICE_CDN3.jet header3399704/packed60646.
- C013_41_3: VOICE_CDN3.jet header3460374/packed97844.
- C013_41_4: VOICE_CDN3.jet header3558242/packed84051.
- C013_41_5: VOICE_CDN3.jet header3642317/packed89485.
- C013_41_6: VOICE_CDN3.jet header3731826/packed97008.
- C013_41_7: VOICE_CDN3.jet header3828858/packed117906.
- C013_41_8: VOICE_CDN3.jet header3946788/packed158448.
- C013_41_9: VOICE_CDN3.jet header4105260/packed127519.
- C013_42_1: VOICE_CDN3.jet header4232803/packed84051.
- C013_42_2: VOICE_CDN3.jet header4316878/packed56884.
- C013_42_3: VOICE_CDN3.jet header4373786/packed128773.
- C013_42_4: VOICE_CDN3.jet header4502583/packed74856.
- C013_42_5: VOICE_CDN3.jet header4577463/packed65661.
- C013_42_6: VOICE_CDN3.jet header4643148/packed48943.
- C013_42_7: VOICE_CDN3.jet header4692115/packed81544.
- C013_43_1: VOICE_CDN3.jet header4773683/packed129609.
- C013_43_2: VOICE_CDN3.jet header4903316/packed81544.
- C013_45_1: VOICE_CDN3.jet header4984884/packed95754.
- C013_45_2: VOICE_CDN3.jet header5080662/packed137132.
- C013_45_3: VOICE_CDN3.jet header5217818/packed118324.
- C013_45_4: VOICE_CDN3.jet header5336166/packed152179.
- C013_45_5: VOICE_CDN3.jet header5488369/packed138386.
- C013_46: VOICE_CDN3.jet header5626779/packed146327.
- CUTIN_E0301: CUT_E0301.jet header406674/packed61.
- FX_CLASH: SND1.jet header5799887/packed20071.
- N001_39_1: VOICE_CDN8.jet header3232414/packed69841.
- N001_39_10: VOICE_CDN8.jet header3302279/packed108711.
- N001_39_11: VOICE_CDN8.jet header3411014/packed79872.
- N001_39_2: VOICE_CDN8.jet header3490910/packed140476.
- N001_39_3: VOICE_CDN8.jet header3631410/packed104113.
- N001_39_4: VOICE_CDN8.jet header3735547/packed84051.
- N001_39_5: VOICE_CDN8.jet header3819622/packed114144.
- N001_39_6: VOICE_CDN8.jet header3933790/packed157612.
- N001_39_7: VOICE_CDN8.jet header4091426/packed141312.
- N001_39_8: VOICE_CDN8.jet header4232762/packed95754.
- N001_39_9: VOICE_CDN8.jet header4328540/packed113308.
- N001_46_1: VOICE_CDN8.jet header4441872/packed94918.
- N001_46_10: VOICE_CDN8.jet header4536814/packed90321.
- N001_46_11: VOICE_CDN8.jet header4627159/packed89903.
- N001_46_2: VOICE_CDN8.jet header4717086/packed103695.
- N001_46_3: VOICE_CDN8.jet header4820805/packed99098.
- N001_46_4: VOICE_CDN8.jet header4919927/packed123757.
- N001_46_5: VOICE_CDN8.jet header5043708/packed44345.
- N001_46_6: VOICE_CDN8.jet header5088077/packed128355.
- N001_46_7: VOICE_CDN8.jet header5216456/packed86977.
- N001_46_8: VOICE_CDN8.jet header5303457/packed15506.
- N001_46_9: VOICE_CDN8.jet header5318987/packed57302.
- N001_BG: N001_BG.jet header2282340/packed49.
- N002_BG: N002.jet header1501679/packed159.
- N003_46_1: VOICE_CDN1.jet header4766381/packed57720.
- N003_46_2: VOICE_CDN1.jet header4824125/packed118742.
- N003_46_3: VOICE_CDN1.jet header4942891/packed29299.
- N003_46_4: VOICE_CDN1.jet header4972214/packed76528.
- N004_BG: N004.jet header1640181/packed271.

## Promotion boundary

This closes original catalog/dialogue paths, final text, source record hashes, named header ownership and explicit selection gaps. It does not prove a download, native material map binding, battle body construction, a win, clear, reward receipt or original final balance. Parent should prepare an additive hash-guarded original overlay, then validate native story/control/combat and retain unsupported GC3/GC4 until their actual item/redemption contracts are reconstructed.
