# GitHub — real-mcp rep 3 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Confirmed: issue #12 exists with title "afs-github-mcp-r3-mrbspjoj", state open, at https://github.com/Olorinm/afs-task-sandbox/issues/12.

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/12","final_command":"mcp__github__issue_read(method=get, owner=Olorinm, repo=afs-task-sandbox, issue_number=12)","wrong_attempts":0,"friction_notes":["issue_write returns a decimal 'id' (global GitHub node/issue id, 4835571491) distinct from the issue 'number' (12) used for read-back and URL; no ambiguity encountered, just noting the two identifiers differ"],"docs_pages_used":["https://docs.github.com/rest"],"confidence":"high"}
```
