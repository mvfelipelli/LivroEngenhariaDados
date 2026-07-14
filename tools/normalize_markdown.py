from __future__ import annotations

import argparse
import re
from pathlib import Path


def normalize_file(path: Path, apply_changes: bool) -> int:
    original = path.read_text(encoding="utf-8")

    # Normaliza finais de linha.
    content = original.replace("\r\n", "\n").replace("\r", "\n")

    # Remove linhas em branco excedentes.
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Garante exatamente uma quebra de linha no final.
    content = content.rstrip() + "\n"

    if content == original:
        return 0

    if apply_changes:
        path.write_text(content, encoding="utf-8", newline="\n")

    return 1


def find_markdown_files(root: Path) -> list[Path]:
    ignored_directories = {
        ".git",
        ".obsidian",
        ".venv",
        "venv",
        "__pycache__",
        "999-Arquivos-Temporarios",
    }

    files: list[Path] = []

    for path in root.rglob("*.md"):
        if any(part in ignored_directories for part in path.parts):
            continue
        files.append(path)

    return sorted(files)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normaliza arquivos Markdown do projeto."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica as alterações. Sem essa opção, apenas simula.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Arquivos ou diretórios. O padrão é a raiz atual.",
    )
    args = parser.parse_args()

    targets = [Path(item) for item in args.paths] if args.paths else [Path(".")]
    markdown_files: set[Path] = set()

    for target in targets:
        if target.is_file() and target.suffix.lower() == ".md":
            markdown_files.add(target)
        elif target.is_dir():
            markdown_files.update(find_markdown_files(target))
        else:
            print(f"[IGNORADO] Caminho inexistente ou inválido: {target}")

    changed = 0

    for path in sorted(markdown_files):
        result = normalize_file(path, args.apply)

        if result:
            changed += 1
            status = "NORMALIZADO" if args.apply else "ALTERARIA"
            print(f"[{status}] {path}")

    print(f"\nArquivos analisados: {len(markdown_files)}")
    print(f"Arquivos com alterações: {changed}")

    if not args.apply:
        print("Nenhum arquivo foi modificado.")
        print("Execute novamente com --apply para aplicar as alterações.")


if __name__ == "__main__":
    main()
