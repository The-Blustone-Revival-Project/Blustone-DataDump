import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                 'grade-vs-level-factor-2026-10-06.md')
t = open(p, encoding='utf-8').read()

OLD_START = '## 6. HP / ATK / DEF from rank-up frames'
OLD_END = '## 7. Is grade now separable from level?'
i = t.find(OLD_START)
j = t.find(OLD_END)
assert i > 0 and j > i, (i, j)

NEW = """## 6. HP / ATK / DEF — found, but **not** in a rank-up frame

The brief asked whether the rank-up result screen carries core stats. **It does
not**, and that part is now settled rather than merely unobserved:

- **T1** (`rank2`, 1024×911) and **T2** (`0d40a5e4…-1`, 1024×904) are both
  ランクアップ審査 (review) + ランクアップ成功 (success) pairs. Both carry
  **戦闘力** and the granted skill's name and **icon** only. **No HP, ATK or DEF
  value appears in either**, at any magnification.
- **T3** (all three crops) carries **no numeric row at all** beyond the wallet HUD.
- **T6/T7** (bulk rank-up, release/market) carry counts and prices only.
- This is *structural*, not a census result: the rank-up result screen is a
  **collapsed hero header** (portrait, name, grade pill, 戦闘力). HP/ATK/DEF live in
  the `詳細情報` Character Attributes panel, which the prior lane established is
  never open in this corpus.

**But the core stats were recovered anyway**, from a screen class nobody had looked
at — the **キャパ超越 success screen**, already on disk and already cited by the
prior lane for its 戦闘力 token, with its three stat columns unread. See **§3, T4**:

    Bear 036, star3 / Lv.1, grade AND level both fixed
      ATK  365 -> 401   x1.098630
      DEF  423 -> 465   x1.099291
      HP   619 -> 681   x1.100162

All six digits re-read at 1000 px. The three independent quantities agree to
**0.139 %**, which is the tightest internal consistency check anywhere in this corpus
and validates the reading method more strongly than any single-token reading can.

This is a **gear-free** core-stat reading — the rank-up article states that equipment
unlocks only at ★4, and this hero is ★3, so the frame contains no equipment UI and the
hero provably cannot be wearing any. That is precisely the class of reading
`coverage.md` has been unable to produce (§10 below explains why it still earns no
coverage credit).

**What it settles, and what it does not.**
- It **settles** that a pure, grade-and-level-independent core-stat multiplier exists
  and is **×1.0994** (mean of three), cumulative ceiling **×1.3287** over the three
  applications the guide permits.
- It **settles** that **戦闘力 is not a linear function of the core stats**: under the
  same fixed-grade, fixed-level operation 戦闘力 rises **×1.1625**, i.e. **5.74 %**
  faster than the stats it must be derived from. So §5's 戦闘力 bound provably cannot
  be transferred to HP/ATK/DEF, and the reason is now measured rather than inferred.
- It **does not** give the per-level factor, because a capacity transcendence moves no
  level. It is a *third axis* of the scaling model, not a substitute for the second.

"""

t = t[:i] + NEW + t[j:]
open(p, 'w', encoding='utf-8', newline='\n').write(t)
print('section 6 replaced; bytes now', len(t.encode('utf-8')))