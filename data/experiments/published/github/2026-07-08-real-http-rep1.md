# GitHub — real-http rep 1 (2026-07-08)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

Confirmed via read-back: issue #16, id `4835583243`, title matches exactly, state open, at https://github.com/Olorinm/afs-task-sandbox/issues/16.

```json
{"result":"pass","resource_id":"https://github.com/Olorinm/afs-task-sandbox/issues/16","final_command":"curl -s -K /srv/claude-code/workspace/.afs/credentials/github.curlrc -X POST https://api.github.com/repos/Olorinm/afs-task-sandbox/issues -H \"Accept: application/vnd.github+json\" -H \"X-GitHub-Api-Version: 2022-11-28\" -d '{\"title\":\"afs-github-http-r1-mrbsrg6j\",\"body\":\"Filed autonomously by an AI agent as part of an agent-friendly-services verification task.\"}'","wrong_attempts":0,"friction_notes":["WebFetch's summarizer model returned X-GitHub-Api-Version: 2026-03-10 for the create-issue header (matching the sandbox's current date rather than GitHub's actual pinned version) — cross-checked against the apiVersion=2022-11-28 query param in the fetched doc URL itself and used the correct real value instead; this is a harness/model artifact, not a GitHub docs error","sandboxed Bash blocked a piped curl|grep as a 'multiple operations' command requiring separate approval — worked around by running curl alone and reading full JSON output"],"docs_pages_used":["https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue","https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#get-an-issue"],"confidence":"high"}
```
