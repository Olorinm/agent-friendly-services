已实际调用 Firecrawl 无密钥搜索接口完成，依据均为 **Python 3.13 官方文档**。

1. **默认不启用自由线程。** 普通构建仍默认启用 GIL；3.13 的自由线程属于实验性、可选构建。[官方说明](https://docs.python.org/3.13/howto/free-threading-python.html)

2. **启用方式：** 在官方 macOS／Windows 安装器中选装自由线程版本，或源码编译时使用 `./configure --disable-gil`。该构建默认关闭 GIL；可用 `PYTHON_GIL=0` 或 `-X gil=0` 强制关闭，值 `1` 则开启。关闭选项**仅适用于自由线程构建**。可用 `sys._is_gil_enabled()` 检查实际状态。[安装与检查](https://docs.python.org/3.13/howto/free-threading-python.html)、[运行参数](https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHON_GIL)

3. **现有 C 扩展不能直接假定兼容。** 必须为自由线程专门编译、提供独立 wheel；3.13 自由线程构建不支持 Limited C API／Stable ABI。扩展必须明确声明支持，否则导入时会警告并重新开启 GIL；还需处理共享状态、无锁宏和借用引用等线程安全问题。[官方扩展适配指南](https://docs.python.org/3.13/howto/free-threading-extensions.html)

证据已保存，含请求方法、URL、参数、原始响应、网页全文、UTC 访问时间及 SHA-256：

- [完整证据说明](evidence/README.md)
- 搜索请求：[02](evidence/02-firecrawl-search-request.json)、[04](evidence/04-firecrawl-search-request.json)；真实响应：[02](evidence/02-firecrawl-search-response.json)、[04](evidence/04-firecrawl-search-response.json)
- [结论—原文—搜索发现位置索引](evidence/source-map.json)

三个引用页面 URL 均出现在真实搜索响应中；扩展指南和运行参数页来自响应正文中的官方链接，具体位置已记录。