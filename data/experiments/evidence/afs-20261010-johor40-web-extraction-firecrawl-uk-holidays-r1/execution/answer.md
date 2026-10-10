Response 200, `success: true`. Now let me parse the 2027 England and Wales table programmatically.
The markdown table labeled "2027" appears to contain 2028 dates (dates shifted one year). Let me inspect the full structure of the returned content before trusting the heading.
The returned Markdown shows a systematic one-year offset in the year headings: the table under "2027" actually contains 2028 dates (verified by the page's own day-of-week column), while the 2027 data sits under the "2026" heading. I need the raw HTML to confirm the true heading–table association before answering.
The raw HTML resolves it definitively: the 2027 table is encoded with `<time datetime="2027-...">`. Let me extract the exact 2027 England & Wales rows from the HTML.
完成。已通过指定服务 Firecrawl 抓取 `https://www.gov.uk/bank-holidays`（2 次匿名 scrape，间隔约 63 秒，均 HTTP 200），并从页面 HTML 中提取 England and Wales 2027 表。

**交付文件**：`[WORKSPACE]/england-wales-bank-holidays-2027.csv`（UTF-8 无 BOM，表头 `date,holiday`，日期升序，8 条）

```
date,holiday
2027-01-01,New Year’s Day
2027-03-26,Good Friday
2027-03-29,Easter Monday
2027-05-03,Early May bank holiday
2027-05-31,Spring bank holiday
2027-08-30,Summer bank holiday
2027-12-27,Christmas Day (substitute day)
2027-12-28,Boxing Day (substitute day)
```

**官方来源**：https://www.gov.uk/bank-holidays （Open Government Licence v3.0，来源：GOV.UK）

**关键核对说明**：Firecrawl 返回的 Markdown 把年份标题整体错位了一年（标着 “2027” 的表内容实为 2028），若直接采用会出错。我改以同一响应中的 `rawHtml` 为准，用表格 caption “Upcoming bank holidays in England and Wales 2027” 以及每行 `<time datetime="2027-…">` 的显式年份来锁定该地区该年记录，未用算法推算、未改动节日原日历日期，名称按页面原文保留（含 `(substitute day)`，含印刷体撇号 `’`）。抓取期间未触发 403/429 或任何授权/付费要求。