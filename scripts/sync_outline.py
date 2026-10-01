"""根据 docs/outline.md 生成侧边栏配置，并为尚不存在的章节创建占位文件。

已存在的章节文件不会被覆盖。用法：python3 scripts/sync_outline.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

part_re = re.compile(r"^## (.+)$")
chapter_re = re.compile(r"^### \[(.+?)\]\((/[^)]+)\)\s*(\S*)")
section_re = re.compile(r"^- (.+)$")

sidebar = [{"text": "开始", "items": [
    {"text": "阅读指南", "link": "/guide"},
    {"text": "全书目录", "link": "/outline"},
]}]
chapters = []

for line in (DOCS / "outline.md").read_text(encoding="utf-8").splitlines():
    if m := part_re.match(line):
        sidebar.append({"text": m.group(1), "collapsed": True, "items": []})
    elif m := chapter_re.match(line):
        title, link, level = m.groups()
        sidebar[-1]["items"].append({"text": title, "link": link})
        chapters.append({"title": title, "link": link, "level": level,
                         "part": sidebar[-1]["text"], "sections": []})
    elif (m := section_re.match(line)) and chapters:
        chapters[-1]["sections"].append(m.group(1))

(DOCS / ".vitepress").mkdir(exist_ok=True)
(DOCS / ".vitepress" / "sidebar.json").write_text(
    json.dumps(sidebar, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

created = 0
for ch in chapters:
    path = DOCS / (ch["link"].lstrip("/") + ".md")
    if path.exists():
        continue
    path.parent.mkdir(parents=True, exist_ok=True)
    level = f" {ch['level']}" if ch["level"] else ""
    body = [f"# {ch['title']}{level}", "",
            f"> {ch['part']}", "",
            "::: warning 本章正文撰写中", "以下为本章大纲。", ":::", ""]
    for s in ch["sections"]:
        body += [f"## {s}", "", "*待撰写*", ""]
    path.write_text("\n".join(body), encoding="utf-8")
    created += 1

print(f"sidebar: {len(chapters)} chapters; created {created} stub files")
