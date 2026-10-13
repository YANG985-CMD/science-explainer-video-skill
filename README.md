# Continuous Science Explainer Video Skill

一个制作科学与工程科普视频的 Codex Skill：深色背景、柔和辉光细线、连续承接的对象，以及与模型计算同步的因果动画。

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
- [辉光画布 helper](science-explainer-video/scripts/glow_canvas.py)：主线、柔和辉光、字幕区域和 ffmpeg 输出。
- [RC 动画示例](science-explainer-video/scripts/render_example.py)：模型与画面同步的最小示范。
- [公开声线资源](science-explainer-video/assets/voice/default-zh-male/)与[使用说明](science-explainer-video/references/voice-profile.md)：视频同款参考音频、参数、依赖与生成方法。

代码与原理示例为原创实现。公开声线资源由仓库所有者明确授权提供；模型来源及生成方式保留在档案中。

## License

仓库代码、文档与此次授权公开的参考音频使用 MIT。Qwen 模型遵守其上游 Apache-2.0 许可证；依赖包和本机字体遵守其各自许可证。
