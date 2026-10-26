import json,os,subprocess,unittest
from pathlib import Path
from PIL import Image,ImageChops
from build_v78 import ROOT,b
from teddy_check_stage import correction,START,STOP,ROOT_TEXT,END,GUARDS
from probe_teddy_check import CASES
class TeddyCheckTests(unittest.TestCase):
 def test_incremental_native_field_and_other_two_replies_preserved(self):
  path=os.environ.get('EARTHBOUND_ROM')
  if not path:self.skipTest('Private ROM not supplied')
  source=Path(path).read_bytes();f=json.loads((ROOT/'tools/v78/v78_fixtures.json').read_text())['teddy_check'];self.assertEqual(f['new_distinct_sources'],1)
  for p in ('accents','ascii'):
   prior=subprocess.check_output(['git','show',f'0df2d43c6c64b54cc2e7cbf8faa1dffd2fbbb749:patches/EarthBound_Beginnings_FR_v78_{p}.ips'],cwd=ROOT);base=b.apply(source,b.records(prior));q=f['profiles'][p];self.assertEqual(b.sha(prior),q['input_patch_sha256']);writes=correction(source,base,p);ips=b.append(prior,writes);self.assertEqual((ROOT/f'patches/EarthBound_Beginnings_FR_v78_{p}.ips').read_bytes(),ips);self.assertEqual(b.sha(ips),q['output_patch_sha256']);target=b.apply(base,writes);self.assertEqual(b.sha(target),q['output_rom_sha256']);self.assertEqual(base[:START],target[:START]);self.assertEqual(base[STOP:],target[STOP:]);self.assertEqual(b.commands(target[ROOT_TEXT:END]),b.commands(base[ROOT_TEXT:END]));self.assertEqual(target[0x352d77:0x352db8],base[0x352d77:0x352db8])
   for a in [START,*GUARDS]:
    bad=bytearray(base);bad[a]^=1
    with self.assertRaises(AssertionError):correction(source,bytes(bad),p)
 def test_actual_Voir_three_reply_cycle_and_absent_control(self):
  root=ROOT/'tests/emulation_v78_teddy_check';c=json.loads((root/'coverage.json').read_text());self.assertEqual((c['capture_references'],c['unique_png_files'],c['changed_pairs']),(40,12,4));self.assertEqual(c['new_distinct_sources'],1)
  for path in c['reports']:
   r=json.loads((ROOT/path).read_text());self.assertEqual(r['returncode'],0);self.assertEqual(r['preparation_hex'],CASES[r['case']].hex());self.assertTrue(r['native_menu_used']);self.assertFalse(r['bedside_text_called_directly']);self.assertFalse(r['wram_written_directly']);self.assertFalse(r['natural_initial_journey_or_injury_verified']);self.assertTrue(r['flag_numbers_are_one_based']);self.assertEqual(607 in r['active_npc_ids'],r['case']=='present')
   if r['case']=='present':
    self.assertEqual([x['message_pointer'] for x in r['flag_cycle']],['352D72','352D90','352DB2','352D72']);self.assertEqual([[x['closed']['0003'],x['closed']['0004']] for x in r['flag_cycle']],[[True,False],[True,True],[False,False],[True,False]]);self.assertTrue(all(x['interacting_npc']==607 for x in r['flag_cycle']));self.assertEqual(r['arrival_after_eight_native_Up_frames'],[6440,4328])
   else:self.assertFalse(r['flag_cycle'][0]['closed']['0003']);self.assertFalse(r['flag_cycle'][0]['closed']['0004']);self.assertFalse(any(a.startswith('352D') for a in r['pointer_frame_counts']))
  for pair in c['pairs']:
   ims=[]
   for k in ('before','after'):
    cap=pair[k];path=ROOT/cap['path'];im=Image.open(path).convert('RGB');self.assertEqual(b.sha(path.read_bytes()),cap['png_sha256']);self.assertEqual(b.sha(im.tobytes()),cap['sha256_rgb']);ims.append(im)
   diff=ImageChops.difference(*ims);box=diff.getbbox();self.assertEqual(list(box) if box else None,pair['difference_bbox']);self.assertEqual(bool(box),pair['case']=='present' and pair['name'] in ('message0','message3'));diff.paste((0,0,0),tuple(pair['allowed_window']));self.assertIsNone(diff.getbbox())
if __name__=='__main__':unittest.main()
