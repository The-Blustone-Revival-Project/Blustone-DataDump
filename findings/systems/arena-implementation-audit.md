# Arena source audit before native control

2026-10-04. Read-only current `arena.ts`, `arena-service.ts`, state/routes and arena tests against curated native contracts. No source edits, runtime requests, adb/Ghidra or test execution by this agent. Parent reports full suite passed; daemon14416 still serves the old module, so no native Arena outcome is inferred from these source checks.

## Concrete findings

**1. Persisted arena progress conflicts with lobby/profile snapshots.** Arena.Enter returns `game.arena` counters, but `ownedPartyProfile` still starts from bootstrap league_level1/rating_point0 and never overlays Arena state. `lobbyEnter` also publishes a root battle object with hardcoded league1/rating0/rank0/league_win0. Example: after one accepted win, Arena.Enter publishes rating110/win1, while subsequent lobby/profile fields still publish rating0/league1. Native user-detail reads those fields, so the restart/bootstrap data sources disagree even though Arena persistence itself works. Overlay the recovered league/rating/message values in the authoritative profile and supported lobby battle fields; preserve card and mission fields. Add a restart/profile coherence check, not just an Arena.Enter counter assertion.

**2. Case4 can change during an active attempt.** `state.setDeck` does not guard Arena-active case4 edits. Start snapshots member IDs in `game.arena.active.deck_inst_ids`; Complete constructs card EXP map from that snapshot. Native ParseBattleResult instead iterates **current case4**. A valid setDeck(type4) between Start and Complete therefore creates two different rosters; the callback can skip receipt entries for old members and current formation no longer describes the battle that finished. Refuse case4 changes while the attempt is active, or provide a separately recovered synchronization rule; don't silently rewrite the active snapshot to the new roster. Current no-XP reward policy limits immediate ownership effects but does not remove the contract mismatch.

**3. Retry after a lost first Complete response loses the original receipt.** First Complete commits counters/honor and clears active. A native retry while none is active succeeds with new prev==cur pairs and empty card map instead of the original receipt. Backend doesn't pay twice, which is good; however the client's first received result in that network-loss scenario shows zero rating/honor delta even though the server paid. ReqBattleCompleteCB's retries are recovered, so this is a meaningful transaction/UX case, not a hypothetical invented nonce. Persist/replay the most recent matching accepted receipt while no attempt is active; keep the documented later-same-target ambiguity separate. Test simulated lost response/restart by calling identical Complete twice and comparing receipts as well as unchanged state.

These are bounded coherence/retry findings; no mandatory Start/Complete parser crash was found in the current known envelope fields.

## Shapes and isolation that match

Start has full known-card rival, flat user.ap/ap_charge_time/bp/bp_charge_time and root refresh_price. Newly recovered ParseRefreshCost confirms that root cost object plus optional wallet branches; current BP-only response can omit them. Complete supplies mandatory battle pairs, outside-battle user.honor pair and top card map keyed to case4 snapshot, with no invented resource resync. Unknown achievement and rewards are omitted. Reference GetBattle publishes six league rows/weekly array, complete strict-string rival fields and deck inst_N objects; no rival grant enters owned inventory.

BP1, rating±10/honor10, six wins per league, season/rival data and no hunter XP are explicit local policies. Start replay costs once; mission Start is refused while Arena active; training source guards include active Arena members; campaign progress/AP are not paid/cleared by Arena settlement. Mutation-specific validation precedes paid counter changes, with one persistence operation at each Start/Complete acceptance. Legacy state missing arena normalizes an empty Arena without resetting existing honor/owned cards.

## Unproven native outcome rule

Current Complete refuses `is_win1` whenever enemy_total_hp is nonzero. The eight parser/request dumps do not prove that all Fight Club victories require annihilation; timed-win behavior needs **CSRFC.OnFinish0x947ad4** and its deciding caller. Do not call this a proved native incompatibility yet, but don't describe it as recovered validation either. If the client reports a legitimate timeout victory with remaining enemyHP, this rule would reject/retry its completion. Current tests mirror the rule and cannot establish native semantics.

Empty rival card slots, thumbnail/country fallback, season datetime units, tutorial/input gates, BP overflow display, refresh operation and result screen behavior remain native controls. `/arena/RefreshRival` is forwarded to the Arena service but returns unsupported operation; published cost100 does not establish implemented refresh purchasing. Preserve these limitations in claims.

Parent should decide/fix the three concrete coherence findings before promoting a complete native-loop claim, then run the one bounded real Start/fight/Complete control. This audit does not alter source or consume live BP.

## Resolution review — source only, not deployed

Read-only follow-up confirms all three findings were addressed in the current source:

- ownedPartyProfile overlays persisted league_level/rating_point; lobby battle fields derive Arena counters. Empty Arena rating0 preserves the legacy profile default rather than introducing an unrelated bootstrap rating change.
- setDeck refuses changing case4 during an active attempt, while allowing an identical formation replay. Existing snapshot/source protection remains intact.
- Arena.last_result persists a normalized metric signature and validated original receipt. Matching Complete while no attempt is active returns that receipt unchanged, including original deltas/card entries, across restart. A newly active attempt still settles separately; the documented stale same-target completion ambiguity is not claimed solved by a nonexistent nonce.

The unproved enemyHP0-only win rule was removed; valid native is_win plus bounded numeric metrics is accepted without a reconstructed anti-cheat claim. Rival selects002 only when published, otherwise001, avoiding a missing reference under smaller fixture rosters; runtime legality/rendering of either fixture remains a native control.

Current tests include flat/lobby coherence, active deck edit refusal and identical receipt replay/restart. Parent reports focused tests/build passed; this agent did not execute them. **No new concrete source regression found in this follow-up.** Native Fight Club battle rendering/settlement, season timing and unsupported refresh/friendship/revenge remain the previously recorded validation/fidelity limits. No deployment or live BP consumption occurred in this review.
