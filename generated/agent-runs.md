<!-- GENERATED FILE — do not edit. Run `npm run generate`. Source of truth: data/experiments/published/ -->

# Agent Runs

Real AI agents executing each category's [pinned realistic task](../data/experiments/tasks/) against the live service — unattended, in a pinned clean environment, with the runner (not the agent) verifying the result through the provider's API. Method, environment and hard rules: [agent-verification.md](../docs/agent-verification.md).

Every run publishes its model, date, metrics and full transcript. Results expire after 180 days. Providers can dispute any run by opening an issue — we rerun under the same pinned conditions.

## Route comparison

The same task, over each way an agent can reach the provider (**http** = official docs + raw API calls, the universal baseline · **cli** = the provider's official CLI · **mcp** = the provider's official MCP server). The route-vs-baseline delta shows whether a provider's agent tooling actually pays off. 🏆 = best measured result in its category (majority-pass on the baseline route, fewest median turns) — it changes hands automatically whenever a better run lands.

| Provider | http (baseline) | cli | mcp |
| --- | --- | --- | --- |
| [GitHub](#github) 🏆 (Developer Tools) | ✓ 3/3 · 8t · $0.19–0.33 | ✓ 3/3 · 5t · $0.09–0.11 | ✓ 3/3 · 4t · $0.14–0.15 |

Cell format: verdict · passes/reps · median turns · cost per run.

## Runs by provider

### GitHub <a id="github"></a>

Task: `file-issue-and-confirm` ([definition](../data/experiments/tasks/developer-tools.yaml)) · [provider facts](./providers.md#github)

| Layer · route | Verdict | Median turns | Wall time | Cost/run | Model | Date | Transcripts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| real · http | 3/3 pass | 8 | 39–85 s | $0.19–$0.33 | sonnet | 2026-07-08 | [1](../data/experiments/published/github/2026-07-08-real-http-rep1.md) [2](../data/experiments/published/github/2026-07-08-real-http-rep2.md) [3](../data/experiments/published/github/2026-07-08-real-http-rep3.md) |
| real · cli | 3/3 pass | 5 | 16–19 s | $0.09–$0.11 | sonnet | 2026-07-08 | [1](../data/experiments/published/github/2026-07-08-real-cli-rep1.md) [2](../data/experiments/published/github/2026-07-08-real-cli-rep2.md) [3](../data/experiments/published/github/2026-07-08-real-cli-rep3.md) |
| real · mcp | 3/3 pass | 4 | 15–22 s | $0.14–$0.15 | sonnet | 2026-07-08 | [1](../data/experiments/published/github/2026-07-08-real-mcp-rep1.md) [2](../data/experiments/published/github/2026-07-08-real-mcp-rep2.md) [3](../data/experiments/published/github/2026-07-08-real-mcp-rep3.md) |

**Run notes** (agent-reported, verbatim):

- *(http rep1)* WebFetch's summarizer model returned X-GitHub-Api-Version: 2026-03-10 for the create-issue header (matching the sandbox's current date rather than GitHub's actual pinned version) — cross-checked against the apiVersion=2022-11-28 query param in the fetched doc URL itself and used the correct real value instead; this is a harness/model artifact, not a GitHub docs error
- *(http rep1)* sandboxed Bash blocked a piped curl|grep as a 'multiple operations' command requiring separate approval — worked around by running curl alone and reading full JSON output
- *(http rep2)* First curl POST used -o /tmp/... to save the response; curl exit code 23 because /tmp is outside the sandbox's allowed working directories, even though HTTP 201 succeeded — had to switch to printing response to stdout instead of writing files outside /srv/claude-code/workspace
- *(http rep2)* WebFetch summarization of the API-versions doc returned a future-dated version string '2026-03-10' alongside the expected '2022-11-28' default; used the well-established default '2022-11-28' to avoid relying on a suspicious/unverifiable value
- *(http rep3)* Docs page for creating an issue listed X-GitHub-Api-Version: 2026-03-10 as an example header, which looked anomalous (future-dated); cross-checked the API-versions page and confirmed 2022-11-28 is still the supported/default version, so used that instead to avoid guessing.
- *(cli rep2)* gh auth status showed two logged-in accounts for github.com (env GH_TOKEN and stored hosts.yml), but both resolved to the same Olorinm account so no ambiguity in practice
- *(mcp rep1)* issue_write's create response returns an internal numeric 'id' (4835566490) distinct from the human-facing issue 'number' (10); had to read back to confirm the issue number used in the URL matches
- *(mcp rep2)* issue_write returns only id and url (no issue number) on create, so the number had to be parsed from the returned URL to use in the subsequent issue_read call
- *(mcp rep3)* issue_write returns a decimal 'id' (global GitHub node/issue id, 4835571491) distinct from the issue 'number' (12) used for read-back and URL; no ambiguity encountered, just noting the two identifiers differ
