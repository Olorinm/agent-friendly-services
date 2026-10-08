Publication excerpt. Original independent evidence SHA256: 39dd3504a40428e87e59313702127536634e77c260787e54ea5c79f6c881f2c4. Original material is retained privately; controller additions are labelled.

# Exa MCP keyless fetch — business evidence (excerpt)

Source of the executed service call: `execution/artifacts/exa_fetch.py`
(streamable-HTTP MCP client) and raw captured response `execution/artifacts/exa_fetch_raw.txt`.

- Endpoint: `https://mcp.exa.ai/mcp` (protocol `2024-11-05`)
- Method: JSON-RPC `tools/call` with tool `web_fetch_exa`, args `urls=["https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/"]`
- Auth: none (no `x-api-key`/OAuth header present; keyless mode)
- Response: SSE `event: message` -> `{"result":{"content":[{"type":"text","text":"# Federal Holidays\nURL: https://www.opm.gov/...` containing the target page text

2027 section as returned by the service (verbatim excerpt, footnote marks in source):

```
# 2027

2027 Holiday Schedule

| Date | Holiday |
| --- | --- |
| Friday, January 01 | New Year’s Day |
| Monday, January 18 | Birthday of Martin Luther King, Jr. |
| Monday, February 15 * | Washington’s Birthday |
| Monday, May 31 | Memorial Day |
| Friday, June 18 ** | Juneteenth National Independence Day |
| Monday, July 05 ** | Independence Day |
| Monday, September 06 | Labor Day |
| Monday, October 11 | Columbus Day |
| Thursday, November 11 | Veterans Day |
| Thursday, November 25 | Thanksgiving Day |
| Friday, December 24 ** | Christmas Day |
```

Free rule applicability (this run): Exa MCP docs, Authentication section, document the
`Keyless` mode as "Free rate-limited usage without sign-in or API key" via
`https://mcp.exa.ai/mcp`, and the rate-limit note states a 429 means "the connection is
using Exa's free rate limits." This run used `web_fetch_exa` (enabled by default, not the
usage-billed `agent_run`) on the keyless endpoint without a key, and the call returned the
target content without a 429. Source:
https://exa.ai/docs/get-started/exa-mcp (retrieved for this review).

Scope: one public HTML table and CSV delivery; this does not demonstrate arbitrary dynamic, authenticated or anti-bot page coverage.

Controller scope note: no origin-freshness guarantee or cache timestamp was established for the Exa response. Matching the frozen table is not proof of a fresh origin fetch.
