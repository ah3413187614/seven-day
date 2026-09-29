# CODEX_HANDOFF · V0.4

## 当前事实

根目录`SeventhDay.html`、`dist/SeventhDay.html`与项目ZIP里的网页逐字节一致。Android内置网页只在导出存档函数增加`AndroidBridge.saveJson`，其余内容相同，且包含同一`GAME_BUILD_ID`。当前构建标识以`tests/final-build-manifest-v04.json`为准。唯一发布入口：`python scripts/release_v04.py`。**先改源码，再运行该入口；不要手改HTML或Android资产。**

89节点、356行动、24弧光、10项Truth；首周目/NG+各16,384路径，跨模式166个可达称号。`data/choices.json`和`data/endings.json`的条件效果保持上一提交原样。状态与存档仍用`seventh-day-v2`、路径schemaVersion 2；图鉴、档案的旧快照只读。新完成旅程记录version 0.4.0，旧记录保留原版本。

## 素材与体验

本体：文字、UI、六幅按地点复用场景图、少量纹章和BGM。卷首1幅；特殊结局8幅Premium图以`artType/artKey`映射，图鉴只有解锁后显示。普通Ending无大图；剧情不显示像素人物。14个NPC的`spriteKey`保留在数据但页面仅用首次身份标签。

八首72秒原创程序配乐：`title/home/normal/explore/tension/final_day/ending/ending_dark`。WAV母版、Ogg交付资源均在`assets/audio/bgm/`。`scripts/generate_bgm.py`需NumPy；Ogg由FFmpeg Vorbis编码。页面加载不播放；首次手势激活；旧profile关闭偏好与音量不覆盖。`src/audio.js`的pending/settled/retired竞态修复保持不变。五个SFX仍只有接口，无音效文件。

`data/prose_variants.json`由`build.py`写入bundle；`src/prose.js`在引擎视图外添加只读过渡，不改选择、状态或回看快照。条件优先顺序为数据行顺序，前置choice ID或已知truth/flag均由真实七日状态验证。没有匹配时共用正文；跨地区额外标明次日转移。13个choice条件变体和一组truth条件均有可达见证，详见`docs/narrative_variants_v04.md`。

## 构建与验证

`python scripts/release_v04.py`运行全路径、Truth、Arc、档案、文本变体、音频竞态/autoplay、实际HTML模拟DOM、WAV结构、交付Ogg解码、Android静态检查和可用时浏览器测试，随后生成ZIP。`tests/browser-report-v04.json`目前标记blocked：没有可用Chrome/Edge，因此未完成七视口截图、真实听感、WebView与真机操作。此环境有JDK但无Android SDK/Gradle/adb；新版APK未实际生成。GitHub Actions手动工作流使用JDK17、SDK35、Gradle8.9构建debug包；推送后须重新触发并检查产物。

Android的applicationId仍是`com.seventhday.game`。CI的临时debug密钥可能不同，不能承诺覆盖安装以前下载的debug APK；正式升级需稳定签名。留待实测：Chrome/Edge 320/375/390/430截图及音频试听、Android返回键与后台恢复、真实用户盲测。不要把静态模拟当作设备验收。
