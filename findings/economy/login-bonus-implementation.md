# Daily Sign In login-bonus reconstruction, 2026-10-05

## Attribution correction

Daily Sign In Supply28D is NOT the legacy /supply/AttendReward seam. Native
OnButtonClick Gd68bd4 obtains GetCurLoginBonusInfo, chooses current count or
claimed-vector length, subtracts1 and indexes GetAttendSupply's cached vector.
Zero count/empty vector underflows before HTTP; a server error receipt cannot
repair that crash. Cached vector is built by ParseLoginBonusRef Gf4ae7c.
RequestLoginReward Gf49410 posts /supply/LoginBonusReward with target_cnt.

Reference ret_data.login_bonus is an ARRAY of target_cnt/gold/free_iap and
item_list/card_list JSON STRING arrays, whose rows use ref_id/qty. Instance
ret_data.login_bonus has cur_value,cycle,cycle_log. Callback Gf4e43c passes
ret_data to ParseLoginBonusReward and ParseLobbyEnter. Reward is nested under
ret_data.reward: gold resides in reward.user.gold.cur, not root user/gold.
Parallel ret_data.inst updates calendar through ParseLoginBonusInst. Root
dailyquest_min_stage empty string and daily_quest/linear_quest empty arrays
satisfy the unguarded transitive achievement string without new quest data.
Fresh curated proof: ghidra-login-bonus-{contract,keys,callback,callback-keys}.
Legacy AttendReward receipt and bootstrap are retained separately; earlier
attendance-contract-next.md attribution was corrected by the research agent.

## Local service and limits

Publishes28 positive ordered entries,100gold each, no items/hunters. Original
reward amounts, cadence, timezone, cycle reset/catch-up remain UNKNOWN.
Authenticated V2_GetSupplyInst observes one visit per new UTC day; missed days
do not invent visits, rollback cannot reopen days. Offers cap at28; this is a
bounded one-time LOCAL calendar with cycle1, not an original monthly reset.
Reads offer but never grant gold. Claims accept only the positive CURRENT
offered day, require unclaimed status and safe balance capacity. Gold and claim
journal persist together; duplicates/refusals never grant twice. Initial legacy
journal migrates to unvisited, without retroactive rewards. Existing fuel Supply
and all owned/progression/tutorial data are preserved.

Full npm test/build passed. New tests cover ordered refs and JSON strings,
offer versus actual reward, receipt parents, day/count/auth checks, duplicate,
restart, rollback, missed days, cap, overflow and owner/state isolation.

## Native validation status

Promoted wrapper27280 with unchanged file SHA before client reload, same
1634663/46assets/11packages. Existing instrumented+8 normally relaunched to load
new references, accepted one54MB prompt167; no install/clear/client patch.
PID20690 fetched references and authenticated Supply instances, completed normal
download and reached village170. Visit journal eligible1/unclaimed persisted;
gold remains10660. Audit of owned hunters/items/party/tutorial/stars unchanged.
No reward was automatically paid and no /LoginBonusReward request was issued.

Native pending Search guide currently blocks calendar access: village170 then
free indicated aircraft input advances to Search building focus171. App held
safe village GUIDE, not a free village and not active combat. Thus new calendar
render/positive-day OK/claim/reward/reload remain UNVERIFIED, despite native
bootstrap parser acceptance. No new instrumented release owed.

Parallel search-guide-completion.md proves37/1 ACK belongs to guided recruitment
after BT_RECRUIT's trace threshold gate, not battle End. Two actual traces vs
the local10 threshold explains pending guide; do not manually clear flags or
grant tutorial hunters. Its optional tutorial-clear reward marker is a further
seam to reconstruct before claiming guided recruitment completion.
