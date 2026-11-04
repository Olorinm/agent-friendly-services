# Private cloud role work packages

`scripts/work_package.py` connects independently collected task-design and material-preparation output to the existing task queue. It validates and submits work, without starting model sessions or changing credentials, runners or the service catalog.

Both role outputs use `schema_version: 1`, a controller-assigned `package_id`, `status` (`ready` or `held`) and `blockers`. Held work needs a concrete reason; ready work cannot contain unresolved blockers. The preparer binds the exact designer JSON bytes with `designer_sha256`.

Each new role input includes `output-schema.json`, generated from `scripts/role_contract.py`, which also checks the consumer's accepted field names and types. The schema is part of the frozen input membership and hashes. Unknown fields remain rejected with a JSON location such as `$.assignments[0].task_version`; blockers are string arrays. Descriptive metadata such as each material's `source`/`validation` and the preparer's `resource_prerequisites`/`frozen_dates` may retain structured JSON and real unknown values. Validation notes belong inside material entries, not a new top-level `validation` field. No ready state is inferred from format compliance.

The designer declares `tasks` with `id`, `version`, `description`, `inputs`, `expected_output`, `success`, `failure`, `material_ids` and `applicable_target_ids`. Optional demand sources, applicability notes and synthetic `material_requirements` remain private preparation evidence. The preparer lists every declared task/target/round in `assignments`, marking each ready or held, and records generated files in `materials` with `id`, `file` and the actual `sha256`. Files must be under `materials/`; only controller-approved CSV, JSON and TXT record schemas are accepted.

The controller supplies a separate private policy:

- `rounds`: distinct positive trial numbers.
- `max_tasks`: optional positive integer limiting the number of designer task entries in one package. Booleans, zero and other types are rejected. Exceeding the cap is rejected before task files are written or queue submission begins. Omit it to retain the existing uncapped behavior; an empty explicitly held design remains allowed. A one-business-task pilot sets `max_tasks: 1`; approved `targets` and `rounds` separately bound services and repetitions.
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

Each role-settings file supplies the explicit model, reasoning effort, harness version/mode, runtime, seconds, account billing, deadline and all four official adapter commands. The design input contains `AGENTS.md`, `prompt.txt` and the assigned demand/service brief; no prior answers are included. The runtime policy and credentials are not passed to the model. The preparer's boundary contains approved IDs, rounds, raw material schemas and a whitelist projection of the assigned catalog entry/docs, resource authorization and matching service/route fee qualification. The original reference file is hashed before design, but its answers, assessments, other services and prior review conclusions are not passed through. These preparation facts do not prove current availability, business completion or actual service charges.

A package may also specify `preparation_context: {"file": "/absolute/private/context.json", "sha256": "<exact bytes>"}`. This is an explicit controller selection, not a new approval role. The context uses `schema_version: 1`, `targets` and `evidence`. Each target key must match an approved policy target and contains exactly `service`, `route`, and `observations`. Each observation contains `topic`, `status` (`confirmed`, `unknown`, `held`), `statement` and `evidence_ids`. Each evidence entry contains `id`, relative `file`, exact `sha256`, descriptive `source`, `purpose` and `kind` (`official_documentation`, `capability_metadata`, `sealed_baseline`, `resource_observation`, or `synthetic_description`). Sources can be official URLs or an explicit local/synthetic explanation.

The controller must select only relevant original preparation evidence and review it for credentials, commands/solutions, old answers, assessments and other verdicts before declaring this context. Its contents are evidence, never executable instructions or authority to override a hold. Context bytes and each selected file are frozen and checked before role dispatch; links and paths outside the context directory are rejected. Only selected files reach the preparer under derived `controller-context/` paths, indexed by `controller-context.json`. Unlisted files, full configurations and old records are not copied. Context never becomes an execution attachment automatically: the existing compiler continues to accept only the approved raw materials registry. Hashes establish provenance and immutability, not the factual correctness of a controller claim.

Context source paths must be canonical absolute paths without a symlink at the file or any ancestor directory. The native role collection proof records `private_input_files` for known role/control inputs, schemas, boundary files and the explicit `controller-context/` evidence. The compiler derives protected hashes from both verified role manifests and formal role/control JSON files. A newly generated material that is a byte-identical renamed copy of these sources is rejected even if its CSV/JSON/TXT schema is otherwise valid. This does not classify every input or artifact as private: ordinary original data and the controller's explicit approved raw-material registry retain their existing semantics. Hash matching cannot detect rewritten instructions or semantic answer leakage; controller/role content review remains necessary.

The safe admission projection is deliberately not a complete hold or review view. It does not transmit old hold reasons or assessments. The existing downstream admission check still reads the original frozen reference and enforces its exact service/route hard holds before actual execution; the new preparation context does not waive that gate.

```sh
python3 scripts/role_producer.py init /absolute/private/producer --plan /absolute/private/producer-plan.json
python3 scripts/role_producer.py run /absolute/private/producer
python3 scripts/task_queue.py run /absolute/private/queue
```

The concurrency envelope reserves space for preparation as well as the service queue: the sum of both configured ceilings cannot exceed the total. Parallel preparation packages require distinct physical preparation runtimes, and none may share an executor or grader container. Low storage pauses every new role allocation, including the transition from design to preparation. Active collection and confirmed stopping remain available. A failed role affects its own handle; an unconfirmed stop remains visible and reserves capacity until reconciled.

Use an external supervisor with the same deadline and an independent container-stop check for deployment. Stop the producer and queue separately before refreshing any runtime source. A producer reaching `finished` means its packages have been submitted or held; it does not mean the service executions and independent grading have drained. Source/fixture validation does not establish a successful live cloud deployment.
