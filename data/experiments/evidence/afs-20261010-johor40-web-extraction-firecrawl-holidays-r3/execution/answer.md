Now I'll make the designated Firecrawl scrape request for the OPM page.
I have the 2027 table. Let me parse it programmatically and generate the CSV.
完成。已通过指定服务 Firecrawl 匿名入口（`https://api.firecrawl.dev/v2/scrape`）抓取该 OPM 页面一次（HTTP 200，`success:true`，`creditsUsed:1`，`cacheState:hit`），并解析其中“2027 Holiday Schedule”表生成 CSV。

**文件**：`[WORKSPACE]/2027_holidays.csv`（UTF-8，列 `date,weekday,holiday`，11 条，按日期升序，脚注 `*/**` 已去除）

| date | weekday | holiday |
|---|---|---|
| 2027-01-01 | Friday | New Year's Day |
| 2027-01-18 | Monday | Birthday of Martin Luther King, Jr. |
| 2027-02-15 | Monday | Washington's Birthday |
| 2027-05-31 | Monday | Memorial Day |
| 2027-06-18 | Friday | Juneteenth National Independence Day |
| 2027-07-05 | Monday | Independence Day |
| 2027-09-06 | Monday | Labor Day |
| 2027-10-11 | Monday | Columbus Day |
| 2027-11-11 | Thursday | Veterans Day |
| 2027-11-25 | Thursday | Thanksgiving Day |
| 2027-12-24 | Friday | Christmas Day |

**来源**：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ （仅“2027 Holiday Schedule”表）

日期均按表中公布值记录（如 Independence Day 记为 07-05、Christmas Day 记为 12-24），未替换为节日日历日期。原始响应与页面 Markdown 一并保存在同目录，仅作本轮证据。