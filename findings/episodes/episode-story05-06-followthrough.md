# E01 Story05/06: original dialogue and next material dependencies

2026-10-08. Read-only original final PAD resources and recovered reference exports. No ADB, Ghidra, runtime, source, profile or save mutations. Root reported actual Story04 clear through native bare `/episode/Read E01_S04`, persisted cleared_ids containing E01_S04 and empty reward_ids. That observation is root evidence, not an action by this lane.

## Original dialogue provenance and control boundaries

Source: `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/DIAL-EN.jet`. Complete 24-byte-header walk ends at3133395; header+12 uint64 names decode using `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`. Selected declared zlib bodies inflate to RW envelopes, XML starts at+6. All three conversations have empty ConditionsString values and one linear route, no choices.

- **EP_0402A** header2438643, body2438667, packed2162, inflated27779; RW SHA256 `12580ee200d787db0347589602f5fa59c91d12001e5a111609e7173536eeed29`.
- **EP_0403A** header2440829, body2440853, packed1692, inflated19078; RW SHA256 `71d209e21b2232809f2e23eeef3c11253a7db56b1bb2f2f436edbbed8a291f5c`.
- **EP_0403B** header2442545, body2442569, packed2395, inflated34708; RW SHA256 `3bc9e0caf358f6f61d119d445999544daa9dcfd7a7e8039fbd17278165977487`.

Original EPISODE_S01 declares Story05 entry EP_0402A/battlefalse, Story06 EP_0403A/battletrue; both local_EASTSNOW x1340/y1180. These are narrative metadata, not new campaign-area references or server unlock rules.

**Story05 EP_0402A**: 18 nodes, **15 nonempty text entries**, including narration THUMP/CRASH/THUD, along `0->1->2->3->4->5->6->7->8->10->11->12->35->36->37->38->40->41`. First text node2 is colored `THUMP-!!`; final text node40 is Gerard: **“First and foremost, focus on protecting your teammates and yourself. The rest is secondary.”** Terminal41 executes `episode_clear`, fade0.6/wait0.6; **no explicit ctrl-scene-back**. Do not assume identical return behavior to Story04. Declared actors Captain009, Gerard005, Lantern001; BG001_1, C005_SND03 and voice families C009_26_1..7, C005_26_1..3, C001_26_1..2.

**Story06 EP_0403A**: 12 nodes, **nine spoken lines** along `0->1->2->11->3->4->5->6->7->8->9->10`. First Tyltyl node2: **“Captain, how have you been? Haven't seen you in a while.”** Final Captain node9: **“Tyltyl!”** Terminal10 executes fade0.6/wait0.6/`combat_goto id:CB0103`. Stop textbox advancement at the final line until the guarded battle controller is ready. Declared actors Captain009/Tyltyl004/Bear036; BG001_2, BGM_BATTLE1, C004_27_1..4, C009_27_1..4 and C036_SND03.

**CB0103 win EP_0403B**: 23 nodes, **19 spoken lines**, linear `0->1->2->21->3->4->5->6->7->8->9->10->11->12->13->22->14->15->16->17->18->19->20`. First Captain node2: “Tyltyl, are you all right? Did you get hurt?” Final Gerard node19: **“Stop asking questions... It will only make you feel more pathetic...”** Terminal20 clears, fade0.6/wait0.6/ctrl-scene-back cnt2. Node22 after spoken node13 fades and loads **CUTIN_E0101**, removes BG001_2 and fades back; this can cause a pause without adding a spoken line. Voices C009_28_1..4, C005_28_1..3, C004_28_1..6, C036_28_1..6; BGM_LANA/BGM_COMIC1.

## Exact CB0103 participants

`analysis/recovered-reference/EPISODE_COMBAT_CB0103.json`: idCB0103, titleE01_TITLE, stage_nameE01_S06_TITLE, power2500, game_res_id string7, bgmBGM_BATTLE2. WinEP_0403B, loseEP_0000A, repeatloseEP_0000B. Left includes four empty owned-party slots plus **CB0103_005_1** rank2/level1/attr2/skillflags[1,1,0,0,0]; right **CB0103_036_1** rank3/level1/attr3/skillflags[1,1,1,0,0]. These are native scripted actors, not grants.

`EPISODE_STAT_ACTORS.json` exact **CB0103_036_1**: ref036/resC036/attr3/role2/cool_time5000. Stat rank3, HP1700, ATK330, DEF220, SPD5.00, crit20.00, critdamage200, penetration0.00, block20.00, blockdamage30, attrresist0, hpregen0. Skill1 cool8000/cost4, effect(type1,target1,stat1,refer_target1,refer_stat1,base-1600,duration0,interval0); skill2 effect(type4,target1,stat4,refer_target1,refer_stat0,base-25,duration5000,interval0); skill3 effect(type2,target2,stat1,refer_target2,refer_stat4,base4,duration3000,interval3000). Preserve serialized effects; no invented ordinary-level formula.

Exact **CB0103_005_1**: ref005/resC005/attr2/role2/cool5000, rank2 HP310/ATK210/DEF290/SPD7.00, crit11/critdamage180, penetration0, block27/blockdamage52, attrresist0/hpregen9. This differs from CB0102 Gerard's separate scripted tuple; do not overwrite either with the other.

## Positive original named-record coverage and profile gaps

All resources below are present in the same preserved original PAD directory. Bounded original-name scan establishes their ownership. Captured `recovered-assets/replica-activation-20261005/profile.json` plus existing Episode/Story04/Veteran overlays do **not explicitly select** the new packs below; parent must compare current live profile before expansion. Presence on disk is not native residency/rendering proof.

- **C036.jet** 1567284 bytes, SHA256 `e4f7cb46ab924b75f173752a0696e72c8288534273ca8f6104529b08c656b360`, six records/exact EOF: C036,C036_A,C036_B,C036_D,C036_DA,C036_DB. Animation event strings name **C036_E01/E02/E03/EC** and **C036_SND01..04**.
- **C036_Q.jet** 53949 bytes, SHA256 `73002b5ee10b3dd49e5647531b142fb4fff410ab11cf8a99f6386d031e4baa25`,39 records/exact EOF. Positive sprite records C036_XX/WEP/AMOR/ACCRY/XXX/STHN/X/THN/SHA/SI01..05/WP/AM/AC/STH/TH/SHADOW/SI1..5. Anonymous numeric image IDs also occur; they are not missing named sprites.
- **C036_EFT.jet** 1320814 bytes, SHA256 `b3a0a27dfdb4f79b1119cc27591ec768303a0209a85c1b0f66247d5fe38ddb83`, eight records/exact EOF: C036_E01/E02/E03/EC, each with matching _A companion. Closes all base animation effect names.
- **C036_SND.jet** 192144 bytes, SHA256 `d4f8ff00e412c6f0515ba8caf61351b88e20769deebf882fff9ff7ca13f9ce02`,four records/exact EOF, C036_SND01..04. Closes base events and prebattle C036_SND03.
- **VOICE_CDN1.jet** 6023659 bytes, SHA256 `a04b9a3098d9142b09492089eb64e5e3475c32caaa5b299359cb25e31851f83b`,77 records/exact EOF; exact C001_26_1..2.
- **VOICE_CDN4.jet** 5193253 bytes, SHA256 `d1ea1fce10dbec7c8467980dd3be164f864c3717498c73e6d12c83f36443ef5d`,91 records/exact EOF; exact C036_28_1..6.
- **VOICE_CDN7.jet** 5205609 bytes, SHA256 `c40c97dc28a858a06882f6aa6fa9e8da9e75ef0ef5f430a20d59f8e09156608b`,76 records/exact EOF; exact C009_26_1..7, C009_27_1..4, C009_28_1..4.
- **CUT_E0101.jet** 375950 bytes, SHA256 `32b1d7cc27c180bb4e814447974930a7ba1c7768f7a008b2625dbafb6a9e6e92`,six records/exact EOF, includes exact CUTIN_E0101.

Already explicitly selected VOICE_CDN6 has C005_26_1..3/C005_28_1..3/C004_27_1..4/C004_28_1..6. BG001_1/BG001_2 live in original DIAL_BG.jet; current Story04 background already renders, but this lane does not prove which bundled file supplies runtime residency. Avoid redundant delivery without checking current packaging.

No C036A/B variant, synthetic C036 alias, new owned036 grant, stat rewrite, fake clear, chapter coupon or reward follows from this report. Restore genuine original materials through the normal CDN path before guarded native CB0103 testing.
