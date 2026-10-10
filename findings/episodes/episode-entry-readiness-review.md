# Episode first-story readiness review

2026-10-05. Bounded source/retained native evidence review only; no Ghidra,
device, account, source mutation, tests or runtime acceptance claim.

## Protocol assessment

No concrete first-story response-schema defect was found in current
`server-ts/src/episode-progress.ts` and `state.ts:episodeAction`.
The real boot requester is /episode/GetLog, not a recovered GetEpisode content
route. CSRInstanceSync.ReqEpisodeCB Gae62e0 checks result1, then passes ret_data
to CSRMEpisode.ParseLog Gb19268 (`native-episode-log.txt`). Current GetLog returns
read_log/reward_log collections of objects with string id. Read IDs use r_ and
clear IDs are bare, matching InsertReadOrClearID Gb1954c. No inferred parent
clear flags are inserted.

Current /episode/Read returns dailyquest_min_stage:"", daily_quest:[],
linear_quest:[] on success and refusal, including native-auth refusal. That
matches callback Gb20000, which inserts its captured encoded request ID or
queues deferred retry, then always invokes Achieve.ParseLobbyEnter. The source
rolls back a newly appended progress ID if persistence throws. No currency,
item, AP or tutorial debit/grant is fabricated for ordinary S01 acknowledgments.

E01's original GC2 quantity3 reward remains unsupported and is refused. This is
a real later chapter-completeness limit, not evidence that E01_S01 entry needs
that reward/reference now. E05-only supported settlement must not be advertised
as complete Episode reward support.

## Entry and material boundary

The current ordinary Mission choice has a recovered native gate: TALK entry4
from predecessor2 requires GetStageAchieveCnt(TU35), which maps to n_02_03.
Cruise success proves common dialogue choice processing can work; it does not
prove the blocked Mission callback ran. Normal earned stage progression is the
appropriate next control; no server scene alias/unlock is justified.

First story E01_S01 loads local EP_0301A; its real actors are Char009, NPC001 Lana
and Char004 Tyltyl. Original DIAL-EN, N001_BG, BGM_LANA, AMB_PLT and voice records
are located and selected by the 13-pack Episode profile. Catalog loading uses
local SEASON_LIST/SEASON1 with proved native case normalization. Generated
C003_DIALOG registration and complete runtime actor/layout rendering remain
unverified; outer-record absence does not prove a missing alias. No new content
endpoint or alias should be implemented from that absence.

For the subsequent CB0101 fight, fixed actors bind through Episode STAT, not a
required owned009 grant. ENV99 selects STI099, and original LEVELING_E is
present. Existing first-combat report records these dependencies and their
remaining native acceptance limit.

## Bounded next step

No additional server implementation is justified by this review. After earning
the existing n_02_03 prerequisite, use ordinary Mission entry and first-story
selection. Capture the first native load failure or actual Read packet if one
occurs; distinguish GetLog success, story rendering, encoded Read acknowledgment
and reload persistence. That single control can identify a concrete missing
resource/parser seam without speculative aliases or original balance changes.

Evidence: episode-progression-contract.md, episode-native-resource-loading.md,
episode-first-story-assets.md, episode-first-combat-contract.md,
episode-live-dispatch-boundary.md and episode-choice-node-fields.md.
