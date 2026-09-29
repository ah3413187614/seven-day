# V0.4 断点记录 · 2026-09-29

版本：`v0.4.0+16facfdc460f`。已完成并接入八首72秒BGM（WAV母版、Ogg交付）、卷首1幅＋地点6幅＋Premium结局8幅插画、地点背景、开场与局部剧情衔接、13项可达入场文字变体、导航与音乐提示。保留旧存档和结局回看；89节点、356行动、首周目/NG+各16,384路径及24弧光通过。`src/audio.js`的播放竞态修复与旧静音偏好没有改动。

构建：`scripts/release_v04.py`生成根HTML、dist、Android资产、ZIP，并检查Android只多存档导出桥接。最终HTML SHA-256 `ccd3994a05e0e76834274de862dd0a4af9fd4a200177668d9c134859484d3b99`。ZIP内HTML与Android资产已核对；Git提交`87748ba`，另有Git bundle供Windows仓库接续。

剩余的**设备验收**：本环境无Chrome/Edge可执行文件、Android SDK/Gradle/adb。真实浏览器截图、扬声器试听、手机触摸、WebView返回键与安装升级均未验证；新版APK未构建。不要将模拟DOM、FFmpeg解码或旧APK算作上述验收。

下一条可执行操作：在有Edge和Android构建环境的Windows仓库引入V0.4提交并推送，触发GitHub Actions的`Build Android debug APK`，下载实际产物；用本机Edge检查320/375/390/430布局与音乐试听，用Android设备检查安装、存档、后台和返回键。若观察到具体失败，再针对该失败修复并重新运行`python scripts/release_v04.py`。
