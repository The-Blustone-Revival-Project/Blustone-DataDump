# Ordinary Episode entrance: proved scene identity, route still incomplete

**Continuation:** episode-dialogue-choice-dispatch.md now closes the original
ordinary route: NPC0000/NPC0005 missions entry4 runs goto-scene mainstream,
which maps to Episode58 through intermediate83. The route-incomplete statements
below are historical for that exact choice. Live listener/command execution and
Episode rendering remain unverified; the two Airport input probes were unchanged.

2026-10-05. Read-only original ELF Thumb/TBH/RTTI, retained episode routing evidence and native symbols. No Ghidra, adb, source edits, flags, scene invocation or navigation. Parent's tester remains on the retained archive screen; this lane did not operate it.

## Exact Episode List identity

**CSRSceneMgr.ApplyScene Gea6600** dispatches a bounded scene enum through TBH atea673a. ADRr2 at ea6712 selects table **ea6744**, and branch PC is ea673e. Table index **58decimal/0x3a** targets **eaa256**, which constructs **CSRSceneMEpisodeList**. Positive constructor evidence: shared_ptr<CSRScene> conversion **ec459c** is called ateaa2d8, and that object/control pair is stored atmanager+34/+38 ateaa2e8. Thus **SceneTYPE58 is the Episode List**, not an inferred story-archive type.

Its **OnInit Ge5141c** loads original **EPISODE/E_T_EPISODE** (LDR e5146a/ADD e51472), uses BGM_LANA, and reads markers **GET_EPISODE_REWARD** and **event_episode**. It selects **SetData Ge51908** with event mode1 at e516e2 or ordinary mode0 at e516fe. The ordinary/event ID marker interpretation and entry-dependent default season need the complete OnInit decompile before a live action can be proposed.

The tester's Story/archive menu belongs to **CSRTableDlgCollection** (its OnButtonClick Gfef1ce). An archive rendering or its dialogue collection does not prove the Episode List scene was reached. The Episode List's original graph/load resources and progress API are separate, as episode-progression-contract.md documents.

## Positive Village route is an event badge

Original function-object vtable **ELF216bd04** invokes **Gdc3568**; RTTI explicitly names **CSRPopUpVillage.MakeEventBadge::$_44**. That callback sets local **event_episode** marker with string **Depth** (LDRdc3580/ADDdc3586 anddc358c/dc358e; SetMarker atdc359e), then executes the normal UI callback transition **PushSceneFadeNone(TYPE58) atdc35ca**.

This is a genuine native clickable event-badge route, **not** proof that the same control opens regular S01. The containing maker is **Village.MakeEventBadge Gdb18f8**. Its exact visible badge label/hash and original schedule/visibility gates are not reconstructed in this bounded lane. Do not activate an expired EV05 or manually create this marker to manufacture an entrance. The exported original event catalog's historical end date still applies.

## Airport/area-selector observations and gates

**CSRSceneAreaSel.OnButtonClick Ge741dc** explicitly compares original controls **BT_NOMAL** (spelling is original; ADD e7421a), **BT_SPECIAL** (e7423c), **BT_MY_ST** (e744e2) and **USER_BT** (e74596). The first2 select normal/special area data. No direct constant SceneTYPE58 transition was identified in this ordinary handler's inspected body. Dynamic area-node/table/inherited callbacks remain possible; do not rename BT_MY_ST as a proved Episode button merely from its shorthand.

**SetAreaState Ge75cdc** applies a real team-level gate: GetUserLevel at e75d34 compares against **AREA_INFO+40 level_limit** at e75d38/e75d3c. It also calls **GetStageAchieveCnt at e7608c** for progress gating. These are actual area gates, but the exact original Episode area/link record and which control routes to it are **unknown**. Current reconstructed normal campaign areas are not evidence of a missing Episode row identity that can be guessed into GetArea.

A few other exact TYPE58 call sites exist (e.g. MStage post-result closure b38df6→PushSceneFadeOutIn b38e02 and Episode List e549a4→e549aa), but their caller prerequisites are not recovered here. They must not become direct scene-jump proposals.

## Smallest parent dump set

To close the actual regular UI entrance without guessing routes/buttons:

```text
AreaSel.OnButtonClick e741dc
AreaSel.SetAreaState e75cdc / SetSpecialAreaState e765fc
EpisodeList.OnInit e5141c / SetData e51908
Village.MakeEventBadge db18f8 (event route/visible label only)
MStage continuation containing b38df6 (normal post-story availability route)
```

The known constructor branch eaa256/ec459c and enum58 attribution need no additional guessing. If AreaSel uses a transitive node command/helper, dump only that helper once the parent decompile names it. A bounded screenshot of actual airport selector controls/locks and current scene-vptr will then connect a real user action with the recovered route.

The regular S01 entrance, exact visible English button/hash, and original Airport Episode-link record remain **unproved** in this report. Do not add a fabricated reference route, force TYPE58, edit markers, reset usage or unlock gates. This report supplies positive identity/event-route/gate evidence and precise remaining targets, not native entrance acceptance.
