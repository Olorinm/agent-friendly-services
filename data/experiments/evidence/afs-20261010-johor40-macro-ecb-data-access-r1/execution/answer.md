Basic call works. Now testing the documented query methods sequentially (2s spacing).
All query methods verified. Now creating a reusable script with caching and enforcing the 2s single-threaded policy.
Everything works, including cache. Writing a concise result note in the working directory.
已接通，可用。

**结果**：ECB Data Portal 官方 API 免账号/Key，全部指定方式实测 HTTP 200——单序列 CSV、通配符、日期区间、宏观指标（欧元区 HICP）、SDMX-JSON、dataflow 列表与结构元数据。无阻碍。

**保存的配置/产物**：
- 通用连接配置：`/home/node/service-tools/service-config.json`（base_url、UA、限流、Accept 头、参数说明、已验证项）
- 复用脚本：`ecb_query.py`（自动 ≥2s 单线程限流 + 相同请求磁盘缓存）
- 样本：`raw/`；缓存：`cache/`；说明：`RESULT.md`

用法：`python3 ecb_query.py describe` 或 `python3 ecb_query.py`（自检）。署名 © European Central Bank, ECB Data Portal，改动需说明。