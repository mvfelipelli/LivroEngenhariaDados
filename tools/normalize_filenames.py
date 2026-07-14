from __future__ import annotations

import argparse
import re
import subprocess
import unicodedata
from pathlib import Path


IGNORED_DIRECTORIES = {".git", ".obsidian", ".venv", "venv", "__pycache__"}
CONTENT_DIRECTORIES = ("000-Atlas", "005-Wiki", "100-Volumes")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]")


def normalized_name(name: str) -> str:
    stem = Path(name).stem
    stem = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode()
    stem = re.sub(r"\s*-\s*", "-", stem)
    stem = re.sub(r"\s+", "-", stem)
    stem = re.sub(r"[^A-Za-z0-9-]+", "-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-")
    return f"{stem}.md"


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in IGNORED_DIRECTORIES for part in path.parts)
    )


def build_mapping(root: Path) -> dict[Path, Path]:
    mapping: dict[Path, Path] = {}
    for directory in CONTENT_DIRECTORIES:
        content_root = root / directory
        if not content_root.exists():
            continue
        for path in markdown_files(content_root):
            new_path = path.with_name(normalized_name(path.name))
            if new_path != path:
                mapping[path] = new_path
    return mapping


def validate_mapping(mapping: dict[Path, Path]) -> None:
    targets: dict[str, Path] = {}
    sources = set(mapping)
    for source, target in mapping.items():
        key = str(target).casefold()
        if key in targets:
            raise ValueError(f"Colisão: {source} e {targets[key]} -> {target}")
        if target.exists() and target not in sources:
            raise ValueError(f"Destino já existe: {target}")
        targets[key] = source


def target_maps(root: Path, mapping: dict[Path, Path]) -> tuple[dict[str, str], dict[str, str]]:
    stems: dict[str, str] = {}
    paths: dict[str, str] = {}
    for source, target in mapping.items():
        stems[source.stem] = target.stem
        old_relative = source.relative_to(root).with_suffix("").as_posix()
        new_relative = target.relative_to(root).with_suffix("").as_posix()
        paths[old_relative] = new_relative
    return stems, paths


def rewrite_wikilinks(text: str, stems: dict[str, str], paths: dict[str, str]) -> tuple[str, int]:
    changes = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changes
        old_target = match.group(1)
        anchor = match.group(2) or ""
        alias = match.group(3)
        normalized_target = old_target.replace("\\", "/")
        new_target = paths.get(normalized_target) or stems.get(old_target)
        if not new_target or new_target == old_target:
            return match.group(0)
        changes += 1
        visible_text = alias or old_target.rsplit("/", 1)[-1]
        return f"[[{new_target}{anchor}|{visible_text}]]"

    return WIKILINK_PATTERN.sub(replace, text), changes


def rename_with_git(source: Path, target: Path) -> None:
    result = subprocess.run(
        ["git", "mv", "--", str(source), str(target)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"Falha ao renomear {source}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normaliza nomes Markdown e atualiza Wikilinks relacionados."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica a migração.")
    parser.add_argument("--root", default=".", help="Raiz do Vault.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    mapping = build_mapping(root)
    validate_mapping(mapping)
    stems, paths = target_maps(root, mapping)

    changed_files: list[tuple[Path, str]] = []
    link_changes = 0
    for path in markdown_files(root):
        original = path.read_text(encoding="utf-8")
        updated, changes = rewrite_wikilinks(original, stems, paths)
        if changes:
            changed_files.append((path, updated))
            link_changes += changes

    print(f"Arquivos a renomear: {len(mapping)}")
    print(f"Arquivos com Wikilinks a atualizar: {len(changed_files)}")
    print(f"Wikilinks a atualizar: {link_changes}")
    for source, target in mapping.items():
        print(f"{source.relative_to(root)} -> {target.name}")

    if not args.apply:
        print("\nSimulação concluída. Nenhum arquivo foi modificado.")
        return

    for path, updated in changed_files:
        path.write_text(updated, encoding="utf-8", newline="\n")
    for source, target in mapping.items():
        rename_with_git(source, target)

    print("\nMigração concluída.")


if __name__ == "__main__":
    main()
