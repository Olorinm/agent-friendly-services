公开证据节选；独立核验原文件 SHA256：d11317412c4a13b318406fbe0622fb77bb074f94556f288559ee14d67a22646a。原始材料私有保存，以下编辑不改验收结论。

# 核验摘要：Tavily keyless 免费适用与本次访问时间

## 免费规则来源
- 官方文档：https://docs.tavily.com/documentation/keyless （2026-10-08 读取）
- 官方文档释义：Search 与 Extract 允许无需账号或 Key 的免费访问，仍受速率限制。

## 本次适用证据（脱敏，取自本次真实请求）
- 搜索：`POST https://api.tavily.com/search`，请求头 `Content-Type: application/json`、`X-Tavily-Access-Mode: keyless`，无 `Authorization`；返回 HTTP 200，响应体已存 `execution/artifacts/search1.json`、`s_whatsnew.json`、`s_ext.json`、`s_bin.json`、`s_gil.json`。
- 提取：`POST https://api.tavily.com/extract`，同样 `X-Tavily-Access-Mode: keyless`、无 `Authorization`；返回 HTTP 200，响应体已存 `execution/artifacts/ex_free.json`、`ex_ext.json`、`ex_wn.json`、`ex_cmd.json`。
- 未使用任何付费 research/crawl/proxy 端点，未提供账号或密钥。

## 访问时间
- 本次运行时间窗口（运行回执）：started_at 2026-10-08T12:04:00Z，ended_at 2026-10-08T12:05:29Z。
- 各次工具调用另有逐次时间戳，可核对；执行者未单独产出访问时间文件。


搜索响应必要字段；源文件 s_whatsnew.json SHA256 1b577ea22709f881195373daddb8c14f3f304eb2fea2d184646d0e16e129b4f5

查询：What's New In Python 3.13 free-threaded CPython experimental
- What’s New In Python 3.13 — Python 3.14.8 documentation | https://docs.python.org/3/whatsnew/3.13.html
- Python experimental support for free threading — Python 3.13.16 documentation | https://docs.python.org/3.13/howto/free-threading-python.html
- Python support for free threading — Python 3.14.8 documentation | https://docs.python.org/3/howto/free-threading-python.html
- PEP 779: Criteria for supported status for free-threaded Python - PEPs - Discussions on Python.org | https://discuss.python.org/t/pep-779-criteria-for-supported-status-for-free-threaded-python/84319


搜索响应必要字段；源文件 s_ext.json SHA256 32835bdd005e8c46b6fb2fbee0aee774d9d977f2cd50c2552384977f52103221

查询：Python free-threading C extension compatibility howto
- Python support for free threading — Python 3.14.8 documentation | https://docs.python.org/3/howto/free-threading-python.html
- C API Extension Support for Free Threading — Python 3.14.8 documentation | https://docs.python.org/3/howto/free-threading-extensions.html
- How to get an extension module working w/ free threading? - Python Help - Discussions on Python.org | https://discuss.python.org/t/how-to-get-an-extension-module-working-w-free-threading/63653
- PEP 803 – “abi3t”: Stable ABI for Free-Threaded Builds | peps.python.org | https://peps.python.org/pep-0803
