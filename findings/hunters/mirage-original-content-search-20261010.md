# Original Mirage content: final-build help and bounded web search

2026-10-10. Independent read-only research lane. No ADB/UI, Ghidra, server,
account, client patch, stat hunt or runtime action. Only this note was written.

The final **2.8.0.1** client itself preserves concrete Mirage rules previously
cited mainly from the older **1.4.4.1** help. These are original shipped rule
descriptions; they do not supply the missing server-generated floor instances.
No original grade/balance rows, enemy selections or per-stair payout quantities
were recovered by this pass. An arbitrary balance10000 remains unjustified.

## Authoritative local source and reproduction

Source: `analysis/extracted/assets/UI_CSV.jet`, 93,380 bytes, SHA-256
`73a9dc4755baf8eb84c3fa945b7dd8b10228fe73d47a945de27137de2c84dac8`.
Inflate zlib starting at byte540; remove its six-byte RW+uint32 header. The help
JSON is 288,762 bytes, SHA-256
`730070894cb69ccbfc85bbaa3d44de5ed8dbb8238081d91ab196a2716eb6b754`;
`json.loads` succeeds and yields205 records. All12 `CONTENTS9_*` rows exist.
The file/hash/body recipe was executed independently this turn; these values
agree with `base-stats-visual-hunt/help-2_8-sweep-2026-10-05.md`.

Read-only reproduction (writes nothing):

```python
import hashlib, json, zlib
from pathlib import Path
blob = Path('analysis/extracted/assets/UI_CSV.jet').read_bytes()
body = zlib.decompress(blob[540:])[6:]
print(len(blob), hashlib.sha256(blob).hexdigest())
print(len(body), hashlib.sha256(body).hexdigest())
rows = json.loads(body)
for row in rows:
    if row.get('id', '').startswith('CONTENTS9_'):
        print(json.dumps(row, ensure_ascii=True))
```

This is a final-build attribution, not a precise creation date for each string
or proof that the last production server implemented every help description.
Unchanged help can outlive a rule change. Native consumers and actual captured
server responses remain necessary for exact transaction behavior.

## Concrete final-build rules, paraphrased by original row ID

- `CONTENTS9_1`: enemies resemble hunters; deeper floors increase enemy strength
  and Mirage Fragment yield. It does not enumerate a maximum floor.
- `CONTENTS9_2`: all owned hunters may participate in the sortie, but duplicates
  contribute only the strongest copy. The chosen copy stays fixed during that
  ruin attempt. JA explicitly frames strongest as combat power; no tiebreaker
  or exact calculation is published here.
- `CONTENTS9_3`: battles are5-versus5. Consumed HP persists within the current
  floor, and fainted hunters cannot sortie again. KO/JA/SC/TC explicitly scope
  the no-recovery rule to the floor in progress. This does not establish that
  healing skills are disabled inside combat; it describes carryover.
- `CONTENTS9_4`: re-entry availability renews once daily at midnight. Retry
  resets the current progress. KO says the re-entry becomes available again,
  which is more precise than reading the EN prose as an unsolicited automatic
  midnight wipe of an ongoing run. Timezone and whether multiple saved clocks
  exist are still unknown.
- `CONTENTS9_5`: fragments fund the Mirage Market. Its goods refresh at midnight,
  with at most3 purchased resets. This is a shop clock, separate from run
  re-entry and temporary boosted hunters.
- `CONTENTS9_6`: a minority of hunters are stronger only inside Mirage; that
  power moves to different hunters every few days. No fixed weekly weekday,
  rotation list, number of boosted hunters or multiplier is published.
- `CONTENTS9_7`: the current and highest cleared floors are displayed, as are
  friends' highest floors. This establishes two distinct floor concepts.
- `CONTENTS9_8`: stage27 or above unlocks the initial entrance explanation;
  Gullveig's third dialogue choice subsequently enters Mirage. **desc1.EN is
  absent** in the final build; KO/JA/SC/TC retain the rule. This agrees with the
  native re-entry observation in AGENTS§216, independently of that runtime.
- `CONTENTS9_9`: initial assignment depends on average team combat power. A
  fully cleared floor followed by re-entry goes deeper; failing to clear the
  entire floor moves toward the surface. There is no numeric floor formula,
  jump size, averaging population or threshold table.
- `CONTENTS9_10`: **floors1–20 contain3 battles; floors21–40 contain6; floors41+
  contain9**. All five locales corroborate these bounds. These are final
  shipped help values, superseding a merely historical1.4.4.1 attribution.
  This gives a count policy but not individual stair grades/balances/rewards.
- `CONTENTS9_11`: Manda buys limited first aid for fainted hunters, permitting
  immediate participation in the next battle. **KO/JA/SC/TC explicitly say full
  HP is restored**; EN only says HP returns. No price, use cap or escalation is
  supplied, so a partial/full numeric heal transaction cannot be priced here.
- `CONTENTS9_12`: Harley traces are described as Mirage Market exclusives;
  Harley is a4-star ice defender, unavailable through Lottery Mouse draws.
  The prose retains forward-looking wording and supplies no listing quantity,
  item/ref ID, fragment price or guarantee about the final production shop.

This final-build evidence also corrects a possible interpretation error in
older economy notes: the weekly local `ref_hero.end_ltime` policy is not the
daily run-reset clock. Their cadence cannot be compared as one timer.

## Original help visual availability: bounded check

The final help maps rows9_2..12 to original `G_LI9_*` resources (SC uses the
`_ZHS` suffix). `CONTENTS9_1` uses `G_LI9_1`. A bounded decoder inspection of
`analysis/extracted/assets/GUIDE.jet`, `GUIDE2.jet`, `GUIDE3.jet`, `GUIDE4.jet`
completed; inspecting inflated chunks for literal ASCII `G_LI9_` found none.
This establishes only that these four exposed inflated byte streams did not
carry that literal resource label. It does **not** establish missing help
artwork or missing DB bindings. Resource ownership and screenshot inspection
were not closed; no screenshot was used to invent a grade sequence.

## Web search coverage and limits

Fresh searches used exact English `Blustone`, `Mirage Ruins`, `VisualShower`,
2018/2019 and Korean `신기루 유적`/`비주얼샤워`, plus official/community domain
filters. Direct opens of [official English notice board](https://bs.visualshower.com/notice_en),
[official-hosted firsthand thread1160203](https://bs.visualshower.com/share_en/1160203),
[its dated archive](https://web.archive.org/web/20190916082001/https://bs.visualshower.com/share_en/1160203)
and [VSFan](https://vsfan.net/) returned inaccessible from the web tool.
No accessible primary publisher Mirage post or firsthand video emerged in this
bounded pass. No video was played; this is not an exhaustive absence claim.

Search did surface secondary guides and Korean wiki mirrors. They were used
as discovery leads only. Their concrete market quantities are inconsistent
across pages/eras (e.g. Harley trace quantities3 versus5), and they do not
supply final2.8 floor instances. No secondary figure was promoted into the
replica or declared original numeric content. Existing local reports of a
2019 floor250 firsthand thread remain historical leads, not a newly viewed
floor250 enemy roster or transferable balance table.

## Implication for implementation

The3/6/9 floor-count rule, strongest-copy constraint, floor-local HP carryover,
full first-aid recovery, daily re-entry availability and separate temporary
boost cadence now have final shipped help provenance. They can guide original
semantics and focused tests once the native run/entry/end/reward seams are
closed. They cannot justify activating a floor without original or expressly
identified local content. Still missing: assigned floor formula, per-stair
grade and balance, generated hunter instances, reward list/quantity, HP field
authority, reset/entry transaction and first-aid pricing.
