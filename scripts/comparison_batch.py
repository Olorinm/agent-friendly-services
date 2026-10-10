"""Run prepared comparison groups with a global session cap and runtime exclusion.

Reuse the original group barrier, evidence snapshots and role adapters. Different
groups can overlap, but a retained-state runtime must never host two sessions.
"""
import argparse
import json
from pathlib import Path
import time

import comparison_group as groups
import pipeline as runs

TERMINAL = ('reviewed', 'needs_attention', 'stopped')


def inventory(directories):
    entries, seen = [], set()
    for directory in directories:
        manifest, state = groups.load(directory)
        for member in manifest['members']:
            path = Path(member['directory'])
            if path in seen:
                raise ValueError('A run cannot belong to two batch groups')
            seen.add(path)
            entries.append((directory, path, runs.read(path / 'config.json'), runs.read(path / 'state.json')))
    return entries


def occupied(entries):
    active = []
    for group, path, config, state in entries:
        if state['phase'] == 'stopped' and state.get('stopped_role') and not state.get('stop_confirmed'):
            raise ValueError('Unconfirmed runtime stop; reconcile before further batch dispatch')
        if groups.active(state):
            role = state['phase'].split('_')[0]
            active.append((group, config[role]['runtime'], path))
    if len({runtime for _, runtime, _ in active}) != len(active):
        raise ValueError('Multiple active sessions already occupy the same runtime')
    return active


def advance(directories, max_concurrency, dispatch_guard=None):
    if type(max_concurrency) is not int or max_concurrency < 1:
        raise ValueError('Batch max_concurrency must be a positive integer')
    directories = [Path(p).resolve() for p in directories]
    if not directories or len(set(directories)) != len(directories):
        raise ValueError('Provide distinct prepared comparison groups')
    for directory in directories:
        active = occupied(inventory(directories))
        if len(active) > max_concurrency:
            raise ValueError('Existing sessions exceed the requested batch ceiling')
        outside = [item for item in active if item[0] != directory]
        groups.advance(directory, busy_runtimes={runtime for _, runtime, _ in outside},
                       max_active=max_concurrency - len(outside), dispatch_guard=dispatch_guard)
    # Check again before reporting: an uncertain stop in the last group is also
    # a batch-level blocker, not permission to dispatch more on the next tick.
    active = occupied(inventory(directories))
    states = {p.name: runs.read(p / 'state.json')['phase'] for p in directories}
    done = all(phase in TERMINAL for phase in states.values())
    phase = ('reviewed' if all(s == 'reviewed' for s in states.values()) else 'needs_attention') if done else 'running'
    return {'phase': phase, 'max_concurrency': max_concurrency, 'active_sessions': len(active), 'groups': states}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('groups', nargs='+', type=Path)
    parser.add_argument('--max-concurrency', type=int, required=True)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    directories = [p.resolve() for p in args.groups]
    entries = inventory(directories)
    # Own every member and group lock so another controller cannot clear a
    # container between the occupancy check and the actual dispatch.
    with groups.locks([*directories, *(path for _, path, _, _ in entries)]):
        previous = None
        while True:
            state = advance(directories, args.max_concurrency)
            if state != previous:
                print(json.dumps(state), flush=True)
                previous = state
            if args.once or state['phase'] in TERMINAL:
                return
            time.sleep(2)


if __name__ == '__main__':
    main()
