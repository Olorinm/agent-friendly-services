完成。通过指定服务 `https://api.firecrawl.dev/v2/scrape` 匿名抓取 `https://www.gov.uk/bank-holidays`（HTTP 200，单次请求，未触发 403/429），仅取 "Upcoming bank holidays in England and Wales 2027" 表，共 8 条。

文件：`[WORKSPACE]/england_wales_bank_holidays_2027.csv`（UTF-8）

```
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

官方来源：https://www.gov.uk/bank-holidays （England and Wales → 2027；页面标注 Last updated: 24 November 2025）。原始抓取证据存于 `firecrawl_response.json`，未使用 Scotland/Northern Ireland 或其他年份，也未改用 JSON/ICS 接口。