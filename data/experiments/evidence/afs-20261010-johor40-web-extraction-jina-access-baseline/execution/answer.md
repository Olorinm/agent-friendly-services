Now I'll check Jina Reader's official docs and make the extraction call.
Extraction succeeded (HTTP 200). Now saving the persistent config and evidence.
接通成功。

**提取结果**（`https://r.jina.ai/https://example.com/`，HTTP 200，1 次请求）
- 页面标题：**Example Domain**
- 内容概述：example.com 是专供文档示例使用的域名，无需授权即可引用，且明确声明它并非一项服务、不建议用于测试或监控目的。

**已保存配置**
- `/workspace/service-config.json`（通用连接配置，持久保留；无密钥，匿名免费入口）
- 原始证据（私有）：任务目录下 `evidence_example_com_body.txt` / `evidence_example_com_headers.txt`

**接入步骤**
1. 无需注册：Jina Reader 匿名免费入口直接可用，无 Key、账号或付款。
2. 在目标 URL 前拼接 `https://r.jina.ai/` 发起 GET，例如 `https://r.jina.ai/https://example.com/`。
3. 设置具名 `User-Agent`（本环境要求 `agent-friendly-services/20261010`）与 `Accept: text/plain`（或 `application/json` 取结构化字段）。
4. 从响应解析 `Title:`、`Markdown Content:` 等字段；响应头 `x-usage-tokens`、`x-ratelimit-*` 可用于计量。

**门槛与限制**
- 匿名免费档限 **20 RPM**（实测响应头 `x-ratelimit-limit: 20, 20;w=60`），因此按协议单线程、相邻请求间隔 ≥20s、每阶段最多 6 次尝试。
- 默认 **5 分钟缓存**，重复同一 URL 会命中缓存（按规则保留默认缓存，未强制 fresh）；首次请求有约数秒冷启动延迟。
- 无人工介入、无额外申请、未触发 403/429 或付费要求，未注册/未付款，符合授权范围。

本次仅 1 次提取请求，未达任何保护上限。