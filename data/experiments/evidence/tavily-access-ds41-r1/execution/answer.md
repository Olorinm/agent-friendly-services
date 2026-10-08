已完成接入并验证可用。

**接入步骤（全部自助完成，无需人工）**
1. 阅读官方 keyless 文档：https://docs.tavily.com/documentation/keyless
2. 确认免 Key 调用方式：`POST https://api.tavily.com/search`，请求头加 `X-Tavily-Access-Mode: keyless`（无账号、无 API Key、无支付）。
3. 用 curl 实际发起真实搜索并读取返回网页内容。
4. 将连接配置写入持久目录。

**真实搜索结果（示例）**
- 查询：`latest stable Python release version 2025`
  - 标题：*Latest Python Version (2025) – What's New in Python 3.14?*
  - 链接：https://www.liquidweb.com/blog/latest-python-version
- 查询：`best time to visit Japan cherry blossom`
  - 标题：*The Best Time to Visit Japan for Cherry Blossoms Revealed*
  - 链接：https://www.theinvisibletourist.com/best-time-to-visit-japan-for-cherry-blossoms

两次均 HTTP 200，返回标准 Tavily 结果 schema，确认可用。

**已保存的本地配置**
- `/home/node/service-tools/service-config.json`（端点、方法、必需请求头、默认参数；keyless 无密钥，故无秘密文件）
- 通用依赖目录：`/home/node/service-tools/installed-tools`（本次仅用系统自带 curl，无需安装）
- 任务脚本/结果（仅本题目录，不持久）：`tavily-search.sh`、`search-result.json`

**阻碍/说明**
- 无账号来源（ENVIRONMENT 未提供账户），官方 keyless 模式本身也不需要注册，故未创建任何账号。
- 仅使用免费匿名限流额度，未使用需付费/需 Key 的 `/crawl`、`/map`、`/research` 端点；未付款、未写远端数据、未发消息。
- 若后续触发限流，官方会返回自然语言提示，可选注册免费 Key（1000 credits/月），配置已预留 `Authorization: Bearer` 升级说明。