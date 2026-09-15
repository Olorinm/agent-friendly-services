# 公开核验摘要

数据服务：[CapitolExposed](https://www.capitolexposed.com/api-docs)。总控依据本次独立验收整理，原始交易行、答案、日志及交叉参考私有保留。

`financial-disclosures-001/v1`，独立结论为 `completed`。验收者核对真实服务请求与采集响应，独立按官方提交月份重筛，确认交付的匹配集合及所需字段符合冻结官方参考。交易日、提交日和通知日分别核对，家庭成员归属及金额区间正确；具体原始出处和服务署名齐全。

[官方 PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf) 采集副本 SHA-256 为 `6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`，与事前冻结原件一致；[官方年度索引](https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip)支持提交月份的范围核对。哈希用于识别材料，不能替代逐项核对。

执行约 4 分 22 秒，无超时。过程包含查询、分页、原件下载及解析工具安装，这不是单次 API 延迟。官方文档及实际调用支持免费免 Key 只读使用，服务费用为零。

同期另一服务的实际输出在验收前冻结，验收者确有读取；本次结论依据自身完整交付和独立官方参考，未用其他答案补齐。单题一次完成不代表长期稳定性、总体排名或其他接入方式。
