"""Validate normalized record keys, evidence locators/hashes and export parity."""
from pathlib import Path
import hashlib,json,math,re
ROOT=Path(__file__).resolve().parents[2]
LABELS={'RECOVERED','COMMUNITY-SOURCED','INFERRED','INFERRED-FIXTURE','UNKNOWN'}
hashes={};count=0
def walk(value):
    global count
    if isinstance(value,dict):
        if 'provenance' in value:
            p=value['provenance'];file=(ROOT/p['path']).resolve()
            assert file.is_relative_to(ROOT.resolve()) and file.is_file(),p['path']
            assert p['label'] in LABELS and p['locator'] and re.fullmatch(r'src-[0-9a-f]{16}',p['source_id'])
            assert re.fullmatch(r'[0-9a-f]{64}',p['sha256'])
            if str(file) not in hashes:hashes[str(file)]=hashlib.sha256(file.read_bytes()).hexdigest()
            assert hashes[str(file)]==p['sha256'],p['path'];count+=1
        if 'detail_path' in value:assert (ROOT/value['detail_path']).is_file(),value['detail_path']
        for v in value.values():walk(v)
    elif isinstance(value,list):
        for v in value:walk(v)
datasets=sorted((ROOT/'datasets').rglob('*.json'))
normalized=0
for file in datasets:
    data=json.loads(file.read_text(encoding='utf-8-sig'))
    if isinstance(data,list) and data and all(isinstance(r,dict) and 'id' in r for r in data):
        ids=[r['id'] for r in data];assert None not in ids and len(ids)==len(set(ids)),str(file);normalized+=1
    walk(data)
observations=json.loads((ROOT/'datasets/hunters/stat-observations.json').read_text(encoding='utf-8'))
assert all(r['counts_as_base_stat'] is False for r in observations)
assert all(r['value'] is None or isinstance(r['value'],(int,float)) and math.isfinite(r['value']) for r in observations)
quotes=json.loads((ROOT/'datasets/economy/market-quotes.json').read_text(encoding='utf-8'))
for row in quotes:
    assert row['lot_price'] > 0 and (row['quantity'] is None or row['quantity'] > 0),row['id']
    assert re.fullmatch(r'[0-9a-f]{64}',row['image_sha256']),row['id']
    transcript=row['transcription']['provenance']
    assert transcript['path']==row['transcript_path'] and transcript['locator']==f"line:{row['transcript_line']}"
    lines=(ROOT/transcript['path']).read_text(encoding='utf-8-sig').splitlines()
    assert lines[row['transcript_line']-1].split('\t')[0]==str(row['image_id']),row['id']
manifest=json.loads((ROOT/'exports/server/manifest.json').read_text(encoding='utf-8'))
for row in manifest['files']:
    assert hashlib.sha256((ROOT/row['destination']).read_bytes()).hexdigest()==row['provenance']['sha256']
print(json.dumps({'normalized_datasets':normalized,'provenance_claims_verified':count,'source_hashes_verified':len(hashes),'export_files_verified':len(manifest['files'])}))
