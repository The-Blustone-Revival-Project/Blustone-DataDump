# CB0103 scripted actor and settlement audit

2026-10-08. Read-only review of preserved original JSON and existing native dumps. No Ghidra, ADB, source, runtime, profile or save changes. This complements `episode-story05-06-followthrough.md`; it does not prove a live CB0103 result.

## Assembly and ownership

`EPISODE_COMBAT_CB0103.json` has four empty left slots followed by fixed Hunter `CB0103_005_1`, and one right Hunter `CB0103_036_1`. Left skills are `[1,1,0,0,0]`; right `[1,1,1,0,0]`. Both are native Hunter actors, not mission monsters. Their thumb levels are 1, ranks 2/3 and attributes 2/3. There is no owned-card grant in this descriptor.

Existing `ghidra-episode-first-combat.txt` LoadCombat G b17260 binds each nonempty actor ID through FindActorRef and stores its CardInfo shared pair at ACTOR+34/+38 (lines 99–106 and 157–164). `ghidra-episode-combat-actors.txt` FindActorRef G b1c2ac loads the local STAT table and ParseActor constructs the Episode CardInfo. MakeStageInst G b23f60 copies that pair for nonempty actor IDs. Inventory.FindCard/SetRefID belongs to the empty-slot owned-party branch. Therefore adding an ordinary `/reference/GetCard` row 036 or granting an owned Bear is not required by this recovered scripted path.

MakeStageInst initially assigns generated serials as it consumes left slots. Empty slots replace their card serial with the selected owned instance ID; the loop's positional counter still advances. With the descriptor unchanged, predicted fixed left Gerard serial is **5**, right Bear **6**. These are static predictions requiring the existing guarded native material/serial observer to corroborate. Namespace1 owned IDs avoid both low generated serials; do not reintroduce legacy low aliases. Check each live map lookup resolves the same actor pointer/camp, particularly right C036/camp1.

## Exact fixed stats and skills

`EPISODE_STAT_ACTORS.json` supplies Gerard ref005/resC005/rank2: HP310, ATK210, DEF290, SPD7.00, crit11, critdamage180, block27, blockdamage52, hpregen9. This is a separate tuple from CB0102 Gerard; do not reuse that fight's stats. Bear ref036/resC036/rank3: HP1700, ATK330, DEF220, SPD5.00, crit20, critdamage200, block20, blockdamage30, hpregen0. Both cool_time5000.

Both first skills have cool_time8000/cost4. Gerard first effect base_number -2000; Bear -1600. Gerard second effect uses target_stat14/base -30/duration5000. Bear second uses target_stat4/base -25/duration5000; third uses effect_type2, target_type2, target_stat1, refer_target_type2, refer_target_stat4, base4/duration3000/interval3000. Preserve original serialized effects and rank flags. No ordinary Hunter growth or skill balance can be inferred from these fixed tuples.

## Material and win-path boundaries

Restore original C036/C036_Q/C036_EFT/C036_SND, not C036A/B aliases. Base animation event names C036_E01/E02/E03/EC and C036_SND01..04 are closed by the original EFT/SND packs. Existing C005 equivalents are still required for Gerard. Voices for Stories05/06 and victory are in VOICE_CDN1/4/7 plus already selected VOICE_CDN6, as detailed in the followthrough report.

Combat `game_res_id` is string **7**, a native environment selector, not an ordinary stage ID or a 7.jet filename. Background closure must be checked through the existing environment profile.

CB0103 victory selects **EP_0403B**; full/repeat loss selects EP_0000A/EP_0000B. Story06 entry is EP_0403A. Victory has 19 spoken lines; after spoken node13, node22 changes the image to **CUTIN_E0101** (owned by original CUT_E0101.jet), with fades but no additional spoken line. Allow that transition to finish before advancing dialogue. Terminal node20 runs `episode_clear`, fade/wait and scene-back count2.

Expected native persisted clear is **E01_S06**, not CB0103 or EP_0403B. `EPISODE_S01.json` links E01_S06 to CB0103 and declares next E01_S07 entry EP_0404A/battlefalse. The current server records bare `/episode/Read` IDs as cleared and `r_` IDs as read. Confirm native terminal request plus fresh persisted E01_S06 clear after the original victory dialogue; enemy HP0 alone does not prove settlement. E01_S07 remains a separate story to follow through.

Chapter reward is a separate request and contract. No Bear ownership, rewards, GC2 coupon grant or chapter completion should be inferred merely from CB0103 victory or E01_S06 clear.
