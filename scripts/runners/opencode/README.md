# OpenCode runner

This command adapter runs the repository pipeline on an SSH-accessible Linux
host. It uses the BigModel **Coding Plan** endpoint and OpenCode's JSON CLI;
no desktop automation or ZCode login is involved. The pipeline remains independent
of this adapter; another runner implements the same four-command protocol.

## Setup and reuse

The controller needs Python 3.11+ and SSH. The Linux host needs Docker and
noninteractive `sudo -n docker` for the selected SSH user. Configure SSH
authentication and host-key trust first; the scripts do not disable host-key
checking. They do not create cloud resources or purchase capacity.

Build `Dockerfile` once. `OPENCODE_VERSION` pins the CLI; `DEBIAN_MIRROR` can select
an appropriate Debian mirror. Keep image digests and installed versions in the
private batch manifest. Preinstall `ripgrep`, since OpenCode otherwise downloads
it on the first file search in each fresh home.

Provision a dedicated container per service/route and a separate grader container.
Limit memory, CPUs and PIDs; publish no ports and mount neither the host home nor
the Docker socket. The image runs as uid 1000. Only the controller uses root to
collect records and maintain `/run/afs` with mode 0700. `provision.py up` installs
the worker and recorder there and sends a mode-0600 `bigmodel.key` over SSH stdin.
The key
must be a Coding Plan key; the proxy cannot forward to the normal pay-as-you-go
API. Do not put these private files in the model's workspace.

Create a private adapter configuration outside Git (for example under the ignored
`data/experiments/results/` directory). Infrastructure values below are placeholders:

```json
{
  "host": "your-ssh-alias",
  "remote_root": "/private/runner-root",
  "key_file": "/private/coding-plan.key",
  "image": "afs-opencode:1.18.29",
  "memory": "2g",
  "cpus": 1,
  "pids_limit": 256,
  "containers": {
    "execution-runtime": "service-route-container",
    "grading-runtime": "grader-container"
  },
  "retained_paths": {
    "execution-runtime": ["credentials.json", "installed-tools"],
    "grading-runtime": []
  }
}
```

Use the same file for provisioning and dispatch:

```sh
# Once per image/version; no model calls.
python3 scripts/runners/opencode/provision.py --config /private/adapter.json build
# Creates containers or restarts stopped containers and refreshes worker code.
python3 scripts/runners/opencode/provision.py --config /private/adapter.json up
```

`up` prints the actual OpenCode version, image ID and resource limits. Save that
output in the private batch manifest; use the measured version in the pipeline's
`harness`. It refuses running containers and containers it did not create.
It does not migrate existing containers to a new image: use new container names
when changing the image. Failed setup can leave its own containers present;
inspect their state before retrying. Optional `build_args` can set
`OPENCODE_VERSION` and `DEBIAN_MIRROR`.

The remote root must be writable by the SSH user. Supply service credentials separately
under `/home/node/service-tools` and authorize their exact scope in the pipeline
configuration. `retained_paths` lists top-level entries to preserve for subsequent
tasks: credentials/configuration and installed service dependencies, not previous
answers or generated task scripts. Other state is archived to `/run/afs/archive`.
Each task starts with a fresh home, session and workspace. An installation batch
continues in the same service container. Stop containers after the batch; keeping
the image avoids reinstalling OpenCode next time.

Use these command arrays for each pipeline role, replacing the operation:

```json
["python3", "/path/to/adapter.py", "--config", "/private/adapter.json", "start", "{request}"]
```

The supported operations are `start`, `status`, `collect`, `stop`. Use
`scripts/pipeline.py prepare/run/status/record` as the controller. Grading gets
its own frozen role instructions and the completed execution evidence. It does
not inherit the execution session or its service credentials. Follow the
[pipeline configuration](../../../data/experiments/AGENTS.md#通用-pipeline-的使用)
for task selection, permissions, attachments and references. In each role set
`model` to `glm-5.3-flash`, `reasoning_effort` to `high`, the measured OpenCode
version, and one distinct configured runtime. Fill all four command arrays with
the adapter's absolute path and the external configuration path. Service/task IDs
belong to the task configuration; connection details and keys stay private.

```sh
python3 scripts/pipeline.py prepare data/experiments/results/<run-id> --config /private/task.json
python3 scripts/pipeline.py run data/experiments/results/<run-id>
python3 scripts/pipeline.py status data/experiments/results/<run-id>
# After checking the selected public evidence:
python3 scripts/pipeline.py record data/experiments/results/<run-id> --generate
# After all workers finish; stop these batch containers, retaining their state.
python3 scripts/runners/opencode/provision.py --config /private/adapter.json stop
```

For an active task use `pipeline.py stop` first. A runtime lock rejects overlapping
workers within one container. Parallel tasks need separate service/route
containers and separate grader runtimes; the controller schedules their budgets
and the host's available capacity. Model request capture stays enabled throughout.

`collect` retains raw CLI events, session export, actual outgoing model
messages/tools, streaming responses, artifacts and a runtime receipt. The wire
capture lives outside the executor's permissions. All of this stays private;
only explicitly selected and reviewed evidence belongs in public results.

Token normalization reconciles each wire response with OpenCode's independent
`step_finish` counters. OpenCode's `input` excludes cache hits and its `output`
excludes reasoning; both are restored to inclusive canonical counts. BigModel's
automatic cache has a hit count and no separate billable cache-write counter.
Missing/failed requests or inconsistent totals remain incomplete. The pipeline
computes model estimates from its frozen LiteLLM rates, not OpenCode's Coding
Plan `$0` display. Service charges still require the independent grader's
supported billing evidence.

This adapter is initially exercised with the GitHub REST route. Native MCP,
SDK/CLI installation batches and concurrent load require their own trials;
working SSH dispatch alone does not verify those paths.

The collector preserves `assessment.raw.json`. It can mechanically nest existing
`rule`, `observed`, `evidence` fields under `service_cost.applicability` and resolve
the documented final-answer alias to the actual captured answer. These operations
are logged in `adapter-normalizations.json`; they never add a billing fact, change
a judgment, or guess an amount. Missing evidence is still rejected by the shared
validator. Rejected grading attempts remain part of the recorded grading overhead.
