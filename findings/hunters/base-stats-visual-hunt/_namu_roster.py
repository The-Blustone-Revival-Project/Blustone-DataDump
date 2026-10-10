# -*- coding: utf-8 -*-
"""Extract the namu 헌터 role tables into a structured hero roster, then
cross-check 속성(element) and 태생 등급(birth grade) against the 2019 JP archive.

The Korean->catalog_id map is authored by reading the rendered Korean and is
stored explicitly in KOREAN_TO_ID so it can be audited; the Korean strings are
taken verbatim from the rendered DOM, never retyped by hand into the roster.
"""
import io
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = os.path.join(os.environ.get("TEMP", "."), "namu_hunter_tables.json")
ARCHIVE = os.path.join(os.environ.get("TEMP", "."), "namu_archive.json")

# role table index -> (role_en, role_ko)
ROLE_TABLES = {13: ("Offense", "공격수"), 14: ("Defense", "수비수"),
               15: ("Bomber", "폭격수"), 16: ("Support", "도우미")}

# Korean hero label (as printed in the name cell, stripped of its title prefix)
# -> catalog_id. Authored from the rendered Korean; verified against the
# project's cards.json English names below.
KOREAN_TO_ID = {
    # --- 공격수 Offense (table 13)
    "변절자 빈센트": "010", "정체불명의 쌍둥이 릴리&랄라": "047",
    "파이트클럽의 수호자 백헨": "051", "혹한의 마녀 옥타비아": "028",
    "고귀한 창 나탈리아": "037", "은반의 요정 유리": "045",
    "특급 전령사 헤르메스": "023", "두 얼굴의 소녀 하이디": "044",
    "불멸의 칼슈타이너": "061", "늑대아이 비비": "040",
    "산타걸 레베카": "038", "나쁜아이 사냥꾼 산타클로스터": "042",
    "사라진 숲의 모글리": "002", "방랑 격투가 스카": "032",
    "황혼의 방망이단 레베카": "021", "쾌속의 검술가 라피스": "017",
    "방랑 검객 발리안": "019", "사라지지 않는 노병 실베스터": "006",
    # --- 수비수 Defense (table 14)
    "정의로운 자 할리": "046", "강철의 레버넌트 칼리버": "053",
    "전설적인 말썽꾸러기 네네": "003", "강철의 보디가드 카인": "029",
    "전장의 불꽃 아테나": "027", "대자연의 선물 곰": "036",
    "기이한 노인 덤블": "048", "로봇 공학자 에드워드": "041",
    "희대의 탈옥수 빠삐용": "043", "불굴의 제라드": "005",
    "거친 인생 리코": "024", "할로윈 마녀 리코": "078",
    "생존술의 대가 로빈": "018", "지키는자 헤카테": "011",
    "캡틴": "009",
    # --- 폭격수 Bomber (table 15)
    "천재 기후학자 디노": "054", "최초의 헌터 랜턴": "001",
    "조용한 송곳니 파트로네": "033", "천둥 화살 디아나": "031",
    "비행선 관리원 걸베이그": "039", "중위 레비": "015",
    "공포의 곰인형 테디보머": "025",
    "로크 앤 캐쉬 CEO 로크": "014",
    "오늘도 화끈한 메티스": "007", "화력덕후 시에나": "020",
    # --- 도우미 Support (table 16)
    "도망친 신부 테레사": "065", "마성의 물리치료사 테라피": "050",
    "성냥팔이 소년 브라이트": "049", "동물 애호가 팬지": "057",
    "강령술사 크로커스": "058", "신목의 무녀 아카샤": "008",
    "걸어다니는 진료실 조이": "035", "청결의 요정 데날리": "013",
    "식물학자 아세로라": "030", "데스메탈 전도사 브루스방": "016",
    # deliberately unresolved: no unambiguous catalog id, see report
    "실험체 2호 해선": "", "최고의 요리사 치르치르": "",
    "이상한 나라의 치르치르": "",
}

# namu element token -> canonical English
ELEM_NAMU = {"전속": ("Lightning", "전격"),
             "수속": ("Ice", "냉기"),
             "화속": ("Fire", "화염")}
# archive element_ja -> canonical English
ELEM_ARCHIVE = {"電撃": "Lightning", "冷気": "Ice", "火炎": "Fire"}

TITLE_RE = re.compile(r"^(변절자|정체불명의 쌍둥이|파이트클럽의 수호자|혹한의 마녀|고귀한 창|"
                      r"은반의 요정|특급 전령사|두 얼굴의 소녀|불멸의|늑대아이|산타걸|"
                      r"나쁜아이 사냥꾼|사라진 숲의|방랑 격투가|황혼의 방망이단|쾌속의 검술가|"
                      r"방랑 검객|사라지지 않는 노병|정의로운 자|강철의 레버넌트|"
                      r"전설적인 말썽꾸러기|강철의 보디가드|전장의 불꽃|대자연의 선물|"
                      r"기이한 노인|로봇 공학자|희대의 탈옥수|불굴의|거친 인생|할로윈 마녀|"
                      r"생존술의 대가|지키는자|천재 기후학자|최초의 헌터|조용한 송곳니|"
                      r"천둥 화살|비행선 관리원|중위|공포의 곰인형|록 앤 캐쉬 CEO|"
                      r"오늘도 화끈한|화력덕후|도망친 신부|마성의 물리치료사|성냥팔이 소년|"
                      r"동물 애호가|강령술사|신목의 무녀|걸어다니는 진료실|실험체 2호|"
                      r"청결의 요정|식물학자|데스메탈 전도사|최고의 요리사|이상한 나라의)")


def star_count(cell):
    """namu writes the birth grade as a run of ☆ glyphs; a damaged row shows
    two runs separated by whitespace ('☆☆ ☆☆'). Count both."""
    return cell.count("☆") + cell.count("★")


def load_cards():
    p = os.path.join(HERE, "..", "..", "catalogue", "data", "cards.json")
    p = os.path.normpath(p)
    d = json.load(io.open(p, encoding="utf-8"))
    return {c["card_id"]: c for c in d}


def main():
    tables = {t["index"]: t for t in json.load(io.open(TABLES, encoding="utf-8"))}
    arch = {h["id"]: h for h in json.load(io.open(ARCHIVE, encoding="utf-8"))["heroes"]}
    cards = load_cards()

    roster = []
    for idx in sorted(ROLE_TABLES):
        role_en, role_ko = ROLE_TABLES[idx]
        t = tables[idx]
        for r_i, row in enumerate(t["rows"]):
            if r_i == 0:
                continue
            grade_cell = row[0].strip()
            elem_cell = row[1].strip()
            name_cell = row[2].strip()
            if not name_cell:
                continue
            name_clean = re.sub(r"\s*\[\d+\]\s*$", "", name_cell).strip()
            cid = KOREAN_TO_ID.get(name_clean, "")
            stars = star_count(grade_cell)
            # The namu star badge is split into more than one DOM run for some
            # rows ('☆☆ ☆☆'), so the grade is the TOTAL glyph count across
            # runs. namu's own prose independently confirms 4성 for both of the
            # rows that render this way (Vincent, Lily&Lyla).
            grade_n = stars
            elem_en, elem_ko = ELEM_NAMU.get(elem_cell, ("?", "?"))
            a = arch.get(cid)
            a_elem = ELEM_ARCHIVE.get(a["element_ja"], "?") if a else None
            c = cards.get(cid) if cid else None
            c_elem = c["element"] if c else None
            roster.append({
                "table": idx, "role_en": role_en, "role_ko": role_ko,
                "row": r_i,
                "grade_raw": grade_cell, "grade_stars": grade_n,
                "elem_raw": elem_cell, "elem_en": elem_en, "elem_ko": elem_ko,
                "name_ko": name_cell, "name_ko_clean": name_clean,
                "catalog_id": cid,
                "name_en": c["name"] if c else None,
                "catalogue_element_en": c_elem,
                "catalogue_role_en": c["role"] if c else None,
                "catalogue_rarity": c["rarity"] if c else None,
                "archive_present": a is not None,
                "archive_element_en": a_elem,
                "archive_rarity": a["rarity"] if a else None,
                "archive_role_ja": a["role_ja"] if a else None,
                "archive_hp": a["hp"] if a else None,
                "archive_atk": a["atk"] if a else None,
                "archive_def": a["def"] if a else None,
                "element_agrees": (a_elem is None or a_elem == elem_en) if a else None,
                "element_agrees_catalogue": (c_elem is None or c_elem == elem_en) if c else None,
                "role_agrees_catalogue": (c is None or c["role"] == role_en),
            })

    out = os.path.join(os.environ.get("TEMP", "."), "namu_roster.json")
    io.open(out, "w", encoding="utf-8", newline="\n").write(
        json.dumps(roster, ensure_ascii=False, indent=1))

    print("roster rows: %d" % len(roster))
    by_role = {}
    for h in roster:
        by_role.setdefault(h["role_en"], []).append(h)
    for r, hs in by_role.items():
        print("  %-8s %d" % (r, len(hs)))
    unmapped = [h["name_ko_clean"] for h in roster if not h["catalog_id"]]
    print("unmapped to catalog id: %d %s" % (len(unmapped), unmapped))

    # Mapping audit: namu vs the project catalogue (cards.json).
    mapped = [h for h in roster if h["catalog_id"]]
    ce = [h for h in mapped if h["element_agrees_catalogue"] is False]
    cr = [h for h in mapped if h["role_agrees_catalogue"] is False]
    print("MAPPING AUDIT vs cards.json: mapped=%d  element mismatch=%d  role mismatch=%d"
          % (len(mapped), len(ce), len(cr)))
    for h in ce + cr:
        print("  MAP-DISAGREE id=%s %-24s namu=%s/%s  catalogue=%s/%s"
              % (h["catalog_id"], h["name_ko_clean"], h["elem_en"], h["role_en"],
                 h["catalogue_element_en"], h["catalogue_role_en"]))

    both = [h for h in roster if h["archive_present"]]
    dis = [h for h in both if h["element_agrees"] is False]
    print("cross-checkable vs 2019 archive: %d   element DISAGREEMENTS: %d" % (len(both), len(dis)))
    for h in dis:
        print("  DISAGREE id=%s ko=%s en=%s namu=%s catalogue=%s archive=%s"
              % (h["catalog_id"], h["name_ko_clean"], h["name_en"],
                 h["elem_en"], h["catalogue_element_en"], h["archive_element_en"]))
    gd = [h for h in both
          if h["archive_rarity"].isdigit()
          and h["grade_stars"] != int(h["archive_rarity"])]
    print("grade DISAGREEMENTS: %d" % len(gd))
    for h in gd:
        print("  GRADE id=%s ko=%s namu=%s* archive=%s*" %
              (h["catalog_id"], h["name_ko_clean"], h["grade_stars"],
               h["archive_rarity"]))
    print("wrote", out)


if __name__ == "__main__":
    main()
