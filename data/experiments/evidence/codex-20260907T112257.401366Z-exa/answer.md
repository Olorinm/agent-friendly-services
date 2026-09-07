已实际使用指定 Exa MCP 完成检索；下列三个官方 URL 均出现在其真实搜索响应中。

1. **默认不启用。** Python 3.13 的自由线程仍属实验性功能，普通升级不会自动关闭 GIL，需要独立的自由线程解释器。[官方依据：3.13 新变化](https://docs.python.org/zh-cn/3.13/whatsnew/3.13.html)

2. **启用方式：** 选装官方 Windows/macOS 安装器中的自由线程组件，或使用 `--disable-gil` 从源码构建，然后运行 `python3.13t app.py`。该构建可用 `-X gil=0` 显式关闭 GIL、`-X gil=1` 重新启用。[官方依据](https://docs.python.org/zh-cn/3.13/whatsnew/3.13.html) 导入应用依赖后，可用 `sys._is_gil_enabled()` 检查实际状态；`False` 表示 GIL 已关闭。[官方自由线程指南](https://docs.python.org/zh-cn/3.13/howto/free-threading-python.html)

3. **C 扩展兼容性：** 必须针对自由线程构建单独编译、提供对应 wheel；3.13 自由线程构建**不支持 Limited C API／Stable ABI**。扩展还需处理共享状态、部分宏、借入引用等线程安全问题，并通过 `Py_mod_gil` 或 `PyUnstable_Module_SetGIL()` 声明支持；否则通常会警告并重新启用 GIL。[官方 C 扩展指南](https://docs.python.org/zh-cn/3.13/howto/free-threading-extensions.html) 因此，重新编译或强制关闭 GIL，不能代替线程安全适配。

证据已保存至 `evidence/`：

- [证据索引](evidence/README.md)：搜索请求与原始响应为 `12-search-zh313.*`、`15-search-zh313-extensions.*`；引用网页为 `16-*`、`17-*`、`18-*`。
- [逐条依据、访问时间和 SHA-256](evidence/manifest.json)；[离线核验结果](evidence/verification.json)：通过。