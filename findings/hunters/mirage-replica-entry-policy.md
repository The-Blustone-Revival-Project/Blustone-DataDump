# Mirage initial read contract and clock policy

2026-10-06. Implemented server-ts/src/mirage.ts, authenticated state route and
native local clock field; full host suite/build passed. Native entry pending.

Recovered: GetInfo's selected subtree hierarchy, native card-ID string vectors,
deck ID list, and scalar fields are documented in mirage-native-entry-contract.md.
RetryInfo compares ref_hero.end_ltime against CGMTime.GetCurLocalTime. GetExtra
was publishing server_utc only, leaving local_time zero. SetExtra independently
reads those fields and synchronizes local time from local_time; GetCurLocalTime
then advances in seconds. Publishing a Unix deadline alone would have hidden
the assertion while leaving a wrong countdown. The replica now also supplies
local_time in Unix seconds aligned with its UTC server clock.

Local policy: UTC weeks beginning Monday. The read-only period ends at the next
Monday00:00UTC, a stable boundary across retries within a week. This is not the
original timezone, rotation or restart policy. The typed initial state has no
entered hunters, deck, enemies, floors, stairs, weekly heroes or bonus. Unknown
collections are empty; no texture ID is promoted to a server entity. Scalar
zero initial fields are replica policy, not recovered original mode values.

No Mirage run is implemented. GetInfo is a read regardless of request flags;
it does not perform reset/resume/entry transactions or debit/payout. Other
Mirage endpoints refuse2001, replacing generic success. No reward/stat/hunter
grant or state reset. Empty cur has a native sentinel guard in RetryInfo's
SetThisWeekHunter, but this does not prove whole scene acceptance. Initial
state/stair UI and original resources may expose further dependencies.

Tests cover native seconds range, Monday rollover and stable deadlines,
authentication, unsupported mutation refusal and unchanged game state. All
server tests/build passed; preserved split28/1634667 manifest is byte-identical
after activation. No APK change or release owed. Installed client reload32261
is downloading its normal106MB bootstrap, not yet a Mirage acceptance result.

The user-supplied stats-lane handoff was read before continuing. Completed
STATS-ESTIMATE-2026-10-06.md exists at131881bytes. No further visual-stat hunt,
stat blending or Docker endpoint intervention was performed. Original
LEVELING_R combat settings and EXPLORE30positions remain available for later
Mirage reconstruction; they do not recover hero/stair/weekly server content.

Native acceptance now passed mirage-001: GetInfo renders theRetryInfo popup
with a coherent5Day countdown, nativeClear25/0 persists, Okay opens emptyFloor0,
and Home returnsVillage withPID32261alive. Wallets/cards/stars/claims unchanged.
This supersedes the pending-entry statements above; modeplay remains missing.
