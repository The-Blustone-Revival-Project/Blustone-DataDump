# -*- coding: utf-8 -*-
"""Generate the huge guesstimate tables and append to STATS-ESTIMATE-2026-10-06.md.

Read-only with respect to all source data files. Writes only the report file.
"""
import csv, json, statistics, sys, io
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:/Users/shaha/Documents/ChatGPT/Blustone'
OUT = BASE + r'/analysis/research/base-stats-visual-hunt/STATS-ESTIMATE-2026-10-06.md'

# ---------- load ----------
cat = list(csv.DictReader(open(BASE + r'/analysis/catalogue/data/card-catalogue.tsv', encoding='utf-8'), delimiter='\t'))
cat_by_id = {r['card_id']: r for r in cat}

arch = list(csv.DictReader(open(BASE + r'/analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv', encoding='utf-8'), delimiter='\t'))
arch_by_id = {r['catalog_id']: r for r in arch}

unc = list(csv.DictReader(open(BASE + r'/analysis/research/base-stats-visual-hunt/uncovered-archive-roster-2019.tsv', encoding='utf-8'), delimiter='\t'))
unc_by_id = {r['catalog_id']: r for r in unc}

epd = json.load(open(BASE + r'/analysis/recovered-reference/EPISODE_STAT_ACTORS.json', encoding='utf-8'))
epd_hunters = [r for r in epd if str(r.get('res_id', '')).startswith('C')]
epd_monsters = [r for r in epd if str(r.get('res_id', '')).startswith('M')]
epd_by_ref = defaultdict(list)
for r in epd_hunters:
    if r.get('ref_id'):
        epd_by_ref[r['ref_id']].append(r)

stages = list(csv.DictReader(open(BASE + r'/analysis/recovered-data/campaign-stages.csv', encoding='utf-8')))
s01 = json.load(open(BASE + r'/analysis/recovered-reference/EPISODE_S01.json', encoding='utf-8'))

ROLE_JA = {'攻撃手': 'Offense', '守備手': 'Defense', '爆撃手': 'Bomber', 'ヘルパー': 'Support'}
ELEM_JA = {'火炎': 'Fire', '冷気': 'Ice', '電撃': 'Lightning'}
ROLE_JP = {'Offense': 'Offense', 'Defense': 'Defense', 'Bomber': 'Bomber', 'Support': 'Support'}

def fnum(x):
    x = (x or '').strip().replace(',', '')
    try:
        return float(x)
    except ValueError:
        return None

# ---------- role substat medians from archive ----------
ROLE_COLS = ['speed', 'crit', 'crit_damage', 'penetration', 'block',
             'block_damage_reduction', 'element_enhance', 'element_resistance', 'hp_regen']
role_stats = defaultdict(lambda: defaultdict(list))
for r in arch:
    role = ROLE_JA.get(r['role_ja'])
    if not role:
        continue
    for c in ROLE_COLS:
        v = fnum(r[c])
        if v is not None:
            role_stats[role][c].append(v)
role_median = {role: {c: statistics.median(vs) for c, vs in cols.items()} for role, cols in role_stats.items()}

# r and s medians per role
r_med = {'Defense': 0.7647, 'Support': 1.0000, 'Offense': 1.3396, 'Bomber': 1.5452}
s_med = {'Defense': 0.9255, 'Support': 0.9088, 'Offense': 0.9190, 'Bomber': 1.1366}
HP_MED = {1: 1537, 2: 1624, 3: 1750, 4: 1955}
HP_MED_5 = 2542  # 1955 x 1.30 extrapolation

# CP approximate law (portal-derived, coarse)
CP = dict(intercept=-7884.12, hp=3.0603, atk=5.2060, dfn=5.8217, spd=43.5644, crit=33.0842,
          critdmg=5.2763, pen=34.0118, blk=31.9338, blkred=10.1295, eenh=-16.6714, eres=10.4604, regen=-4.9129)

def est_cp(hp, atk, dfn, sub):
    return (CP['intercept'] + CP['hp']*hp + CP['atk']*atk + CP['dfn']*dfn
            + CP['spd']*sub['speed'] + CP['crit']*sub['crit'] + CP['critdmg']*sub['crit_damage']
            + CP['pen']*sub['penetration'] + CP['blk']*sub['block'] + CP['blkred']*sub['block_damage_reduction']
            + CP['eenh']*sub['element_enhance'] + CP['eres']*sub['element_resistance'] + CP['regen']*sub['hp_regen'])

def guess_core(rarity, role):
    hp = HP_MED.get(rarity, HP_MED_5)
    s = s_med[role]; r = r_med[role]
    tot = hp * s
    atk = tot * r / (1 + r)
    dfn = tot / (1 + r)
    return round(hp), round(atk), round(dfn)

def guess_sub(role):
    m = role_median.get(role, {})
    return {c: round(m.get(c, 0), 2) for c in ROLE_COLS}

def esc(s):
    return (s or '').replace('|', '/').replace('\n', ' ').strip()

# ---------- build hero rows ----------
meta_rows = []   # everything for table A
for r in cat:
    cid = r['card_id']
    if cid in ('901', '902', '903', '904', '912', '913', '914', 'x914'):
        continue  # item rows, handled separately
    name, title = r['name'], r['title']
    # rarity/role/element: prefer adjudicated roster, then archive, then catalogue
    u = unc_by_id.get(cid)
    a = arch_by_id.get(cid)
    if u and u.get('rarity') not in ('', None):
        rarity, role, elem = u['rarity'], u['role'], u['element']
        meta_src = 'roster'
    elif a:
        rarity, role, elem = a['rarity_on_draw'], ROLE_JA.get(a['role_ja'], '?'), ELEM_JA.get(a['element_ja'], '?')
        meta_src = 'archive'
    else:
        rarity, role, elem = r['rarity'], r['role'], r['element']
        meta_src = 'catalogue'
    try:
        rarity_i = int(rarity)
    except ValueError:
        rarity_i = None

    epd_rows = epd_by_ref.get(cid.split('_')[0], [])
    if cid.endswith('_1'):
        epd_rows = [e for e in epd_rows if str(e.get('res_id', '')).endswith('_1')] or epd_rows

    notes = []
    row = {'id': cid, 'name': name, 'title': title, 'rarity': rarity, 'role': role, 'elem': elem}

    if a:
        vals = {c: fnum(a[c]) for c in
                ['combat_power', 'hp', 'atk', 'def', 'speed', 'crit', 'crit_damage', 'penetration',
                 'block', 'block_damage_reduction', 'element_enhance', 'element_resistance', 'hp_regen']}
        numeric_ok = vals['hp'] is not None
        if numeric_ok:
            row.update({k: (int(v) if v is not None and v == int(v) else v) for k, v in vals.items()})
            conf, word = 65, 'MEDIUM'
            if cid in ('004', '008', '019', '032', '034', '036', '038', '040', '042', '049', '055', '058', '060'):
                conf, word = 75, 'MEDIUM-HIGH'
            notes.append('2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished')
            if rarity_i == 4:
                notes.append('4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows')
            if cid == '051':
                conf, word = 85, 'HIGH'
                notes.append('ONLY strict row: archive cross-validates the Lv.30 no-equipment panel (2879/1471/1149); gear-invariance shown, shape drift <=2.2%')
        else:
            row.update({k: '?' for k in vals})
            conf, word = 5, 'VERY LOW'
            notes.append('archive page renders ??? placeholders (Genovia) - no numeric transcription exists')
    else:
        hp, atk, dfn = guess_core(rarity_i, role) if (rarity_i and role in s_med) else (None, None, None)
        sub = guess_sub(role) if role in s_med else {}
        row['hp'], row['atk'], row['def'] = hp, atk, dfn
        row.update(sub)
        if hp:
            row['combat_power'] = round(est_cp(hp, atk, dfn, sub))
        epd_tuples = [(int(float(e['stat']['hp'])), int(float(e['stat']['atk'])), int(float(e['stat']['def'])), e['stat'].get('rank')) for e in epd_rows]
        if epd_tuples and rarity_i:
            conf, word = 30, 'LOW'
            notes.append('NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse)')
            notes.append('Episode scripted tuple exists: ' + '; '.join(f'{h}/{a2}/{d2}@r{rk}' for h, a2, d2, rk in epd_tuples[:3]))
        elif rarity_i:
            conf, word = 20, 'VERY LOW'
            notes.append('NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law')
        else:
            conf, word = 10, 'VERY LOW'
            notes.append('rarity unresolved - magnitude cannot even be banded')
        if cid.endswith('_1'):
            notes.append('awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%)')
    if epd_rows and a:
        t = '; '.join(f"{int(float(e['stat']['hp']))}/{int(float(e['stat']['atk']))}/{int(float(e['stat']['def']))}@r{e['stat'].get('rank')}"
                      for e in epd_rows[:3])
        notes.append('Episode scripted tuples: ' + t)
        notes.append('identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums')
    row['conf'], row['word'], row['notes'] = conf, word, ' | '.join(notes)
    meta_rows.append(row)

# ---------- emit ----------
buf = io.StringIO()
w = buf.write

w('\n---\n\n# APPENDIX — the guesstimate tables (2026-10-06)\n\n')
w('**How to read the confidence columns.** `Conf%` = estimated probability that the '
  'row\'s core numbers (HP/ATK/DEF and, where present, the other published fields) sit within '
  '±10% of the original game\'s values in the stated context. Word scale: **HIGH** >=75, '
  '**MEDIUM** 50–74, **LOW** 25–49, **VERY LOW** <25, **CONTESTED** = two sources disagree '
  '(word carries the row regardless of %). Evidence classes: [ORIGDATA] shipped client data, '
  '[NATIVE] parser evidence, [COMM] community, [PIXEL] original-game pixels, [DERIVED] computed '
  'here from the corpus priors (never a source by itself).\n\n')
w('Every derived number below is a **guesstimate for reconstruction**, not recovered data. '
  'Era rule: anything dated before 2019-09-05 is PRE-rebalance; the 2019 JP archive rows are POST; '
  'the two eras must never be merged into one table without a scale bridge.\n\n')

# ---- Table A: heroes ----
w('## A. Per-hero stat guesstimates — all 113 catalog characters (121 rows incl. awakened)\n\n')
w('Core sources: 2019 JP archive (62 numeric rows, POST-era) > Episode STAT (scripted, rank>1 '
  'usually) > derived priors. Column order: identity, core tuple, substats, confidence.\n\n')
w('| ID | Name | Title | Draw★ | Role | Elem | HP | ATK | DEF | CP | SPD | Crit% | CritDmg% | Pen | Block% | BlockRes | EEnh | ERes | HPReg | Conf% | Word | Notes |\n')
w('|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n')
COLS = ['speed', 'crit', 'crit_damage', 'penetration', 'block', 'block_damage_reduction',
        'element_enhance', 'element_resistance', 'hp_regen']
for r in meta_rows:
    def g(k):
        v = r.get(k)
        return '' if v is None else v
    w(f"| {r['id']} | {esc(r['name'])} | {esc(r['title'])} | {r['rarity']} | {r['role']} | {r['elem']} "
      f"| {g('hp')} | {g('atk')} | {g('def')} | {g('combat_power')} "
      f"| {g('speed')} | {g('crit')} | {g('crit_damage')} | {g('penetration')} | {g('block')} "
      f"| {g('block_damage_reduction')} | {g('element_enhance')} | {g('element_resistance')} | {g('hp_regen')} "
      f"| {r['conf']} | {r['word']} | {esc(r['notes'])} |\n")
w(f'\n_{len(meta_rows)} rows. 62 carry 2019-archive numbers (806 source cells), 13 are two-source '
  'shape-confirmed, ~45 are derived priors, ~6 Episode-only, 1 placeholder (056)._\n')

# ---- Table B: episode hunter tuples ----
w('\n## B. Episode scripted hunter tuples — every hunter-typed row (117 rows / 54 heroes)\n\n')
w('These are per-appearance story tuning, NOT base stats. Kept complete because they are the '
  'only shipped numeric pairing of a hero identity with HP/ATK/DEF.\n\n')
w('| Combat ID | Hero ref | res_id | Rank | HP | ATK | DEF | SPD | Crit | CritDmg | Pen | Block | BlockRes | EEnh | ERes | HPReg | Conf% | Word | Notes |\n')
w('|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n')
for e in epd_hunters:
    st = e['stat']
    cat_row = cat_by_id.get(str(e.get('ref_id', '')))
    nm = cat_row['name'] if cat_row else ''
    def n(key):
        v = st.get(key, '')
        try:
            return int(float(v)) if float(v) == int(float(v)) else v
        except (ValueError, TypeError):
            return v
    w(f"| {e['id']} | {e.get('ref_id','')} {esc(nm)} | {e['res_id']} | {n('rank')} | {n('hp')} | {n('atk')} | {n('def')} "
      f"| {st.get('spd','')} | {st.get('crt_chance','')} | {st.get('crt_dmg','')} | {st.get('penetration','')} "
      f"| {st.get('block_chance','')} | {st.get('block_dec_dmg','')} | {st.get('attr_enhance','')} | {st.get('attr_resist','')} | {st.get('hp_regen','')} "
      f"| 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |\n")

# ---- Table C: episode monster tuples ----
w('\n## C. Episode scripted monster tuples — the 34 M* rows (42 monster-like rows incl. 8 monster-typed C* placements)\n\n')
w('| Combat ID | Monster | Rank | HP | ATK | DEF | SPD | Crit | CritDmg | Pen | Block | BlockRes | HPReg | Cool(ms) | Conf% | Word | Notes |\n')
w('|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n')
for e in epd_monsters:
    st = e['stat']
    def n(key):
        v = st.get(key, '')
        try:
            return int(float(v)) if float(v) == int(float(v)) else v
        except (ValueError, TypeError):
            return v
    ct = e.get('cool_time', '')
    w(f"| {e['id']} | {e['res_id']} | {n('rank')} | {n('hp')} | {n('atk')} | {n('def')} "
      f"| {st.get('spd','')} | {st.get('crt_chance','')} | {st.get('crt_dmg','')} | {st.get('penetration','')} "
      f"| {st.get('block_chance','')} | {st.get('block_dec_dmg','')} | {st.get('hp_regen','')} | {ct} "
      f"| 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |\n")
w('\n_Additional monster placements not shown: `CB1102_006/_008/_011/_018/_019` (C006/C008/C011/C018/C019) '
  'and 3 monster-placed `C010` rows — 8 monster-typed C* rows (SYNTHESIS correction, 2026-10-06)._\n')

# ---- Table D: monster catalog ----
mon = json.load(open(BASE + r'/analysis/catalogue/data/monsters.json', encoding='utf-8'))
w('\n## D. Monster catalog — 22 IDs (identity only; zero base-stat sources)\n\n')
w('| ID | Art pack | Bytes | Conf% | Word | Notes |\n|---|---|---:|---:|---|---|\n')
for m in mon:
    mid = m.get('monster_id', '')
    art = ','.join(m.get('art', []))
    w(f"| {mid} | {art} | {m.get('bytes_total','')} | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |\n")

# ---- Table E: jewels ----
w('\n## E. Jewel set bonuses — all 12 families, both shipped versions [ORIGDATA]\n\n')
w('| # | Family | Mount | 1.4.4.1 (PRE) | 2.8.0.1 (POST) | Conf% | Word | Notes |\n|---|---|---|---|---|---:|---|---|\n')
JEWELS = [
    ('1', 'HP', '2', '5%', '6%', 'HP/AP/DP x1.20 between versions'),
    ('2', 'Offensive (AP)', '2', '5%', '6%', ''),
    ('3', 'Defensive (DP)', '2', '5%', '6%', ''),
    ('4', 'Critical (crit chance)', '2', '4.5%', '6%', 'x1.333'),
    ('5', 'Block (block chance)', '2', '4.5%', '5%', 'x1.111'),
    ('6', 'Fatal (crit damage)', '4', '50%', '60%', 'x1.20'),
    ('7', 'Super Block (block-dmg reduction)', '4', '5% (KO 9%)', '10% (SC 9%)', 'CONTESTED: shipped client disagrees with itself across locales'),
    ('8', 'Element (enhancement)', '4', '+23 flat', '35', 'decimal ambiguity resolved for the SET effect only'),
    ('9', 'Resistance', '4', '+23 flat', '35', ''),
    ('10', 'Speed (attack speed)', '4', '1.72', '1.72', 'unchanged'),
    ('11', 'Regeneration (HP regen)', '4', '30', '30', 'unchanged; no unit printed anywhere'),
    ('12', 'Penetration', '4', '12', '16', 'x1.333'),
]
for num, fam, mount, v1, v2, note in JEWELS:
    word = 'CONTESTED' if 'CONTESTED' in note else 'HIGH'
    conf = 60 if word == 'CONTESTED' else 95
    w(f"| {num} | {fam} | {mount} | {v1} | {v2} | {conf} | {word} | {note} |\n")
w('\n_Confidence 95 = [ORIGDATA] help text in five locales, two shipped versions. These are '
  'HELP-STRING values, not engine constants; a help table can lag live balance (proven in-client)._\n')

w('\n## E.2 Mounted jewel samples — 6 transcribed Lv.15 panels [PIXEL, era-unknown]\n\n')
w('| Panel | Slot | Main | Sub 1 | Sub 2 | Sub 3 | Sub 4 | Conf% | Word | Notes |\n|---|---|---|---|---|---|---|---:|---|---|\n')
PANELS = [
    ('img22 Radiant Speed', 'Weapon', 'ATK +29', 'Crit Dmg +3.13', 'Block Ch +0.72', 'Elem Resist +1.44', 'Dmg Red Blk +0.50', 'removal footer 40000 gold + 40'),
    ('img23 Radiant Offensive', 'Weapon', 'ATK +29', 'DEF +11', 'Dmg Red Blk +0.38', 'Elem Enh +1.65', 'ATK +11', 'same jewel name yields different mains by slot'),
    ('img24 Radiant Offensive', 'Accessory', 'Max HP +58', 'ATK +12', 'Max HP +21', 'Elem Resist +1.69', 'Block Ch +0.56', ''),
    ('img25 Radiant Speed', 'Accessory', 'Max HP +58', 'Max HP +18', 'Crit Dmg +3.87', 'Block Ch +0.56', 'ATK +13', ''),
    ('img26 Radiant Speed', 'Armor', 'Block Ch +2.30', 'Block Ch +0.56', 'Max HP +21', 'Dmg Red Blk +0.50', 'DEF +11', ''),
    ('img27 Radiant Speed', 'Armor', 'DEF +29', 'Crit Ch +0.67', 'Dmg Red Blk +0.38', 'ATK +11', 'Crit Dmg +3.86', ''),
]
for p in PANELS:
    w(f"| {p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} | {p[5]} | {p[6]} | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15; {p[7]} |\n")

# ---- Table F: multipliers ----
w('\n## F. Multipliers — shipped battle tuning and measured combat scalars\n\n')
w('| Multiplier | Values | Applies to | Class | Conf% | Word | Notes |\n|---|---|---|---|---:|---|---|\n')
MULTS = [
    ('Monster rank (hp)', '2.6 / 2.2 / 1.8 / 1.4 / 1.0', 'rank 1-5', 'LEVELING.jet chunk 9 [ORIGDATA]', 95, 'HIGH', 'monster-rank, not hero rank'),
    ('Monster rank (atk/def)', '1.4 / 1.3 / 1.2 / 1.1 / 1.0', 'rank 1-5', 'LEVELING.jet chunk 9 [ORIGDATA]', 95, 'HIGH', ''),
    ('Role bonus (hp)', 'Bomber 0.85, Support 0.80, others 1.0', 'battle camps', '[ORIGDATA]', 95, 'HIGH', ''),
    ('atk_camp', '2.0 / 2.6 / 1.0', 'attack camp scaling', '[ORIGDATA]', 95, 'HIGH', 'semantics per-camp index'),
    ('Stage bonus', '1.1 x3 (hp/atk/def) for cards 051', 'bonus.stage b_00_01', '[ORIGDATA]', 90, 'HIGH', 'single entry only'),
    ('SP economy', 'first 1.5, regen 0.21/s, +2.0/kill, +0.02/attack, max 10', 'battle SP', '[ORIGDATA] chunk 9', 95, 'HIGH', 'live group measured 0.01-0.21 rate by mode'),
    ('Rarity magnitude step', 'approx x1.30 HP and ATK+DEF per grade', 'hero draw grade', '[DERIVED] n=62 archive', 70, 'MEDIUM', 'HP and ATK+DEF both x1.29-1.30; substats NOT scaled'),
    ('Per-level compound', 'x1.0189 avg (HP 1.01879 / ATK 1.01852 / DEF 1.01930)', 'hero level 1-30', '[DERIVED] 051 anchor, 29 steps', 60, 'MEDIUM', 'single-g misses panel by 6.6 cp; Natalia conflict 1.0101 unresolved'),
    ('enemy_atk_per / enemy_hp_per', '100 = 100% (neutral)', 'stage scalars', '[NATIVE]', 99, 'HIGH', 'proven: paths do not scale by it; do not "fix" to 1'),
    ('Transcendence T3', 'x1.30 (Hermes exact 3/3; flat ladder fits 8/9)', 'grade-up to 5-star', '[PIXEL] measured 3 heroes', 55, 'MEDIUM', 'cumulative x1.716 REFUTED; T1/T2 per-step x1.10/x1.20 UNTESTED; do not implement'),
    ('Tier scalar (PRE pairs)', 'x1.199 / 1.201 / 1.201 (HP/ATK/DEF)', 'Base-to-Max 25 pairs', '[COMM] contaminated', 40, 'LOW', 'Locke=Metis duplicate rows; PRE era'),
    ('EVCB event scale', 'approx x1.36 (median 1.358-1.375, CV 13.7%)', 'event combat vs archive', '[DERIVED] hypothesis', 30, 'LOW', 'test only, never install'),
    ('2019-09-05 rebalance', 'equipment +50%; crystal main +30% (1-3-star) / +50% (4-5-star); substats +50%; substat upgrades fixed at max', 'equipment/crystals', 'official announcement', 95, 'HIGH', 'no per-item delta; era boundary for every dated visual'),
    ('Power law (approx)', 'cp = -7884 + 3.060hp + 5.206atk + 5.822def + 43.56spd + 33.08crit + 5.28critdmg + 34.01pen + 31.93blk + 10.13blkred - 16.67eenh + 10.46eres - 4.91regen', 'combat power', '[DERIVED] OLS n=59 R2=0.996', 40, 'LOW', 'portal-derived fit, not a recovered formula; max residual ~81 cp'),
    ('block_damage_reduction cp weight', 'exactly 18 cp units', 'combat power', '[DERIVED] collision pairs', 45, 'LOW', 'portal-derived, exactly determined in 2 roles'),
]
for name, vals, appl, cls, conf, word, note in MULTS:
    w(f"| {name} | {vals} | {appl} | {cls} | {conf} | {word} | {note} |\n")

# ---- Table G: per-area campaign rewards ----
area_titles = {'n_01': 'Snowfield', 'n_02': 'Glacier', 'n_03': 'Red Rock', 'n_04': 'Aurora Tundra', 'n_05': 'Deep Cavern'}
area_name_conf = {'n_01': '90 · HIGH', 'n_02': '90 · HIGH', 'n_03': '90 · HIGH', 'n_04': '15 · VERY LOW', 'n_05': '15 · VERY LOW'}
w('\n## G. Per-area campaign rewards — 5 expedition areas x 10 stages (50 stages, [RECOVERED] structure)\n\n')
w('Stage/area/serial structure is recovered from `LEVELING.jet` chunk 0. All AMOUNTS are local '
  'fixtures unless marked; originals are unknown. Stars: 3 conditions per stage (native), '
  'default rules Complete/Under-60s/<=1 straggler are local policy.\n\n')
by_area = defaultdict(list)
for s in stages:
    by_area[s['area']].append(s)
w('| Area | Title | Stages | Stage IDs | First-clear gold (fixture) | First-clear user EXP (fixture) | Hunter EXP/win (fixture) | AP cost (fixture) | Chest thresholds | Chest amounts | Conf% | Word | Notes |\n')
w('|---|---|---|---|---|---|---|---|---|---|---:|---|---|\n')
for area in sorted(by_area):
    sts = sorted(by_area[area], key=lambda x: x['stage'])
    ids = ', '.join(s['stage'] for s in sts)
    t = area_titles.get(area, '?')
    w(f"| {area} | {t} | {len(sts)} | {ids} | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) "
      f"| {area_name_conf.get(area, '15 · VERY LOW')} "
      f"| Title: {('measured on screen' if area in ('n_01','n_02','n_03') else 'fixture')} | structure [RECOVERED] n={len(sts)} stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |\n")
w('\n_Capsule drop: AIRSHIP_TICKET x1 per qualifying normal victory is a LOCAL rule; the tutorial '
  'proves capsules come from clearing general stages but not the rate. Loss refunds fuel '
  '([ORIGDATA] help, 4 locales) — replica implements reservation-based refund._\n')

# ---- Table H: episode chapter rewards ----
w('\n## H. Episode chapter rewards — all 18 declarations [ORIGDATA, exact]\n\n')
w('| Chapter | Stories | Declared reward | Settled? | Conf% | Word | Notes |\n|---|---:|---|---|---:|---|---|\n')
ch_stories = {'E01': 7, 'E02': 8, 'E03': 7, 'E04': 4, 'E05': 8, 'E06': 7, 'E07': 5, 'E08': 7, 'E09': 7, 'E10': 7, 'E11': 8, 'E12': 7, 'E13': 8, 'E14': 7, 'E15': 8, 'E16': 9, 'E17': 9, 'E18': 5}
settled = {'E01': 'YES (implemented)', 'E02': 'YES (30 free Manda)', 'E05': 'YES (20 capsules)', 'E18': 'YES (100000 gold)'}
item_names = {'GC2': 'Lottery coupon', 'FMD1': 'free-Manda identity', 'RP1': 'gold display identity', 'AIRSHIP_TICKET': 'Helium capsule (crosswalk UNPROVED)'}
for ch in s01['childs']:
    if ch.get('type') != 'episode':
        continue
    cid = ch['id']
    rw = ch.get('reward', {})
    items = ', '.join(f"{i['ref_id']} x{i['qty']}" for i in rw.get('item', []))
    nm = ' + '.join(f"{i['ref_id']} ({item_names.get(i['ref_id'], 'material')})" for i in rw.get('item', []))
    st = settled.get(cid, 'NO (refuses; item row missing)')
    w(f"| {cid} | {ch_stories.get(cid,'?')} | {items} ({nm}) | {st} | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |\n")

# ---- Table I: original-pixel reward anchors ----
w('\n## I. Original-pixel reward anchors [PIXEL]\n\n')
w('| Anchor | Value | Context | Conf% | Word | Notes |\n|---|---|---|---:|---|---|\n')
PIX = [
    ('Search payout', '+1400 Rupees + scroll 5 / leaf 4 / trace 40 / orb 1', 'Volcanic Abyss, team lvl 40', 60, 'MEDIUM', 'first original Search payout pixels ever transcribed'),
    ('Search payout', '+2000 Rupees + crystals 8 / stones 5 / trace 40 / scroll 1', 'Electric Abyss, team lvl 62', 60, 'MEDIUM', ''),
    ('Search payout', '+2000 Rupees + leaf 5 / orb 3 / trace 3 / scroll 1', 'Volcanic Abyss, lvl 55', 60, 'MEDIUM', ''),
    ('Co-op reward', '21000 Rupees, 3 stars, rank 210', 'Co-op Exploration', 60, 'MEDIUM', 'single screen'),
    ('Recruitment mileage', '3 / 10 / 25 / 40 pulls (sum 78)', 'mileage phases', 70, 'MEDIUM', 'original pixels, phases split'),
    ('Skill training cost', '800 Rupees + materials 4/4/2', 'skill Lv.35', 60, 'MEDIUM', 'PRE-era, single account'),
    ('Transcendence cost', '9000 Rupees + 9 gems / 90 crystals', 'transcend button', 60, 'MEDIUM', 'matches two-source ladder 9/90/9000 at 3-star'),
    ('Advancement cost', '8000 (2 fodder) / 12000 (3 fodder)', '3-star to 4-star', 60, 'MEDIUM', 'cost varies with fodder count; no formula inferred'),
    ('Equipment upgrade', '50000 Rupees + 320/27 toolboxes', 'armor Lv.49 to 50', 60, 'MEDIUM', ' Vincent 010 screen'),
    ('Jewel removal fee', '40000 gold + 40 (second currency unknown)', 'jewel panel footer', 40, 'LOW', 'single image, era unknown'),
]
for a in PIX:
    w(f"| {a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]} |\n")

# ---- Table J: prices ----
w('\n## J. Price / economy guesstimates\n\n')
w('| Item | Value | Class | Conf% | Word | Notes |\n|---|---|---|---:|---|---|\n')
PRICE = [
    ('Gacha single draw', '30 Manda', '[NATIVE]+[COMM]', 95, 'HIGH', 'native constant vector [100,300,11,30]; counts 1 and 11 only'),
    ('Gacha 10+1 bundle', '300 Manda, guaranteed 3-star or above', '[NATIVE]+[PIXEL]', 95, 'HIGH', 'guarantee seen on device'),
    ('Gacha pools / probabilities / pity', 'UNKNOWN', '-', 5, 'VERY LOW', 'community prose only (4-star at 16 pulls uncorroborated)'),
    ('Gacha boost events', 'limited 3-star 400%/500%, all 3-star 200%', 'official event posts', 80, 'HIGH', 'per-scope reading; no base rate published'),
    ('AP refill item', '+10 AP, 5 Manda or 100 gold, 3/day shared', 'fixture', 15, 'VERY LOW', 'original amount/prices/reset unknown; VSFan +5/+7 is VIP benefit not price'),
    ('BP refill item', '+5 BP, 5 Manda or 100 gold, 3/day shared', 'fixture', 15, 'VERY LOW', 'BP mechanism [NATIVE] but values unknown'),
    ('Skill training gold', 'banded 100 to 1000 per decade of levels (L1-4=100 ... L45-49=1000)', '[COMM] x2', 55, 'CONTESTED', 'vs local 100xlevel formula (agree at L1 only); CONTESTED against fixture, sources agree with each other'),
    ('Skill training materials', 'role material from Lv5: 0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1, 0/4/2, 0/5/3, 0/6/4 per decade', '[COMM] x2 (30/30 cells agree)', 75, 'HIGH', 'decadal fragments 1-5; skill Lv.25 contested 4+1 vs 5+2'),
    ('Skill level caps', '10 / 20 / 30 / 40 / 50 by grade', '[COMM]+[ORIGDATA]+native shape', 90, 'HIGH', 'INFERRED from 10-per-grade rule'),
    ('Raise (training) cost', 'UNKNOWN per-source (fixture 100 gold)', '[COMM] pixels 8000/12000 at 2/3 fodder', 25, 'LOW', 'fixture 1000/source is 8-12x off pixel previews; no per-source anchor'),
    ('Rank-up materials', 'N same-star partners for rank N (1/2/3/4)', '[COMM] x2 + native capacity shape', 90, 'HIGH', 'rank 5 terminal row unpublished'),
    ('Rank-up stat bonus', 'formula 1 + (stat_bonus/100) x rank_up_cnt', '[NATIVE] formula', 85, 'HIGH', 'coefficient 5% is a fixture'),
    ('Transcendence ladder', '1-star: 5/50/5000, 15/150/15000, 45/450/45000; 2-star: 7/70/7000, 25/250/25000, 60/600/60000; 3-star: 9/90/9000, 30/300/30000, 80/800/80000; 4-star: 12/120, 40/400, 110/1100 (crystal/fragment/rupees)', '[COMM] x2, 39 cells agree', 70, 'MEDIUM', 'fragment:crystal 10:1 table-scoped; 2-star T3 60/600 single-source; era unresolved'),
    ('Transcendence duplicates', '1 / 2 / 3 per T1/T2/T3', '[COMM] x2', 70, 'MEDIUM', 'same hunter consumed, fodder 3-star floor'),
    ('Trace exchange threshold', 'per-hunter star-graded (fixture 10/20); Namu ladder 20/40/80/160', '[COMM] era-unresolved', 30, 'CONTESTED', 'shape (doubling) corroborated; absolute value unrecovered; local 10/20 NOT upheld as error'),
    ('Fight Club entry', '1 BP (fixture)', 'fixture', 10, 'VERY LOW', 'BP economy native shape only, zero value agreements'),
    ('Fight Club tier rewards', 'Silver/Gold 100 chips + 2 Manda; Emerald/Metron 150+2; Mandarin 200+2', '[COMM] single-source', 40, 'LOW', 'Bronze row unrecorded (not zero)'),
    ('Fight Club scoring', 'win +15, loss -8, defense loss -5 to -6, revenge/forfeit -8', '[COMM] x2', 65, 'MEDIUM', 'two-source agreement'),
    ('Fight Club rank rewards', '31 bands: rank 1 = 2500 chips + 800 Manda, descending 100 chips/band to 30000+ = 100 chips + 1 fuel coupon', '[COMM] single-source', 35, 'LOW', 'band 551-720 pays 255 (sic, preserved anomaly); Manda ends at rank 4700'),
    ('Arena rival refresh', 'UNKNOWN (fixture price_type 2 / 100)', 'fixture', 10, 'VERY LOW', 'no table vocabulary for refresh_price'),
    ('Attendance events', 'Sep 2018: 30 Manda/day x 9 = 270; Halloween: 20/day x 15 = 300', 'official posts', 80, 'HIGH', 'event-parameterised; no fixed daily number exists'),
    ('Lootbox', '1 box per 30 Manda or 200 fuel; 11 prizes, no probability column', 'official post', 60, 'MEDIUM', '300 fuel is itself a prize'),
    ('Weekly first-purchase bonus', '1 Special Request + 40 traces', 'official post', 60, 'MEDIUM', 'two independent 2018 events granted 10 per 10+1'),
    ('Login calendar', 'UNKNOWN (fixture 28 days x 100 gold)', 'fixture', 10, 'VERY LOW', 'no original daily-attendance counterpart in corpus'),
    ('Episode material settlement', 'E01 GC2x3 native-claimed; E03-E17 need item rows GC3/GC4/GC8/OV1/CERUM01-03/SK13/23/33/43/EM02/LCOIN/GC9-11', '[ORIGDATA] declarations', 60, 'MEDIUM', 'declarations exact; redemption items unreconstructed'),
    ('Team EXP ladder', 'UNKNOWN (fixture two-row 0/100 caps team level 2)', '[COMM] EXP-to-max 200/400/1200/4800/24000 = 200 x R!', 35, 'LOW', 'grade ladder multi-source; per-level step min_exp unrecovered from 7 corpora'),
    ('Grade EXP-to-max', '1-star 200, 2-star 400, 3-star 1200, 4-star 4800, 5-star 24000', '[COMM] x3-6 per rung', 80, 'HIGH', 'ratio 1:2:6:24:120 = 200 x R!; cruise rate 11 EXP per 6 fuel corroborates (x4)'),
    ('Star-advancement rupees', '1000 / 3000 / 12000 unanimous; 4-star to 5-star 60000 (x5) vs 15000 (x1 dissent)', '[COMM] x6', 65, 'MEDIUM', 'different axis from transcendence; fodder 1/2/3/4 same-grade'),
    ('Equipment upgrade breakpoints', '500/1000/5000/15000/30000/100000 at Lv 10/20/30/40/50 (community)', '[COMM]', 45, 'LOW', 'garbled Namu toolbox costs 500/1000/5000 NOT transcribed as exact'),
    ('Polish / gem prices', 'UNKNOWN (schema [NATIVE]: level, price_type, price, possibility, failed_compensation, add_sub_ability)', '[NATIVE] schema', 50, 'MEDIUM', 'zero original row values; polish is probabilistic, fail loses rupees only'),
    ('Gem mining price', 'UNKNOWN — no native route isolated', 'negative', 5, 'VERY LOW', 'Check10GatchOverGemMineLimit is a limit check, not a price'),
    ('Chest payouts (10/20/30 stars)', 'UNKNOWN (fixture 300/200/100 gold)', '[NATIVE] mechanism, amounts missing', 15, 'VERY LOW', 'chest item identities 912/913/914 = 2/3/4-star Transcendence Tickets [ORIGDATA]'),
]
for p in PRICE:
    w(f"| {p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} | {p[5]} |\n")

# ---- non-card rows note ----
w('\n## K. Non-card catalogue rows (items, no stats)\n\n')
w('| ID | Meaning | Conf% | Word | Notes |\n|---|---|---:|---|---|\n')
w('| 901/902/903/904 | premium/free currency display identities | 80 | HIGH | Manda display identities [ORIGDATA] |\n')
w('| 912/913/914 | 2/3/4-star Transcendence Tickets (area chests) | 90 | HIGH | CHAR_STR_RO rows; quantities unknown |\n')
w('| x914 | variant of 914 | 60 | MEDIUM | |\n')

# write
data = buf.getvalue()
with open(OUT, 'a', encoding='utf-8') as f:
    f.write(data)
print('appended', len(data), 'chars to', OUT)