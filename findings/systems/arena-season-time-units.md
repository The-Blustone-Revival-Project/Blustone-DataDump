# Arena season datetime units

2026-10-04. Read-only original Thumb disassembly, curated parser decomp and corrected literals. No device/Ghidra/source/runtime operations. G addresses = ELF code VA +0x10000.

**Verified: end_datetime is numeric server-epoch seconds, not milliseconds.** Current arenaSeason Unix-second values agree with this native unit. Original season duration, calendar alignment, timezone and reset schedule remain local fixture choices.

## Exact field-to-consumer proof

ParseSeason G942e24 indexes end_datetime with corrected literal LDR942f34 / ADD942f3c (ghidra-arena-corrected-strings.txt). Its numeric64 result is stored by **STRD942f88 into parsed season+0x10**. Integers are copied directly; numeric strings/floats are converted without a time-unit division.

ParseEnter calls ParseSeason into a stack temporary at942cd6. It loads temporary+0x10 into d16/d17 at942cda/942ce2 and stores those bytes to **CSRFCPlayData+0xf0 at942cfc/942d00**. The whole season begins PlayData+0xe0 (942d04/942d0c). This pins +f0 to end_datetime, rather than inferring identity from nearby date fields.

CSRPopUpFC::RemainTimeTextRenewal Gc0c5cc loads **end_datetime+f0** atc0c5ea and c0c638, calls **CGMTime::GetCurServerTime** atc0c624/c0c672, and directly compares/subtracts the returned signed32 server time from the64-bit deadline (c0c628..c0c630 and c0c680/c0c684). There is no millisecond scaling between deadline and clock.

Remaining duration is divided by **86400**: MOVW r6,#0x5180 c0c69e plus MOVT r6,#1 c0c6a4; divisor r2=r6/c0c6aa and r3=0/c0c6ac precede division helper c0c6ae. It multiplies quotient by86400 and subtracts it atc0c6b4/c0c6b8, renders day count, then passes residual directly to **CMTimeToStrOnlyHMS** atc0c706. Millisecond input would show a grossly enlarged day count.

CGMTime::GetCurServerTime G797628 calls RMGetTickCount at79762e, divides its tick milliseconds by **1000** (797632..797638), then adds clock.server_utc+14 and subtracts initialization_ticks_seconds+8 (79763c..797642). Existing SetExtra/SetTime evidence in revival-systems-next.md pins server_utc to the server's seconds anchor. No local_time/utc_0 adjustment enters this getter.

## Coverage and limits

ParseSeason stores all six datetime fields as numeric64 without scaling: start at+8, end+10, next+18, weekly_start+20, weekly_end+28, weekly_next+30. They share the season timestamp vocabulary; consistent server-second values are supported by this recovered consumer. Only end_datetime's displayed deadline is independently traced here; additional weekly UI consumers were not inspected. This proves units and clock coordinate, not original historical calendar/economy or native rendered countdown success. Server timestamps after signed32 epoch range remain constrained by GetCurServerTime despite the64-bit wire fields.

Sources: ghidra-arena-lobby-helpers.txt, ghidra-arena-corrected-strings.txt, original libnative_core.so Thumb ranges above, revival-systems-next.md clock appendix, server-ts/src/arena.ts.
