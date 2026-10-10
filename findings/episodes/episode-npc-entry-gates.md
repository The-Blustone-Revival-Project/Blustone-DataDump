# Regular S01 Episode entry: original graph fields and gate limits

2026-10-05. Bounded read-only recovered original R_EPISODE S01 graph/localization and existing native entrance/parent-progress reports. No VM, Ghidra, server/reference changes, rewards, read/clear flags, unlocks or scene jumps. Current +12 UI observations are parent context, not an action by this lane.

## Exact regular catalog identity and first chapter

Original R_EPISODE named **SEASON_LIST** payload is `["season1"]`; named **SEASON1** payload's graph root is **type:"season",id:"S01",title:"S01_TITLE",desc:"",res1:"RES1",res2:"RES2",childs:[...]**. The loader resource name season1 is separate from graph ID S01. Existing native ReadJson lookup handles case; no new alias or API route follows from this spelling.

Original `analysis/recovered-reference/EPISODE_S01.json` has18 chapters/128stories/147unique nodes. Its first chapter **E01** has typeepisode,titleE01_TITLE,descempty,res1EP_BTN_01,res2C003_DIALOG and reward.itemGC2qty3/free_iap0. Parent's reward handling is separate; this original display declaration is not an entrance gate or grant.

Original localization (`UI_EPISODE.json`) names **S01_TITLE = Season 1. Metron Hunter**, **E01_TITLE = A Sudden Test**, **E01_S01_TITLE = Captain Qualification Test**.

## First chapter's actual location and entrypoint map

All positions below are original `pos.localname/x/y` metadata, not /reference/GetArea or village NPC IDs:

- **E01_S01**: local_MIDGARD, x1235/y1150, entrypointEP_0301A, battlefalse.
- **E01_S02**: local_GYM, x1225/y1160, entrypointEP_0302A, battletrue, linkedcombatonlyforrefCB0101.
- **E01_S03**: local_MIDGARD, x1235/y1150, entrypointEP_0303A, battlefalse.
- **E01_S04**: local_EASTSNOW, x1340/y1180, entrypointEP_0401A, battletrue.
- **E01_S05**: local_EASTSNOW, x1340/y1180, entrypointEP_0402A, battlefalse.
- **E01_S06**: local_EASTSNOW, x1340/y1180, entrypointEP_0403A, battletrue.
- **E01_S07**: local_MIDGARD, x1235/y1150, entrypointEP_0404A, battlefalse.

Exact EN location text: **local_MIDGARD Midgard**, **local_GYM Hunter Gym**, **local_EASTSNOW East Snowfields**. These support narrative/map geography only. Do not publish guessed campaign area/link rows or assign village house IDs from these names/coordinates.

The original first conversation **EP_0301A** positively exists in DIAL-EN.jet (episode-first-story-assets.md). It includes playerChar009, **NPC001 Lana**, and Char004 Tyltyl. **NPC001 is a cast member inside that conversation**, not a proved village entrance NPC for SceneTYPE58. Likewise chapterres2C003_DIALOG is parsed illustration metadata, not an entryNPCID. Its unused generated-name helper is not a route prerequisite (episode-portrait-binding.md).

## No explicit opening gate is serialized in regular S01

A recursive bounded scan of all147 original S01 nodes finds **zero fields named/containing limit, require, schedule, level, tuto, read, clear or unlock**. E01 and its first leaf have no tutorial type/step, team level, cleared campaign stage, predecessor-read condition, or activation datetime. This is an exact property of this recovered graph, **not proof regularS01 should be globally unlocked**: native scene/NPC code, enum/parser defaults, implicit child order and player progression can impose additional conditions.

The graph's seven E01 children are ordered as above. JSON ordering provides a story sequence; it does not independently prove which preceding read/clear acknowledgment activates the next cell. **episode-parent-progress.md** proves actual clear/read sets and native pending traversal: encodedr_ID reads are distinct from bareID clears, and parent IDs require their own normal native acknowledgment path rather than automatic server inference. Those progression semantics do not supply an original initial S01 NPC entrance condition.

Thus original JSON cannot justify a rule such as "clear stage7/8 to open Episode", "finish TU37", "teamlevelX" or "NPCY exposes S01". Those would require actual native caller/gate evidence. No such rule is inserted here from server fixtures.

## Native entrance evidence remains separate

Existing **episode-ui-entrance.md** proves **SceneTYPE58/0x3a = CSRSceneMEpisodeList**, OnInit Ge5141c loads EPISODE/E_T_EPISODE, and ordinary/event SetData branches differ. A genuine village **event badge** closure Gdc3568 sets **event_episode:"Depth"** then PushSceneFadeNone(TYPE58). This is positive event-mode routing, **not a regularS01 entrance**, and should not activate an expired event or manufacture the marker.

The +12 Story menu is **CSRTableDlgCollection/dialogue archive**; reaching it does not mean regular EpisodeList was entered. The known Airport normal/special/mission controls likewise do not yet prove an Episode route. Existing AreaSel.SetAreaState team-level/achievement checks apply to actual area references, but no original Episode area/link row was recovered; do not synthesize one to make those generic gates fit.

The inspected existing native entrance documentation does **not** identify a regularS01 village NPC, house, exact button/hash, NPC reply, tutorial prerequisite or implicit graph gate. This is a narrow unresolved route, not evidence that the preserved catalog is incomplete.

## Finite next proof boundary

Catalog/story identities, E01 geography, original conversation cast and absence of serializedS01 gates are closed. The next parent-only proof is a genuine ordinary EpisodeList entry caller and its scene/NPC activation condition, plus ordinary OnInit/SetData defaults if needed. Use actual NPC/dialogue routing or the retained TYPE58 caller chain; do not repurpose the archive, Depthbadge, native dialogue actor IDs or /reference/GetArea fixture names. No grants, flags, fake unlocks or direct scene invocation follow from this report.
