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

默认正常速度；中文共同推演使用“我们”，个人实现与实验使用“我”。音色是用户提供的外部配置，本仓库不含私人录音、声音模型或参考视频。

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

示例和 helper 是原创实现，用于说明制作方法。它们不是完整视频生成平台，不含完整稿件、配音服务、ASR 对齐器或论文数据库。正式视频需建立分镜、声音时间轴、核实内容来源，并检查最终编码文件。

## 内容

- [Skill 入口](science-explainer-video/SKILL.md)：适用范围、制作规则、音色与证据边界、交付检查。
- [分镜与证据参考](science-explainer-video/references/animation-playbook.md)：连续镜头、论文承接、定量场景与示例模型。
- [辉光画布 helper](science-explainer-video/scripts/glow_canvas.py)：主线、柔和辉光、字幕区域和 ffmpeg 输出。
- [RC 动画示例](science-explainer-video/scripts/render_example.py)：模型与画面同步的最小示范。

本仓库没有复制第三方视频画面、配音或代码。它总结通用的连续原理讲解方法，并实现可复用的原创辅助代码。

## License

MIT。依赖包和本机字体遵守其各自许可证；仓库不分发字体。
