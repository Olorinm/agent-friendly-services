# OpenCode runner

This command adapter runs the repository pipeline on an SSH-accessible Linux
host. It supports the DeepSeek direct API and BigModel **Coding Plan** through OpenCode's JSON CLI;
no desktop automation or ZCode login is involved. The pipeline remains independent
of this adapter; another runner implements the same four-command protocol.

## Setup and reuse

The controller needs Python 3.11+ and SSH. The Linux host needs Docker and
noninteractive `sudo -n docker` for the selected SSH user. Configure SSH
authentication and host-key trust first; the scripts do not disable host-key
checking. They do not create cloud resources or purchase capacity.

Build `Dockerfile` once. `OPENCODE_VERSION` pins the CLI; `DEBIAN_MIRROR` can select
an appropriate Debian mirror. Keep image digests and installed versions in the
private batch manifest. The image includes `ripgrep`, `pip`, and Poppler's
`pdftotext` so ordinary file search, Python dependency installation, and public
PDF extraction work in fresh runtimes without task-specific helper scripts.

Provision a dedicated container per service/route and a separate grader container.
Limit memory, CPUs and PIDs; publish no ports and mount neither the host home nor
the Docker socket. The image runs as uid 1000. Only the controller uses root to
collect records and maintain `/run/afs` with mode 0700. `provision.py up` installs
the worker and recorder there and sends a mode-0600 `model.key` and provider
settings over SSH stdin. Choose `provider: "deepseek"` for the DeepSeek API, or
`provider: "zhipuai-coding-plan"` for a BigModel Coding Plan key. Omitting the
provider preserves the legacy BigModel route. The proxy forwards only to the
selected provider's fixed endpoint and never exposes its key to the model.
Do not put these private files in the model's workspace.

Optional private settings `max_model_requests` and `deadline_epoch` bound each
role's forwarded requests and its absolute Unix deadline. The proxy checks these
before contacting the provider, pins the requested model, and caps DeepSeek
output at 32,000 tokens per request. Failed upstream attempts still consume the
request ceiling; proxy restarts count previously captured requests. The worker
also stops its model process before the absolute deadline. Each result retains
`controller-limits.json` and any proxy guard events. Declare the limits in every
affected batch's frozen environment and preparation note; changed budgets are
separate experimental conditions. These per-role limits are not a shared dollar
budget: the controller must reserve a conservative cost for all dispatched roles,
including grading, and retain the reservation when usage cannot be reconciled.

Create a private adapter configuration outside Git (for example under the ignored
`data/experiments/results/` directory). Infrastructure values below are placeholders:

```json
{
  "host": "your-ssh-alias",
  "remote_root": "/private/runner-root",
  "provider": "deepseek",
  "model": "deepseek-flash",
  "key_file": "/private/deepseek.key",
  "image": "afs-opencode:1.18.35",
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
  },
  "retained_children": {
    "execution-runtime": {
      "installed-tools": ["package.json", "package-lock.json", "node_modules"]
    }
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
After changing runner code or provider settings, run `up` on stopped runtimes
to install the updated worker, recorder and provider configuration. Use separate
containers and batch records when changing the model for a new comparison.
It does not migrate existing containers to a new image: use new container names
when changing the image. Failed setup can leave its own containers present;
inspect their state before retrying. Optional `build_args` can set
`OPENCODE_VERSION` and `DEBIAN_MIRROR`.

The remote root must be writable by the SSH user. Supply service credentials separately
under `/home/node/service-tools` and authorize their exact scope in the pipeline
configuration. `retained_paths` lists top-level entries to preserve for subsequent
tasks: credentials/configuration and installed service dependencies, not previous
answers or generated task scripts. Other state is archived to `/run/afs/archive`.
For a retained dependency directory, optional `retained_children` lists its direct
children to keep. This archives task downloads written beside dependencies before
the next session. A named parent must be a real directory, never a symlink.
Review retained helper scripts and configuration for task-specific contents when
reusing an older container; a filename policy does not inspect file contents.
Each task starts with a fresh home, session and workspace. The worker
also archives previous `/tmp` and `/var/tmp` contents between sessions; task
downloads must not survive through a shared temporary directory. An installation batch
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
`model` to `deepseek-flash` (DeepSeek V4.1 Flash), `reasoning_effort` to `high`, the measured OpenCode
version, and one distinct configured runtime. Fill all four command arrays with
the adapter's absolute path and the external configuration path. Service/task IDs
belong to the task configuration; connection details and keys stay private.
Both execution and grading must explicitly select the new model. Existing
frozen GLM runs keep their recorded configuration; do not rewrite them or combine
their results with the new batch. The adapter rejects a GLM model sent to a
DeepSeek runtime, and vice versa.

```sh
python3 scripts/pipeline.py prepare data/experiments/results/<run-id> --config /private/task.json
python3 scripts/pipeline.py run data/experiments/results/<run-id>
python3 scripts/pipeline.py status data/experiments/results/<run-id>
# After checking the selected public evidence:
python3 scripts/pipeline.py record data/experiments/results/<run-id> --generate
# After all workers finish; stop these batch containers, retaining their state.
python3 scripts/runners/opencode/provision.py --config /private/adapter.json stop
```

For an active task use `pipeline.py stop` first; grouped runs use `pipeline.py
stop-group`. The adapter confirms that the model process group, capture proxy,
and worker have exited before returning `stopped: true`. A missing process
receipt or an unconfirmed stop requires reconciliation. A runtime lock rejects overlapping
workers within one container. Parallel tasks need separate service/route
containers and separate grader runtimes; the controller schedules their budgets
and the host's available capacity. Model request capture stays enabled throughout.

For multiple prepared comparison groups, run a single batch controller:

```sh
python3 scripts/comparison_batch.py --max-concurrency 10 /private/group-1 /private/group-2
```

The ceiling covers execution and grading sessions across these groups. The
controller also excludes occupied runtimes, so successive tasks can overlap
execution and grading without sharing a container concurrently. Each group still
seals its same-task answer snapshot before grading. Actual concurrency is bounded
by the available distinct runtimes; raising the ceiling does not create containers.
Container CPU and memory settings are upper limits, not reserved allocations.
Choose the batch ceiling from measured throughput and host memory headroom,
including cold OpenCode startup, tool execution and independent grading. More
sessions can increase local startup time enough to reduce overall throughput,
even when model inference runs remotely. Measure time to the first captured
model request separately from upstream response time before changing capacity.
Shared grader runtimes may be assigned to different runs while idle; each uses
a fresh home/session/workspace and retains no executor credentials or task state.
The controller holds all group/member locks and refuses further dispatch after an
unconfirmed runtime stop. Run the whole batch together, rather than independently
starting controllers that reuse its runtimes.

Peer metadata distinguishes declared members (`run_ids`) from members with an
answer in the frozen snapshot (`available_run_ids`). A member deferred before
dispatch contributes no answer or business failure. If only one service ran, the
public review label states that no other service answer was available.

`collect` retains raw CLI events, session export, actual outgoing model
messages/tools, streaming responses, artifacts and a runtime receipt. The wire
capture lives outside the executor's permissions. All of this stays private;
only explicitly selected and reviewed evidence belongs in public results.

The collector also extracts `tool-records.json` from the CLI events, preserving
each tool's exact input, output/error, status, and source line/hash. Failed or
unrecognized events are not silently treated as success. The shared pipeline
uses these private records to build `review-packet/index.json`, full per-call
files, and an empty assessment template for the grader. Previews explicitly mark
truncation; the original logs remain available. This saves log parsing and file
discovery without inferring a verdict or publishing raw tool records.
JSON CLI and SSE records are split on LF only; Unicode separators inside JSON
strings must remain part of the captured tool output.

Token normalization reconciles each wire response with OpenCode's independent
`step_finish` counters. OpenCode's `input` excludes cache hits and its `output`
excludes reasoning; both are restored to inclusive canonical counts. Both providers'
automatic cache has a hit count and no separate billable cache-write counter.
Missing/failed requests or inconsistent totals remain incomplete. The pipeline
computes model estimates from its frozen LiteLLM rates. Missing model prices stay
unknown; a Coding Plan `$0` display is not a model-cost estimate. Service charges still require the independent grader's
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

For a free-cost result with a plain-text `applicability`, the collector can move
that existing observation into `applicability.observed` when the original rule
and evidence are also present and there is no competing `observed` field. If
this layout repair lacks a `note`, it copies the existing rule text into it.
Conflicting or incomplete facts remain rejected; this is not another grading pass.
An existing nonempty list of evidence references may be joined with newlines for
the scalar `applicability.evidence` field, retaining every reference and its order.

Artifact collection never follows symbolic or hard links. It copies regular files
and lists omitted links in private `artifact-omissions.json`; other unsafe archive
entries still fail collection. The worker persists its observed process receipt
and usage before artifact collection, so a collection error does not erase them.
Historical captures that lack the process receipt must retain unknown status or
timing fields; a final model message alone does not establish a successful exit.
