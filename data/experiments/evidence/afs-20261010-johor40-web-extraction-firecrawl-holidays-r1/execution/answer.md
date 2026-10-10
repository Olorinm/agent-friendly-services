Found the 2027 table at page.md:126-138. Now generating the CSV by parsing that table.
完成。

**文件**：`[WORKSPACE]/holidays_2027.csv`（UTF-8，列 `date,weekday,holiday`，11 行，按日期升序）

**来源**：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ （经指定服务 `https://api.firecrawl.dev/v2/scrape` 抓取，HTTP 200，内容为页面 “2027 Holiday Schedule” 表）

内容如下：

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

按网页公布值记录（如 Juneteenth 记为 6/18、Independence Day 记为 7/05、Christmas 记为 12/24），未转换为节日日历日期；脚注标记 `*`/`**` 已去除。首次请求即成功，无重试或限流。