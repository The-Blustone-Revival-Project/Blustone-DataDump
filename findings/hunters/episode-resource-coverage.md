# Recovered Episode catalog and resource coverage

2026-10-05. Read-only original PAD JETs, exported LevelDB/reference JSON, native symbols/original Thumb and existing episode reports. No exports duplicated: systems owns EPISODE_S01.json export. No originals/client/VM/Ghidra/server changes.

## Real original catalog

`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/R_EPISODE.jet` is **38080bytes/66records**, exact header walk endingatfilesize. Each namedRW body decompresses to RW+u32length+UTF8JSON (content starts+6; UTF8 BOM tolerated). Names use verifiednativeuint64/base38headerdecoder. This is actual episode data, not a title-string table or texturepack.

Verified records: SEASON_LIST (offset977, JSON["season1"]), SEASON1 (offset1032,80826contentbytes), EVENT(offset0), TUTO(offset16216), STAT(offset4324,383817bytes) and CB*/EVCB* battle definitions. STAT contains original **episode-tuned actor stats**, not provedordinaryhunterbasevalues; do not import them as globalhunterbalance.

SEASON1 root type=season,id=S01,title=S01_TITLE,childs=[...]. It has **18 chapters E01..E18**, with child counts **7,8,7,4,8,7,5,7,7,7,8,7,8,7,8,9,9,5** (128story nodes). First real leaf: type=story,id=E01_S01,title=E01_S01_TITLE,res1=EP_DIA_4,res2=C003_DIALOG,pos={localname:local_MIDGARD,x:1235,y:1150},entrypoint=EP_0301A,battle=false. TUTO rootidTUTORIAL contains T00/T00_S01 etc. No arbitraryepisodeIDs are needed.

`EPISODE.jet` is a separate **6529928byte/128record artpack**, exactwalk; inspectedresources are images/animation art, noJSONcatalog. BothR_EPISODE andEPISODE originalfilesexist. ST001..ST007 artfilesalsoexist. Filename existence alone doesnotprovecompleteactor/dialoguebinding.

## Native loading contract, separate from server API

Original **CSRMEpisode::LoadData Gb1a618** clearslinks, calls ReadJson with literal **season_list** (Gb1a6ac/callGb1a6bc), iterates returnedJSONseason names intoSeasonParserGb1aec0; separatelyloads **event** and **tuto** literals (Gb1a792/Gb1a7be), registersread/clearIDs.

**ReadJson Gb1a8b0** has a debug/file path ending`.JSON` and CMLoadTextRaw; normalresourcepath calls **CRMResourceMgr4::LoadRawData G10eac8c atGb1abd4**, splits slashpath and traversesJSONsubtrees. Thus Episode definitions are **local namedRWresources**, not a missing /reference/GetEpisode route. Loadercase normalization/subpathdetails requireparentfullReadJsondecomp ifneeded; rawheadernamesuppercase and native literalslowercase shouldnotbechangedbyguessingaliases.

Server routes are separately /episode/GetLog,/episode/Read,/episode/Reward, with native RequestReadOrClear/RequestClear sharingthefamily. Existing episode-route-table.md ishistorical aboutserverimplementation/runtimecalls; refreshsourcebeforefuturestatusclaims. GetLog read_log/reward_log uses actualidstrings; realcatalog enablesdurableprogressidentity without replacinglocalresourcegraph.

## Current CDN seam

Default launcher stillserves11top-levelpackages, with extraoriginalJETassets folded into **E_NEW** by `server-ts/src/server.ts::packageTreeEntries` andtools/start-server.ps1. Currentdefault cardglobC001..C006 plus8stageassets does **not explicitlyinclude R_EPISODE/EPISODE**. TheymayalreadybeAPK-bundled; CDNomissionisnotproofnativeabsence.

A server-only candidate is additive folding of originalR_EPISODE.jet andEPISODE.jet through explicitRESOURCE_ASSET_NAMES_EXTRA/assetprofile, preservingexisting11+card/stageentries and normalmanifest/hash/download lifecycle. This wouldnotrequireAPKrebuild. Do not advertisea newresourceversionorwidenliveprofilebeforedependencies/auditsarecomplete; successfuldownloadaloneisnotnativeLoadRawData/readinessproof.

## Confirmed localization; remaining dependencies unknown

`analysis/recovered-reference/UI_EPISODE.json` has **297localizedrecords**, includingE01..E18chapter/storytitlekeys andlocalmapnames. Itislocalizationonly, nottheepisodeLINKcatalog.

Firstleafrequires EP_DIA_4,C003_DIALOG and actualdialogue entrypointEP_0301A; battledefs separatelyname CB*/EVCB* actorIDs,fieldbackground/BGM and win/lose dialogueIDs. A boundedscanof exported UI_JSON_RO/UI_XML_RO found **no EP_0301A,AD00002B2 orEP_DIA_4 key/value hits**. This provesabsencefromthoseexportedtablesonly; originaldialoguefiles/otherresourcecontainers couldstillprovide them. Theircompleteavailability/loadingdescriptor is **unresolved**, notclaimedmissingfromthewholegame. CurrentC003familyfilesexist butres2binding isnotverifiedbyfilenamealone.

EVENT schedules/rewardvalues areoriginalserializedcontent, butcurrentdateavailabilityandserverclaimreceiptsareseparatecontracts. Preserveoriginalrecords; do not inventrewardamounts oractivatehistoricaleventssolelybecausecatalogexists.

## Actionable next unit

1. Use systems' immutablecatalogexport toderivevalidnode/read/clearIDs,requiredparentsandbattleflag; implementdurableread/clearonly againstthoseIDs withowner/replayvalidation.
2. ParentfocusedLoadDataGb1a618/ReadJsonGb1a8b0/SeasonParserGb1aec0/RecursiveParserGb1b45c decomp preservesnativegraph/pathproof ifneeded; no newIDscheme.
3. Inventorydependencysets fromcatalog: dialogueentrypoints,res1/res2,mapart,battleactor/background/BGM; establishactualnativeconversationsourceandrecordpresence beforeCDNadvertisement/claimingstoryplayable.
4. Thenaddonlyrequiredoriginalpacks toexplicitCDNprofile and observeLoadRawData catalog plusoneactualnonbattle story opener. Serverread/clearpersistencealoneisnotverifieddialogueplayback.

This unit confirmsusableoriginalcatalog/localization andnativeRWloader, withdialogue/artclosureunknown. No reward,readflag,storylaunchorassetprofilewasmutated.
