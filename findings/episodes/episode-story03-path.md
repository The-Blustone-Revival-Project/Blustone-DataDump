# E01 Story03: original linear dialogue and chapter reward

2026-10-07. Read-only original public PAD DIAL-EN.jet and recovered SEASON1
export. No device, Ghidra, server/client edits, private account body, grants,
stat hunting or original-file writes.

`analysis/recovered-reference/EPISODE_S01.json:66-82` identifies **E01_S03**,
entrypoint **EP_0303A**, `battle:false`, local_MIDGARD x1235/y1150. It does not
link CB0101; CB0101 is the preceding E01_S02.

Original package:
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/DIAL-EN.jet`.
Header+12's uint64 decoded with native base38 alphabet
`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._` is exactly EP_0303A. Header offset
**2432354**, compressed body **2432378**, packed **2321**, inflated **29565**;
inflated RW payload SHA256
`2a3b4e1d934c7b042723fb51cc80741c3a6a76a83ca557390f13988e15add1a8`.
The package's 24-byte header walk ends exactly at3133395 bytes.

The TalkerMakerProject has one Conversation ID1, title Midgard, **19 nodes**
and exactly one path:

```text
0→1→2→3→4→5→6→7→8→9→37→10→11→38→12→13→14→28→35
```

Every nonterminal has exactly one outgoing link, node35 has none, and all
ConditionsString elements are empty. Menu Text values are only `normal`,
`shout` and `empty` presentation tags. **No choice/alternate branch, combat_goto
or goto command occurs.** Fifteen nodes have nonempty spoken dialogue text.
This establishes that the original story is linear; it does not prove the
native Skip handler executes terminal scripts. Normal UI Skip is a reasonable
bounded action once the live Story03 identity is confirmed; require the actual
native unprefixed **/episode/Read id:E01_S03** success and resulting clear
state rather than setting flags from the host.

Node1 adds original **BG002_1** and waits0.6. Actor declarations are captain
Char009, Lana NPC001, Nene Char003, Lantern Char001; actual spoken nodes use
captain, Nene and Lantern. Node38 uses sentinel actor999 for a fade transition,
not an additional hunter to invent. Original voice requests are
**C009_23_1..6**, **C003_23_1..5**, **C001_23_1..4**. No play-bgm/play-env
command appears in this script. These are exact requested dependencies;
resident native resource/art binding was not newly verified in this lane.
Lana is declared but has no spoken node, so declaration alone does not prove
her portrait is displayed.

Terminal node35's UserScript is:

```text
episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
```

Unlike EP_0302B it has no ctrl-scene-back cnt2 command. Native dialogue close
and clear behavior should be verified from the actual transition/wire.

Original **E01 chapter reward** in
`analysis/recovered-reference/EPISODE_S01.json:17-25` is exactly
**item ref_id GC2, qty3; free_iap0**. Story03 clear does not itself establish
whole-E01 eligibility or a claim. Native request **/episode/Reward id:E01**
is separate. See `research/episode-e01-gc2-evidence.md`: GC2 is a real Lottery
coupon inventory reference, but exact original item metadata, coupon tier,
eligible pool and redemption contract remain unreconstructed. Keep this
declaration exact; do not substitute gold/Manda/cards or fabricate an inert
item merely to make a chapter claim succeed.
