"""Preparation holds are not service failures or retrospective regrading."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import admission
import pipeline
import pipeline_test as fixtures


def free_qualification():
    # This declares fixture scope, not a real external price verification.
    return {'service_fee': {'status': 'documented_free_within_scope', 'amount': 0,
                           'scope': ['Fixture read-only scope'],
                           'source_urls': ['https://example.com/pricing'],
                           'actual_run_fee': None, 'observed_paid_request': False}}


def photon_reference():
    # The keys/status/scope mirror the observed preparation conflict. No model
    # transcript, personal location or original assessment is a test input.
    return {'service_fee_qualification': {'photon': {'service_fee': {
        'status': 'unknown', 'amount': None, 'currency': None,
        'scope': 'Account/keyless/demo access is not evidence of a monetary price; actual receipts remain unobserved.',
        'source_urls': [], 'actual_run_fee': None, 'observed_paid_request': False},
        'docs': [{'id': 'public-search-api', 'docs': 'https://photon.komoot.io/'}],
        'quota': {'scope': 'public demo', 'notes': 'Discretionary throttle; quantitative quota not established.'}}}}


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.config = {'service': 'photon', 'route': 'public-search-api',
                       'trial_protocol': pipeline.HANDOFF_PROTOCOL}
        self.task = {'id': 'geocoding-venue-001', 'version': 'v1', 'sha256': 'a' * 64,
                     'resources': 'Fixture task uses confirmed-free read-only resources.'}
        self.role = b'Fixture canonical role: confirmed-free-only.'

    def check(self, reference=None):
        raw = json.dumps(reference).encode() if reference is not None else None
        return admission.plan(self.config, self.task, reference, raw, self.role, pipeline.HANDOFF_PROTOCOL)

    def test_actual_photon_unknown_qualification_holds_before_dispatch(self):
        with self.assertRaisesRegex(ValueError, 'unknown under the confirmed-free-only'):
            self.check(photon_reference())

    def test_exact_held_route_remains_held_even_if_fee_is_free(self):
        reference = {'service_fee_qualification': {'photon': free_qualification()},
                     'cohort_disclosure': {'held_routes': {'photon/public-search-api':
                         'Current explicit fee proof missing; retain fee unknown under unchanged v1.'}},
                     'reference_recheck': {'decision': 'Photon is held under the existing task prerequisite.'}}
        with self.assertRaisesRegex(ValueError, 'assigned route is held: photon/public-search-api'):
            self.check(reference)

    def test_held_other_service_or_route_and_prose_do_not_pollute_free_assignment(self):
        self.config['service'] = 'nominatim'
        reference = photon_reference()
        reference['service_fee_qualification']['nominatim'] = free_qualification()
        reference['cohort_disclosure'] = {'held_routes': {
            'photon/public-search-api': 'held', 'nominatim/other-route': 'held',
            'nominatim/public-search-api-extra': 'held'}}
        reference['reference_recheck'] = {'decision': 'Photon held; paid_candidate remains for another route.'}
        self.assertEqual(self.check(reference)['status'], 'documented_free')

    def test_free_amount_is_not_claimed_as_actual_charge(self):
        reference = {'service_fee_qualification': {'photon': free_qualification()}}
        value = self.check(reference)
        fee = value['fee_evidence'][0]['qualification']
        self.assertIsNone(fee['actual_run_fee'])
        self.assertNotIn('service_cost_usd', value)
        self.assertEqual(value['reference_sha256'], hashlib.sha256(json.dumps(reference).encode()).hexdigest())
        self.assertEqual(value['execution_role_sha256'], hashlib.sha256(self.role).hexdigest())

    def test_other_service_and_other_route_qualifications_cannot_authorize_missing_fee(self):
        cases = [
            {'service_fee_qualification': {'nominatim': free_qualification()}},
            {'service_fee_qualification': {'photon': {**free_qualification(), 'route': 'other-route'}}},
            {'reference_recheck': {'decision': 'Current route looks free and usable.'}},
        ]
        for reference in cases:
            with self.subTest(reference=reference), self.assertRaisesRegex(ValueError, 'missing matching service/route'):
                self.check(reference)

    def test_free_qualification_needs_sources_scope_and_consistent_amount(self):
        cases = [({'source_urls': []}, 'source URLs'),
                 ({'source_urls': ['javascript:free']}, 'source URLs'),
                 ({'scope': ''}, 'applicable scope'),
                 ({'scope': [None]}, 'applicable scope'),
                 ({'amount': 1}, 'contradicts')]
        for changes, reason in cases:
            qualification = free_qualification()
            qualification['service_fee'].update(changes)
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, reason):
                self.check({'service_fee_qualification': {'photon': qualification}})

    def test_explicit_config_unknown_cannot_be_hidden_by_free_reference(self):
        self.config['resource_authorization'] = {
            'service': 'photon', 'route': 'public-search-api', 'fee_policy': 'confirmed_free_only',
            'service_fee': deepcopy(photon_reference()['service_fee_qualification']['photon']['service_fee'])}
        with self.assertRaisesRegex(ValueError, 'unknown under the confirmed-free-only'):
            self.check({'service_fee_qualification': {'photon': free_qualification()}})

    def test_resource_authorization_must_match_current_assignment(self):
        self.config['resource_authorization'] = {
            'service': 'another-service', 'route': 'public-search-api', 'fee_policy': 'confirmed_free_only'}
        with self.assertRaisesRegex(ValueError, 'match the assigned service and route'):
            self.check({'service_fee_qualification': {'photon': free_qualification()}})

    def test_structured_environment_fee_evidence_does_not_require_an_answer_reference(self):
        self.config['resource_authorization'] = {
            'service': 'photon', 'route': 'public-search-api', 'fee_policy': 'confirmed_free_only',
            'service_fee': free_qualification()['service_fee']}
        value = self.check()
        self.assertEqual(value['status'], 'documented_free')
        self.assertIsNone(value['reference_sha256'])
        self.assertEqual(value['fee_evidence'][0]['source'], 'config.resource_authorization.service_fee')

    def test_unknown_opt_in_does_not_override_current_free_only_role(self):
        self.config['resource_authorization'] = {
            'service': 'photon', 'route': 'public-search-api', 'fee_policy': 'allow_unknown',
            'authorization_file': '/must-not-read-future-authorization.json'}
        with self.assertRaisesRegex(ValueError, 'authorized new role/input version'):
            self.check(photon_reference())

    def test_missing_qualification_holds_all_new_prepares_by_default(self):
        for protocol in (pipeline.HANDOFF_PROTOCOL, 'afs-20261010'):
            self.config['trial_protocol'] = protocol
            with self.subTest(protocol=protocol), self.assertRaisesRegex(ValueError, 'hold for preparation review'):
                self.check()

    def test_explicit_legacy_compatibility_is_private_unchecked_only(self):
        self.config.update(trial_protocol='afs-20261010', admission_mode='legacy_unchecked')
        value = self.check()
        self.assertEqual(value['status'], 'unchecked')
        self.assertIn('not confirmed', value['warnings'][0])
        self.config['trial_protocol'] = pipeline.HANDOFF_PROTOCOL
        with self.assertRaisesRegex(ValueError, 'unavailable for the current protocol'):
            self.check()

    def test_legacy_unchecked_cannot_release_explicit_unknown_or_hold(self):
        self.config.update(trial_protocol='afs-20261010', admission_mode='legacy_unchecked')
        with self.assertRaisesRegex(ValueError, 'unknown under the confirmed-free-only'):
            self.check(photon_reference())
        with self.assertRaisesRegex(ValueError, 'assigned route is held'):
            self.check({'cohort_disclosure': {'held_routes': {'photon/public-search-api': 'hold'}}})

    def test_malformed_current_qualification_is_a_preparation_error(self):
        with self.assertRaisesRegex(ValueError, 'assigned service_fee must be an object'):
            self.check({'service_fee_qualification': {'photon': {'service_fee': None}}})


class FreezeAdmissionTests(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp
    prepare = fixtures.PipelineTests.prepare

    def test_unknown_qualification_stops_before_run_creation(self):
        self.config['trial_protocol'] = pipeline.HANDOFF_PROTOCOL
        pipeline.write(self.root / 'reference.json', {'service_fee_qualification': {
            'fixture': photon_reference()['service_fee_qualification']['photon']}})
        self.config['reference'] = str(self.root / 'reference.json')
        pipeline.write(self.config_path, self.config)
        with patch.object(pipeline, 'invoke') as invoke:
            with self.assertRaisesRegex(ValueError, 'unknown under the confirmed-free-only'):
                self.prepare()
            invoke.assert_not_called()
        self.assertFalse(self.directory.exists())

    def test_missing_current_qualification_stops_before_run_creation(self):
        self.config['trial_protocol'] = pipeline.HANDOFF_PROTOCOL
        self.config.pop('reference')
        pipeline.write(self.config_path, self.config)
        with self.assertRaisesRegex(ValueError, 'hold for preparation review'):
            self.prepare()
        self.assertFalse(self.directory.exists())

    def test_plan_binds_exact_frozen_bytes_and_remains_outside_role_inputs(self):
        self.prepare()
        frozen = self.directory / 'frozen'
        value = pipeline.read(frozen / 'admission.json')
        self.assertEqual(value['status'], 'documented_free')
        self.assertEqual(value['reference_sha256'], pipeline.digest(frozen / 'grading/reference.json'))
        self.assertEqual(value['execution_role_sha256'], pipeline.digest(frozen / 'execution/AGENTS.md'))
        self.assertEqual(value['task']['sha256'], pipeline.read(self.directory / 'task.json')['sha256'])
        self.assertEqual((frozen / 'admission.json').stat().st_mode & 0o777, 0o600)
        for role in ('execution', 'grading'):
            self.assertFalse((frozen / role / 'admission.json').exists())
        pipeline.verify(self.directory)
        pipeline.write(frozen / 'admission.json', {**value, 'status': 'unchecked'})
        with self.assertRaisesRegex(ValueError, 'Frozen inputs changed: admission.json'):
            pipeline.verify(self.directory)

    def test_original_reference_changes_do_not_change_frozen_admission(self):
        self.prepare()
        frozen = self.directory / 'frozen'
        original = pipeline.read(frozen / 'admission.json')
        pipeline.write(self.config['reference'], {'service_fee_qualification': {
            'fixture': photon_reference()['service_fee_qualification']['photon']}})
        pipeline.verify(self.directory)
        self.assertEqual(pipeline.read(frozen / 'admission.json'), original)

    def test_old_frozen_run_verification_and_dispatch_do_not_reapply_new_prepare_rules(self):
        self.prepare()
        # Reproduce the absence of the new plan in an old valid frozen run.
        (self.directory / 'frozen/admission.json').unlink()
        hashes = pipeline.read(self.directory / 'frozen-hashes.json')
        hashes.pop('admission.json')
        pipeline.write(self.directory / 'frozen-hashes.json', hashes)
        with patch.object(pipeline, 'admission_plan', side_effect=AssertionError('retroactive admission')):
            pipeline.verify(self.directory)
            state = pipeline.advance(self.directory)
        self.assertEqual(state['phase'], 'execution_running')


if __name__ == '__main__':
    unittest.main()
