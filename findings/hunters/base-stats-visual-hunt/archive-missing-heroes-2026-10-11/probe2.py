import re, urllib.parse
html = open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/index-20191209130354.html', encoding='utf-8', errors='replace').read()
# error-shell checks
shells = ["Temporarily Offline", "bot-traffic", "Wayback Machine", "redirect interstitial",
          "404", "This page is available on the web"]
print("len", len(html))
# extract /hunter/ links
links = re.findall(r'href="([^"]*?/hunter/[^"]*)"', html)
print("raw hunter hrefs:", len(links))
uniq = sorted(set(links))
print("uniq hrefs:", len(uniq))
with open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/index-dec-links.txt', 'w', encoding='utf-8') as f:
    for u in uniq:
        f.write(u + "\n")
# profile-shape: rarity + title (2 segments after /hunter/)
prof = []
for u in uniq:
    # normalize absolute/relative
    if u.startswith("/"):
        path = u
    elif "blustone.jp" in u:
        path = urllib.parse.urlparse(u).path
    else:
        path = u
    segs = [s for s in path.split("/") if s]
    if len(segs) == 3 and segs[0] == "hunter":
        prof.append(urllib.parse.unquote(segs[2]))
prof = sorted(set(prof))
print("dec profile titles:", len(prof))
with open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/index-dec-titles.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(prof))
census = open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/profile-titles.txt', encoding='utf-8').read().split("\n")
cs, ps = set(census), set(prof)
print("census-not-in-dec:", len(cs - ps), "dec-not-in-census:", len(ps - cs))
with open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/index-diff.txt', 'w', encoding='utf-8') as f:
    f.write(f"census={len(cs)} dec={len(ps)}\n")
    f.write("---IN CENSUS NOT DEC---\n" + "\n".join(sorted(cs - ps)) + "\n")
    f.write("---IN DEC NOT CENSUS---\n" + "\n".join(sorted(ps - cs)) + "\n")
print("wrote diff")
