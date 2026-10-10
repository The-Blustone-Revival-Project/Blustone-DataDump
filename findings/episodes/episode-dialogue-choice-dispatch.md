# Airport missions choice: original dialogue dispatch to Episode List

2026-10-05. Bounded read-only original DIAL-EN.jet XML and existing `ghidra-dialogue-scene-routing.txt/-strings.txt`, plus retained scene enum proof. No VM, Ghidra, source/original changes, scene invocation, grants or flags.

## Exact original choice and dialogue records

The choice **I heard I have missions?** is present in two original native-named resources:

- **NPC0000**: DIAL-EN.jet header2979453, packed3757bytes.
- **NPC0005**: DIAL-EN.jet header2990054, packed3757bytes.

Both are original RW/XML TalkerMakerProject dialogues with46 DialogEntry nodes. Both declare actor1 **NameLana/CardTypeNPC/CardID001**, actor2 **Name%user_name%/CardTypeChar/CardID009**. The original choice is **DialogEntry ID4**, actor999/conversant1, Menu Textnormal, Emotionnormal. Its full rendered text field is:

```text
{res=UI_DI_SL_B2}I heard I have <color='240, 20, 50, 255'>missions</color>?
```

Both dialogs' root route is **entry0→1→2**, then entry2 has normal outgoing choices **3,4,5,6**. Incoming link to ID4 is exactly OriginDialogID2/DestinationDialogID4, IsConnectorfalse, ConversationID0/OriginConvoID0/DestinationConvoID0. **ConditionsString is empty on ID4 and all46 nodes in both dialogues**. Root0 is IsRoottrue/TitleSTART; ID4 has IsRootfalse/IsGroupfalse/FalseCondtionActionBlock. Empty condition is an exact serialized fact, not proof there are no native NPC/guide/input gates outside the XML.

ID4's exact command sequence is:

```text
scr-fade duration:0.1 color:(0,0,0,255)
wait duration:0.1
snd-stop
goto-scene id:mainstream
```

NPC0000 stores a final newline after mainstream; NPC0005 does not. Neither ID4 has outgoing links. By comparison both variants' cruise choiceID3 uses **goto-scene id:mission-area**. **NPC0000** ID6 uses main-menu, while **NPC0005** ID6 uses **fishing**; the latter must not be mislabeled an exit. All share the identical scr-fade/wait prefix, but only missionsID4 adds snd-stop. They are different original command IDs; do not conflate missions with the normal campaign map.

## Existing native hash dispatcher closes the real route

Original command-string CRC32 **mainstream = 0xd98de1c6**. Existing **CSRDlgScriptPlayer.GoToScene(GOTO_SCENE const&) G8f92d4**, dump393..395, matches exactly that hash (with the high hash word0), assigns **uVar11=0x3a**, and calls its normal scene overload. This exact hash arm has no tutorial/stage/level gate; unrelated guild/tutorial branches elsewhere in the dispatcher must not be attributed to it.

The overload **GoToScene(SceneTYPE,string const&) G8f99d8**, dump618..622, handles case0x3a by **SceneMgr.SceneGoTo(0x83)** then retains **param_2=0x3a**. At dump790 it calls **SceneMgr.PushSceneFadeOutIn(param_2,0xff000000)**. Therefore the actual native sequence is **normal intermediate scene0x83, then push58/0x3a Episode List**, not a replacement transition that loses58. Existing ApplyScene TBH/constructor proof in episode-ui-entrance.md identifies **TYPE58 as CSRSceneMEpisodeList**.

This is a positive original ordinary dialogue→Episode entrance and **supersedes episode-ui-entrance.md's route-still-incomplete conclusion for this specific missions choice**. It does not say the current live choice was accepted or that Episode OnInit loaded/rendered successfully. If a tap appears unchanged, observe actual dialogue listener/command dispatch and next-scene stack rather than inventing a missing original area row or gate.

## Midgard/S01 relationship and remaining boundaries

Original first regular story **E01_S01** gives pos.localnamelocal_MIDGARD, entrypointEP_0301A and battlefalse. Its recovered XML cast includes **NPC001 Lana** alongside player009/Tyltyl004; the ordinary airport-choice dialogues above likewise name NPC001 Lana and use N001_BG/BGM_LANA/AMB_PLT in setup. This positively connects the same original NPC identity and presentation resources, **not a separate NPC field or house ID serialized in S01**. Do not derive a new location→NPC reference table from those shared values.

A complete bounded scan of all1357 DIAL-EN outer records found **only NPC0000/0005 with a UserScript mainstream command**. All147 S01 graph nodes remain without explicit gate fields as episode-npc-entry-gates.md records. Native choice listener acceptance, variant selection, EpisodeList ordinary default season and guide/input constraints are distinct next observations; no flags, forced scene jump or unlock is justified.
