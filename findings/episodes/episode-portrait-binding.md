# Episode res2 portrait binding: actual consumers and limits

2026-10-05. Read-only original ELF Thumb/retained symbols, parent `ghidra-episode-presentation.txt/-keys.txt` and `ghidra-episode-story-cell.txt/-keys.txt`, and original C003 package bytes. No VM, Ghidra, client/server/original mutation. G addresses are ELF+0x10000.

## Recovered fields, not an automatic loader

CSREpisodeData constructor **Gb153cc** parses res1 at **Gb155fc/Gb15600** into a native string **data+0x28**, and res2 at **Gb15646/Gb1564a** into **data+0x34**. Original first story E01_S01 gives res1 EP_DIA_4/res2 C003_DIALOG. Parsing a string does not prove a resource request.

**SRGetResDlgID2 G10ad60c** formats `%s_DIALOG`; original LDR G10ad614/ADD G10ad61c proves the name format. Parent reports no direct Ghidra callers. Therefore this helper cannot establish that Episode reads res2, loads C003_DIALOG, or registers it. It must not be promoted into a mandatory first-story resource dependency based on name resemblance alone.

## Actual chapter and story presentation paths

**Chapter:** CSRCellMEpisodeDraw.SetData **Ge55b50**, parent dump line1001, hashes **data+0x28=res1** then calls **CSRUIImageNode.LoadSprite at Ge5608e** into named **SPR_BG**. This is a proven original sprite consumer of res1. Its second LoadSprite at Ge56426 is reward/requirement item info thumbnail string+0x38 (dump1236), not Episode res2. No res2+0x34 loader appears in the audited chapter-cell body.

**Story-list cell:** CSRSceneMEpisodeStageList.SetTableViewItemData **Ge642cc** calls **CSRCellMEpisodeStageDraw.SetData Ge646b8 at Ge6433e**; factory is Ge64b8c. Original factory sequence is LoadView Ge66108, Create Ge66410, then SetData. Parent story-cell dump and original0x4d4-byte SetData show title/detail text and EP_DIA_FIGHT/EP_DIA_TALK/EP_CLEAR/deactive visibility. No LoadSprite, LoadAnim, LoadSpine or resource-name transformation consumes res2 in that audited body. Its fixed cached view initialization is separate from the graph strings.

**Actual map point:** original **StageList.SetData Ge5f2e4** calls **CSREpisodeMapDraw.AddPoint Ge62af4 at Ge5f510**. AddPoint calls **CSREpisodeMapPointDraw.factory Ge676ac at Ge62b2e**, then attaches the resulting node at Ge62b8c. Factory calls LoadView Ge66e78, Create Ge670cc, then SetData Ge666dc. Original SetData is0x1b4bytes and sets TX_EP_ON/TX_EQ_DT1 text; it contains no resource loader. Original Create copies cached view, clears/attaches children and aligns them; no dynamic sprite/animation loader appears. Parent can decompile the small SetData/factory if a readable confirmation is wanted; these are actual map consumers rather than an unused naming helper.

Thus **res2 is parsed data but has no demonstrated loading role in the three audited presentation consumers**. These findings remove the earlier assumption that C003_DIALOG must be separately loaded for first-story map presentation. They do not prove the field globally unused: graph-to-EPISODE_STAGEDATA construction or an unaudited later consumer might read it. StageList.SetData Ge5f2e4 is the narrow remaining dataflow target if global exclusion is required.

## Original C003 resources, not a fabricated alias

The original C003.jet complete header walk yields **C003, C003_A, C003_AB, C003_B, C003_D, C003_DA, C003_DB**, with respective headers0,318773,319647,319918,348085,1013027,1013428. Original RW C003_DA includes atlas text `C003_d.png` with a1024x1024 atlas and Body1 region; C003_DB is binary actor/skeleton data. No verified record or consumer maps these to C003_DIALOG. No original alias should be added from suffix similarity.

`episode-first-story-assets.md` preserves the exhaustive774-pack outer-header inventory: no descriptive outer record C003_DIALOG, while EP_DIA_4 and EP_0301A are positively recovered. Outer-name absence does not exclude runtime-generated/nested/hashed identifiers. The original first-story XML actors are Char009 user, NPC001 Lana and Char004 Tyltyl; the real dialogue actors and their creation loaders are a separate dependency check from C003 map metadata.

## Safe next action

Do not block a bounded original first-story opener solely on the unused `%s_DIALOG` helper, and do not add guessed aliases. Positive original catalog, EP_DIA_4, English EP_0301A XML and all its explicit background/music/voice records are documented. If parent wants a complete static closure before native observation, recover **StageList.SetData Ge5f2e4**'s graph-to-stage construction and the actual dialogue portrait creation helpers for Char009/004 and NPC001. This report claims the proven consumer boundaries, not runtime playback or a recovered C003_DIALOG registration.
