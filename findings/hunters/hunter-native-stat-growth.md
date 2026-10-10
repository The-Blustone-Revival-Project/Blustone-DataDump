# Native ordinary Hunter stat growth boundary

2026-10-08. Original library, read-only Ghidra. No APK, runtime, saved EXP,
rank, balance or account changes. Addresses are retained Ghidra coordinates.

`CSRCardInfo::GetStat` at G87acc8 selects an explicit rank/awakening row;
it does not infer a rank multiplier. `ordinaryRankStats` repeats identical
local values across five ranks. The former source comment claiming implicit
native rank scaling was therefore removed.

`CSRCard::SetExp` at G869ea4 stores EXP at card+20, asks UserLV.GetCardLevel
with rank at +24 and awakening at +694, and stores the result at +678. When
that level changes it refreshes lower/upper EXP bounds at +680/+684 using
GetCardMinExp/GetCardMaxExp. See `ghidra-hunter-set-exp.txt`.

The exact seven instructions of `SRCalcStat` at G10ac71c establish:

```
uint32 sum = base + increment * level; // ARM mla, wrapping 32-bit arithmetic
return float(sum) * multiplier;       // unsigned conversion, float32 product
```

Evidence: `ghidra-stat-formula-insn.txt`. The decompiler's formal float
parameter is misleading: the fourth argument is physically r3, moved to s2.
`CSRCard::Validate` calls this helper three times (G86adee/G86aec4/G86af86)
with card+678 as level. However, the base/increment arguments have passed
through decimal representation conversion and other calculations, and the
caller applies further rank-up/card-book/other bonuses. This is **not** yet
a closed mapping from wire hp/hp_up/atk/atk_up/def/def_up to final actor stats.
Do not replace the entire chain with the helper alone or claim recovered
original growth magnitudes. See `ghidra-owned-stat-validate-speed.txt` and
`ghidra-stat-formula-callers.txt`.

`CSRCard::GetStat` G869d24 accumulates the selected reference row and five
additional stat components before overwriting rank/awakening. Its companion
GetStatWithoutEquip G869e10 copies the selected reference row. This supports
keeping reference selection separate from equipment/other contributions.

`CSRGameActorStat::LoadStat` G9b4770 asks CardAnalyzer for final damage,
defense and health and stores them at actor-stat +38/+40/+24,+28. It obtains
CalcAtkSpeed and writes `(1 / CalcAtkSpeed) / tuning[+254]` at +3c.
CalcAtkSpeed G86de4c reconstructs the selected stat's decimal value using
power-of-ten conversion. Exact arithmetic survives in
`ghidra-hunter-speed-insn.txt`; `ghidra-owned-battle-stat-load.txt` records
the actor conversion. The tuning field and input stat binding still need
closure, so the archived speed 7/8 versus fixture 100/110 remains a unit
question, not permission to replace the values.

## Further closure: parser fields, speed and native ownership

Exact PC-relative string resolution in `ghidra-stat-parser-keys.txt`, matched
to parser instructions, binds CSRCardStat offsets: hp +18, atk +28, def +38,
spd +8, hp_up +c8, atk_up +d8, def_up +e8. These are hexadecimal offsets;
each numeric stat is a 16-byte decimal representation, not a native float.
See `ghidra-stat-parser-first-insn.txt` and
`ghidra-stat-parser-growth-insn.txt`. Parser's scale argument can modify stats;
these bindings alone do not establish a particular call's scale argument.

Original CSRCard primary vtable G2151198 has slot0=G869d25 (GetStat) and
slot4=G869e11 (GetStatWithoutEquip), Thumb bits set. Constructor/GOT evidence
is in `ghidra-card-primary-got.txt`, `ghidra-card-primary-functions.txt`,
`ghidra-card-owner-literal.txt` and `ghidra-leveldata-owner-constructor.txt`.
Validate calls slot4 into stack+158. Thus its three helper calls use def/def_up,
hp/hp_up, atk/atk_up respectively, with native level and multiplier **1.0**.
They decode decimal integer components before the helper; other bonuses follow.
For positive integral rows with no bonuses and scale1, the base-growth term is
`base + up * level`, **not** `base + up * (level-1)`. No undocumented implicit
rank factor appears in this term. This does not recover original magnitudes.

CalcAtkSpeed's slot0 calls GetStat, reconstructing spd from its mantissa and
power-of-ten exponent. LoadStat then stores an **interval**, not a rate:
`1 / spd / atk_spd_bonus`. Original LevelData parser G a19542..a195c8 binds
`atk_spd_bonus` to +254 (`ghidra-episode-leveling-background-keys.txt:98-99`,
`ghidra-episode-leveling-background.txt:2578`). GetAtkSpd multiplies that
interval by the buff interval and clamps to at least0.06 seconds; see
`ghidra-combat-stat-vip-getters.txt` and `stage3-input-gate.md`.

Original `analysis/extracted/assets/LEVELING.jet` SHA256
ba73fff17002cc94f7f1a98bf657be1bef042283051a5b92c395347006d3c57e
has bonus0.8 in JSON chunks9/10/11/12/14 and1.0 in17; chunks13/15/16/18 omit it.
Constructor default is1.0 and omission preserves the existing value. Do not
deduce live selection from a chunk's presence. For example spd100/bonus0.8
would produce0.0125 seconds before the minimum; spd7 would produce~0.1786.
These examples explain units, not a live measured attack rate or retune.

`InspectNativeInput --combat-tuning --frame` now observes the selected
DataMgr+a850/a854 pair. The DataMgr owner retains its existing exact guard.
Separate LevelData control primary ELF2143558 owns pointer at+c (original
LoadLevelData G8b26e4); emplace control ELF2143530 owns embedded object at+c
(original destructor G8b59e8). Unknown/expired owners refuse before field reads.
Both owner chains/bonus are rechecked. No native calls, writes or input.
`ghidra-leveldata-owner-insn.txt`, `ghidra-leveldata-owner-literal.txt`,
`ghidra-leveldata-owner-vtable.txt`, `ghidra-leveldata-control-entries.txt` and
`ghidra-datamgr-level-default.txt` establish those bounds. Initial separate-only
guard refused the live emplace registration, as intended; after recovering its
destructor/table the additional exact owner was accepted.

Client27494, Village, read-only frame snapshot
`analysis/testing/hunter-tuning-village-004.txt`: selected bonus **1.0**.
This is current registration evidence; it does **not** prove CB0102 tuning.
No battle started or stats changed. Probe compiled and ran successfully.

The recovered level selectors are documented separately in
`hunter-native-level-selectors.md`. Current dense fixture selectors match
native behavior. All original intermediate XP thresholds and ordinary stat
magnitudes remain unresolved; preserve actual earned EXP and ranks.
