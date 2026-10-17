"""Build the accessory main-stat estimate table for the 100 distinct accessory
names in the shipped Blustone catalogue.

Model (full derivation in REPORT.md):

  M1 shape   : main_stat(L) = base + up * L          (linear in item level;
               shape-identical to the recovered native card-stat helper
               uint32(base + up*level) * multiplier, STATS-ESTIMATE-2026-10-08 §158)
  M2 scope   : the main stat is a function of SLOT x ITEM LEVEL, not of the
               item and not of the owning hero's rarity.
               Evidence: two unrelated armours on heroes of different rarity
               (Chicken Wings, Beckhen 051 3-star, panel DEF 102 @ Lv.50) and
               (Purple Combat Coat, Vincent 010 4-star, upgrade-preview
               DEF 101 @ Lv.49 -> 102 @ Lv.50) agree exactly.
  M3 armour  : DEF(L) = 52 + L exactly (same-item two-point fit, 101 @ 49 and
               102 @ 50 on faq-image07).
  M4 transfer: keep the armour's normalised increments - base/MAX = 52/102 and
               up/MAX = 1/102 - and apply them to the accessory cap MAX = 260
               (Jack, faq-image21).  This reproduces the armour curve exactly.

Read-only with respect to every source file; writes only inside this lane.
"""

from __future__ import annotations

import io
import os

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

CARD_CATALOGUE = os.path.join(REPO, "catalog", "legacy-catalogue-data", "card-catalogue.tsv")
CHARSTR_ITEMS = os.path.join(REPO, "findings", "hunters", "base-stats-visual-hunt",
                             "charstr-items-2026-10-06.tsv")
CROSSWALK = os.path.join(REPO, "findings", "hunters", "base-stats-visual-hunt",
                         "miraheze-equipment-crosswalk-2026-10-06.tsv")

# ---------------------------------------------------------------- curve model
ACCESSORY_CAP = 260          # Jack, Max HP at Lv.50, faq-image21  [RECOVERED]
ARMOUR_CAP = 102             # Chicken Wings DEF at Lv.50, faq-image20 [RECOVERED]
ARMOUR_UP = 1                # Purple Combat Coat DEF 101 -> 102, faq-image07
ARMOUR_BASE = ARMOUR_CAP - 50 * ARMOUR_UP      # 52

FRAC_UP = ARMOUR_UP / ARMOUR_CAP               # 0.009804  per level, per cap point
FRAC_BASE = 1.0 - 50 * FRAC_UP                 # 0.509804


def curve(level: int, cap: int = ACCESSORY_CAP) -> int:
    """M4: cap * (FRAC_BASE + FRAC_UP * level), rounded."""
    return int(round(cap * (FRAC_BASE + FRAC_UP * level)))


def slope_from_point(level: int, value: int, cap: int = ACCESSORY_CAP) -> float:
    return (cap - value) / (50 - level)


# Hard bounds on the per-level slope, from the one independent accessory reading
# (faq-image08, accessory at Lv.20, entire HP equipment delta +221):
#   the accessory's own contribution can never exceed the whole delta, so
#   acc(20) <= 221  =>  up >= (260-221)/30 = 1.300
#   a linear curve must stay non-negative at Lv.1  =>  up <= 260/50 = 5.200
SLOPE_MIN = slope_from_point(20, 221)          # 1.3
SLOPE_MAX = ACCESSORY_CAP / 50.0               # 5.2
BASE_MIN = ACCESSORY_CAP - 50 * SLOPE_MAX      # 0
BASE_MAX = ACCESSORY_CAP - 50 * SLOPE_MIN      # 195


def read_tsv(path: str) -> list:
    return [line.split("\t") for line in
            io.open(path, encoding="utf-8").read().split("\n") if line.strip()]


def build_rows() -> list:
    cards = read_tsv(CARD_CATALOGUE)
    header = cards[0]
    idx = {name: i for i, name in enumerate(header)}
    i_acc = idx["accessory"]

    charstr = read_tsv(CHARSTR_ITEMS)
    cidx = {name: i for i, name in enumerate(charstr[0])}
    shipped_locales = {}
    for row in charstr[1:]:
        en = row[cidx["accessory_en"]].strip()
        if not en:
            continue
        shipped_locales[en] = {
            "num": row[cidx["num"]].strip(),
            "ja": row[cidx["accessory_ja"]].strip(),
            "ko": row[cidx["accessory_ko"]].strip(),
            "sc": row[cidx["accessory_sc"]].strip(),
            "tc": row[cidx["accessory_tc"]].strip(),
        }

    cross = read_tsv(CROSSWALK)
    xidx = {name: i for i, name in enumerate(cross[0])}
    wiki_owners = {}
    wiki_in_shipped = {}
    for row in cross[1:]:
        if row[xidx["slot"]].strip() != "Accessory":
            continue
        name = row[xidx["wiki_name"]].strip()
        wiki_owners[name] = row[xidx["heroes"]].strip()
        wiki_in_shipped[name] = row[xidx["in_shipped_2_8_0_1_CHARSTR"]].strip()

    # accessory -> list of (card_id, card_name, rarity, role)
    owners: dict = {}
    for row in cards[1:]:
        name = row[i_acc].strip()
        if not name:
            continue
        owners.setdefault(name, []).append({
            "card_id": row[idx["card_id"]].strip(),
            "name": row[idx["name"]].strip(),
            "rarity": row[idx["rarity"]].strip(),
            "role": row[idx["role"]].strip(),
        })

    out = []
    for name in sorted(owners, key=lambda n: n.lower()):
        entries = sorted(owners[name], key=lambda e: e["card_id"])
        locales = shipped_locales.get(name)
        shipped_num = locales["num"] if locales else ""
        rarities = sorted({e["rarity"] for e in entries if e["rarity"]}, key=lambda r: int(r))
        roles = sorted({e["role"] for e in entries if e["role"]})
        card_ids = ";".join(e["card_id"] for e in entries)
        card_names = ";".join(e["name"] for e in entries)
        wiki = wiki_owners.get(name, "")
        in_shipped = wiki_in_shipped.get(name, "")

        if name == "Jack":
            tier = "T1"
            klass = "[RECOVERED]"
            point = 100
            band = 0
            method = ("printed accessory panel: faq-image21 shows Jack 50/50 with "
                      "Max HP 260; cross-checked inside the same build "
                      "(260 + jewel HP 58+21+58+18+21 = 436 vs observed +437)")
            lv1 = curve(1)
            lv50 = ACCESSORY_CAP
            conf_note = "exact printed value; no model applied"
        elif shipped_num:
            tier = "T2"
            klass = "[DERIVED-ESTIMATE]"
            point = 85
            band = 20
            method = ("M1-M4 slot-level curve: Max HP(L) = round(260*(0.509804 + "
                      "0.009804*L)); Lv.50 anchored on Jack, increments inherited "
                      "from the exact armour pair 101@49 -> 102@50; rarity "
                      "independence from 3-star Beckhen vs 4-star Vincent armours")
            lv1 = curve(1)
            lv50 = curve(50)
            conf_note = "point 85 = slot-wide model on 2 cross-rarity items; band +-20%"
        else:
            tier = "T3"
            klass = "[DERIVED-ESTIMATE]"
            point = 80
            band = 25
            method = ("same M1-M4 slot-level curve; item identity from the live-wiki "
                      "equipment crosswalk + card catalogue only (absent from the "
                      "shipped 105-record CHAR_STR accessory column, "
                      "in_shipped_2_8_0_1_CHARSTR=NO)")
            lv1 = curve(1)
            lv50 = curve(50)
            conf_note = "point 80 = T2 minus 5 for identity provenance"

        loc = "datasets/hunters/observed-stats/found/faq-image21-gear-accessory-jack.png"
        if shipped_num:
            locator = ("%s ; CHAR_STR_RO|%s|ACCESSORY ; "
                       "catalog/legacy-catalogue-data/card-catalogue.tsv %s"
                       % (loc, shipped_num, card_ids))
        else:
            locator = ("findings/hunters/base-stats-visual-hunt/miraheze-equipment-crosswalk-"
                       "2026-10-06.tsv Accessory/%s ; card-catalogue.tsv %s"
                       % (name, card_ids))

        notes = []
        if len(entries) > 1:
            notes.append("accessory shared by %d catalogue rows (%s)"
                         % (len(entries), card_ids))
        if len(rarities) > 1:
            notes.append("owners span rarity %s - slot-level model asserted "
                         "rarity-invariant (armour 102 on 3-star and 4-star heroes)"
                         % "/".join(rarities))
        if not shipped_num:
            notes.append("awakened-form accessory; not in shipped CHAR_STR")
        if wiki:
            notes.append("live-wiki owner(s): %s" % wiki)
        if roles:
            notes.append("owner role(s): %s" % "/".join(roles))

        out.append({
            "item_name_en": name,
            "item_name_ja": (locales or {}).get("ja", ""),
            "item_name_ko": (locales or {}).get("ko", ""),
            "item_name_sc": (locales or {}).get("sc", ""),
            "item_name_tc": (locales or {}).get("tc", ""),
            "charstr_num": shipped_num,
            "owning_card_ids": card_ids,
            "owning_heroes": card_names,
            "wiki_owner_names": wiki,
            "slot": "Accessory",
            "hero_rarity": "/".join(rarities),
            "main_stat": "Max HP",
            "max_hp_lv1": lv1,
            "max_hp_lv50": lv50,
            "max_hp_lv50_band_low": int(round(lv50 * (1 - band / 100.0))),
            "max_hp_lv50_band_high": int(round(lv50 * (1 + band / 100.0))),
            "tier": tier,
            "class": klass,
            "confidence_point_pct": point,
            "confidence_band_pct": band,
            "confidence_note": conf_note,
            "method": method,
            "source_locator": locator,
            "notes": "; ".join(notes),
        })
    return out


COLUMNS = [
    "item_name_en", "item_name_ja", "item_name_ko", "item_name_sc", "item_name_tc",
    "charstr_num", "owning_card_ids", "owning_heroes", "wiki_owner_names", "slot",
    "hero_rarity", "main_stat", "max_hp_lv1", "max_hp_lv50",
    "max_hp_lv50_band_low", "max_hp_lv50_band_high", "tier", "class",
    "confidence_point_pct", "confidence_band_pct", "confidence_note", "method",
    "source_locator", "notes",
]


def main() -> None:
    rows = build_rows()
    lines = ["\t".join(COLUMNS)]
    for row in rows:
        lines.append("\t".join(str(row[c]).replace("\t", " ").replace("\n", " ")
                               for c in COLUMNS))
    dest = os.path.join(LANE, "accessory-stat-estimates-2026-10-11.tsv")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")

    # curve table for the report
    curve_lines = ["level\tmax_hp\tdef_armour\tatk_weapon"]
    for level in range(1, 51):
        curve_lines.append("%d\t%d\t%d\t%d" % (
            level, curve(level),
            int(round(ARMOUR_CAP * (FRAC_BASE + FRAC_UP * level))),
            int(round(134 * (FRAC_BASE + FRAC_UP * level)))))
    with io.open(os.path.join(LANE, "per-level-curve.tsv"), "w",
                 encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(curve_lines) + "\n")

    counts = {}
    for row in rows:
        counts[row["tier"]] = counts.get(row["tier"], 0) + 1
    print("rows:", len(rows), "tiers:", counts)
    print("slope band: %.3f .. %.3f ; base band: %.1f .. %.1f"
          % (SLOPE_MIN, SLOPE_MAX, BASE_MIN, BASE_MAX))
    print("curve L1/L20/L50:", curve(1), curve(20), curve(50))
    print("wrote", dest)


if __name__ == "__main__":
    main()
