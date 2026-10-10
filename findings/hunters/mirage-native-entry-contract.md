# Mirage GetInfo entry and retry-time failure boundary

2026-10-06. Read-only existing ghidra-mirage-decomp-08/10, strings07..14,
mirage-getinfo-keys.tsv and bounded original Thumb inspection. No native actions,
Ghidra, source/account edits or fixture implementation.

RequestInfo **G92b30c** posts /mirage/GetInfo using auth and reset/stay/entry,
inst_base/inst_enemy/ref_stair_list/ref_hero request flags (strings07).
Their historical interpretation as game data objects in mirage-getinfo.md is
not a substitute for actual request builder arguments. New ordinary NPC0023
entry proves this mode can be requested after boot; the old 'boot only' scope
must not be treated as an invariant.

## Exact response hierarchy

Success continuation **G9359ac** checks GetResultCode1, then tests presence of
ret_data. Within that object it separately tests these keys before parsing:

- achievement → Achieve.ParseAchievementsElement.
- entry → Parse_Entry **933aec**, call935b5c.
- inst_base → Parse_InstBase **933d80**, call935bd6.
- inst_enemy → Parse_InstEnemy **92dff4**.
- ref_stair → ParseStairInfo **9343b4**.
- ref_hero → ParseHeroInfo **9347f8**.

Original literal ADD sites935a0e/935a60(ret_data),935b54(entry),
935bcc(inst_base),935c46(inst_enemy),935cc0(ref_stair),935d52(ref_hero)
corroborate the names and immediate parents. Each helper receives its selected
subtree, not the full response. Old decompiler inference of Parse_Entry's
receiver type is unreliable: original935b5a moves selected JSON to r1 before
the call. Parse_Entry uses global PlayData/Inventory independently.

## Parsed subtrees and prerequisites

entry is an iterated row collection with **id, mirage_remain_hp**; Parse_Entry
also calls Inventory.ResetCardMirageRemainHP at933b2e. Do not synthesize an
owned hunter or reset server progress from a guessed row.

inst_base keys: **bg_res, dlg_begin, dlg_end, new_record, floor, stair, state,
deck, tier_percent, highest, revive_price, begin_ltime**. Exact nested deck
shape/state enum/timestamps still require helper dataflow; key vocabulary alone
does not justify a ready battle fixture.

inst_enemy rows: **n, ref_id, rank, rank_up_cnt, overcome_cnt, exp,
skill_1_level..skill_5_level**. Parser92dff4 instantiates ordinary card refs,
so nonempty enemy rows require real published card identity/stat/art bindings.

ref_stair keys: **res_prefix, res_postfix_list, list, grade, balance**.
Exact stair row nesting and original layout values remain unimplemented.

ref_hero keys: **bonus, end_ltime, cur, next**. Raw ParseHeroInfo stores bonus
as32bits to model+b4 at93486a and end_ltime as32bits to model+b0 at9348ba.
cur iterates a collection and strictly converts each element to STRING at
9349be, building the vector atmodel+98/9c/a0; next follows atADD934a32.
These are hero-ID collections, not full card records or numeric statistics.
Original hero membership and empty-vector consumer safety are not proved here.

All dispatcher keys are presence-conditional. A generic successful metadata
response can therefore skip native initialization while a later scene still
uses default cached fields. Empty response compatibility does not establish
safe RetryInfo presentation.

## New failure and next bounded proof

Ordinary Mirage entry emitted GetInfo and then RetryInfo.cpp58 asserted
**uiEndT>=uiCurT**; root reports PID3409 exited. Hero end_ltime is a concrete
candidate source because it is parsed into a time-like field, but its path to
that exact assertion, clock coordinates/units, retry eligibility and other UI
requirements await parent's RetryInfo decomp. Do not claim causality or publish
an arbitrary future timestamp from the key name alone.

Exact next targets: RetryInfo.Init **c05554**, SetThisWeekHunter **c0589c**;
model helpers **933d80/9343b4/9347f8** as needed. No original Mirage period,
hero/stair stats, reward, price or grants were recovered. A complete entry
response must satisfy proven consumer dependencies, not merely remove one
assertion with invented fields.

Parent follow-up closes the field path: RetryInfo.SetData Gc0643c reads
CGMTime.GetCurLocalTime, then GetHeroInfo()+0x18. GetHeroInfo G92eb60 returns
model+0x98, so that is model+0xb0, exactly ParseHeroInfo's end_ltime field.
The uiEndT>=uiCurT assertion is line58/Gc064b0. GetCurLocalTime G797646 returns
RMGetTickCount divided by1000 plus synchronizedbase+0x28 minusoffset+8.
This proves second-based clock arithmetic, not the original weekly schedule.
The schedule origin/timezone synchronization and original rotation remain
unknown; do not claim an arbitrary future timestamp reproduces the game.

Observed NPC0023 terminal sends actual GetInfo10:48:50.952Z, then assertion
10:48:51.226local13:48:51.226 and PID3409 exits. The generic response has no
native subtrees; it leaves caches unpopulated. This establishes the required
dependency at this entry, not a fully reconstructed Mirage battle/reward model.
