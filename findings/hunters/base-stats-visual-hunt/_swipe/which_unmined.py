"""Hash-compare the 28 freshly decoded FAQ images against the 17 files already
in analysis/catalogue/stats/found/, so the UNMINED set is exact rather than a
guess based on filenames."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(HERE, "gdoc")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "catalogue", "stats", "found"))


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


repo = {}
for n in sorted(os.listdir(REPO)):
    p = os.path.join(REPO, n)
    if os.path.isfile(p):
        repo[sha(p)] = n
print("repo files: %d" % len(repo))

fresh = []
for n in sorted(os.listdir(G)):
    if not n.startswith("faq_"):
        continue
    p = os.path.join(G, n)
    h = sha(p)
    fresh.append((n, os.path.getsize(p), h, repo.get(h)))

matched = [f for f in fresh if f[3]]
unmatched = [f for f in fresh if not f[3]]
print("exact-hash matched: %d   unmatched (UNMINED): %d" % (len(matched), len(unmatched)))
print("\n-- MATCHED --")
for n, s, h, r in matched:
    print("  %-12s -> %s" % (n, r))
print("\n-- UNMINED --")
for n, s, h, r in unmatched:
    print("  %-12s %8d  %s" % (n, s, h[:16]))
with open(os.path.join(HERE, "unmined.txt"), "w", encoding="utf-8", newline="\n") as f:
    for n, s, h, r in unmatched:
        f.write("%s\n" % n)
