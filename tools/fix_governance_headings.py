from __future__ import annotations

import argparse
from pathlib import Path


FILES = (
    "README.md",
    "AGENTS.md",
    "EDITORIAL.md",
    "STYLE_GUIDE.md",
    "ARCHITECTURE.md",
    "ROADMAP.md",
    "MEMORY.md",
    "PROJECT_STATUS.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "Welcome.md",
)

def fix_headings(path: Path, apply_changes: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    inside_fence = False
    first_h1_found = False
    changes = 0
    output: list[str] = []

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            inside_fence = not inside_fence
            output.append(line)
            continue

        if not inside_fence and line.startswith("# "):
            if first_h1_found:
                line = "#" + line
                changes += 1
            else:
                first_h1_found = True

        output.append(line)

    if changes and apply_changes:
        path.write_text("".join(output), encoding="utf-8")

    return changes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Corrige múltiplos títulos H1 nos arquivos de governança."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica as correções. Sem esta opção, apenas simula.",
    )
    args = parser.parse_args()

    total = 0

    for filename in FILES:
        path = Path(filename)

        if not path.exists():
            print(f"[IGNORADO] {filename}: arquivo não encontrado")
            continue

        changes = fix_headings(path, args.apply)
        total += changes

        action = "CORRIGIDO" if args.apply else "SIMULAÇÃO"
        print(f"[{action}] {filename}: {changes} título(s) a alterar")

    print(f"\nTotal: {total} alteração(ões).")

    if not args.apply:
        print("Nenhum arquivo foi modificado.")
        print("Use --apply após revisar o resultado.")


if __name__ == "__main__":
    main()
