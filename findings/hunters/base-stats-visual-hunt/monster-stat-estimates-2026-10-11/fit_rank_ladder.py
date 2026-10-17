#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fit_rank_ladder.py -- fit the episode-monster stat ladder and report it.

Reads the 34 recovered EPISODE_STAT_ACTORS.json monster rows (res_id M###) and
the 61 EPISODE_COMBAT_*.json stage records, joins them, and reports
  * per-rank hp/atk/def distribution (median, p10, p90)
  * power -> rank mapping
  * rank-multiplier recovery vs LEVELING.jet chunk 9 bonus.rank_1..5
Prints only; the numbers feed monster-stat-estimates-2026-10-11.tsv.
"""
import io, os, json, struct, statistics, collections

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
REF = os.path.join(ROOT, "sources", "client-tables", "reference")

rows = json.load(io.open(os.path.join(REF, "EPISODE_STAT_ACTORS.json"),
                         encoding="utf-8"))
mon = [r for r in rows if isinstance(r, dict)
       and str(r.get("res_id", "")).startswith("M")]
print("monster rows (res_id M###): %d" % len(mon))

# stage context
stage = {}
for fn in sorted(os.listdir(REF)):
    if not (fn.startswith("EPISODE_COMBAT_") and fn.endswith(".json")
            and "manifest" not in fn):
        continue
    d = json.load(io.open(os.path.join(REF, fn), encoding="utf-8"))
    sid = d.get("id")
    slots = []
    for side in ("left", "right"):
        for sl in (d.get(side) or []):
            for e in (sl or []):
                if isinstance(e, dict) and e.get("actor_id"):
                    slots.append((side, e))
    stage[sid] = {"power": int(d.get("power") or 0),
                  "title": d.get("title"), "stage_name": d.get("stage_name"),
                  "combat_base": d.get("combat_base"),
                  "left": sum(1 for s, e in slots if s == "left"),
                  "right": sum(1 for s, e in slots if s == "right"),
                  "slots": slots}

recs = []
for r in mon:
    aid = r["id"]
    st = r.get("stat") or {}
    ctx = None
    for sid, s in stage.items():
        for side, e in s["slots"]:
            if e.get("actor_id") == aid:
                ctx = (sid, s, e)
                break
        if ctx:
            break
    if ctx is None:
        sid, s, th, lvl, rank, hyper, attr = ("(no combat placement)",) + (None,) * 6
        power = None
    else:
        sid, s, e = ctx
        t = e.get("thumb") or {}
        power, th = s["power"], (t.get("level"), t.get("rank"),
                                 t.get("hyper"), t.get("attr"))
        lvl, rank, hyper, attr = th
    recs.append({"actor": aid, "res": r["res_id"], "ref_id": r.get("ref_id"),
                 "attr": r.get("attr"), "role": r.get("role"),
                 "rank": int(st.get("rank") or 0),
                 "hp": int(st.get("hp") or 0), "atk": int(st.get("atk") or 0),
                 "def": int(st.get("def") or 0),
                 "stage": sid, "power": power, "level": lvl,
                 "thumb_rank": rank, "hyper": hyper,
                 "slot_type": e.get("type") if ctx else None})

print("\n%-14s %-6s %-5s %-5s %-8s %-6s %-6s %-6s %-5s %-4s %s"
      % ("actor", "res", "rank", "lvl", "power", "hp", "atk", "def",
         "attr", "role", "stage"))
for x in sorted(recs, key=lambda z: (z["rank"], z["hp"])):
    print("%-14s %-6s %-5s %-5s %-8s %-6s %-6s %-6s %-5s %-4s %s"
          % (x["actor"], x["res"], x["rank"], x["level"], x["power"],
             x["hp"], x["atk"], x["def"], x["attr"], x["role"], x["stage"]))

print("\n--- per-rank ladder (n, hp median/p10/p90, atk, def) ---")
by = collections.defaultdict(list)
for x in recs:
    by[x["rank"]].append(x)


def pct(v, p):
    if not v:
        return 0
    v = sorted(v)
    k = (len(v) - 1) * p
    f, c = int(k), min(int(k) + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)


for rk in sorted(by):
    v = by[rk]
    hps = [x["hp"] for x in v]; atks = [x["atk"] for x in v]
    defs = [x["def"] for x in v]
    print("rank %d  n=%-2d hp med=%-6.0f [%d..%d]  atk med=%-6.0f [%d..%d]  "
          "def med=%-5.0f [%d..%d]"
          % (rk, len(v), statistics.median(hps), pct(hps, .1), pct(hps, .9),
             statistics.median(atks), pct(atks, .1), pct(atks, .9),
             statistics.median(defs), pct(defs, .1), pct(defs, .9)))

print("\n--- power -> rank ---")
pr = collections.defaultdict(set)
for x in recs:
    if x["power"]:
        pr[x["power"]].add(x["rank"])
for p in sorted(pr):
    print("  power %-7d -> ranks %s" % (p, sorted(pr[p])))

print("\n--- power -> hp/atk/def (log-log slope) ---")
import math
pts = [(x["power"], x["hp"], x["atk"], x["def"]) for x in recs if x["power"]]
for i, nm in ((1, "hp"), (2, "atk"), (3, "def")):
    xs = [math.log(p) for p, *_ in pts]
    ys = [math.log(r[i]) for r in pts]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / \
        sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    pred = [math.exp(a + b * x) for x in xs]
    act = [r[i] for r in pts]
    mape = sum(abs(p - q) / q for p, q in zip(pred, act)) / n
    print("  %-3s log-log slope=%.3f  intercept=%.3f  MAPE=%.0f%%"
          % (nm, b, a, 100 * mape))

print("\n--- LEVELING.jet chunk 9 bonus.rank_1..5 (recovered multipliers) ---")
mult = {1: (2.6, 1.4, 1.4), 2: (2.2, 1.3, 1.3), 3: (1.8, 1.2, 1.2),
        4: (1.4, 1.1, 1.1), 5: (1.0, 1.0, 1.0)}
print("  rank: hp x, atk x, def x")
for r in sorted(mult):
    print("   %d: %.1f %.1f %.1f" % (r, *mult[r]))
print("  NOTE direction debate: catalog/INDEX.md 5.2 infers rank 1 = toughest")
print("       band (hp 2.6x) and rank 5 = baseline 1.0x, i.e. rank counts DOWN.")
print("  Cross-check against the observed ladder direction:")
base = {}
for r in sorted(by):
    base[r] = (statistics.median([x["hp"] for x in by[r]]),
               statistics.median([x["atk"] for x in by[r]]),
               statistics.median([x["def"] for x in by[r]]))
r5 = base[5]
print("  rank -> median tuple, and hp relative to rank-5 median:")
for r in sorted(base):
    h, a, d = base[r]
    print("   %d: hp=%-7.0f (%.2fx r5)  atk=%-7.0f (%.2fx)  def=%-5.0f (%.2fx)"
          % (r, h, h / r5[0], a, a / r5[1], d, d / r5[2]))
print("\n  => observed hp ratio r1/r5 = %.2f ; LEVELING rank_1/rank_5 = 2.60"
      % (base[1][0] / r5[0]))
print("  => observed atk ratio r1/r5 = %.2f ; LEVELING rank_1/rank_5 = 1.40"
      % (base[1][1] / r5[1]))
