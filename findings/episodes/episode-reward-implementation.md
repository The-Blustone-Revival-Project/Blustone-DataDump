# Original Episode reward settlement, 2026-10-05

Supported first chapter reward: E05's original shipped item AIRSHIP_TICKET qty20.
Capsule reference already published; no invented reward amount/material effects.
Other chapter rewards refuse until item definitions are recovered. GC2 identified
as Lottery coupon; full GetItem definition remains unknown. FMD1's display use
must not silently convert the original Episode item reward into currency.

Local conservative eligibility requires every E05 descendant story bare-ID clear
in the owner's durable logs (eight stories). Prefixed read, parent-only and partial
clear cannot grant. Native client checks parent clear; its aggregation is not yet
fully traced. This gate is local policy, not an original-server rule claim.
Client reports clears; actual story battles remain unverified. No live clears or
rewards have been inserted. Test accounts are disposable.

CSRMEpisode.ParseReward uses SyncItem, whose native rows are inst_id/ref_id/added;
added is an increment. Null user skips zero currency rewards. Validate all source/
item/capacity constraints before mutation; persist stack increase+reward_log marker
atomically. Fresh receipt contains20added; duplicate claim afterrestart returns
item[] empty, user:null and neutral quests, never replays the additive receipt.
This avoids duplicate grants but a lost first response can require native inventory
reload to reconcile the already-persisted stack; protocol has no claim nonce or
absolute-item receipt. Full lost-response client reconciliation is unverified.

Full suite/build and compiled reward test pass: original amount, read-vs-clear,
parent/partial refusal, all-story gate, uint32 quantity capacity, other materials,
no unrelated state mutations, native DTO, duplicate/restart marker and isolation.
Native reward popup/story playback remain pending BlueStacks recovery approval.

Review follow-up: fixed new item-ID collision checks, rollback stack/counter/claim
marker on persist failure, and neutral callback fields for every NativeAuthError.
Final focused regressions cover new/existing-stack save refusal and mismatched
credential/pvid; passed with build. Full suite had passed before these focused
repairs. Replica20456 healthy, same profile, live state hash unchanged.
