import csv, json
titles = open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/profile-titles.txt', encoding='utf-8').read().split('\n')
rows = list(csv.DictReader(open('findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.tsv', encoding='utf-8'), delimiter='\t'))
have = set(r['listed_name'] for r in rows)
out = []
out.append(f"census_titles={len(titles)} tsv_names={len(have)}")
missing = [t for t in titles if t not in have]
extra = [h for h in have if h not in titles]
out.append(f"census_not_in_tsv={len(missing)}")
out.append(f"tsv_not_in_census={len(extra)}")
with open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/title-diff.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out) + "\n---MISSING---\n" + "\n".join(missing) + "\n---EXTRA---\n" + "\n".join(extra) + "\n")
print("wrote title-diff")
