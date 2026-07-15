# paas.build — dry-fire rep 2 (2026-07-15)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

## Findings

**Provider:** paas.build (PayFac powered by UniPaaS, FCA-authorised Payment Institution No. 929994).

**Documented API surface** (from `https://paas.build/SKILL.md` / `https://paas.build/llms-full.txt`, cross-checked against `https://paas.build/agents` and `https://paas.build/llms.txt`) — only three direct REST endpoints exist, all `POST`, base URL `https://paas.build/api`:

1. `POST /api/identify` — optional, **no credential required**.
2. `POST /api/go-live` — creates a **REAL** merchant account ("Progressive KYB: the account is live immediately, capped ~£1,500 until verification completes") and *issues* the credential (`vendorId`/`accessToken`). This is a signup/account-creation call, out of bounds under the hard rules — I did not call it.
3. `POST /api/checkout` — the only endpoint that *consumes* a credential (`vendorId`, scoped access token per docs), body: `{"vendorId":"<id>","amount":...,"currency":...,"description":...,"env":"sandbox"}`.

There is no listed GET/list-style read anywhere in official docs — this is a payments platform, not a resource-listing API. So the canonical "first authenticated call obtainable without signing up" is `/api/checkout` with a fabricated `vendorId`.

**Execution and contrast tests** (to isolate endpoint/shape correctness from auth rejection):

| Call | Result |
|---|---|
| `POST /api/identify` (public, no auth) | `200` + documented JSON shape — confirms routing/connectivity is fine |
| `POST /api/checkout` with fake `vendorId` (full valid shape) | `502`, body `{"error":"checkout failed","status":401,"raw":{"statusCode":401,"message":"Unauthorized","code":401}}` — repeated twice, identical |
| `POST /api/checkout` with empty body `{}` | `400`, body `{"error":"vendorId and amount required"}` — proves field-presence validation is real, and our fake-credential request passed it |
| `POST /api/checkout-nonexistent` | `404`, body `{"error":"not found"}` — proves a wrong path looks distinctly different |

The contrast tests confirm endpoint, method, headers, and request body shape are all correct for `/api/checkout`: a missing-field request gets a different (400) shape, a wrong path gets 404, and our full fake-credential request reaches backend auth logic that rejects it with an embedded `401 Unauthorized`. However, the **outer transport-level HTTP status is 502**, not 401/403 — paas.build's gateway (Render + Cloudflare) appears to re-wrap upstream (UniPaaS) non-2xx auth rejections as an outer 502 rather than propagating 401/403 directly. This is undocumented behavior and, per the task's literal PASS bar (401/403 top-level status required), this scores as a **fail** — despite strong circumstantial evidence the request itself is correctly formed. Worth flagging: this quirk would cause naive client code that checks `status < 500` to misclassify a permanent auth failure as a transient server error and retry.

**Human gates** (from official docs, no guessing beyond what's stated):
- Providing real business identity/email/region to `/api/go-live` (fabricated data isn't permitted under this task's hard rules, and the account is immediately "REAL" per docs) — evidence: `https://paas.build/SKILL.md`.
- Completing the background KYB verification to lift the ~£1,500 progressive cap — mechanism not specified in official docs (unknown).

```json
{"result":"fail","http_status":502,"final_command":"curl -sS -i -X POST https://paas.build/api/checkout -H \"Content-Type: application/json\" -d '{\"vendorId\":\"sk-agent-pilot-dummy-vendor-id-0000\",\"amount\":12,\"currency\":\"GBP\",\"description\":\"dry-fire verification probe\",\"env\":\"sandbox\"}'","error_body_excerpt":"{\"error\":\"checkout failed\",\"status\":401,\"raw\":{\"statusCode\":401,\"message\":\"Unauthorized\",\"code\":401}}","wrong_attempts":0,"friction_notes":["No REST 'list/read' endpoint exists at all — paas.build only exposes 3 POST endpoints (identify, go-live, checkout); go-live is itself account creation/signup so it's off-limits for this test, leaving checkout as the only crediential-consuming call.","Official docs (SKILL.md, llms-full.txt, /agents, llms.txt) never document an error-response shape or status code for invalid credentials, so there is no documented 401/403 shape to match against.","Auth rejection for an invalid vendorId is returned as an outer HTTP 502 with the real 401/Unauthorized only visible embedded in the JSON body ({\"status\":401,\"raw\":{...}}) — this is inconsistent with REST convention and would cause naive retry-on-5xx client logic to misclassify a permanent auth failure as transient.","Confirmed via contrast tests that endpoint/method/headers/body-shape are correct: empty body gives a distinct 400 'vendorId and amount required', and a wrong path gives a clean 404 'not found', so the 502+embedded-401 on the fake vendorId is a genuine, repeatable auth rejection and not a routing failure.","MCP server README (raw.githubusercontent.com/UNIPaaS/paas-build-mcp) contains no curl/header examples beyond what's in SKILL.md; no Authorization header format is documented anywhere for the direct /api/checkout call, only the vendorId in the JSON body."],"human_gates":[{"step":"Provide real business name, email, region and website to POST /api/go-live to create the actual (immediately-live) merchant account — cannot be faked, and is out of scope for this dry-fire test under the no-signup rule","evidence":"https://paas.build/SKILL.md"},{"step":"Complete background KYB verification to lift the ~£1,500 progressive cap on the newly created account (exact mechanism/steps not specified in official docs)","evidence":"https://paas.build/SKILL.md"}],"confidence":"medium"}
```
