# 投资的世界

面向初学者的中文投资书籍，用 VitePress 构建，发布在 GitHub Pages：https://guiyuanju.github.io/investment-book/

## 结构

- `docs/outline.md`：全书目录（唯一的目录来源）。章节链接格式 `### [第N章 标题](/partXX/chYY) 难度`。
- `docs/guide.md`：读者定位、章节结构、写作原则。写作前必读。
- `docs/partXX/chYY.md`：章节正文。未写的章节是占位文件（含“本章正文撰写中”）。
- `scripts/sync_outline.py`：根据 `outline.md` 生成 `docs/.vitepress/sidebar.json`，并为缺失的章节创建占位文件，不覆盖已有内容。
- `.github/workflows/deploy.yml`：推送到 `main` 后自动构建并部署到 GitHub Pages。

## 命令

- `npm run dev`：本地预览
- `npm run build`：构建（会检查死链，提交前必须通过）
- `npm run sync`：修改 `outline.md` 后同步侧边栏和占位文件

## 写作与审阅

撰写、审阅、修复章节时，使用 `write-chapters` skill（`.claude/skills/write-chapters/`）。要点：

- 读者生活在日本、读中文；日中美三个市场都覆盖，日本优先。
- 概念正确第一：所有数字用 python3 重算；2024 年以后的数据和不确定的事实必须联网核实。
- 每批章节写完后，每章派一个 subagent 并行审阅，汇总后让用户选择采纳的级别，再修复。

## 进度

- 第一部分（第 1–5 章）：已完成，已审阅并修复。
- 第二部分（第 6–14 章）：已完成，已审阅并修复（2026-10）。
- 第三部分（第 15–20 章）：已完成，已审阅并修复（2026-10）。
- 第四部分（第 21–23 章）：已完成，已审阅并修复（2026-10）。
- 第五部分（第 24–28 章）：已完成，已审阅并修复（2026-10）。
- 第六部分（第 29–32 章）：已完成，已审阅并修复（2026-10）。
- 第七部分（第 33–39 章）：已完成，已审阅并修复（2026-10）。
- 其余部分：占位。
