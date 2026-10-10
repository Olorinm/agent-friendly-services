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

    def test_json_suffix_with_curl_status_preserves_original_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);f=d/'create-db.json'
            original='{"token":"api-key-12345"}\nHTTP 200\n'
            f.write_text(original)
            changed=redact_tree(d,['api-key-12345'])
            self.assertEqual(f.read_text(),'{"token":"[SERVICE_SECRET]"}\nHTTP 200\n')
            self.assertEqual(len(changed),1)
            self.assertIn('not a single JSON',changed[0]['format_note'])

    def test_valid_json_must_remain_valid_and_rejection_changes_no_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);first=d/'first.txt';last=d/'last.json'
            first.write_text('api-key-12345');last.write_text('{"private_id":12345678}')
            with self.assertRaises(ValueError):redact_tree(d,['api-key-12345','12345678'])
            self.assertEqual(first.read_text(),'api-key-12345')
            self.assertEqual(last.read_text(),'{"private_id":12345678}')

    def test_invalid_json_artifact_removes_encoded_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);f=d/'transcript.json';key='api-key-12345'
            f.write_text('saved token='+base64.b64encode(key.encode()).decode())
            redact_tree(d,[key])
            self.assertEqual(f.read_text(),'saved token=[SERVICE_SECRET]')

if __name__=='__main__':unittest.main()
