# GitHub — real-http rep 2 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Successfully created and verified the issue.

Task complete: created issue #17 (id 4835590416) titled "afs-github-http-r2-mrbssi28" in Olorinm/afs-task-sandbox via the GitHub REST API, then read it back with a GET request confirming title, body, and metadata match.

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/17","final_command":"curl -s -K /srv/claude-code/workspace/.afs/credentials/github.curlrc -H \"Accept: application/vnd.github+json\" -H \"X-GitHub-Api-Version: 2022-11-28\" \"https://api.github.com/repos/Olorinm/afs-task-sandbox/issues/17\"","wrong_attempts":1,"friction_notes":["First curl POST used -o /tmp/... to save the response; curl exit code 23 because /tmp is outside the sandbox's allowed working directories, even though HTTP 201 succeeded — had to switch to printing response to stdout instead of writing files outside /srv/claude-code/workspace","WebFetch summarization of the API-versions doc returned a future-dated version string '2026-03-10' alongside the expected '2022-11-28' default; used the well-established default '2022-11-28' to avoid relying on a suspicious/unverifiable value"],"docs_pages_used":["https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue","https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#get-an-issue","https://docs.github.com/en/rest/about-the-rest-api/api-versions"],"confidence":"high"}
```
