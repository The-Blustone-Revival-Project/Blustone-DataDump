import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                 'grade-vs-level-factor-2026-10-06.md')
t = open(p, encoding='utf-8').read()

# 1. complete the script list
old = """  `pagetext.py`, `attach.py`, `links.py`, `entry.py`, `listpages.py`, `ident.py`,
  `ident2.py`, `zoom.py`, `calc.py`."""
new = """  `pagetext.py`, `attach.py`, `links.py`, `entry.py`, `listpages.py`, `catpages.py`,
  `ident.py`, `ident2.py`, `zoom.py`, `zoom_capa2.py`, `calc.py`, `capa_math.py`,
  `audit.py`, `fixeol.py`, and the section-fix helpers `peek.py` / `fixsec6.py` /
  `fixsum.py`."""
assert old in t
t = t.replace(old, new)

# 2. add confidence rows for the new findings
anchor = "| 戦闘力 archive column ≉ 戦闘力 in-game |"
i = t.find(anchor)
assert i > 0
rows = """| Capacity Transcendence is a pure **×1.0994** core-stat multiplier at fixed grade and level | **high** | `capa2`, three independent stats (ATK/DEF/HP) agreeing to **0.139 %**, digits re-read at 1000 px; guide text confirms it raises 基本能力値 |
| Capacity Transcendence is allowed **at most 3 times, one per rank-up** | **high** | verbatim in `/育成論/キャパ超越`; ceiling ×1.3287 is arithmetic on ×1.0994 |
| **戦闘力 is not a linear function of HP/ATK/DEF** | **high** | ×1.1625 vs ×1.0994 at one fixed-grade, fixed-grade/level point in one frame |
| the archive row for `036` cannot be reached from its ★3/Lv.1 row by one scalar across the three core stats | **high** for the constraint, **none** for the cause | ratios 3.1066 / 2.0685 / 2.0426 span **1.52×**; the archive row's grade and level are unestablished, so the spread is **not** attributed |
| `2019/03/capa.jpg` (189,444 B, 633×432, recovered here) is an **illustration**, not a stat frame | **high** | inspected directly |
"""
t = t[:i] + rows + t[i:]

# 3. record the capa.jpg negative in the searched table
old2 = """- `2019/02/capa2.jpg` and `2019/03/capa.jpg` (容量超越 / Capacity Transcendence,
  full-size originals). **`2019/03/capa.jpg` IS captured** — CDX row
  `20190401022918`, 200, WARC length 189,161 — so it needs only one fetch and one page
  read, and it was *not* in the prior lane's recovered set. The article's own
  semantics are unrecovered. If キャパ超越 is a *same-level* grade-equivalent boost,
  its ×1.162511 on Bear `036` would be a pure grade-side factor and would feed the
  system directly. **This is the single most promising unexplored lead.**"""
new2 = """- ~~`2019/02/capa2.jpg`~~ — **RESOLVED, and it is where the answer was.**
  `2019/03/capa.jpg` **is** captured (`20190401022918`; fetched here, **189,444 B**,
  **633×432**) but is an **illustration** (hero + hero = hero), no numbers.
  `2019/02/capa2.jpg` resolves to **no capture**; the payload is in the
  **`2018/11/capa2-1024x911.jpg`** that was already on disk — see **§3, T4**.
  The article's semantics were read and are decisive: キャパ超越 raises 基本能力値,
  max 3 times, once per rank-up."""
assert old2 in t
t = t.replace(old2, new2)

# 4. record the capa.jpg provenance in files touched
old3 = "- **Read only:** `_archives_work/`"
new3 = """- **Also recovered:** `img/2019-03_capa.jpg` (189,444 B, 633×432, ts
  `20190401022918`) — inspected and recorded as an illustration in §7.
- **Read only:** `_archives_work/`"""
assert old3 in t
t = t.replace(old3, new3, 1)

open(p, 'w', encoding='utf-8', newline='\n').write(t)
print('ok, bytes', len(t.encode('utf-8')))