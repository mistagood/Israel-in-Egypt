import json
from collections import defaultdict
import os

with open("md_topic_summary.json", "r", encoding="utf-8") as f:
    summary = json.load(f)

# Reverse map: topic → list of files
topic_map = defaultdict(list)

for filename, data in summary.items():
    top_terms = [term for term, _ in data["top_terms"][:5]]
    for term in top_terms:
        topic_map[term].append(filename)

# Build Markdown index
lines = ["# 🧠 Topic Index\n"]
for topic in sorted(topic_map):
    lines.append(f"## {topic.title()}")
    for file in sorted(topic_map[topic]):
        file_display = file.replace(".md", "")
        link = f"./{file}"  # relative markdown link
        lines.append(f"- [{file_display}]({link})")
    lines.append("")

with open("topics_index.md", "w", encoding="utf-8") as out:
    out.write("\n".join(lines))

print("✅ Created topics_index.md")