import argparse,json
from pathlib import Path
from PIL import Image,ImageChops
from build_v78 import ROOT,b
from collect_dad_phone import sanitize
from probe_teddy_check import CASES
def collect(source):
 dest=ROOT/'tests/emulation_v78_teddy_check';dest.mkdir(exist_ok=True);f=json.loads((ROOT/'tools/v78/v78_fixtures.json').read_text())['teddy_check'];reports=[];pairs=[];files=set()
 for p in ('accents','ascii'):
  for case in CASES:
   runs={}
   for mode in ('before','after'):
    r=json.loads((source/p/case/mode/'results.json').read_text());assert r['returncode']==0 and r['base_rom_sha256']==f['profiles'][p]['input_rom_sha256' if mode=='before' else 'output_rom_sha256'];caps=[]
    for c in r['captures']:
     raw=Path(c['path']).read_bytes();sha=b.sha(raw);path=dest/f'frame_{sha}.png';path.write_bytes(raw);files.add(path);assert b.sha(Image.open(path).convert('RGB').tobytes())==c['sha256_rgb'];caps.append(dict(name=Path(c['path']).stem,path=str(path.relative_to(ROOT)),png_sha256=sha,sha256_rgb=c['sha256_rgb']))
    r=sanitize(r);r['captures']=caps;path=dest/f'{p}_{case}_{mode}.json';path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');reports.append(str(path.relative_to(ROOT)));runs[mode]=r
   assert runs['before']['commands']==runs['after']['commands'] and runs['before']['flag_cycle']==runs['after']['flag_cycle'] and runs['before']['pointer_frame_counts']==runs['after']['pointer_frame_counts']
   for a,z in zip(runs['before']['captures'],runs['after']['captures']):
    assert a['name']==z['name'];diff=ImageChops.difference(Image.open(ROOT/a['path']).convert('RGB'),Image.open(ROOT/z['path']).convert('RGB'));box=diff.getbbox();assert bool(box)==(case=='present' and a['name'] in ('message0','message3'));diff.paste((0,0,0),(104,16,248,48));assert diff.getbbox() is None;pairs.append(dict(profile=p,case=case,name=a['name'],before=a,after=z,difference_bbox=list(box) if box else None,allowed_window=[104,16,248,48]))
 c=dict(profiles={p:{k:f['profiles'][p][k] for k in ('input_rom_sha256','output_rom_sha256')} for p in ('accents','ascii')},reports=reports,pairs=pairs,capture_references=2*len(pairs),unique_png_files=len(files),changed_pairs=sum(bool(x['difference_bbox']) for x in pairs),native_Voir_and_cycle_verified=True,working_flag_sequence_after_close=[[True,False],[True,True],[False,False],[True,False]],native_check_interacting_npc=607,appearance_flag_03B4_prepared=True,natural_initial_journey_or_injury_verified=False,new_distinct_sources=1,physical_source_spans=1,private_binaries_or_memory_dumps_distributed=False);(dest/'coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print({k:c[k] for k in ('capture_references','unique_png_files','changed_pairs')})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);collect(ap.parse_args().out)
