Got the page via Firecrawl (HTTP 200, success). Now parse the England and Wales 2027 table.
完成。通过指定服务 Firecrawl 匿名入口（`https://api.firecrawl.dev/v2/scrape`，HTTP 200，返回 `success:true`）取得页面，从“Upcoming bank holidays in England and Wales 2027”表中提取了 8 条记录。

**文件**：`[WORKSPACE]/england-wales-bank-holidays-2027.csv`（UTF-8，表头 `date,holiday`，按日期升序）

```csv
date,holiday
2027-01-03,New Year’s Day (substitute day)
2027-04-14,Good Friday
2027-04-17,Easter Monday
2027-05-01,Early May bank holiday
2027-05-29,Spring bank holiday
2027-08-28,Summer bank holiday
2027-12-25,Christmas Day
2027-12-26,Boxing Day
```

**官方来源**：https://www.gov.uk/bank-holidays

说明：日期与名称均照页面该地区 2027 表原文，未做推算、未改动名称中的 substitute day 标注；未使用 JSON/ICS 接口或直连原站，仅 1 次提取请求，无 403/429。原始响应与页面缓存在同目录（`firecrawl-response.json`、`firecrawl-bank-holidays.md`）。