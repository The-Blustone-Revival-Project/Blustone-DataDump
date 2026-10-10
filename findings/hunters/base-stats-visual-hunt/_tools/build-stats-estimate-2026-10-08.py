# -*- coding: utf-8 -*-
"""Build STATS-ESTIMATE-2026-10-08.md from the 2026-10-06 corpus file.

Same format; applies the confidence raises and new data from AGENTS.md §136–§165.
Read-only with respect to the source file.
"""
import json, sys, io, re
sys.stdout.reconfigure(encoding='utf-8')

SRC = r'C:/Users/shaha/Documents/ChatGPT/Blustone/analysis/research/base-stats-visual-hunt/STATS-ESTIMATE-2026-10-06.md'
OUT = r'C:/Users/shaha/Documents/ChatGPT/Blustone/analysis/research/base-stats-visual-hunt/STATS-ESTIMATE-2026-10-08.md'
EPD = r'C:/Users/shaha/Documents/ChatGPT/Blustone/analysis/recovered-reference/EPISODE_STAT_ACTORS.json'
CAT = r'C:/Users/shaha/Documents/ChatGPT/Blustone/analysis/catalogue/data/card-catalogue.tsv'

txt = open(SRC, encoding='utf-8').read()

# ---------- intro edits ----------
txt = txt.replace(
    '# Blustone stat-recovery guesstimate — corpus assessment (2026-10-06)',
    '# Blustone stat-recovery guesstimate — corpus assessment (2026-10-08 refresh)')

CHANGELOG = """
## 0. What changed in the 2026-10-08 refresh (evidence: AGENTS.md §136–§165)

The corpus itself was already research-complete; this refresh folds in native
verifications the live client produced in the two days after the Oct-6 file.
Same format, same tables — the deltas:

1. **Grade EXP-to-max endpoints 200/400/1200/4800/24000 raised 80→95 (HIGH):**
   an in-client consumer audit (§156) corroborates all five endpoints against
   the owned hunters' native levels. Interior thresholds remain unknown.
2. **Owned-hunter stats 001–004 are now native-verified** at their live levels
   (§159 archive-2019-projection deployed; detail/BuildTeam parity, native
   strength 25904). New Table A.2. The decomposition into base+growth still
   uses fixture growth (+10/+1/+1), so Table A base rows keep their archive
   confidence; A.2 is the display-pipeline proof.
3. **Enemy-side hunter-class rows natively rendered** (§160–§165): CB0102
   Gerard HP1000, CB0103 Bear HP1700, CB0201 enemy Bright HP900, CB0202 ally
   Bright HP600, CB0301 Denali HP1300, CB0302 Vincent HP3000. New Table C.2 —
   these rows jump to ~90 (HIGH). Chapter-specific tuning re-confirmed
   (E03-M023 650/160/10 ≠ E02-M023).
4. **Wire stat growth formula closed [NATIVE]** (§158): hp/atk/def/spd at
   CSRCardStat+18/+28/+38/+8, growth +c8/+d8/+e8, helper =
   uint32(base+up×level)×multiplier, Validate receives GetStatWithoutEquip.
   **Attack-speed unit closed**: interval = (1/spd)/atk_spd_bonus, min 0.06 s.
   **Level selectors closed** (§157): no sentinel; first threshold above EXP →
   level-1. All added to Table F. Magnitudes remain fixtures.
5. **SP/Rage is mode-dependent**: live CB0102 groups measured rate 0.03/max 10
   (§160) — the chunk-9 values are not global. Skill-cost debit verified
   natively (Nene cost 3: SP 10→7.04, §161).
6. **E02 FMD1×30 receipt verified natively** (§164: free Manda 239640→239670);
   the ×30 quantity is original, the wallet mapping stays replica policy.
   Login claim path verified day3/day4 (§146/§155); Special Supply settlement
   verified for all 16 local rows (§147).
7. **Fishing settlement contract wire-verified but data-blocked**: EndWithSell
   posts `log_id:"-1"`; terminal ACK is 27/2; missing fish reference → DUMMY
   zero popup, not a legitimate catch. All 6 local LevelDB cache containers
   scanned, zero reference keys (§145).
8. Mirage no longer crashes (§136: `GetExtra.local_time` + GetInfo DTOs; the
   Oct-6 clock assertion is retired). Not a stat datum, but it un-blocks the
   Mirage mode for future content work.

Nothing was re-derived: every raise quotes its §-numbered source.
"""

anchor = '> numbers in it comes from.'
txt = txt.replace(anchor, anchor + '\n' + CHANGELOG, 1)

# bottom-line tweak
txt = txt.replace(
    '| Multipliers | Shipped tuning fully in hand | ~90% of battle model | HIGH (shipped) / MEDIUM (measured) |',
    '| Multipliers | Shipped tuning fully in hand | ~95% of battle model (wire growth + attack-speed unit now [NATIVE]) | HIGH (shipped) / MEDIUM (measured) |')

# ---------- Table A: 001–004 note additions ----------
A_NOTES = {
    '001': 'NATIVE-VERIFIED display at owned Lv4: 1561/1062/657/SPD7 (§159)',
    '002': 'NATIVE-VERIFIED display at owned Lv3: 1654/842/685/SPD8 (§159)',
    '003': 'NATIVE-VERIFIED display at owned Lv3: 1780/729/867/SPD7 (§159)',
    '004': 'NATIVE-VERIFIED display at owned Lv9: 1557/688/688/SPD7 (§159)',
}
lines = txt.splitlines(keepends=True)
for i, l in enumerate(lines):
    m = re.match(r'^\| (00[1-4]) \|', l)
    if m and l.rstrip().endswith('|'):
        cid = m.group(1)
        lines[i] = l.rstrip()[:-1].rstrip() + ' / ' + A_NOTES[cid] + ' |\n'
txt = ''.join(lines)

# ---------- insert A.2 after Table A tail ----------
A2 = """
## A.2 Native-verified live display stats — owned hunters (2026-10-08)

Rendered in the instrumented client against the deployed archive-2019
projection; detail view and BuildTeam agree, and these exact stats fought and
won CB0102/CB0103/CB0201/CB0202/CB0301 (§159–§165). These verify the **display
pipeline and the base+up×level formula**, not original magnitudes — the
per-level growth increments are fixtures.

| Ref | Hero | Owned level | HP | ATK | DEF | SPD | Conf% | Word | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 001 | Lantern | 4 | 1561 | 1062 | 657 | 7 | 85 | HIGH | native detail view + BuildTeam (§159); growth +10/+1/+1 per level is a fixture |
| 002 | Mowgli | 3 | 1654 | 842 | 685 | 8 | 85 | HIGH | same pipeline proof (§159) |
| 003 | Nene | 3 | 1780 | 729 | 867 | 7 | 85 | HIGH | same pipeline proof (§159) |
| 004 | Tyltyl | 9 | 1557 | 688 | 688 | 7 | 85 | HIGH | same pipeline proof (§159) |

Native BuildTeam strength across the full four-hunter party: **25904**
(§159). Wins §160–§165 were fought with exactly these numbers — local
projection playability is proven; original balance is NOT claimed.
"""
tailA = '_113 rows. 62 carry 2019-archive numbers (806 source cells), 13 are two-source'
idx = txt.index(tailA)
end = txt.index('\n', txt.index('_\n', idx)) + 1 if '_\n' in txt[idx:idx+400] else idx
# find end of that italic line
line_end = txt.index('\n', idx) + 1
txt = txt[:line_end] + A2 + txt[line_end:]

# ---------- build C.2 from Episode STAT actors ----------
import csv
cat_by_id = {}
with open(CAT, encoding='utf-8') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        cat_by_id[r['card_id']] = r
epd = json.load(open(EPD, encoding='utf-8'))
PREFIXES = ('CB0102', 'CB0103', 'CB0201', 'CB0202', 'CB0301', 'CB0302', 'CB1102')
NATIVE = {
    'CB0102': 'rendered HP1000→0 in the live native win (§160)',
    'CB0103': 'Bear rendered HP1700→0, original cut-in followed (§161–162)',
    'CB0201': 'enemy Bright rendered HP900→0 (§164)',
    'CB0202': 'ally Bright HP600 held alive through the win (§164)',
    'CB0301': 'Denali rendered HP1300→0 in the live native win (§165)',
    'CB0302': 'Vincent rendered HP3000 — combat pending (§165)',
    'CB1102': 'not yet exercised in play',
}
rows = [e for e in epd if str(e.get('res_id', '')).startswith('C')
        and any(str(e['id']).startswith(p) for p in PREFIXES)]
buf = io.StringIO()
w = buf.write
w('\n## C.2 Enemy/allied hunter-class rows — natively exercised combats (2026-10-08)\n\n')
w('The `C*`-namespace rows the Episode combats place outside the player party. '
  'Where §-evidence exists the row was seen live in the instrumented client at '
  'exactly these values, which raises confidence above the scripted-data baseline.\n\n')
w('| Combat ID | Hero ref | res_id | Rank | HP | ATK | DEF | SPD | Block | BlockRes | HPReg | Conf% | Word | Notes |\n')
w('|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n')
for e in sorted(rows, key=lambda x: x['id']):
    st = e['stat']
    cat_row = cat_by_id.get(str(e.get('ref_id', '')))
    nm = cat_row['name'] if cat_row else ''
    def n(k):
        v = st.get(k, '')
        try:
            return int(float(v)) if float(v) == int(float(v)) else v
        except (ValueError, TypeError):
            return v
    pref = str(e['id'])[:6]
    native = NATIVE.get(pref, '')
    conf = 90 if native.startswith(('rendered', 'Bear', 'enemy', 'ally', 'Denali', 'Vincent')) else 55
    word = 'HIGH' if conf == 90 else 'MEDIUM'
    note = ('scripted story context' if not native else native)
    if not native:
        note += '; scripted tuning [ORIGDATA], not yet natively exercised'
    w(f"| {e['id']} | {e.get('ref_id','')} {nm} | {e['res_id']} | {n('rank')} | {n('hp')} | {n('atk')} | {n('def')} "
      f"| {st.get('spd','')} | {st.get('block_chance','')} | {st.get('block_dec_dmg','')} | {st.get('hp_regen','')} "
      f"| {conf} | {word} | {note} |\n")
w(f'\n_{len(rows)} rows extracted from EPISODE_STAT_ACTORS.json (151-row STAT table); '
  'monster-typed CB1102 rows included for completeness. M* rows remain in Table C._\n')
C2 = buf.getvalue()

tailC = '_Additional monster placements not shown:'
idx = txt.index(tailC)
line_end = txt.index('\n', idx) + 1
txt = txt[:line_end] + C2 + txt[line_end:]

# ---------- Table F: SP row update + new rows ----------
old_sp = ('| SP economy | first 1.5, regen 0.21/s, +2.0/kill, +0.02/attack, max 10 | '
          'battle SP | [ORIGDATA] chunk 9 | 95 | HIGH | live group measured 0.01-0.21 rate by mode |')
new_sp = ('| SP economy | first 1.5, regen 0.21/s, +2.0/kill, +0.02/attack, max 10 — **mode-dependent**: live CB0102 groups measured rate 0.03/max 10 (§160) | '
          'battle SP | [ORIGDATA] chunk 9 + [NATIVE] live read | 95 | HIGH | do not assume chunk-9 values globally; skill-cost debit natively verified (Nene cost 3: SP10→7.04, §161) |')
txt = txt.replace(old_sp, new_sp, 1)

F_ADD = """| Wire stat growth formula | hp/atk/def/spd stored at CSRCardStat+18/+28/+38/+8, growth at +c8/+d8/+e8; helper = uint32(base + up×level) × multiplier; Validate receives GetStatWithoutEquip | hero stat pipeline | [NATIVE] §158 | 90 | HIGH | formula shape proven; magnitudes/growth increments remain fixtures |
| Attack-speed unit | actor interval = (1/spd)/atk_spd_bonus, then buff, minimum 0.06 s; LevelData+254 = 0.8 (chunks 9/10/11/12/14) or 1.0 (17), omitted elsewhere | attack interval | [NATIVE] §158 | 90 | HIGH | do not infer the selected chunk from field presence |
| Hunter level selectors | GetCardLevel = first threshold above EXP returns row.level-1 (min 1), else last row.level; GetCardMaxLevel = last row.level; RaiseExp indexes level-1, clamped | level lookup | [NATIVE] §157 | 90 | HIGH | no sentinel row needed; interior XP thresholds still unknown |
| Stat consumer getters | GetAtk = base(+38)×buff(+38), upper clamp 3, lower unresolved, final min 1; GetDef at +40; GetAtkSpd at +3c product | combat stat read | [NATIVE] §156 | 85 | HIGH | bounded readonly audit of original Thumb |
| Active-skill activation | native press→eventpool→ReserveSkill→SP debit; Nene cost 3: SP 10→7.04, pause2/state4→resume | skill economy | [NATIVE] §161 | 85 | HIGH | numeric effect damage NOT isolated amid ordinary hits/healing |
"""
tailF_row = '| block_damage_reduction cp weight | exactly 18 cp units | combat power | [DERIVED] collision pairs | 45 | LOW | portal-derived, exactly determined in 2 roles |'
idx = txt.index(tailF_row)
line_end = txt.index('\n', idx) + 1
txt = txt[:line_end] + F_ADD + txt[line_end:]

# ---------- Table J updates ----------
old_exp = ('| Grade EXP-to-max | 1-star 200, 2-star 400, 3-star 1200, 4-star 4800, 5-star 24000 | '
           '[COMM] x3-6 per rung | 80 | HIGH | ratio 1:2:6:24:120 = 200 x R!; cruise rate 11 EXP per 6 fuel corroborates (x4) |')
new_exp = ('| Grade EXP-to-max | 1-star 200, 2-star 400, 3-star 1200, 4-star 4800, 5-star 24000 | '
           '[COMM] x3-6 + in-client corroboration (§156) | 95 | HIGH | ratio 1:2:6:24:120 = 200 x R!; endpoints verified against owned native levels; interior thresholds remain unknown |')
assert old_exp in txt
txt = txt.replace(old_exp, new_exp, 1)

old_ep = ('| Episode material settlement | E01 GC2x3 native-claimed; E03-E17 need item rows GC3/GC4/GC8/OV1/CERUM01-03/SK13/23/33/43/EM02/LCOIN/GC9-11 | '
          '[ORIGDATA] declarations | 60 | MEDIUM | declarations exact; redemption items unreconstructed |')
new_ep = ('| Episode material settlement | E01 GC2x3 pending claim; **E02 FMD1x30 natively credited (free Manda 239640→239670, §164)**; E03-E17 need item rows GC3/GC4/GC8/OV1/CERUM01-03/SK13/23/33/43/EM02/LCOIN/GC9-11 | '
          '[ORIGDATA] declarations + [NATIVE] receipt | 75 | MEDIUM-HIGH | quantity x30 is original; the wallet mapping is replica policy; E01 auto-request was correctly refused (§162) |')
assert old_ep in txt
txt = txt.replace(old_ep, new_ep, 1)

old_login = ('| Login calendar | UNKNOWN (fixture 28 days x 100 gold) | fixture | 10 | VERY LOW | '
             'no original daily-attendance counterpart in corpus |')
new_login = ('| Login calendar | UNKNOWN (fixture 28 days x 100 gold; day3/day4 claimed natively at 100 gold + 20 VIP EXP, §146/§155) | fixture + [NATIVE] claim path | 15 | VERY LOW | '
             'claim/receipt mechanics native-verified; the 100-gold amounts remain local fixture |')
assert old_login in txt
txt = txt.replace(old_login, new_login, 1)

J_ADD = '| Fishing settlement | BLOCKED — original fish item reference missing; EndWithSell posts log_id:"-1" (wire-verified); terminal ACK is 27/2 | [NATIVE] wire + [ORIGDATA] parser | 50 | MEDIUM | missing reference falls back to DUMMY zero INFO — NOT a legitimate catch; no empty-catch success until a real fish row exists (§143–145) |\n'
tail_j = '| Chest payouts (10/20/30 stars) | UNKNOWN (fixture 300/200/100 gold) | [NATIVE] mechanism, amounts missing | 15 | VERY LOW | chest item identities 912/913/914 = 2/3/4-star Transcendence Tickets [ORIGDATA] |'
idx = txt.index(tail_j)
line_end = txt.index('\n', idx) + 1
txt = txt[:line_end] + J_ADD + txt[line_end:]

# ---------- write ----------
with open(OUT, 'w', encoding='utf-8', newline='') as f:
    f.write(txt)
print('wrote', OUT, len(txt), 'chars')
print('C.2 rows:', len(rows))
for e in rows:
    print(' ', e['id'], e.get('ref_id'), e['res_id'], e['stat']['hp'], e['stat']['atk'], e['stat']['def'])