公开证据节选；独立核验原文件 SHA256：3bf97dd692769c92edfc641d3254961a1105a943856f2e59a082a712bfd198dd。原始材料私有保存，以下编辑不改验收结论。

# 核验摘要：Exa 搜索响应摘要与最终引用对照（脱敏）

本文件是本次运行工具输出的必要业务字段摘录，非原始会话；无账号、密钥、会话标识。

## 1. 当次对指定服务（Exa 匿名 MCP，https://mcp.exa.ai/mcp）的真实调用
- `web_search_exa` "Python 3.13 free-threading build official documentation" → 返回含：
  - https://docs.python.org/3/howto/free-threading-python.html （标题 "Python support for free threading — Python 3.14.7/3.14.8 documentation"）
  - https://docs.python.org/3/whatsnew/3.13.html （标题 "What's New In Python 3.13 — Python 3.14.5 documentation"）
  - https://github.com/python/cpython/blob/main/Doc/howto/free-threading-python.rst
  - https://blog.python.org/2024/10/python-3130-final-released/
  - https://docs.python.org/3/_sources/howto/free-threading-python.rst.txt
- `web_search_exa` "C API extension support for free threading ..." → 返回含：
  - https://docs.python.org/3/howto/free-threading-extensions.html
  - https://docs.python.org/3/c-api/extension-modules.html
  - https://github.com/python/cpython/issues/116322
  - https://py-free-threading.github.io/porting-extensions/
  - https://discuss.python.org/t/concerns-about-pyunstable-module-setgil/89374
- `web_fetch_exa` 抓取 https://docs.python.org/3/howto/free-threading-python.html（标题 3.14.7）与 .../free-threading-extensions.html（标题 3.14.6），内容已存 execution/artifacts/raw_ft_python.json、raw_ft_ext.json。
- `web_search_exa` "site:docs.python.org free-threading limitations ..." → 返回含：
  - https://docs.python.org/3/howto/free-threading-python.html
  - https://docs.python.org/3/howto/free-threading-extensions.html
  - https://docs.python.org/3.15/howto/abi3t-migration.html
  - https://docs.python.org/3.16/howto/abi3t-migration.html
  - https://docs.python.org/3/builtins/threadsafety.html
  - https://docs.python.org/3/c-api/threads.html

## 2. Q1（默认状态）在被返回的官方页面中的原文
来源 docs.python.org/3/whatsnew/3.13.html（响应内标题为 "What's New In Python 3.13"）：
独立复核释义：返回的 Python 3.13 更新说明明确表示自由线程为实验性、默认未启用，需要单独的自由线程可执行文件。原文保留私有，来源哈希可核验。

同一响应内 free-threading-python.html 提供安装（官方安装器可选、`--disable-gil`）、运行期 `PYTHON_GIL` / `-X gil`、检测方法（`python -VV`、`sys._is_gil_enabled()`、`sysconfig.get_config_var("Py_GIL_DISABLED")`）。free-threading-extensions.html 提供 C 扩展须显式声明（`Py_mod_gil` / `PyUnstable_Module_SetGIL`）、否则警告并重开 GIL、不支持 Limited C API/stable ABI、Windows 需手动 `Py_GIL_DISABLED=1`、线程安全例外等。三个结论均能在当次搜索响应内容中找到依据。

## 3. 最终答复引用 URL 与当次响应 URL 对照
| 答复 §4 引用 | 当次搜索响应中出现的对应页面 | 说明 |
|---|---|---|
| https://docs.python.org/3.13/whatsnew/3.13.html | https://docs.python.org/3/whatsnew/3.13.html | 同一 "What's New in Python 3.13" 文档，版本前缀不同 |
| https://docs.python.org/3.13/howto/free-threading-python.html | https://docs.python.org/3/howto/free-threading-python.html | 同名 howto；响应页面标题为 3.14.7 |
| https://docs.python.org/3.13/howto/free-threading-extensions.html | https://docs.python.org/3/howto/free-threading-extensions.html | 同名 howto；响应页面标题为 3.14.6 |
| https://peps.python.org/pep-0703/ | 未在搜索响应中出现 | 仅 curl 返回 200 |

## 4. 版本对应证据
- 未见任何重定向捕获，也无 `/3/` 与 `/3.13/` 内容比对记录。
- 唯一"版本对应"操作是用 curl 对 /3.13/whatsnew/3.13.html、/3.13/howto/free-threading-python.html、/3.13/howto/free-threading-extensions.html、peps.python.org/pep-0703/ 取 HTTP 状态码，均返回 200；未读取页面内容。
