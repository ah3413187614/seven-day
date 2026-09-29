# V0.3 音频系统实装说明

`assets/audio/bgm/` 有5段实际原创程序合成12秒循环WAV：title、normal、tension、final_day、ending。22050Hz单声道PCM，低动态量、小钟与持续音。它们是功能性氛围原型，不声称真人编曲或商业母带质量。源码 `scripts/generate_bgm.py` 可再生，音乐资源不依赖CDN。

`src/audio.js` 新用户偏好默认为开启，但页面加载不创建音频或调用play；首次点击开始/继续或页面时才播放。用户主动关闭后保持关闭。音量默认27%，滑块与开关保存在当前profile，不修改路线存档。曲目切换约900ms交叉淡入淡出；离开标签页暂停；浏览器拒绝play会捕获并退回静音。保存的开启偏好在重新打开页面后需一次手势恢复。环境无法真实播音试听，波形与行为测试仅证明文件/控制结构。

`choice/page/bell/sword/ending_reveal` 五个SFX事件接口已经接入，但 `GAME_SFX` 当前为空，触发返回false且保持静音。没有制作或冒充任何SFX文件。未来需原创录制或明确授权的器物声、页纸声、钟声与金属声，再以同键注入；音频线索不承载独占剧情信息。

## Autoplay 修复

保存或默认的 `enabled=true` 只是待激活偏好。明确保存的 `enabled=false` 永不自动改写。页面初始化和 `render()` 只选择当前 `musicKey`，不调用 `Audio()` 或 `play()`。玩家首次明确点击/按键后调用 `activate()`。若浏览器拒绝本次 `play()`，控制器保留 `enabled=true`，标记待激活；下一次交互再次播放。切到后台立即停音，返回页面不会自行播放。测试为模拟浏览器行为；真实浏览器实际听感和平台策略仍待实测。

## Edge反馈后的状态修复

用户实际打开的 `SeventhDay(3).html` 与交付HTML哈希相同。音乐按钮现在按实际状态处理：关闭→启用并播放；待播放/失败→保持启用并重试；播放中→主动关闭。`play()`成功或失败的异步回调都会重绘按钮，失败显示“音乐：重试”，鼠标悬停可见异常名称、消息及可用的 `MediaError.code/message`；详细结构也写入浏览器控制台。成功后清除旧错误。音频控制器保留 `lastError` 供诊断，既不把错误写入存档，也不因为失败修改玩家偏好。

`tests/autoplay-v03.cjs`模拟拒播→按钮重试→成功→关闭、待播放直接点击、跨刷新偏好和异常保留；`tests/media-v03.cjs`验证媒体错误代码/消息。它们无法证明 Edge 扬声器实际有声。最终HTML的真实Chrome/Edge `play()`状态与设备声音仍须在有浏览器的环境检查。

## Edge `AbortError` 竞态修复（最新）

用户将HTML移到桌面仍稳定复现 `play() request was interrupted by a call to pause()`，确认与下载临时目录无关。此前 `pointerdown` 启动 title 后，click/render 很快切曲或停音，会在 title 的 `play()` Promise 未结束前执行 `pause()`。现在每条音轨都有单独的 pending/settled/retired 状态；待结束的旧音轨先静音，Promise settle 后才 pause。同一曲目的多次 activate 与 render 共用一次 in-flight 启动；新曲目成功后才开始淡入并淡出前曲。

`AbortError` 作为内部中断保留在 `lastInterruption` 诊断中，不记录为 autoplay 拒绝，也不把 enabled 改为 false。`onError` 只输出诊断；异步 `onStatus` 只更新现有按钮的文字和属性，绝不重绘整页或调用 `switchTo`。`tests/audio-race-v03.cjs` 和 `tests/autoplay-v03.cjs` 用受控 Promise 验证早切曲、关闭、重复手势、AbortError 恢复与异步状态刷新。真实 Edge 可听测试仍需用户本机完成。

## Edge `Illegal invocation` 修复

用户本机报告 `fadeIn` 处 `TypeError: Illegal invocation`。默认计时器原先直接引用 `globalThis.setInterval/clearInterval`，在部分 Edge 环境中脱离宿主调用失败。现在默认适配器以 `root.setInterval(...)` 和 `root.clearInterval(...)` 调用，测试注入接口保持不变。检查音频模块未拆取 `audio.play/pause` 或其他宿主方法。播放 Promise 链增加最终 catch；`TypeError` 保留真实诊断，绝不冒充浏览器 autoplay 拒绝。新回归使用要求正确 `this` 的宿主计时器运行 `fadeIn`，并对打包 HTML 运行 autoplay 与竞态测试。当前执行环境仍无可用浏览器，无法声称 Edge 实际扬声器已验证；用户应以此版 HTML 本机重试。

## 当前曲目更新（2026-09-29）

五段WAV已改为24秒循环，含主题旋律、和声与后半段变化；`tests/audio_quality_v03.py`检测采样、24秒时长、轨间RMS一致性、峰值和前后半段不完全重复。实测RMS均约-16.2dBFS，峰值约0.58–0.63。新玩家默认音量40%，旧profile音量与开关不迁移。无法在当前环境真人试听或验证手机扬声器；主观好听和长时间阅读舒适度仍待测试。SFX仍只有接口。
