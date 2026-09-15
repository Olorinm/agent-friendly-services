import importlib.util
import json
from pathlib import Path
import signal
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('runtime_stop', Path(__file__).resolve().parents[1] / 'scripts/runners/opencode/runtime_stop.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class RuntimeStopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        (self.directory / 'process.json').write_text(json.dumps({'pid': 100, 'proxy_pid': 101}))

    def test_missing_receipt_is_not_reported_as_stopped(self):
        (self.directory / 'process.json').unlink()
        self.assertFalse(runtime.stop(self.directory, 'worker')['stopped'])

    def test_waits_for_model_proxy_and_worker_to_exit(self):
        running = [True]
        def finish(_): running[0] = False
        with patch.object(runtime, 'worker_running', side_effect=lambda _: running[0]), \
                patch.object(runtime, 'alive', side_effect=lambda *a, **k: running[0]), \
                patch.object(runtime.os, 'killpg') as kill, patch.object(runtime.time, 'sleep', side_effect=finish):
            self.assertTrue(runtime.stop(self.directory, 'worker')['stopped'])
        kill.assert_called_once_with(100, signal.SIGTERM)

    def test_absent_worker_does_not_signal_stale_child_pids(self):
        with patch.object(runtime, 'worker_running', return_value=False), \
                patch.object(runtime, 'alive', return_value=True), patch.object(runtime.os, 'killpg') as kill:
            self.assertFalse(runtime.stop(self.directory, 'worker')['stopped'])
        kill.assert_not_called()

    def test_unresponsive_process_is_not_falsely_confirmed(self):
        clock = [0]
        def tick(_): clock[0] += 1
        with patch.object(runtime, 'worker_running', return_value=True), \
                patch.object(runtime, 'alive', return_value=True), \
                patch.object(runtime.time, 'monotonic', side_effect=lambda: clock[0]), \
                patch.object(runtime.time, 'sleep', side_effect=tick), patch.object(runtime.os, 'killpg') as kill:
            self.assertFalse(runtime.stop(self.directory, 'worker', timeout=5)['stopped'])
        self.assertEqual([c.args for c in kill.call_args_list], [(100, signal.SIGTERM), (100, signal.SIGKILL)])


if __name__ == '__main__':
    unittest.main()
