import json
import re
from collections import Counter
from pathlib import Path


DATASET_PATH = Path("ai_math_contributions.json")
README_PATH = Path("README.md")


def table_from_counter(counter, header_name, limit=None):
    rows = counter.most_common(limit)
    lines = [f"| {header_name} | Entries |", "|---|---|"]
    lines.extend(f"| {name} | {count} |" for name, count in rows)
    return "\n".join(lines)


def replace_section(text, heading, body):
    pattern = rf"(### {re.escape(heading)}\n)(.*?)(?=\n### |\n## |\Z)"
    replacement = rf"\1{body.rstrip()}\n"
    new_text, count = re.subn(pattern, replacement, text, flags=re.S)
    if count != 1:
        raise ValueError(f"Could not replace README section: {heading}")
    return new_text


def main():
    data = json.loads(DATASET_PATH.read_text(encoding="utf-8-sig"))
    entries = data["entries"]
    readme = README_PATH.read_text(encoding="utf-8")

    source_counts = Counter(entry["source"] or "Individual papers" for entry in entries)
    area_counts = Counter(entry["mathematical_area"] for entry in entries)
    conjecture_counts = Counter(entry["was_conjecture"] for entry in entries)
    ai_systems = sorted({system for entry in entries for system in entry["ai_systems"]})

    readme = re.sub(
        r"\*\*Entries:\*\* \d+",
        f"**Entries:** {len(entries)}",
        readme,
        count=1,
    )

    readme = replace_section(readme, "By source", table_from_counter(source_counts, "Source"))
    readme = replace_section(
        readme,
        "By mathematical area (top 8)",
        table_from_counter(area_counts, "Area", limit=8),
    )

    conjecture_body = "\n".join(
        [
            f"- **{conjecture_counts[True]} entries** (`was_conjecture: true`) - longstanding conjectures posed by others",
            f"- **{conjecture_counts[False]} entries** (`was_conjecture: false`) - open research problems posed by the solving paper's own authors",
            f"- **{conjecture_counts[None]} entries** (`was_conjecture: null`) - unclear",
        ]
    )
    readme = replace_section(readme, "Was it a pre-existing conjecture?", conjecture_body)

    systems_body = ", ".join(ai_systems)
    readme = replace_section(readme, "AI systems represented", systems_body)

    README_PATH.write_text(readme, encoding="utf-8", newline="\n")
    print(f"Updated README statistics for {len(entries)} entries")


if __name__ == "__main__":
    main()
