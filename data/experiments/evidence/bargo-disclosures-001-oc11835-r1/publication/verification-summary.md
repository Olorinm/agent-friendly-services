# 独立验收的公开摘要

结论：completed
独立验收确认本题全部用户要求满足：指定服务真实返回的数据集合完整，按官方提交日期筛选，股票类型、日期、方向、金额区间与原始申报出处均已核对。

本文件由总控从已完成的独立验收中删减整理，仅作为发布前摘要；未重新判分。原始答案、交易行、完整日志和完整验收依据私有保存。

原始独立验收 SHA256：`65c7377734999adf9ed98a0e2991df0cec14e8bc587af0dbfb0a5187c3dd03a1`

## 核对项目

- 通过：业务数据由指定服务 bargo-congress 真实 API 返回，未用其他聚合服务或模型记忆替代
- 通过：记录集合与冻结官方参考完全一致：无遗漏、无重复或无依据记录
- 通过：口径正确：按官方提交日筛选，区分交易日/通知日/提交日；仅普通股、含家庭成员交易；金额保留区间，未表述为本人精确成交金额
- 通过：原始申报出处可核对：Filing ID、官方 PDF 链接与检索入口
- 通过：标明数据服务来源并满足署名要求
- 通过：授权与约束遵守：仅免 Key 免费入口、不注册不付款、限额内、结果私有留存、指定入口与执行配置相符

## 来源与留底

- 数据服务：Bargo，https://www.bargo.ai/free-apis/congress
- 服务条款：https://www.bargo.ai/free-apis/terms
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip；冻结源 SHA256：`75bc79034ec5b3c6d84385442377c6de56c54291ca799e4f64b6c60196d9a78c`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf；冻结源 SHA256：`6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`

私有执行日志 SHA256：`a655256825db10fbe4be19a16a3f267f7569ad68f146c94ca20d8080c003d1ad`
私有原始答案 SHA256：`465274b632aab7fdb421f8e4bffd0cfa4df9dbb2e8bf46f205b73f24d9900c4b`

## 服务费用依据

费用分类：confirmed_free
- 免费规则：官方接入文档明确 read 端点免 Key 免费（仅限流：免 Key 30 请求/100 行每日每 IP），付费 Key 仅为可选的限额提升，页面标注 FREE · NO CARD
- 本次适用观察：本次执行未注册、未提供 Key 或支付方式；对 /trades、/members、/stats、openapi.json 的免 Key 请求均成功返回，响应头 x-ratelimit-limit=30、x-ratelimit-remaining 最低 24，远低于每日免费限额

模型用量、执行费用、验收费用以运行器记录和冻结价表计算为准；API 价估算不代表订阅账户实付。

## 本轮前提

本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
