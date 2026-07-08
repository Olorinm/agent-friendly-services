# GitHub — real-cli rep 2 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Read-back confirms: title matches exactly, body present, issue is open at the expected URL.

- **Issue ID (node id):** `I_kwDOTRPxZ88AAAABIDkK2g`
- **Issue number:** 14
- **URL:** https://github.com/Olorinm/afs-task-sandbox/issues/14

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/14","final_command":"gh issue view 14 --repo Olorinm/afs-task-sandbox --json id,number,title,body,url,state,author","wrong_attempts":0,"friction_notes":["gh auth status showed two logged-in accounts for github.com (env GH_TOKEN and stored hosts.yml), but both resolved to the same Olorinm account so no ambiguity in practice"],"docs_pages_used":["https://cli.github.com"],"confidence":"high"}
```
