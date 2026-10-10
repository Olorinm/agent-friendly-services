import importlib.util
from pathlib import Path
import socket
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location('network_preflight', Path(__file__).resolve().parents[1]/'scripts/runners/opencode/network_preflight.py')
probe = importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)


class PreflightTests(unittest.TestCase):
    def test_accepted_auth_surface_is_reachable_without_reading_body_or_following_redirects(self):
        conn = Mock();conn.getresponse.return_value.status = 401
        resolver = Mock(return_value=[(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('203.0.113.1', 443))])
        result = probe.check([{'url':'https://example.com/auth','accepted_statuses':[401]}], resolve=resolver, connect=Mock(return_value=conn))
        self.assertTrue(result['ready'])
        conn.getresponse.return_value.read.assert_not_called()
        conn.request.assert_called_once()
        conn.close.assert_called_once()

    def test_403_and_dns_failure_hold_dispatch_without_claiming_a_cause(self):
        conn = Mock();conn.getresponse.return_value.status = 403
        result = probe.check([{'url':'https://example.com'}], resolve=Mock(return_value=[]), connect=Mock(return_value=conn))
        self.assertFalse(result['ready'])
        self.assertIn('unresolved',result['checks'][0]['reason'])
        result = probe.check([{'url':'https://example.com'}], resolve=Mock(side_effect=socket.gaierror('fixture')))
        self.assertFalse(result['ready'])
        self.assertEqual(result['checks'][0]['reason'],'gaierror')

    def test_preflight_cannot_create_resources_or_send_credentials(self):
        for target in ({'url':'https://example.com','method':'POST'}, {'url':'https://user:secret@example.com'}, {'url':'http://example.com'}):
            with self.assertRaises(ValueError): probe.validate([target])


if __name__ == '__main__': unittest.main()
