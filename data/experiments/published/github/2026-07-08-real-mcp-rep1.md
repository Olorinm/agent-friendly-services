# GitHub — real-mcp rep 1 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Successfully created and verified the issue.

- **Issue #10**: "afs-github-mcp-r1-mrbsoht1" in `Olorinm/afs-task-sandbox`
- **id**: 4835566490, **number**: 10
- **URL**: https://github.com/Olorinm/afs-task-sandbox/issues/10
- **State**: open, confirmed via readback with matching title and body.

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/10","final_command":"mcp__github__issue_read(method=\"get\", owner=\"Olorinm\", repo=\"afs-task-sandbox\", issue_number=10)","wrong_attempts":0,"friction_notes":["issue_write's create response returns an internal numeric 'id' (4835566490) distinct from the human-facing issue 'number' (10); had to read back to confirm the issue number used in the URL matches"],"docs_pages_used":["https://docs.github.com/rest"],"confidence":"high"}
```
