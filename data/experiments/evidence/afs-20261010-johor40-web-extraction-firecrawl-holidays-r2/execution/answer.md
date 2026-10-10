Got the 2027 table. Now generating the CSV.
Done. Used the specified Firecrawl service (1 request, HTTP 200, no retries) to scrape the OPM page and extracted only the **2027 Holiday Schedule** table.

**File:** `[WORKSPACE]/opm_2027_holidays.csv` (UTF-8, 11 rows, sorted by date; footnote markers removed; weekdays verified against each date)

```
date,weekday,holiday
2027-01-01,Friday,New Year’s Day
2027-01-18,Monday,"Birthday of Martin Luther King, Jr."
2027-02-15,Monday,Washington’s Birthday
2027-05-31,Monday,Memorial Day
2027-06-18,Friday,Juneteenth National Independence Day
2027-07-05,Monday,Independence Day
2027-09-06,Monday,Labor Day
2027-10-11,Monday,Columbus Day
2027-11-11,Thursday,Veterans Day
2027-11-25,Thursday,Thanksgiving Day
2027-12-24,Friday,Christmas Day
```

**Source:** https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ (2027 Holiday Schedule table)

Notes: dates are recorded exactly as published in the table (observed dates, e.g. Juneteenth → 2027-06-18, Independence Day → 2027-07-05), not the nominal holiday calendar dates. Holiday names keep the page's spelling/punctuation. Raw scrape response saved at `firecrawl_response.json`; build script at `build_csv.py`.