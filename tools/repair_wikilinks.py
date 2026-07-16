from __future__ import annotations

import argparse
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from validate_project import (
    IGNORED_DIRECTORIES,
    WIKILINK_PATTERN,
    build_link_index,
    find_markdown_files,
    parse_frontmatter,
)


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"^\d{2}[- ]+", "", value)
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def add_candidate(index: dict[str, set[str]], key: str, target: str) -> None:
    if key.strip():
        index[normalized(key)].add(target)


def target_for(path: Path, root: Path) -> str:
    return path.relative_to(root).with_suffix("").as_posix()


def build_candidates(root: Path) -> dict[str, set[str]]:
    candidates: dict[str, set[str]] = defaultdict(set)
    for path in find_markdown_files(root):
        target = target_for(path, root)
        data, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        add_candidate(candidates, path.stem, target)
        add_candidate(candidates, re.sub(r"^\d{2}-", "", path.stem), target)
        if data:
            title = data.get("title")
            if isinstance(title, str):
                add_candidate(candidates, title, target)
            aliases = data.get("aliases")
            if isinstance(aliases, list):
                for alias in aliases:
                    add_candidate(candidates, str(alias), target)

    for readme in root.rglob("README.md"):
        if any(part in IGNORED_DIRECTORIES for part in readme.parts):
            continue
        target = target_for(readme, root)
        add_candidate(candidates, readme.parent.name, target)
        add_candidate(candidates, readme.parent.name.replace("-", " "), target)

    candidates[normalized("DataRetail S.A.")].add("030-Projetos/DataRetail Platform/README")
    candidates[normalized("DataRetail Platform")].add("030-Projetos/DataRetail Platform/README")
    return candidates


def valid_target(target: str, stems: set[str], paths: set[str], aliases: set[str]) -> bool:
    key = target.replace("\\", "/").strip().rstrip("/").casefold()
    return key in stems or key in paths or key in aliases


def rewrite_text(
    text: str,
    candidates: dict[str, set[str]],
    stems: set[str],
    paths: set[str],
    aliases: set[str],
) -> tuple[str, int, int]:
    mapped = 0
    unlinked = 0
    output: list[str] = []
    in_fence = False
    in_frontmatter = False

    def replace(match: re.Match[str]) -> str:
        nonlocal mapped, unlinked
        old_target = match.group(1).strip()
        if valid_target(old_target, stems, paths, aliases):
            return match.group(0)
        raw = match.group(0)
        inner = raw[2:-2]
        before_alias, separator, alias = inner.partition("|")
        target_without_anchor, anchor_separator, anchor = before_alias.partition("#")
        visible = alias if separator else target_without_anchor.rsplit("/", 1)[-1]
        matches = candidates.get(normalized(target_without_anchor), set())
        if len(matches) == 1:
            new_target = next(iter(matches))
            anchor_part = f"#{anchor}" if anchor_separator else ""
            mapped += 1
            return f"[[{new_target}{anchor_part}|{visible}]]"
        unlinked += 1
        return visible

    for number, line in enumerate(text.splitlines(keepends=True), start=1):
        if number == 1 and line.strip() == "---":
            in_frontmatter = True
            output.append(line)
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            output.append(line)
            continue
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            output.append(line)
            continue
        output.append(line if in_fence else WIKILINK_PATTERN.sub(replace, line))
    return "".join(output), mapped, unlinked


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Repara Wikilinks usando destinos existentes e remove links sem destino."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica as alterações.")
    parser.add_argument("--root", default=".", help="Raiz do Vault.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    candidates = build_candidates(root)
    stems, paths, aliases = build_link_index(root)
    changes: list[tuple[Path, str, int, int]] = []
    total_mapped = 0
    total_unlinked = 0

    for path in find_markdown_files(root):
        original = path.read_text(encoding="utf-8")
        updated, mapped, unlinked = rewrite_text(original, candidates, stems, paths, aliases)
        if mapped or unlinked:
            changes.append((path, updated, mapped, unlinked))
            total_mapped += mapped
            total_unlinked += unlinked

    print(f"Arquivos a atualizar: {len(changes)}")
    print(f"Links redirecionados: {total_mapped}")
    print(f"Links convertidos em texto: {total_unlinked}")
    for path, _, mapped, unlinked in changes:
        print(f"{path.relative_to(root)}: redirecionados={mapped}, texto={unlinked}")

    if not args.apply:
        print("\nSimulação concluída. Nenhum arquivo foi modificado.")
        return

    for path, updated, _, _ in changes:
        path.write_text(updated, encoding="utf-8", newline="\n")
    print("\nWikilinks reparados.")


if __name__ == "__main__":
    main()
