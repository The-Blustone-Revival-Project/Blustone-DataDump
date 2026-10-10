# Local Search Retry/Reset implementation, 2026-10-05

Native GetPlayCnt(ref) G90bc18 returns matching completed play rows MINUS
matching retry_log strings. Original Thumb SUB G90be00 confirms the decompiler's
missing integer return. Popup normal type2 uses max_play_cnt minus that result,
and max_retry_cnt plus VIP minus purchased retries. Targeted Retry therefore
retains completed plays and appends a retry credit. Sources: freshly curated
ghidra-search-repeat-counts.txt, ghidra-search-repeat-ui.txt and agent report
search-repeat-eligibility.md. Reset's original server log policy remains unknown.

Replica publishes local flat fees Retry10/Reset30 Manda, type1, free-first.
These are NEW LOCAL fixtures, not recovered price tiers. Request quotes are
validated exactly. Paid responses use recovered SyncUser iap/free_iap prev/cur
pairs and direct ParseInst parent. No capsule, trace, hunter, helper availability,
campaign star or tutorial flag is granted by either operation.

Persisted Search.repeat holds current period start, completed play vector,
retry strings, reset counter and last operation/completed-log acknowledgement.
Legacy states migrate existing last completed log and timestamp without changing
costs/reward/active log. Reads filter expired vectors, no write. Begin starts a
fresh local one-hour period when expired; End appends exactly one completed log.
The native cooltime is absolute server seconds, not a duration or milliseconds.

Retry buys one credit only when exhausted and local max_retry1 remains. Global
Reset clears current play/retry vectors, starts a new LOCAL hour and increments
reset count, preserving last End receipt and monotone battle IDs. Active combat,
insufficient funds, bad identity/quote and capacity refuse before mutation.
Same operation for same last completed log acknowledges without repeated debit
and emits user:null. This is a bounded local replay policy, not a recovered nonce
or promise of arbitrary concurrent exactly-once transport.

Full npm test/build pass. Isolated account EARNS three capsules through campaign,
wins initial Search, buys Retry, wins again, buys Reset and wins a third time.
Checks count arithmetic, actual10/30 debit, mixed free/paid wallet pairs,
restart/replay, stale quotes, insufficient funds, active-combat refusal,
old-End dedup after reset and inventory/party/progression preservation. No live
inventory, clock, wallet or tutorial writes were used for this proof.

Promoted wrapper33672 with unchanged state-file SHA and resource profile
1634663/46assets/11packages. Native PID16687 re-entered normal Search and parsed
fresh /explore/GetInst HTTP200 at02:07:30.656Z, screen163. No Retry/Reset paid
button was invoked. Tutorial37/1 still repeats; normal Android Back did not
leave its modal. Following indicated Hunter List advanced original dialogue to
"Let's go a bit closer" (165), without a battle or request mutation. Safe held
guide, not village. Native paid receipt/UI and subsequent earning remain pending.
No client patch/rebuild/install/clear or new instrumented release owed.
