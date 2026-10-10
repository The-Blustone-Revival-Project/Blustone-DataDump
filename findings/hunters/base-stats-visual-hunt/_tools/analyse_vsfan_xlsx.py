#!/usr/bin/env python3
"""Characterise the axis structure of the VSFan 'Hunter Stats [BROKEN IGNORE].xlsx'.

Finding so far: the sheet is organised by GRADE (Bronze/Silver/Gold/Green/Blue)
crossed with {Base, Max} -- NOT by transcendence level. So it cannot yield a T1/T2
reading. But the Base/Max pair is a two-point comparison whose LEVEL is unstated,
which is exactly the open item 'does any source state a level for the reference
table'. This script measures what the pair looks like so the parent can judge
whether it is a usable level lever.

Read-only on the xlsx.
"""
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
NS_DOCREL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

GRADES = ["Bronze", "Silver", "Gold", "Green", "Blue"]


def col(ref):
    m = re.match(r"([A-Z]+)", ref or "")
    n = 0
    if not m:
        return -1
    for ch in m.group(1):
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def load(path):
    z = zipfile.ZipFile(path)
    sst = []
    try:
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(f"{NS_MAIN}si"):
            sst.append("".join(t.text or "" for t in si.iter(f"{NS_MAIN}t")))
    except KeyError:
        pass
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    tgt = {}
    for r in rels.findall(f"{NS_REL}Relationship"):
        t = r.get("Target") or ""
        t = t[1:] if t.startswith("/") else ("xl/" + t if not t.startswith("xl/") else t)
        tgt[r.get("Id")] = t
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    sheets = {}
    for sh in wb.iter(f"{NS_MAIN}sheet"):
        rid = sh.get(f"{NS_DOCREL}id")
        if rid in tgt:
            sheets[sh.get("name")] = tgt[rid]
    return z, sst, sheets


def cells(z, sst, path):
    out = []
    for row in ET.fromstring(z.read(path)).iter(f"{NS_MAIN}row"):
        d = {}
        for c in row.findall(f"{NS_MAIN}c"):
            i = col(c.get("r"))
            t = c.get("t")
            if t == "s":
                v = c.find(f"{NS_MAIN}v")
                d[i] = sst[int(v.text)] if v is not None and v.text else ""
            else:
                v = c.find(f"{NS_MAIN}v")
                d[i] = v.text if v is not None and v.text is not None else ""
        out.append((row.get("r"), d))
    return out


def main():
    path = sys.argv[1]
    z, sst, sheets = load(path)
    rows = cells(z, sst, sheets["Stats"])

    hero = None
    data = {}
    for rnum, d in rows:
        c0 = (d.get(0) or "").strip()
        if not c0:
            continue
        if c0.startswith("- "):
            # labels are literally "- Base Bronze" / "- Max Gold": STATE then GRADE
            parts = c0[2:].strip().split()
            state, g = parts[0], parts[1]
            key = (hero, g, state)
            vals = {}
            for idx, lab in [(1, "strength"), (2, "life"), (3, "atk"), (4, "def")]:
                raw = (d.get(idx) or "").strip()
                try:
                    vals[lab] = float(raw)
                except ValueError:
                    vals[lab] = None
            data[key] = vals
        else:
            hero = c0

    print(f"heroes seen: {len({k[0] for k in data})}")
    print(f"rows parsed : {len(data)}")
    print("\n=== does a transcendence axis exist anywhere? ===")
    allgrades = sorted({k[1] for k in data})
    allstates = sorted({k[2] for k in data})
    print(f"  grade-like axis : {allgrades}")
    print(f"  state axis      : {allstates}")
    print("  -> the only axes are GRADE x {Base,Max}. No T1/T2/T3/T4 axis exists.")

    print("\n=== Base -> Max deltas, per hero/grade (numeric cells only) ===")
    print(f"  {'hero':16s} {'grade':7s} {'dStr':>8s} {'dLife':>8s} {'dAtk':>8s} {'dDef':>8s}"
          f"  {'ratio L/A/D':>26s}")
    ratios = []
    for (h, g, st), v in sorted(data.items()):
        if st != "Base":
            continue
        m = data.get((h, g, "Max"))
        if not m:
            continue
        ds, dl, da, dd = [], [], [], []
        ok = True
        for lab, acc in [("strength", ds), ("life", dl), ("atk", da), ("def", dd)]:
            if v.get(lab) is None or m.get(lab) is None:
                ok = False
                break
            acc.append(m[lab] - v[lab])
        if not ok:
            continue
        rl = (m["life"] / v["life"]) if v["life"] else None
        ra = (m["atk"] / v["atk"]) if v["atk"] else None
        rd = (m["def"] / v["def"]) if v["def"] else None
        rr = f"{rl:.4f}/{ra:.4f}/{rd:.4f}" if None not in (rl, ra, rd) else "-"
        if None not in (rl, ra, rd):
            ratios += [rl, ra, rd]
        print(f"  {h[:16]:16s} {g:7s} {ds[0]:8.0f} {dl[0]:8.0f} {da[0]:8.0f} {dd[0]:8.0f}  {rr:>26s}")

    if ratios:
        ratios.sort()
        print(f"\n  Max/Base ratio over {len(ratios)} numeric fields: "
              f"min {ratios[0]:.4f}  median {ratios[len(ratios)//2]:.4f}  "
              f"max {ratios[-1]:.4f}  spread {(ratios[-1]-ratios[0])/ratios[-1]*100:.1f}%")

    print("\n=== cross-grade structure at Base, per hero (Life/Atk/Def) ===")
    for h in sorted({k[0] for k in data}):
        line = []
        for g in GRADES:
            v = data.get((h, g, "Base"))
            if v and v.get("life") is not None:
                line.append(f"{g[:2]}:{v['life']:.0f}/{v['atk']:.0f}/{v['def']:.0f}")
        if line:
            print(f"  {h[:16]:16s} " + "  ".join(line))


if __name__ == "__main__":
    main()
