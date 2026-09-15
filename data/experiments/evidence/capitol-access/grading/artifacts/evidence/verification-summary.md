数据来源：[CapitolExposed](https://www.capitolexposed.com/)。本页仅展示核验摘要。

# 验收摘要 — financial-access-001/v1（capitol-exposed 接入）

## 核对内容（不含原始数据行，不重构记录）

1. **指定方式真实调用**：执行记录显示对指定入口 `https://www.capitolexposed.com/api/v1` 的直连 curl GET（`/stats`、`/members?chamber=senate&party=D`、`/search`、`/members/nancy-pelosi/trades`）均返回 HTTP 200，响应为文档声明的 `{status, data, meta, citation}` 信封格式；未使用任何聚合替代服务或模型记忆。
2. **真实金融数据（非仅文档/健康检查）**：`/members/nancy-pelosi/trades` 返回 STOCK Act 申报明细（交易日期、金额区间、owner、指向 House Clerk 原始 PTR PDF 的出处链接）；当次响应已保存为交付物 `execution/artifacts/api-probe-trades.json`（sha256 `bdfb9fe9ae5f02682b7ec569a4cfd0c25fa9c1acf72f3961bbb9a2b8db64eab8`，与索引一致）。原始数据行按公开证据要求不摘录。
3. **配置可复用**：执行者向持久目录 `/home/node/service-tools/service-config.json` 写入连接配置（base_url、免 Key 认证说明、已验证端点、限流与署名要求），写入工具返回成功；运行器采集的 retained-files.json 列出该文件已保留，可供新会话使用。该持久目录属执行环境，验收环境不挂载，以采集记录为准。
4. **接入门槛**：官方文档（执行中抓取 https://www.capitolexposed.com/api-docs ）声明免费层无需认证、按 IP 限流；本轮所有请求均未携带 API Key，未注册、未付款，符合授权范围（本轮亦禁止注册）。无人工介入步骤。
5. **限流头佐证**：`x-ratelimit-limit: 60` 与任务参考中"免 Key 读取端点 60 次/分/IP"的免费规则一致。
6. **独立复核（验收环境现场）**：本验收环境直接 GET `/stats`（免 Key）返回 HTTP 200，`member_count=532`、`trade_count=36992`，与执行当次捕获一致（时间戳不同），确认服务真实可用、免费入口无需凭据。
7. **运行配置匹配**：回执显示 model `glm-5.3-flash`（reasoning high）、harness OpenCode 1.18.29，运行 09:14:32–09:16:51 UTC（约 139 秒 < 600 秒上限），exit_code 0，未超时；与测评配置一致。

## 来源与署名

- 官方接入文档：https://www.capitolexposed.com/api-docs（免费层免 Key、按 IP 限流；署名 "Public Records — Attribution Requested"）
- 任务参考免费规则：免 Key member/trade 列表端点 60 次/分/IP；免费读取、要求署名。
- 关键交付物哈希：`execution/answer.md` sha256 `6fd82b84d0f89b69a96c06a8be7ad7652149002b6ff216e24c8568fa7f133ddd`；`execution/artifacts/api-probe-trades.json` sha256 `bdfb9fe9ae5f02682b7ec569a4cfd0c25fa9c1acf72f3961bbb9a2b8db64eab8`。
