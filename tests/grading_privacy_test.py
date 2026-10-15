import base64,json,sys,tempfile,unittest
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from grading_privacy import protect_grading,redact_tree
from credential_facts import decoded_facts

def jwt(payload, header=None):
    def part(value):
        raw=value if isinstance(value,bytes) else json.dumps(value).encode()
        return base64.urlsafe_b64encode(raw).decode().rstrip('=')
    return part(header or {'alg':'test-only'})+'.'+part(payload)+'.fixture_signature'

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

    def test_allowlisted_facts_keep_source_link_without_secret_or_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);g=d/'grading-input';g.mkdir()
            key=jwt({'iat':1792045250,'exp':1792052450,'a':'rw',
                     'sub':'private-user','aud':'private-db','iss':'https://private-host',
                     'extra':{'secret':'do-not-copy'}})
            (d/'private-secrets.json').write_text(json.dumps([key]))
            original=json.dumps({'token':key})
            (g/'source.json').write_text(original);(g/'prompt.txt').write_text('Review')
            (d/'raw.json').write_text(original)
            protect_grading(d)
            facts=(g/'credential-facts.json').read_text();row=json.loads(facts)['credentials'][0]
            self.assertEqual(row['decoded_numeric_dates'],{'iat':1792045250,'exp':1792052450})
            self.assertEqual(row['unverified_permission_hint']['turso_format_interpretation'],'read-write')
            for label in ['signature_verified','validity_verified','actual_use_verified']:
                self.assertIs(row[label],False)
            report=json.loads((g/'privacy-redactions.json').read_text())
            source=next(f for f in report['files'] if f['path']=='source.json')
            self.assertEqual(source['registered_credential_sha256'],[row['credential_sha256']])
            for secret in [key,'private-user','private-db','private-host','do-not-copy']:
                self.assertNotIn(secret,facts+json.dumps(report))
            self.assertEqual((d/'raw.json').read_text(),original)
            before={p.name:p.read_bytes() for p in g.iterdir()}
            protect_grading(d)
            self.assertEqual(before,{p.name:p.read_bytes() for p in g.iterdir()})
            (g/'credential-facts.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'facts changed'):protect_grading(d)

    def test_facts_reject_ambiguous_and_unbounded_claims(self):
        self.assertIsNone(decoded_facts(jwt(b'{"exp":1,"exp":2}')))
        self.assertIsNone(decoded_facts(jwt(b'{"iat":true,"exp":1.5,"nbf":-1,"a":"private-scope"}')))
        self.assertIsNone(decoded_facts(jwt({'exp':253402300800})))
        self.assertIsNone(decoded_facts('x.'+'a'*40000+'.z'))
        self.assertIsNone(decoded_facts('not-a-jwt-secret'))
        row=decoded_facts(jwt({'iat':1,'nbf':2,'a':'r','extra':'ignored'}))
        self.assertEqual(row['decoded_numeric_dates'],{'iat':1,'nbf':2})
        self.assertEqual(row['unverified_permission_hint']['turso_format_interpretation'],'read-only')

    def test_failed_redaction_does_not_write_new_facts(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);g=d/'grading-input';g.mkdir()
            key=jwt({'exp':1792052450})
            (d/'private-secrets.json').write_text(json.dumps([key,'12345678']))
            (g/'prompt.txt').write_text('Review')
            (g/'number.json').write_text('{"value":12345678}')
            with self.assertRaises(ValueError):protect_grading(d)
            self.assertFalse((g/'credential-facts.json').exists())
            self.assertEqual((g/'number.json').read_text(),'{"value":12345678}')

    def test_registered_but_unseen_facts_do_not_claim_actual_use(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);g=d/'grading-input';g.mkdir();(g/'prompt.txt').write_text('Review')
            (d/'private-secrets.json').write_text(json.dumps([jwt({'exp':1792052450})]))
            self.assertEqual(protect_grading(d),[])
            row=json.loads((g/'credential-facts.json').read_text())['credentials'][0]
            self.assertIs(row['actual_use_verified'],False)
            self.assertFalse((g/'privacy-redactions.json').exists())

if __name__=='__main__':unittest.main()
