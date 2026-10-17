t = open('findings/hunters/base-stats-visual-hunt/namu-browser-2026-10-10/role-bomber.txt', encoding='utf-8').read()
names = ["Geranium", "Audrey", "Selene", "Blondie", "Themis", "Judith"]
out = []
out.append(f"len={len(t)}")
for n in names:
    i = t.find(n)
    out.append(f"{n}: idx={i}")
    if i >= 0:
        out.append(repr(t[max(0, i-300):i+300]))
open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/namu-probe.txt', 'w', encoding='utf-8').write("\n".join(out))
print("wrote")
