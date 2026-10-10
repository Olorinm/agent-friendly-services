# 独立验收的公开摘要

结论：completed
独立验收确认本题全部用户要求满足：指定服务提供的两名成员数据完整，逐笔滞后天数与汇总统计正确，按官方提交日期筛选并附可核对的原始申报出处。

本文件由总控从已完成的独立验收中删减整理，仅作为发布前摘要；未重新判分。原始答案、交易行、完整日志和完整验收依据私有保存。

原始独立验收 SHA256：`7094c74600279184468166e7ab9edc49c7d4395db4808cf8ce6a85ab4fba5ad9`

## 核对项目

- 通过：核心业务数据来自指定服务 bargo-congress API（keyless 直连），未用其他聚合服务或模型记忆替代
- 通过：8 月官方提交窗口内匹配交易完整且与独立冻结参考一致（含排除项处理）
- 通过：逐笔自然日差、笔数、最短与最长间隔计算正确，汇总无编造
- 通过：使用官方提交日而非通知日/平台上架日，并附原始申报出处
- 通过：遵守服务免费条款与署名要求：keyless 免费额度内调用，注明数据服务署名

## 来源与留底

- 数据服务：Bargo，https://www.bargo.ai/free-apis/congress
- 服务条款：https://www.bargo.ai/free-apis/terms
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip；冻结源 SHA256：`75bc79034ec5b3c6d84385442377c6de56c54291ca799e4f64b6c60196d9a78c`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf；冻结源 SHA256：`6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035106.pdf；冻结源 SHA256：`eac1d6e5b8f6335e4dcd74c8f8222b11af6708e77be03c7cfc0264285bbf0c31`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035216.pdf；冻结源 SHA256：`6e5b2f96da59704c5033f0b0b61a5c33a20641e626247e0422e2ed6bdc4777b6`
- 官方核对来源：https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035275.pdf；冻结源 SHA256：`d15fa69d8ee9dd925c074f095de6c44b71573ddddf9f58ca3388a376c90c3d64`
- 官方核对来源：https://ethics.house.gov/wp-content/uploads/2023/12/CY-2017-Instruction-Guide-for-Financial-Disclosure-Statements-and-PTRs_0_0.pdf；冻结源 SHA256：`4943c3d9da30197bb24f9064415865b8902df0473feb69f7f84a5220d99b201c`

私有执行日志 SHA256：`2783375485d16e1c845add363e34fd1a92898b008447683b3ef4357374094c19`
私有原始答案 SHA256：`05ac2f6496f08cb5911f86f899d6ac91ed6ec92836bbb17429627ac6f0bdd113`

## 服务费用依据

费用分类：confirmed_free
- 免费规则：bargo-congress 读端点无需 Key 即可免费使用，仅按 IP 限速（keyless 每日 30 请求/100 行）；免费 Key 仅用于提高限额与解锁 MCP，非必需
- 本次适用观察：本次 2 次业务调用均为无 Key 直连（service-config.json auth.mode=keyless、api_key=null），HTTP 200 返回完整数据并带 X-RateLimit-Limit: 30 / X-RateLimit-Rows-Limit: 100 响应头；全程无注册、无支付方式

模型用量、执行费用、验收费用以运行器记录和冻结价表计算为准；API 价估算不代表订阅账户实付。

## 本轮前提

本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
