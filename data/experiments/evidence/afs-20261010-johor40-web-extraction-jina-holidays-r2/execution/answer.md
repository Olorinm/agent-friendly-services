完成。CSV 已按网页公布的 2027 Holiday Schedule 表生成，11 条全部按日期排序，日期取表中公布值（如 Independence Day 记 2027-07-05、Christmas Day 记 2027-12-24，未自行换成节日日历日），星期与日期已交叉校验一致。

- 文件：`holidays_2027.csv`（UTF-8，列：`date,weekday,holiday`）
- 来源：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/#url=2027
- 通过指定服务取得：`https://r.jina.ai/https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/`（HTTP 200，一次请求；原始响应存于 `opm.md`）

未使用其他网站、日历数据或模型记忆；脚注标记 `*`/`**` 已去除。