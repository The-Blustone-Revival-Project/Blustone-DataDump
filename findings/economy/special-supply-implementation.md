# Persistent Special Supply implementation, 2026-10-05

Native contract evidence: special-supply-contract.md and special-supply-display.md.
Gold-only local policy: every future newly accepted matching explicit normal-stage
first victory queues a 10-gold bonus independently of capsule capacity. The existing
battle gold remains paid immediately. This amount is a local fixture, not a
recovered original reward. No starter grants, old clear backfill, defeat awards,
Search awards or repeated-clear awards. Pending and claimed source rows persist.

RefreshSpecialList, lobby Enter and V2_GetSupplyInst expose pending special[].
Row title/npc_id/str_id/str_param are strings. Local portrait C001 uses existing
native C001_TH evidence; it is not an original NPC identity claim. expire_date=0
is proved unlimited in native PushList. Empty item/card/gem/skin rewards avoid
unreconstructed inventory settlement and the single-item type30 claim filter.

SpecialListReward authenticates owner and parses numeric IDs from the native
JSON-array string. Validate the full batch and uint32 gold capacity before
mutation. Persist gold and claim markers together. Native target_inst_id[] and
absolute user.gold prev/cur acknowledge new claims. Retries acknowledge IDs only,
without repeated reward pairs or payout. Unknown/foreign/malformed targets refuse.
No app patch or release, no native claim or host live reward issued.

Full suite/build passed; final focused tests cover two earned stages, no starters/
defeats/replays, wrapper/portrait, restart pending/claimed, malformed batches,
unknown mixed batches, foreign accounts, gold overflow and nonreward isolation.
Native Special Supply screen/ReceiveAll remain unverified until VM recovery.

Review found and fixed capsule-capacity coupling; a regression verifies full capsules
do not prevent an earned gold-only Supply. Final focused tests/build passed.
Promoted wrapper36824 with state SHA unchanged and existing CDN/skill/recruit profile.

