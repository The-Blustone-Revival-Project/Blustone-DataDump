"""Build immutable dated stats/evidence documents from this repository's data."""
from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import argparse,hashlib,json,re,subprocess

ROOT=Path(__file__).resolve().parents[2]
DATASETS={
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
 coverage=load(ROOT/'catalog/coverage.json')
 curated=[]
 for path in ['datasets/hunters/observed-stats/051.md','datasets/hunters/observed-stats/010_1.md','datasets/hunters/observed-stats/010.md','datasets/equipment/GEAR.md']:
  curated+=tables(path)
 extra='findings/resources/vsfan-extracted-assets.md'
 if (ROOT/extra).exists():curated += [t for t in tables(extra) if 'jewel set' in t['section'].lower()]
 latest='findings/hunters/base-stats-visual-hunt/jewel-help-locales-2026-10-05.md'
 curated += [t for t in tables(latest) if t['section'].startswith(('1.4 ','1.5 ','2.2 '))]
 sources=[{'path':path,'sha256':digest((ROOT/path).read_bytes()),'records':len(datasets[name])} for name,path in DATASETS.items()]
 for path in sorted(set(t['source'] for t in curated)):
  sources.append({'path':path,'sha256':digest((ROOT/path).read_bytes())})
 snapshot={'format_version':1,'version':version,'as_of':as_of,'timezone':'Asia/Jerusalem',
           'previous_version':previous.get('version') if previous else None,'coverage':coverage,
           'changes':changes,'datasets':datasets,'curated_source_tables':curated,'sources':sources,
           'limitations':['As-of date describes this research snapshot, not original game version or observation date.',
             'Historical 2019 observations do not establish unequipped final-version base stats.',
             'Missing values remain unknown; conflicting and contaminated observations are retained separately.']}
 link=lambda path:f'{REPO}/blob/{version}/{path}'
 stats=[f'# BLUSTONE Stats — {version}',f'\nResearch snapshot as of **{as_of} (Asia/Jerusalem)**. This date is a publication cutoff; each observation retains its own historical capture date and context.\n',
 '## What this snapshot establishes\n',
 f"{coverage['character_rows']} catalogue rows ({coverage['playable_character_rows']} playable identities), {coverage['monster_identities']} monster identities, {coverage['numeric_historical_stat_claims']} historical numeric claims across {coverage['historical_rows_with_numeric_hp']} archived profiles with numeric HP. Symbolic formulas and original identifiers are preserved. Missing base stats remain unknown.\n",
 '## Changes since the previous snapshot\n',
 'Initial published baseline; all included dataset records are introduced here.\n' if not previous else f"Compared with **{previous['version']}**. A changed record includes changed context or provenance, not necessarily a new numerical value.\n",
 table(['Dataset','Added records','Changed records','Removed records'],[(k,v['added'],v['changed'],v['removed']) for k,v in changes.items()]),
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
 'The following tables retain their source section and context. Beckhen 051 has a visually checked unequipped Lv.30 column; it is not a Lv.1 growth curve. Vincent 010_1 has unknown gear and cannot establish unequipped base values. Gear/jewel tables describe observed samples, not full distributions.\n',
 'The historical GEAR table contains unresolved wording. Later evidence corroborates flat +23 Element/Resistance set values, while the old 1.4.4.1 Super Block differs by locale (KO 9%; EN/JP/ZH/ZT 5%). The included 2.8.0.1 help comparison records the renamed Reduction effect at 10% for KO/EN/JA/TC, while SC preserves a distinct older wording/value. Help-copy values are not native runtime proof. The ATK subtotal discrepancy remains unresolved. Read the evidence document before using these numbers.\n']
 for entry in curated:
  stats += [f"### {Path(entry['source']).stem}: {entry['section']}\n",entry['markdown']+'\n',
            f"Source: [{entry['source']}]({link(entry['source'])}#L{entry['line']}); SHA-256 `{entry['sha256']}`.\n"]
 stats += ['## Monster stats and remaining gaps\n','22 art identities are catalogued; no complete identified original monster HP/ATK/DEF tuples are asserted by this snapshot. Campaign entries enumerate 50 IDs from analytics data, not recovered difficulty or AP cost.\n',
           f"Detailed coverage and unresolved claims: [coverage ledger]({link('findings/hunters/base-stats-visual-hunt/coverage.md')}).\n"]
 evidence=[f'# BLUSTONE Evidence and Coverage — {version}',f'\nAs of **{as_of} (Asia/Jerusalem)**; source observation dates remain separate.\n',
 '## Evidence classes\n','- RECOVERED: original extracted record with exact file/key/chunk locator.\n- COMMUNITY-SOURCED: source-backed page/archive/screenshot claim.\n- INFERRED: explicit derivation or hypothesis.\n- INFERRED-FIXTURE: replica policy; not original-game evidence.\n- UNKNOWN: missing or unresolved.\n',
 '## Dataset coverage\n',table(['Dataset','Records','Pinned source'],[(name,len(datasets[name]),path) for name,path in DATASETS.items()]),
 '## Reading the stats document\n','Archive claims retain original URL, capture timestamp, raw text, units, identity match and unknown state fields in BLUSTONE-Stats.json. Screenshot tables carry a pinned document hash and source-line locator. Do not merge measurements at different levels, ranks or equipment states. White/green display separation is evidence for one observed build, not proof of final-version balance.\n',
 '## Conflicts and known limits\n','- 2019 archive levels/equipment are unestablished; zero archive claims count as complete base-stat evidence.\n- Beckhen 051 Lv.30 equipment ATK has a 78-point unreconciled subtotal.\n- Vincent 010_1 equipment state is unknown.\n- The 1.4.4.1 Super Block locale conflict and the distinct 2.8.0.1 Reduction wording/reordered help table are preserved; do not collapse eras or locales.\n- Monster video/HUD readings without an identified full/max HP cannot establish a base tuple.\n- Original reward IDs are separate from server settlement mappings.\n- No native battle, phone operation or new stat measurement is implied by publishing this snapshot.\n',
 '## Source fingerprints\n',table(['Source path','SHA-256'],[(r['path'],r['sha256']) for r in sources]),
 '## Reproduce this release\n',f'Check out tag `{version}`, run `python tools/normalize/validate-datasets.py`, then `python tools/releases/build-snapshot.py --date {as_of} --revision {args.revision} --out local/reproduced/{version}`. Use the previous release\'s BLUSTONE-Stats.json with `--previous-json` when applicable.\n',
 '## Integrity\n','SHA256SUMS.txt pins the two documents, the JSON snapshot and the release manifest. The release manifest pins every dataset source used to construct this snapshot. Private captures, cookies, saves, signing keys and raw account telemetry are excluded.\n']
 notes=f'''# Blustone DataDump {version}\n\nStats and evidence snapshot as of {as_of} (Asia/Jerusalem).\n\n## Included\n\n- **BLUSTONE-Stats.md:** historical hunter values, curated screenshot/equipment tables, original IDs and explicit unknowns.\n- **BLUSTONE-Evidence.md:** source classes, coverage, conflicts, source hashes and reproduction instructions.\n- **BLUSTONE-Stats.json:** all eight normalized datasets, curated source tables and machine-readable changes from the previous release.\n- **RELEASE-MANIFEST.json** and **SHA256SUMS.txt:** reproducibility and integrity.\n\n## Changes\n\n{'Initial research baseline.' if not previous else 'Compared with '+previous['version']+'.'}\n\n{table(['Dataset','Added','Changed','Removed'],[(k,v['added'],v['changed'],v['removed']) for k,v in changes.items()])}\n\n## Coverage and limits\n\n121 catalogue rows /113 playable identities;22 monster identities;806 numeric historical claims;50 campaign IDs;147 Episode nodes;1070 symbolic skill records. Historical archive values remain observations with unknown level/gear, not recovered final-version base stats. Conflicting jewel values and incomplete monster/base-stat evidence remain visible.\n'''
 out.mkdir(parents=True)
 (out/'BLUSTONE-Stats.md').write_text('\n'.join(stats),encoding='utf-8')
 (out/'BLUSTONE-Evidence.md').write_text('\n'.join(evidence),encoding='utf-8')
 (out/'BLUSTONE-Stats.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 manifest={'version':version,'as_of':as_of,'timezone':'Asia/Jerusalem','previous_version':snapshot['previous_version'],'sources':sources,
           'files':[{'name':name,'sha256':digest((out/name).read_bytes()),'bytes':(out/name).stat().st_size} for name in ['BLUSTONE-Stats.md','BLUSTONE-Evidence.md','BLUSTONE-Stats.json']]}
 (out/'RELEASE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 (out/'SHA256SUMS.txt').write_text(''.join(digest(f.read_bytes())+'  '+f.name+'\n' for f in sorted(out.iterdir()) if f.is_file()),encoding='utf-8')
 (out/'RELEASE-NOTES.md').write_text(notes,encoding='utf-8')
 print(json.dumps({'version':version,'output':str(out),'previous_version':snapshot['previous_version'],'files':6}))

if __name__=='__main__':main()
