"""The controller must seal imported inputs before any grader process starts."""
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tarfile
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
spec = importlib.util.spec_from_file_location('codex_input_adapter', ROOT/'scripts/runners/codex/adapter.py')
adapter = importlib.util.module_from_spec(spec); spec.loader.exec_module(adapter)


class CodexInputPreparationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()

    def test_transport_materializes_hardlinks_without_changing_sources(self):
        source = self.root/'source'; source.mkdir()
        first = source/'prompt.txt'; first.write_bytes(b'frozen user input\n')
        os.link(first, source/'same-input.txt'); first.chmod(0o640)
        before = {p.name: (p.read_bytes(), p.stat()) for p in source.iterdir()}
        raw = adapter.archive(source)
        with tarfile.open(fileobj=io.BytesIO(raw)) as tar:
            self.assertEqual(len(tar.getmembers()), 2)
            for member in tar:
                self.assertTrue(member.isfile()); self.assertFalse(member.islnk())
                self.assertEqual(tar.extractfile(member).read(), before[member.name][0])
        for path in source.iterdir():
            data, info = before[path.name]
            self.assertEqual(path.read_bytes(), data)
            after = path.stat()
            self.assertEqual((after.st_ino, after.st_nlink, after.st_mode, after.st_uid, after.st_gid),
                             (info.st_ino, info.st_nlink, info.st_mode, info.st_uid, info.st_gid))

    def test_transport_rejects_links_and_special_files(self):
        source = self.root/'source'; source.mkdir()
        (source/'link').symlink_to(self.root)
        with self.assertRaisesRegex(ValueError, 'links forbidden'): adapter.archive(source)
        (source/'link').unlink(); os.mkfifo(source/'pipe')
        with self.assertRaisesRegex(ValueError, 'special files forbidden'): adapter.archive(source)

    def tree(self):
        controller = self.root/'controller'; controller.mkdir(mode=0o700)
        inputs = controller/'inputs'; inputs.mkdir(mode=0o700)
        tree = inputs/'fixture-grading'; tree.mkdir(mode=0o777); tree.chmod(0o777)
        (tree/'prompt.txt').write_bytes(b'unchanged frozen prompt\n')
        (tree/'prompt.txt').chmod(0o7777)
        return controller, tree

    def prepare_portable(self, controller, tree, failure=False):
        # Exercise the production script against real bytes/permissions. Only
        # ownership syscalls are emulated because macOS tests cannot become root.
        # All imported nodes begin uid/gid 1000; protected parents begin uid 0.
        real_stat, real_lstat, real_fstat = os.stat, os.lstat, os.fstat
        owners = {}; changed = []
        def info(value):
            owner = owners.get((value.st_dev, value.st_ino), (1000, 1000))
            fields = list(value); fields[4:6] = owner
            return os.stat_result(fields)
        for path in (controller, tree.parent):
            value = real_lstat(path); owners[value.st_dev, value.st_ino] = (0, 0)
        def chown(fd, uid, gid):
            if failure: raise PermissionError('normalization denied')
            value = real_fstat(fd); owners[value.st_dev, value.st_ino] = (uid, gid)
            changed.append((value.st_ino, uid, gid))
        script = adapter.PREPARE_INPUT_TREE.replace("root=Path('/run/afs');", 'root=Path('+repr(str(controller))+');', 1)
        output = io.StringIO()
        with patch.object(os, 'geteuid', return_value=0), patch.object(os, 'stat', side_effect=lambda *a, **k: info(real_stat(*a, **k))), patch.object(os, 'lstat', side_effect=lambda *a, **k: info(real_lstat(*a, **k))), patch.object(os, 'fstat', side_effect=lambda fd: info(real_fstat(fd))), patch.object(os, 'fchown', side_effect=chown), patch.object(sys, 'argv', ['prepare', str(tree)]), redirect_stdout(output):
            exec(compile(script, '<controller-input-preparation>', 'exec'), {})
        return json.loads(output.getvalue()), changed

    def test_uid1000_import_becomes_root_data_without_special_bits_or_byte_changes(self):
        controller, tree = self.tree()
        data = (tree/'prompt.txt').read_bytes(); digest = hashlib.sha256(data).hexdigest()
        result, changed = self.prepare_portable(controller, tree)
        self.assertTrue(result['content_unchanged']); self.assertEqual(result['files'], 1)
        self.assertEqual({(uid, gid) for _, uid, gid in changed}, {(0, 0)})
        self.assertEqual(len(changed), 2)
        self.assertEqual(stat.S_IMODE(tree.stat().st_mode), 0o755)
        self.assertEqual(stat.S_IMODE((tree/'prompt.txt').stat().st_mode), 0o755)
        self.assertEqual(hashlib.sha256((tree/'prompt.txt').read_bytes()).hexdigest(), digest)

    def test_import_links_hardlinks_and_special_items_fail_before_chown(self):
        for kind in ('symlink', 'directory-link', 'hardlink', 'fifo'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory(dir=self.root) as tmp:
                root = self.root; self.root = Path(tmp)
                try:
                    controller, tree = self.tree(); target = tree/'unsafe'
                    if kind == 'symlink': target.symlink_to(tree/'prompt.txt')
                    elif kind == 'directory-link': target.symlink_to(controller, target_is_directory=True)
                    elif kind == 'hardlink': os.link(tree/'prompt.txt', target)
                    else: os.mkfifo(target)
                    before = (tree/'prompt.txt').stat().st_mode
                    # A call to chown would raise PermissionError instead: the
                    # structural ValueError must occur before any normalization.
                    with self.assertRaises(ValueError):
                        self.prepare_portable(controller, tree, failure=True)
                    self.assertEqual((tree/'prompt.txt').stat().st_mode, before)
                finally: self.root = root

    def test_failed_ownership_normalization_is_fatal(self):
        controller, tree = self.tree()
        with self.assertRaisesRegex(PermissionError, 'normalization denied'):
            self.prepare_portable(controller, tree, failure=True)
        self.assertEqual((tree/'prompt.txt').read_bytes(), b'unchanged frozen prompt\n')

    def start(self, fail=False):
        inputs = self.root/'source'; inputs.mkdir()
        (inputs/'prompt.txt').write_bytes(b'frozen task bytes')
        request = {'role': 'grading', 'model': 'gpt-6.1-sol', 'reasoning_effort': 'high',
                   'runtime': 'grade', 'run_id': 'fixture', 'input': str(inputs)}
        path = self.root/'request.json'; original = json.dumps(request).encode(); path.write_bytes(original)
        calls = []; prepared = {'policy': 'root-owned-data-input-v1', 'content_unchanged': True}
        def remote(config, argv, data=None, check=True):
            calls.append((argv, data))
            if '-c' in argv and adapter.PREPARE_INPUT_TREE in argv:
                self.assertIn('-I', argv)
                if fail: raise subprocess.CalledProcessError(1, argv)
                return SimpleNamespace(stdout=json.dumps(prepared).encode())
            if any('hashlib.sha256' in x for x in argv):
                return SimpleNamespace(stdout=json.dumps({'worker.py': hashlib.sha256(b'source').hexdigest()}).encode())
            return SimpleNamespace(stdout=b'sha256:test-image\n')
        config = {'billing_mode': 'chatgpt', 'containers': {'grade': 'fixture-container'}, 'remote_root': '/private/controller'}
        with patch.object(adapter, 'load', return_value=config), patch.object(adapter, 'sources', return_value={'worker.py': b'source'}), patch.object(adapter, 'remote_ssh', side_effect=remote), patch.object(sys, 'argv', ['adapter', '--config', 'fixture.json', 'start', str(path)]), redirect_stdout(io.StringIO()):
            if fail:
                with self.assertRaises(subprocess.CalledProcessError): adapter.main()
            else: adapter.main()
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual((inputs/'prompt.txt').read_bytes(), b'frozen task bytes')
        return calls, request, prepared

    def test_start_seals_after_copy_before_worker_and_keeps_frozen_request(self):
        calls, request, prepared = self.start()
        imported = next(i for i, (argv, _) in enumerate(calls) if argv[:4] == ['sudo', '-n', 'docker', 'cp'])
        normalized = next(i for i, (argv, _) in enumerate(calls) if adapter.PREPARE_INPUT_TREE in argv)
        worker = next(i for i, (argv, _) in enumerate(calls) if '-d' in argv)
        self.assertLess(imported, normalized); self.assertLess(normalized, worker)
        staged = json.loads(next(data for argv, data in calls if argv[0] == 'tee'))
        self.assertEqual(staged['input_preparation'], prepared)
        for key, value in request.items(): self.assertEqual(staged[key], value)

    def test_failed_sealing_never_stages_request_or_starts_worker(self):
        calls, _, _ = self.start(fail=True)
        self.assertFalse(any('-d' in argv or argv[0] == 'tee' for argv, _ in calls))


if __name__ == '__main__': unittest.main()
