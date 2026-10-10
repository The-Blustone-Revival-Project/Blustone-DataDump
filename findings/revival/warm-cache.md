# Warm Search: helper serial collision versus wave-cache resend

2026-10-05. Read-only current source, parent Begin/MakeStageInst decomp and original helper branch Thumb. No device/Ghidra/server writes, fake End or refund. Parent reports funded log2 accepted with warm wave_info0, helper serial18 and HUD1/2 but no enemy/HP loss; cold first Search had helper0 and real monsters.

## Concrete helper-ID collision

The allocator in **CSRFindShard::MakeStageInst G90610c** initializes local_134/local_130 from **maximum OWNED inventory serial only** (GetCardInstIDList, battle-end decomp207..285). Nonowned virtual helpers are not part of that maximum.

Helper handling then separates zero and nonzero card serials:

- The zero-ID virtual path resolves vfid in the reference virtual-friend map. It takes the **GLOBAL template CSRCard pointer at mapnode+38**, rather than assigning a fresh independent card first (decomp604). It increments the owned-based allocator and **writes its new serial into that template CSRCard+10/+14** (637..640). Thus a template starting0 can become18 after the first battle.
- The existing nonzero helper path at **90674e** loads helper+10/+14, tests nonzero, constructs ACTOR_INFO and **copies the selected helper via CSRCard::operator= at906766**. It does not advance/max-adjust the allocator for that retained helper serial (decomp714 onward).
- Each monster subsequently **increments the same owned-based allocator**, then writes the generated serial into its fresh card (decomp1042..1045), with no separate helper-ID exclusion.

For owned maximum17: first cold helper0 becomes18 and advances the allocator, so enemies receive19/20. On warm reuse the global template already18; Arrange copies it into the selected helper, the nonzero path leaves allocator17, and first enemy becomes18 as well. This is an **exact native construction collision**, not an inferred enum or pointer offset. The observed native friend_leader_id18 and enemy HP1010 matching Lantern's HP instead of M001100 strongly corroborate it, though no bounded live actor-map collision snapshot was captured in this lane.

A narrowly marked server reference fixture can publish the nonowned helper with a positive reserved serial outside owned/generated enemy ranges, then verify the ordinary warm helper packet and native second battle. It remains a reference template, not an owned hunter grant. Validate the reservation against owned IDs plus the generated enemy range; simply checking that the serial is not currently owned is insufficient. Original virtual-helper identity/serial policy is unknown. No client allocator patch is proposed here.

The current paid attempt/capsule debit must remain intact; this report does not authorize an outcome, refund or second charge. A preserved cold reload of an appropriately reconstructed helper reference is a separate native control owned by the parent/tester.

## ParseBegin wave cache is insert-only

**RequestBegin** posts wave_info1 only when its target-stage WAVE map lacks a key; existing key produces0. **ParseBegin915d6c** accepts absent/null or empty wave_info and jumps directly to achievement/consumption (915f2c branch, decomp1367..1372), leaving the existing wave map unchanged.

A nonempty wave_info builds temporary WAVE objects/vector, then uses **__emplace_unique_key_args** into stage map+18 (decomp1868..1869). For an already present stage key it retains the existing entry; it is **not a replacing assignment** and does not erase the old vector. Temporary new vector/shared objects are released afterward. Thus repeatedly sending the same two-row definition does not prove that the native cache was cleared or enemies removed. Native old data would win even if the server attempted to change multipliers/skills during the process lifetime.

Protocol-coherent response behavior is to provide the complete cache definition on flag1 and omit it (or null/empty) on flag0. That change avoids redundant insert-only work, but **by itself is not a proved fix for the warm missing-enemy failure**. The serial collision has an independent exact path matching the observed helper ID/HP.

## Monster-link reuse is separate

MakeStageInst reads CSRGameMob.GetStageMonsterLinkData for the stage and the corresponding cached Search WAVE by vector index. Its monster cards are freshly created per actor. Search WAVE metadata and stageMonsterlink data are different tables; wave_info0 refers to the former cache only. Do not infer that flag0 says no monster rows should be sent or that End/reward has consumed the reference table.

If a warm control with a reserved helper serial still lacks enemies, next precise targets are **CSRGameMob.AddStageMonster Ga0d194/GetStageMonsterLinkData Ga0cf38**, and the native actor serial-map insertion/duplicate handling. Reuse existing curated AddStageMonster decomp before changing field aliases. A guest PC or bounded IDs/HP/actor-group snapshot can discriminate those remaining paths without forcing an End.

Sources: ghidra-find-shard-battle-end.txt MakeStageInst, ghidra-find-shard-begin.txt ParseBegin/RequestBegin, current search-battle.ts/search-stage.ts; original90674e..90676a. No tests or runtime operations by this lane.
