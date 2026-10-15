"""Capture real outputs without spending the file/disk budget on harness copies."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


capture = module('storage_opencode_capture', 'scripts/runners/opencode/capture_files.py')
grader = module('storage_codex_capture', 'scripts/runners/codex/artifact_capture.py')


class CaptureStorageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        # Production snapshots require uid 0; portable fixtures belong to the
        # test user and cannot manufacture a real root-owned tree on macOS.
        owner = patch.object(grader, 'CONTROLLER_UID', os.geteuid())
        owner.start(); self.addCleanup(owner.stop)

    def put(self, root, name, data=b'real response', mode=0o600):
        path = root/name; path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data); path.chmod(mode)
        return path

    def test_home_harness_caches_cannot_exhaust_the_user_file_count(self):
        home = self.root/'home'; home.mkdir()
        for index in range(30):
            self.put(home, f'.config/opencode/node_modules/lib/{index}.js', b'library'*100)
            self.put(home, f'.npm/_cacache/{index}', b'cache'*100)
        self.put(home, '.cache/opencode/models.json', b'catalog'*100)
        self.put(home, 'z-response.json', b'{"actual_service_rows":[1,2]}')
        stream = io.BytesIO()
        result = capture.archive({'home': str(home)}, stream, {'file_bytes': 1024, 'total_bytes': 1024, 'files': 1})
        self.assertEqual([row['path'] for row in result['files']], ['task-files/home/z-response.json'])
        self.assertEqual(len(result['omitted']), 3)
        self.assertFalse(result['complete_for_declared_file_scope'])
        self.assertTrue(all('cache' in row['reason'] for row in result['omitted']))

    def test_session_config_install_logs_and_similarly_named_task_paths_survive(self):
        home = self.root/'home'; temp = self.root/'temp'; home.mkdir(); temp.mkdir()
        names = ['.config/opencode/opencode.json', '.cache/opencode/actual-response.json',
                 '.npm/_logs/install.log', '.local/share/opencode/storage/session.json',
                 'user-project/node_modules/my-client/response.json']
        for name in names: self.put(home, name)
        temp_names = ['.cache/opencode/models.json', '.config/opencode/node_modules/response.json',
                      '.npm/_cacache/raw-response.json', '.abcd1234-00000000.so']
        for name in temp_names: self.put(temp, name)
        stream = io.BytesIO(); result = capture.archive({'home': str(home), 'tmp': str(temp)}, stream)
        self.assertEqual({row['path'] for row in result['files']},
                         {'task-files/home/'+name for name in names} | {'task-files/tmp/'+name for name in temp_names})
        self.assertTrue(result['complete_for_declared_file_scope'])

    def test_cache_names_with_unexpected_types_are_not_assumed_to_be_caches(self):
        home = self.root/'home'; home.mkdir()
        names = ['.config/opencode/node_modules', '.npm/_cacache',
                 '.cache/opencode/models.json/response.json']
        for name in names: self.put(home, name)
        result = capture.archive({'home': str(home)}, io.BytesIO())
        self.assertEqual({row['path'] for row in result['files']}, {'task-files/home/'+name for name in names})
        self.assertTrue(result['complete_for_declared_file_scope'])

    def fixture(self):
        controller = self.root/'controller'; controller.mkdir(mode=0o700)
        private = controller/'run-grading'; private.mkdir(mode=0o700)
        original = controller/'inputs'/private.name; original.mkdir(parents=True, mode=0o700)
        workspaces = self.root/'workspaces'; workspaces.mkdir()
        return private, original, workspaces

    def collect(self, workspace, private, workspaces):
        out = private/'output'; out.mkdir()
        self.put(out, 'session.raw.jsonl', b'original independent rollout')
        real_run = subprocess.run
        # Portable test: exercise the real subprocess/tar parser without requiring
        # a local uid 1000 account; assert the production privilege-drop hook.
        with patch.object(grader, 'WORKSPACE_ROOT', workspaces), patch.object(grader, 'identity', lambda: None) as identity, patch.object(grader.subprocess, 'run', wraps=real_run) as run:
            grader.collect_artifacts(workspace, private, out)
            self.assertIs(run.call_args.kwargs['preexec_fn'], identity)
            self.assertEqual(run.call_args.args[0][:3], ['python3', '-I', '-c'])
        self.assertEqual((out/'session.raw.jsonl').read_bytes(), b'original independent rollout')
        return out, json.loads((out/'artifact-input-index.json').read_text())

    def test_unchanged_frozen_response_is_indexed_not_copied_and_saves_disk(self):
        private, original, workspaces = self.fixture()
        response = os.urandom(1024*1024)
        self.put(original, 'execution/response.bin', response)
        self.put(original, 'AGENTS.md', b'frozen grading role')
        workspace = workspaces/private.name; shutil.copytree(original, workspace)
        self.put(workspace, 'assessment.json', b'{"status":"completed"}')
        self.put(workspace, 'codex-final.md', b'Independent result')
        legacy = io.BytesIO()
        with tarfile.open(fileobj=legacy, mode='w') as tar: tar.add(workspace, arcname='.')
        out, index = self.collect(workspace, private, workspaces)
        self.assertFalse((out/'artifacts/execution/response.bin').exists())
        self.assertEqual((original/'execution/response.bin').read_bytes(), response)
        self.assertEqual((out/'artifacts/assessment.json').read_bytes(), b'{"status":"completed"}')
        snapshot = index['input_snapshot']
        self.assertEqual(snapshot['entries']['execution/response.bin']['sha256'], hashlib.sha256(response).hexdigest())
        self.assertEqual(snapshot, grader.trusted_snapshot(private))
        self.assertFalse(index['complete_for_workspace_scope'])
        with tarfile.open(private/'artifacts.tar') as tar:
            self.assertNotIn('artifacts/execution/response.bin', tar.getnames())
        self.assertLess((private/'artifacts.tar').stat().st_size, len(legacy.getvalue())/20)
        print(f"Synthetic grading capture: {len(legacy.getvalue())} -> {(private/'artifacts.tar').stat().st_size} tar bytes")

    def test_modified_input_mode_new_same_basename_and_forged_index_are_preserved(self):
        private, original, workspaces = self.fixture()
        self.put(original, 'execution/response.json', b'original response')
        self.put(original, 'mode-only.txt', b'same bytes')
        self.put(original, 'deleted.txt', b'retained original')
        self.put(original, 'linked.txt', b'original')
        workspace = workspaces/private.name; shutil.copytree(original, workspace)
        self.put(workspace, 'execution/response.json', b'changed response')
        (workspace/'mode-only.txt').chmod(0o400)
        (workspace/'deleted.txt').unlink()
        canary = self.put(self.root, 'controller-secret', b'canary secret never read')
        (workspace/'linked.txt').unlink(); (workspace/'linked.txt').symlink_to(canary)
        self.put(workspace, 'new/response.json', b'original response')
        self.put(workspace, 'artifact-input-index.json', b'{"forged":"baseline"}')
        out, index = self.collect(workspace, private, workspaces)
        self.assertEqual((out/'artifacts/execution/response.json').read_bytes(), b'changed response')
        self.assertEqual((out/'artifacts/new/response.json').read_bytes(), b'original response')
        self.assertEqual((out/'artifacts/artifact-input-index.json').read_bytes(), b'{"forged":"baseline"}')
        self.assertNotIn('canary secret', json.dumps(index))
        files = {row['path']: row for row in index['files']}
        self.assertEqual(files['mode-only.txt']['mode'], 0o400)
        self.assertEqual(files['mode-only.txt']['change'], 'modified_input')
        self.assertEqual(files['new/response.json']['change'], 'new')
        omitted = {row['path']: row for row in index['omitted']}
        self.assertEqual(omitted['deleted.txt']['change'], 'deleted_input')
        self.assertEqual(omitted['linked.txt']['change'], 'replaced_by_link')

    def test_directory_link_never_reads_controller_or_grader_auth(self):
        private, original, workspaces = self.fixture()
        self.put(original, 'execution/input.json', b'known input')
        workspace = workspaces/private.name; shutil.copytree(original, workspace)
        shutil.rmtree(workspace/'execution')
        outside = self.root/'auth'; self.put(outside, 'auth.json', b'secret login token')
        (workspace/'execution').symlink_to(outside)
        out, index = self.collect(workspace, private, workspaces)
        self.assertFalse((out/'artifacts/execution/auth.json').exists())
        self.assertNotIn('secret login token', json.dumps(index))
        omitted = {row['path']: row for row in index['omitted']}
        self.assertEqual(omitted['execution/input.json']['change'], 'unread_under_link')

    def test_snapshot_rejects_writable_wrong_owner_and_linked_originals(self):
        private, original, _ = self.fixture()
        file = self.put(original, 'input.json')
        file.chmod(0o666)
        with self.assertRaisesRegex(ValueError, 'Unsafe original'): grader.trusted_snapshot(private)
        file.chmod(0o600)
        with patch.object(grader, 'CONTROLLER_UID', os.geteuid()+1):
            with self.assertRaisesRegex(ValueError, 'controller-owned'): grader.trusted_snapshot(private)
        file.unlink(); file.symlink_to(self.root/'not-an-input')
        with self.assertRaisesRegex(ValueError, 'Unsafe original'): grader.trusted_snapshot(private)

    def test_production_identity_drops_groups_gid_and_uid(self):
        with patch.object(grader.os, 'setgroups') as groups, patch.object(grader.os, 'setgid') as gid, patch.object(grader.os, 'setuid') as uid:
            grader.identity()
        groups.assert_called_once_with([]); gid.assert_called_once_with(1000); uid.assert_called_once_with(1000)

    def test_missing_original_snapshot_never_discards_same_named_files(self):
        private, original, workspaces = self.fixture(); original.rmdir()
        workspace = workspaces/private.name; workspace.mkdir()
        self.put(workspace, 'prompt.txt', b'must retain without trusted original')
        out, index = self.collect(workspace, private, workspaces)
        self.assertFalse(index['input_snapshot']['available'])
        self.assertEqual((out/'artifacts/prompt.txt').read_bytes(), b'must retain without trusted original')

    def test_model_pythonpath_cannot_shadow_the_isolated_collector(self):
        private, original, workspaces = self.fixture()
        self.put(original, 'input.json')
        workspace = workspaces/private.name; shutil.copytree(original, workspace)
        self.put(workspace, 'assessment.json', b'{"independent":"result"}')
        poison = self.root/'pythonpath'
        self.put(poison, 'hashlib.py', b'raise RuntimeError("model-controlled import")')
        with patch.dict(os.environ, {'PYTHONPATH': str(poison)}):
            out, _ = self.collect(workspace, private, workspaces)
        self.assertEqual((out/'artifacts/assessment.json').read_bytes(), b'{"independent":"result"}')


if __name__ == '__main__': unittest.main()
