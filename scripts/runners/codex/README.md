# Independent cloud Codex grading

This adapter runs **Codex CLI 0.162.0 / `gpt-6.1-sol` / high** in a dedicated
Docker grader. Execution can continue with OpenCode and DeepSeek: the two roles
have separate model, harness, runtime and usage records. Changing the grader
creates a new trial protocol; it does not rewrite historical assessments.

The grader receives only the frozen grading packet: the task and role instructions,
execution evidence, optional reference and frozen peer answers. It receives no
executor service credentials, other grading conclusions or repository instructions.
Every assessment uses a fresh home, session and workspace. Previous user files
are archived in a root-only directory; the model runs as uid 1000. The container
has resource limits, no published ports, host mounts or Docker socket.

## Private setup

Use the same SSH or local transport as the OpenCode adapter. Select the ChatGPT
login explicitly, following [Codex headless authentication](https://learn.chatgpt.com/docs/auth).
The selected account must have access to Sol/high. This adapter refuses API-key
fallback. Never put the login file, connection settings or raw rollouts in Git.

Example private adapter configuration (replace the placeholders):

```json
{
  "host": "benchmark-host",
  "remote_root": "/absolute/private/codex-runtime",
  "image": "afs-codex-grader:0.162.0",
  "billing_mode": "chatgpt",
  "auth_file": "/absolute/private/selected-codex-auth.json",
  "containers": { "sol-grader-01": "sol-grader-01" },
  "retained_paths": { "sol-grader-01": [] },
  "memory": "2g",
  "cpus": 1,
  "pids_limit": 256
}
```

`auth_file` is read on the machine running `provision.py`. A resident cloud
controller uses `"transport": "local", "host": "localhost"` and absolute paths
on that host. Upload only the selected private login, not the operator's entire
Codex home or configuration. Keep private directories at 0700 and files at 0600.

```sh
python3 scripts/runners/codex/provision.py --config /absolute/private/adapter.json build
python3 scripts/runners/codex/provision.py --config /absolute/private/adapter.json up
python3 scripts/runners/codex/configure-grading.py \
  --source /absolute/private/deepseek-trial.json \
  --adapter /absolute/private/adapter.json --runtime sol-grader-01 \
  --output /absolute/private/new-sol-trial.json
```

The helper preserves execution settings and replaces only the grader and trial
protocol. It refuses to overwrite a config. The existing pipeline or continuous
queue then consumes the new config normally. Each logical runtime maps to its
own container; the queue includes these graders in total session concurrency
and physical runtime exclusion. Provisioning does not start model calls.

The default grading deadline is 600 seconds. Absolute queue deadlines also apply;
the worker terminates its own model process group if the controller disappears.
CLI output-limit and request-count enforcement are not implemented and are not
claimed. An interrupted start is not automatically repeated. Source hashes and
the actual Docker image are checked before dispatch. Refresh source or login only
after reconciling and stopping the owned container:

```sh
python3 scripts/runners/codex/provision.py --config /absolute/private/adapter.json stop
python3 scripts/runners/codex/provision.py --config /absolute/private/adapter.json up
```

Authentication is provisioned from the selected private login for fresh sessions.
Expired/revoked login or account limits remain operational errors requiring login
refresh or inspection; they are not a service failure or a reason to rerun blindly.

## Receipts and accounting

The worker includes the entire frozen grading role in the prompt, disables user
config, repository rules, skills, apps and memories, and checks the private rollout
for the full prompt and actual Sol/high turn context. Collection retains the CLI
events, raw rollout, assessment, process receipt and numeric per-request usage.
Only evidence explicitly selected and checked for disclosure is published.

Usage must reconcile with the CLI final total and retain source hashes. Missing
totals remain incomplete, with validated observed requests available as a lower
bound. Ambiguous or adjusted counters do not establish that bound. Artifact and
rollout reads use the model user's privileges; collection never follows artifact
links into controller credentials.

ChatGPT account credits and allocated subscription cost are **unknown, not $0**.
This adapter's queue reservation is zero *DeepSeek API dollars* because it uses
the selected ChatGPT login. That is not a claim that grading is free. Account
usage is tracked separately from the DeepSeek API ledger; any frozen API-rate
estimate is labeled separately and does not represent credits or a provider bill.
Concurrency and time controls still apply.

New public records can include the observed grader model, reasoning effort,
harness, timestamps and billing mode under `review.runtime`, independently of
the execution model. Session IDs, auth and private runtime paths stay private.
