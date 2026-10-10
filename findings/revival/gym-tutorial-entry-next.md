# Native Gym tutorial entry: narrow follow-up

2026-10-04, read-only original ELF Thumb call/literal inspection and curated reports. No grants, source/adb/Ghidra/client changes. G addresses are ELF+0x10000.

Ordinary Raise success is_tuto0 does not execute the TutorialLevelUp-specific completion closure, so target5 EXP130 can coexist with uncleared native8/1. Do not clear manually or consume another original card to hide that difference.

## Actual entry/ownership facts

- SceneMgr ApplyScene Gea6600 calls TutorialLevelUpCardSel constructor Geec43c at Gea9d5c, shared_ptr conversion Gebdbc4 at Gea9d66, stores actual current object at manager+34 Gea9d76.
- TutorialLevelUp factory arm calls shared_ptr conversion Gebddc4 at Geadfde, stores actual object to manager+34 Geadfee. Thus tutorial Raise can be a real manager-owned scene, not a guessed modal pointer.
- TutorialCardDetail OnInit Gee6244 first runs ordinary CardDetail OnInit, reads CSRLocalDB.GetSelectedInstCard at Gee62c0 and Gee6386, then resolves Inventory.FindCard at Gee63b2. Selected target comes from native local selection, not a hardcoded target5 demonstrated here.
- It calculates native ordinary hunter level via GetCardLevel at Gee646e. Only when level>=30 and rank==1 (Gee647c..82) does the inspected branch set marker numeric6. This is a native rank-up guide transition, not a reason to reinterpret targetEXP130 as rank-up-ready.
- It reads marker **tuto_training** (LDR slotGee6610, ADDGee64dc architecturalPCGee64e0; original bytes G1d79b94) at GetMarker Gee64e8. Exact dispatch: marker4→SetTutorialLevelUp Gee6614 at Gee654a; marker6→SetTutorialRankUp Gee6834 at Gee655a; marker8→SetTutorialRankUp2 Gee6924 at Gee6552. Other marker values skip these three inspected tutorial starts.
- Known tutorial Raise completion uses is_tuto1 and genuine callback GeeC070 to RequestClear(8,1); ordinary TableLevelUp uses is_tuto0. See training-onboarding-clear-contract.md for full shape and its failure-path caveat.

## Missing entry predicate and minimum parent dumps

The root cause of Home guide remaining plus ordinary Gym choices39 is not yet proved. Need native branch that selects TutorialLevelUpCardSel/TutorialCardDetail versus ordinary CardSel/Detail and sets marker4. Do not infer choice39 equals a tutorial type or manipulate marker from its label alone.

1. **TutorialLevelUpCardSel::OnInit Geec508**, and relevant override/card-selection handler if it invokes a helper: identify target selection and next Scene TYPE.
2. **TutorialCardDetail::OnInit Gee6244** and **SetTutorialLevelUp Gee6614**: prove marker4 setup/read and guided button's actual PushScene TYPE.
3. SceneMgr ApplyScene focused factory slices **Gea9d52..Gea9da4**, **Geadfd8..Geae01c**, plus the dispatcher case entries reaching them: identify exact scene TYPE numbers. Whole ApplyScene is large; prefer dispatcher/case xrefs.
4. **TutorialLevelUp::OnInit Geea490 / SetTutorialLevelUp Geea4b0** only if guide startup/target mapping remains ambiguous after entry.

The inspector can read native current scene vptr and selected-ownedID/marker with existing guarded capabilities. It must not write marker, clear tutorial, grant/consume extra hunter or synthesize is_tuto1 as a substitute for native entry. No native tutorial progression success is claimed here.

## Fresh village/card scene dumps: marker sequence and exact closures

Sources now `ghidra-gym-entry-card-scenes.txt`, `ghidra-gym-entry-card-scene-strings.txt`, `ghidra-gym-village-training-entry.txt` and its strings.

ResumeTutorials Gda0408 sets the local tuto_training marker only when its current numeric value is zero. A stage-achievement enum16 (known n_01_07) positive branch initializes1. A later branch with native state(8,0)>1, stage7 achievement>0, state(8,1)<=1, and stage-achievement enum44 (n_01_08)==0 initializes6 when empty. Nonzero marker is left intact. Other earlier tutorial priority branches can divert execution; these are exact relevant branch conditions, not a claim all preceding tutorial gates are satisfied live.

SetTutorials Gda0ccc reads tuto_training into uVar6. Marker1 or6 schedules the same training guide closure; marker9 removes marker and shows next finger indicator. SetTutorialTraining Gdba178 shows building name tag8, then AppearAfterFade on focus drawer with a captured Village callback. TutorialLevelUpCardSel OnInit Geec508 calls TutorialTraining only when marker==3; TutorialCardDetail OnInit dispatches Raise only when marker==4. These are local guide phases, separate from persistent server tutorial8/1. Ordinary is_tuto0 LevelUp success does not substitute for those guided phases.

Exact original hidden std::function vtable/operator targets for the missing transitions:

- Village SetTutorialTraining: slotGdba268 + matched PCGdba1c8 → vtable G217c66c, operator slot0x18 **Gdc98b8** (nextslot0x20 Gdc9ac0).
- CardSel TutorialTraining: slotGeec76c + PCGeec6cc → vtable G21873b4, operator slot0x18 **Geecbdc** (nextslot0x20 Geecde4).
- Village SetTutorials scheduled marker1/6 closure: slotGda1360 + PCGda0ffe → vtable G217b434, operator slot0x18 **Gdbbbe2** (nextslot0x20 Gdbbc14).

Parent focused decompile should start these exact Thumb callable entries rather than neighboring guesses. They can pin building click/scene route and genuine marker transitions to3/4. Current supplied dumps schedule the closures but do not contain their bodies, so no exact button key or marker1→3→4 mutation is invented here. No server marker route or host SetMarker action is proposed.

## Valid Thumb closure continuation (supersedes bad ARM closure output)

Use `ghidra-gym-entry-closures-thumb.txt`; earlier `ghidra-gym-entry-closures.txt` BADARM output for Gdc98b8/Geecbdc is historical invalid evidence.

- Village Gdc98b8 shows guide comment, then GuideMsg.Appear callback vtable/addresspoint **G217c6a4** (DATGdc9aa4 + PCGdc99a4), operator+0x18 **Gdc9b0c**.
- Gdc9b0c sets focus circle and FocusDraw.Appear; its callback **G217c6dc** (literalGdc9c90 + PCGdc9bcc +8), operator **Gdc9cf8**.
- Gdc9cf8 waits for actual touch; its callback **G217c714** (literalGdc9d68 + PCGdc9d16 +8), operator **Gdc9dd0**.
- CardSel Geecbdc shows guide comment, then GuideMsg.Appear callback **G21873ec** (DATGeecdc8 + PCGeeccc8), operator **Geece30**.
- Geece30 waits for actual touch; callback **G2187424** (literalGeecea0 + PCGeece4e +8), operator **Geecf08**.
- Geecf08 calls GuideMsg.Disappear; callback **G218745c** (literalGeecfec + PCGeecf42 +8), operator **Geed054**.

All invoke targets have original Thumb low-bit1. The smallest next parent valid-Thumb dumps are **Gdc9dd0** and **Geed054**, skipping the pure focus/touch/disappear wrappers. No earlier wrapper itself calls SetMarker or PushScene in the inspected bounded body; exact final button/scene transitions remain to be recovered from those after-touch closures.

## Actual native scene and target transitions reached offline

Village after-touch GuideMsg.Disappear uses addresspoint **G217c74c** (DATGdc9f48 + PCGdc9e7a), operator **Gdc9fb0**. This tiny Thumb function gets app SceneMgr and calls **SceneGoTo(TYPE0xA7)** at Gdc9fbc. No guessed button key or server marker route is necessary to describe this native transition.

CardSel after-touch GuideMsg.Appear uses G2187494 (DATGeed240 + PCGeed140), operator **Geed2a8**. Its subsequent original vtable chain:

```
Geed2a8 WaitForTouchInput -> addresspointG21874cc -> Geed380
Geed380 Disappear/focus -> G2187504 -> Geed560
Geed560 first table item ShowFingerIndicator -> G218753c -> Geed6c0
```

Callback literal checks (all actual code adds8 after matched PC-relative pointer): Geed2bc slotGeed318+PCGeed2c6+8; Geed418 slotGeed4f8+PCGeed422+8; Geed59c slotGeed658+PCGeed5a6+8. Invoke is addresspoint+0x18, with original Thumb bit1.

**Final Geed6c0 performs the real mutation/scene transition:** local marker numeric4 set at Geed6f6/SetMarker Geed708; Inventory.GetCardInstIDList Geed746; nonempty vector sorted by helper **Geed8a0** at Geed77c; first vector uint64 loaded at Geed7c4 then CSRLocalDB.PutSelectedInstCard Geed7c8; **PushSceneFadeOutIn(TYPE0xA9)** Geed7dc. This tutorial automatically chooses the first sorted owned hunter, so the target is not proved to equal the user's ordinary clicked Tyltyl5. Original sort criteria remain a narrow question; do not assume lowest serial/level or write target selection to force it.

Best parent valid-Thumb dumps now **Geed6c0** and **Geed8a0**, then TutorialCardDetail SetTutorialLevelUp Gee6614 if its next guided button transition is needed. Village Gdc9fb0 is a12-byte SceneGoTo tailcall already fully decoded. Guide callbacks/source consumption still require exact existing donor protections; local marker4 is native UI progress, not server8/1 completion.

## Actual Scene TYPE mapping and target comparator (2026-10-04 follow-up)

Original ApplyScene dispatcher at Gea673a is TBH[r2,r0<<1]; tablebase **Gea6744**, architectural branchbase **Gea673e**. Raw halfwords establish:

- TYPE **0xA7 and0xA8** → arm **Gea69da**, which calls SetHouseNPC Geb2580 at Gea6a0a. These are **trainer NPC dialogue entry**, not direct TutorialLevelUpCardSel.
- TYPE **0xA9** → **Geaad06**, calls TutorialCardDetail make_shared Geb9658 at Geaad0a.
- TYPE **0xAE** (174) → **Gea9d52**, constructs TutorialLevelUpCardSel Geec43c and stores it as manager current scene.

The NPC arm passes SetHouseNPC args r1=SceneTYPE0xA8, r2=TU16, r3=SceneTYPE8. Its three literal string arguments are exactly **NPC0042**, **NPC0040**, **NPC0041** from slotsGea6c88/8c/90 with matched PCGea69e2/69ec/69f8. A previous quick intermediate note `042` cross-paired slot/PC and is retracted. Meaning/order of the three dialogue keys requires SetHouseNPC body rather than guessing.

Thus Village SceneGoTo(A7) correctly reaches trainer dialogue. To prove how dialogue progresses into guided selection TYPEAE rather than ordinary Gym choices39, parent smallest dump is **SetHouseNPC Geb2580** plus actual dialogue completion/option handler it configures. Do not rewrite SceneGoTo toAE or force local marker as a workaround.

Target sort comparator **Geedbc8** resolves each uint64 argument through Inventory.FindCard, loads card+0x18 as uint64 for both, and returns unsigned ascending comparison (SUBS/SBCS/LO at Geedd06..14). That member is **regdate**, not inst_id or level: original CSRCard::parse key`inst_id` ADDG8680c4 stores+0x10 atG86810e; key`regdate` ADDG8681b4 stores+0x18 atG868200. The tutorial therefore chooses first/oldest registration after sorting. Equal fixture regdate0 has no comparator tie-break by ID or level, so target5 is not ensured. Existing data should remain unchanged; next native observer must inspect actual selected target before any source transaction.

Parent short proof-preservation targets: **Geedbc8** comparator; **Geb2580** NPC entry; ApplyScene case slices **Gea69da..Gea6a0e**, **Geaad06..Geaad20**, **Gea9d52..Gea9d7a**, plus TBH table indexesA7/A8/A9/AE. Correct original instruction/literal flow avoids the earlier generic nearest-ADD errors.

## SetHouseNPC entry gate and interruption behavior

Fresh `ghidra-trainer-house-npc.txt` resolves the argument semantics: signature is **SetHouseNPC(SceneTYPE, TU_TYPE, TU_TYPE, string,string,string)**. Prior note labeling r3=8 as SceneTYPE is superseded: caller passes nextNPC SceneTYPEA8, achievement gate TU16, entry tutorial TU8.

Exact branches:

1. GetStageAchieveCnt(TU16)==0: ordinary NPCDlg with third key NPC0041 and SR_NPC_BRIDGE.
2. Stage7 achievement exists and GetState(8,0)<2: RequestClear(8,0) first (forTU8, since onlyTU2 skips that clear), then constructs TutorialNPCDlg using first key NPC0042 and SR_NPC_TUTORIAL_BRIDGE.
3. Stage7 achievement exists and state(8,0)>=2: ordinary NPCDlg with second key NPC0040 and SR_NPC_BRIDGE.

This predicts ordinary trainer dialogue after a restart once native Clear8/0 was acknowledged, even when later guided Raise/Clear8/1 never completed. It does not prove the entire continuing guide is irrecoverable or authorize reverting cleared flags. Village ResumeTutorials may separately schedule marker6 for incomplete8/1, but SetHouseNPC itself chooses its tutorial-class branch using8/0.

TBH normalization rechecked: ApplyScene reads current scene TYPE directly from history-node+8 atGea6708; no subtract is applied before TBH Gea673a. TablebaseGea6744 and branchbaseGea673e yield A7/A8 same NPC arm, A9 TutorialCardDetail, AE TutorialLevelUpCardSel. SceneGoTo's own dispatcher subtracts9 for its separate control table; do not apply that subtraction to ApplyScene.

Current SetHouseNPC dump configures bridge names/Init but does not include bridge event handlers. Smallest next parent targets to pin legitimate normal/tuto Stronger bridge: **NPCDlg::Init Gec5e94**, **TutorialNPCDlg::Init Gee8c74**, **NPCDlg::Load Gec6790**, **OnButtonClick Gec6ff4**. Their configured callback/operator targets may hold SceneGoTo/marker-specific continuation. Preserved all-tables snapshot has no NPC0040/41/42 record; no original script body is fabricated from key names. No marker mutation, tutorial rollback, host grant, source consumption or direct AE jump applied/proposed.

## TutorialNPC reply continuation recovered

Fresh `ghidra-trainer-dialogue-bridge.txt` proves TutorialNPC Init calls ordinary NPC Init, then adds tutorial event/finger handlers and reads local markers. Training marker1 or2 selects finger0 callback addresspoint **G2186bf8** (DATGee8fb4+PCGee8ec8), operator **Gee9894**. Original Thumb body sets numeric marker3 at Gee98c6/SetMarker Gee98d8, then **PushSceneFadeOutIn(TYPEAE)** Gee9906. This matches TutorialLevelUpCardSel's marker3-only guide startup.

Training marker6 selects callback **G2186c38** (DATGee8fb8+PCGee8eec), operator **Gee99a8**, directly **PushSceneFadeOutIn(TYPEAE)** Gee99b8 without the same marker3 setup in its tiny body. It routes to selection for the rank tutorial continuation, not proof to rerun first Raise automatically.

Ordinary NPC Init/Load supplied bodies contain no training marker setup/read or tutorial SetFingerIndicator. OnButtonClick handles header currency/BP controls rather than dialogue reply buttons. **Do not yet conclude ordinary NPC0040 cannot resume through a script/generic reply bridge:** its dialogue player callback bindings are outside these supplied functions. A class-only branch difference is not whole-program absence proof.

Smallest final parent dumps: **Gee9894**, **Gee99a8** for concise native bridge proof; **NPCDlg constructor Gec5b1c** to identify player-reply callback targets. Tutorial Init event callbacks additionally resolve G2186af8→Gee95a2 (scene+58), G2186b38→Gee960e (scene+74) if completion bridge differs. No rollback, direct scene jump or marker write recommended/applied.

## Constructor audit and actual generic reply routing seam

`ghidra-trainer-dialogue-constructor.txt` NPCDlg constructor Gec5b1c only allocates CSRDlgPlayer and initializes fields; it does not install the anticipated reply callback. NPC Init calls player's virtual Init with `NEW/SR_DIALOG/0_UI_DIA3`; NPC Load supplies parsed conversation and starts/skips dialogue. Its OnButtonClick is HUD controls, not dialogue reply selection. Guided selection callback fresh valid dumps corroborate previous marker3/AE and marker6/AE behavior.

The actual generic scripted scene seam is **CSRDlgScriptPlayer::GoToScene(GOTO_SCENE const&) G8f92d4**, overload **GoToScene(SceneTYPE,string const&) G8f99d8**. Read-only original Thumb identifies calls into overload at G8f9588/G8f9726/G8f9770, tutorial GetState at G8f97e2, direct SceneGoTo G8f9846, and dialogue GoToDialog G8f9824. Those exact branches can establish whether ordinary SR_NPC_BRIDGE has a marker-dependent guided resume, rather than inferring absence from the NPC class. Reply click progression resides in **CSRDlgPlayer::OnButtonClick G8f1214** and **SpawnNext G8edf70**.

Parent next minimal dumps: G8f92d4 and G8f99d8 first (routing/remap), then G8f1214 only if reply-to-script emission needs attribution. The current observer APK build/publication changes are separate telemetry work and do not prove gameplay routing changed. No ordinary resume guarantee or unsafe directscene workaround is claimed.

## Generic scripted routing does not contain Gym resume remap

Fresh `ghidra-dialogue-scene-routing.txt`/strings fully recover G8f92d4 and overloadG8f99d8. They contain no GetMarker(tuto_training), no TU8/1 state check, and no AE output. The one GetState in the main function is **TU0x26 step0** for guild-war/NPC0083, unrelated to Gym. A command hashed0xd5128a8f maps to **TYPEAF**; its original textual command is not recovered in this pass, so do not name it from CRC guess.

Overload AF invokes SceneGoTo(A8) then PushSceneFadeOutIn(AF); original ApplyScene table AF→armGeab032 constructs **ordinary CSRTableCardList**, shared_ptr conversion Gebdac4 at Geab0be. Contrast AE→TutorialLevelUpCardSel. This is a concrete ordinary-versus-guided divergence without modifying routes or state.

These two generic routing functions therefore provide **no pending8/1-specific remap** themselves. TutorialNPC's explicit marker/finger callbacks remain the only proved AE continuation. Global absence of an ordinary scripted resume is still not proved until actual NPC0040 reply script/bridge event action is inspected; it might explicitly name a different route rather than relying on a generic remap. Current server choice39 alone is not original script-command proof.

No gameplay changes inferred from observer APK/Windows CURRENT CRLF recovery. Existing server/native pending state remains evidence, not a reason to force marker or scene TYPE.
