# GitHub — real-http rep 3 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Confirmed. The issue was created and read back successfully:

- **Number:** 18
- **id:** 4835599798
- **URL:** https://github.com/Olorinm/afs-task-sandbox/issues/18
- **Title:** afs-github-http-r3-mrbsufu1 (exact match)
- **Body:** "Filed autonomously by an AI agent as part of a standardized verification task."

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/18","final_command":"curl -sS -K /srv/claude-code/workspace/.afs/credentials/github.curlrc -H \"Accept: application/vnd.github+json\" -H \"X-GitHub-Api-Version: 2022-11-28\" https://api.github.com/repos/Olorinm/afs-task-sandbox/issues/18","wrong_attempts":0,"friction_notes":["Docs page for creating an issue listed X-GitHub-Api-Version: 2026-03-10 as an example header, which looked anomalous (future-dated); cross-checked the API-versions page and confirmed 2022-11-28 is still the supported/default version, so used that instead to avoid guessing."],"docs_pages_used":["https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue","https://docs.github.com/en/rest/about-the-rest-api/api-versions"],"confidence":"high"}
```
