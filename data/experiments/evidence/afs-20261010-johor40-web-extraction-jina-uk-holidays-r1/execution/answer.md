Single Jina Reader request succeeded (HTTP 200). Extracting the England and Wales 2027 table.
完成。

**文件**：`england-wales-bank-holidays-2027.csv`（UTF-8，表头 `date,holiday`，按日期升序，8 条）

| date | holiday |
| --- | --- |
| 2027-01-01 | New Year’s Day |
| 2027-03-26 | Good Friday |
| 2027-03-29 | Easter Monday |
| 2027-05-03 | Early May bank holiday |
| 2027-05-31 | Spring bank holiday |
| 2027-08-30 | Summer bank holiday |
| 2027-12-27 | Christmas Day (substitute day) |
| 2027-12-28 | Boxing Day (substitute day) |

**官方来源**：https://www.gov.uk/bank-holidays （England and Wales → Upcoming bank holidays in England and Wales 2027）

执行记录：通过指定服务 Jina Reader 单次匿名请求 `https://r.jina.ai/https://www.gov.uk/bank-holidays`，HTTP 200，一次成功，无 403/429；间隔与次数限制均未触及。未使用 JSON/ICS 接口或直连原站，日期与名称（含 substitute day）均取自该返回表格原文。