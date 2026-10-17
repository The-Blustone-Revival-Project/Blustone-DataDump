#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extract_episode_actors.py -- read-only extraction for the monster base-stat lane.

Task 1: re-extract MONSTER actor rows from sources/client-tables/reference/EPISODE_STAT_ACTORS.json
        (rows with NO `ref_id` = enemy/monster actors; rows WITH `ref_id` = scripted
        hunter-side enemies keyed to a card ref_id, 55 distinct refs, 120 rows -- excluded).
Task 2: walk every sources/client-tables/reference/EPISODE_COMBAT_*.json and record
        stage id, `power` (stage rating), and each monster actor_id + thumb
        (level/rank/hyper/attr).

Positive control before trusting the parse: assert the known row
CB1201_BOSS == M100, rank 5, hp 16000, atk 7000, def 300, and that
CB1401_BOSS == M100, rank 5, hp 20000, atk 8000, def 280. If either assertion
fails the script aborts and emits nothing.

Output: episodes-monster-actors.tsv , episode-combat-stages.tsv in this folder.
No file outside this folder is written or modified.
"""
import json, os, sys, io

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
REF = os.path.join(ROOT, "sources", "client-tables", "reference")
OUT = os.path.join(ROOT, "findings", "hunters", "base-stats-visual-hunt",
                   "monster-stat-estimates-2026-10-11")

FIELDS = ["rank", "hp", "atk", "def", "spd", "crt_chance", "crt_dmg",
          "penetration", "block_chance", "block_dec_dmg",
          "attr_enhance", "attr_resist", "hp_regen"]


def load(p):
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def main():
    actors = load(os.path.join(REF, "EPISODE_STAT_ACTORS.json"))
    print("EPISODE_STAT_ACTORS.json: %d rows" % len(actors))

    monster_rows, hunter_ref_rows, other = [], [], []
    for r in actors:
        if not isinstance(r, dict):
            other.append(r); continue
        has_ref = "ref_id" in r and r.get("ref_id") not in (None, "")
        st = r.get("stat") or {}
        rec = {
            "id": r.get("id"), "ref_id": r.get("ref_id"),
            "res_id": r.get("res_id"), "attr": r.get("attr"),
            "role": r.get("role"), "cool_time": r.get("cool_time"),
            "skill_count": len(r.get("skill") or []),
        }
        for f in FIELDS:
            rec[f] = st.get(f)
        (hunter_ref_rows if has_ref else monster_rows).append(rec)

    print("  rows WITHOUT ref_id (monster actors) : %d" % len(monster_rows))
    print("  rows WITH    ref_id (hunter-side)    : %d" % len(hunter_ref_rows))
    print("  non-dict / junk entries             : %d %r" % (len(other), other))
    noref_complete = [m for m in monster_rows
                      if m["hp"] not in (None, "") and m["atk"] not in (None, "")]
    print("  monster rows with a non-empty hp    : %d" % len(noref_complete))
    distinct_hunter_refs = sorted({h["ref_id"] for h in hunter_ref_rows})
    print("  distinct hunter ref_ids             : %d" % len(distinct_hunter_refs))

    # ---- positive control -------------------------------------------------
    by_id = {m["id"]: m for m in monster_rows}
    ctl = [("CB1201_BOSS", "M100", "5", "16000", "7000", "300"),
           ("CB1401_BOSS", "M100", "5", "20000", "8000", "280"),
           ("CB0102_M1",  "M022", "1", "450",  "430",  "180")]
    ok = True
    for cid, rid, rk, hp, atk, df in ctl:
        row = by_id.get(cid)
        got = None if row is None else (row["res_id"], row["rank"], row["hp"],
                                        row["atk"], row["def"])
        exp = (rid, rk, hp, atk, df)
        print("  POSCTL %-14s expect %s got %s -> %s"
              % (cid, exp, got, "OK" if got == exp else "FAIL"))
        ok = ok and (got == exp)
    if not ok:
        sys.exit("POSITIVE CONTROL FAILED - aborting, nothing written")

    # ---- task 1 dump ------------------------------------------------------
    os.makedirs(OUT, exist_ok=True)
    all_rows = monster_rows + hunter_ref_rows
    by_id = {r["id"]: r for r in all_rows if r.get("id")}
    hdr = ["actor_id", "res_id", "monster_id", "attr", "role", "cool_time",
           "skill_count"] + FIELDS
    lines = ["\t".join(hdr)]
    for m in sorted(monster_rows, key=lambda x: (str(x["res_id"]), str(x["id"]))):
        mid = (m["res_id"] or "")
        mid = mid[1:] if mid.startswith("M") else mid
        lines.append("\t".join([
            "" if m["id"] is None else str(m["id"]),
            "" if m["res_id"] is None else str(m["res_id"]),
            ("M" + mid) if mid and mid != "None" else "",
            "" if m["attr"] is None else str(m["attr"]),
            "" if m["role"] is None else str(m["role"]),
            "" if m["cool_time"] is None else str(m["cool_time"]),
            str(m["skill_count"]),
        ] + ["" if m[f] is None else str(m[f]) for f in FIELDS]))
    with io.open(os.path.join(OUT, "episodes-monster-actors.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote episodes-monster-actors.tsv (%d data rows)" % (len(lines) - 1))

    # ---- task 2 dump ------------------------------------------------------
    combat_files = sorted(fn for fn in os.listdir(REF)
                          if fn.startswith("EPISODE_COMBAT_") and fn.endswith(".json")
                          and "manifest" not in fn)
    print("\nEPISODE_COMBAT_*.json : %d files" % len(combat_files))
    ch = ["stage_id", "title", "stage_name", "power", "game_res_id",
          "side", "slot_index", "type", "actor_id",
          "thumb_level", "thumb_rank", "thumb_hyper", "thumb_attr",
          "actor_has_stat_row", "actor_res_id", "actor_stat_rank",
          "actor_stat_hp", "actor_stat_atk", "actor_stat_def"]
    clines = ["\t".join(ch)]
    n_monsters = 0
    for fn in combat_files:
        d = load(os.path.join(REF, fn))
        stage = d.get("id", fn)
        for side in ("left", "right"):
            for si, slot in enumerate(d.get(side) or []):
                for e in (slot or []):
                    if not isinstance(e, dict):
                        continue
                    aid = e.get("actor_id")
                    if aid is None:
                        clines.append("\t".join([
                            stage, str(d.get("title", "")), str(d.get("stage_name", "")),
                            str(d.get("power", "")), str(d.get("game_res_id", "")),
                            side, str(si), str(e.get("type", "")), "<NO actor_id>",
                            "", "", "", "", "n/a", "", "", "", "", ""]))
                        continue
                    th = e.get("thumb") or {}
                    a = by_id.get(aid)
                    # actor id may be recorded under a different stage prefix
                    hit = a
                    if hit is None:
                        for k, v in by_id.items():
                            if k is not None and (k == aid or k.endswith(aid)):
                                hit = v; break
                    # a "monster" slot is only a MONSTER actor if its res_id is M*
                    res = (hit or {}).get("res_id") or ""
                    is_monster = (e.get("type") == "monster"
                                  and str(res).startswith("M"))
                    clines.append("\t".join([
                        stage,
                        "" if d.get("title") is None else str(d.get("title")),
                        "" if d.get("stage_name") is None else str(d.get("stage_name")),
                        "" if d.get("power") is None else str(d.get("power")),
                        "" if d.get("game_res_id") is None else str(d.get("game_res_id")),
                        side, str(si),
                        "" if e.get("type") is None else str(e.get("type")),
                        "" if aid is None else str(aid),
                        str(th.get("level", "")), str(th.get("rank", "")),
                        str(th.get("hyper", "")), str(th.get("attr", "")),
                        "yes" if hit else "NO",
                        "" if not hit else str(hit["res_id"]),
                        "" if not hit else str(hit["rank"]),
                        "" if not hit else str(hit["hp"]),
                        "" if not hit else str(hit["atk"]),
                        "" if not hit else str(hit["def"]),
                    ]))
                    if is_monster:
                        n_monsters += 1
    with io.open(os.path.join(OUT, "episode-combat-stages.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(clines) + "\n")
    print("wrote episode-combat-stages.tsv (%d actor slots, %d monster slots)"
          % (len(clines) - 1, n_monsters))


if __name__ == "__main__":
    main()
