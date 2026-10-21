# Preparing existing registry tasks continuously

`scripts/registered_task_producer.py` consumes controller-approved existing tasks without running a task designer. It calls the existing native `role_handoff` material-preparation role, validates its actual receipt, model, input, native turn and usage proof, then submits original task files/IDs to one existing queue. It does not change the registry, grading rules, frozen runs, worker source, credentials or publication status.

The producer can run from a new controller release with `--base-source-root` pointing at the unchanged release used by the active queue. Its private provenance records the new producer hash separately from all imported base-source hashes. The imported modules must actually come from that base directory; a mixed Python module process is rejected.

A private plan has this shape. Settings and paths are supplied by the controller, never the preparation model:

```json
{
  "schema_version": 1,
  "queue": "/private/queue",
  "deadline_epoch": 1900000000,
  "max_total_concurrency": 12,
  "max_preparation_concurrency": 2,
  "preparation_settings": ["/private/prep-01.json", "/private/prep-02.json"],
  "grading_settings": ["/private/grade-01.json", "/private/grade-02.json"],
  "backlog": ["/private/item-001.json"],
  "backlog_inbox": "/private/new-items"
}
```

Both preparation settings bind distinct physical Codex/Sol medium runtimes. The existing queue ceiling must be at most 10, leaving two preparation slots within the total of 12; deadline equality is mandatory. Preparation cannot share an executor or grader, including any existing frozen queue member. A queue-level owner record rejects a second producer directory. Each native preparation run gets a globally distinct basename, including when a worker is reused. Runtime source and policy drift block new allocation while collection and confirmed stopping remain available.

Each backlog JSON describes one original task and any approved routes/rounds:

```json
{
  "id": "registered-example-001",
  "task_file": "data/experiments/tasks/web-extraction.md",
  "task_id": "web-extraction-access-001",
  "task_sha256": "<exact select_task SHA256>",
  "rounds": [1, 2, 3],
  "targets": {
    "approved-route": {"config": "<full controller-owned config object>", "depends_on": []}
  },
  "material_ids": [],
  "materials": {},
  "generated_materials": {},
  "peer_policy": "posthoc_audit"
}
```

The `config` value above must be an object, with the original task file/ID, current `afs-20261013` access-readiness protocol, explicit roles/adapters, resource authorization, preflight and applicable access dependency. Intake validates every target and lane's existing bounded network-preflight schema and execution preflight command without making network calls. A missing or invalid controller setting is rejected before spending a preparation session. An optional `preparation_context` uses the existing `file`/`sha256` controller-context contract. Only its explicitly selected source facts enter the preparation packet; old assessments and solutions must not be selected. Normal raw materials use the existing `{path, sha256, audience, kind: "raw_data"}` registry, and generated raw schemas use the existing work-package CSV/JSON/TXT rules.

The preparer sees `task-design.json` explicitly labelled `source_kind: registered_task` and `role: registered_task`. It is a controller projection with the original task SHA and resources, **not** a native designer result or a designer collection proof. The existing preparation output contract keeps the field name `designer_sha256`, bound to these projection bytes. No design session is fabricated. Numeric execution/grading limits are projected separately, so a task referring to environment limits does not become held merely because private runner configurations were correctly excluded. Authorized public contact identity still needs explicitly selected controller context; full environment text and credentials are never copied automatically.

When only approved original material IDs are needed, the preparer is told to emit `materials: []`; the controller reattaches those exact original bytes. A schema-valid echoed original ID is also accepted only when its captured file/hash/size match the approved execution material. It cannot replace controller origin metadata, change bytes, promote a grading-only reference, or override an explicit nonsynthetic classification. New generated materials must use approved IDs, paths and record schemas. Renamed exact copies of private role/context/control inputs are rejected. Hash checks do not detect semantic rewriting; content review and role isolation remain necessary.

New access preparation takes priority over waiting business items, with stable ordering within each group. A business preparation starts only after its own access has a validated readiness decision for the same service, route, environment and physical executor. Pending access leaves the item `waiting_preparation_access` without a model call; a held access, including native access preparation held before a queue run exists, records a dependency hold instead of consuming a second preparation session. Neither condition is a service-task failure. A newly supplied context uses a new explicit item/condition; original held outputs are retained.

For a package with several targets, the eligible target subset is frozen into its native preparation input before the model starts. Unready siblings do not enter that packet or block ready targets. After selected targets are submitted, any omitted targets remain explicitly listed in `remaining_targets` and the item is `partial_submitted`, never fully completed. This bounded version does not automatically run another preparation attempt for omitted targets: they need a newly approved context/item with its own declared condition and proof. No collected assignment is deleted, relabelled or retroactively combined. Old packets without selection metadata keep their original full target set.

A collected preparation immediately releases its worker. Original free-only qualification and exact reference holds remain binding; a model-written `ready` or descriptive reference cannot clear them. Access is checked again before submission, so a changed or no-longer-ready prerequisite cannot authorize business work. The default `posthoc_audit` submits each slot as a standalone run, selects a physical idle/least-pending grader from the approved pool just before submission, and freezes that selection. Same task/round grouping remains in private dispatch metadata for later independent source/disagreement audit; no other grades enter a grader packet. Optional `comparison_barrier` retains the existing all-executions-first comparison behavior and its possible throughput delay.

Approved nonpooled execution lanes retain their original behavior and account/write locks. A controller can opt an explicitly anonymous read-only business target into a small execution pool:

```json
{
  "config": "<full original-task qualification/template config object>",
  "execution_pool_policy": {"mode": "readonly_anonymous", "max_active_per_target": 2},
  "execution_pool": [
    {"id": "lane-a", "config": "<full lane-a business config object>", "depends_on": ["lane-a-access-job"]},
    {"id": "lane-b", "config": "<full lane-b business config object>", "depends_on": ["lane-b-access-job"]}
  ]
}
```

All three `config` placeholders above are controller-owned objects, not strings in the actual input. The route must document `auth: none`, and the template and each lane must explicitly declare `service_credentials.provided: false`. The mode declaration is the controller's approval of the task's read-only scope; the producer does not infer that scope from prose. Each lane preserves the task, monetary authorization, independent reference bytes, preflight, model, harness, effort, time/request guards and all template resource locks. It must use a distinct physical executor, its own completed access prerequisite, and the corresponding frozen environment/runtime. A lane's access proof cannot be transferred to another runtime; the original pipeline checks that binding again before execution. Actual baseline/source readiness remains the responsibility of each native access result and the runtime adapter; simply listing a lane does not provision or validate a container.

Pool lanes must share the exact service/route `credential_scope` and `quota_endpoints`; this produces the same existing `route_cooldown` scope and does not multiply an anonymous IP quota. The existing binding requires `quota_resource_locks` to be a subset of that lane's `resource_locks`. For an approved anonymous read-only template without mutable account state, both can be empty: shared `credential_scope` still carries cooldowns, without serializing entire model sessions. The producer never removes a supplied account/write/resource lock. A shared lock may intentionally prevent parallel selection. Authenticated or write workloads must keep the existing single-lane path.

Immediately before submission, under the same queue gate, the producer chooses an actually idle approved lane. Unstarted queued work reserves it too; a known unconfirmed stop keeps it occupied. Completed execution releases its lane while its independent grader may still run. At most the declared one or two pending/active executions may share that quota family; when every eligible lane is busy, the slot remains `waiting_runtime` and the preparation worker is already free. A known family cooldown holds all pool lanes. No runtime is created, credential replaced or limit bypassed. The chosen lane/access/runtime/environment and grader are recorded before submission; an already compiled/submitted slot is never reassigned. After a crash between compilation and queue submission, the original frozen lane must again satisfy idle/cap/cooldown checks before submission; the controller waits without rebinding it. An already submitted job retains idempotent recovery and does not count itself as a new allocation. Pool mode uses `posthoc_audit`, retaining immediate standalone grading and later cross-source auditing. The original single-lane and explicit comparison-barrier paths are unchanged.


```sh
python3 /new-release/scripts/registered_task_producer.py init /private/producer \
  --plan /private/plan.json --base-source-root /unchanged-base-release
python3 /new-release/scripts/registered_task_producer.py run /private/producer --once
python3 /new-release/scripts/registered_task_producer.py run /private/producer
python3 /new-release/scripts/registered_task_producer.py status /private/producer
python3 /new-release/scripts/registered_task_producer.py halt /private/producer
```

Use `enqueue DIRECTORY --entry FILE` or atomically append a new controller JSON file to `backlog_inbox` while the daemon runs. Invalid intake is recorded privately. Exhausted or access-blocked backlog reports `no_ready_work` with individual item states instead of claiming model activity. The daemon continues polling until halted or the absolute deadline. Unknown starts are stopped using their durable predicted handle, never blindly resent; an unconfirmed stop keeps its preparation slot reserved. Halting preserves already-submitted work and does not halt the independent service queue. Deployment needs an external supervisor/finalizer to stop both controllers and verify owned model processes. Offline adapter fixtures do not establish a successful live cloud deployment.
