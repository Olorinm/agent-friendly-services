# 公开核验摘要

数据服务：[CapitolExposed](https://www.capitolexposed.com/api-docs)。总控依据本次独立验收整理，逐行答案、原始响应、PDF 及交叉材料私有保留。

`financial-disclosures-002/v1`，独立结论为 `completed`。四位名单成员的查询、股票过滤、匹配与无匹配结论均与冻结官方参考一致，金额保留区间，出处具体，署名齐全，未以无匹配推断无持仓。

执行者发现股票查询参数未生效后，取回成员全部分页记录并本地过滤；官方原件由服务返回的出处定位。执行者核对了四份原始 PDF，明确披露未能枚举官方全量索引。验收者利用事前冻结的官方索引确认当前样本各自的月份覆盖，并核对采集 PDF 与冻结原件哈希一致；这属于验收核对，没有补写执行答案。该样本的完成不代表该服务在任意名单或月份都无覆盖缺口。

核对来源：[年度索引](https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip)、[Allen PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf)、[Beyer PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035106.pdf)、[Bresnahan PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035216.pdf)、[Case PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035275.pdf)。

本次执行约 517 秒，无超时。服务费用依文档化免费规则及免 Key 只读调用确认为零；模型费用另按实际用量估算。同期另一服务的部分观察仅作交叉参考，不能补齐本次交付。公开副本不包含可重建的交易行。
