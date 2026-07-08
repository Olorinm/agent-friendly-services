# GitHub — real-mcp rep 2 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Task complete. Created and verified issue #11 in Olorinm/afs-task-sandbox.

- **id**: 4835569346 (issue number 11)
- **URL**: https://github.com/Olorinm/afs-task-sandbox/issues/11
- **title**: "afs-github-mcp-r2-mrbsp1em" (exact match)
- **state**: open, confirmed via read-back

```json
{"result":"pass","resource_id":"4835569346 (Olorinm/afs-task-sandbox#11) / https://github.com/Olorinm/afs-task-sandbox/issues/11","final_command":"mcp__github__issue_read(method=get, owner=Olorinm, repo=afs-task-sandbox, issue_number=11)","wrong_attempts":0,"friction_notes":["issue_write returns only id and url (no issue number) on create, so the number had to be parsed from the returned URL to use in the subsequent issue_read call"],"docs_pages_used":["https://docs.github.com/rest"],"confidence":"high"}
```
