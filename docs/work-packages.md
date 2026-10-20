# Private cloud role work packages

`scripts/work_package.py` connects independently collected task-design and material-preparation output to the existing task queue. It validates and submits work, without starting model sessions or changing credentials, runners or the service catalog.

Both role outputs use `schema_version: 1`, a controller-assigned `package_id`, `status` (`ready` or `held`) and `blockers`. Held work needs a concrete reason; ready work cannot contain unresolved blockers. The preparer binds the exact designer JSON bytes with `designer_sha256`.

The designer declares `tasks` with `id`, `version`, `description`, `inputs`, `expected_output`, `success`, `failure`, `material_ids` and `applicable_target_ids`. Optional demand sources, applicability notes and synthetic `material_requirements` remain private preparation evidence. The preparer lists every declared task/target/round in `assignments`, marking each ready or held, and records generated files in `materials` with `id`, `file` and the actual `sha256`. Files must be under `materials/`; only controller-approved CSV, JSON and TXT record schemas are accepted.

The controller supplies a separate private policy:

- `rounds`: distinct positive trial numbers.
- `targets`: approved target IDs mapped to complete controller-owned `config` templates, optional queue `depends_on` IDs and `grading_gate`.
- `materials`: optional previously approved raw-data IDs with absolute controller paths, nonempty SHA256, `kind: raw_data` and a fixed `audience`.
- `generated_materials`: allowed material IDs with exact relative `file`, `format`, size/row bounds and record `columns`. String fields require an explicit pattern; TXT requires a data-line pattern. The model cannot add executable formats or answer columns.
- `designer_collection` and `preparer_collection`: actual collected output `directory`, `receipt_sha256` and `proof_sha256` for `role-collection-proof.json` produced by the formal role controller.

Collection verification binds the formal role manifest, source files, actual captured JSON, receipt and native completed turn. The native rollout must show the frozen prompt, model and reasoning effort; per-request usage must be verified against the native source. An `exit_code: 0`, a model-written `ready`, or an operator claim alone cannot authorize submission. Designer and preparer must have distinct sessions.

Generated task Markdown stays in the ignored private results tree. The compiler derives all task paths, attachment locations, run IDs and specs; the model supplies no shell commands, budgets, runtime settings, credentials or absolute paths. Only approved original material bytes enter execution attachments. Criteria, sources, preparation notes and independently collected references remain in task/grading inputs. References are evidence for the grader to check, not a replacement verdict.

```sh
python3 scripts/work_package.py \
  --queue /absolute/private/queue \
  --designer /absolute/collected-design/task-design.json \
  --preparer /absolute/collected-preparation/material-preparation.json \
  --policy /absolute/private/controller-policy.json \
  --output /absolute/private/compiled-package
```

Successful repeated submission with identical role sources reuses the same immutable handoffs. Changed sources, compiled bytes, unsupported targets, duplicate slots, links, path traversal, mismatched hashes or a changed queued identity are rejected. Partial failures remain inspectable; they are not permission to overwrite uncertain work. A held assignment is retained without creating a trial or recording service failure.

Account-billed grading supports explicitly frozen `gpt-6.1-sol` medium or high effort. The queue preserves that exact setting in its handoff; it does not silently upgrade or downgrade effort. Execution remains separate from the grader container. ChatGPT account usage stays private and unknown in dollars and is not a zero-dollar service or a DeepSeek API charge.

## Continuous cloud preparation

`role_handoff.py` owns one fresh task-design or material-preparation session through the formal Codex adapter. It freezes input membership and bytes, runtime settings and controller source hashes. A durable predicted handle is written before start; a missing start response never causes an automatic second start. Collection checks the native completed turn, full input, actual model/effort, captured output, original input snapshot and native request usage before writing a private `role-collection-proof.json`. A zero exit code alone is insufficient.

`role_producer.py` connects these sessions. After a verified designer completes, it automatically creates the preparer's packet from that exact design and the public portion of the controller's approved material and target policy. After verified preparation, it binds both collection proofs and calls the package compiler. The service queue runs in its own process and can consume submitted work while other packages are still being designed or prepared. Submitted/held packages retain their sources and reasons; the producer neither grades business results nor publishes evidence.

A controller-owned producer plan contains:

- `schema_version: 1`, `queue` (an existing private queue), `deadline_epoch`, `max_total_concurrency` and `max_preparation_concurrency`.
- `packages`, each with a unique approved `id`, an absolute `design_input` directory, `design_settings` and `preparation_settings` files, and the private work-package `policy` file described above.

Each role-settings file supplies the explicit model, reasoning effort, harness version/mode, runtime, seconds, account billing, deadline and all four official adapter commands. The design input contains `AGENTS.md`, `prompt.txt` and the assigned demand/service brief; no prior answers are included. The runtime policy and credentials are not passed to the model. Only approved target IDs, service/route names, round numbers and raw material schemas enter the preparer's boundary file.

```sh
python3 scripts/role_producer.py init /absolute/private/producer --plan /absolute/private/producer-plan.json
python3 scripts/role_producer.py run /absolute/private/producer
python3 scripts/task_queue.py run /absolute/private/queue
```

The concurrency envelope reserves space for preparation as well as the service queue: the sum of both configured ceilings cannot exceed the total. Parallel preparation packages require distinct physical preparation runtimes, and none may share an executor or grader container. Low storage pauses every new role allocation, including the transition from design to preparation. Active collection and confirmed stopping remain available. A failed role affects its own handle; an unconfirmed stop remains visible and reserves capacity until reconciled.

Use an external supervisor with the same deadline and an independent container-stop check for deployment. Stop the producer and queue separately before refreshing any runtime source. A producer reaching `finished` means its packages have been submitted or held; it does not mean the service executions and independent grading have drained. Source/fixture validation does not establish a successful live cloud deployment.
