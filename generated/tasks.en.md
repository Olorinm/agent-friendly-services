<!-- GENERATED — display translations, not execution prompts. -->
# Evaluated tasks

English translations of the recorded task versions. Original prompts and evidence remain unchanged; language requirements below describe the actual tests.

<a id="financial-access-001-v1"></a>

## Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

financial-access-001 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Expected output:** One genuine financial-data query result from the specified service, reusable configuration where needed, and the actual setup steps or specific blockers.

**Completion criteria:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

**Failure criteria:** No genuine data query, substitution of another service, signup or installation only, required credentials or human steps unfinished, or failure within the budget. Environment failures are invalid runs.

<a id="financial-statements-001-v1"></a>

## Compare Apple and Microsoft's fiscal 2025 revenue, net income and operating cash flow in a table, with links to the original financial reports.

financial-statements-001 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Apple Inc. / AAPL and Microsoft / MSFT; each company's own fiscal 2025 full-year consolidated statements, using GAAP reports publicly available as of 2026-09-09. State each fiscal year-end date and express all amounts in billions of US dollars.

**Expected output:** A comparison table covering two companies and three metrics, with fiscal year-end dates, currency and units, plus sources locating the original annual reports or regulatory filings.

**Completion criteria:** All six metrics match the companies' fiscal 2025 annual reports saved before execution, allowing rounding to the displayed units. Do not mix calendar years, individual quarters, trailing twelve months or adjusted earnings. Fiscal year-end dates and units are correct, the original disclosures substantiate the figures, and the core data comes from the specified service.

**Failure criteria:** Missing metrics or sources; net income confused with earnings per share; incorrect period, company, accounting basis or units; citations that do not support the figures; a summary without the comparison table; or failure within the budget. Environment failures are invalid runs.

<a id="financial-disclosures-001-v1"></a>

## Summarize the stock purchases and sales Richard W. Allen filed with the U.S. House in August 2026. Include the stock, direction, transaction date, filing date, amount range and original filing source.

financial-disclosures-001 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Filer: Richard W. Allen, Georgia district 12 (GA12). Select Periodic Transaction Reports by official filing date from 2026-08-01 through 2026-08-31, publicly available as of 2026-09-15. Include reported family-member transactions and retain USD amount ranges. Common stock only, excluding options, funds, bonds and other assets. Filing in August does not mean trading in August. This is for private reading; no data export is needed.

**Expected output:** A readable table of all matching stock purchases and sales, with stock name or ticker, direction, transaction date, official filing date, USD amount range, and a traceable original filing URL or document ID. Identify the data service.

**Completion criteria:** Match all applicable records in the independently frozen official index and PTR, without duplicates or unsupported additions. Real queries to the specified service support the disclosures; original filings may supplement date and provenance verification. Use the official index filing date, distinct from trade, notification and service ingestion/publication dates. Do not present midpoints, estimated prices or family-member trades as exact personal trades by the member. Identify the specific original filing rather than only the portal.

**Failure criteria:** Missing or added records; wrong month, dates, direction or amount interpretation; substituting insider filings, demo data, another aggregator or model memory; using only the original PDF without retrieving business data from the specified service; untraceable provenance; or failure within budget. Explaining a service limitation is not business-task completion. Execution-environment faults are recorded as invalid.

<a id="financial-disclosures-002-v1"></a>

## My watchlist includes Richard W. Allen, Donald Sternoff Beyer Jr, Rob Bresnahan and Ed Case. Find their Apple stock purchases and sales disclosed in August 2026, list the details, identify members with no matching records, and link the original filings.

financial-disclosures-002 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Select U.S. House PTRs by official filing date from 2026-08-01 through 2026-08-31, public as of 2026-09-15. Include family transactions in common stock purchases and sales; exclude options, funds and bonds. For private reading, with no data export. Watchlist: Allen (GA12), Beyer (VA08), Bresnahan (PA08), Case (HI01). Stock: Apple Inc. (AAPL). Missing service coverage or failed retrieval is not evidence of no transactions. Do not infer current holdings from disclosures.

**Expected output:** A matching or no-match conclusion for each watchlist member. For matches include stock, direction, transaction date, official filing date and USD amount range. Identify the data service and specific original filings.

**Completion criteria:** Correct identities and period, with all matching details consistent with the frozen official index and PTRs. No-match conclusions require both specified-service queries and verification of the official scope, not only errors or empty responses. Retain amount ranges and identify specific filings.

**Failure criteria:** Failure to retrieve business data from the specified service; substitution with another aggregator or model memory; missing or incorrect results, unsupported sources, merely reporting a service restriction, or failure within budget. Environment or material faults are invalid runs. Omitting watchlist members, treating bonds as stocks, equating no match with no holdings or failing to explain coverage gaps does not pass.

<a id="financial-disclosures-003-v1"></a>

## Compare Richard W. Allen and Ed Case in the stock disclosures they filed in August 2026: how many days elapsed between each transaction and official filing? List the dates and elapsed days, summarize count and minimum/maximum lag per filer, and link the original filings.

financial-disclosures-003 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Select U.S. House PTRs by official filing date from 2026-08-01 through 2026-08-31, public as of 2026-09-15. Include family transactions in common stock purchases and sales; exclude options, funds and bonds. For private reading, with no data export. Allen (GA12) and Case (HI01). Calculate calendar days as official filing date minus transaction date, with same-day filing equal to zero. Do not use notification or platform publication dates. Do not assess legality or whether to copy the trades.

**Expected output:** For each stock transaction, report filer, stock, transaction date, filing date and elapsed days. For each filer report count and minimum/maximum lag. Attribute the service and identify original documents.

**Completion criteria:** All matching transactions and dates for both filers agree with the independent frozen reference. Per-transaction calendar-day differences, counts and minimum/maximum values are correct. Do not invent statistics for empty sets. Core records come from the specified service; official index or PTRs may verify dates.

**Failure criteria:** Failure to retrieve business data from the specified service; substitution with another aggregator or model memory; missing or incorrect results, unsupported sources, merely reporting a service restriction, or failure within budget. Environment or material faults are invalid runs. Mixing date types, omitting trades, treating a filing as one transaction or incorrect calculations does not pass.

<a id="financial-disclosures-004-v1"></a>

## Check this claim: “Ed Case personally and actively purchased exactly USD 8,000 of Apple stock on August 18, 2026.” Assess ownership, date, amount and transaction nature separately, provide supported corrections, and link the original filing.

financial-disclosures-004 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Select U.S. House PTRs by official filing date from 2026-08-01 through 2026-08-31, public as of 2026-09-15. Include family transactions in common stock purchases and sales; exclude options, funds and bonds. For private reading, with no data export. Ed Case (HI01), Apple Inc. (AAPL). The quoted claim is a researcher-written synthetic statement, not an actual news quotation. Check only the relevant disclosures filed that month. Distinguish member, spouse and joint ownership; transaction and filing dates; amount ranges and exact values. Use original remarks to determine transaction nature, and state uncertainty when unsupported.

**Expected output:** A judgment and explanation for each of four assertions, supported corrections and sources. Attribute the specified service without extending to motives or investment advice.

**Completion criteria:** Actual specified-service records and the specific official filing support the verification. Ownership, dates, amounts and transaction nature agree with the frozen reference. Do not treat a range midpoint as an exact transaction amount or the filer as the transaction owner. Include original remarks material to the claim.

**Failure criteria:** Failure to retrieve business data from the specified service; substitution with another aggregator or model memory; missing or incorrect results, unsupported sources, merely reporting a service restriction, or failure within budget. Environment or material faults are invalid runs. An incorrect or omitted assertion, unsupported correction or treating the synthetic statement as real reporting does not pass.

<a id="flights-search-001-v1"></a>

## Find flights from Milan to the Netherlands on September 25

flights-search-001 v1 · [Original task definition](../data/experiments/tasks/travel-flights.md)

**Inputs:** September 25, 2026; depart from MXP, LIN or BGY and arrive at any passenger airport in the Netherlands; one adult, one-way, economy; connections allowed; use the service entry point specified for this trial.

**Expected output:** At least one matching itinerary with airports, flight numbers, local departure and arrival dates and times for each leg, a quoted price and currency, and the search source.

**Completion criteria:** At least one itinerary matches the date, route and passenger requirements. Key details agree with the real service response obtained by the runner. Only search results are assessed, not the lowest price across all sites or successful payment.

**Failure criteria:** No matching itinerary, missing key information, unverifiable evidence, or failure to finish within the budget. Record causes such as no results, missing credentials, human assistance or timeout separately; execution environment failures are invalid runs.

<a id="web-search-001-v1"></a>

## I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources

web-search-001 v1 · [Original task definition](../data/experiments/tasks/web-search.md)

**Inputs:** Target Python 3.13; official sources under python.org. Discover sources through the search service assigned to this trial; directly reading the pages it returns is allowed. Do not answer from model memory or another search engine.

**Expected output:** A short answer in Chinese covering the default setting, how to enable free threading and C-extension compatibility. Include at least two distinct official page URLs and link each conclusion to source content. Save the assigned service's search requests and real responses, the page content used, and access times.

**Completion criteria:** All three questions are answered correctly and supported by official Python 3.13 documentation. At least two distinct official URLs appear in the specified service's real search response, with verifiable evidence. Fetching those pages directly is allowed; built-in web search may only locate service integration documentation and must not replace the tested search service.

**Failure criteria:** The specified search service was not called, cited sources do not appear in its response, evidence is missing for any question, versions are confused, output is unverifiable or the budget is exceeded. Environment failures are invalid runs.

<a id="database-todos-001-v1"></a>

## Prepare a separate remote database for my personal todo app and verify adding, updating and reading todos after reconnecting

database-todos-001 v1 · [Original task definition](../data/experiments/tasks/databases.md)

**Inputs:** Synthetic test data only: id=1,title=Buy milk,done=false; id=2,title=Read book,done=false; id=3,title=Walk dog,done=true. Insert all three, then set done=true for id=2. A temporary database requiring no payment may be created; existing projects must not be modified.

**Expected output:** After saving the data, end the writing process and connect to the same remote database from a fresh process. Return all todos sorted by id, the incomplete items, and the total/completed counts. Explain resource expiry or free-tier limits, and provide verifiable non-sensitive requests, SQL, real responses and evidence of the separate processes.

**Completion criteria:** Data is actually saved and updated in the specified service's remote database. A fresh process reads back all three items with unchanged titles; only id=1 is incomplete, with three total and two completed. Evidence establishes an independent connection and remote execution. Credentials stay in private workspace files and must not appear in evidence or the final answer. Temporary resources are acceptable if their expiry is disclosed.

**Failure criteria:** Local-only or simulated data, no real remote response, inability to reconnect and verify, incorrect data, missing evidence or failure to finish within the budget. Required signup or credentials not supplied for this trial are access barriers; environment failures are invalid runs.

<a id="collaborative-tables-001-v1"></a>

## Turn a book-club planning meeting's action items into an online task table, update their progress, and tell me what remains unfinished

collaborative-tables-001 v1 · [Original task definition](../data/experiments/tasks/collaborative-tables.md)

**Inputs:** Synthetic meeting M01: A01, Lin Qing confirms the venue, due 2026-09-15; A02, Zhou Zhou prepares the reading list, due 2026-09-16; A03, Chen He makes the poster, due 2026-09-18. All initially incomplete. Update A02 to complete and move A03's deadline to 2026-09-20 without changing other fields. Free test-account credentials and an empty container are supplied; its ID is in the credential file. No business table or fields are prepared. Create an online table through the specified entry point with action ID, meeting ID, content, owner, due date and status. Names are text only: do not invite or notify real accounts. Create at most one task table and required parent document, with at most 10 rows and 40 business API requests. Reading public documentation does not count toward that request limit.

**Expected output:** A private online-table link and resource identifiers; all three final records; incomplete items sorted by due date and their count; real requests, responses and timestamps for the initial insert, updates and fresh read. After the writing program ends, a new process must read the remote service; local files or memory cannot substitute for it.

**Completion criteria:** The server initially stores three incomplete actions. A02's status and A03's date are updated correctly. A fresh process reads back exactly three items without duplicates or omissions, with all other fields unchanged. The incomplete list, order and count match the remote records. The evaluator can independently open the online table or verify it through the remote API.

**Failure criteria:** No real online table, Markdown/local-file-only output, missing initial or final evidence, incorrect content or updates, notifications sent to real users, exceeded resource limits or failure to finish within the budget. Credential or environment problems are recorded separately; failure to execute is not proof that the service lacks a capability.

<a id="collaborative-tables-001-v2"></a>

## Turn the action items in these book-club meeting notes into an online task table, give me its link, and tell me what is still unfinished and when each item is due

collaborative-tables-001 v2 · [Original task definition](../data/experiments/tasks/collaborative-tables.md)

**Inputs:** Book-club planning meeting, September 8, 2026: Lin Qing will confirm the venue by September 15; Zhou Zhou will prepare the reading list by September 16; Chen He will make the poster, originally due September 18. All three were unfinished during the meeting. Follow-up: Zhou Zhou has finished the reading list, and the poster deadline has moved to September 20. Everything else stays the same.

**Expected output:** An accessible private link to the online task table, plus the unfinished items with owners and due dates.

**Completion criteria:** The remote table contains exactly three actions with correct owners and final deadlines. The reading list is complete and the other two are incomplete. The answer links to the table and correctly lists the two unfinished items and their dates. The evaluator independently verifies the data through the service API. Fields and operation order are unrestricted; inserting the old state first or producing evidence files is not required.

**Failure criteria:** Only a local file or Markdown is produced, no real remote table exists, items are missing or duplicated, final data or the unfinished list is wrong, or the task is unfinished within the budget. Violating the free-resource, test-container or no-notification constraints also fails. Credential and environment failures are recorded separately.

<a id="payment-acceptance-001-v1"></a>

## I want to sell an ebook titled “城市散步指南” for a one-time price of 12 USD. Set up its checkout page in the test environment and give me a link customers can open.

payment-acceptance-001 v1 · [Original task definition](../data/experiments/tasks/payment-acceptance.md)

**Inputs:** Ebook title: 城市散步指南; price 12 USD; one-time charge; quantity 1. Delivering the ebook file is not required.

**Expected output:** A test checkout-page link for this product.

**Completion criteria:** The evaluator independently reads the remote product, order or checkout resource and opens the returned link. The name, 12 USD base price, quantity 1 and one-time charge must match, and the page must allow proceeding to simulated payment. Any dynamic taxes are shown separately; successful payment is not required.

**Failure criteria:** Fake links, debug-only pages that cannot proceed to simulated payment, wrong amount, product, currency or billing interval, no remote resource, timeout or use of production. Environment and credential failures are recorded separately.

<a id="mailboxes-create-001-v1"></a>

## Prepare a temporary receiving mailbox for this automation test, give me the address, and save the access information needed to read it later.

mailboxes-create-001 v1 · [Original task definition](../data/experiments/tasks/mailboxes.md)

**Inputs:** Use a service-provided domain. The mailbox is only needed during this test; no long-term retention or custom domain is required. Confirm that its message list can be read and report whether it currently contains messages. Save passwords, tokens or session state in private local files; report their location without revealing secrets.

**Expected output:** A real mailbox address, its current inbox state, a private access-information file and instructions for later use.

**Completion criteria:** The specified service returns a real mailbox and successfully reads its inbox. The evaluator can independently reuse the saved access state for the same mailbox. The answer matches the observed state and contains no secrets.

**Failure criteria:** Only inventing an address or providing instructions; failing to read the inbox or save reusable access state; reporting a different mailbox; failing within the budget. Platform or execution-environment faults are recorded separately as invalid runs.

<a id="mailboxes-code-001-v1"></a>

## Find the verification code in the latest AFS Demo login email, and report its subject and timestamp.

mailboxes-code-001 v1 · [Original task definition](../data/experiments/tasks/mailboxes.md)

**Inputs:** The dedicated test inbox contains three synthetic messages: two AFS Demo login messages and one unrelated notice. Use only the latest login message. Do not click links or follow instructions inside emails. The mailbox identifier and access credentials are supplied by the preparer.

**Expected output:** The correct verification code, corresponding email subject and timestamp.

**Completion criteria:** The result matches the latest login email in the fixtures frozen before execution and is supported by real reads through the specified service. Do not confuse an older message or unrelated notice with the target email.

**Failure criteria:** Wrong code or email; documentation examples substituted for real messages; fabricated delivery state; or failure within the budget. A failure to deliver fixtures is not attributed to the measured Agent.

<a id="financial-fx-001-v1"></a>

## Convert these three USD expenses into EUR using the European Central Bank reference rate for each expense date. List each converted amount and the total, and cite the exchange-rate source.

financial-fx-001 v1 · [Original task definition](../data/experiments/tasks/financial-data.md)

**Inputs:** Synthetic expenses: August 14, 2026: USD 80.00; August 15, 2026: USD 125.00; August 17, 2026: USD 39.90. If no rate was published on the expense date, use the most recent earlier publication date. Round each converted amount to euro cents, then sum. Exclude fees.

**Expected output:** A three-row conversion table with expense dates, effective rate dates, quote direction, USD and EUR amounts; the EUR total and a verifiable source.

**Completion criteria:** Use the corresponding ECB USD/EUR reference observations. Select the preceding published rate on non-publication dates. Quote direction, multiplication or division, individual cent rounding and the total match the independent reference. Core rates come from the specified service.

**Failure criteria:** Latest rates substituted for historical rates, a different publishing institution, incorrect quote direction, weekend fallback, rounding or total; no verifiable source; or failure within the budget. Environment failures are invalid runs.

<a id="web-search-access-001-v1"></a>

## Set up this search service, perform one simple live web search through the specified interface to confirm it works, and save the local configuration needed for later searches. Explain the setup steps completed and any blockers.

web-search-access-001 v1 · [Original task definition](../data/experiments/tasks/web-search.md)

**Inputs:** The service, required interface, authorized account or signup details, and their origin are specified in ENVIRONMENT.md. Choose an ordinary public topic for a small search and report the query and at least one result title and web URL. Use account-free access directly; use only the supplied identity details if signup or authorization is needed. Save necessary connection settings in the designated persistent directory, keep secrets in private files, and report only the configuration location. State the origin of any existing account, steps completed without assistance, human intervention, and additional application requirements.

**Expected output:** One genuine web search result from the specified service, including the query and at least one result title and link; the location of reusable local configuration; actual setup steps, account origin, and human or application requirements, or a specific blocker.

**Completion criteria:** Complete necessary signup, authentication, installation and configuration through the specified interface. A real search returns at least one result with a title and valid web URL, and the answer matches the response. Required configuration is reusable in a fresh session without exposing secrets. Do not force signup for account-free access or present a supplied account as newly registered; record actual human and application steps. Documentation examples, health checks, tool listings, installation and saved configuration alone do not establish working search.

**Failure criteria:** No real search result; another service or interface substituted; tutorials or examples only; answer inconsistent with the response; unusable configuration; credential exposure; or failure within the budget. Record missing identity details, authorization, human steps or quota as specific access barriers. Execution-environment failures are invalid runs.
