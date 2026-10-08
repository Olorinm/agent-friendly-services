I have the 2027 table from the Firecrawl response. Let me verify against the raw HTML and generate the CSV.
完成。通过 Firecrawl 匿名 Public Scrape API（`https://api.firecrawl.dev/v2/scrape`，无 Key）抓取官方页面，从 `2027 Holiday Schedule` 表提取 11 个假日并生成 CSV。

文件：`[WORKSPACE]/federal_holidays_2027.csv`（UTF-8，列 `date,weekday,holiday`，按日期升序；日期为表中公布值，脚注标记已去除）

来源链接：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ （2027 Holiday Schedule 表；抓取返回 HTTP 200 / page status 200）

说明：表中日期含周末顺延后的公布日（如 Independence Day 记为 07-05、Christmas Day 记为 12-24），已按要求原样记录，未换成节日日历日。