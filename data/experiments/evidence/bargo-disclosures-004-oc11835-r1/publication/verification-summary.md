# 独立验收的公开摘要

结论：not_completed
独立验收判定本题未完成：执行触及预算上限，虽已取得相关业务数据并完成部分核对，但未交付四项说法的逐项判断、有依据的成文更正和完整原始申报出处。属本次 Agent 在预算内未完成，未判为服务能力不支持；本次执行 Token 与模型费因最后请求未完整采集而保持未知。

本文件由总控从已完成的独立验收中删减整理，仅作为发布前摘要；未重新判分。原始答案、交易行、完整日志和完整验收依据私有保存。

原始独立验收 SHA256：`6e3e4bb1a7c76306e9388aa9dfd2d6ba8cd4a458125ab1c98af0e98d4a9d6fa0`

## 核对项目

- 通过：业务数据由指定服务 bargo-congress REST API 直接返回（keyless 只读，未用其他聚合服务或模型记忆替代）
- 通过：已取得并核对众议院原始申报 PTR（归属、交易日、通知日、金额、原始备注）
- 未通过：四项主张（交易归属、日期、金额、交易性质）在交付物中逐项给出明确判断
- 未通过：写出有依据的更正并附原始申报出处
- 通过：未把区间中点当精确成交额、未把申报人当交易所有人、未遗漏影响说法真假的原始备注

## 来源与留底

- 数据服务：Bargo，https://www.bargo.ai/free-apis/congress
- 服务条款：https://www.bargo.ai/free-apis/terms
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip；冻结源 SHA256：`75bc79034ec5b3c6d84385442377c6de56c54291ca799e4f64b6c60196d9a78c`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf；冻结源 SHA256：`6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035106.pdf；冻结源 SHA256：`eac1d6e5b8f6335e4dcd74c8f8222b11af6708e77be03c7cfc0264285bbf0c31`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035216.pdf；冻结源 SHA256：`6e5b2f96da59704c5033f0b0b61a5c33a20641e626247e0422e2ed6bdc4777b6`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035275.pdf；冻结源 SHA256：`d15fa69d8ee9dd925c074f095de6c44b71573ddddf9f58ca3388a376c90c3d64`
- 官方核对来源：https://ethics.house.gov/wp-content/uploads/2023/12/CY-2017-Instruction-Guide-for-Financial-Disclosure-Statements-and-PTRs_0_0.pdf；冻结源 SHA256：`4943c3d9da30197bb24f9064415865b8902df0473feb69f7f84a5220d99b201c`

私有执行日志 SHA256：`0d7b764dab735e547ba93e4e4a42954db072f92fc70e852b328f659fbff25b11`
私有原始答案 SHA256：`85709d88cfd019e5e9ee777388f45abe3d2f618be465e00b477ed0a58e9400ee`

## 服务费用依据

费用分类：confirmed_free
- 免费规则：bargo-congress 读端点无需 Key 即可免费调用，仅按 IP 限速（keyless 每日 30 请求 / 100 行）；注册免费 Key 仅用于提高限额。
- 本次适用观察：本次所有对指定服务的调用均为免 Key GET（/members/ed-case、/trades 等），全部返回 HTTP 200，响应头显示 x-ratelimit-limit: 30、x-ratelimit-rows-limit: 100 的 keyless 档位；未注册账号、未提供付款、未使用 API Key。

模型用量、执行费用、验收费用以运行器记录和冻结价表计算为准；API 价估算不代表订阅账户实付。

## 本轮前提

本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
