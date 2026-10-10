# Fight Club: next free native entry check

Current continuation2026-10-10: this historical missing-GetMyRank diagnosis is
superseded by arena-my-rank-contract.md and the deployed handler. Native free
lobby entry/GetMyRank/countdown/return verified in testing/arena-entry-001/report.md.
FindRival, combat, rewards and other tabs are not covered by that validation.

2026-10-04. Read-only current source, curated arena contracts, retained symbols and original Thumb disassembly. No server writes, device/Ghidra activity, patch or native test by this lane.

## Concrete entry gap

The initial Fight Club popup is **CSRPopUpFC**, distinct from the ranking table CSRTableFC. CSRPopUpFC::OnReset G0xc0afc6 unconditionally calls RenewalCurrency at c0afcc, **RenewalMyInfo at c0afd2**, RenewalShopItemNoti at c0afd8, SetCurLeagueInfo at c0afde, SetLeagueProgress at c0afe4, then Reward at c0afee.

RenewalMyInfo G0xc0b380 checks its weak owner and invokes **CSRSyncFC::RequestMyRank G0xf5fb30 at c0b4ba**. The native URL vocabulary includes **/arena/GetMyRank** at ELF string address 0x1d8f920. The dedicated route list in server-ts/src/game-routes.ts currently contains Enter, FindRival, BattleStart, BattleComplete and RefreshRival, but not GetMyRank. Thus a normal popup reset can reach an unreconstructed operation before the player starts a fight. This is a concrete missing entry seam; an actual callback crash or malformed display has not been observed.

The narrow parent dump targets are **RequestMyRank G0xf5fb30** and **ReqMyRankCB G0xf600d8**. Offline callback disassembly shows JSON indexing at f60144/f601a2/f601aa and numeric conversion, then a store into CSRFCPlayData; it does not call a separate named ranking parser. Resolve those actual index keys and their parents instead of borrowing WorldRank or ParseDefender schemas. Rank/profile DTO aliases are not established fixes.

## Existing recovered fields

Current arena-service.ts Enter publishes arena.status1 and season, user.battle and is_weekly_reward0, plus the optional root deck array. arenaProfile supplies all recovered numeric fields and strict message strings. FindRival supplies arena.rival_list[] and root refresh_price. arenaRival supplies strict nickname/thumbnail/profile_status/country_code strings, status/user_exp/vip_exp, empty chain_bonus/gem arrays, numeric card_book, battle profile and exactly five inst_N keys; its nonempty card uses cardInstance and a published 001/002 reference. GetBattle supplies all six league rows and weekly_reward rows with empty item lists. No concrete missing field from those recovered parsers was found in current source.

This does not certify resource rendering, thumbnail interpretation, empty rival slots, tutorial eligibility or rewards UI. Empty array/gem omissions avoid unsupported transitive parsers; they do not establish complete Fight Club functionality. GetMyRank is the additional entry operation now identified.

## Bounded next action

After the tester finishes the existing Gym task, enter the visible Fight Club entrance once from the healthy Village using its normal UI, stop at the initial lobby, and capture a screenshot plus the fresh ordered route trace. Confirm Enter status1 and whether the popup automatically requests GetMyRank. Do not press Fight/BattleStart, paid refresh, reward claim or ranking tabs during this free inspection. Enter may initialize persisted case4 from mission case1 under the current server policy; it should not debit BP, alter mission AP, consume hunters or award honor.

If entry fails, retain the first native assertion/PC and exact last route. Missing GetMyRank response evidence should be recovered before expanding unrelated arena endpoints. Useful precise UI symbols if a later parent dump is needed: CSRPopUpFC::OnInit Gc0adcc, RenewalMyInfo Gc0b380, SetCurLeagueInfo Gc0beec, SetLeagueProgress Gc0c220, Reward Gc0c404, RemainTimeTextRenewal Gc0c5cc. CSRTableFC ranking OnInit Gff2074 is a separate lane.

Sources: analysis/native-evidence.tsv; analysis/native-all-strings.tsv; arena-lobby-contract.md; arena-battle-contract.md; server-ts/src/arena.ts, arena-service.ts, game-routes.ts and bootstrap.ts. G addresses are ELF code VA +0x10000.
