# E01 Story07: original follow-through and separate chapter claim

2026-10-08. Read-only final PAD resources, recovered S01 export and existing reward-contract evidence. No ADB, Ghidra, live state/profile/server edits, rewards or stat hunts. Native playback remains root-owned and unverified by this report.

## Exact original path

Original `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/DIAL-EN.jet` named record **EP_0404A**: header2444964, body2444988, packed2483, inflated37267, RW SHA256 `8b70e316e2a38c2b1b232c969b8a9feefca8ef09d355608093e34609ba17add1`. Header+12 uint64 uses base38 `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`; declared zlib body inflates, XML begins+6. XML parsing finds **25 nodes, 20 nonempty text entries**, including two sound-effect narration entries; all nodes reachable on one linear path, all ConditionsString empty, every nonterminal has exactly one outgoing link. No choices or combat-goto.

`0->1->2->3->4->5->42->8->9->10->11->12->35->37->38->39->56->46->47->48->50->51->52->54->55`

First visible text node2 is colored **CRASH-!!**, followed by Captain “A million and twenty-five!!”; node4 is colored POW-!!. Declared actor identities are Captain009, Gerard005, Lantern001. Story's later unknown speaker is actor999, not an inferred owned/new hunter.

After text13/node37 (“Thanks for taking care of me, Gerard. See you later!”), automatic node38 fades0.6/waits0.6, adds **N001_BG**, removes BG001_1, fades0.6/waits0.6. Text19/node51 is Lantern **“Well, you walk straight from the starting point, then take a right turn...”**. Automatic node52 then fades0.6/waits1.0, adds **BG000_1**, removes N001_BG, waits1.0/fades0.6/waits0.6. This delay does not add a spoken entry.

Final text20/node54 has title **???**, actor999: **“Oho... Look at these guys.”**, script `play-voc res:C003_29` plus wait1.0. One final normal textbox advance reaches terminal55: `episode_clear`, fade0.6/wait0.6. **No explicit ctrl-scene-back or chapter-reward command** occurs in this terminal. From the first CRASH entry, 19 advances reach the final text, then a separate final advance clears. Count is a guide; inspect final text and native emitted request rather than input blindly through a changed screen.

`EPISODE_S01.json` binds E01_S07 to entrypointEP_0404A, battlefalse, local_MIDGARD x1235/y1150. Native terminal settlement should be bare `/episode/Read E01_S07`, not EP_0404A, E01, or a synthetic victory. Actual request/clear/persistence must be verified live by root.

## Positive material and voice ownership

Bounded original package header walks reach exact EOF for these positive matches:

- **VOICE_CDN1.jet** (77 records) owns C001_29_1..7 and exact C003_29.
- **VOICE_CDN6.jet** (89 records) owns C005_29_1.
- **VOICE_CDN7.jet** (76 records) owns C009_29_1..9.
- **C005_SND.jet** (6 records,211032 bytes, SHA256 `b5d7002b46e2fce102557866284df6ca424817c60d4788f120a40b942acfe5d7`) owns C005_SND03, header59208/packed51468.
- **DIAL_BG.jet** (18 records) owns BG001_1, header809877. Native prior Story05 already displayed this setting; actual bundle residency is root evidence, not established by a disk name alone.
- **N001_BG.jet** (21 records,2282467 bytes, SHA256 `4d09c9eaf150befb7adc3a32919bdba6247ceb2097d5cac069de5da48fcb3d40`) owns exact N001_BG at header2282340/packed49. This is already in the separate Episode selection. **N001.jet** is a different pack and does not own this named record.
- **DIAL_BG2.jet** (30 records,2973203 bytes, SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`) owns exact **BG000_1**, header2973037/packed31, inflated AT payload61 bytes. This closes named ownership; a full AT→sprite→image graph/native rendering is not asserted here.

The captured21-key resource profile plus committed Episode/Bear overlays selects VOICE_CDN1/6/7, C005_SND and N001_BG. It **does not explicitly select DIAL_BG2**. Check existing bundled residency or deliver that unchanged original pack before Story07's late transition. Missing late background could appear only after the preceding19 texts; do not misdiagnose the intentional fade delays as combat/loading. No aliases, new ordinary hunters or APK rebuild follow from this report.

## Clear and chapter reward are separate

Original E01 declaration is GC2qty3/free_iap0. Episode reward-contract evidence identifies separate native **RequestReward Gb1979c** `/episode/Reward` request with idE01; StageList **ComfirmClearAndReward Ge61f38** checks unclaimed and native IsClearedDataById(id)==1 before requesting. Terminal55 only executes episode_clear. Parent-clear aggregation and the UI timing of any automatic post-clear claim are not proved by this dialogue XML, so observe them instead of equating leaf clear with a reward grant.

Current all-descendant server authorization is explicitly local; all seven E01 leaf clears should be preserved. GC2 original item definition/thumbnail/redemption remains unreconstructed. Existing material report positively identifies GC2 inventory/coupon consumers but does not justify assigning art/tier/effect. **Do not grant GC2 or substitute another material** from this final story or claim result. Keep clear logs and reward logs distinct; E01_S07 clearance can be a real milestone while reward_ids remains empty and unsupported chapter settlement refuses.

Related evidence: `episode-reward-contract.md`, `episode-reward-materials.md`, `episode-story05-06-followthrough.md`, `episode-cb0103-contract-audit.md`.

## BG000_1 is deliberately opaque black — full original graph closed

Follow-up after root reported original final text rendered on black following downloaded DIAL_BG2. No live inspection by this lane. Exact original unchanged DIAL_BG2 graph:

```text
BG000_1 AT: header2973037, packed31, inflated61
  uint32 frame count+43 =1
  uint64 frame ID+47 =1309678093279 /0x130eee5c3df
S2: header2972467, packed37, inflated66
  uint64 image ID+46 =3542504339 /0xd3265393
I2: header2170840, packed4537, inflated3981758
  decoded852×1136 RGBA
```

Every dependency resolves in this same original package. Existing `jet_decoder.decode_i2_texture` and in-memory Pillow color histogram find **967872/967872 pixels exactly (0,0,0,255)**: one unique color, RGB extrema0..0, alpha extrema255..255, alpha bounding box(0,0,852,1136). This is an opaque black image, not a transparent or missing image. Thus black behind the final unknown-speaker line is **consistent with intentional original pixels**; no background replacement/alias/repair is warranted. The screenshot alone still does not establish native resource internals, but the original complete graph decisively explains the black visual without a missing-resource hypothesis. No image files generated or originals modified.
