MCP 接入成功。现在执行官方来源搜索。
已完成 exa 匿名远程 MCP 接入（tools: `web_search_exa`/`web_fetch_exa`），搜索与抓取的原始记录位于本题目录 `search1.json`、`search2.json`、`fetch1.json`，调用脚本 `mcp_call.py`。结论如下（均来自 python.org 官方页面，链接已逐条验证 200）：

## Python 3.13 自由线程（free-threading / 无 GIL）

**1. 是否默认启用：否**
- 3.13 起 CPython 提供**实验性** free-threaded 构建，GIL 被禁用，但“is an experimental feature and therefore **is not enabled by default**”。
- 需要单独的构建与可执行文件，通常叫 `python3.13t`（Windows 为 `python3.13t.exe`）。

**2. 如何启用**
- **安装**：官方 Windows/macOS 安装器可选装 free-threaded 二进制；其他平台/源码构建时使用 configure 选项 `--disable-gil`。
- **运行时开关**：free-threaded 构建可用环境变量 `PYTHON_GIL` 或命令行 `-X gil=1`（重新启用 GIL）。
- **识别是否生效**：`python -VV` / `sys.version` 含 “experimental free-threading build”；`sys._is_gil_enabled()` 判断当前进程 GIL 是否真的关闭；`sysconfig.get_config_var("Py_GIL_DISABLED") == 1` 表示该构建支持自由线程（推荐用于构建配置判断）。

**3. 现有 C 扩展的兼容性限制**
- 扩展必须**专门为该构建编译**：wheels/共享库/二进制带 `t` 后缀，需单独发布；安装 C 扩展需 pip ≥ 24.1。
- 扩展须**显式声明支持无 GIL**：多阶段初始化（`PyModuleDef_Init()`）加 `Py_mod_gil` 槽；单阶段初始化（`PyModule_Create()`）调用 `PyUnstable_Module_SetGIL()`。未声明者导入时会**打印警告并自动重新启用 GIL**（除非已显式用 `PYTHON_GIL`/`-X gil=0` 关闭）。
- **不支持 Limited C API 与 stable ABI**（需 `py_limited_api` 退出）。
- **内存分配域**：Python 对象只能用 object domain 分配，缓冲区改用 `PyMem_Malloc()`。
- 需自行加锁（critical sections），跨线程访问 frame 对象不安全、共享同一迭代器不安全等。

**官方页面链接**
- What's New In Python 3.13：https://docs.python.org/3.13/whatsnew/3.13.html
- Python 自由线程使用指南：https://docs.python.org/3.13/howto/free-threading-python.html
- C API 扩展对自由线程的支持：https://docs.python.org/3.13/howto/free-threading-extensions.html
- Python 3.13.0 发布公告（Python Insider，官方 blog）：https://blog.python.org/2024/10/python-3130-final-released/

升级提示：默认 3.13 仍行为不变；仅在显式选用 `python3.13t`（或 `--disable-gil` 构建）时才进入无 GIL 模式，且需确认依赖的 C 扩展已标记支持自由线程，否则会自动回退为启用 GIL。