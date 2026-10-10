# E02 entry and original material closure

2026-10-08. Read-only preserved final PAD resources, original recovered Episode JSON, established profile scripts and AGENTS section162. No ADB, Ghidra, runtime, source, profile or save changes. Only this report is written.

## E02 native entry

E02 has eight stories. E01 all-seven and parent clear are root-verified; this lane does not claim E02 entry, native asset residency, combat or clear. Chapter reward is original FMD1 x30/free_iap0; metadata is not a validated item or receipt contract.

E02_S01 is nonbattle EP_0501A, local_MIDGARD x1235/y1150, thumbnail C003_DIALOG. The original conversation has 16 nodes and 13 nonempty text entries including narration. Linear path: 0→1→2→3→4→5→7→8→9→10→11→12→13→14→15→20. No choices or nonempty conditions. First node2 Captain: “Great weather! Great shape! Great feeling!” Final node15 Captain: “Set- Go!” Terminal20 runs episode_clear, scr-fade duration0.6 black, wait0.6; no explicit ctrl-scene-back. Starting from fully displayed first line, twelve normal advances reach the final text, then one advances to terminal. UI animation/readiness remains root responsibility.

Declared speakers are Captain009, Lantern001, Nene003 and NPC Lana001. Entry script uses N001_BG, BGM_TRAIN; voice C009_30_1..5, C003_30_1..2, C001_30_1 and N001_30_1..4; WHOOSH narration uses GACH_SHOT. Against established31groups/54assets plus Bear overlays, the immediate missing explicit pack is **VOICE_CDN8.jet**, solely needed here for Lana N001_30_1..4. Other named dependencies are in selected N001_BG/SND_CDN/VOICE_CDN1/7 and existing actor packs. Native residency remains unproved.

## Original story sequence

- E02_S01: EP_0501A; battle=False; local_MIDGARD; portrait C003_DIALOG.
- E02_S02: EP_0502A; battle=False; local_ICEWOOD; portrait C003_DIALOG.
- E02_S03: EP_0503A; battle=True; local_ICEWOOD; portrait C003_DIALOG; combat CB0201.
- E02_S04: EP_0601A; battle=False; local_ICEWOOD; portrait C005_DIALOG.
- E02_S05: EP_0602A; battle=True; local_AGIT; portrait C005_DIALOG; combat CB0202.
- E02_S06: EP_0603A; battle=False; local_AGIT; portrait C005_DIALOG.
- E02_S07: EP_0604A; battle=False; local_MIDGARD; portrait C005_DIALOG.
- E02_S08: EP_0605A; battle=False; local_MIDGARD; portrait C005_DIALOG.

CB0201: four owned slots vs three original CB0201_M1/M023 and Bright CB0201_049_1/C049; game_res_id2, BGM_TRAIN, win EP_0503B. CB0202: four owned slots plus Bright CB0202_049_1 vs M050/M049/M051/M062; game_res_id2, BGM_BATTLE2, win EP_0602B. Both losses EP_0000A/repeat EP_0000B. Original serialized actor definitions remain authoritative; no owned049 grant or balance rewrite follows.

## Conversation control and exact source offsets

DIAL-EN complete24-byte-header walk ends3133395, exactly original filesize; header+8 packedlength, +12 uint64 base38 name, zlibRW envelope XML+6. Text counts below follow the actual outgoing-link graph rather than physical XML element ordering. Each inspected route is linear with no nonempty conditions.

- **EP_0501A** header2447471, packed1958, RW25100, SHA256 `bad69bb0bb59677a806840cd60e2350c58fd7e8285acd881c9780bcc7004aee5`. 16 nodes/13 texts. Path 0→1→2→3→4→5→7→8→9→10→11→12→13→14→15→20. Final node15: Set- Go! Terminal20: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BGM_TRAIN, C001_30_1, C003_30_1, C003_30_2, C009_30_1, C009_30_2, C009_30_3, C009_30_4, C009_30_5, GACH_SHOT, N001_30_1, N001_30_2, N001_30_3, N001_30_4, N001_BG.
- **EP_0502A** header2449453, packed2142, RW26997, SHA256 `ad248b1eff997baa858c6f6c5af0d7bf4bda35c994b638ef128e15f5c980c10d`. 18 nodes/14 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→35→36→37→38→41. Final node38: Arrrggghhh!! Terminal41: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BG008_1, BG900_1, BGM_GULLVEIG, BGM_TRAIN, C003_31_1, C003_31_2, C003_31_3, C003_31_4, C007_SND02, C009_31_1, C009_31_2, C009_31_3, C009_31_4, C009_31_5, C009_31_6, C009_31_7, C009_31_8, C032_SND01.
- **EP_0503A** header2451619, packed2049, RW27129, SHA256 `33e1aa896ea2c506696e648344f4a9affc1f2b52bed0730ff1cc544374efb11f`. 18 nodes/14 texts. Path 0→1→2→3→4→5→6→7→8→9→11→12→13→14→15→17→18→16. Final node18: Hmph! Don't give me lame excuses! Terminal16: `scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6; combat_goto id:CB0201`.
  Named script dependencies: BG001_3, BG008_1, BGM_BATTLE3, BGM_COMIC1, BGM_TRAIN, C009_32_1, C009_32_2, C009_32_3, C009_32_4, C009_32_5, C009_32_6, C009_32_7, C009_32_8_A, C049_32_1, C049_32_2, C049_SND04, C054_SND01, CHILD_32, FX_GUN1.
- **EP_0503B** header2453692, packed1562, RW15898, SHA256 `196227d36f1994a26ebdadd4284d80185c2d3a464847362aab926e66fa9cfd02`. 10 nodes/7 texts. Path 0→1→2→3→4→5→6→7→8→17. Final node8: Be a family? Terminal17: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6; ctrl-scene-back cnt:2`.
  Named script dependencies: BGM_GULLVEIG, C009_33_1, C009_33_2, C009_33_3, C009_33_4, C049_33_1, C049_33_2, C049_33_3.
- **EP_0601A** header2455278, packed1645, RW17320, SHA256 `183c057e5d53879ea2b7e7c52acbd28b9e735175f34c49da2998640351bcc794`. 11 nodes/8 texts. Path 0→1→9→10→11→12→13→14→15→16→17. Final node16: And what do you mean by "bro?" Are you actually a boy?! Terminal17: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BG001_3, C009_33_5, C009_33_6, C009_33_7, C009_33_8, C049_33_4, C049_33_5, C049_33_6, C049_33_7.
- **EP_0602A** header2456947, packed2267, RW31406, SHA256 `eac2c765c7abda76b616fd103fbd17416dac855bae7f28c5047a19181957f54f`. 20 nodes/15 texts. Path 0→1→25→2→3→27→6→7→8→10→28→11→14→26→19→20→21→22→23→24. Final node23: Haha... Stop playing a hero, your life is at risk! Terminal24: `scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6; combat_goto id:CB0202`.
  Named script dependencies: BGM_BATTLE2, BGM_GULLVEIG, C009_34_1, C009_34_2, C009_34_3, C009_34_4, C049_34_1, C049_34_2, C049_34_3, N500_34_1, N500_34_2, N500_34_3, N500_34_4, N501A_34_1, N501A_34_2, N501B_34_1, N501B_34_2.
- **EP_0602B** header2459238, packed1512, RW14953, SHA256 `1255287e6c8ca0c8d425be685fae51e3faba76c2befff9238b513bee768bd93a`. 9 nodes/6 texts. Path 0→1→2→3→4→5→7→8→6. Final node8: G-Guys! You're all safe! Terminal6: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6; ctrl-scene-back cnt:2`.
  Named script dependencies: BGM_GULLVEIG, C009_35, C049_35_1, C049_35_2, CHILD_35, N500_35.
- **EP_0603A** header2460774, packed1890, RW24092, SHA256 `2d971142bcba2cf7286d010060488b792934d0ea4b2c410531fefa95f464c625`. 16 nodes/13 texts. Path 0→22→23→8→9→10→12→13→14→15→16→17→18→19→20→21. Final node20: Yes! Let's meet again! Terminal21: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BG001_3, C009_36_1, C009_36_2, C009_36_3, C009_36_4, C009_36_5, C009_36_6, C049_36_1, C049_36_2, C049_36_3, C049_36_4, C049_36_5, C049_36_6, CHILD_36.
- **EP_0604A** header2462688, packed2198, RW31788, SHA256 `2e9d518aab29927e55794a6f8f22b781fefe07c9b9ac3f9d0e5c7034e8c4d92b`. 20 nodes/14 texts. Path 0→1→2→33→4→5→37→6→7→9→10→35→12→13→14→15→36→16→34→28. Final node34: W-W-What? Terminal28: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BGM_MOUSE, C001_37_1, C001_37_2, C001_37_3, C003_37_1, C003_37_2, C003_37_3, C003_37_4, C009_37_1, C009_37_2, CUTIN_E0201, N001_37_1, N001_37_2, N001_37_3, N001_37_4, N001_37_5, N001_BG.
- **EP_0605A** header2464910, packed2469, RW33387, SHA256 `46581e56101603d53b4b78b514425ba908940d9fad77b782c1f86d30e64ecab4`. 21 nodes/16 texts. Path 0→17→18→29→30→19→39→34→36→35→37→33→38→31→21→22→23→32→26→27→28. Final node27: Yes. The fear is growing because we still haven't figured out <color='240, 20, 50, 255'>what led him to change.</color> Terminal28: `episode_clear; scr-fade duration:0.6 color:(0,0,0,255); wait duration:0.6`.
  Named script dependencies: BG002_1, BGM_GULLVEIG, C001_38, C003_38_1, C003_38_2, C009_38_1, C009_38_2, C009_38_3, C009_38_4, CUTIN_E0201, N001_38_1, N001_38_2, N001_38_3, N001_38_4, N001_38_5, N001_38_6, N001_38_7, N002_BG, N003_38_1, N003_38_2.

## Exact pack ownership and missing explicit selections

Established original material profile explicitly includes DIAL_BG2, N001_BG, SND1, SND_CDN, VOICE_CDN1/2/4/6/7, base001..006/009 and C036 families. DIAL_BG is not in the explicit current54 folded list; native BG001_1 rendering does not prove whole-pack residency. The later episode02-material-closure.md corrects this implicit-residency assumption and includes original DIAL_BG as an explicit addition for BG001_3. Parent may use these comparisons to prepare a focused original CDN overlay, but this report does not advertise or restart anything.

Missing immediate/later conversation additions: VOICE_CDN8; Story02 DIAL_BG9, C007_SND, C032_SND; Story03 Bright C049 family and C049_SND, C054_SND (voice4 already selected); Story05 N500/N501 and VOICE_CDN5; Story07/08 CUT_E0201 and VOICE_CDN9; Story08 N002 (N002_BG). Story03/05 monster packs are identified separately below. No whole C007/C032/C054 family is implied solely by a sound event.

- C007_SND.jet: 81150 bytes; SHA256 `5e794d5014e333b74927bb508d259cd2b1f78653248379f8e3ca839f4560248c`; exactEOF=True; names C007_SND02.
- C032_SND.jet: 96619 bytes; SHA256 `0e6047ccd0490e0d217493ac473ddfbf634817ba4eba4358eb2b420d86d8cab3`; exactEOF=True; names C032_SND01.
- C049.jet: 747502 bytes; SHA256 `af47cd8414e302aed6bfcbf2edfc6338e529e25258441fc9d216290d9e0af88d`; exactEOF=True; names C049.
- C049_EFT.jet: 2540488 bytes; SHA256 `8d15176a68eaa4544b9995c349a281bdd699302984e8d5adacd4bcad4919100f`; exactEOF=True; names C049_E01, C049_E02, C049_E03, C049_EC.
- C049_SND.jet: 167898 bytes; SHA256 `4e2525e491ba24839edc963705bd106e0f6ca67d3bbff77d8fd2d8ca687c9564`; exactEOF=True; names C049_SND04.
- C054_SND.jet: 176066 bytes; SHA256 `b43abdae9f8ef2f86e5536602888f6f62dda8b484484b33c787b351c7841255a`; exactEOF=True; names C054_SND01.
- CUT_E0201.jet: 381756 bytes; SHA256 `ca39470995f008e4eac95485b26621da2235a9626e7964b6d8b4f57bb7825fb5`; exactEOF=True; names CUTIN_E0201.
- DIAL_BG.jet: 810132 bytes; SHA256 `b12aa44631bceb6da1d20870b8f84476b5922108dfe48c4248637a466148043e`; exactEOF=True; names BG001_3.
- DIAL_BG2.jet: 2973203 bytes; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; exactEOF=True; names BG002_1, BG008_1.
- DIAL_BG9.jet: 2665981 bytes; SHA256 `f085326e3139884fce5e1e2332312885c6aa15bf5dc6d4edf66cda4dc1c85b03`; exactEOF=True; names BG900_1.
- N001_BG.jet: 2282467 bytes; SHA256 `4d09c9eaf150befb7adc3a32919bdba6247ceb2097d5cac069de5da48fcb3d40`; exactEOF=True; names N001_BG.
- N002.jet: 1522723 bytes; SHA256 `cfd0b67b718d7ace8efa082b0fee9e1cc032aac5ca561aec32e6927ee3d88ae1`; exactEOF=True; names N002_BG.
- SND1.jet: 7173961 bytes; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; exactEOF=True; names BGM_BATTLE2, BGM_BATTLE3, BGM_GULLVEIG.
- SND_CDN.jet: 10911430 bytes; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; exactEOF=True; names BGM_COMIC1, BGM_MOUSE, BGM_TRAIN, FX_GUN1, GACH_SHOT.
- VOICE_CDN1.jet: 6023659 bytes; SHA256 `a04b9a3098d9142b09492089eb64e5e3475c32caaa5b299359cb25e31851f83b`; exactEOF=True; names C001_30_1, C001_37_1, C001_37_2, C001_37_3, C001_38, C003_30_1, C003_30_2, C003_31_1, C003_31_2, C003_31_3, C003_31_4, C003_37_1, C003_37_2, C003_37_3, C003_37_4, C003_38_1, C003_38_2, N003_38_1, N003_38_2.
- VOICE_CDN4.jet: 5193253 bytes; SHA256 `d1ea1fce10dbec7c8467980dd3be164f864c3717498c73e6d12c83f36443ef5d`; exactEOF=True; names C049_32_1, C049_32_2, C049_33_1, C049_33_2, C049_33_3, C049_33_4, C049_33_5, C049_33_6, C049_33_7, C049_34_1, C049_34_2, C049_34_3, C049_35_1, C049_35_2, C049_36_1, C049_36_2, C049_36_3, C049_36_4, C049_36_5, C049_36_6, CHILD_32, CHILD_35, CHILD_36.
- VOICE_CDN5.jet: 6264326 bytes; SHA256 `87f5652c06de9e81922270636222031c7332088c777ee3accc0c8e6df21e14aa`; exactEOF=True; names N500_34_1, N500_34_2, N500_34_3, N500_34_4, N500_35, N501A_34_1, N501A_34_2, N501B_34_1, N501B_34_2.
- VOICE_CDN7.jet: 5205609 bytes; SHA256 `c40c97dc28a858a06882f6aa6fa9e8da9e75ef0ef5f430a20d59f8e09156608b`; exactEOF=True; names C009_30_1, C009_30_2, C009_30_3, C009_30_4, C009_30_5, C009_31_1, C009_31_2, C009_31_3, C009_31_4, C009_31_5, C009_31_6, C009_31_7, C009_31_8, C009_32_1, C009_32_2, C009_32_3, C009_32_4, C009_32_5, C009_32_6, C009_32_7, C009_32_8_A, C009_33_1, C009_33_2, C009_33_3, C009_33_4, C009_33_5, C009_33_6, C009_33_7, C009_33_8, C009_34_1, C009_34_2, C009_34_3, C009_34_4, C009_35, C009_36_1, C009_36_2, C009_36_3, C009_36_4, C009_36_5, C009_36_6.
- VOICE_CDN8.jet: 6786890 bytes; SHA256 `e31df9f7ab1693d0350b967f48c4b93a67e82624e93770d00386540036092d8b`; exactEOF=True; names N001_30_1, N001_30_2, N001_30_3, N001_30_4, N001_37_1, N001_37_2, N001_37_3, N001_37_4, N001_37_5, N001_38_1, N001_38_2, N001_38_3, N001_38_4, N001_38_5, N001_38_6, N001_38_7.
- VOICE_CDN9.jet: 5198811 bytes; SHA256 `ecd78b8d0b317cc088d7b11920c0e5b18fc638b947f55c15134d3f1006beab6f`; exactEOF=True; names C009_37_1, C009_37_2, C009_38_1, C009_38_2, C009_38_3, C009_38_4.

C049 animation/Q/EFT/SND complete-family candidate hashes (not C049A/B):
- C049.jet: 747502 bytes; SHA256 `af47cd8414e302aed6bfcbf2edfc6338e529e25258441fc9d216290d9e0af88d`.
- C049_Q.jet: 59245 bytes; SHA256 `4e3e5638bd74f83acc9c722be8b1ad3ea6ab9790a6bcb4f08d791a0cabbd3940`.
- C049_EFT.jet: 2540488 bytes; SHA256 `8d15176a68eaa4544b9995c349a281bdd699302984e8d5adacd4bcad4919100f`.
- C049_SND.jet: 167898 bytes; SHA256 `4e2525e491ba24839edc963705bd106e0f6ca67d3bbff77d8fd2d8ca687c9564`.
- N500.jet: 220037 bytes; SHA256 `a362f88ce48fb503dc035de13f446854282d43e75478cff6def375a2998d7f5c`.
- N501.jet: 222917 bytes; SHA256 `fb76b2c0a27cde2d257dc493c4603049bbae49436ab21c8028a25d8c4ffd4053`.

Monster named-record owners (animation names; complete AT→S2→I2 graph validation remains pending):

- M008.jet: 223669 bytes; SHA256 `04b37480c31248de3a2a23f09901961923441a9ba7524abae037a0eb805074f5`; exactEOF=True; 33 matching records; names M023_R01, M023_R02, M023_R03, M023_R04, M023_H01, M023_H02, M023_H03, M023_H04, M023_H05, M023_H06, M023_H07, M023_H08, M023_H09, M023_H10, M023_H11, M023_H12, M023_H13, M023_H14, M023_H15, M023_SHA, M023_THN, M023_AS1, M023_AS2, M023_AS3, M023_DIE, M023_H1, M023_H2, M023_H3, M023_R1, M023_R2, M023_S, M023_SHADOW, M023_TH.
- M017.jet: 943115 bytes; SHA256 `cf7dae6ce9b3b44fa673d4abfa52030f651264463beae2d0484be6a525f0f1bb`; exactEOF=True; 98 matching records; names M049_H01, M049_H02, M049_H03, M049_H04, M049_H05, M049_H06, M049_H07, M049_H08, M049_H09, M049_H10, M049_H11, M049_H12, M049_H13, M049_H14, M049_H15, M049_R01, M049_R02, M049_R03, M049_R04, M049_SHA, M049_THN, M049_X, M050_H01, M050_H02, M050_H03, M050_H04, M050_H05, M050_H06, M050_H07, M050_H08, M050_H09, M050_H10, M050_H11, M050_H12, M050_H13, M050_H14, M050_H15, M050_R01, M050_R02, M050_R03, M050_R04, M050_THN, M051_THN, M051_R01, M051_R02, M051_R03, M051_R04, M051_H01, M051_H02, M051_H03, M051_H04, M051_H05, M051_H06, M051_H07, M051_H08, M051_H09, M051_H10, M051_H11, M051_H12, M051_H13, M051_H14, M051_H15, M049_AS1, M049_AS2, M049_AS3, M049_DIE, M049_H1, M049_H2, M049_H3, M049_R1, M049_R2, M049_S, M049_SHADOW, M049_TH, M050_AS1, M050_AS2, M050_AS3, M050_DIE, M050_H1, M050_H2, M050_H3, M050_R1, M050_R2, M050_S, M050_SHADOW, M050_TH, M051_AS1, M051_AS2, M051_AS3, M051_DIE, M051_H1, M051_H2, M051_H3, M051_R1, M051_R2, M051_S, M051_SHADOW, M051_TH.
- M021.jet: 1015930 bytes; SHA256 `3c623ebdcfc2db86b66ddabcd09be8d08c008335286e1494dbbfdd8ef78dd328`; exactEOF=True; 33 matching records; names M062_H01, M062_H02, M062_H03, M062_H04, M062_H05, M062_H06, M062_H07, M062_H08, M062_H09, M062_H10, M062_H11, M062_H12, M062_H13, M062_H14, M062_H15, M062_R01, M062_R02, M062_R03, M062_R04, M062_SHA, M062_THN, M062_AS1, M062_AS2, M062_AS3, M062_DIE, M062_H1, M062_H2, M062_H3, M062_R1, M062_R2, M062_S, M062_SHADOW, M062_TH.

Do not claim a native render from a positive header hit. M023/M050/M049/M051/M062 animation/image closure, Bright effects, field2 background and profile delivery/residency need root validation before battle. There is no request to modify instrumented APK, original resources, rewards, account ownership or saved progression.

## Root native entry position check

Root reported delayed render followed by one normal tap showing Nene “Hehe... Captain1000001, you look very confident!” This is original EP_0501A node3, **text ordinal2 of13**, following Captain node2. From this fully displayed line, eleven normal advances reach final node15 “Set- Go!”, then one advances to terminal20. Observe rendering/readiness; this is a source-path bound, not evidence that those inputs have been performed.
