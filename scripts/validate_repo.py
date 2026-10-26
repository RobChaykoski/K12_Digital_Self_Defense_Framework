#!/usr/bin/env python3
"""Structural validation for the K-12 Digital Self-Defense Framework repository.

This is a documentation repository, so the things that break are not compile
errors. They are: a merge-conflict marker left in a published file, a link to a
file that was renamed, an anchor that points at a heading that no longer says
what it used to, a UTF-8 BOM that turns every future edit into a whole-file diff,
and a CTF flag that disagrees with the scoring rubric.

Run with:  python3 scripts/validate_repo.py
Exit status is 0 when clean, 1 when anything fails.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories that are archived, generated, or not ours.
SKIP_DIRS = {".git", "_archive", "node_modules", "exports", "unsloth-tmp", ".venv", "venv"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
CODE_MD_RE = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")
FLAG_RE = re.compile(r"flag\{[^}]*\}")
VALID_FLAG_RE = re.compile(r"^flag\{[a-z0-9_]+\}$")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def fail(self, path: Path | str, message: str) -> None:
        rel = path if isinstance(path, str) else path.relative_to(REPO_ROOT).as_posix()
        self.failures.append(f"{rel}: {message}")

    def ok(self) -> bool:
        return not self.failures


def iter_markdown() -> list[Path]:
    found = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        found.append(path)
    return sorted(found)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    text = re.sub(r"`([^`]*)`", r"\1", heading)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    out = []
    for ch in text.strip().lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch in " \t":
            out.append("-")
        # every other character (punctuation, emoji) is dropped
    return "".join(out)


def collect_anchors(text: str) -> set[str]:
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = github_slug(match.group(2))
        if slug in seen:
            seen[slug] += 1
            anchors.add(f"{slug}-{seen[slug]}")
        else:
            seen[slug] = 0
            anchors.add(slug)
    return anchors


def check_conflict_markers(files: list[Path], report: Report) -> None:
    for path in files:
        for number, line in enumerate(read_text(path).splitlines(), start=1):
            if line.startswith("<<<<<<< ") or line.startswith(">>>>>>> ") or line == "=======":
                report.fail(path, f"line {number}: merge conflict marker")


def check_bom(files: list[Path], report: Report) -> None:
    for path in files:
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            report.fail(path, "file starts with a UTF-8 BOM")


def check_links(files: list[Path], report: Report) -> None:
    anchors_cache: dict[Path, set[str]] = {}
    for path in files:
        text = read_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for target in LINK_RE.findall(line):
                if re.match(r"^(https?:|mailto:|tel:|#)", target):
                    continue
                file_part, _, anchor = target.partition("#")
                destination = (path.parent / file_part).resolve() if file_part else path
                if file_part and not destination.exists():
                    report.fail(path, f"line {line_number}: link target not found: {target}")
                    continue
                if not anchor or destination.suffix != ".md":
                    continue
                if destination not in anchors_cache:
                    anchors_cache[destination] = collect_anchors(read_text(destination))
                if anchor not in anchors_cache[destination]:
                    report.fail(path, f"line {line_number}: anchor not found: {target}")


def markdown_filenames() -> set[str]:
    """Every markdown basename present in the repository (outside skipped dirs)."""
    names: set[str] = set()
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        names.add(path.name)
    return names


def check_inline_md_paths(files: list[Path], report: Report) -> None:
    """Check inline code paths that point at markdown documents.

    Two forms appear in this repository:

      * `docs/implementation_guide.md` -- an explicit path. It must resolve
        relative to the document or to the repository root.
      * `02_Lesson_Plans.md` -- shorthand for "the file of that name in the
        program being discussed". It must resolve next to the document, at the
        root, or as a basename that exists somewhere in the repository.

    Without the basename rule every `02_Lesson_Plans.md` in `docs/` reads as
    broken; without the basename check, a reference to a file that never existed
    passes. The earlier version of this function ignored bare filenames outside
    `Programs/`, which let exactly that through.
    """
    names = markdown_filenames()
    for path in files:
        text = read_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for token in CODE_MD_RE.findall(line):
                if token.startswith("./") or token.startswith("../"):
                    candidates = [path.parent / token]
                else:
                    candidates = [path.parent / token, REPO_ROOT / token]
                if any(candidate.exists() for candidate in candidates):
                    continue
                if "/" not in token and token in names:
                    continue
                report.fail(path, f"line {line_number}: referenced file does not exist: {token}")


def worksheet_flags() -> dict[str, list[str]]:
    flags: dict[str, list[str]] = {}
    for path in sorted(REPO_ROOT.glob("Programs/*/07_CTF_Worksheets.md")):
        flags[path.parent.name] = FLAG_RE.findall(read_text(path))
    return flags


def check_flags(report: Report) -> None:
    per_program = worksheet_flags()
    if not per_program:
        report.fail("Programs", "no CTF worksheets found")
        return

    all_flags: set[str] = set()
    for program, flags in per_program.items():
        if not flags:
            report.fail(f"Programs/{program}", "worksheet contains no flag{...} strings")
        for flag in flags:
            if not VALID_FLAG_RE.match(flag):
                report.fail(f"Programs/{program}", f"flag does not match ^flag\\{{[a-z0-9_]+\\}}$: {flag}")
        all_flags.update(flags)

    rubric = REPO_ROOT / "docs" / "ctf_scoring_rubric.md"
    if not rubric.exists():
        report.fail("docs/ctf_scoring_rubric.md", "missing")
        return
    rubric_flags = set(FLAG_RE.findall(read_text(rubric)))
    missing = sorted(all_flags - rubric_flags)
    if missing:
        report.fail("docs/ctf_scoring_rubric.md", f"flags missing from rubric: {', '.join(missing)}")


def check_git_clean_hint(report: Report) -> None:
    """Warn (do not fail) when there are uncommitted changes, so CI output is honest."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return
    if result.returncode == 0 and result.stdout.strip():
        print("note: working tree has uncommitted changes (not a failure)")


def main() -> int:
    files = iter_markdown()
    report = Report()

    checks = [
        ("conflict markers", lambda: check_conflict_markers(files, report)),
        ("byte-order marks", lambda: check_bom(files, report)),
        ("links and anchors", lambda: check_links(files, report)),
        ("inline file paths", lambda: check_inline_md_paths(files, report)),
        ("CTF flags", lambda: check_flags(report)),
    ]

    for name, check in checks:
        before = len(report.failures)
        check()
        added = len(report.failures) - before
        status = "ok" if added == 0 else f"{added} problem(s)"
        print(f"[{status}] {name}")

    print(f"\nchecked {len(files)} markdown files")
    if report.ok():
        print("PASS")
        return 0

    print(f"\n{len(report.failures)} failure(s):")
    for failure in report.failures:
        print(f"  - {failure}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
