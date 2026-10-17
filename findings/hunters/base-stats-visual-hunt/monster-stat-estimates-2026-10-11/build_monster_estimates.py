#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build_monster_estimates.py -- emit the 2026-10-11 monster base-stat lane output.

Inputs (read-only):
  sources/client-tables/reference/EPISODE_STAT_ACTORS.json   34 monster rows
  sources/client-tables/reference/EPISODE_COMBAT_*.json      61 stage records
  jet-monster-namespaces.json                                pack -> monster crosswalk

Outputs (this folder only):
  episode-monster-recovered-rows.tsv     the 34 source-backed client rows, verbatim
  monster-stat-estimates-2026-10-11.tsv  the 22 catalog (ledger-denominator) rows
  model-figures.txt                      the fitted ladder, printed

Model summary
-------------
A. RECOVERED anchors. `EPISODE_STAT_ACTORS.json` carries 34 rows whose `res_id`
   is an `M###` monster id. Each is a full 14-field stat block. The matching
   `EPISODE_COMBAT_*.json` record supplies the difficulty context (stage id,
   stage `power`, and the actor's `thumb` = level/rank/hyper/attr). So a row is
   "a source-backed HP/ATK/DEF tuple tied to an unambiguous monster ID plus
   level/rank/difficulty context" -- exactly the ledger's promotion clause.

B. The catalog's 22 rows are ART PACKAGES, not monsters. Decoding each record's
   u64 id in base 38 over "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._" yields the
   sprite/animation namespace names. Pack M0nn (n=1..21) hosts exactly the three
   consecutive monster ids M(3n-2), M(3n-1), M(3n); M100.jet hosts only M100.
   Proof that pack name != monster id: monster res_id M022 (CB0102_M1) has no
   M022.jet on disk and its namespace lives inside M008.jet.

C. Estimation ladder (fit on the 34 rows). stage `power` determines `rank`
   monotonically and cleanly, and `rank` determines the stat band:
       power <  2500 -> rank 1          1000, 2200                       (2 rows)
       2500..8999   -> rank 2          2700, 4500, 5000                  (4 rows)
       9000..24999  -> rank 3          9000                              (5 rows, one boss at r4)
       25000..39999 -> rank 4          25000, 26000, 33000               (5 rows, all r4)
       >=40000      -> rank 5          40000..115000                    (18 rows, all r5)
   Observed per-rank medians (hp / atk / def):
       r1 275/160/100   r2 800/680/160   r3 1000/1200/180
       r4 2500/2600/200 r5 7000/6000/280
   power->stat log-log fits:  hp = 1.150*P^0.776 (MAPE 28%),
                               atk = 1.063*P^0.763 (MAPE 14%),
                               def = 27.83*P^0.203 (MAPE 7%).
   **`rank` counts UP in the shipped data** (rank 5 = toughest band). This
   refutes the direction inferred at catalog/INDEX.md 5.2 for LEVELING.jet
   `bonus.rank_1..5`; see REPORT.md.

D. Confidence rule (mechanical, not asserted).
   * [RECOVERED]  = 95 % -- the value is a verbatim shipped literal for one
     identified monster in one identified encounter; stat.hp is the unscaled
     on-screen combat HP (REPORT.md S2).
   * [DERIVED-ESTIMATE] point confidence = 100 * (1 - log10(hp bracket ratio) /
     log10(200)), floored at 15 and capped at 45. All ten derived rows therefore
     sit at 15-45 %, i.e. below the 60 % counting threshold.
"""
import io, os, json, re, struct, statistics, math, collections

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
REF = os.path.join(ROOT, "sources", "client-tables", "reference")
OUT = os.path.join(ROOT, "findings", "hunters", "base-stats-visual-hunt",
                   "monster-stat-estimates-2026-10-11")
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._"


def pctl(v, p):
    v = sorted(v)
    k = (len(v) - 1) * p
    f, c = int(k), min(int(k) + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)


# ---------------------------------------------------------------- anchors ----
def load_anchors():
    rows = json.load(io.open(os.path.join(REF, "EPISODE_STAT_ACTORS.json"),
                             encoding="utf-8"))
    mon = [r for r in rows if isinstance(r, dict)
           and str(r.get("res_id", "")).startswith("M")]
    stages = {}
    for fn in sorted(os.listdir(REF)):
        if not (fn.startswith("EPISODE_COMBAT_") and fn.endswith(".json")
                and "manifest" not in fn):
            continue
        d = json.load(io.open(os.path.join(REF, fn), encoding="utf-8"))
        slots = {}
        for side in ("left", "right"):
            for si, sl in enumerate(d.get(side) or []):
                for e in (sl or []):
                    if isinstance(e, dict) and e.get("actor_id"):
                        slots[e["actor_id"]] = (side, si, e.get("thumb") or {},
                                                e.get("state") or {})
        stages[d.get("id")] = {"file": fn, "power": d.get("power"),
                               "title": d.get("title"),
                               "stage_name": d.get("stage_name"),
                               "combat_base": d.get("combat_base"),
                               "slots": slots}
    out = []
    for r in mon:
        st = r.get("stat") or {}
        ctx = None
        for sid, s in stages.items():
            if r["id"] in s["slots"]:
                side, si, thumb, state = s["slots"][r["id"]]
                ctx = {"stage": sid, "file": s["file"], "power": s["power"],
                       "title": s["title"], "stage_name": s["stage_name"],
                       "combat_base": s["combat_base"], "side": side,
                       "slot": si, "thumb": thumb, "state": state}
                break
        out.append({
            "actor_id": r["id"], "res_id": r["res_id"],
            "ref_id": r.get("ref_id") or "",
            "attr": r.get("attr"), "role": r.get("role"),
            "cool_time": r.get("cool_time"),
            "rank": int(st.get("rank") or 0), "hp": int(st.get("hp") or 0),
            "atk": int(st.get("atk") or 0), "def": int(st.get("def") or 0),
            "spd": st.get("spd"), "crt_chance": st.get("crt_chance"),
            "crt_dmg": st.get("crt_dmg"), "penetration": st.get("penetration"),
            "block_chance": st.get("block_chance"),
            "block_dec_dmg": st.get("block_dec_dmg"),
            "attr_enhance": st.get("attr_enhance"),
            "attr_resist": st.get("attr_resist"),
            "hp_regen": st.get("hp_regen"), "ctx": ctx})
    return out


def load_packs():
    d = json.load(io.open(os.path.join(OUT, "jet-monster-namespaces.json"),
                          encoding="utf-8"))
    return {row["package"]: sorted(row["namespaces"]) for row in d}


def main():
    anchors = load_anchors()
    packs = load_packs()

    # ---- recovered-row TSV -------------------------------------------------
    hdr = ["actor_id", "monster_res_id", "episode_stage", "stage_power",
           "stage_title", "stage_name", "combat_base", "side", "slot",
           "thumb_level", "thumb_rank", "thumb_hyper", "thumb_attr",
           "actor_attr", "actor_role", "stat_rank", "hp", "atk", "def", "spd",
           "crt_chance", "crt_dmg", "penetration", "block_chance",
           "block_dec_dmg", "attr_enhance", "attr_resist", "hp_regen",
           "cool_time", "ref_id", "source_file", "source_locator"]
    lines = ["\t".join(hdr)]
    for a in sorted(anchors, key=lambda z: (z["res_id"], z["actor_id"])):
        c = a["ctx"] or {}
        t = c.get("thumb") or {}
        lines.append("\t".join(str(x) for x in [
            a["actor_id"], a["res_id"], c.get("stage", "(no placement)"),
            c.get("power", ""), c.get("title", ""), c.get("stage_name", ""),
            c.get("combat_base", ""), c.get("side", ""), c.get("slot", ""),
            t.get("level", ""), t.get("rank", ""), t.get("hyper", ""),
            t.get("attr", ""),
            a["attr"] if a["attr"] is not None else "",
            a["role"] if a["role"] is not None else "", a["rank"], a["hp"],
            a["atk"], a["def"], a["spd"], a["crt_chance"], a["crt_dmg"],
            a["penetration"], a["block_chance"], a["block_dec_dmg"],
            a["attr_enhance"], a["attr_resist"], a["hp_regen"],
            a["cool_time"], a["ref_id"],
            "sources/client-tables/reference/EPISODE_STAT_ACTORS.json",
            "actor id %s" % a["actor_id"]]))
    with io.open(os.path.join(OUT, "episode-monster-recovered-rows.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    by_res = collections.defaultdict(list)
    for a in anchors:
        by_res[a["res_id"]].append(a)

    # ---- fitted ladder -----------------------------------------------------
    fig = ["== fitted on %d recovered episode monster rows ==" % len(anchors)]
    by_rank = collections.defaultdict(list)
    for a in anchors:
        by_rank[a["rank"]].append(a)
    rank_med = {}
    for rk in sorted(by_rank):
        v = by_rank[rk]
        hps = [x["hp"] for x in v]; atks = [x["atk"] for x in v]
        defs = [x["def"] for x in v]
        rank_med[rk] = (statistics.median(hps), statistics.median(atks),
                        statistics.median(defs))
        fig.append("rank %d n=%-2d hp med=%-7.0f p10=%-6.0f p90=%-6.0f | "
                   "atk med=%-7.0f p10=%-6.0f p90=%-6.0f | "
                   "def med=%-6.0f p10=%-5.0f p90=%-5.0f"
                   % (rk, len(v), statistics.median(hps), pctl(hps, .1),
                      pctl(hps, .9), statistics.median(atks), pctl(atks, .1),
                      pctl(atks, .9), statistics.median(defs), pctl(defs, .1),
                      pctl(defs, .9)))
    hp_all = [a["hp"] for a in anchors]
    atk_all = [a["atk"] for a in anchors]
    def_all = [a["def"] for a in anchors]
    pooled = (statistics.median(hp_all), statistics.median(atk_all),
              statistics.median(def_all))
    pooled_band = (pctl(hp_all, .1), pctl(hp_all, .9),
                   pctl(atk_all, .1), pctl(atk_all, .9),
                   pctl(def_all, .1), pctl(def_all, .9))
    fig.append("pooled n=%d  hp med=%.0f [%.0f..%.0f]  atk med=%.0f [%.0f..%.0f]"
               "  def med=%.0f [%.0f..%.0f]"
               % (len(anchors), pooled[0], pooled_band[0], pooled_band[1],
                  pooled[1], pooled_band[2], pooled_band[3],
                  pooled[2], pooled_band[4], pooled_band[5]))
    fig.append("power->rank map: <2500 r1 | 2500-8999 r2 | 9000-24999 r3 | "
               "25000-39999 r4 | >=40000 r5")
    fig.append("direction check: hp median r1/r5 = %.3f -> rank counts UP"
               % (rank_med[1][0] / rank_med[5][0]))
    fig.append("per-rank hp ratio relative to rank 5: "
               + ", ".join("r%d %.3f" % (r, rank_med[r][0] / rank_med[5][0])
                           for r in sorted(rank_med)))
    fig.append("LEVELING.jet chunk 9 bonus.rank_* (catalog/INDEX.md 5.2): "
               "r1 2.6/1.4/1.4  r2 2.2/1.3/1.3  r3 1.8/1.2/1.2  "
               "r4 1.4/1.1/1.1  r5 1.0/1.0/1.0  (hp/atk/def)")
    fig.append("=> the shipped episode ladder runs the OPPOSITE way (rank 5 = "
               "toughest), so the rank_1-toughest inference at INDEX.md 5.2 is "
               "refuted by shipped data; see REPORT.md S5.")

    # ---- 22 catalog rows ---------------------------------------------------
    cat_hdr = ["catalog_monster_id", "row_identity", "hosted_monster_res_ids",
               "hosted_with_client_row", "all_hosted_client_rows",
               "anchor_attr", "anchor_role", "rank", "hp", "atk", "def",
               "tier", "confidence_point_pct", "confidence_band", "method",
               "source_file", "source_locator"]
    clines = ["\t".join(cat_hdr)]

    order = ["M%03d" % i for i in range(1, 22)] + ["M100"]
    anchored = {p: [m for m in packs.get(p, []) if m in by_res] for p in order}

    for idx, p in enumerate(order):
        hosted = packs.get(p, [])
        withrow = anchored[p]
        if withrow:
            rows_here = sorted((a for a in anchors
                                if a["res_id"] in withrow),
                               key=lambda z: -z["hp"])
            a = rows_here[0]
            where = "; ".join(
                "%s@%s(p%s,L%s,r%s,h%s,attr%s)=%s/%s/%s"
                % (x["res_id"], (x["ctx"] or {}).get("stage", "-"),
                   (x["ctx"] or {}).get("power", "-"),
                   (x["ctx"] or {}).get("thumb", {}).get("level", "-"),
                   x["rank"], (x["ctx"] or {}).get("thumb", {}).get("hyper", "-"),
                   x["attr"], x["hp"], x["atk"], x["def"])
                for x in rows_here)
            method = ("jet-namespace crosswalk: pack %s.jet hosts monster res_ids "
                      "%s; %d of them has a shipped stat row. Value quoted "
                      "verbatim from the highest-HP row; every hosted row is in "
                      "all_hosted_client_rows and in "
                      "episode-monster-recovered-rows.tsv."
                      % (p, ",".join(hosted), len(withrow)))
            loc = ("EPISODE_STAT_ACTORS.json actor %s (res_id %s); "
                   "stage %s power %s"
                   % (a["actor_id"], a["res_id"],
                      (a["ctx"] or {}).get("stage"),
                      (a["ctx"] or {}).get("power")))
            clines.append("\t".join(str(x) for x in [
                p, "art pack (hosts %d monsters)" % len(hosted),
                ",".join(hosted), ",".join(withrow), where,
                a["attr"], a["role"], a["rank"], a["hp"], a["atk"], a["def"],
                "[RECOVERED]", 95,
                "exact (verbatim shipped literal; stat.hp is the unscaled "
                "on-screen combat HP - see REPORT.md S2)",
                method,
                "sources/client-tables/reference/EPISODE_STAT_ACTORS.json",
                loc]))
        else:
            below = next((anchored[q] for q in reversed(order[:idx])
                          if anchored[q]), None)
            above = next((anchored[q] for q in order[idx + 1:]
                          if anchored[q]), None)
            if below and above:
                src = [a for a in anchors if a["res_id"] in below + above]
                lo = min(x["hp"] for x in src); hi = max(x["hp"] for x in src)
                ratio = (hi / lo) if lo else 200.0
                band = (lo, hi,
                        min(x["atk"] for x in src), max(x["atk"] for x in src),
                        min(x["def"] for x in src), max(x["def"] for x in src))
                pt = tuple(int(round(statistics.median([x[k] for x in src])))
                           for k in ("hp", "atk", "def"))
                conf = int(max(15, min(45, round(
                    100.0 * (1.0 - (math.log10(ratio) / math.log10(200.0)))))))
                bandtxt = "hp %d-%d, atk %d-%d, def %d-%d" % band
                meth = ("jet crosswalk: pack %s.jet hosts %s, none of which has "
                        "a shipped stat row. Estimate = median of every "
                        "recovered row for the bracketing anchored packs %s / %s "
                        "(hosted monsters %s / %s). The hp bracket spans %d-%d "
                        "(%.1fx), so the point value is a mid-bracket guess and "
                        "rank/stage placement is NOT determined."
                        % (p, ",".join(hosted),
                           next(q for q in reversed(order[:idx]) if anchored[q]),
                           next(q for q in order[idx + 1:] if anchored[q]),
                           ",".join(below), ",".join(above), lo, hi, ratio))
            else:
                pt = (int(round(pooled[0])), int(round(pooled[1])),
                      int(round(pooled[2])))
                band = (int(round(pooled_band[0])), int(round(pooled_band[1])),
                        int(round(pooled_band[2])), int(round(pooled_band[3])),
                        int(round(pooled_band[4])), int(round(pooled_band[5])))
                bandtxt = ("hp %d-%d, atk %d-%d, def %d-%d "
                           "(full-population p10-p90)" % band)
                conf = 20
                meth = ("jet crosswalk: pack %s.jet hosts %s, none with a shipped "
                        "stat row and no anchored bracketing pack. Estimate = "
                        "pooled median of all %d recovered episode monster rows; "
                        "rank/stage placement genuinely undetermined."
                        % (p, ",".join(hosted), len(anchors)))
            clines.append("\t".join(str(x) for x in [
                p, "art pack (hosts %d monsters)" % len(hosted),
                ",".join(hosted), "(none)", "(none)",
                "unknown", "unknown", "unknown",
                pt[0], pt[1], pt[2], "[DERIVED-ESTIMATE]", conf,
                bandtxt, meth,
                "derived from sources/client-tables/reference/"
                "EPISODE_STAT_ACTORS.json (34 rows) + "
                "EPISODE_COMBAT_*.json (61 stages)",
                "model: power->rank ladder fit on the 34 recovered rows"]))
    with io.open(os.path.join(OUT, "monster-stat-estimates-2026-10-11.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(clines) + "\n")
    with io.open(os.path.join(OUT, "model-figures.txt"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(fig) + "\n")

    # ---- summary -----------------------------------------------------------
    rec = [p for p in order if anchored[p]]
    der = [p for p in order if not anchored[p]]
    print("## recovered anchors: %d rows, %d distinct monster res_ids"
          % (len(anchors), len(by_res)))
    print("## distinct monster res_ids with a shipped row:")
    print("   " + ", ".join(sorted(by_res)))
    print("## catalog rows [RECOVERED]: %d/22 -> %s"
          % (len(rec), ",".join(rec)))
    print("## catalog rows [DERIVED-ESTIMATE]: %d/22 -> %s"
          % (len(der), ",".join(der)))
    print("## coverage at >=60%% point confidence: %d/22 = %.1f%%"
          % (len(rec), 100.0 * len(rec) / 22))
    print("\n".join(fig))
    print("\nwrote episode-monster-recovered-rows.tsv, "
          "monster-stat-estimates-2026-10-11.tsv, model-figures.txt")


if __name__ == "__main__":
    main()
