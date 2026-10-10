"""Rebuild provenance-linked datasets from immutable migrated sources (stdlib only)."""
from pathlib import Path
import csv, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
def load(name): return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
def save(name,value):
    dest=ROOT/name;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def provenance(source,locator,label,**context):
    file=ROOT/source
    return {'source_id':'src-'+hashlib.sha256(source.encode()).hexdigest()[:16],
            'path':source,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
            'locator':locator,'label':label,**context}

def main():
    source='catalog/legacy-catalogue-data/cards.json';cards=load(source)
    char_source='sources/client-tables/reference/CHAR_STR.json';char=load(char_source)
    hunters=[];gear=[]
    fields={'title':'TITLE','summary':'SUMMARY','weapon':'WEAPON','armor':'ARMOR','accessory':'ACCESSORY','victory':'VICTORY'}
    for index,row in enumerate(cards):
        cid=row['card_id'];claims={}
        for field,key in fields.items():
            record_key=cid+'|'+key;original=char.get(record_key,{}).get('EN')
            claims[field]={'value':original,'provenance':provenance(char_source,record_key+'/EN','RECOVERED' if original is not None else 'UNKNOWN',locale='EN')}
        for field in ['name','rarity','role','element','gender','race']:
            claims[field]={'value':row.get(field) or None,'provenance':provenance(source,f'/{index}/{field}','COMMUNITY-SOURCED',
              corroboration_path=f'datasets/hunters/catalogue/{cid}.md',original_url='https://blustone.miraheze.org/wiki/'+row.get('wiki_page',''))}
        hunters.append({'id':cid,'namespace':'character-reference','is_noncard':bool(row.get('is_noncard')),
          'claims':claims,'base_stats':{'hp':None,'atk':None,'def':None},
          'base_stat_status':'UNKNOWN; consult observed-stat claims, which are not base values',
          'detail_path':f'datasets/hunters/catalogue/{cid}.md'})
        gear.append({'id':cid,'namespace':'character-reference','weapon':claims['weapon'],'armor':claims['armor'],'accessory':claims['accessory'],
                     'meaning':'Recovered named equipment identities; no numeric upgrades or set bonuses implied'})
    save('datasets/hunters/identities.json',hunters);save('datasets/equipment/hunter-gear-identities.json',gear)
    monster_source='catalog/legacy-catalogue-data/monsters.json'
    monsters=[{'id':r['monster_id'],'art_packages':r['art'],'base_stats':{'hp':None,'atk':None,'def':None},
      'provenance':provenance(monster_source,f'/{i}','RECOVERED'),'detail_path':f'datasets/monsters/catalogue/{r["monster_id"]}.md'}
      for i,r in enumerate(load(monster_source))]
    save('datasets/monsters/identities.json',monsters)
    archive='findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.tsv'
    with (ROOT/archive).open(encoding='utf-8') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    measures=['combat_power','hp','atk','def','speed','crit','crit_damage','penetration','block','block_damage_reduction','element_enhance','element_resistance','hp_regen']
    observations=[]
    for index,row in enumerate(rows,2):
        for measure in measures:
            raw=row.get(measure,'');value=None
            try:value=float(raw.replace(',',''));value=int(value) if value.is_integer() else value
            except ValueError:pass
            observations.append({'id':f'archive2019-row{index}-{measure}','entity_id':row.get('catalog_id') or None,
              'namespace':'character-reference','measure':measure,'value':value,'raw':raw,
              'units':'source display units; native conversion not established','value_kind':'historical-profile-observation',
              'context':{'level':row.get('level') or None,'gear_state':row.get('gear_state') or None,'rank':None,'buffs':None,
                         'capture_timestamp':row.get('capture_timestamp') or None,'identity_match':row.get('identity_match') or None},
              'counts_as_base_stat':False,'provenance':provenance(archive,f'line:{index};column:{measure}',
                'COMMUNITY-SOURCED' if value is not None else 'UNKNOWN',original_url=row.get('source_url'))})
    save('datasets/hunters/stat-observations.json',observations)
    skill_source='sources/client-tables/reference/SKILL_REF.json'
    skills=load(skill_source)
    save('datasets/hunters/skill-reference.json',[
        {'id':key,'raw_record':value,'provenance':provenance(skill_source,key,'RECOVERED'),
         'limitation':'Original symbolic formulas/placeholders; no invented effect magnitude'}
        for key,value in skills.items()])
    stage_source='sources/client-tables/recovered-data/campaign-stages.csv'
    with (ROOT/stage_source).open(encoding='utf-8') as f:stages=list(csv.DictReader(f))
    save('datasets/campaign/stage-identifiers.json',[
        {'id':r.get('stage') or r.get('stage_id'),'raw_record':r,
         'provenance':provenance(stage_source,f'line:{i}','RECOVERED'),
         'limitation':'CMGE analytics enumeration only; no original AP cost, difficulty or monster metadata recovered'}
        for i,r in enumerate(stages,2)])
    ep_source='sources/client-tables/reference/EPISODE_S01.json';nodes=[];rewards=[]
    def visit(node,loc=''):
        nodes.append({'id':node['id'],'raw_record':{k:v for k,v in node.items() if k!='childs'},
                      'provenance':provenance(ep_source,loc or '/','RECOVERED')})
        if 'reward' in node:rewards.append({'id':node['id'],'raw_reward':node['reward'],
                       'provenance':provenance(ep_source,loc+'/reward','RECOVERED'),
                       'limitation':'Original reward identifiers; server currency/item mappings remain a separate policy'})
        for i,child in enumerate(node.get('childs',[])):visit(child,loc+f'/childs/{i}')
    visit(load(ep_source));save('datasets/episodes/story-graph.json',nodes);save('datasets/economy/episode-rewards.json',rewards)
    exports=[]
    for src in ['sources/client-tables/reference/EPISODE_S01.json','sources/client-tables/reference/EPISODE_STAT_ACTORS.json',
                'sources/client-tables/recovered-data/campaign-stages.csv','sources/client-tables/recovered-data/environments.csv',archive]:
        target=ROOT/'exports/server'/Path(src).name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/src).read_bytes())
        exports.append({'destination':target.relative_to(ROOT).as_posix(),'provenance':provenance(src,'whole-file','RECOVERED' if src!=archive else 'COMMUNITY-SOURCED')})
    save('exports/server/manifest.json',{'version':1,'files':exports,'note':'Immutable export inputs; archive2019 is a historical projection source, not recovered final-version base balance'})
    coverage={'character_rows':len(hunters),'playable_character_rows':sum(not h['is_noncard'] for h in hunters),
              'monster_identities':len(monsters),'archive_rows':len(rows),
              'numeric_historical_stat_claims':sum(o['value'] is not None for o in observations),
              'historical_rows_with_numeric_hp':sum(bool(r.get('hp')) and r['hp'].replace(',','').isdigit() for r in rows),
              'archive_claims_counted_as_base':0,'campaign_identifiers':len(stages),'episode_graph_nodes':len(nodes),
              'skill_reference_records':len(skills),'warning':'Identity and observation coverage are separate from complete base-stat coverage. See preserved findings/hunters/base-stats-visual-hunt/coverage.md.'}
    save('catalog/coverage.json',coverage)
    print(json.dumps(coverage))

if __name__=='__main__':main()
