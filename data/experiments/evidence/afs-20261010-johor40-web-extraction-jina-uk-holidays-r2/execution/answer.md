完成。通过指定服务 Jina Reader (`https://r.jina.ai/https://www.gov.uk/bank-holidays`) 匿名单次提取（HTTP 200，限流余量 19/20），从返回 Markdown 的 “Upcoming bank holidays in England and Wales 2027” 表取得全部 8 条假日。

- 文件：`[WORKSPACE]/england-and-wales-bank-holidays-2027.csv`（UTF-8，表头 `date,holiday`，按日期升序）
- 官方来源：https://www.gov.uk/bank-holidays （England and Wales → 2027）

| date | holiday |
|---|---|
| 2027-01-01 | New Year’s Day |
| 2027-03-26 | Good Friday |
| 2027-03-29 | Easter Monday |
| 2027-05-03 | Early May bank holiday |
| 2027-05-31 | Spring bank holiday |
| 2027-08-30 | Summer bank holiday |
| 2027-12-27 | Christmas Day (substitute day) |
| 2027-12-28 | Boxing Day (substitute day) |

名称与页面一致（含 substitute day 与 U+2019 撇号），仅取 2027 年 England and Wales，未混入 Scotland、Northern Ireland 或其他年份，也未使用 JSON/ICS 接口。原始响应留存在 `jina_response.md`。