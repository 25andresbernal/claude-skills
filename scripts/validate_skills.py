#!/usr/bin/env python3
"""Validate skills/*/SKILL.md files and scan the repo for banned characters.

Checks:
  1. Every skills/<name>/SKILL.md exists and has YAML frontmatter with the
     required fields: name, description.
  2. The frontmatter `name` matches the folder name exactly.
  3. `name` follows the documented rules: at most 64 characters, lowercase
     letters, numbers, and hyphens only, no reserved words.
  4. `description` is non-empty and at most 1024 characters, the documented
     Claude Skills limit.
  5. Every relative markdown link in SKILL.md (templates, reference files,
     examples) points to a file that actually exists.
  6. No em dashes or emoji appear anywhere in the repository's text files.

Stdlib only. Python 3.10+.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

MAX_DESCRIPTION_LEN = 1024
MAX_NAME_LEN = 64
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED_WORDS = {"anthropic", "claude"}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

EM_DASH = chr(0x2014)  # em dash
EMOJI_PATTERN = re.compile(
    "["
    "\U0001f1e6-\U0001f1ff"  # regional indicators (flags)
    "\U0001f300-\U0001faff"  # symbols, pictographs, emoticons, transport
    "\U00002600-\U000027bf"  # misc symbols and dingbats
    "\U00002b00-\U00002bff"  # misc symbols and arrows
    "\U0000fe0f"  # variation selector-16
    "]"
)

TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".txt", ".toml", ".cfg", ".json"}


class FrontmatterError(Exception):
    pass


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise FrontmatterError("missing YAML frontmatter delimited by '---'")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value
    return fields


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    folder_name = skill_dir.name
    rel_skill_md = skill_md.relative_to(REPO_ROOT)

    if not skill_md.exists():
        return [f"{skill_dir.relative_to(REPO_ROOT)}: no SKILL.md found"]

    text = skill_md.read_text(encoding="utf-8")

    try:
        fields = parse_frontmatter(text)
    except FrontmatterError as exc:
        return [f"{rel_skill_md}: {exc}"]

    name = fields.get("name")
    description = fields.get("description")

    if not name:
        errors.append(f"{rel_skill_md}: frontmatter missing required field 'name'")
    else:
        if name != folder_name:
            errors.append(
                f"{rel_skill_md}: name '{name}' does not match folder name '{folder_name}'"
            )
        if len(name) > MAX_NAME_LEN:
            errors.append(f"{rel_skill_md}: name exceeds {MAX_NAME_LEN} characters")
        if not NAME_RE.match(name):
            errors.append(
                f"{rel_skill_md}: name must be lowercase letters, numbers, and hyphens only"
            )
        if name in RESERVED_WORDS:
            errors.append(f"{rel_skill_md}: name uses a reserved word ('{name}')")

    if not description:
        errors.append(f"{rel_skill_md}: frontmatter missing required field 'description'")
    elif len(description) > MAX_DESCRIPTION_LEN:
        errors.append(
            f"{rel_skill_md}: description is {len(description)} characters, "
            f"exceeds the {MAX_DESCRIPTION_LEN} character limit"
        )

    for link_target in LINK_RE.findall(text):
        if link_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = link_target.split("#", 1)[0]
        if not target:
            continue
        target_path = (skill_md.parent / target).resolve()
        if not target_path.exists():
            errors.append(f"{rel_skill_md}: referenced file not found: {link_target}")

    return errors


def scan_banned_characters() -> list[str]:
    errors: list[str] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(REPO_ROOT)
        for lineno, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line:
                errors.append(f"{rel}:{lineno}: contains an em dash")
            if EMOJI_PATTERN.search(line):
                errors.append(f"{rel}:{lineno}: contains an emoji")
    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"error: {SKILLS_DIR} does not exist", file=sys.stderr)
        return 1

    all_errors: list[str] = []

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        all_errors.append(f"{SKILLS_DIR.relative_to(REPO_ROOT)}: no skill folders found")

    for skill_dir in skill_dirs:
        all_errors.extend(check_skill(skill_dir))

    all_errors.extend(scan_banned_characters())

    if all_errors:
        print(f"validate_skills: {len(all_errors)} problem(s) found\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(
        f"validate_skills: {len(skill_dirs)} skill(s) passed all checks, "
        "no em dashes or emoji found"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
