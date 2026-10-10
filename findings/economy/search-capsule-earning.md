# Earned Search capsules — 2026-10-05

Native Search reads inventory quantity under the exact AIRSHIP_TICKET literal
(Ge23f36/Ge23f38). Its preserved tutorial now visibly says capsules come from
clearing general stages (revival-010/66). Original drop amounts/rates remain
missing; the local rule is one capsule per new accepted normal campaign victory,
including a new replay attempt. No retroactive award, initial grant or mail grant.

The item definition retains this recovered ID. Name/rank/use_type0/inert effect
and empty thumbnail are local reference metadata, not recovered ITEM_REF data.
Direct Search quantity lookup uses the ID, not the guessed use_type. Unknown
original capsule metadata remains documented in search-capsule-content.md.

completeMission requires a matching live battle, explicit play_info.clear1 and a
published normal n_* stage before awarding. Legacy absent/unreadable play_info
win defaults cannot grant capsules. Losses, duplicate/standalone completion,
wrong-stage/battle requests grant none. Existing unlocked capsule stack keeps
its instance ID and increments by1; new stack uses the normal item allocator.
Native unsigned32 quantity overflow refuses the capsule addition. State and
receipt are persisted together through the existing mission settlement.

Receipt item[] has {inst_id,ref_id,added:1}. Original native AddItem symbol
CSRInventory::AddItem(unsigned long long,string const&,unsigned int) and helper
Gaec508 prove existing quantity increments by the final argument; added is a
delta, not the total. UseItem Gaea5f8 consumes inst_id/qty instead, so Search
consumption must not copy the award DTO. Evidence decomp retained separately.

Full npm test/build pass. Dedicated tests cover initial absence, malformed win
flags, standalone completion, loss, stage mismatch, one award, duplicate receipt,
new replay award with stable stack/delta, persistence, account isolation and
overflow. Chest test now checks its own item identity, retaining duplicate-claim
protection independently of campaign drops.

Promotion stopped verified replica listener25260, started wrapper20716 with
unchanged1634663/46asset/11package profile. State SHA unchanged across promotion;
native PID919 remains alive. Current native capsule reference cache predates the
new definition; preserve a normal ref refresh before the first item-drop trial.
Live account still has no earned capsules and received no fixture test grants.
Native capsule earning/display/reload validation remains pending.

Additional native progress: the original guided Search button at count0 enters
the Lapis intro story (69/70/71) before any Begin/consumption. Skip transitions to
Prepare for Battle (72), fetches actual targetstage n_01_07/M001 and shows the
real four owned CASE1 party and Select Partner. Same919, no Begin/End, paid
action, reward or battle. Do not infer ordinary Search is free from this original
tutorial path. Capsule earning policy and separate Search lifecycle remain distinct.

## Partner screen: next pre-request blocker

Free Select Partner opens73 and emits abyss/GetHelperList plus guild/GetDetailInfo.
The helper list is visibly empty, with original guide finger at the upper-left.
Widened opt-in game-value logging to Search owner/helper/wave/log IDs, leaving
credentials excluded. Preserved replica promotion wrapper33972 keeps state SHA
unchanged. A single native Begin Battle tap74 closes PID919 before ANY HTTP
request reaches this new server. No Search log/cost/attempt was created.
Private bounded crash log retained under recovered-assets/emulator-2026-10-05-
search-partner-failure/logcat.txt; SIGSEGV Thread9 fault0x1 at01:53:36.627+03.
No guest ARM PC was captured. Empty helper/tutorial target is a concrete next
dependency to trace, not an established fault instruction. App is now dead;
do not describe it as safely held at prep or a successful Search battle.
