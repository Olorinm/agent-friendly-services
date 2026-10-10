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

`up` prints the actual OpenCode version, image ID, resource limits and injected
runner source hashes. Save that
output in the private batch manifest; use the measured version in the pipeline's
`harness`. It refuses running containers and containers it did not create.
After changing runner code or provider settings, run `up` on stopped runtimes
to install the updated worker, recorder and provider configuration. Use separate
containers and batch records when changing the model for a new comparison.
It does not migrate existing containers to a new image: use new container names
when changing the image. Failed setup can leave its own containers present;
inspect their state before retrying. Optional `build_args` can set
`OPENCODE_VERSION` and `DEBIAN_MIRROR`.

The image digest does not identify the worker files installed under `/run/afs`.
Before allocating each new run, the adapter compares those files with its local
runner checkout. Missing or stale files stop dispatch before any model request;
there is no automatic upgrade or retry. Inspect and stop only the idle owned
runtime, preserve its preparation evidence, then use `up` to install the intended
version and record the changed conditions. The request and runtime receipt retain
this preflight hash manifest and timestamp. It describes the pre-dispatch read,
not protection against a controller changing files during a run. Collection and
status queries remain available for historical runs without requiring new code.

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
Source objects containing only `url`/`note`, or `ref`/`type`/`note`, may likewise
be joined into source strings with all supplied values retained. Ambiguous or
unrecognized fields are left for validation rather than silently discarded.

Artifact collection never follows symbolic or hard links. It copies regular files
and lists omitted links in private `artifact-omissions.json`; other unsafe archive
entries still fail collection. The worker persists its observed process receipt
and usage before artifact collection, so a collection error does not erase them.
Historical captures that lack the process receipt must retain unknown status or
timing fields; a final model message alone does not establish a successful exit.

## Continuous handoffs (protocol `afs-20261010`)

`scripts/task_queue.py` owns one runner pool and accepts new ready jobs while it
runs. Discovery and task-design sessions produce sourced inputs; the controller
checks those handoffs and submits a private job with `ready: true`. This flag is
an explicit readiness decision, not an automatic check of research quality.
The queue freezes the selected task/route, reference, materials, role files and
price snapshot. Unrelated catalog additions do not replace a submitted task.
It prepares business jobs only after their access dependencies pass independent
grading. Independent jobs overlap; each comparison still freezes all member
answers before launching its separate graders. Publication remains a separate
reviewed `pipeline.py record` operation and does not block the execution queue.

Initialize a **new authorized window**, with an explicit pool identity, deadline,
model-cost cap and total session concurrency:

```sh
python3 scripts/task_queue.py init /absolute/private/queue \
  --pool afs-johor --max-concurrency 8 \
  --budget-usd AMOUNT --expires-at TIMESTAMP_WITH_TIMEZONE
python3 scripts/task_queue.py submit /absolute/private/queue --spec /absolute/private/job.json
python3 scripts/task_queue.py run /absolute/private/queue
python3 scripts/task_queue.py status /absolute/private/queue
```

`--once` performs a resumable tick. The controller keeps waiting when the inbox
is empty, so a new handoff does not need a new heartbeat or batch restart. At the
deadline it stops paid workers, collects measured usage, saves state and exits.
It does not extend an expired authorization. Interrupted/uncertain starts are
never resent; a partial preparation or unconfirmed stop requires inspection.

### Resident cloud controller

The queue can run on the dedicated Docker host. Set `"transport": "local"` and
`"host": "localhost"` in its private adapter config. Omitting `transport` retains
the SSH behavior. Local operations execute literal argv without a shell and use
the same isolated worker, source-hash check, collection and stop protocol. This
does not let model containers access the controller's files or Docker socket.

Install a reviewed, versioned repository release, Python 3.11+, Node and the
locked npm dependencies on the controller host. Keep the release, private
configuration, credentials, references and queue owned by the operator; private
directories use mode 0700, files 0600. No HTTP queue endpoint is required. Resolve
all handoff paths on that host, including the adapter command path, reference,
materials and prerequisite run. Upload inputs to a new staging directory, verify
their hashes, and only then run `task_queue.py submit` over authenticated SSH.
The resulting `ready.json` is published last; merely copying a draft is not a
submission. Producers can submit while the one resident controller is running.
They cannot overwrite an existing job ID or its frozen handoff.

Use [the service template](controller.service.example) with the operator's actual
absolute paths. `Restart=no` is intentional: inspect saved run IDs, worker status,
stop confirmation and ledger before restarting after a failure. SIGTERM/SIGINT
prevents new dispatch, finishes the current adapter operation, then stops and
collects owned sessions. A stopped queue stays halted; starting its process again
does not grant a new authorization. The per-worker absolute deadline also stops
model calls if the controller disappears. Keep one controller per Docker pool;
do not start another Mac scheduler against the same containers.

This decouples task production, execution and publication. It does not manufacture
research tasks or approve evidence: the role sessions and controller still review
each sourced handoff before admission, and review public copies after grading.

Single-run handoff example (all paths private and absolute):

```json
{
  "id": "access-001",
  "kind": "run",
  "ready": true,
  "directory": "/absolute/repo/data/experiments/results/access-001",
  "config": "/absolute/private/access.config.json",
  "depends_on": []
}
```

For a business handoff, `depends_on` lists access job IDs; its run config also
keeps the existing `depends_on` prerequisite directory. A comparison handoff has
`kind: "comparison"`, `directory` for the new group, `round`, and `members`, each
with a new run `directory`, private `config`, and optional peer `evidence` paths.
Member identity is `(service, route)`, allowing REST/MCP comparison of one service
without inventing separate service IDs. Every execution and grader still needs
a distinct runtime. Three repeats are three predeclared rounds, not reruns until
three successes. See [the first repeat protocol](../../../data/experiments/tasks/resource-guards-and-repeats.md).

Queued roles require `max_model_requests` and the bounded OpenCode/DeepSeek
adapter. The ledger reserves a whole session ceiling before dispatch: every
request at the saved worst context/cache rate, 1,048,576 input tokens (or a larger
saved model limit) and the enforced 32,000 output cap. Known reconciled costs
replace reservations. Incomplete usage keeps its full ceiling, with any known
lower bound alongside it. These are estimates at frozen standard API rates,
not a provider bill; service fees and server fees remain separate. The queue
shows holds for insufficient budget, time or occupied shared resources. It
requires enough time for the full frozen role budget before starting it.

Optional `execution.resource_locks`, such as `["grist-account-a"]`, serialize
sessions sharing an account across distinct containers. They do not calculate a
provider's remaining quota. Quota/rate-limit observations still need inspection;
there is no blind registration retry or automatic account/region switching.
CLI controllers for the same pool share an OS lock. Use this one controller for
the pool: legacy batch/direct pipeline commands and controllers on other Macs do
not participate in that pool registry. Remote worker locks remain the final
container exclusion check.

### Entry check and closure reminder

A queued run config requires a `preflight` plan and an execution adapter command:

```json
{
  "preflight": [
    {"url": "https://api.example.com/auth", "method": "GET", "accepted_statuses": [401]}
  ],
  "execution": {
    "max_model_requests": 40,
    "closure_fraction": 0.85,
    "commands": {
      "preflight": ["python3", "/absolute/repo/scripts/runners/opencode/adapter.py", "--config", "/absolute/private/adapter.json", "preflight", "{request}"]
    }
  }
}
```

Merge these fields into the usual full role config. Select a documented, safe,
unauthenticated GET/HEAD target for the actual entry; no mutation, signup,
credentials, redirects or response bodies are collected. At most three targets
run inside the execution container, bounded to 18 seconds including DNS. An
accepted 401 proves only reachability of the authentication surface. A 403 is
ambiguous. Failed checks save a `preflight_blocked` operational hold and do not
start a model or create a service-failure score. Inspect the cause and submit a
new run/cohort rather than silently discarding a failed test.

At 85% of time or reserved request count, the proxy inserts a controller reminder
into the **next** model request to save deliverables and close. It preserves the
original task, does not create an extra model request, and cannot interrupt a
single already-running model call or long tool operation. The original hard
bounds remain. `wire/budget-warnings.jsonl` records actual delivery of the hint;
`controller-limits.json` records the effective bounds. Provision updated support
code into idle runtimes before using this protocol; the adapter rejects stale
runner hashes before allocating a run.

### Partial accounting and separate result facts

The normalizer scans each provider response independently. A failed or truncated
request no longer discards valid requests around it. `adapter_usage.py` verifies
raw-source hashes, request identities and numeric counters before exposing
`requests_verified` and `lower_bound_usage`. An interrupted total stays null;
model cost shows `lower_bound_usd` as “at least X; total unknown”. Complete means
remain unknown when a member lacks full cost/usage. Source tampering, duplicate
identities, unknown pricing or inconsistent partial counters establish no bound.
Receipt failures still preserve measured cost but cannot authorize grading or
publication. A confirmed budget stop is collected and passed to independent
grading when its receipt is valid; it is not automatically a service failure.

New graders must return evidence-backed `outcome` facets: `service_execution`,
`user_delivery`, `blocking_factors`, and `evidence`. The whole user-task verdict
continues to require the user's complete delivery. Network, access, model budget,
Agent execution, test protection, materials and service capability are distinct
possible blockers, not inferred from a single HTTP code. New protocol, request
bounds and runner support hashes participate in comparison grouping; wall-clock
receipt timestamps do not split otherwise identical repeats. Historical records
are unchanged.

Write tasks needing post-execution independent readback (such as Grist formula
recalculation) submit `"grading_gate": true`. Their executions are collected and
the comparison barrier seals normally, but no grader starts until the controller
has performed the predeclared verification and frozen its minimal data:

```sh
python3 scripts/task_queue.py release-grading /absolute/private/queue \
  --job JOB_ID --proofs /absolute/private/independent-readback
```

A comparison proof directory has one subdirectory per exact run ID; a single-run
proof directory directly contains that run's data. The release binds the original
execution, captured files and proof hashes; changed proof cannot dispatch a
grader. Data enters `grading-input/controller-verification/` and its packet index,
never the executor. This gate does not run readback scripts or supply a verdict.
The controller must use the frozen authorized mutations and independently
collected evidence, not execute an Agent's self-check. Other ready jobs keep
running while the gate waits. Expiry does not authorize extra verification
model calls. Account lock identities and physical container bindings apply
across admitted jobs; the pool must never use an executor container as a grader.
