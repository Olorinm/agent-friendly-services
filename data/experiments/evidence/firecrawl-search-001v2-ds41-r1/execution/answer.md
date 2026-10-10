搜索已完成，官方 3.13 页面已核对。写入答案文件：
已用 Firecrawl 匿名 Search API 检索 docs.python.org 并核对官方 3.13 页面，答案存于 `answer.md`。要点：

**1. 是否默认启用**：否。自由线程是 3.13 实验性特性，「not enabled by default」，需要单独可执行文件 `python3.13t`。

**2. 如何启用**
- 安装：官方 Windows/macOS 安装器的可选 free-threaded 组件，或源码 `--disable-gil` 构建。
- 运行时：`PYTHON_GIL` 环境变量或 `-X gil`（`-X gil=0` 关、`=1` 开）。
- 识别：`python -VV`/`sys.version` 含 "experimental free-threading build"；`sys._is_gil_enabled()`；`sysconfig.get_config_var("Py_GIL_DISABLED")`。C 扩展安装需 pip ≥ 24.1。

**3. C 扩展兼容性限制**
- 必须专为 free-threaded 构建编译（`t` 后缀 wheel），不能复用普通二进制。
- 须显式声明支持：多阶段用 `Py_mod_gil` slot（`Py_MOD_GIL_NOT_USED`），单阶段用 `PyUnstable_Module_SetGIL()`；否则导入会自动重开 GIL 并告警。
- 当前**不支持 Limited C API / stable ABI**，需单独 wheel。
- 借用引用（如 `PyList_GetItem`）在并发修改下不安全，改用 `PyList_GetItemRef`/`PyDict_GetItemRef` 等强引用版本；`PyList_GET_ITEM` 等宏无锁；`PyDict_Next` 需 `Py_BEGIN_CRITICAL_SECTION`。
- Python 对象必须用 object 域分配；线程状态/GIL API 仍需使用；扩展内部共享状态需自行加锁。
- Windows 从源码构建扩展需手动定义 `Py_GIL_DISABLED=1`。
- 3.13 单线程性能约降 40%。

**官方链接**
- https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython
- https://docs.python.org/3.13/howto/free-threading-python.html
- https://docs.python.org/3.13/howto/free-threading-extensions.html
- PEP 703：https://peps.python.org/pep-0703/

说明：匿名 Firecrawl 免费额度受每 IP 每日请求数与 credits 双上限；本轮只检索并读取官方页面，未注册/未付费。