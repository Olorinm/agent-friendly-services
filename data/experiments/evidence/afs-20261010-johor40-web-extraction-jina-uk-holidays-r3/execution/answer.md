I have the England and Wales 2027 table. Now I'll extract it programmatically into a CSV.
完成。用 Jina Reader（`https://r.jina.ai/`）对该 GOV.UK 页面发出 1 次请求即返回 HTTP 200，从返回 Markdown 中仅取 "Upcoming bank holidays in England and Wales 2027" 表。

文件：`[WORKSPACE]/england_wales_bank_holidays_2027.csv`（UTF-8，表头 `date,holiday`，按日期升序，8 条）

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

名称保留页面原文（含 `New Year’s Day` 的弯引号及 `(substitute day)` 标注），日期用表内公布值。

官方来源：https://www.gov.uk/bank-holidays

过程记录：1 次提取请求（≤6 次/阶段，间隔要求满足），无重试、无 403/429，未使用原站 JSON/ICS 接口或其他数据源。原始返回保存在 `jina_bank_holidays.md`。