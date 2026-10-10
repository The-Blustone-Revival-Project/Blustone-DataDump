# Fishing catalog: next substantive contract and evidence gate

2026-10-08. Targeted read-only audit of current `state.ts`, retained original
native decomp, original string index and existing fishing/cache reports. No
ADB, Ghidra, server/profile/save edits, private response dump or catch grant.
No numeric Hunter hunt. Root retains exclusive BlueStacks control.

## Decision

**No genuine fish item identity has been recovered.** The next useful fishing
implementation is conditional on recovering one original fish reference row;
more fishing texture activation or a successful empty settlement does not close
that dependency. Current authenticated `GetInven`/`GetRecord` bare arrays are
already implemented (`server-ts/src/state.ts`, `fishingAction`). All other
fishing routes still refuse result2001. Do not report the older entry report's
generic-success fallback as current behavior.

The smallest catalog evidence unit is an original `GetItem.ret_data.item[]`
row with its exact `id`, string `name/desc/thumbnail_id/effect`, numeric
`rank/use_type/sell_price/collect_qty`, and corroboration that the ID is used as
a fishing `fish_id`. A lone resource `FS001`, item icon `FISH_01`, or the
NPC0004 species name Calcium Smelt does not provide that corroboration.
One real row could unblock a **clearly labeled local tutorial settlement**;
it would not recover the original demo species selection, grade, length or
economics, and would not by itself justify ordinary catch pools.

## New retained-parser finding: price response is a collection

`analysis/ghidra-fishing-pool-begin.txt:1249` contains complete original
**ParsePrice G b2e438**. The parser extracts fullJSON.ret_data, conditionally
applies `achievement`, determines its collection size, then indexes ret_data
numerically in a loop. It reads three price quantities through numeric
conversions into **uint32** locals, then a **strict string** fish identity
(literal expression at G b2e5ee; `from_json<string>` immediately afterward).

The three key spellings `b_price/s_price/g_price` are retained in the original
string index at 0x1d7b001/009/011 and prior fishing field reports. This pass
does not independently assign each decomp numeric local to its key without
the exact PC-relative key dump. The complete collection structure is directly
visible and does not depend on that assignment.

The fish string is the key of native `map<string, PRICE>` at **Fishing+0x1c**.
For an existing key, the parser overwrites all three node price words
(node+0x1c/+0x20/+0x24). Otherwise it inserts a node containing the string and
three prices. It does not clear the map in this inspected function. Thus a
nonempty price response must be an **array of price rows**, even when the
request asks for one fish. Do not publish a flat
`ret_data:{fish_id,b_price,s_price,g_price}` object or infer an authoritative
whole-catalog replacement from the upsert path. No original price amount,
grade-domain completeness, overflow policy or sale receipt is recovered here.

## Exact settlement gates already proved

* `GetFishingPool` actual receiver **G b324c8** consumes ret_data directly as
  rows with strict `lure_id` and `fish_id` strings. This is membership only;
  no weights, cast-distance table or fish definition is supplied by those rows.
* Tutorial really emitted `EndWithSell(log_id:"-1")` after gauge100. The
  current backend refusal is not an earned catch receipt. Tutorial and ordinary
  requests share **ReqEndCB b2a308 → ParseEnd b2a560**.
* ParseEnd strict string `fish_id` writes Fishing+0x68. A nonempty value invokes
  **AddInven b2e758 / UpdateRecord b2e980**, using returned grade and length.
  Those client mutations are additive: replaying an identical success response
  can duplicate native inventory even if server persistence is idempotent.
* Hook mode4 performs real guide **Clear(27,2)** and unconditionally opens
  Success.Init; its item lookup is exactly Fishing+0x68. Empty identity hits
  GetItemData's DUMMY/static fallback, not a proved null crash; that fallback
  still supplies no legitimate original fish text/art or catch.
* Result grade2 selects silver, grade3 gold, otherwise bronze-style display;
  length is displayed in hundredths of a centimeter. This does not recover
  valid grade enums or original length distributions. Optional `ret_data.sell`
  enters **ParseSell b2b018**; its success shape and resource/count mutations
  must be recovered before any sale amount is credited.

Sources: `fishing-pool-begin-contract.md`,
`fishing-tutorial-settlement-contract.md`,
`fishing-tutorial-demo-identity.md`, `shop-fuel-contract.md`.

## Finite next research operations, in priority order

1. **Original public resource descriptor ownership**, not another state-DB scan:
   native LoadStr uses the resource map and uppercases to
   `REFEN/REFERENCE/GETITEM` (other locales analogous). Determine the encoding
   and registration of the slash-containing resource key, then inspect only
   matching original JET descriptors/raw JSON. The current 774-filename miss
   does not test descriptors. Numeric/base38 outer names cannot represent a
   literal slash path without a distinct registration rule; prove that rule
   before a bulk scan. Root-only native target is the exact registration chain
   called by `CRMResMap.IsExistingRes G717e04 / LoadRawData G10eac8c`.
2. **Direct bait consumers**, if fish reference recovery remains blocked:
   `CSRSceneMFishing.RequestBuyGlobalItem G e6e724`, `UpdateBait G e6ea48`,
   `CSRMFishing.GetBait G b2efd0`. A direct reference lookup might positively
   bind original `BAIT1/BAIT2` to item identity/use-type rather than guessing
   from `BAIT01` art. Even a confirmed ID leaves quantity, effect and price
   metadata open; no bait purchase should be enabled from literal names alone.
3. **Price/sale receipt closure**: parent can obtain exact keys for ParsePrice
   b2e438 and full ParseSell b2b018. This closes receiver semantics and replay
   constraints while awaiting data. It does not manufacture prices.

Already exhausted within scope: 13 localization/reference tables' fish token
scan; canonical PAD outer filenames; indexed WebView paths; keys-only scans
of UserData/EtcData in all three preserved snapshots, including active
MANIFEST/SST/WAL records. `native-getitem-cache-key-scan.md` confirms all six
containers contain zero normalized GetItem/REF namespace matches and source
hashes remain unchanged. Do not repeat those scans. CDN resource descriptor
ownership is a separate unresolved source, not proof that the state containers
secretly contain a missed row.

External videos can corroborate display species, bait-loss timing and UI;
ordinary footage does not expose internal item IDs or encrypted server
responses. Existing final original HELP_DATA already proves bait loss after
bite/failure/cancel, withdrawal before bite, and fury no-tapping behavior.
No web search was run because those presentation rules are already recovered
and would not resolve this audit's internal-identity gate. An original table
or authorized server response supplied by another revival developer would be
stronger new evidence than another visual fishing search.

## Reproduction commands

```powershell
rg -n 'fishingAction|GetFishingPool|EndWithSell' server-ts/src
Get-Content analysis/ghidra-fishing-pool-begin.txt | Select-Object -Skip 1248 -First 320
rg -n 'b_price|s_price|g_price' analysis/native-all-strings.tsv
Get-Content analysis/research/native-reference-offline-storage.md
Get-Content analysis/research/native-getitem-cache-key-scan.md
Get-Content analysis/research/fishing-tutorial-demo-identity.md
```

No substantive fishing settlement can currently be made faithful simply by
changing response success codes. Retain explicit refusal while pursuing the
positive identity/metadata and receiver evidence above.
