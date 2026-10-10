# Trace recruitment service, 2026-10-05

Implemented /shop/PieceExchange as an authenticated account transaction, replacing
the empty generic shop fixture. Native source contract is in
trace-recruitment-contract.md. Request cnt means hunters, item_inst_id identifies
the owned trace stack. Thresholds10 Sylvester/20 Gerard and stats remain LOCAL.

Success returns complete owned card ARRAY and truthful consumed_inst_list
inst_id/qty delta. Updates trace quantity, fresh hunter IDs, persistent ownership
and cardbook together. No gacha marker/reward guesses: native confirmation builds
its own result marker. Existing hunters/decks/wallets/progress/tutorials stay intact.
Checks reject malformed count, wrong/nontrace/locked item, insufficient quantity,
unpublished birth rank/stat support, capacity100, unsafe allocator/reserved helper
ID overlap and active combat before mutation. No request nonce exists; funded
repeats are additional purchases, not exactly-once replay. After lost responses,
reconcile inventory before retry. Consumes only the requested stack, never silently
unrelated duplicate trace stacks.

Fresh native decomp G844918 CSRAchieve::ParseLobbyEnter and relocated keys prove
dailyquest_min_stage is an unguarded string; nonempty value changes its gate,
empty leaves it intact. daily_quest and linear_quest are iteration inputs.
Receipt includes empty string and empty arrays, omits achievement, so no quest
updates are fabricated. Curated proof: ghidra-trace-lobby-achieve*.txt.

Full npm test and build passed. New isolated test earns20 actual service traces
through campaign victories and capsule-funded Search, advances test clock only,
exchangescnt2 for20 traces/two unique006 hunters, checks restart/cardbook/oldparty
and wallet preservation. Tests cover owner isolation, quantity/identity/lock,
capacity/overflow/reserved IDs and active-combat refusal. Synthetic capacity data
is confined to a disposable account. Focused test/build passed after combat guard.

Promoted server with unchanged persisted state SHA, same resource1634663,
46folded assets/11packages, livePID16687 safe village. Live traceqty2 remains
below configured10; no successful native exchange or manual grant was attempted.
Success cinematic/result and plural presentation remain pending. No client
patch/rebuild/install/clear, new instrumented release or private data check-in.
