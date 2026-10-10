# Earned Team EXP is not republished on reload

2026-10-04. Read-only source and curated native dumps/literals/symbols. No source/adb/Ghidra/runtime changes by this agent. Parent reports persisted earned game.exp270 from actual mission completions; this task did not read private state or execute another completion. **The reload publication bug is now fixed in source and the exact parser/getter gap is closed below. Native relaunch validation remains separate.**

## Confirmed source/wire mismatch

`completeMission` updates/persists **game.exp** and returns **ret_data.user.exp{prev,cur}**. Existing native Mission callback `native-mission-complete.txt:1480` writes exp.cur into **CSRPlayData+0x14c**. Thus this is genuine native Team/user progression, separate from per-hunter EXP.

At the initial audit, reload producers published **zero**:

- `ownedPartyProfile` starts from bootstrap.partyProfile, where **group_exp:0**, and overlays cards/Arena fields without replacing group_exp.
- `lobbyEnter.ret_data.user.group_exp` is explicitly0 in state.ts.
- Profile snapshots/relation views using ownedPartyProfile therefore also return zero despite game.exp270.

This was a **confirmed publication mismatch**, not proof the persisted backend EXP was lost. Don't credit another270 or migrate/wipe it; republish the existing value. Current ownedPartyProfile.group_exp and lobbyEnter.user.group_exp both derive **game.exp**, read-only confirmed after the parent fix.

## Native reload field evidence — exact key-to-offset proof closed

**CSRSyncGlobal::ParseUserDatailInfo0xf6e240** consumes full envelope.ret_data, then the literal **group_exp** at LDR0xf6e3ba/slot0xf6e574/addPC0xf6e3bc, address0x1d776b4 (`ghidra-userdetail.txt`). `native-pucinven.txt` parses that field as numeric cumulative EXP into its target-user/profile data, not hunter exp_leader. It also reads vip_exp separately; do not conflate VIP progress.

**CSRPlayData::ParseUserInfo0xb65850** consumes full envelope.ret_data.user and unconditionally writes its numeric **group_exp** into **PlayData+0x14c**. Fresh authoritative evidence is `ghidra-user-exp-persistence-strings.txt` and `ghidra-user-exp-lobby-instructions.txt`: ret_data LDR0xb6586e/ADD0xb65874; user LDR0xb65a8a/ADD0xb65a8e; group_exp **LDR0xb65e3e from slot0xb65ef8, matched r1 ADD0xb65e46** resolves0x1d776b4. Numeric conversion follows lookup0xb65e48; **STR0xb65e90 stores to [r10,+0x14c]**. This is the exact same counter overwritten by Mission.user.exp.cur.

The earlier decompiled PC sum was useful for locating the field, but fresh matched registers/instructions are authoritative. No remaining literal inference is needed for the reload reset.

The applied narrow correction is **ownedPartyProfile.group_exp=game.exp** and **lobbyEnter.user.group_exp=game.exp**, leaving mission exp pairs unchanged. Don't replace it with arbitrary scalar level, card EXP, stage reward group_exp, or VIP EXP. No source edit is made by this research agent.

## Published Team level curve and gates

Current `/reference/GetLevel` **user** array is only `[{min_exp:0},{min_exp:100}]`. Existing SetLevel0x109f114 decompile stores a vector of those numeric thresholds at UserLV+0x54/+0x58, distinct from rank-keyed card curves. It is a **local fixture**, not the original Team leveling table.

Retained native functions and follow-up proof:

- **CSRPlayData::GetUserLevel0xb6cbf0** — pin EXP read+0x14c and delegation.
- **CSRUserLV::GetUserLevel0x10a0916**.
- **GetUserMaxLevel0x10a0940**, **GetUserMaxExp0x10a094a**, **GetUserMinExp0x10a0972**.

Fresh `ghidra-user-exp-getters.txt` closes the main getter proof: **PlayData.GetUserLevel0xb6cbf0 reads this+0x14c and delegates to UserLV.GetUserLevel0x10a0916**. The latter scans the published threshold vector in order while threshold<=EXP, returns the number consumed, with minimum1 (including empty vector). Thus current rows0/100 yield **level1 for EXP0..99 and level2 for EXP>=100, capped2**, including earned270. It never derives level30 from the equal mission receipt fixture. Min/max EXP range getters remain separate functions if needed for progress-bar/receipt modeling, but the current computed level/cap is now proved.

**Gates do use the native computed Team level.** Existing `native-area-ui.txt:570` obtains GetUserLevel and compares it with **AREA_INFO+0x40 level_limit** before opening an area; the same mechanism appears at641/726 and the area-lock path around964. `native-setstage.txt:3995` also uses GetUserLevel. A response's invented level number does not replace these getters or unlock original level-gated areas.

At the initial audit, `FIXTURE_USER_LEVEL` in state.ts was **30**, returned as equal previous/current pairs by mission completion and unrelated to game.exp/current two-row curve. Follow-up `mission-team-level-receipt.md` proved the actual parser parent **user.exp.level** (old root/user aliases were ignored). Current source now derives nested level pairs with `team-level.ts` and uses the same getter for area gates; max_ap stays unchanged. This activates the real0x02 notice on a threshold crossing, so native level-up popup/resources still require a bounded control. The two-row leveling capacity remains a separate fixture completeness limit.

## Acceptance checks

After the narrow publication fix, compare persisted game.exp270 with scalar flat/profile group_exp270 and lobby user.group_exp270; mission Complete still returns absolute exp pairs and hunter maps independently. Perform a preserved relaunch and confirm native Team EXP/derived level does not reset. At a real threshold crossing, verify computed level, level-up receipt/UI and area gate agree with the **published local curve**; retain labels that original thresholds/rewards are missing. No extra reward, credential rotation, reinstall, app clear or client patch is needed to test the scalar correction.

Parent added `tests/team-exp.ts`: four normal isolated mission Start/Complete calls earn120, cross level1→2 with correct nested receipt, then profile/lobby/restart values agree; another account remains isolated and no extra XP is awarded on reload. Read-only source/test review confirms those checks exist; parent reports full suite/build passed, this agent did not execute them. The two-level fixture curve remains a completeness limit; level-gated areas above2 cannot be unlocked by this curve merely by accumulating more EXP. Hardcoded mission receipt30 is no longer the source behavior.
