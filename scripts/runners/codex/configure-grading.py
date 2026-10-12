#!/usr/bin/env python3
"""Create a new private run config; preserve the selected execution role exactly."""
import argparse
import copy
import json
import os
from pathlib import Path


def configure(source, adapter, runtime, seconds=600):
    config = copy.deepcopy(source)
    if runtime == config['execution']['runtime']: raise ValueError('Separate grader runtime required')
    path = str(Path(__file__).with_name('adapter.py').resolve())
    config['grading'] = {'runtime': runtime, 'model': 'gpt-6.1-sol', 'reasoning_effort': 'high',
        'harness': {'name': 'codex', 'version': '0.162.0', 'mode': 'noninteractive'},
        'seconds': seconds, 'billing_mode': 'chatgpt',
        'commands': {op: ['python3', path, '--config', str(Path(adapter).resolve()), op, '{request}']
                     for op in ('start', 'status', 'collect', 'stop')}}
    config['trial_protocol'] = 'afs-20261012-codex-grading'
    return config


def main():
    os.umask(0o077)
    p = argparse.ArgumentParser(); p.add_argument('--source', type=Path, required=True)
    p.add_argument('--adapter', type=Path, required=True); p.add_argument('--runtime', required=True)
    p.add_argument('--output', type=Path, required=True); p.add_argument('--seconds', type=int, default=600)
    a = p.parse_args()
    if a.seconds < 1: p.error('Positive seconds required')
    if a.output.exists(): p.error('New config path required; frozen runs must not be overwritten')
    result = configure(json.loads(a.source.read_text()), a.adapter, a.runtime, a.seconds)
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n'); a.output.chmod(0o600)


if __name__ == '__main__': main()
