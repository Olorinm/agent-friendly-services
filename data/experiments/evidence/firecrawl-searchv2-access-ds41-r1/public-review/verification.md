公开证据节选；独立核验原文件 SHA256：5e3e4eab73bd8755e4c63d5783953aa2dac13f54af7226620e7220922bb8ff78。原始材料私有保存，以下编辑不改验收结论。

# Firecrawl 匿名搜索接入 — 验收核验摘要（脱敏）

来源：本次执行采集副本 `execution/`（工具记录预览见私有 `review-packet/`）。
未包含任何账号、密钥或私有凭据；本次调用为无认证匿名请求。

## 指定服务与入口
- 服务：firecrawl
- 入口：`POST https://api.firecrawl.dev/v2/search`
- 认证：匿名，无 `Authorization` 头；未注册、未购买、未绑卡
- 请求体示例：`{"query": "<query>", "limit": 3}`

## 实际搜索调用（真实响应）
1) 首次验证（bash curl，带 HTTP 状态）
   - 查询：`python programming language official website`
   - 结果：`success:true`，`creditsUsed:2`，`HTTP_STATUS:200`
   - 结果 1：`Python.org` — https://www.python.org/

2) 交付搜索（`./fc_search.sh "how to bake sourdough bread" 3`，保存到 raw-search-result.json）
   - 查询：`how to bake sourdough bread`（limit=3）
   - 响应字段：`success:true`，`creditsUsed:2`
   - 结果 1：`Sourdough Bread: A Beginner's Guide - The Clever Carrot`
     https://www.theclevercarrot.com/2014/01/sourdough-bread-a-beginners-guide/
   - 结果 2：`How To Bake Sourdough Like A Pro - YouTube`
     https://www.youtube.com/watch?v=7Un6mV2YQ54
   - 结果 3：`Beginner's Guide to Making Sourdough Bread - Allrecipes`
     https://www.allrecipes.com/article/how-to-make-sourdough-bread/

答复 `execution/answer.md` 给出的查询、结果 1/2 标题与链接、`success:true`、`creditsUsed:2`、HTTP 200 与实际响应一致。

## 本地可复用配置（持久目录）
- 位置：`/home/node/service-tools/service-config.json`（执行环境持久目录）
- 保存动作：write 成功；随后 `ls -la` 显示文件存在（930 字节）
- 内容（无秘密）：service=firecrawl；endpoint=https://api.firecrawl.dev/v2/search；method=POST；
  auth.mode=anonymous（header/api_key 均为 null）；content_type=application/json；
  request_example={query,limit}；docs=https://docs.firecrawl.dev/features/search
- 可复用查询脚本：`./fc_search.sh`（本题工作目录，非持久目录）

## 免费依据（本次适用）
- 规则来源：`frozen-execution/ENVIRONMENT.md` 指定“官方匿名 REST Search API … 仅用官方免费匿名入口”，
  且说明匿名免费额度受每 IP 每日请求数与 credits 双上限约束；官方文档
  `https://docs.firecrawl.dev/features/search` 说明无需 API key 即可开始使用。
- 本次观察：两次匿名请求均返回 `success:true`、`creditsUsed:2`，无认证头、无账号与支付；未出现计费或付费要求。

## 人工介入
- 本次执行未观察到任何人工步骤：无注册、无授权申请、无人工审批；全程由执行 Agent 自助完成。

## 阻碍/限制
- 匿名免费额度上限数值未公开，无法预知剩余额度；与另一匿名服务共享出口 IP。未做任何绕过限流操作，未遇验证码或封禁。


本轮按相同web-search-001/v2任务比较，旧v1不合并统计。接入和业务均为匿名公开入口，额度余量未知，同一服务器出口IP；持久化配置经检查未含业务答案。执行原始返回与三份事前独立官方参考均私有保留；来源链由独立验收核对，没有额外最低页面数要求。单次试跑只说明这次任务，不是普遍可靠性排名。
