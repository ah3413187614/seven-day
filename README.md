# 《第七日的勇者》

**Dark Fantasy Interactive Narrative · 当前开发版 V0.4**

七天选择结构，每天四个行动。**Yesterday's choice determines today's options.** 七日的行动、已知真相和关系共同影响终局。直接打开根目录 `SeventhDay.html` 即可离线游玩。

V0.4 采用文字、地点环境、少量纹章、八首离线 BGM 和八幅特殊结局插画；普通结局以文字呈现，不使用日常像素人物。通关后可在命运图鉴回看结局，旅程档案保留已完成的路线。旧版存档和图鉴资料沿用同一存储键。

Android 工程在 `android/`，使用本地网页资产。当前工作环境未构建新版 APK；GitHub Actions 工作流可在推送后手动触发 debug 构建。调试签名包与正式上架签名不同。

从源码构建并验收：`python scripts/release_v04.py`。它按顺序生成数据、运行回归、构建网页、同步 Android 资产并打包完整项目。音频母版在 `assets/audio/bgm/*.wav`，交付压缩格式在 `assets/audio/bgm/ogg/`；若修改配乐，先执行 `python scripts/generate_bgm.py`，再按 `ffmpeg -i 输入.wav -c:a libvorbis -q:a 4 输出.ogg` 逐轨重制，最后运行发布脚本。需要 Python、NumPy、Node.js；音频解码测试需要 FFmpeg。

89 个节点、356 个行动、24 条可验证人物弧光；首周目与 NG+ 各 16,384 条路径，合计 166 个可达称号。自动测试不能替代真实 Chrome/Edge 视觉和设备试听。详见 `CHANGELOG_V0.4.md` 与 `docs/CODEX_HANDOFF.md`。

历史标签：[`v0.1.0`](../../tree/v0.1.0)、[`v0.2.0`](../../tree/v0.2.0)、[`v0.3.0`](../../tree/v0.3.0)。V0.4 当前为后续提交，不改写历史标签。
