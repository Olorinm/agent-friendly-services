已完成。通过 Tavily 官方 keyless Search API（`X-Tavily-Access-Mode: keyless`，基础调用 HTTP 200）发现来源，并用 Tavily Extract 读取 python.org 官方页面。结论如下，均来自 Python 3.13 官方文档。

## 1. 自由线程是否默认启用？
**否。** 3.13 的自由线程（GIL 禁用）是实验性功能，默认不启用，且需要**单独的可执行文件** `python3.13t` / `python3.13t.exe`；常规 3.13 发行版本身不具备该模式。

- What's New 3.13 原文：*"This is an experimental feature and therefore is not enabled by default. The free-threaded mode requires a different executable, usually called `python3.13t` or `python3.13t.exe`."*
- 依据：https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython

## 2. 如何启用
- **源码构建**：`./configure --disable-gil`
  - https://docs.python.org/3.13/using/configure.html#cmdoption-disable-gil
- **官方安装包**：3.13 起 Windows/macOS 官方安装器可选装 free-threaded 二进制（python.org/downloads）。
  - https://docs.python.org/3.13/howto/free-threading-python.html#installation
- **运行时开关**（在 free-threaded 构建内，GIL 默认关闭，可切换）：
  - `PYTHON_GIL=1` 强制开 GIL；`PYTHON_GIL=0` 强制关（需 `--disable-gil` 构建）。
  - `-X gil=0/1`，且**优先级高于** `PYTHON_GIL`。
  - 导入未声明支持自由线程的 C 扩展时，GIL 会**自动重新启用**并打印 warning；可用 `PYTHON_GIL=0` 或 `-X gil=0` 覆盖（风险自负）。
  - 依据：https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHON_GIL 、#cmdoption-X
- **识别方式**：`python -VV` / `sys.version` 含 "experimental free-threading build"；`sys._is_gil_enabled()`；`sysconfig.get_config_var("Py_GIL_DISABLED") == 1`。

## 3. 现有 C 扩展的兼容性限制
- **必须专门构建**：free-threaded build 的扩展、wheel、库需单独构建（文件名带 `t` 后缀，如 `python3.13t`）。
- **不支持 Limited C API / Stable ABI**（3.13 free-threaded build 当前不支持）。
- **必须显式声明支持**：multi-phase init 加 `Py_mod_gil` slot；single-phase init 调 `PyUnstable_Module_SetGIL()`（用 `#ifdef Py_GIL_DISABLED` 保护）。未声明者导入时触发上面的 GIL 回退。
- **线程安全约束**：直接访问结构体字段、`PyList_GET_ITEM`/`PyList_SET_ITEM` 等宏不安全；borrowed reference API 不安全，需改用 strong ref 版（如 `PyList_GetItemRef`、`PyDict_GetItemRef`）；`PyDict_Next` 需用 `Py_BEGIN_CRITICAL_SECTION` 保护。
- **内存域强制**：Python 对象必须走 object domain（`PyObject_Malloc`），缓冲区用 `PyMem_Malloc`——从"最佳实践"变为硬性要求。
- **内部状态**：原先靠 GIL 保护的缓存/全局状态需自行加锁或改线程本地存储。
- **Windows**：从源码构建扩展时须手动定义 `Py_GIL_DISABLED=1`。
- **性能代价**：3.13 free-threaded build 单线程性能约下降 40%（pyperformance）。
- 依据：https://docs.python.org/3.13/howto/free-threading-extensions.html 、https://docs.python.org/3.13/howto/free-threading-python.html#known-limitations

## 接入说明
- 使用 Tavily 官方 keyless Search/Extract API，无账号、无 Key；配置已存在于持久位置 `/home/node/service-tools/service-config.json`（本轮无需新建，也无需注册）。
- 未使用付费研究/代理端点，遵守官方限流。

**仍未完成/注意**：官方明确 3.13 该特性为实验性；升级前须核实你的具体 C 扩展是否已发布带 `t` 后缀的 free-threaded wheel 并声明 `Py_mod_gil`，否则导入时会自动回退到 GIL（失去自由线程收益）。搜索/提取原始结果存于本题工作目录（`search1.json`、`s_*.json`、`page_*.txt`），不输出任何密钥。