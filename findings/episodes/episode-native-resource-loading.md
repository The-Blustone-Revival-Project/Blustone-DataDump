# Episode native resource dependency and case normalization

2026-10-05. Read-only original ELF Thumb, episode catalog exports, server.ts packageTreeEntries and start-server.ps1. No Ghidra/VM/device/source edits or resource aliases. Code coordinates are Ghidra addresses (ELF VA plus10000hex).

## Catalog chain is native local-resource loading

CSRMEpisode.LoadData **Gb1a618** constructs the string **season_list** atb1a6b0 and calls **ReadJson Gb1a8b0 atb1a6bc**. Each resulting collection element goes to **SeasonParser Gb1aec0 atb1a742**. SeasonParser converts its element to a string atb1aee8 and calls ReadJson again atb1aef4. The shipped list ["season1"] therefore supplies a resource name to load, while that resource's JSON graph root idS01 is separate gameplay identity. LoadData also loads event and tuto resources; no GetEpisodeRef HTTP route is needed or recovered.

ReadJson has a localized path selected by a DataMgr byte and a normal fallback. The localized path appends .JSON atb1a91a. The **normal path atb1aa38** splits the requested string by '/', retains the resource name, and calls **CRMResourceMgr4.LoadRawData G10eac8c atb1abd4 with reloadfalse**. Local resource identifiers must not be confused with paths served directly through an imagined episode endpoint.

## Case mismatch is already handled by the engine

LoadRawData first calls **FindResource G10e97b4 at10eacc0** when reloadfalse. FindResource copies the requested name into its own string at10e97ee, then loops over **every character**, calling **toupper at10e9812**, writing back at10e9816, before looking up its resource-name hash map at10e9830. Thus the resident-resource lookup is case-normalized, not raw case-sensitive CMHashID comparison.

If absent, LoadRawData calls **LoadResourceFromFile G10e9704 at10eace8**. That method calls **CRMResMap.GetResInfo G75dda8 at10e972c**. GetResInfo independently copies the key, **toupper at75de0a/store75de0e**, then looks up its map at75de1c. Both resident and file-descriptor fallback paths therefore normalize case. The observed loader strings **season_list/season1** can resolve descriptors **SEASON_LIST/SEASON1** using the existing native mechanism. No lowercase descriptor duplication, manual hash alias or APK patch is justified merely by their spelling difference.

This proves case behavior for these ASCII names. It does not claim arbitrary Unicode locale normalization, successful runtime load or contents of a missing descriptor. The character lane separately inventories original descriptor names and offsets; rootS01 alone is not proof of a descriptor name.

## Original JET folding is a server/CDN dependency, not JSON replacement

In **server.ts packageTreeEntries**, when packageBase isE_NEW.JET and BLUSTONE_RESOURCE_ASSET_DIR is configured, the server reads the explicitly selected BLUSTONE_RESOURCE_ASSET_NAMES (or glob matches), validates file basenames/existence, and pushes **{name,payload:readFileSync(assetPath)}** into the PKGI package. It deduplicates case-insensitive filenames. The actual **original JET bytes are included verbatim**, so curated JSON exports do not automatically replace the native descriptor/container content.

**tools/start-server.ps1** chooses the preserved public PAD asset directory when present, merges BLUSTONE_RESOURCE_ASSET_NAMES_EXTRA into the folded set, and refuses selected missing files before startup. Its default card art selection is C001..C006 family glob. At this inspection, no default explicit R_EPISODE/EPISODE addition was found; a parent-selected EXTRA/glob is required to fold them. Existing active process configuration/download completion was not inspected by this lane. Merely adding an HTTP /episode/Read handler cannot populate native local story resources.

Original public sources available:

- R_EPISODE.jet:38080bytes, SHA2567f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e. Native JSON catalog, STAT and combat records; curated exports and hashes live in EPISODE_S01.manifest.json and EPISODE_COMBAT_STAT.manifest.json.
- EPISODE.jet:6529928bytes, SHA2567bc7b12c57847e690648286170167b2d14ab9207d6df21d35c87f7c6b909ed30. Distinct art container; no JSON catalog in the read-only decode.

A resource promotion must use the project's normal consistent CDN version/manifest/package process so native CPVCDN2 actually materializes the selected JETs. This report performed no promotion or native load test.

## Actual first-story dependencies and limits

Recovered E01_S01 is a story node with **entrypointEP_0301A**, res1EP_DIA_4, res2C003_DIALOG, local_MIDGARD position, battlefalse. E01_S02 isEP_0302A/local_GYM, battletrue, with linked episode combat data. These are original local narrative/resource relationships; they are not mission-stage aliases. Conversation resources/art and actor dependencies must exist before native story UI or story battle is claimed complete. This unit did not trace every narrative request caller or verify those materials downloaded.

The safe next dependency seam is original descriptor/catalog/art serving plus encoded Episode progress persistence already recovered, followed by a bounded normal UI story entry. Preserve original season/event schedules; no manual story state, broad aliases, direct scene jumps or fabricated reward materials follow from this loader proof.

## Read-only audit of opt-in profile and CDN verifier

Initial tools/episode-resource-profile.ps1 and server-ts/scripts/verify-episode-cdn.ts were inspected source-only. Profile validates12 existing public JET files and minimum sizes, prints hashes, and changes no VM/server state itself. It keeps an already-set ASSET_NAMES list and appends selected packs; InspectOnly skips environment mutations. Native C003_DIALOG generation/playback remains explicitly unresolved.

Two concrete initial-source bugs were sent to parent:

- Profile merges into **BLUSTONE_EXTRA_STAGE_ASSETS**, but start-server.ps1 reads **BLUSTONE_RESOURCE_ASSET_NAMES_EXTRA**. In the documented fresh-shell order, where ASSET_NAMES is unset, sourcing this profile then start-server fails to select any of its12 packs. The verifier directly sets ASSET_NAMES and therefore does not exercise this broken profile flow. Use the actual consumed EXTRA variable while preserving its previous entries.
- Verifier sets ASSET_NAMES12 but leaves inherited **BLUSTONE_RESOURCE_ASSET_GLOB** intact. A shell with C*.jet or another wide glob makes server.ts fold additional files, potentially hundreds of MB, although the verifier still asserts only its12 target payloads. Explicit empty GLOB in its saved/restored settings makes that verification bounded and isolated from the calling profile.

Otherwise the inspected verifier creates an in-memory ServerState and an ephemeral loopback-only listener, checks advertised full-package MD5, resource stamp/counts, PKGI1 record size/offset payloads byte-for-byte and a206 byte-range response, then closes the listener and restores its modified environment variables. It does not read host account state through createApp's absent stateFile. No VM action or test run was performed by this audit lane. Fix status and native playback remain unclaimed here.
