"""First native Voir response at Teddy's bedside; existing cycle replies retained."""
import json
from pathlib import Path
from build_v78 import ROOT,b
ROOT_TEXT=0x352d42;START=0x352d53;STOP=0x352d71;END=0x352d77
EN='@He lays very quiet and still.';FR='@Il reste calme et immobile.'
GUARDS={0x38799b:'29ff00c90100d0034caa795cb032c1',0x3879d4:'ad625dc95f02f0034ce979a9422d850aa9f500850c5c9433c1'}
def correction(source,data,p):
 assert b.sha(source)==b.ROM_SHA and data[ROOT_TEXT:END]==source[ROOT_TEXT:END] and b.decode(source[START:STOP],b.dictionary_from_rom(source))==EN
 for a,h in GUARDS.items():assert source[a:a+len(bytes.fromhex(h))]==data[a:a+len(bytes.fromhex(h))]==bytes.fromhex(h)
 assert not any(START<a<STOP for a in set(b.pointer_index(source))|set(b.pointer_index(data)));raw=b.encode(FR,p).ljust(STOP-START,b.encode(' ',p));assert len(raw)==STOP-START;target=b.apply(data,[(START,raw)]);assert b.commands(target[ROOT_TEXT:END])==b.commands(data[ROOT_TEXT:END]) and target[0x352d77:0x352db8]==data[0x352d77:0x352db8];return [(START,raw)]
def extend(source,out,plan,fixtures):
 f=dict(new_distinct_sources=1,physical_source_spans=1,entries=[dict(offset=f'{START:06X}',en=EN,fr=FR,kind='native_person_Voir_response_Teddy_bedside')],profiles={})
 for p in ('accents','ascii'):
  path=Path(out)/f'EarthBound_Beginnings_FR_v78_{p}.ips';prior=path.read_bytes();data=b.apply(source,b.records(prior));writes=correction(source,data,p);ips=b.append(prior,writes);target=b.apply(data,writes);path.write_bytes(ips);f['profiles'][p]=dict(input_records_added=plan['profiles'][p]['records_added'],input_patch_sha256=b.sha(prior),input_rom_sha256=b.sha(data),output_patch_sha256=b.sha(ips),output_rom_sha256=b.sha(target),records=[dict(offset=f'{a:06X}',hex=v.hex()) for a,v in writes]);plan['profiles'][p]=dict(sha256=b.sha(ips),target_rom_sha256=b.sha(target),records_added=plan['profiles'][p]['records_added']+len(writes))
 fixtures['teddy_check']=f;plan.update(distinct_new_translations=plan['distinct_new_translations']+1,changed_text_spans=plan['changed_text_spans']+1,current_execution_new_distinct_sources=126,new_since_execution_baseline=126,pending_distinct_since_published_checkpoint=238,teddy_check_display_and_cycle_validated=False,execution_validation_pending=True)
 coverage=ROOT/'tests/emulation_v78_teddy_check/coverage.json'
 if coverage.exists():
  c=json.loads(coverage.read_text());valid=c['native_Voir_and_cycle_verified'] and all(c['profiles'][p]['output_rom_sha256']==f['profiles'][p]['output_rom_sha256'] for p in ('accents','ascii'));plan.update(teddy_check_display_and_cycle_validated=valid,execution_validation_pending=not valid)
 for name,value in [('v78_fixtures',fixtures),('validation_v78',plan)]:(ROOT/f'tools/v78/{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
 return plan
