# Xquik — dry-fire rep 2 (2026-07-15)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

## Summary

**Endpoint discovery:** Both `https://docs.xquik.com` and `https://docs.xquik.com/api-reference/overview` independently point to the same canonical first call: `GET https://xquik.com/api/v1/account` authenticated via `x-api-key: xq_...` (or `Authorization: Bearer xq_...`), documented as "the account status check ... requiring only your API key header."

**Test executed:**
```
curl -s -i https://xquik.com/api/v1/account -H "x-api-key: xq_agent_pilot_dummy_key_0000000000"
```
Result: `HTTP/2 401` from `xquik.com` (Cloudflare-fronted), body:
```json
{"error":"unauthenticated","message":"Authentication required. Provide a valid API key or bearer token."}
```

This exactly matches the documented error shape from `https://docs.xquik.com/guides/error-handling`: `{ "error": "error_code", "message": "..." }` with `unauthenticated` explicitly listed as the 401 code for "missing or invalid API key or bearer token." The `www-authenticate: Bearer realm="xquik"` header further corroborates this is the real, correctly-routed auth-checking endpoint, not a 404/routing miss. **PASS.**

**Human gates for a real credential:**
1. Sign up for a dashboard account — https://dashboard.xquik.com/signup
2. Generate the first API key using the dashboard session (docs: "Use a dashboard session cookie to create the first API key") — https://docs.xquik.com/api-reference/api-keys/create
3. (Conditionally, for X-data/write endpoints only) Connect/re-authenticate an X account via OAuth in the dashboard — inferred from `x_auth_failure`/`account_needs_reauth` error codes at https://docs.xquik.com/guides/error-handling
4. (Conditionally, for paid endpoints) Billing/subscription setup via Stripe, per the "Account & Billing" doc category — https://docs.xquik.com

```json
{"result":"pass","http_status":401,"final_command":"curl -s -i https://xquik.com/api/v1/account -H \"x-api-key: xq_agent_pilot_dummy_key_0000000000\"","error_body_excerpt":"{\"error\":\"unauthenticated\",\"message\":\"Authentication required. Provide a valid API key or bearer token.\"}","wrong_attempts":0,"friction_notes":["Docs list two possible header schemes (x-api-key vs Authorization: Bearer) with no explicit statement of which is canonical for standard account keys vs guest/MPP keys — inferred x-api-key as primary from repeated example curl commands","pricing page (xquik.com/pricing) appears JS-rendered; WebFetch could not extract payment/free-tier prerequisites, left as unknown"],"human_gates":[{"step":"Sign up for a dashboard account","evidence":"https://dashboard.xquik.com/signup"},{"step":"Generate first API key via dashboard session cookie","evidence":"https://docs.xquik.com/api-reference/api-keys/create"},{"step":"Connect/re-authenticate an X account via OAuth (required for X-data/write endpoints)","evidence":"https://docs.xquik.com/guides/error-handling"},{"step":"Set up billing/subscription for paid endpoints","evidence":"https://docs.xquik.com"}],"confidence":"high"}
```
