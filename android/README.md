# 第七日的勇者 V0.3 · Android 封装工程

这是以最终 `SeventhDay.html` 为内容的原生 Android WebView 外壳，不增加剧情或玩法。当前仓库**不含已构建 APK**：本次执行环境没有 Android SDK、Gradle、aapt/d8 或可用下载通道，不能真实编译与真机验收。

## 在已有 Android Studio 的电脑生成安装包

1. 用 Android Studio 打开本目录 `android/`，安装 Android SDK Platform 35 和 Build Tools 34.0.0 或更高版本，使用 JDK 17。工程指定 Android Gradle Plugin 8.7.3、Gradle 8.9；若 Android Studio提示缺少 Gradle，选择本机安装的 Gradle 8.9，或先生成该版本的 wrapper。
2. 选择 **Build > Build Bundle(s) / APK(s) > Build APK(s)**，即 `:app:assembleDebug`。产物在 `app/build/outputs/apk/debug/app-debug.apk`，它是调试签名包，可安装试玩，不用于正式商店发布。
3. 若命令行工具和 SDK 已配置，也可以执行 `bash build-apk.sh`。每次构建前执行 `python3 sync_game.py`，保证资源来自同目录上层的最终 V0.3 HTML。独立复制本文件夹时，已同步的 `app/src/main/assets/SeventhDay.html` 可以直接构建；同步脚本需要原项目的上级 HTML。

## 封装行为

- 唯一内容通过 `https://appassets.androidplatform.net/assets/SeventhDay.html` 的 HTTPS 同源地址由内置资源拦截提供；应用不声明 INTERNET 权限，也不加载远程资源。DOM Storage 保留图鉴、旅程档案与音频偏好。
- Android 系统文件选择器提供 JSON 存档导入和导出；资产 HTML 只在导出函数添加 `AndroidBridge.saveJson`，其余内容和 Web 版逐字节相同。导出的 JSON仍为本局路径存档，不是整个旅程档案。
- 继续遵守用户手势音频政策，WebView 不提前播放 BGM。按钮与触屏由现有 V0.3 HTML 提供。
- 最低 Android 8.0（API 26），目标 API 34。未在真机上测试，不保证所有厂商 WebView 的音频或文件选择器表现。

`python3 tests/check_wrapper.py` 验证资产来源、导出适配、离线配置和存档入口；这属于静态检查，不是 APK 安装测试。正式发布需要自有签名密钥、真机七日流程和导入导出/背景音/横竖屏检查。
