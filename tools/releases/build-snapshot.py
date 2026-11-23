"""Build immutable dated stats/evidence documents from this repository's data."""
from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import argparse,csv,hashlib,json,re,subprocess

ROOT=Path(__file__).resolve().parents[2]
DATASETS={
 'balance_followup':'datasets/gameplay/balance-observations.json',
 'snowfields_gameplay':'datasets/campaign/snowfields-gameplay.json',
 'hunter_level_one_panels':'datasets/hunters/level-one-panels.json',
 'historical_market_quotes':'datasets/economy/market-quotes.json',
 'hunter_identities':'datasets/hunters/identities.json',
 'hunter_stat_observations':'datasets/hunters/stat-observations.json',
 'hunter_skill_reference':'datasets/hunters/skill-reference.json',
 'monster_identities':'datasets/monsters/identities.json',
 'campaign_identifiers':'datasets/campaign/stage-identifiers.json',
 'episode_story_graph':'datasets/episodes/story-graph.json',
 'episode_rewards':'datasets/economy/episode-rewards.json',
 'hunter_gear_identities':'datasets/equipment/hunter-gear-identities.json',
}
REPO='https://github.com/The-Blustone-Revival-Project/Blustone-DataDump'
DERIVATIONS={
 'hero_at_draw_estimates':('findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-11-23.tsv','catalog_id'),
 'accessory_stat_estimates':('findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv','item_name_en'),
 'monster_stat_estimates':('findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv','catalog_monster_id'),
 'skill_magnitude_estimates':('findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv',('card_id','slot')),
}
RESEARCH='findings/balance-research-2026-11-23.md'
def load_derivations():
 rows={}
 for name,(rel,key) in DERIVATIONS.items():
  with (ROOT/rel).open(encoding='utf-8-sig',newline='') as f:raw=list(csv.DictReader(f,delimiter='\t'))
  out=[]
  for r in raw:
   rid='-'.join(str(r[k]) for k in ((key,) if isinstance(key,str) else key))
   out.append({'id':rid,**{k:(v if v!='' else None) for k,v in r.items()}})
  rows[name]=out
 return rows
def load(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def digest(data):return hashlib.sha256(data).hexdigest()
def cell(value):return str(value if value is not None else 'Unknown').replace('|','\\|').replace('\n',' ')
def table(header,rows):
 return '\n'.join(['| '+' | '.join(header)+' |','|'+'|'.join('---' for _ in header)+'|']+
                   ['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])+'\n'
def tables(path):
 lines=(ROOT/path).read_text(encoding='utf-8-sig').splitlines();result=[];section='';i=0
 while i<len(lines):
  if lines[i].startswith('#'):section=lines[i].lstrip('# ').strip()
  j=i+1
  while j<len(lines) and not lines[j].strip():j+=1
  if lines[i].startswith('|') and j<len(lines) and re.match(r'^\|[\s:|\-]+\|?$',lines[j]):
   start=i;block=[lines[i],lines[j]];i=j+1
   while i<len(lines):
    if lines[i].startswith('|'):block.append(lines[i]);i+=1
    elif not lines[i].strip() and i+1<len(lines) and lines[i+1].startswith('|'):i+=1
    else:break
   result.append({'section':section,'line':start+1,'markdown':'\n'.join(block),'source':path,
                  'sha256':digest((ROOT/path).read_bytes())})
  else:i+=1
 return result
def current_date():
 try:return datetime.now(ZoneInfo('Asia/Jerusalem')).date().isoformat()
 except Exception:raise SystemExit('Pass --date YYYY-MM-DD when IANA timezone data is unavailable')
def compare(datasets,previous):
 old=previous.get('datasets',{}) if previous else {};result={}
 for name,rows in datasets.items():
  before={str(r['id']):r for r in old.get(name,[])};after={str(r['id']):r for r in rows}
  result[name]={'added':len(after.keys()-before.keys()),'removed':len(before.keys()-after.keys()),
               'changed':sum(before[k]!=after[k] for k in before.keys()&after.keys()),
               'unchanged':sum(before[k]==after[k] for k in before.keys()&after.keys())}
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--date',default=None)
 p.add_argument('--revision',type=int,default=1);p.add_argument('--previous-json',type=Path);p.add_argument('--out',type=Path)
 args=p.parse_args();as_of=args.date or current_date();date.fromisoformat(as_of)
 if args.revision<1:raise SystemExit('Revision must be positive')
 version=as_of+('' if args.revision==1 else '.'+str(args.revision))
 out=args.out or ROOT/'releases'/version
 if out.exists():raise SystemExit('Snapshot already exists; choose the next same-day revision')
 datasets={name:load(ROOT/path) for name,path in DATASETS.items()}
 previous=load(args.previous_json) if args.previous_json else None
 changes=compare(datasets,previous)
 derivations=load_derivations()
 changes.update(compare(derivations,{'datasets':previous.get('derivations',{}) if previous else {}}))
 coverage=load(ROOT/'catalog/coverage.json')
 curated=[]
 for path in ['datasets/hunters/observed-stats/051.md','datasets/hunters/observed-stats/010_1.md','datasets/hunters/observed-stats/010.md','datasets/equipment/GEAR.md']:
  curated+=tables(path)
 extra='findings/resources/vsfan-extracted-assets.md'
 if (ROOT/extra).exists():curated += [t for t in tables(extra) if 'jewel set' in t['section'].lower()]
 latest='findings/hunters/base-stats-visual-hunt/jewel-help-locales-2026-10-05.md'
 curated += [t for t in tables(latest) if t['section'].startswith(('1.4 ','1.5 ','2.2 '))]
 lane='findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/scrape-consolidation-2026-10-14.md'
 curated += [t for t in tables(lane) if t['section'].startswith(('2. Hit census','3. Back-calculation'))]
 curated += tables('findings/hunters/base-stats-visual-hunt/panel-adjudication-2026-10-17.md')
 def indexed_tables(rows):
  result=[];seen={}
  for row in rows:
   key=row['source']+'::'+row['section']+'::'+row['markdown'].splitlines()[0]
   seen[key]=seen.get(key,0)+1
   result.append({'id':key+'::'+str(seen[key]),**row})
  return result
 changes.update(compare({'curated_source_tables':indexed_tables(curated)},
   {'datasets':{'curated_source_tables':indexed_tables(previous.get('curated_source_tables',[]))}} if previous else None))
 sources=[{'path':path,'sha256':digest((ROOT/path).read_bytes()),'records':len(datasets[name])} for name,path in DATASETS.items()]
 observation_sources={row['provenance']['path'] for name in ('snowfields_gameplay','hunter_level_one_panels','historical_market_quotes') for row in datasets[name]}
 observation_sources.update(row['transcript_path'] for row in datasets['historical_market_quotes'])
 followup=datasets['balance_followup']
 observation_sources.update(row['provenance']['path'] for row in followup)
 observation_sources.update(ref['provenance']['path'] for row in followup for ref in row['sources'] if 'provenance' in ref)
 for path in sorted({t['source'] for t in curated} | observation_sources | {RESEARCH}):
  sources.append({'path':path,'sha256':digest((ROOT/path).read_bytes())})
 for rel in [rel for rel,_ in DERIVATIONS.values()]:
  sources.append({'path':rel,'sha256':digest((ROOT/rel).read_bytes())})
 snapshot={'format_version':1,'version':version,'as_of':as_of,'timezone':'Asia/Jerusalem',
           'previous_version':previous.get('version') if previous else None,'coverage':coverage,
           'changes':changes,'datasets':datasets,'derivations':derivations,'curated_source_tables':curated,'sources':sources,
           'limitations':['As-of date describes this research snapshot, not original game version or observation date.',
             'Historical 2019 observations do not establish unequipped final-version base stats.',
             'At-draw state is unverified for all 62 Tier A archive tuples. Dependent estimates inherit that uncertainty.',
             'Battle HP includes party effects. Each Snowfields payout was observed once. Shop quotes apply to the pictured lot.',
             'Missing values remain unknown; conflicting and contaminated observations are retained separately.']}
 link=lambda path:f'{REPO}/blob/{version}/{path}'
 def reference_links(row):
  links=[]
  for ref in row['sources']:
   if 'url' in ref:
    links.append(f"[Footage {len(links)+1}]({ref['url']})")
   elif 'image_id' in ref:
    links.append(f"[Image {ref['image_id']}]({link(ref['transcript_path'])}#L{ref['transcript_line']})")
   else:
    links.append(f"[Original record]({link(ref['document'])})")
  return ' · '.join(links)
 stats=[f'# BLUSTONE Stats — {version}',f'\nResearch snapshot as of **{as_of} (Asia/Jerusalem)**. This date is a publication cutoff; each observation retains its own historical capture date and context.\n',
 '## What this snapshot establishes\n',
 f"{coverage['character_rows']} catalogue rows ({coverage['playable_character_rows']} playable identities), {coverage['monster_identities']} monster identities, {coverage['numeric_historical_stat_claims']} historical numeric claims across {coverage['historical_rows_with_numeric_hp']} archived profiles with numeric HP. Symbolic formulas and original identifiers are preserved. Derived estimates (113 hero at-draw rows, 100 accessory rows, 22 monster rows, 565 skill rows, fixture rows excluded) are listed below with per-row class and confidence; unestimated values remain unknown.\n",
 '## Changes since the previous snapshot\n',
 'Initial published baseline; all included dataset records are introduced here.\n' if not previous else f"Compared with **{previous['version']}**. A changed record includes changed context or provenance, not necessarily a new numerical value.\n",
 table(['Dataset','Added records','Changed records','Removed records'],[(k,v['added'],v['changed'],v['removed']) for k,v in changes.items()]),
 '## Hunter growth, repeat expeditions, market stock and combat timing\n',
 table(['Subject','Era','Observation','Sources'],[[r['subject'],r['era'],r['summary'],reference_links(r)] for r in followup]),
 '## Original gameplay and shop observations\n',
 'Full battle HP and settled Rupees for the same party. Each area has one observed clear.\n',
 table(['Snowfields area','Entry level','Protagonist HP','Tyltyl HP','Fuel','Hunter levels gained','Collected Rupees','Footage'],
       [[r[k] for k in ('area','entry_level','protagonist_hp','tyltyl_hp','fuel','hunter_levels_gained','collected_rupees')]+[f"[Spawn]({r['spawn_url']}) · [Result]({r['result_url']})"] for r in datasets['snowfields_gameplay']]),
 'Level-one Hunter detail panels. The month dates the upload. Equipment and exact client build are unknown.\n',
 table(['Hunter','Era','Upload month','Stars','HP','ATK','DEF','Speed','Strength','Footage'],
       [[r[k] for k in ('hunter','era','upload_month','stars','hp','atk','def','attack_speed','strength')]+[f"[Panel]({r['detail_url']})"+(f" · [Strength]({r['strength_url']})" if r['strength_url'] else '')] for r in datasets['hunter_level_one_panels']]),
 'Prices apply to the entire displayed lot. Dates come from screenshot filenames.\n',
 table(['Date','Era','Shop or panel','Item','Quantity','Lot price','Currency','Source'],
       [[r[k] for k in ('filename_date','era','shop','item','quantity','lot_price','currency')]+[f"[Image {r['image_id']}]({link(r['transcript_path'])}#L{r['transcript_line']})"] for r in datasets['historical_market_quotes']]),
 '## Historical hunter profile readings\n',
 'These are display readings from the archived 2019 database. Level, rank and equipment are not established. None of these archive claims counts as recovered base-stat evidence. Attack speed uses source display units; native conversion is not established.\n']
 identities={r['id']:r['claims']['name']['value'] for r in datasets['hunter_identities']};groups={}
 for row in datasets['hunter_stat_observations']:
  rowid=row['id'].rsplit('-',1)[0];groups.setdefault(rowid,{'entity':row['entity_id'],'values':{},'context':row['context'],'url':row['provenance'].get('original_url')})
  groups[rowid]['values'][row['measure']]=row['value']
 measures=['hp','atk','def','speed','crit','crit_damage','penetration','block','block_damage_reduction','element_enhance','element_resistance','hp_regen']
 stats.append(table(['ID','Name']+measures+['Capture','Level / gear'],[
  [r['entity'],identities.get(r['entity'],'Unknown')]+[r['values'].get(m) for m in measures]+[r['context']['capture_timestamp'],str(r['context']['level'])+' / '+str(r['context']['gear_state'])] for r in groups.values()]))
 stats += ['## Curated screenshot and equipment observations\n',
 'The tables retain their dated interpretations. The November review supersedes the October at-draw classification. Beckhen 051 has a visually checked unequipped Lv.30 column; it is not a Lv.1 growth curve. Vincent 010_1 has unknown gear and cannot establish unequipped base values. Gear/jewel tables describe observed samples, not full distributions.\n',
 'The historical GEAR table contains unresolved wording. Later evidence corroborates flat +23 Element/Resistance set values, while the old 1.4.4.1 Super Block differs by locale (KO 9%; EN/JP/ZH/ZT 5%). The included 2.8.0.1 help comparison records the renamed Reduction effect at 10% for KO/EN/JA/TC, while SC preserves a distinct older wording/value. Help-copy values are not native runtime proof. The ATK subtotal discrepancy remains unresolved. Read the evidence document before using these numbers.\n']
 for entry in curated:
  stats += [f"### {Path(entry['source']).stem}: {entry['section']}\n",entry['markdown']+'\n',
            f"Source: [{entry['source']}]({link(entry['source'])}#L{entry['line']}); SHA-256 `{entry['sha256']}`.\n"]
 stats += ['## Derived at-draw and balance estimates\n',
 'Under the 2026-10-11 derivation-counts policy, derivation from recovered mechanics plus source-backed anchors counts as documentation, with per-row class and confidence; `[INFERRED-FIXTURE]` never counts. The November review classifies all 62 Tier A archive tuples as estimates when used for at-draw stats. Level and equipment are unverified. Estimates and historical confidence bands that use these tuples inherit that uncertainty. Tier-B/C hero point estimates are band centres (exact-tuple confidence is much lower than band confidence); monster rows are per-encounter tuples, not permanent base stats; skill fixture rows are excluded from the JSON.\n']
 heroes=derivations['hero_at_draw_estimates']
 stats.append(table(['ID','Name','Role','Rar','HP','ATK','DEF','Tier','Confidence'],
  [[r['catalog_id'],r['name'],r['role'],r['rarity'],r['hp_at_draw'],r['atk_at_draw'],r['def_at_draw'],r['tier'],r['confidence']] for r in heroes]))
 accs=derivations['accessory_stat_estimates']
 stats.append(table(['Accessory','Slot','MaxHP@50','Tier','Point/Band'],
  [[r['item_name_en'],r['slot'],r['max_hp_lv50'],r['tier'],str(r['confidence_point_pct'])+' / ±'+str(r['confidence_band_pct'])] for r in accs]))
 mons=derivations['monster_stat_estimates']
 stats.append(table(['Pack','Rank','HP','ATK','DEF','Tier','Point conf'],
  [[r['catalog_monster_id'],r['rank'],r['hp'],r['atk'],r['def'],r['tier'],r['confidence_point_pct']] for r in mons]))
 from collections import Counter as _Counter
 skillgroups=_Counter((r['archetype'],r['class']) for r in derivations['skill_magnitude_estimates'])
 stats.append(table(['Skill archetype','Class','Rows'],
  [[a,c,n] for (a,c),n in sorted(skillgroups.items(),key=lambda x:(-x[1],x[0][0] or '',x[0][1] or ''))]))
 stats += ['## Monster stats and remaining gaps\n','22 art identities are catalogued; episode-table monster tuples for 22 monster res_ids are listed under Derived estimates above (12 packs anchored, 10 estimated). Expedition monster stats remain server-side and unshipped; campaign entries enumerate 50 IDs from analytics data, not recovered difficulty or AP cost.\n',
           f"Detailed coverage and unresolved claims: [coverage ledger]({link('findings/hunters/base-stats-visual-hunt/coverage.md')}).\n"]
 evidence=[f'# BLUSTONE Evidence and Coverage — {version}',f'\nAs of **{as_of} (Asia/Jerusalem)**; source observation dates remain separate.\n',
 '## Evidence classes\n','- RECOVERED: original extracted record with exact file/key/chunk locator.\n- COMMUNITY-SOURCED: source-backed page/archive/screenshot claim.\n- INFERRED: explicit derivation or hypothesis.\n- INFERRED-FIXTURE: replica policy; not original-game evidence.\n- UNKNOWN: missing or unresolved.\n',
 '## Dataset coverage\n',table(['Dataset','Records','Pinned source'],[(name,len(datasets[name]),path) for name,path in DATASETS.items()]+[(name,len(derivations[name]),dict(DERIVATIONS)[name][0]) for name in DERIVATIONS]),
 '## Reading the stats document\n','Archive claims retain original URL, capture timestamp, raw text, units, identity match and unknown state fields in BLUSTONE-Stats.json. Screenshot tables carry a pinned document hash and source-line locator. Do not merge measurements at different levels, ranks or equipment states. White/green display separation is evidence for one observed build, not proof of final-version balance.\n',
 '## November observations and open research\n',
 (ROOT/RESEARCH).read_text(encoding='utf-8').replace('](hunters/', f']({link("findings/hunters/")}').replace('](gameplay/', f']({link("findings/gameplay/")}').replace('](economy/', f']({link("findings/economy/")}').split('\n',1)[1],
 '## Conflicts and known limits\n','- The 62 archive tuples are historical display readings. Their at-draw level and equipment remain unverified. The November classification supersedes the October interpretation.\n- Beckhen 051 Lv.30 equipment ATK has a 78-point unreconciled subtotal.\n- Vincent 010_1 equipment state is unknown.\n- The 1.4.4.1 Super Block locale conflict and the distinct 2.8.0.1 Reduction wording/reordered help table are preserved; do not collapse eras or locales.\n- Monster episode rows are per-encounter tuples; monster display names stay unknown.\n- Tier-B/C hero point estimates are band centres; exact-tuple confidence is 2–25%.\n- Original reward IDs are separate from server settlement mappings.\n- No native battle, phone operation or new stat measurement is implied by publishing this snapshot.\n',
 '## Derivation sources and methods\n','Per-row class (`[RECOVERED]` / `[DERIVED-ESTIMATE]`), confidence and method live in BLUSTONE-Stats.json under `derivations`. `[INFERRED-FIXTURE]` rows are excluded from the snapshot payload. Methods: hero archive-level derivation (`findings/hunters/base-stats-visual-hunt/archive-level-derivation-2026-10-11.md`), hero archetype model (`findings/hunters/base-stats-visual-hunt/hero-archetype-guesstimate-2026-10-11.md`), accessory model (`findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/REPORT.md`), monster model (`findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/REPORT.md`), skill model (`findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/REPORT.md`). The four estimate TSVs are fingerprinted in the sources table above.\n',
 '## Source fingerprints\n',table(['Source path','SHA-256'],[(r['path'],r['sha256']) for r in sources]),
 '## Reproduce this release\n',f'Check out tag `{version}`, run `python tools/normalize/validate-datasets.py`, then `python tools/releases/build-snapshot.py --date {as_of} --revision {args.revision} --out local/reproduced/{version}`. Use the previous release\'s BLUSTONE-Stats.json with `--previous-json` when applicable.\n',
 '## Integrity\n','SHA256SUMS.txt pins the two documents, the JSON snapshot and the release manifest. The release manifest pins every dataset source used to construct this snapshot. Private captures, cookies, saves, signing keys and raw account telemetry are excluded.\n']
 notes=f'''# Blustone DataDump {version}\n\nStats and evidence snapshot as of {as_of} (Asia/Jerusalem).\n\n## Included\n\n- **BLUSTONE-Stats.md:** repeat expedition payouts, observed combat timing, historical Hunter values, curated screenshot/equipment tables, original IDs and explicit unknowns.\n- **BLUSTONE-Evidence.md:** source classes, coverage, conflicts, source hashes and reproduction instructions.\n- **BLUSTONE-Stats.json:** all {len(datasets)} normalized datasets, derived estimate tables (113 hero at-draw rows, 100 accessory rows, 22 monster rows, 565 skill rows), curated source tables and machine-readable changes from the previous release.\n- **RELEASE-MANIFEST.json** and **SHA256SUMS.txt:** reproducibility and integrity.\n\n## Changes\n\n- The first seven observed Snowfields victories pay 378 Rupees in total. Full battle HP readings now extend to starter level 26. Three level-one Hunter panels carry upload-era context.\n- The market ledger records {len(datasets['historical_market_quotes'])} priced offers across {len({r['image_id'] for r in datasets['historical_market_quotes']})} dated screens, including ordinary Market lots and separate purchase screens.\n- Added {len(followup)} observations on Hunter progression, repeat expeditions, combat and Market stock. Midgard Snowfields Area 4 paid 54 Rupees on first clear and 1,098 across 20 guided dispatches. The starting Captain reached Strength 586 at one star, level 30 and 799 after advancement to two stars, level 1. Episode 13 and 15 replays show the combat clock pausing during skill animations.\n- Reclassified 62 Japanese archive tuples as uncalibrated at-draw estimates. Their recorded numeric values are preserved.\n\n{'Initial research baseline.' if not previous else 'Compared with '+previous['version']+'.'}\n\n{table(['Dataset','Added','Changed','Removed'],[(k,v['added'],v['changed'],v['removed']) for k,v in changes.items()])}\n\n## Coverage and limits\n\n121 catalogue rows /113 playable identities;22 monster identities;806 numeric historical claims;50 campaign IDs;147 Episode nodes;1070 symbolic skill records. Derived estimates carry per-row class and historical confidence; fixture rows are excluded from the payload. Conflicting jewel values and incomplete monster/base-stat evidence remain visible.\n'''
 out.mkdir(parents=True)
 (out/'BLUSTONE-Stats.md').write_text('\n'.join(stats),encoding='utf-8',newline='\n')
 (out/'BLUSTONE-Evidence.md').write_text('\n'.join(evidence),encoding='utf-8',newline='\n')
 (out/'BLUSTONE-Stats.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 manifest={'version':version,'as_of':as_of,'timezone':'Asia/Jerusalem','previous_version':snapshot['previous_version'],'sources':sources,
           'files':[{'name':name,'sha256':digest((out/name).read_bytes()),'bytes':(out/name).stat().st_size} for name in ['BLUSTONE-Stats.md','BLUSTONE-Evidence.md','BLUSTONE-Stats.json']]}
 (out/'RELEASE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
 (out/'SHA256SUMS.txt').write_text(''.join(digest(f.read_bytes())+'  '+f.name+'\n' for f in sorted(out.iterdir()) if f.is_file()),encoding='utf-8',newline='\n')
 (out/'RELEASE-NOTES.md').write_text(notes,encoding='utf-8',newline='\n')
 print(json.dumps({'version':version,'output':str(out),'previous_version':snapshot['previous_version'],'files':6}))

if __name__=='__main__':main()
