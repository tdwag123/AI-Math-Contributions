import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


DATASET_PATH = Path("ai_math_contributions.json")

REQUIRED_TOP_LEVEL_FIELDS = {"schema_version", "description", "entries"}

REQUIRED_ENTRY_FIELDS = [
    "id",
    "source",
    "source_problem_number",
    "level_of_contribution",
    "ai_systems",
    "humans",
    "solution_status",
    "problem_tag",
    "problem_statement",
    "date_solved",
    "mathematical_area",
    "solution_reference",
    "verification_status",
    "literature",
    "literature_found_on",
    "literature_similar",
    "was_conjecture",
]

def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


def is_valid_date(value):
    if not isinstance(value, str):
        return False
    return bool(re.match(r"^\d{4}(-\d{2}){0,2}$", value))


def is_valid_url(value):
    if not is_non_empty_string(value):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_entry(entry, index, id_counts):
    errors = []
    prefix = f"entries[{index}]"

    if not isinstance(entry, dict):
        return [f"{prefix}: entry must be an object"]

    missing = [field for field in REQUIRED_ENTRY_FIELDS if field not in entry]
    extra = [field for field in entry if field not in REQUIRED_ENTRY_FIELDS]

    for field in missing:
        errors.append(f"{prefix}: missing field '{field}'")
    for field in extra:
        errors.append(f"{prefix}: unknown field '{field}'")

    if missing:
        return errors

    entry_id = entry["id"]
    if not isinstance(entry_id, str) or not re.match(r"^math_\d{3,}$", entry_id):
        errors.append(f"{prefix}.id: expected format math_###")
    elif id_counts[entry_id] > 1:
        errors.append(f"{prefix}.id: duplicate id '{entry_id}'")

    if entry["source"] is not None and not is_non_empty_string(entry["source"]):
        errors.append(f"{prefix}.source: expected non-empty string or null")

    if entry["source_problem_number"] is not None and not isinstance(entry["source_problem_number"], int):
        errors.append(f"{prefix}.source_problem_number: expected integer or null")

    if not is_non_empty_string(entry["level_of_contribution"]):
        errors.append(f"{prefix}.level_of_contribution: expected non-empty string")

    for list_field in ("ai_systems", "humans"):
        value = entry[list_field]
        if not isinstance(value, list) or not all(is_non_empty_string(item) for item in value):
            errors.append(f"{prefix}.{list_field}: expected list of non-empty strings")

    if not entry["ai_systems"]:
        errors.append(f"{prefix}.ai_systems: expected at least one AI system")

    if not is_non_empty_string(entry["solution_status"]):
        errors.append(f"{prefix}.solution_status: expected non-empty string")

    for text_field in ("problem_tag", "problem_statement", "date_solved", "mathematical_area"):
        if not is_non_empty_string(entry[text_field]):
            errors.append(f"{prefix}.{text_field}: expected non-empty string")

    if not is_valid_date(entry["date_solved"]):
        errors.append(f"{prefix}.date_solved: expected YYYY-MM-DD or YYYY-MM")

    if not is_valid_url(entry["solution_reference"]):
        errors.append(f"{prefix}.solution_reference: expected http(s) URL")

    if not is_non_empty_string(entry["verification_status"]):
        errors.append(f"{prefix}.verification_status: expected non-empty string")

    for nullable_text_field in ("literature", "literature_found_on"):
        value = entry[nullable_text_field]
        if value is not None and not isinstance(value, str):
            errors.append(f"{prefix}.{nullable_text_field}: expected string or null")

    if entry["literature_similar"] is not None and not isinstance(entry["literature_similar"], (str, bool, list, dict)):
        errors.append(f"{prefix}.literature_similar: expected JSON value or null")

    if entry["was_conjecture"] is not None and not isinstance(entry["was_conjecture"], bool):
        errors.append(f"{prefix}.was_conjecture: expected boolean or null")

    return errors


def main():
    if not DATASET_PATH.exists():
        print(f"Missing dataset: {DATASET_PATH}", file=sys.stderr)
        return 1

    try:
        data = json.loads(DATASET_PATH.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors = []

    missing_top_level = REQUIRED_TOP_LEVEL_FIELDS - set(data)
    for field in sorted(missing_top_level):
        errors.append(f"top level: missing field '{field}'")

    entries = data.get("entries")
    if not isinstance(entries, list):
        errors.append("top level: entries must be a list")
        entries = []

    ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    id_counts = Counter(ids)

    for index, entry in enumerate(entries):
        errors.extend(validate_entry(entry, index, id_counts))

    if errors:
        print("Dataset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Dataset validation passed: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
