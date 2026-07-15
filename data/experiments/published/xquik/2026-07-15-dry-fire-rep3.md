# Xquik — dry-fire rep 3 (2026-07-15)

Model: sonnet · max turns: 40 · runner: scripts/agent-verify.ts

---

I have enough evidence to complete the verification.

## Summary

**Canonical first call**: `GET https://xquik.com/api/v1/account` with header `x-api-key: xq_<key>` — documented in the API reference as "Copy-paste this to verify your API key works" (docs.xquik.com/api-reference/overview).

**Executed** with a fake key (`xq_0000...dead`, obviously invalid, never a real credential) → got `HTTP/2 401` from the correct `xquik.com` origin (Cloudflare-fronted, correct CSP/security headers matching the real app), with JSON body:
```json
{"error":"unauthenticated","message":"Authentication required. Provide a valid API key or bearer token."}
```
This matches the documented auth-failure shape from `docs.xquik.com/guides/error-handling` (`error: "unauthenticated"`, 401, message about missing/invalid key) — same error code, near-identical message. **PASS.**

**Human gates found** (no signup/KYC/payment attempted):
- Create an account via dashboard signup (docs.xquik.com/api-reference/api-keys/create implies dashboard session needed first)
- Generate an API key: `POST /api/v1/api-keys` while authenticated via dashboard session or OAuth — `fullKey` shown only once
- Docs don't state whether a paid subscription is required before `/account` works; the llms.txt summary says the *radar* endpoint "requires subscription," implying some gating exists, but pricing page fetch returned no tier/payment details
- Docs don't mention KYC/phone/card explicitly, but Stripe checkout is referenced in the site's CSP (`checkout.stripe.com`), suggesting billing is Stripe-based — unconfirmed from text alone

```json
{"result":"pass","http_status":401,"final_command":"curl -s -i -X GET \"https://xquik.com/api/v1/account\" -H \"x-api-key: xq_0000000000000000000000000000000000000000000000000000000000dead\"","error_body_excerpt":"{\"error\":\"unauthenticated\",\"message\":\"Authentication required. Provide a valid API key or bearer token.\"}","wrong_attempts":0,"friction_notes":["docs.xquik.com/llms.txt lists REST base URL as https://xquik.com/api/v1, not under docs.xquik.com — easy to miss and hit docs domain by mistake","api-reference/api-keys/create page does not document signup/payment/KYC prerequisites, only key creation once already authenticated","pricing page fetch returned no concrete tier/payment/API-access gating details despite llms.txt claiming /radar 'requires subscription'","actual 401 message text differs slightly from the error-handling guide's example message but error code and status match exactly"],"human_gates":[{"step":"Create a Xquik account via dashboard signup","evidence":"https://dashboard.xquik.com/signup"},{"step":"Authenticate to dashboard (session cookie) or obtain OAuth bearer token, then POST /api/v1/api-keys to generate a real API key (fullKey shown only once)","evidence":"https://docs.xquik.com/api-reference/api-keys/create"},{"step":"Possibly subscribe to a paid plan — llms.txt states some endpoints 'require subscription'; exact gating for /account unconfirmed from public pricing page","evidence":"https://xquik.com/pricing"}],"confidence":"high"}
```
