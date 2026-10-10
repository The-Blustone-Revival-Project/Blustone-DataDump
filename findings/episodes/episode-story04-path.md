# E01 Story04: original dialogue, CB0102 and outcome destinations

Read-only final-client original DIAL-EN.jet extraction and recovered Episode
reference exports. No device, Ghidra, server/client/state edits, stats hunt,
web research or original-file writes.

`analysis/recovered-reference/EPISODE_S01.json` identifies **E01_S04**, entry
**EP_0401A**, `battle:true`, linked combat **CB0102**. Original package is
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/DIAL-EN.jet`.
The complete 24-byte outer-header walk ends exactly at3133395. Header+12's
uint64 decodes with alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`.
Each selected zlib body inflates to an RW wrapper (six bytes before XML).

Exact outer-record provenance:

```text
EP_0401A header2434699 body2434723 packed1866 inflated20658
RW SHA256 0dc11c08f810812e871aa57d15b3c76112a90d267dc915143b07f1517a653e5b
EP_0401B header2436589 body2436613 packed2030 inflated23511
RW SHA256 10015fd40c59656fd302ee6a87d5a3ff250a7c7ffcf31670f63d66be896d4cde
EP_0000A header2420925 body2420949 packed2622 inflated40278
RW SHA256 ab70173a672f4b161d8bcaf73650611d189358808bc003a2ad817c2ab46d4c53
EP_0000B header2423571 body2423595 packed2302 inflated32372
RW SHA256 c4d6b7b86e364a41730f31bddb3324ee286676661b07a02d23134e699b5894da
```

## Prebattle: the exact transition point

EP_0401A contains one Conversation ID1 and13 nodes, with one linear path:

```text
0→1→2→3→4→36→6→8→9→10→11→12→35
```

All ConditionsString values are empty. All nonterminal nodes have one outgoing
link; terminal35 has none. There are ten spoken lines and no choice branch.
Declared and spoken actors are captain Char009, Gerard Char005 and Lantern
Char001. Node1 stops sound, plays BGM_GULLVEIG, adds BG001_1 and waits0.6.
Voice resources are C009_24_1..3, C001_24_1..2 and C005_24_1..5.

The final spoken node12 is Gerard's **"Ok, now... Before we get started, let
me see what you got."** Advancing this line reaches terminal35:

```text
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
combat_goto id:CB0102
```

Root should stop ordinary textbox automation at this final spoken line until
its bounded combat input/observation loop is ready. The next transition starts
combat after the original fade/wait, with no further preparation choice in this
script. Confirm native live HUD before attacking; do not interpret the visible
Gerard dialogue as an active fight. Skip behavior remains separately unproved.

## Win: EP_0401B

Original `analysis/recovered-reference/EPISODE_COMBAT_CB0102.json` gives
`win_dialog:EP_0401B`, `lose_dialog:EP_0000A`, `lose_dialog2:EP_0000B`.
These are distinct destinations, unlike historical CB0101's identical ending
dialogs. CB0102 `game_res_id:7`, BGM_GULLVEIG and field_bg_res BG_RES remain
original declarations; native residency/rendering is root's separate check.

EP_0401B contains15 nodes, twelve spoken lines, no choice and empty conditions:

```text
0→1→38→39→40→2→3→4→7→36→37→8→9→10→35
```

Node1 adds BG001_1 and waits0.6. Lantern opens with "How was he? With the actual
training?" Gerard answers that the captain seems sloppy but mysterious; their
conversation concerns Vincent and Genovia. Voices are C001_25_1..6 and
C005_25_1..6. Captain009 is declared but has no spoken line in this ending.
Final spoken node10 is Gerard's "Anyway, now I should focus on helping that
guy do his job." Terminal35 is:

```text
episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
ctrl-scene-back cnt:2
```

Native EP_0401B rendering plus actual unprefixed `/episode/Read id:E01_S04`
and persisted clear are meaningful distinct win-path evidence. This report
does not claim such an outcome was observed. Scene classification alone is
insufficient because ending dialogue can retain the Episode scene class.

## Loss: choices, no story clear

EP_0000A contains28 nodes. Tyltyl explicitly says the player lost and explains
General Stages and recruitment. Its branch node16 offers four choices through
31/32/33/34. EP_0000B contains25 nodes and begins with the shorter repeat
warning at node7, offering the same four choices immediately.
Both scripts add N004_BG with sepiascale255 and play BGM_D_START. Every
ConditionsString is empty; **neither script contains episode_clear**.

The choices and destinations are exact:

- 31: General Stages →38, fade0.6/wait0.6/ignore-goto/goto-scene id:mission-area.
- 32: new teammates →39, fade0.6/wait0.6/ignore-goto/goto-scene id:gatcha.
- 33: try again →40, fade0.3/wait0.3/ctrl-scene-back cnt:2.
- 34: explain again →35→36, then loops through explanation to the choice node.

The "try again" branch has no explicit combat_goto; do not assert automatic
fight restart from its label. Stop ordinary dialogue tapping at these choices
and inspect the native screen. Selecting a loss option is separate from attack
input. These destinations do not authorize a host clear, reward or unlock.

## Follow-up: actual loss text identity and speaker discrepancy

Root reported a native CB0102 snapshot with left0/right1 and modal216cdc8,
followed by two displayed lines attributed to Captain. A bounded original
package scan decoded all **1357** DIAL-EN records and inflated each declared
zlib body; the two exact sentences occur **only in EP_0000A**:

- Node5: "No time to discuss such trivial stuff. You lost." Original
  Actor3 = **Tyltyl, Char004**, Conversant1 = Captain Char009, Emotion normal.
- Node6: "Oh, right. No wonder my neck felt stiff..." Original
  Actor1 = **Captain Char009**, Conversant1 = Captain Char009, Emotion shock.

Thus those sentences establish the original loss dialogue identity even if
node5's native presentation showed Captain. The indoor background agrees
with the exact EP_0000A declaration N004_BG, sepiascale255. Displayed speaker
or portrait divergence remains a presentation/binding question, not evidence
for a different original dialogue or a win.

The actual original R_EPISODE.jet was also decoded directly, not merely its
export:38080 bytes, SHA256
`7f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e`.
Logical inflated resource index10, zlib offset18466, root CB0102 has exactly
win EP_0401B, lose EP_0000A, lose2 EP_0000B. The recovered export agrees.
Server source does not supply the local COMBAT graph; native ReadJson loads
it from the original resource. This lane did not inspect resident native
memory, so it does not independently prove runtime graph identity. The
reported scene counters and displayed original loss text are consistent.
No clear flag, chapter claim or host mutation was performed.
