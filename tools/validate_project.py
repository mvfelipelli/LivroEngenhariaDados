from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".venv",
    "venv",
    "__pycache__",
    "999-Arquivos-Temporarios",
}


def find_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*.md"):
        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue
        files.append(path)

    return sorted(files)


def run_pymarkdown(files: list[Path], config: Path) -> int:
    if not files:
        print("Nenhum arquivo Markdown encontrado.")
        return 0

    command = [
        sys.executable,
        "-m",
        "pymarkdown",
        "--config",
        str(config),
        "scan",
        *[str(path) for path in files],
    ]

    print("Executando validação Markdown...\n")
    result = subprocess.run(command, check=False)

    return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Valida os arquivos Markdown do projeto."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Arquivo ou diretório a validar. O padrão é a raiz atual.",
    )
    parser.add_argument(
        "--config",
        default=".pymarkdown.json",
        help="Arquivo de configuração do PyMarkdown.",
    )
    args = parser.parse_args()

    target = Path(args.path)
    config = Path(args.config)

    if not config.exists():
        print(f"Erro: configuração não encontrada: {config}")
        raise SystemExit(2)

    if target.is_file():
        if target.suffix.lower() != ".md":
            print(f"Erro: o arquivo não é Markdown: {target}")
            raise SystemExit(2)
        files = [target]
    elif target.is_dir():
        files = find_markdown_files(target)
    else:
        print(f"Erro: caminho não encontrado: {target}")
        raise SystemExit(2)

    print(f"Arquivos encontrados: {len(files)}")

    return_code = run_pymarkdown(files, config)

    if return_code == 0:
        print("\nValidação concluída sem erros.")
    else:
        print("\nValidação concluída com erros ou avisos bloqueantes.")

    raise SystemExit(return_code)


if __name__ == "__main__":
    main()
