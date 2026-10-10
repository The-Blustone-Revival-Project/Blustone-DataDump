# -*- coding: utf-8 -*-
"""Insert G.2 per-stage reward table (50 rows) before section H. Read-only elsewhere."""
import csv, sys, io
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:/Users/shaha/Documents/ChatGPT/Blustone'
OUT = BASE + r'/analysis/research/base-stats-visual-hunt/STATS-ESTIMATE-2026-10-06.md'

stages = list(csv.DictReader(open(BASE + r'/analysis/recovered-data/campaign-stages.csv', encoding='utf-8')))
area_titles = {'n_01': 'Snowfield', 'n_02': 'Glacier', 'n_03': 'Red Rock',
               'n_04': 'Aurora Tundra', 'n_05': 'Deep Cavern'}

buf = io.StringIO()
w = buf.write
w('\n## G.2 Per-stage reward guesstimates — all 50 campaign stages\n\n')
w('Structure [RECOVERED] (stage id, area, serial from `LEVELING.jet` chunk 0). Every AMOUNT '
  'column is a local fixture shown for completeness; the original per-stage amounts are '
  'unknown (14 documented unknowns in `rewards-economy-2026-10-05.md` §D). Stars: 3 '
  'conditions/stage (native); wave contents are NOT recovered — no original stage→monster '
  'mapping exists locally.\n\n')
w('| Stage | Area | Serial | First-clear gold (fixture) | First-clear user EXP (fixture) | Hunter EXP (fixture) | AP cost (fixture) | Stars | Conf% | Word | Notes |\n')
w('|---|---|---:|---|---|---|---|---|---:|---|---|\n')
for s in sorted(stages, key=lambda x: x['stage']):
    area, serial = s['area'], s['serial']
    w(f"| {s['stage']} | {area} {area_titles.get(area,'?')} | {serial} | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | "
      f"15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished "
      f"(enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |\n")
w('\n_Area chest anchors: thresholds 10/20/30 stars per area ([NATIVE] achieve_cnt = stage_cnt x (i+1)); '
  'payout amounts unknown. Chest item identities 912/913/914 = 2/3/4-star Transcendence Tickets ([ORIGDATA])._')

data = buf.getvalue()
lines = open(OUT, encoding='utf-8').read().splitlines(keepends=True)
idx = next(i for i, l in enumerate(lines) if l.startswith('## H. Episode chapter rewards'))
lines.insert(idx, data + '\n')
open(OUT, 'w', encoding='utf-8', newline='').writelines(lines)
print('inserted', len(data), 'chars before section H; file now', sum(len(l) for l in lines), 'chars')