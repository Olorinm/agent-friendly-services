Publication excerpt. Original independent evidence SHA256: 152c319ac98f8736246d91cb411373261f76d85e10d6683392a936e4e76815ca. Original material is retained privately; controller additions are labelled.

# Firecrawl anonymous access verification

Official sources: https://docs.firecrawl.dev/rate-limits and https://docs.firecrawl.dev/capabilities . Their keyless rules explicitly permit free Scrape use, subject to separate daily per-IP request and credit limits; the numerical anonymous allowances are not published.

The executor sent POST https://api.firecrawl.dev/v2/scrape with Content-Type: application/json and no API key/Authorization, for https://example.com/. The actual response was HTTP200, success=true, metadata.statusCode=200, title Example Domain and creditsUsed=1. Its returned body supported the delivered title and summary. Reusable configuration was saved in the declared persistent directory without secrets.

The independent grader also made one separate anonymous verification request with the same successful title/status. Thus the captured evidence describes one executor request plus one grader verification request, not one request for both phases combined. No account/payment was used.
