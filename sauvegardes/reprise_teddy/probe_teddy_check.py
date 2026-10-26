"""Native Voir, three bedside replies and reset; native flags/warp preparation."""
import argparse,json
from pathlib import Path
from build_v78 import ROOT,b
from probe_stub_plural_review import StubSession
from targeted_warp_session import destination_fixture
from teddy_check_stage import GUARDS
from prepare_instant_win_states import scalar
CASES={'present':bytes.fromhex('04b4030503000504001f2102'),'absent':bytes.fromhex('05b4030503000504001f2102')}
def flags(s):
 raw=scalar(s,0x9c08,1);return {'0003':bool(raw&4),'0004':bool(raw&8)}
def words(s,at,n):
 raw=bytes.fromhex(s.send({'ram':dict(offset=hex(at),length=2*n)})['ram_hex']);return [int.from_bytes(raw[i:i+2],'little') for i in range(0,len(raw),2)]
def run(a):
 source=a.rom.read_bytes();flag_guard=bytes.fromhex('c2313aa8290700aabf2f56c448984a4a4aaa68');assert source[0x21628:0x21628+len(flag_guard)]==flag_guard
 for p in ('accents','ascii'):
  for case,prep in CASES.items():
   for kind in ('before','after'):
    out=a.out/p/case/kind;data=b.apply(source,b.records((ROOT/f'patches/EarthBound_Beginnings_FR_v78_{p}.ips').read_bytes()));off,raw=destination_fixture(data,2,6440,4336,1);s=StubSession(source,a.core,out,p,kind,None,0,stage='teddy_check',preparation=prep,fixture_writes=[(off,data[off:off+8],raw,'private_bedside_arrival')]);caps=[];w=[]
    try:
     for at,h in GUARDS.items():assert s.data[at:at+len(bytes.fromhex(h))]==bytes.fromhex(h)
     state=a.states_dir/p/'accept/handoff.state';s.send({'load':str(state.resolve()),'frames':0});s.step(60,sample=False)
     for key in ['A','Right','A','A','A']:s.tap(key,sample=False)
     s.step(1800,sample=False)
     for key in ['B']*8:s.tap(key,sample=False)
     s.step(60,sample=False);s.step(1,sample=True);s.step(8,('Up',),sample=False);s.step(1,sample=True);xy=words(s,0xb8e,60);ids=words(s,0x2c9a,30);scripts=words(s,0xa62,30);active=[ids[i] for i in range(23) if scripts[i]!=0xffff and ids[i]<1584];assert (607 in active)==(case=='present');initial_position=[xy[24],xy[54]]
     for i in range(4 if case=='present' else 1):
      before=flags(s)
      for key in ['A','Down','Down','A']:s.tap(key,sample=False)
      s.step(600,sample=False);s.step(1,sample=True);caps.append(s.capture('message'+str(i)));message=flags(s);selected=scalar(s,0x5d62,2);pointer=s.last['rom_offset'] if s.last else None
      s.tap('A',sample=False);s.step(120,sample=False)
      if case=='present':s.tap('A',sample=False);s.step(120,sample=False)
      s.step(1,sample=True);caps.append(s.capture('closed'+str(i)));w.append(dict(cycle=i,before=before,message=message,closed=flags(s),interacting_npc=selected,message_pointer=pointer))
     r=dict(profile=p,case=case,kind=kind,base_rom_sha256=b.sha(s.data),fixture_rom_sha256=b.sha(s.fixture),core_sha256=b.sha(a.core.read_bytes()),initial_state_sha256=b.sha(state.read_bytes()),preparation_hex=prep.hex(),temporary_rom_writes=s.routing,commands=s.commands,captures=caps,active_npc_ids=active,arrival_after_eight_native_Up_frames=initial_position,flag_cycle=w,pointer_frame_counts=dict(s.counts),native_check_hook='38799B',bedside_npc=607,bedside_appearance_flag='03B4',flag_numbers_are_one_based=True,native_flag_reader_guard=flag_guard.hex(),native_menu_used=True,bedside_text_called_directly=False,wram_written_directly=False,natural_initial_journey_or_injury_verified=False)
    finally:s.close()
    r['returncode']=s.proc.returncode;(out/'history.json').unlink(missing_ok=True);(out/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(p,case,kind,w,flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser()
 for name in ('rom','core','states-dir','out'):ap.add_argument('--'+name,type=Path,required=True)
 run(ap.parse_args())
