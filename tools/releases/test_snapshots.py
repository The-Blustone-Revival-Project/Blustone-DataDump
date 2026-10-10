"""Snapshot regression checks: date revisions must not manufacture data changes."""
import importlib.util,unittest,json,hashlib,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('snapshot_builder',Path(__file__).with_name('build-snapshot.py'))
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
class Snapshots(unittest.TestCase):
 def test_incremental_context_changes_and_removals_are_visible(self):
  before={'datasets':{'stats':[{'id':'a','value':7,'gear':'unknown'},{'id':'b','value':8},{'id':'c','value':9}]}}
  after={'stats':[{'id':'a','value':7,'gear':'unequipped'},{'id':'b','value':8},{'id':'d','value':10}]}
  self.assertEqual(builder.compare(after,before)['stats'],{'added':1,'removed':1,'changed':1,'unchanged':1})
 def test_same_day_revision_preserves_data_and_pins_documents(self):
  with tempfile.TemporaryDirectory() as folder:
   out=Path(folder)/'second';previous=ROOT/'releases/2026-10-10/BLUSTONE-Stats.json'
   subprocess.run([sys.executable,str(Path(__file__).with_name('build-snapshot.py')),'--date','2026-10-10','--revision','2','--previous-json',str(previous),'--out',str(out)],check=True,capture_output=True)
   data=json.loads((out/'BLUSTONE-Stats.json').read_text(encoding='utf-8'))
   self.assertEqual(data['version'],'2026-10-10.2');self.assertEqual(data['previous_version'],'2026-10-10')
   self.assertTrue(all(v['added']==v['changed']==v['removed']==0 for v in data['changes'].values()))
   self.assertTrue(any(t['source'].endswith('jewel-help-locales-2026-10-05.md') for t in data['curated_source_tables']))
   for line in (out/'SHA256SUMS.txt').read_text().splitlines():
    h,name=line.split('  ',1);self.assertEqual(hashlib.sha256((out/name).read_bytes()).hexdigest(),h)
   rerun=subprocess.run([sys.executable,str(Path(__file__).with_name('build-snapshot.py')),'--date','2026-10-10','--out',str(out)],capture_output=True)
   self.assertNotEqual(rerun.returncode,0,'Existing immutable snapshots cannot be overwritten')
if __name__=='__main__':unittest.main()
