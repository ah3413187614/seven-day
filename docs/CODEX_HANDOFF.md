# CODEX_HANDOFF · V0.3 封板

## 当前版本与边界

89个剧情节点、356个行动、24条人物弧光、10项Truth、18个终局动态权限槽。首周目16,384条路径有165个可达称号；NG+ 16,384条路径合计可达166个称号，真结局有22条NG+路径。`src/engine.js`和剧情判定未在本次视觉与存档修复中修改。不要从V0.2重写89场景。

最终玩家画面为文字、UI、五首离线BGM、小型纹章、可选的Premium Ending插画。**剧情不显示日常像素人物，普通Ending没有大型或像素结局图。** 14个`spriteKey`、节点`characterIds`、相遇数据和首次简短身份标签仍在项目数据。像素SVG原型只随源码保留，不打入玩家HTML。普通结局规则`artType=none, artKey=null`；8个Premium规则使用`artType=premium`和独立`artKey`。实际完成的Premium插画为8，缺图时省略图片区域；创作说明见`docs/art_prompts_v03.md`。

## 主要文件

- `src/ui.js`：首次开场、首次相遇标签、首周目无系统得失的四个选项、图鉴与旅程档案、只读Ending Recall、音频状态按钮。`state`与`recalled.snapshot`分离。
- `src/journal.js`：最近40次完整旅程、每个Ending一份完整代表记录、旧资料迁移与只读深拷贝。旧版只有称号但无完整历史的条目不能凭空补写尾声。
- `src/audio.js`：`enabled`玩家偏好与`activated`当前会话手势许可分开。首次加载只设置默认或旧偏好；新用户默认开启、音量0.40，首次交互后尝试播放。旧资料明确关闭时维持关闭；播放被拒后待下次手势重试。后台暂停。五首程序合成WAV已实际嵌入。五个SFX接口存在，素材为0。
- `scripts/build.py`：生成带人物与结局视觉键的数据；`scripts/pack.py`：单文件内嵌CSS、数据、引擎、档案、音频、UI与WAV，Premium有图才内嵌。
- `scripts/finalize_v03.py`：同步根目录HTML及文档、生成`tests/final-build-manifest.json` SHA-256并压缩完整项目。

存储键仍为`seventh-day-v2`，路径`schemaVersion=2`，资料`saveVersion=3`。当前路线导出是JSON路径存档，不包括跨设备的完整档案。每次导入都用随机UUID或时间+随机数新建runId；不使用choiceIds身份。首次开场未完成且历史为空时，刷新后“继续旅程”仍回开场；真正进入第一日后新局与NG+不再重复。Ending Recall不调用导入、记录或保存，不覆盖当前runId和七日选择。

## 构建与验证

在项目根目录顺序运行：

```sh
python3 scripts/build.py
node tests/exhaustive.cjs
node tests/evidence-v02.cjs
python3 scripts/pack.py
node tests/journal-v03.cjs
node tests/media-v03.cjs
node tests/autoplay-v03.cjs
node tests/package.cjs
node tests/browser.cjs
python3 scripts/finalize_v03.py
```

`tests/package.cjs`读取实际打包HTML，模拟序章→七日→结局→图鉴回看→第二局→档案→返回，以及同一Day3存档导入两次产生不同Ending。穷举、权限、弧光、Truth、旧资料、音频拒绝重试和跨刷新开关的记录在`docs/playtest_v03.md`。结局引擎未结构修改，未在V0.3重新执行100,000随机模拟；`tests/random-report.json`属于V0.2历史结果。

环境中没有可用Chromium；`tests/browser-report-v03.json`标记七个视口未运行。模拟DOM和CSS断点检查不能代替真实浏览器视觉/触控、音频听感或Android WebView验收。没有CDN、远程字体、服务器请求和联网依赖；核心离线文件包装可供下一阶段WebView实机验证，APK本轮未制作。

## 后续

合法SFX、真人配乐试听和母带调校、Chrome/Edge七视口和触控/听感QA、真人盲测、Android WebView实机与APK，均未完成。当前24秒原创程序合成WAV已提高响度并加入旋律与和声；仍未通过人耳和设备听感验收。

## 最终音频按钮补丁

实际Edge使用的`SeventhDay(3).html`与项目HTML字节一致。旧按钮把待播放点击视为关闭；现改为关→启用/播放，待播放或失败→保持开启/重试，播放中→关闭。`src/audio.js`保留真实`play()`拒绝名/消息及媒体错误码/消息，成功和失败都通知UI刷新；`src/ui.js`显示“音乐：重试”并在标题与控制台提供诊断。再次修改音频后必须运行`tests/autoplay-v03.cjs`、`tests/media-v03.cjs`和`tests/package.cjs`，重新`pack.py`及`finalize_v03.py`。不要用模拟测试或WAV格式检查宣称Edge实际出声。

**最新Edge竞态修复：** 用户在桌面路径依然复现AbortError，旧`src/audio.js`在pending play()时调用pause()。现以每音轨pending/settled/retired状态延迟pause、静音退场，并对同键single-flight；onStatus只更新按钮，不render全页。运行`node tests/audio-race-v03.cjs`与原有三项媒体/包测试。AbortError只记内部中断，不进入autoplay失败通道；核心引擎未动。Android资源需再运行`python3 android/sync_game.py`同步新版HTML。

## 2026-09-29 视觉与音乐补充

卷首1幅、环境6幅和Premium Ending 8幅原创生成插画已存于`assets/scenes/*.jpg`、`assets/endings/premium/*.jpg`，由`pack.py`嵌入离线HTML。按实际地点复用环境图，不按89节点逐幅配图；手机端场景图高度105–125px。普通结局继续只用小纹章，本体不显示像素小人。新图片缺失时省略，不阻断故事。

`generate_bgm.py`现在生成五段24秒循环，旋律/和声/两段变化，约-16.2 dBFS且轨间差<1.5dB；新profile默认音量0.40，已有设置不被改写。仅波形与模拟播放验证，Edge实际可听、循环接缝及手机扬声器听感仍需人工验收。开场明确村民身份与第一天四件具体行动，局部修复八处抵达/称呼衔接。核心引擎和选项效果未改。根HTML与Android WebView资产同步；Android APK尚未在本工作环境构建。
