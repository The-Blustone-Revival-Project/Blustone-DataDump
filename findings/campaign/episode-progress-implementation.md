# Persistent regular Episode progress, 2026-10-05

Episode progress validates against the original 147-node S01 graph exported from
R_EPISODE. Source/build load the canonical recovered JSON relative to the module,
independent of process working directory. Missing catalog refuses startup;
there is no synthetic fallback or seasonal-event whitelist.

Authenticated GetLog returns stable encoded read_log[].id: r_ID for read, ID for
clear. Reward log is separate. Read acknowledges native client-reported reading
or clearing, including deferred retries, and persists once per distinct state.
It does not independently attest actual story battle victory. No resource debit,
reward, tutorial clear, automatic unlock or live account mutation was added.
Original normal S01 graph has no require fields; seasonal EV05 stays excluded.

Native Read callback parses Achieve.ParseLobbyEnter even on a refusal. Success
and Read failures therefore include neutral dailyquest_min_stage/daily_quest/
linear_quest fields. Unsupported Reward returns failure instead of mock success;
its original reward values are known but inventory/native playback remain gaps.

Full suite/build passed after authenticating the historical smoke-test GetLog
request. Focused final tests/build pass with neutral refusal fields/authfailure.
Compiled Episode test also passed, verifying source/build catalog resolution.
Coverage includes encodedread+clear reload, duplicate requests, missingauth,
unknown/doubleprefix/seasonal IDs, isolation, malformed stored state and no grants.
Replica37668 promoted healthy with live state SHA unchanged, same CDN/skill/recruit
profile. No APK rebuild/release or BlueStacks operations. Native story UI pending.

2026-10-05 follow-up: Episode Read now rolls back its new flag on a failed save,
returns neutral callback fields, and lets retry persist normally. Tests verify
separate explicit parent acknowledgments rather than inferred parent flags.
Full suite/build and review passed. Replica2484 healthy, live state hash unchanged.
Native deferred retry/playback remains unverified; no live flags were written.
