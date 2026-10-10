# Jewel set-bonus help locales — `CONTENTS11_8`, 1.4.4.1 vs 2.8.0.1 (2026-10-05)

Full per-locale transcription of the in-game **jewel set-effect help table**
(`UI_CSV` help record `CONTENTS11_8`, resource `G_LI11_8`) from the two shipped
APK generations, plus the impure rebalance reading of its bonus numerals.

**Read-only.** No server change, no APK change, no rebuild, no release, no
catalogue edit, no emulator operation. Nothing was written outside this file and
the `polluted-observations.md` append.

**No coverage credit.** This is help/UI **copy**, i.e. *set-bonus definitions*,
never a per-jewel-instance stat row. Strict coverage is unchanged at
**heroes 1/113, accessories 1/100, monsters 0/22** (`coverage.md`). §2 is
explicitly impure rebalance material.

Scope: `apk-diff-2026-10-05.md` §4 reported the English `desc2` rewrite. This
file does the **whole record in every shipped locale**, resolves the exact
locale divergence, and **corrects two claims** in that section (see §1.6 and
§2.5).

---

## 0. Provenance, decoding, and offset conventions

### 0.1 The two sources

| | 1.4.4.1 | 2.8.0.1 |
|---|---|---|
| Path | `analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/3d98d128.json` | `analysis/extracted/assets/UI_CSV.jet` |
| Size | **187,121 B** | **93,380 B** (compressed; the 8 resources sum to **343,322 B** inflated as recomputed here — `apk-diff-2026-10-05.md` §4 cites 343,329 B, a 7 B discrepancy in the earlier count, irrelevant to every value below) |
| SHA-256 | `ce32b2fffb0f7da7a391b46e3b9be40587cb2d02c2733457dd36442d5fe786c4` | `73a9dc4755baf8eb84c3fa945b7dd8b10228fe73d47a945de27137de2c84dac8` |
| Shape | plain JSON array, **157** records, CRLF | JET container, **8** logical `RW` resources; the category list is one 288,762 B `RW` body, **205** records |
| Line endings | `\r\n` | `\r\n` |

The 2.8.0.1 `RW` body that carries this record:
size **288,762 B**, SHA-256
`730070894cb69ccbfc85bbaa3d44de5ed8dbb8238081d91ab196a2716eb6b754`,
inflated-stream offset **540** within `UI_CSV.jet`.

### 0.2 Decoding — correction to a prior limitation claim

`apk-diff-2026-10-05.md` §9 states the CJK in **both** UI_CSV generations is
mojibake under the tooling, because the old bytes were read as CP949/EUC-KR.
**That is wrong for these files, and the KO/Super-Block 9% reading did not need
numeral-position inference.**

- The 1.4.4.1 help JSON is **valid UTF-8 over all 187,121 bytes**
  (187,121 B → 123,987 chars; zero undecodable bytes). CP949 and EUC-KR both
  *fail* on it at byte 113 (`0xed`). The earlier "mojibake" was a CP1252 read
  artefact.
- The 2.8.0.1 help records are UTF-8 too (a UTF-8 BOM appears on the resource
  that begins with CJK, resource[6]).
- Consequently **every locale line below is transcribed in its real script**,
  not as numeral-only fragments.

### 0.3 Offset conventions

- **1.4.4.1 offsets are true on-disk byte offsets** into the plain JSON file.
- **2.8.0.1 offsets are byte offsets into the 288,762 B inflated `RW` body**,
  pointing at the opening quote of each string value. They are **not** on-disk
  offsets: that body lives inside a zlib stream starting at `UI_CSV.jet` offset
  540 and is therefore not byte-addressable in the container.
- Value offsets are the opening `"` of each JSON string value.

### 0.4 Structural notes

- `CONTENTS11_8` is the **last record** of the 1.4.4.1 array (record anchor at
  char 121,065; array closes at EOF). In 2.8.0.1 it is also last
  (record anchor at char 147,345 of the `RW` body).
- Record keys are identical in both versions and in the same order:
  `type`, `id`, `res`, `title`, `desc1`, `desc2`. `type` = `contents`,
  `res` = `G_LI11_8`.
- Locale keys were renamed only: `ko/en/jp/zh/zt` → **`KO/EN/JA/SC/TC`**
  (`zh`→`SC`, `zt`→`TC`, `jp`→`JA`). Order is preserved.
- **Whole-file `json.loads` fails on the 1.4.4.1 corpus** at the final `]`
  (char 123,986 of 123,987; no raw control characters anywhere). Values were
  therefore extracted per-string with `JSONDecoder.raw_decode`. This is a
  property of the shipped corpus, not a tooling defect, and it is recorded
  rather than "fixed".
- Sibling `G_LI11_*` help records exist for both versions: old
  `CONTENTS11_1..11_8` (8), new `CONTENTS11_1`, `11_4`, `11_5`, `11_6`,
  `11_7`, `11_8` (6). **Bounded check:** only `CONTENTS11_8` carries any
  set-bonus numeral. The other five differ between versions only by introduced
  `<size='29'>` / `<color='241,26,90,255'>` markup numerals, so no other
  jewel-help bonus value was revised. See §2.7.

---

# SECTION 1 — PURE TRANSCRIPTION

Pure = the literal shipped bytes, per locale, with offsets. No interpretation,
no era tags, no deltas. All interpretive material is quarantined in Section 2.

## 1.1 Title — **byte-identical in all five locales**

| old key | new key | value | old byte offset | new `RW`-body offset | identical |
|---|---|---|---|---|---|
| `ko` | `KO` | 생명의 결정 → `세트 효과` | 182,271 | 213,025 | yes (`49aa3c32…`) |
| `en` | `EN` | `Set Effect` | 182,303 | 213,055 | yes (`80eea210…`) |
| `jp` | `JA` | セット効果 | 182,332 | 213,082 | yes (`d502250b…`) |
| `zh` | `SC` | 套装效果 | 182,366 | 213,114 | yes (`985ed478…`) |
| `zt` | `TC` | 組合效果 | 182,397 | 213,143 | yes (`8ddeff76…`) |

All five title strings are unchanged across the version span.

## 1.2 `desc1` — the "how set effect works" rules text

No set-bonus numerals in either version. Old strings are plain text; new
strings introduce `<size>` / `<color>` markup and `\n\n` paragraph breaks.
Sizes/fingerprints for audit:

| pair | old chars / SHA-256 | new chars / SHA-256 | identical |
|---|---|---|---|
| `ko`→`KO` | 125 / `df2e3ce7…` | 211 / `2b5929bd…` | no |
| `en`→`EN` | 222 / `97d69912…` | 316 / `2b3f3fe7…` | no |
| `jp`→`JA` | 109 / `45ce95fa…` | 194 / `b0c6080e…` | no |
| `zh`→`SC` | 69 / `5197277f…` | 131 / `fc0bf324…` | no |
| `zt`→`TC` | 66 / `124aa6a0…` | 160 / `a075e0c9…` | no |

Offsets: old `ko` 182,454 / `en` 182,765 / `jp` 183,010 / `zh` 183,336 /
`zt` 183,549. New `KO` 213,195 / `EN` 213,592 / `JA` 213,931 / `SC` 214,344 /
`TC` 214,620.

**2.8.0.1 English `desc1` ships malformed markup** — an unmatched `</color>`
and a stray `</size>`:

```
<size='29'> • You can apply the set effect by </size>mounting the required number</color> of the same Jewels.</size>
```

Recorded as a transcription fact about the shipped string, not as a rendering
claim (no native render of this record was observed). The old English text was
markup-free. English wording also changed from
"mounting the same Jewels required" to
"mounting the required number of the same Jewels".

## 1.3 `desc2` — the set-bonus table, every locale, old → new

**Separator change (pure structural fact):** 1.4.4.1 separates the 12 entries
with a single `\n` (11 separators → 12 lines). 2.8.0.1 separates with `\n\n`
(11 double separators → 23 `\n`, 13 non-empty display lines for `KO`/`EN`/`JA`
because the `<color>` tag occupies its own line; 12 for `SC`/`TC` which carry no
tag). `SC` and `TC` also begin with one leading `\n`.

Trailing-whitespace, verbatim: old `zt` line 1 ends with a space; new `TC`
lines 2, 4, 6 and 12 (entries 1, 2, 3, 6) end with a space. No other locale
line has trailing whitespace in either version.

### 1.3.1 `ko` → `KO` — value **9%** old

| row | 1.4.4.1 `ko` (offset 183,779, 360 chars) | 2.8.0.1 `KO` (offset 214,942, 400 chars) |
|---|---|---|
| 1 | 생명의 결정 - 2개 장착 시, 생명력 5% 증가 | 생명의 결정 - 2개 장착 시, 생명력 6% 증가 |
| 2 | 공격의 결정 - 2개 장착 시, 공격력 5% 증가 | 공격의 결정 - 2개 장착 시, 공격력 6% 증가 |
| 3 | 방어의 결정 - 2개 장착 시, 방어력 5% 증가 | 방어의 결정 - 2개 장착 시, 방어력 6% 증가 |
| 4 | 치명의 결정 - 2개 장착 시, 치명타 확률 4.5% 증가 | **속도의 결정 - 4개 장착 시, 공격 속도 1.72 증가** (moved here) |
| 5 | 막기의 결정 - 2개 장착 시, 막기 확률 4.5% 증가 | 치명의 결정 - 2개 장착 시, 치명타 확률 6% 증가 |
| 6 | 충격의 결정 - 4개 장착 시, 치명타 피해량 50% 증가 | 충격의 결정 - 4개 장착 시, 치명타 피해량 60% 증가 |
| 7 | 철벽의 결정 - 4개 장착 시, **막기 피해량 9% 증가** | 속성의 결정 - 4개 장착 시, 속성 강화 35 증가 |
| 8 | 속성의 결정 - 4개 장착 시, 속성 강화 23 증가 | 관통의 결정 - 4개 장착 시, 관통력 16 증가 |
| 9 | 저항의 결정 - 4개 장착 시, 속성 저항 23 증가 | 막기의 결정 - 2개 장착 시, 막기 확률 5% 증가 |
| 10 | 속도의 결정 - 4개 장착 시, 공격 속도 1.72 증가 | 철벽의 결정 - 4개 장착 시, **피해 감소량 10% 증가** |
| 11 | 재생의 결정 - 4개 장착 시, 재생량 30 증가 | 저항의 결정 - 4개 장착 시, 속성 저항 35 증가 |
| 12 | 관통의 결정 - 4개 장착 시, 관통력 12 증가 | 재생의 결정 - 4개 장착 시, 재생량 30 증가 |

2.8.0.1 wraps the whole string in `<color='241,26,90,255'>` … `</color>`.

### 1.3.2 `en` → `EN` — value **5%** old

| # | 1.4.4.1 `en` | 2.8.0.1 `EN` |
|---|---|---|
| 1 | HP Jewel - Mount 2, Increase HP 5% | HP Jewel - Mount 2, Increase HP 6% |
| 2 | Offensive Jewel - Mount 2, Increase AP 5% | Offensive Jewel - Mount 2, Increase AP 6% |
| 3 | Defensive Jewel - Mount 2, Increase DP 5% | Defensive Jewel - Mount 2, Increase DP 6% |
| 4 | Critical Jewel - Mount 2, Increase Critical Attack Chance 4.5% | **Speed Jewel - Mount 4, Increase Attack Speed 1.72** (moved here) |
| 5 | Block Jewel - Mount 2, Increase Block Chance 4.5% | Critical Jewel - Mount 2, Increase Critical Attack Chance 6% |
| 6 | Fatal Jewel - Mount 4, Increase Critical Attack Damage 50% | Fatal Jewel - Mount 4, Increase Critical Attack Damage 60% |
| 7 | **Super Block Jewel** - Mount 4, Damage Reduction Rate Increase 5% | Element Jewel - Mount 4, Increase Elemental Enhancement 35 |
| 8 | Element Jewel - Mount 4, Increase Elemental Enhancement 23 | Penetration Jewel - Mount 4, Increase Armor Penetration 16 |
| 9 | Resistance Jewel - Mount 4, Increase Elemental Resistance 23 | Block Jewel - Mount 2, Increase Block Chance 5% |
| 10 | Speed Jewel - Mount 4, Increase Attack Speed 1.72 | **`Reduction Jewel - Mount 4, Damage Reduction Increase 10%`** |
| 11 | Regeneration Jewel - Mount 4, Increase HP Regeneration 30 | Resistance Jewel - Mount 4, Increase Elemental Resistance 35 |
| 12 | Penetration Jewel - Mount 4, Increase Armor Penetration 12 | Regeneration Jewel - Mount 4, Increase HP Regeneration 30 |

Rows are **entry**-aligned (twelve families), not rendered-line aligned. The old
English string holds twelve entries but only **eleven** `\n`, and there are two
defects: a missing separator before `Increase 5%` (entry 7 wraps onto two
rendered lines) and a missing separator before `Speed Jewel` (entries 9 and 10
share one rendered line). Consequences worth recording:

- `Penetration`, the twelfth entry, has **no line of its own**;
- the rendered-line order after entry 8 is offset by one relative to the entry
  order, which is exactly why `apk-diff-2026-10-05.md` §4's line-based English
  table showed `Penetration 12` trailing with no partner row and read as if the
  family had dropped out of the new table. It did not — the new table ends
  `…Resistance 35 / Regeneration 30` and has no Penetration line at that
  position because Penetration moved to entry 8.

2.8.0.1 fixes both separators (twelve entries, twelve well-formed lines) and
wraps the whole string in `<color='241,26,90,255'>` … `</color>`.

Exact old English line list, all 12 lines verbatim:

```
HP Jewel - Mount 2, Increase HP 5%
Offensive Jewel - Mount 2, Increase AP 5%
Defensive Jewel - Mount 2, Increase DP 5%
Critical Jewel - Mount 2, Increase Critical Attack Chance 4.5%
Block Jewel - Mount 2, Increase Block Chance 4.5%
Fatal Jewel - Mount 4, Increase Critical Attack Damage 50%
Super Block Jewel - Mount 4, Damage Reduction Rate
Increase 5%
Element Jewel - Mount 4, Increase Elemental Enhancement 23
Resistance Jewel - Mount 4, Increase Elemental Resistance 23 Speed Jewel - Mount 4, Increase Attack Speed 1.72
Regeneration Jewel - Mount 4, Increase HP Regeneration 30
Penetration Jewel - Mount 4, Increase Armor Penetration 12
```

### 1.3.3 `jp` → `JA` — value **5%** old

| row | 1.4.4.1 `jp` (offset 185,197, 268 chars) | 2.8.0.1 `JA` (offset 216,453, 304 chars) |
|---|---|---|
| 1 | HP結晶 - 2コ装着：HP 5%▲ | HP結晶 - 2コ装着：HP 6%▲ |
| 2 | 攻撃結晶 - 2コ装着：攻撃力 5%▲ | 攻撃結晶 - 2コ装着：攻撃力 6%▲ |
| 3 | 防御結晶 - 2コ装着：防御力 5%▲ | 防御結晶 - 2コ装着：防御力 6%▲ |
| 4 | 致命結晶 - 2コ装着：致命打率 4.5%▲ | **スピード結晶 - 4コ装着：攻撃速度 1.72▲** (moved here) |
| 5 | ブロック結晶 - 2コ装着：ブロック率 4.5%▲ | 致命結晶 - 2コ装着：致命打率 6%▲ |
| 6 | 衝撃結晶 - 4コ装着：致命打ダメージ量 50%▲ | 衝撃結晶 - 4コ装着：致命打ダメージ量 60%▲ |
| 7 | 鉄壁結晶 - 4コ装着：**ブロックダメージ減少量 5%**▲ | 属性結晶 - 4コ装着：属性強化 35▲ |
| 8 | 属性結晶 - 4コ装着：属性強化 23▲ | **貫通結晶 - 4コ装着：貫通力 16▲** |
| 9 | 耐性結晶 - 4コ装着：属性耐性 23▲ | ブロック結晶 - 2コ装着：ブロック率 5%▲ |
| 10 | スピード結晶 - 4コ装着：攻撃速度 1.72▲ | 鉄壁結晶 - 4コ装着：**ダメージ減少量 10%**▲ |
| 11 | 再生結晶 - 4コ装着：再生力 30▲ | 耐性結晶 - 4コ装着：属性耐性 35▲ |
| 12 | 貫通結晶 - 4コ装着：貫通力 12▲ | 再生結晶 - 4コ装着：再生力 30▲ |

### 1.3.4 `zh` → `SC` — value **5%** old, **9%** new (not the same string)

| row | 1.4.4.1 `zh` (offset 185,819, 268 chars) | 2.8.0.1 `SC` (offset 217,113, 278 chars) |
|---|---|---|
| 1 | HP结晶 - 镶嵌2个时，增加HP 5% | HP结晶 - 镶嵌2个时，增加HP 5% |
| 2 | 攻击结晶 - 镶嵌2个时，增加攻击力5% | 攻击结晶 - 镶嵌2个时，增加攻击力5% |
| 3 | 防御结晶 - 镶嵌2个时，增加防御力5% | 防御结晶 - 镶嵌2个时，增加防御力5% |
| 4 | 暴击结晶 - 镶嵌2个时，增加暴击率4.5% | 暴击结晶 - 镶嵌2个时，增加暴击率4.5% |
| 5 | 阻挡结晶 - 镶嵌2个时，增加阻挡概率4.5% | 阻挡结晶 - 镶嵌2个时，增加阻挡概率4.5% |
| 6 | 冲击结晶 - 镶嵌4个时，增加暴击杀伤力50% | 冲击结晶 - 镶嵌4个时，增加暴击杀伤力50% |
| 7 | 铁壁结晶 - 镶嵌4个时，增加**阻挡被害减少量 5%** | 铁壁结晶 - 镶嵌4个时，增加**伤害减少量 9%** |
| 8 | 属性结晶 - 镶嵌4个时，增加属性强化23 | 属性结晶 - 镶嵌4个时，增加属性强化23 |
| 9 | 耐性结晶 - 镶嵌4个时，增加属性耐性23 | 耐性结晶 - 镶嵌4个时，增加属性耐性23 |
| 10 | 速度结晶 - 镶嵌4个时，增加攻击速度1.72 | 速度结晶 - 镶嵌4个时，增加攻击速度1.72 |
| 11 | 恢复结晶 - 镶嵌4个时，增加**恢复量**30 | 恢复结晶 - 镶嵌4个时，增加**恢复力**30 |
| 12 | 穿透结晶 - 镶嵌4个时，增加穿透力12 | 穿透结晶 - 镶嵌4个时，增加穿透力12 |

Two of twelve lines differ beyond the numeral: row 7 loses the
`阻挡`/`被害` ("blocked damage") qualifier and 5%→9%; row 11 changes
`恢复量`→`恢复力` ("recovery amount"→"recovery power"). Neither `SC` nor `TC`
carries the `<color>` tag in 2.8.0.1.

### 1.3.5 `zt` → `TC` — value **5%** old

| row | 1.4.4.1 `zt` (offset 186,463, 270 chars) | 2.8.0.1 `TC` (offset 217,773, 280 chars) |
|---|---|---|
| 1 | HP結晶 - 鑲嵌2個時，增加HP 5%␠ | HP結晶 - 鑲嵌2個時，增加HP 6%␠ |
| 2 | 攻擊結晶 - 鑲嵌2個時，增加攻擊力5% | 攻擊結晶 - 鑲嵌2個時，增加攻擊力6%␠ |
| 3 | 防禦結晶 - 鑲嵌2個時，增加防禦力5% | 防禦結晶 - 鑲嵌2個時，增加防禦力6%␠ |
| 4 | 暴擊結晶 - 鑲嵌2個時，增加暴擊機率4.5% | **速度結晶 - 鑲嵌4個時，增加攻擊速度1.72** |
| 5 | 阻擋結晶 - 鑲嵌2個時，增加阻擋機率4.5% | 暴擊結晶 - 鑲嵌2個時，增加暴擊機率6% |
| 6 | 衝擊結晶 - 鑲嵌4個時，增加暴擊殺傷力50% | 衝擊結晶 - 鑲嵌4個時，增加暴擊殺傷力60%␠ |
| 7 | 鐵壁結晶 - 鑲嵌4個時，增加**阻擋傷害減少量 5%** | 屬性結晶 - 鑲嵌4個時，增加屬性強化35 |
| 8 | 屬性結晶 - 鑲嵌4個時，增加屬性強化23 | 穿透結晶 - 鑲嵌4個時，增加穿透力16 |
| 9 | 耐性結晶 - 鑲嵌4個時，增加屬性耐性23 | 阻擋結晶 - 鑲嵌2個時，增加阻擋機率5% |
| 10 | 速度結晶 - 鑲嵌4個時，增加攻擊速度1.72 | 鐵壁結晶 - 鑲嵌4個時，增加**傷害減少量 10%** |
| 11 | 恢復結晶 - 鑲嵌4個時，增加恢復力30 | 耐性結晶 - 鑲嵌4個時，增加屬性耐性35 |
| 12 | 穿透結晶 - 鑲嵌4個時，增加穿透力12 | 恢復結晶 - 鑲嵌4個時，增加恢復力30 |

`␠` marks a literal trailing space.

## 1.4 The core matrix — all ten locale strings, bonus values only

`desc2` values in shipped order, mount counts (`2`/`4`) and the `<color>`
tag numerals stripped out. This is the single most useful table in the file.

| # | 1.4.4.1 `ko` | 1.4.4.1 `en` | 1.4.4.1 `jp` | 1.4.4.1 `zh` | 1.4.4.1 `zt` | 2.8.0.1 `KO` | 2.8.0.1 `EN` | 2.8.0.1 `JA` | 2.8.0.1 `SC` | 2.8.0.1 `TC` |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5% | 5% | 5% | 5% | 5% | 6% | 6% | 6% | 5% | 6% |
| 2 | 5% | 5% | 5% | 5% | 5% | 6% | 6% | 6% | 5% | 6% |
| 3 | 5% | 5% | 5% | 5% | 5% | 6% | 6% | 6% | 5% | 6% |
| 4 | 4.5% | 4.5% | 4.5% | 4.5% | 4.5% | 1.72 | 1.72 | 1.72 | 4.5% | 1.72 |
| 5 | 4.5% | 4.5% | 4.5% | 4.5% | 4.5% | 6% | 6% | 6% | 4.5% | 6% |
| 6 | 50% | 50% | 50% | 50% | 50% | 60% | 60% | 60% | 50% | 60% |
| 7 | **9%** | 5% | 5% | 5% | 5% | 35 | 35 | 35 | **9%** | 35 |
| 8 | 23 | 23 | 23 | 23 | 23 | 16 | 16 | 16 | 23 | 16 |
| 9 | 23 | 23 | 23 | 23 | 23 | 5% | 5% | 5% | 23 | 5% |
| 10 | 1.72 | 1.72 | 1.72 | 1.72 | 1.72 | 10% | 10% | 10% | 23 | 10% |
| 11 | 30 | 30 | 30 | 30 | 30 | 35 | 35 | 35 | 1.72 | 35 |
| 12 | 12 | 12 | 12 | 12 | 12 | 30 | 30 | 30 | 30 | 30 |

Rows are **positional**, not per-family: the order itself was rewritten (see
§1.5). Row 7 is `Super Block` in 1.4.4.1 and `Reduction` in 2.8.0.1.

Per-locale value fingerprints (SHA-256 of the UTF-8 `desc2` string) so any line
in §1.3 can be re-verified:

| pair | old `desc2` SHA-256 | new `desc2` SHA-256 | byte-identical |
|---|---|---|---|
| `ko`→`KO` | `a18dae56…` | `4396ca92…` | no |
| `en`→`EN` | `6e3b58a2…` | `51364974…` | no |
| `jp`→`JA` | `a5b94ed2…` | `a50a59f7…` | no |
| `zh`→`SC` | `6aad9f99…` | `462f0cea…` | no |
| `zt`→`TC` | `9ba0ab79…` | `017cbf53…` | no |

## 1.5 Row-order map (pure reordering, no value implication)

Family → row, 1.4.4.1 → 2.8.0.1:

| Family | old row | new row |
|---|---|---|
| HP | 1 | 1 |
| Offensive / AP | 2 | 2 |
| Defensive / DP | 3 | 3 |
| Speed / Attack Speed | **10** | **4** |
| Critical / Crit chance | 4 | 5 |
| Fatal / Crit damage | 6 | 6 |
| Element / Enhancement | 8 | 7 |
| Penetration | **12** | **8** |
| Block / Block chance | 5 | 9 |
| Super Block → **Reduction** | 7 | 10 |
| Resistance | 9 | 11 |
| Regeneration | 11 | 12 |

Row numbers are the **twelve-entry positional order**, read off the numeral
sequence (`2|5%` / `4|23` mount+value pairs), not the rendered line count —
which matters only for 1.4.4.1 `en`, where two missing `\n` separators make
twelve entries render as twelve lines with one line carrying two entries
(§1.3.2). `SC` alone kept the old row order.

## 1.6 Corrections to `apk-diff-2026-10-05.md` §4

1. **"CJK mojibake in this tooling"** — the files are valid UTF-8 (§0.2). The
   KO 9% reading did **not** depend on numeral position in row 7; it is a
   literal numeral in a legible Korean line:
   `철벽의 결정 - 4개 장착 시, 막기 피해량 9% 증가`.
2. **"SC retains the OLD table verbatim, including Super Block 9%"** — SC does
   retain the *old numeric profile*, but its row-7 value is **9%**, which was
   the **KO** variant, not the 1.4.4.1 `zh` value (5%). And the string is
   **not** verbatim: row 7 drops the `阻挡被害` qualifier, row 11 changes
   `恢复量`→`恢复力`, entries are `\n\n`-separated with a leading newline, and
   the `<color>` tag the other new locales carry is absent. SC's row-7 value is
   better described as *the KO-era 9% variant surviving in SC*, i.e. the
   pre-existing KO/rest split relocating from KO-vs-rest to SC-vs-rest, with
   both copies re-authored.

## 1.7 Wording change on the renamed jewel (pure)

1.4.4.1 names row 7 "Super Block" (EN) / 철벽 / 鉄壁 / 铁壁 / 鐵壁 and describes
it as **block damage reduction**: `막기 피해량`, `ブロックダメージ減少量`,
`阻挡被害减少量`, `阻擋傷害減少量`. 2.8.0.1 keeps the same jewel name in every
non-English locale (철벽/鉄壁/铁壁/鐵壁, **not** renamed in script), renames only
the **English** label to `Reduction Jewel`, and **drops the "block" qualifier in
all five locales**: `피해 감소량`, `ダメージ減少量`, `伤害减少量`, `傷害減少量`,
`Damage Reduction` (2.8.0.1 EN also drops `Rate`, which the old EN had).

---

# SECTION 2 — UNPURE: bonus numerals as rebalance deltas

Everything in this section is interpretation. Nothing here is a recovered
stat, and nothing here changes any coverage denominator.

## 2.1 Why these numerals are impure

They are **set-bonus definitions in help copy**, not any recovered engine
constant. Specifically:

- No native consumer of these twelve values was located. They are display
  strings in `UI_CSV` help resources, and the replica's `/reference/*`-driven
  architecture means any authoritative value would live server-side
  (`analysis/research/base-stats-visual-hunt/README.md`, old-APK lane).
- The numbers are **rounded display integers** (`4.5%`, `1.72`, `23`, `35`)
  with **no printed unit discipline**: some are `%`, some are dimensionless
  points (`23`, `30`, `35`, `1.72`, `16`, `12`). Which underlying stat a bare
  `35` scales, and whether it is an integer or a truncation, is unproven.
- A **help table can lag or lead the live balance table**. A string is not a
  balance authority.
- **Locale copies disagree** (9% vs 5% in one shipped corpus), which is direct
  proof that at least one copy was wrong at some point.

Use these only as rebalance-direction anchors. Never quote them as hero,
monster, or jewel-instance stats.

## 2.2 Per-family delta, 1.4.4.1 → 2.8.0.1 (EN reference; §1.4 shows locales)

| Family | Mount | old | new | absolute Δ | relative | announcement's qualitative bucket |
|---|---|---|---|---|---|---|
| HP | 2 | 5% | 6% | +1 pp | ×1.20 | "HP … strengthened" |
| Offensive / AP | 2 | 5% | 6% | +1 pp | ×1.20 | "attack … strengthened" |
| Defensive / DP | 2 | 5% | 6% | +1 pp | ×1.20 | "defense … strengthened" |
| Critical / crit chance | 2 | 4.5% | 6% | +1.5 pp | ×1.333 | "crit chance … smaller boost" |
| Fatal / crit damage | 4 | 50% | 60% | +10 pp | ×1.20 | "crit damage … smaller boost" |
| Block / block chance | 2 | 4.5% | **5%** | +0.5 pp | ×1.111 | "block chance … smaller boost" |
| Super Block → Reduction | 4 | 5% (EN) / **9%** (KO) | 10% | +5 pp (EN) / +1 pp (KO) | ×2.00 / ×1.111 | "block-damage reduction … smaller boost" |
| Element / enhancement | 4 | 23 | 35 | +12 | ×1.5217 | "elemental enhancement/resistance … strengthened" |
| Resistance | 4 | 23 | 35 | +12 | ×1.5217 | "elemental enhancement/resistance … strengthened" |
| Penetration | 4 | 12 | 16 | +4 | ×1.333 | "penetration … strengthened" |
| Speed / attack speed | 4 | 1.72 | 1.72 | **0** | **×1.00** | not mentioned |
| Regeneration / HP regen | 4 | 30 | 30 | **0** | **×1.00** | not mentioned |

Every changed family moved **up**; none moved down. Two families are
**unchanged** across the whole span.

## 2.3 Era tags

Threshold: the 2019-09-05 rebalance (`stat-version-context.md`).

- **2.8.0.1 = POST.** Safe: this is the build recorded installed on the phone,
  last updated 2024-05-07 (AGENTS.md §10), years past the threshold.
- **1.4.4.1 = PRE, inferred.** Version code `1441` is below `2.0`, and
  Blustone 2 (`2.0.x`) is a 2018 release (AGENTS.md §77), so this build
  predates 2019-09-05. **No build date or version archive timestamp is pinned
  anywhere in this workspace**, so this is an inference from version numbering,
  not a dated fact.

## 2.4 Correspondence with the official 2019-09-04 announcement

The announcement (`stat-version-context.md` §1) says, qualitatively: attack,
defense, HP, elemental enhancement/resistance and penetration were
**strengthened**; crit chance, crit damage, block chance and block-damage
reduction got **smaller boosts**; set bonuses were raised with **no exact
amounts** given.

The measured deltas match that shape family-for-family, including the relative
ordering (HP/AP/DP/crit-damage all ×1.20, below ×1.333 for crit chance and
penetration, below ×1.52 for elemental, and the smallest of all ×1.111 for
block chance).

**This is corroboration of shape, not identification of the change.** The
client span 1.4.4.1 → 2.8.0.1 is far wider than the announcement window, so
other balance revisions are certainly folded in; the announcement supplies no
numbers, so it cannot be used to derive any figure here. The two unmarked
families (attack speed, HP regeneration) are equally consistent with
"intentionally untouched".

## 2.5 Locale divergence is itself the most useful signal here

Within the **same shipped 2.8.0.1 corpus**, `KO`/`EN`/`JA`/`TC` carry one table
and `SC` carries the old profile. That is direct in-client evidence that:

- the revision was **not a single global string replacement** — it shipped
  incomplete, and one locale kept the previous revision;
- the `9%` seen in 1.4.4.1 `ko` is the value that **survived** in 2.8.0.1 `SC`.
  So `9%` is not a mistranscription of `5%`; two values genuinely circulated.

Practical consequence for any rebalance model: **do not treat one locale as
canonical.** A model fitted to 1.4.4.1 EN would mis-predict a Chinese client
and a Korean client differently, and the disagreement is not resolvable from
the files alone.

## 2.6 Explicitly labelled hypothesis (unproven)

`23 → 35` equals `23 × 1.5` rounded up (34.5 → 35); `12 → 16` and
`4.5 → 6` both equal `× 4/3` exactly; `5 → 6` and `50 → 60` both equal
`× 1.2` exactly. This is consistent with the displayed integers being rounded
from scaled underlying float constants rather than hand-typed. **Not proven**:
there is no engine constant, no `LEVELING.jet` row and no native field
corresponding to these twelve values, the ×1.111 (block chance) and the
KO-relative ×1.111 (reduction) do not fit a single neat multiplier, and the
2.8.0.1 `SC` copy proves the displayed table was maintained by hand. Do not
propagate this ratio back onto other values.

## 2.7 Bounded negative: no other jewel-help bonus value changed

`CONTENTS11_1`, `11_4`, `11_5`, `11_6`, `11_7` exist in both versions and
their numeral sequences all differ — but the differences are **entirely** the
new `<size='29'>` / `<size='22'>` and `<color='241,26,90,255'>` markup numerals
plus the `11_x`/`1` id echoes. **None of those five records carries a
set-bonus numeral**, so `CONTENTS11_8` is the only jewel-help record with a
revised bonus value.

A whole-corpus numeral-sequence sweep reports 73 changed / 84 unchanged record
ids, but that figure is **not** a balance signal: the new corpus introduced
markup numerals into most help strings, which contaminates any naive numeral
diff. It is recorded so nobody re-derives it as evidence of mass rebalance.

## 2.8 Limits

- Both sources are **client help copy**, not the balance table.
- 1.4.4.1 has **no pinned date**; its PRE tag is a version-numbering inference.
- The **live 2.8.0.1 server-side set-bonus values are unknown** and may differ
  from this string.
- The 2.8.0.1 `SC` copy means the shipped 2.8.0.1 client **disagreed with
  itself**; which copy reflects live behaviour in a Chinese client is unproven.
- `1.72` and `30` never changed; the announcement does not mention them, so
  "unchanged" is an observation about two strings, not proof of a deliberate
  balance decision.
- No native render, no in-game screenshot and no engine read of this record was
  performed. Everything here is decoded file content.
- Round-tripping percent points into a formula needs the underlying stat
  definitions, which remain unrecovered.

## 2.9 Cross-references

- `apk-diff-2026-10-05.md` §4 — the version-diff claim this file expands and
  partially corrects.
- `stat-version-context.md` — the 2019-09-04/05 rebalance and era usage.
- `coverage.md` — unchanged denominators; no credit from this file.
- `polluted-observations.md` — appended impure entry for these deltas.
- `readme.md` §98 — the VSFan tree that supplies the 1.4.4.1 baseline.