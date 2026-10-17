import csv
rows = list(csv.DictReader(open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/missing-heroes-recheck.tsv', encoding='utf-8'), delimiter='\t'))
print("rows:", len(rows))
print("cols:", rows[0].keys() if rows else None)
rec = [r for r in rows if r['numeric_row_recovered'] == 'yes']
print("recovered:", len(rec))
import os
print("report_bytes:", os.path.getsize('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/REPORT.md'))
