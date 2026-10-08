import base64,json,sys,tempfile,unittest
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from grading_privacy import protect_grading,redact_tree

class GradingPrivacyTests(unittest.TestCase):
    def test_all_copies_redact_variants_and_preserve_raw_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);g=d/'grading-input';(g/'review-packet/tools').mkdir(parents=True)
            key='private-key+long/12345'
            (d/'private-secrets.json').write_text(json.dumps([key]))
            payload=json.dumps({'literal':key,'url':quote(key,safe=''),'base64':base64.b64encode(key.encode()).decode()})
            (d/'raw.json').write_text(payload)
            for name in ['execution.json','review-packet/tools/0001.json','prompt.txt']:(g/name).write_text(payload)
            changed=protect_grading(d)
            self.assertEqual(len(changed),3)
            self.assertEqual((d/'raw.json').read_text(),payload)
            for name in ['execution.json','review-packet/tools/0001.json']:
                self.assertEqual(set(json.loads((g/name).read_text()).values()),{'[SERVICE_SECRET]'})
            self.assertNotIn(key,(g/'privacy-redactions.json').read_text())

    def test_peer_copy_redacts_other_members_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);(d/'peer.txt').write_text('peer-api-key-12345')
            self.assertEqual(len(redact_tree(d,['own-api-key-67890','peer-api-key-12345'])),1)
            self.assertEqual((d/'peer.txt').read_text(),'[SERVICE_SECRET]')

    def test_unsafe_filename_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);(d/'api-key-12345.txt').write_text('content')
            with self.assertRaisesRegex(ValueError,'filename'):redact_tree(d,['api-key-12345'])

if __name__=='__main__':unittest.main()
