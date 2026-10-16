# Continuous Science Explainer Video Skill

一个制作科学与工程科普视频的 Codex Skill：深色背景、连续承接的对象，以及与模型计算同步的因果动画。所有者后续视频统一使用线条动画，支持男声讲解和无配音简约两种解说方式，泛光可选。

重点是把原理演出来：保留参考波形 → 改变候选参数 → 重新计算预测 → 画出残差 → 更新误差指标 → 将同一候选带入误差空间。论文介绍沿着“困难、现象、新增操作、变化、条件”展开。

## 安装

将仓库中的 [`science-explainer-video`](science-explainer-video/) 文件夹复制到 Codex skills 目录，例如 `~/.codex/skills/`。入口是 [SKILL.md](science-explainer-video/SKILL.md)。也可使用 skill-installer 安装这个仓库的 `science-explainer-video` 子目录。

## 使用

```text
使用 $science-explainer-video，为我制作一个解释电机参数辨识的视频。
采用横屏、正常速度，用连续动画展示候选参数、预测电流、残差与更新；
先做一段代表性样片，声音使用我提供的授权音色档案。
```

默认正常速度；中文共同推演使用“我们”，个人实现与实验使用“我”，具体主语要求按用户当前约定调整。仓库现已包含所有者授权公开的中文科普男声参考资源，也可以使用自己的授权音色档案。

制作新视频前，一起确认三个问题；当前需求已经明确的选项不重复询问：

1. 是否使用简约风？简约风成片为 **3–4 分钟**，无人声，背景音乐根据内容、情绪及是否有旁白从本机配乐库**自动匹配**；不再每条固定使用 WeNever。
2. 是否加泛光？加泛光时仍保留清晰线条和简洁构图；也可明确选择低泛光或无泛光。
3. 配色选 **金色强调（#D3B370）**，还是 **FOC 明亮版（#B5EAFF + #FFDA9E）**？后者加载 `foc-line-bright60-v1` 的完整数值配置，紫 / 粉信号分别为 `#C3B3FF` / `#F5A3C2`。旧名“冰蓝香槟金”仅作别名；选择配色不会改变是否配人声。

加泛光时，将柔和光晕集中在有意义的活动光点、扫描头和变化区域，保留清晰核心、文字及安静的背景结构。画面底部不放来源/方法小字行，依据完整放在附带文档里，图中必要的单位、条件和解释仍保留。

2026-10-15 新增参考：[电子智人《自指：我是个怪圈》](https://www.douyin.com/video/7692591222837300507)。转场、文字入场、配色和动感，以这条新参考优先；冲突的旧规则已替换。两个讲解模式都采用对象承接与重构图、路径绘制与扫描、逐字/分短语揭示及焦点变化，保留读图停顿，不再把全片做成同一种淡入淡出。图文分层，转场完成后检查没有意外残影。具体观察、实现建议及配色见[动态科技风规范](science-explainer-video/references/dynamic-tech-style.md)；原有音色、简约风 3–4 分钟及背景音乐约定继续保留。

2026-10-16 最新要求：所有者今后的视频直接采用**线条动画**，不再主动制作其它动画风格或多风格对比；封面主题最大，字幕和必要标签按[手机大字规范](science-explainer-video/references/line-animation-mobile-type.md)处理。男声版字幕必须是实际解说原话，并按最终速度音频逐句对齐，不能用摘要替代。原创讲解中的“本例”改为自然的“本视频”表述；UART/CAN/LIN/1-Wire 用单词读法、SPI 逐字母、I²C 读“i 方 c”，“引脚”的“脚”读 jiǎo。完整规则见[解说与字幕纠错规范](science-explainer-video/references/narration-subtitle-corrections.md)。1.1 倍、1.15 倍及无 BGM 属于具体视频设置，不是所有视频的新默认。

字幕专用的两条通用规则：希腊字母中文译名统一显示为对应标准符号（如 α、β、γ、δ）；控制与信号处理经典算法相关人名采用标准英文拼写（如 Clarke、Park、Kalman、Mamdani）。这些规则适用于后续全部视频的烧录及导出字幕，保留原解说读音和内容，不回写 TTS 输入；具体大小写、语境与验收规则见[解说与字幕纠错规范](science-explainer-video/references/narration-subtitle-corrections.md)。

[无配音简约风规范](science-explainer-video/references/minimalist-no-voiceover.md)记录了构图、短文案和阅读节奏。[自动配乐规则](science-explainer-video/references/music-selection.md)记录主题匹配、完整音源检查和署名要求。私人曲库通过本机配置接入，不随仓库分发；使用 `scripts/select_music.py` 可从实际可用的完整音源中选择。此前按所有者的明确要求提供的 WeNever 独立音源继续作为候选资源：

- [M4A 原音轨](science-explainer-video/assets/music/we-never-remix/we-never-remix.m4a)：直接提取 AAC 音轨，没有重新编码。
- [MP3 通用版](science-explainer-video/assets/music/we-never-remix/we-never-remix.mp3)：256 kbit/s，转换时预留 4 dB 电平余量。
- [曲目信息与文件校验值](science-explainer-video/assets/music/we-never-remix/music_profile.json)。曲目为《WeNever (Remix)（若如初见）》— Hi Noise / 秋成，约 3 分 13 秒。

这些旧版音源的片尾在使用前需检查；所有者本机已有去掉平台提示音的干净版本，未来制作优先使用本机目录记录的校验文件。成片中的循环、音量调整与首尾淡入淡出应按每次视频重新处理。音乐署名和许可范围见[第三方资源说明](THIRD_PARTY_NOTICES.md)。

## 已确认 FOC 视觉参数

当前 FOC 明亮线条版已保存为 [`foc-line-bright60-v1`](science-explainer-video/references/foc-bright60-style.json)：实际 HEX/RGB、背景渐变、线芯宽度与 27% 混白提亮、近远泛光半径和增益、微软雅黑粗体各级字号、字幕位置和原生 4K 60 fps 参数。[参数说明](science-explainer-video/references/foc-bright60-style.md)说明坐标缩放与合成顺序。色名仅作别名，制作时直接加载数值配置；旧参考色板不能覆盖这个已确认版本。

## 视频同款声线

已公开视频制作时使用的参考录音、认可试听、生成参数和复用脚本：

- [试听 MP3](science-explainer-video/assets/voice/default-zh-male/approved-preview.mp3) / [原始试听 WAV](science-explainer-video/assets/voice/default-zh-male/approved-preview.wav)。
- [实际合成参考片段](science-explainer-video/assets/voice/default-zh-male/icl-reference.wav)及对应文字。
- [音色参数档案](science-explainer-video/assets/voice/default-zh-male/voice_profile.json)：模型来源、版本、参考音频与权重校验值。
- [使用步骤](science-explainer-video/references/voice-profile.md) / [旁白生成脚本](science-explainer-video/scripts/generate_narration.py)。

声线包使用已确认的 Qwen3-TTS 0.6B CustomVoice 实验性 ICL 方法，复用参考音频编码、运行时类型覆盖及全零说话人向量；它是这套视频的实际生成记录，不能误记为官方固定说话人或一个独立训练的声音模型。Qwen 权重从[官方模型页](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice)单独下载，仓库内的三个音频合计约 0.85 MiB。

安装声线依赖、下载模型后，可以这样生成一个短段落；所有缓存和中间文件放在明确指定的 `--work-dir`：

```bash
export VOICE_WORK=/path/to/temporary-work
mkdir -p "$VOICE_WORK"
export TMPDIR="$VOICE_WORK" HF_HOME="$VOICE_WORK/hf-cache" PIP_CACHE_DIR="$VOICE_WORK/pip-cache"
python -m venv "$VOICE_WORK/venv"
source "$VOICE_WORK/venv/bin/activate"
python -m pip install -r requirements-narration.txt
hf download Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice --local-dir "$VOICE_WORK/model"
python science-explainer-video/scripts/generate_narration.py \
  --model-dir "$VOICE_WORK/model" \
  --text-file science-explainer-video/assets/voice/default-zh-male/approved-transcript.txt \
  --output "$VOICE_WORK/narration.wav" \
  --work-dir "$VOICE_WORK/synthesis-cache"
```

Windows 的 CPU 环境与 PowerShell 示例见[声线使用步骤](science-explainer-video/references/voice-profile.md)。音色以保存的试听为准，合成后检查声线和朗读内容；长讲稿分段生成，再根据各段录音排字幕与动画。

## 可运行的原创示例

需要 Python 3.10+、Pillow、NumPy 和支持 libx264 的 ffmpeg。示例是**无声的 RC 原理动画**；波形、残差和误差曲线来自同一个明确给定的解析模型，不代表实测结果。

```bash
python -m pip install -r requirements.txt
python science-explainer-video/scripts/render_example.py \
  --output /path/to/temporary-work/rc-demo.mp4 \
  --work-dir /path/to/temporary-work \
  --ffmpeg /path/to/ffmpeg \
  --font /path/to/a-readable-font.ttf
```

请将 `--work-dir` 放在环境指定的临时目录；Windows 可用绝对路径。默认 1920 × 1080、30 fps、12 秒；`--width 960 --height 540 --fps 15` 可快速预览。`--preview-only` 只写代表性帧和模型检查记录。

示例和 helper 是原创实现，用于说明制作方法。视频动画示例保持无声；新增旁白脚本可单独复用公开声线。正式视频需建立分镜、声音时间轴、核实内容来源，并检查最终编码文件。

## 内容

- [Skill 入口](science-explainer-video/SKILL.md)：适用范围、制作规则、音色与证据边界、交付检查。
- [分镜与证据参考](science-explainer-video/references/animation-playbook.md)：连续镜头、论文承接、定量场景与示例模型。
- [动态科技风规范](science-explainer-video/references/dynamic-tech-style.md)：最新参考的观看记录、优先级、转场、文字揭示、动感与冰蓝香槟金配色。
- [辉光画布 helper](science-explainer-video/scripts/glow_canvas.py)：主线、柔和辉光、字幕区域和 ffmpeg 输出。
- [RC 动画示例](science-explainer-video/scripts/render_example.py)：模型与画面同步的最小示范。
- [公开声线资源](science-explainer-video/assets/voice/default-zh-male/)与[使用说明](science-explainer-video/references/voice-profile.md)：视频同款参考音频、参数、依赖与生成方法。

代码与原理示例为原创实现。公开声线资源由仓库所有者明确授权提供；模型来源及生成方式保留在档案中。

## License

仓库代码、文档与所有者授权公开的男声参考音频使用 MIT。第三方背景音乐不适用 MIT，见[第三方资源说明](THIRD_PARTY_NOTICES.md)。Qwen 模型遵守其上游 Apache-2.0 许可证；依赖包和本机字体遵守其各自许可证。
