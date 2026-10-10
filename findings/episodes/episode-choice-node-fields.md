# Episode choice TALK node fields: ID and incoming predecessor

2026-10-05. Bounded existing native dumps and already-decoded original NPC0000/NPC0005 XML only. No runtime, VM, Ghidra, source edits, flags or grants. G addresses use ELF+0x10000.

## Exact field writers

**CSRParserDlg.ParseTalk Gb5b604** initializes TALK+4 to0 and TALK+8 to-1: `ghidra-episode-talk-node-types.txt` lines93–94. The actual `@ID` literal is resolved in `ghidra-episode-talk-node-type-keys.txt` line3: LDRGb5b6ca/ADDGb5b6cc. ParseTalk's numeric conversion of that JSON attribute ends with **`*(uint *)(param_1 + 4) = uVar9`**, node-types line158. Therefore **TALK+4 is DialogEntry @ID**, not Actor or ConversationID.

**CSRParserDlg.ParseJson Gb5a490** performs a later incoming-link pass: `ghidra-episode-dialogue-conversation-ids.txt` lines1154–1171. It iterates each source TALK's outgoing next-ID vector at map-node+0x70/+0x74 (lines1154–1156), finds a destination node by that numeric ID, obtains **`iVar31 = piVar36[6]`** (line1162), and assigns **`*(int *)(local_d0 + 0x1c) = iVar31`** into the destination (line1171). The map stores TALK at node+0x14: source node+0x18 is TALK+4, and destination node+0x1c is TALK+8. The vector arithmetic corroborates the same offset: node+0x70−TALK+0x14=next-ID vector+0x5c, matching the native choice consumer.

Thus **TALK+8 is a recorded incoming source/predecessor DialogEntry ID**. It is a scalar populated by the postpass, not the conversation number, actor ID or field type.

## Original missions node and native gate

Already decoded original **NPC0000 and NPC0005** both have containing Conversation@ID1, missions **DialogEntry@ID4**, and a unique incoming link **entry2→4**. Both mission nodes have Actor field TypeActor/value999 and Conversant TypeActor/value1. Accordingly their parsed static TALK tuple is **(+4,+8)=(4,2)**; Actor999 and Conversation1 are separate evidence.

`episode-choice-listener-contract.md` records native **DlgPlayer.OnButtonClick G8f1214** comparing selected TALK+4/+8 against4/2 at **G8f1346/G8f134c**, then gating at **G8f14f2→GetStageAchieveCnt(TU35) G8f14fc**. Its exact native stage mapping is **n_02_03**. This establishes which original static node tuple can take that gate; it **does not prove a current live Mission callback ran or that the live selected TALK was this record**. Parent's reported zero stage stars and unchanged taps are separate observations. No current-node reader was executed here.

## Multi-incoming uncertainty

The incoming-link pass writes one destination+8 scalar unconditionally for each found incoming source. Multiple incoming links can therefore overwrite it; the retained source ID reflects the last applicable write in native traversal, not necessarily the predecessor used by a later live dialogue transition. This unit does not certify traversal order or runtime rewriting for general multi-incoming dialogs. NPC0000/0005 missionsID4 each have only the one2→4 link, so that ambiguity does not alter this specific original static tuple.

The saved evidence closes the ID/predecessor meaning without guessing actors, gatefields, dialogue IDs or live dispatch. No further search or recovery action is implied.
