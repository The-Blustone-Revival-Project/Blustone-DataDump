# Cross-check for AGENTS.md §128 — `ICON_GOLD`→`IT_CO` confirmed, but **RP1 is not shown to be gold**

**Written:** 2026-10-06, read-only against the shipped LevelDB tables. Nothing
here was applied; `server-ts` untouched. Raised because §128 is *currently in
progress* and rests on an RP1 identity assumption this note puts in question.

Source: `analysis/recovered-data/leveldb-tables/all-tables.json`
(`tables.UI_JSON_RO`, `tables.UI_XML_RO`). Positive control: 453 entries contain
`IT_`, 5,277 `PopUp` symbols present — the reader works.

---

## 1. `ICON_GOLD` → `IT_CO` is **[RECOVERED]**, and your choice is right

`UI_XML_RO[281]`, key **`KO/SR_COMMON/2_UI_CM_MD/13_UI_LV_MD`**, verbatim:

```xml
<sprite name="ICON_MANDA"  res-name="IT_MIXMD"  pos="-151, 0" align="right, center" scale="0.4" visible="false"/>
<sprite name="ICON_GOLD"   res-name="IT_CO"     pos="-151, 0" align="right, center" scale="0.4" visible="false"/>
<sprite name="ICON_10FREE" res-name="IT_10FREE" pos="-151, 0" align="right, center" scale="0.4" visible="false"/>
```

The direct `ICON_GOLD` → `IT_CO` binding is shipped, not inferred — so replacing
the provisional `IT_GCO` medal with `IT_CO` matches the original. Two details
worth carrying:

- It sits in a **currency trio** with `ICON_MANDA`→`IT_MIXMD` and
  `ICON_10FREE`→`IT_10FREE`.
- All three are **`visible="false"`** by default. The sprite is a template toggled
  on at runtime, so *which* currency icon shows is decided by logic, not by the
  layout. The screen is `UI_LV_MD` — a level-up/material screen.

## 2. **RP1 is not demonstrated to be gold** — flagging an assumption in §128

§128 registers RP1 as a *"known native gold identity"*, display-only. The shipped
UI does not support that. **RP1 occurs in exactly four widget keys and in ZERO
`UI_XML_RO` entries** — it has **no sprite/icon resource of its own**:

| widget key | EN text | KO text |
|---|---|---|
| `TXT_CHARGE_RP1` | **`500 Rupees`** | `500 루피` |
| `RP1_CHARGE_COUNT` | **`Daily Acquisition Amount: 10/10 Times`** | `일일 획득 가능 횟수 10/10` |
| `TXT_RP1_TIME1` | `00 : 00` | — |
| `TXT_RP1_TIME2` | `00 : 00` | — |

Read together those are a **chargeable, daily-capped, timer-based resource** —
a price, a daily acquisition cap of **10**, and two timer readouts. That is the
shape of a purchasable energy/stamina mechanic, not of an alias for the
currency. A currency alias would not carry a charge price or a daily cap.

**The ambiguity, stated honestly.** `TXT_CHARGE_RP1` = "500 Rupees" is genuinely
two-way: it could label a price *denominated in* RP1 (supporting the gold reading)
or the *cost of* RP1. The daily cap and the timers are what tip it — a gold alias
does not need a 10/day acquisition limit. **But this is inference, not proof.**

**Why it matters.** §122 settled the E18 reward (shipped `RP1 qty 100000`) by
mapping it to a gold receipt, on the reasoning that the original `LoginBonus`
reader treats RP1 as the gold *display* identity. Display adjacency is not
identity: a shop that happens to price things in Rupees would produce the same
co-occurrence. If RP1 is in fact a distinct chargeable resource, that mapping is
wrong in the same way the Chu-coin hypothesis was — and §122/E18 credit is
already implemented.

**Cheap discriminator, if you want it:** a `charge`/`recharge` RPC in the native
route table would confirm a distinct resource; so would RP1 appearing in a
`/reference/GetItem`-style row with its own `use_type`. Neither RP1, GC2 nor FMD1
appears in the **105-row `CHAR_STR.db` item table**
(`charstr-items-2026-10-06.tsv`), which is equipment-only — so the tables cannot
settle it either way, and the item inventory remains the place to look.

## 3. Incidental: the gold currency's shipped name

The CHAR_STR item table gives adjacent vocabulary that may help naming:
`014` accessory **Lucky Coin** (`ラッキーコイン` / `행운의 동전`) with weapon
**Rupee Gun** and armour **Pure Gold Armor**; `084` accessory **Pure Gold Chain
Necklace**. These are *equipment*, not the currency — but they confirm **Rupee**
is the shipped English name for the gold unit, matching the "Collected Rupees"
string already seen in native result screens.

## 4. What is NOT claimed

- I did **not** determine what RP1 actually is. Only that the "known gold
  identity" is unproven and contradicted by a charge/cap/timer UI.
- I did **not** verify §128's runtime behaviour — the calendar and Rupees
  detail reportedly render correctly, and nothing here contradicts that. This is
  about the *label* attached to RP1, not about the preview working.
- No file outside this folder was read for writing; `server-ts`, fixtures, APK,
  seeds, emulator and phone untouched. Coverage counters unmoved.
