# VSFan packet capture findings

Scope: the five PCAP files in `analysis/VSFan/Packet Captures/`, plus the matching extracted package and reslist directories where needed to understand the HTTP asset traffic. This is a protocol and research-lead report, not a re-publication of capture contents. All five captures were read locally; no network requests were made.

## Capture inventory

Frame counts, byte sizes, and timestamp intervals below come from the classic PCAP headers and packet records. Classic PCAP does not encode a time zone, so the displayed wall-clock times are only the host's conversion of those timestamps. App versions for the first two are cross-referenced to the matching dated `Extracted Assets (2026)` folders and reslists.

| Capture | Size | Frames | Captured interval (host-local rendering) | Context / result |
|---|---:|---:|---|---|
| `blustone.pcap` | 128,731,909 B | 8,103 | 2017-09-05 06:56:11–07:06:24 | Blustone 1.1.2.0; clear HTTP platform and game API routes, game bootstrap/reference requests, tutorial and mission requests, plus CDN `.pkg` downloads. |
| `bs_transcendence.pcap` | 54,929,150 B | 3,436 | 2017-09-08 13:53:00–13:54:04 | Blustone 1.1.3.0; clear HTTP launch/bootstrap and reference traffic, updated reslist/package fetches, and one additional reference route (`GetCardOvercome`). |
| `btba_install.pcap` | 21,496,355 B | 1,908 | 2017-09-06 02:01:57–02:03:42 | A separate BTBA/`_BTBA_PRD` install and entry flow, not Blustone. It exposes platform, purchase-catalog and content-gate routes, then fetches BTBA packages. |
| `btba.pcap` | 1,102,501 B | 770 | 2017-09-06 02:35:45–02:36:04 | TCP/TLS traffic only at the application layer; no readable HTTP request or game API route recovered. |
| `whiteisland.pcap` | 96,353,113 B | 4,191 | 2017-09-06 02:36:12–02:39:16 | TCP/TLS traffic only at the application layer; no readable HTTP request or game API route recovered. |

The packet parser found 297, 125, 44, 141, and 29 TCP directional flows respectively. In the last two captures, streams begin with TLS records rather than readable HTTP. TLS SNI/HTTP2 decryption was not attempted; there is no session-key log in these files.

## Blustone 1.1.2.0 — `blustone.pcap`

The capture establishes a useful request order and exact body classes:

1. `POST pv-prd.vshower.com/pv_launcher/check_acceptable` is form encoded. Its field names describe app/resource version, platform, device/OS, network, locale/language, and display resolution.
2. `POST pv-prd.vshower.com/shared_secret/Exchange` is form encoded with a `publicKey` field. This exposes the key-agreement endpoint and public key exchange, not the private key needed to decrypt the session.
3. `POST pv-prd.vshower.com/account/Login` is 512 bytes of `application/octet-stream`, i.e. opaque binary rather than readable form/JSON.
4. `POST pv-prd.vshower.com/pv_tracker/record_check_point` is form encoded. It includes checkpoint metadata and account/session association fields.
5. The game host `sr-prd.gshower.net` receives encrypted binary API requests. Ordinary reference/lobby calls in this capture are 80 bytes; `/tuto/Clear` is 96 bytes, `/mission/Start` 160 bytes, and `/mission/Complete` 256 bytes.
6. The CDN host receives plain HTTP `GET /_SR_PRD/<package>_<stamp>.pkg` requests. The capture visibly requests character package families such as `C###`, `C###_EFT`, and `C###_SND`, plus `AUTOPLAY`. The corresponding unpacked image trees are in `analysis/VSFan/Extracted Assets (2026)/1.1.2.0 (blustone.pcap, 2017-09-04)/`.

Reference-data routes visible in this build include:

- Character and combat data: `/reference/GetCard`, `/reference/GetCardBook`, `/reference/GetCardChain`, `/reference/GetCardRankUp`, `/reference/GetCardEnhancePrice`, `/reference/GetBattle`, `/reference/GetLevel`.
- Equipment/item, economy, and progression: `/reference/GetItem`, `/reference/GetSupply`, `/reference/GetShop`, `/reference/GetGacha`, `/reference/GetQuest`, `/dailyquest/GetRefList`, `/dailyquest/GetInstList`.
- Stage and monster data: `/reference/GetArea`, `/reference/GetStage`, `/reference/GetMonster`, `/reference/GetStageMonster`, `/reference/GetAbyss`.
- Supporting narrative/UI and owned-state calls: `/reference/GetDialog`, `/reference/GetScenario`, `/reference/GetNpc`, `/lobby/Enter`, `/lobby/GetMissionInst`, `/lobby/GetCardInven`, `/lobby/GetItemInven`, `/lobby/GetShopInst`, `/lobby/GetSupplyInst`, `/lobby/GetCardBook`, `/lobby/GetWeather`, `/lobby/GetAbyss`, `/scenario/GetList`.
- Activity: `/tuto/Clear`, `/mission/Start`, `/mission/Complete`.

This is the strongest PCAP for gameplay sequence and for identifying which reference responses could hold base hunter, level/rank growth, item/jewelry, monster, stage, mission, and reward tables. The request paths alone do **not** establish response field names or numeric values.

## Blustone 1.1.3.0 — `bs_transcendence.pcap`

The protocol shape remains the same: plain form launcher/key-exchange/tracker calls; a 512-byte opaque binary login body; and encrypted `application/octet-stream` game API requests, usually 80 bytes. The capture includes the same broad reference and lobby families as 1.1.2.0. Its notable extra route is `/reference/GetCardOvercome`, a potential lead for hunter limit-break/overcome stat progression.

Unlike the 1.1.2.0 session, this capture visibly fetches `/_SR_PRD/reslist_20170908141924.list`, followed by updated packages. The matching local file is `analysis/VSFan/Research/Blustone/Extracted Updates/1.1.3.0/reslist_20170908141924.txt`; its header reports resource version `20170908141924`, 149 entries, and 385,496,169 total bytes. The paired 1.1.2.0 reslist `reslist_20170904165634.txt` reports version `20170904165634`, 140 entries, and 379,438,483 total bytes. Reslist rows encode package name, package timestamp, byte size, a numeric flag, and a SHA-1 digest. These are useful for matching package revisions and asset provenance, not numeric hero-stat sources by themselves.

The corresponding extracted tree is `analysis/VSFan/Extracted Assets (2026)/1.1.3.0 (bs_transcendence.pcap, 2017-09-08)/`. The `.pkg` package listings and extracted per-package content give a route to character portraits, effects, and voice assets. Those can help identify heroes/skins and date variants, but no plaintext stat response was recovered from the PCAP.

## Other captures

### `btba_install.pcap`

This is a separate product/install flow: `/pv_gateway/record_app_state`, `/pv_launcher/check_acceptable`, `/account/Login`, `/pv_tracker/record_check_point`, `/pv_purchase/get_action_ref`, `/pv_purchase/get_ref_item`, `/pv_purchase/get_ref_coin`, and `/WI_contentgate/req_enter_game` appear before requests under `/_BTBA_PRD/`. It fetches story/chapter and localization/audio packages (for example `CHA_*`, `S1EP*`, `EXT_EN`, `UIP_EN`, and `SND*`). This may be useful for understanding VisualShower platform plumbing or the companion game's purchase/content-gate interfaces, but it is not evidence for Blustone hero, jewelry, monster, or reward numbers.

The account/login and content-gate requests include opaque `enc` data. Tracker and gateway forms contain account/session identifiers. The report deliberately records field names and route names only.

### `btba.pcap` and `whiteisland.pcap`

Both contain TCP/TLS flows but no readable HTTP request lines or Blustone API paths in the captured bytes. Without TLS secrets or a supported decrypted export, these sessions cannot presently yield endpoint bodies, game-reference values, or rewards. The user-provided files remain untouched.

## Payload confidentiality and compression

- **Game API bodies are encrypted at the application layer.** The clearest direct evidence is the opaque `application/octet-stream` request bodies and fixed request sizes. The already-existing VSFan note `analysis/VSFan/Research/Blustone/API Endpoints.md` also identifies the session-key exchange and says game bodies are encrypted. Because the PCAPs do not contain the client ephemeral private key/session-key log, the encrypted reference responses (`GetCard`, `GetMonster`, `GetItem`, etc.) cannot be decoded from these captures alone.
- **Platform bootstrap/tracker calls are partly readable form data.** Their names and field names are visible, but response data from launcher/account flows may carry an `enc` field. Public-key exchange is visible; secrets and values are not reproduced here.
- **CDN paths are plain HTTP, package bytes are binary files.** The captures show package URLs and request sequencing. Matching local extraction results include named package trees and raster assets; `bs_parsed` displays package entry metadata (for example `C002.pkg` contains a `C002.jetH` entry). That proves a structured package/container workflow, but does not prove whether every individual package/member is compressed or encrypted. No `Content-Encoding` header was found in the two Blustone PCAP byte streams; chunked transfer framing is present and is not itself compression.
- **BTBA/White Island TLS payloads are transport encrypted.** Their visible encrypted streams provide no readable request/response JSON. The BTBA install capture also has readable HTTP for some web/static assets, but those responses do not expose Blustone stat tables.

## Data value for the active stats/rebalance work

| Research target | PCAP opportunity | What remains unavailable |
|---|---|---|
| Heroes | `/reference/GetCard`, `GetLevel`, `GetCardRankUp`, `GetCardEnhancePrice`, `GetCardChain`, and (1.1.3.0) `GetCardOvercome`; the downloaded `C###`/EFT/SND assets can aid identity and variant matching. | No readable card-stat response or level/rank/equipment context, so no new strict base-stat row. |
| Jewelry / equipment | `/reference/GetItem` is the likely item catalog source; lobby item inventory and price/supply routes may reveal owned-state or economy if decrypted. | The request path does not prove which item records are jewelry; no item stat values are visible. |
| Monsters | `/reference/GetMonster` plus `/reference/GetStageMonster` provide the likely enemy-stat and encounter-table sources. | Both response bodies are encrypted; no monster numerical values or level context recovered. |
| Rewards / progression | `/reference/GetStage`, `/reference/GetQuest`, `/dailyquest/GetRefList`, `/reference/GetGacha`, `/reference/GetShop`, `/mission/Complete`, and supply routes identify likely sources for stage, mission, daily, gacha, shop, and clear rewards. | Route visibility alone does not reveal reward records or quantities. |

**Stats-goal credit from these five captures: none.** They materially improve the protocol/source map and show where future decoded or extracted evidence should be sought, but do not independently prove any missing hero, jewelry, or monster stat value. The locally extracted 1.1.2.0/1.1.3.0 image/package trees may still support the separate polluted/unclear-hero identity and variant notes.

## Redaction and handling

The captures contain account/session-associated fields such as `pvid`, login `enc` blobs, checkpoint/tracker values, and tracking keys/IDs. These values were neither copied into this file nor printed in its examples. No raw credential, token, cookie, account ID, or personal user value is included. Original files under `analysis/VSFan/` were only read; none was modified or removed.

## Evidence map

- `blustone.pcap`: timestamps, launch/form routes, 80/96/160/256-byte encrypted API request classes, 1.1.2.0 reference/lobby/mission paths, and `_SR_PRD` package GETs.
- `bs_transcendence.pcap`: timestamps, 1.1.3.0 reference/lobby paths including `GetCardOvercome`, and the 2017-09-08 reslist fetch.
- `analysis/VSFan/Research/Blustone/API Endpoints.md`: existing decoded route catalog and note on session encryption; used as cross-check, not as independent plaintext response evidence.
- `analysis/VSFan/Research/Blustone/Extracted Updates/1.1.2.0/reslist_20170904165634.txt` and `.../1.1.3.0/reslist_20170908141924.txt`: package counts, aggregate byte totals, per-package versions/sizes/digests.
- `analysis/VSFan/Research/Blustone/Extracted Updates/{1.1.2.0,1.1.3.0}/bs_parsed/`: package-entry metadata; `analysis/VSFan/Extracted Assets (2026)/{1.1.2.0...,1.1.3.0...}/`: extracted visual/audio/package member trees.
- `btba_install.pcap`, `btba.pcap`, and `whiteisland.pcap`: additional product/platform context, documented above; not Blustone stat evidence.
