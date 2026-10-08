接入完成，Firecrawl 匿名 Search API 实测可用。

**搜索实测**
- 查询内容：`how to bake sourdough bread`（limit=3）
- 结果 1：`Sourdough Bread: A Beginner's Guide - The Clever Carrot`
  - https://www.theclevercarrot.com/2014/01/sourdough-bread-a-beginners-guide/
- 结果 2：`How To Bake Sourdough Like A Pro - YouTube`
  - https://www.youtube.com/watch?v=7Un6mV2YQ54
- 返回 `success:true`，`creditsUsed:2`，HTTP 200。

**完成的接入步骤**
1. 阅读官方文档 https://docs.firecrawl.dev/features/search，确认匿名调用方式（`POST https://api.firecrawl.dev/v2/search`，无需 `Authorization`）。
2. 用 curl 直接发起真实搜索，验证匿名免费入口连通（Python 与 sourdough 两次真实搜索均成功）。
3. 保存连接配置到持久目录，并写了可复用查询脚本到本题工作目录。

**已有账号来源**：无。ENVIRONMENT.md 未提供账号、API key、支付方式，本轮仅用官方匿名入口，未注册、未购买、未绑卡。

**阻碍/限制**
- 匿名额度受“每 IP 每日请求数 + credits”双上限约束且数值未公开，无法预知剩余额度；本轮与另一匿名服务共享出口 IP。
- 未做任何绕过限流/换 IP 操作，未遇到验证码或封禁，两次调用均正常。

**配置与产物位置**
- 连接配置（无秘密，纯匿名）：`/home/node/service-tools/service-config.json`
- 通用依赖目录：`/home/node/service-tools/installed-tools/`（未装额外依赖，仅用系统 curl）
- 查询脚本：`./fc_search.sh`；原始结果：`./raw-search-result.json`（本题工作目录）
- 本轮无任何密钥或私有凭据生成，故无需隐藏私有文件。