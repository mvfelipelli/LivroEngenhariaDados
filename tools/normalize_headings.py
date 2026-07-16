from __future__ import annotations

import argparse
import re
from pathlib import Path

from normalize_markdown import find_markdown_files


HEADING_PATTERN = re.compile(r"^(#{1,6})(\s+.*)$")


def heading_positions(lines: list[str]) -> list[tuple[int, int]]:
    positions: list[tuple[int, int]] = []
    in_frontmatter = False
    in_fence = False
    for index, line in enumerate(lines):
        if index == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            continue
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_PATTERN.match(line)
        if match:
            positions.append((index, len(match.group(1))))
    return positions


def normalize_file(path: Path, apply_changes: bool) -> int:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    positions = heading_positions(lines)
    h1_positions = [index for index, level in positions if level == 1]
    if len(h1_positions) <= 1:
        return 0

    first_h1 = h1_positions[0]
    changes = 0
    for index, level in positions:
        if index <= first_h1 or level >= 6:
            continue
        lines[index] = "#" + lines[index]
        changes += 1

    if changes and apply_changes:
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return changes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Preserva um H1 por documento e desloca a hierarquia subsequente."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica as alterações.")
    parser.add_argument("paths", nargs="*", help="Arquivos ou diretórios; padrão: raiz atual.")
    args = parser.parse_args()

    targets = [Path(item) for item in args.paths] if args.paths else [Path(".")]
    files: set[Path] = set()
    for target in targets:
        if target.is_file() and target.suffix.lower() == ".md":
            files.add(target)
        elif target.is_dir():
            files.update(find_markdown_files(target))

    changed_files = 0
    changed_headings = 0
    for path in sorted(files):
        changes = normalize_file(path, args.apply)
        if changes:
            changed_files += 1
            changed_headings += changes
            action = "NORMALIZADO" if args.apply else "ALTERARIA"
            print(f"[{action}] {path}: {changes} título(s)")

    print(f"\nArquivos analisados: {len(files)}")
    print(f"Arquivos com alterações: {changed_files}")
    print(f"Títulos a ajustar: {changed_headings}")
    if not args.apply:
        print("Nenhum arquivo foi modificado.")


if __name__ == "__main__":
    main()
