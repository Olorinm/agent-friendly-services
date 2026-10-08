已完成调研（通过 Exa 官方匿名 MCP 发现来源，仅用 python.org 等官方页面）。完整结果：`[WORKSPACE]/result.md`。

## 1. 3.13 自由线程默认启用吗？
**不。** 属**实验性**特性，官方原文：“This is an experimental feature and therefore is **not enabled by default**.”。默认 `python3.13` 仍带 GIL；自由线程是另一个独立构建/可执行文件，通常叫 `python3.13t`。

## 2. 如何启用
- **安装**：官方 Windows/macOS 安装器可选安装 free-threaded 二进制；源码构建用 `./configure --disable-gil`。
- **运行期开关**：`PYTHON_GIL` 环境变量或 `-X gil`（`=0` 禁用、`=1` 启用）。
- **检测**：`python -VV`/`sys.version` 含 “experimental free-threading build”；`sys._is_gil_enabled()`；`sysconfig.get_config_var("Py_GIL_DISABLED")==1`。
- C 侧宏 `Py_GIL_DISABLED`（自由线程构建中为 1）。

## 3. 现有 C 扩展的兼容性限制
- **必须为自由线程单独重建**（不能与常规构建通用）；装 C 扩展需 **pip ≥ 24.1**。
- 必须**显式声明**支持，否则导入会打印警告并**自动重新启用 GIL**：
  - 多阶段初始化 → 加 `Py_mod_gil` slot = `Py_MOD_GIL_NOT_USED`；
  - 单阶段初始化 → `PyUnstable_Module_SetGIL(m, Py_MOD_GIL_NOT_USED)`（用 `#ifdef Py_GIL_DISABLED` 保护）。
- **不支持 Limited C API / stable ABI（abi3）**。
- Windows 从源码构建扩展需**手动定义 `Py_GIL_DISABLED=1`**。
- C API 线程安全例外：直接访问结构体字段、访问宏（`PyList_GET_ITEM` 等）、借用引用均不安全；`PyDict_Next()` 不加锁需 `Py_BEGIN_CRITICAL_SECTION`；Python 对象必须用 object 分配域。
- 官方警告：实验性，**expect some bugs and a substantial single-threaded performance hit**；部分第三方扩展会重新启用 GIL。

## 4. 官方依据
- https://docs.python.org/3.13/whatsnew/3.13.html （§Free-threaded CPython）
- https://docs.python.org/3.13/howto/free-threading-python.html
- https://docs.python.org/3.13/howto/free-threading-extensions.html
- https://peps.python.org/pep-0703/

未做本地实测安装（本轮仅授权免费匿名检索，未注册/付款）。