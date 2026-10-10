# Original native Hunter level selectors — 2026-10-08

Read-only review of `analysis/ghidra-hunter-level-getters-insn.txt` and
`analysis/ghidra-card-stat-level-detail.txt`, compared with
`server-ts/src/training.ts` and `server-ts/src/hunter-levels.ts`.
Addresses below are relocated Ghidra addresses; ELF virtual addresses are
Ghidra minus `0x10000`. The instruction dump resolves returns omitted by the
decompiler's incorrect `void` prototypes. No runtime, state or balance changes
were made by this review.

## Proven contracts

`CARD_LEVEL_INFO` rows have stride `0x10`: level at `+0`, cumulative minimum
EXP at `+4`, material/raise EXP at `+8`, sale price at `+0xc`.
GetCardLevel, GetCardMaxLevel, GetCardMaxExp and GetCardMinExp select the map at
`this+0x7c` by ordinary rank when awakening is zero, or the map at `this+0x88`
by awakening step otherwise. Missing keys return level 1 or EXP 0, respectively.

- **GetCardLevel (G010a0b2c):** walk rows in stored order until the first
  `min_exp > EXP`. Return that row's `level - 1`, clamped to at least 1.
  If every threshold is reached, return the last row's level, likewise clamped.
  An empty vector returns 1. Instructions G010a0bb2–G010a0bd0, dump lines 62–76.
- **GetCardMaxLevel (G010a0c68):** return the last row's **level field**.
  G010a0cf6 loads `[end-0x10]`, dump line 187. This is neither the vector
  count nor count minus one. A present but empty vector is not safely handled;
  publish a nonempty vector for every advertised rank.
- **GetCardMaxExp (G010a0d0c):** for level L greater than zero, return
  `rows[L].min_exp` when L is less than row count, otherwise the last row's
  `min_exp`. Level zero specially returns the second row's minimum EXP.
  Instructions G010a0d44–G010a0d58, lines 217–223; level-zero branch
  G010a0d94–G010a0d98, lines 249–250. The zero branch requires a second row.
- **GetCardMinExp (G010a0da0):** index by `uint32(L-1)`; if that unsigned
  index is outside the vector, return the last minimum EXP; otherwise return
  the indexed minimum EXP. Consequently **level zero returns the last minimum
  EXP**, because the unsigned bounds check runs before the signed-negative
  branch. Instructions G010a0e10–G010a0e2a, lines 301–311.
- **GetCardRaiseExp (G010a0e34):** select only the ordinary rank map at
  `this+0x7c`; index by `uint32(L-1)` and return that positional row's `+8`
  field, clamping an out-of-range index to the last row. Level zero therefore
  returns the last raise EXP. The awakening map is not selected in this
  function. Missing rank returns 0. Instructions G010a0e4a and
  G010a0e98–G010a0eb4, lines 325 and 358–368.

## Current fixture parity and limits

The current ordinary tables publish 30 dense rows per rank, levels 1 through
30, minimum EXP `100*(level-1)`, and raise EXP `100*level`. For valid ordinary
cards, `trainingCurve` already matches the native selector and positional
raise-EXP lookup. Its cap is the final minimum EXP, 2900, which is also the
native maximum EXP at native maximum level 30. **No extra terminal/sentinel
row is needed.** Adding one with a larger level would increase native maximum
level rather than merely delimit the existing cap.

Examples under this fixture: EXP 99 gives level 1/raise EXP 100; EXP 100 gives
level 2/200; EXP 240 gives level 3/300; EXP 840 gives level 9/900; EXP 2900 or
greater gives level 30/3000. The fixture's numbers remain local policy;
the recovered selector arithmetic establishes no original numeric thresholds.
Saved EXP should remain unchanged. Awake training remains intentionally refused
because its reference curve is unreconstructed.

Future replacement tables must retain nonempty, dense, ordered levels and
ordered cumulative thresholds. Native level computation uses the level field,
while EXP/raise-EXP getters index the vector position. `trainingCurve` currently
finds the raise row by level field; this is equivalent for the dense fixture,
but would diverge from native positional lookup with sparse level labels.
There is no demonstrated current parity defect requiring a source change.
