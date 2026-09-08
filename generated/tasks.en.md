<!-- GENERATED — display translations, not execution prompts. -->
# Evaluated tasks

English translations of the recorded task versions. Original prompts and evidence remain unchanged; language requirements below describe the actual tests.

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
