from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


IGNORED_DIRECTORIES = {".git", ".obsidian", ".venv", "venv", "__pycache__"}
CONTENT_DIRECTORIES = ("000-Atlas", "005-Wiki", "050-Templates", "100-Volumes")
EXCLUDED_FILES = {"CHANGELOG.md", "SUMMARY.md"}
REQUIRED_FIELDS = ("title", "description", "tags", "aliases", "created", "updated")


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for directory in CONTENT_DIRECTORIES:
        content_root = root / directory
        if not content_root.exists():
            continue
        files.extend(
            path
            for path in content_root.rglob("*.md")
            if path.name not in EXCLUDED_FILES
            and path.stat().st_size > 0
            and not any(part in IGNORED_DIRECTORIES for part in path.parts)
        )
    return sorted(files)


def frontmatter_bounds(text: str) -> tuple[int, int] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return (4, end) if end >= 0 else None


def existing_fields(raw: str) -> set[str]:
    return {
        match.group(1)
        for line in raw.splitlines()
        if (match := re.match(r"^([A-Za-z][A-Za-z0-9_-]*):", line))
    }


def title_from(path: Path, text: str, raw: str | None) -> str:
    if raw:
        match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', raw, re.MULTILINE)
        if match and match.group(1).strip():
            return match.group(1).strip()
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    if path.name == "README.md":
        return path.parent.name.replace("-", " ")
    return path.stem.replace("-", " ")


def description_for(path: Path, title: str) -> str:
    parts = set(path.parts)
    if "Glossario" in parts:
        return f"Definição e contexto de {title} na Engenharia de Dados."
    if path.name == "README.md":
        return f"Visão geral, objetivos e navegação de {title}."
    if "050-Templates" in parts:
        return f"Template editorial para {title}."
    if "100-Volumes" in parts:
        return f"Capítulo técnico sobre {title} na Formação em Engenharia de Dados."
    return f"Página de navegação e referência sobre {title}."


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def missing_lines(fields: set[str], title: str, description: str, date: str) -> list[str]:
    values = {
        "title": f"title: {yaml_string(title)}",
        "description": f"description: {yaml_string(description)}",
        "tags": "tags: []",
        "aliases": "aliases: []",
        "created": f'created: "{date}"',
        "updated": f'updated: "{date}"',
    }
    return [values[field] for field in REQUIRED_FIELDS if field not in fields]


def normalize(path: Path, date: str) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    bounds = frontmatter_bounds(text)
    raw = text[bounds[0] : bounds[1]] if bounds else None
    fields = existing_fields(raw or "")
    title = title_from(path, text, raw)
    additions = missing_lines(fields, title, description_for(path, title), date)
    if not additions:
        return text, []
    if bounds:
        insertion = "\n".join(additions)
        updated = text[: bounds[1]].rstrip() + "\n" + insertion + text[bounds[1] :]
    else:
        header = "---\n" + "\n".join(additions) + "\n---\n\n"
        updated = header + text.lstrip("\n")
    return updated, additions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Completa o frontmatter obrigatório dos documentos editoriais."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica as alterações.")
    parser.add_argument("--root", default=".", help="Raiz do Vault.")
    parser.add_argument("--date", default="2026-07-14", help="Data usada nos campos ausentes.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changes: list[tuple[Path, str, list[str]]] = []
    for path in markdown_files(root):
        updated, additions = normalize(path, args.date)
        if additions:
            changes.append((path, updated, additions))

    print(f"Documentos analisados: {len(markdown_files(root))}")
    print(f"Documentos a atualizar: {len(changes)}")
    for path, _, additions in changes:
        fields = ", ".join(line.split(":", 1)[0] for line in additions)
        print(f"{path.relative_to(root)}: {fields}")

    if not args.apply:
        print("\nSimulação concluída. Nenhum arquivo foi modificado.")
        return

    for path, updated, _ in changes:
        path.write_text(updated, encoding="utf-8", newline="\n")
    print("\nFrontmatter atualizado.")


if __name__ == "__main__":
    main()
