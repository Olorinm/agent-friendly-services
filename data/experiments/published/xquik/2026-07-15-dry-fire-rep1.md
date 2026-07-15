# Xquik — dry-fire rep 1 (2026-07-15)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

The endpoint returned exactly the documented authentication-failure shape. Summary:

**Canonical first call**: `GET https://xquik.com/api/v1/account` with header `x-api-key: xq_...` — this is explicitly given as a worked curl example on the API reference overview page (https://docs.xquik.com/api-reference/overview), described as ideal "for verifying API key functionality."

**Result**: HTTP 401, JSON body `{"error":"unauthenticated","message":"Authentication required. Provide a valid API key or bearer token."}`. This matches the documented error code `"unauthenticated"` and the documented `{error, message}` shape from https://docs.xquik.com/guides/error-handling (which also lists this exact code for missing/invalid API keys), and the `www-authenticate: Bearer realm="xquik"` header confirms it's a real auth-layer rejection from the correct route (Cloudflare-fronted, JSON content-type, not an HTML/404 page).

**Human gates for a real credential**:
1. Create an Xquik account — https://dashboard.xquik.com/signup
2. Select/confirm a plan (some scopes may require billing) — https://xquik.com/pricing
3. Authenticate into the dashboard (session/OAuth), then generate an API key — https://docs.xquik.com/api-reference/api-keys/create
4. (If using the credential-less "Guest API Key" `paid_reads` tier instead) complete Stripe verification — noted in https://docs.xquik.com/llms.txt, no dedicated doc page found for this flow beyond that mention

```json
{"result":"pass","http_status":401,"final_command":"curl -s -i https://xquik.com/api/v1/account -H \"x-api-key: xq_agent0000000000000000000000000000000000000000000000000000dead\"","error_body_excerpt":"{\"error\":\"unauthenticated\",\"message\":\"Authentication required. Provide a valid API key or bearer token.\"}","wrong_attempts":0,"friction_notes":["llms.txt labeled GET /api-keys as the 'simplest authenticated read' but noted it requires session/cookie auth, not the x-api-key scheme used elsewhere — used GET /account (explicit curl example on api-reference/overview) instead, which is API-key-authenticated","api-reference/api-keys/create page documents only the POST-to-create flow with no worked GET example; had to cross-reference api-reference/overview for the actual request shape","error-handling guide's sample message text for 'unauthenticated' differs slightly in wording from the live response, but the error code and JSON field shape matched exactly"],"human_gates":[{"step":"Create Xquik account","evidence":"https://dashboard.xquik.com/signup"},{"step":"Select a plan (billing may gate higher scopes)","evidence":"https://xquik.com/pricing"},{"step":"Log into dashboard and generate an API key (xq_ prefixed)","evidence":"https://docs.xquik.com/api-reference/api-keys/create"}],"confidence":"high"}
```
