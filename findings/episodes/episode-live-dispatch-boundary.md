# Ordinary Episode dispatch: source chain and live boundary

2026-10-05. Original public dialogue bytes and native code identify the actual
missions choice; no reference rows, gates, markers or scene jumps were added.

NPC0000 and NPC0005 entry4 contain the visible missions text with empty conditions
and a user script: black scr-fade0.1, wait0.1, snd-stop, goto-scene mainstream.
The native dispatcher matches mainstream CRC32d98de1c6 (upperword0), selects
TYPE58/0x3a, goes through83 and then PushSceneFadeOutIn58. Factory construction
independently identifies58 as CSRSceneMEpisodeList. This is the ordinary entrance,
not the Story-menu dialogue archive or the separate Depth event badge.

The complete original S01 graph has no explicit opening-gate fields or NPC
entrance map. Its first story is Midgard/EP_0301A, but dialogue cast does not
establish a separate house ID. Do not invent GetArea links or unlock flags.

On +12/PID12142, normal navigation reached the actual Airport choices. One
missions tap and one held input (~259ms) left the same scene/options visible.
Delivered Android press/release does not prove native choice acceptance, parsed
command execution or next-scene stack updates. No errors in a bounded tail do
not prove the commands executed. The pending cruise control uses the same
fade/wait prefix and a different goto mission-area; only missions adds snd-stop.

Parser flag distinction: SetIgnoreGoTo G8c7e40 writes+0xd. Parse G8cea30 resets
+0xe to0 for each script. InsertIgnoreGoto G8cd768 sets+0xe only when+0xd is
nonzero; InsertGoToScene G8cb8e4 refuses+0xe==1. They are not one direct flag.
The literal missions script contains no ignore-goto command. This does not
establish its live assembled script/flag state, and no flag was disabled.

The MStage callback Gb38de0 (proven ELF unwind start b28de0) also performs83→58;
its containing tutorial-result prerequisites remain unknown. The large ApplyScene
decompile timed out; the factory enum proof uses original TBH/constructor bytes,
not that failed output. Evidence is the named ghidra-episode-* dispatch/flag dumps
and episode-009 report. All account/progression journals remain preserved.

## Control and entry-specific gate recovered

One ordinary cruise control succeeded: runtime vptr21719b4 matches original
CSRSceneAreaSel vtable21719ac+8; actual Expedition Area/Glacier/Snowfield displayed.
Thus common choice handling and the shared fade/wait prefix can work. This still
does not directly trace the earlier Mission callback.

OnButtonClick8f1214 requires BT_SEL widget identity and specially checks selected
TALK(+4,+8)==(4,2). ParseTalk writes @ID to+4; ParseJson's incoming-link pass writes
the source entry's ID to destination+8. This is entry4 from predecessor2, not
actor/type/conversation. Both original Mission records have link2→4. That branch
requires nonzero GetStageAchieveCnt(TU35), mapped by native StaticData to n_02_03.
The account currently has0 stars/no earned orders for that stage. The original
XML's lack of gatefields therefore does not remove this native listener gate.

The original Mission Actor999 is separate from these fields. Parser flag+d/+e
distinction remains; no flag is disabled. Current normal Glacier map has0/30
and node11 available, later12/13 locked. Earned sequential battle progression
toward n_02_03 is authorized; no host unlock, Complete call or star assignment.
See episode-choice-listener-contract.md and episode-choice-node-fields.md.
