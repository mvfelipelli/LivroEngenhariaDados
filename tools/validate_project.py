from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".venv",
    "venv",
    "__pycache__",
    "999-Arquivos-Temporarios",
}
CONTENT_DIRECTORIES = ("000-Atlas", "005-Wiki", "100-Volumes")
FRONTMATTER_DIRECTORIES = ("000-Atlas", "005-Wiki", "050-Templates", "100-Volumes")
REQUIRED_FRONTMATTER = {"title", "description", "tags", "aliases", "created", "updated"}
FRONTMATTER_EXCLUDED_FILES = {"CHANGELOG.md", "SUMMARY.md"}
AVAILABLE_CHECKS = ("markdown", "yaml", "names", "wikilinks", "modules")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass(frozen=True)
class Issue:
    check: str
    path: Path
    message: str
    line: int | None = None

    def render(self, root: Path) -> str:
        try:
            location = self.path.resolve().relative_to(root.resolve())
        except ValueError:
            location = self.path
        suffix = f":{self.line}" if self.line else ""
        return f"[{self.check}] {location}{suffix}: {self.message}"


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRECTORIES for part in path.parts)


def find_markdown_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() == ".md" else []
    return sorted(path for path in target.rglob("*.md") if not is_ignored(path))


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, str | None]:
    if not text.startswith("---\n"):
        return None, "frontmatter YAML ausente"
    end = text.find("\n---", 4)
    if end < 0:
        return None, "frontmatter YAML não foi encerrado"
    raw = text[4:end]
    data: dict[str, object] = {}
    current_list: str | None = None
    for number, line in enumerate(raw.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s+-\s+(.+)$", line)
        if list_match and current_list:
            value = data.setdefault(current_list, [])
            if isinstance(value, list):
                value.append(list_match.group(1).strip().strip('"\''))
            continue
        key_match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not key_match:
            return None, f"YAML simples inválido na linha {number}"
        key, value = key_match.groups()
        value = (value or "").strip()
        if value in {"", "[]"}:
            data[key] = [] if value == "[]" else None
            current_list = key
        else:
            data[key] = value.strip('"\'')
            current_list = None
    return data, None


def is_in_directories(path: Path, root: Path, directories: tuple[str, ...]) -> bool:
    try:
        relative = path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return bool(relative.parts and relative.parts[0] in directories)


def check_yaml(files: list[Path], root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in files:
        if (
            path.stat().st_size == 0
            or path.name in FRONTMATTER_EXCLUDED_FILES
            or not is_in_directories(path, root, FRONTMATTER_DIRECTORIES)
        ):
            continue
        data, error = parse_frontmatter(path.read_text(encoding="utf-8"))
        if error:
            issues.append(Issue("yaml", path, error, 1))
            continue
        missing = sorted(REQUIRED_FRONTMATTER - set(data or {}))
        if missing:
            issues.append(Issue("yaml", path, f"campos obrigatórios ausentes: {', '.join(missing)}", 1))
    return issues


def check_names(files: list[Path], root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in files:
        if not is_in_directories(path, root, CONTENT_DIRECTORIES):
            continue
        if re.search(r"\s", path.name) or any(ord(character) > 127 for character in path.name):
            issues.append(Issue("names", path, "nome deve usar hífens, sem espaços ou acentos"))
    return issues


def build_link_index(root: Path) -> tuple[set[str], set[str], set[str]]:
    stems: set[str] = set()
    relative_paths: set[str] = set()
    aliases: set[str] = set()
    for path in find_markdown_files(root):
        stems.add(path.stem.casefold())
        relative = path.relative_to(root).with_suffix("")
        parts = relative.parts
        relative_paths.add(relative.as_posix().casefold())
        for start in range(1, len(parts) - 1):
            relative_paths.add(Path(*parts[start:]).as_posix().casefold())
        data, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        if data and isinstance(data.get("aliases"), list):
            aliases.update(str(alias).casefold() for alias in data["aliases"])
    return stems, relative_paths, aliases


def check_wikilinks(files: list[Path], root: Path) -> list[Issue]:
    stems, relative_paths, aliases = build_link_index(root)
    issues: list[Issue] = []
    for path in files:
        in_fence = False
        in_frontmatter = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if number == 1 and line.strip() == "---":
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
            for match in WIKILINK_PATTERN.finditer(line):
                target = match.group(1).replace("\\", "/").strip().rstrip("/").casefold()
                if target in stems or target in relative_paths or target in aliases:
                    continue
                issues.append(Issue("wikilinks", path, f"destino não encontrado: [[{match.group(1)}]]", number))
    return issues


def completed_module_directories(root: Path) -> list[Path]:
    volumes = root / "100-Volumes"
    modules: list[Path] = []
    if not volumes.exists():
        return modules
    for volume in volumes.iterdir():
        if not volume.is_dir():
            continue
        for module in volume.iterdir():
            if not module.is_dir() or not re.match(r"^\d{2}-", module.name):
                continue
            readme = module / "README.md"
            if not readme.exists() or not readme.stat().st_size:
                continue
            data, _ = parse_frontmatter(readme.read_text(encoding="utf-8"))
            if not data or str(data.get("type", "")).casefold() not in {"module", "modulo", "módulo"}:
                continue
            status = str(data.get("status", "")).casefold().replace("í", "i").replace("-", " ")
            if status in {"concluido", "completo", "concluida", "completa"}:
                modules.append(module)
    return sorted(modules)


def check_modules(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    required_patterns = {
        "README": r"^README\.md$",
        "Objetivos": r"^01-.*\.md$",
        "Introdução": r"^02-.*\.md$",
        "Estudo de Caso": r"^10-.*\.md$",
        "Resumo": r"^11-.*\.md$",
        "Perguntas de Entrevista": r"^12-.*\.md$",
        "Exercícios": r"^13-Exercicios\.md$",
        "Gabarito": r"^13-Gabarito\.md$",
        "Laboratório": r"^14-Laboratorio\.md$",
        "Solução": r"^14-Solucao\.md$",
        "Referências": r"^15-Referencias\.md$",
    }
    for module in completed_module_directories(root):
        names = [path.name for path in module.glob("*.md") if path.stat().st_size]
        for label, pattern in required_patterns.items():
            if not any(re.match(pattern, name) for name in names):
                issues.append(Issue("modules", module, f"componente obrigatório ausente: {label}"))
    return issues


def run_pymarkdown(files: list[Path], config: Path, root: Path) -> list[Issue]:
    if not files:
        return []
    issues: list[Issue] = []
    pattern = re.compile(r"^(.*?):(\d+):\d+:\s+(MD\d+):\s+(.*)$")

    # Evita exceder o limite de comprimento da linha de comando no Windows
    # à medida que o Vault cresce.
    for start in range(0, len(files), 100):
        batch = files[start:start + 100]
        command = [
            sys.executable,
            "-m",
            "pymarkdown",
            "--config",
            str(config),
            "--enable-extensions",
            "front-matter,markdown-tables,markdown-task-list-items",
            "scan",
            *map(str, batch),
        ]
        result = subprocess.run(command, check=False, capture_output=True, text=True)
        batch_issues = 0
        for line in (result.stdout + result.stderr).splitlines():
            match = pattern.match(line)
            if match:
                path, number, rule, message = match.groups()
                issues.append(Issue("markdown", Path(path), f"{rule}: {message}", int(number)))
                batch_issues += 1
        if result.returncode != 0 and batch_issues == 0:
            issues.append(Issue("markdown", root, "PyMarkdown falhou sem diagnóstico estruturado"))

    return issues


def check_multiple_h1(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in files:
        in_frontmatter = False
        in_fence = False
        h1_lines: list[int] = []
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if number == 1 and line.strip() == "---":
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
            if not in_fence and re.match(r"^#\s+", line):
                h1_lines.append(number)
        for number in h1_lines[1:]:
            issues.append(Issue("markdown", path, "mais de um título H1 no documento", number))
    return issues


def parse_checks(value: str) -> tuple[str, ...]:
    checks = tuple(item.strip() for item in value.split(",") if item.strip())
    invalid = sorted(set(checks) - set(AVAILABLE_CHECKS))
    if invalid:
        raise argparse.ArgumentTypeError(f"verificações desconhecidas: {', '.join(invalid)}")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser(description="Valida conteúdo, estrutura e navegação do Vault.")
    parser.add_argument("path", nargs="?", default=".", help="Arquivo ou diretório a validar.")
    parser.add_argument("--config", default=".pymarkdown.json", help="Configuração do PyMarkdown.")
    parser.add_argument(
        "--checks",
        type=parse_checks,
        default=AVAILABLE_CHECKS,
        help=f"Lista separada por vírgulas: {','.join(AVAILABLE_CHECKS)}.",
    )
    parser.add_argument("--max-issues", type=int, default=100, help="Máximo de problemas exibidos.")
    args = parser.parse_args()

    root = Path.cwd().resolve()
    target = Path(args.path).resolve()
    config = Path(args.config).resolve()
    if not target.exists():
        parser.error(f"caminho não encontrado: {target}")
    if "markdown" in args.checks and not config.exists():
        parser.error(f"configuração não encontrada: {config}")

    files = find_markdown_files(target)
    if target.is_file() and not files:
        parser.error(f"o arquivo não é Markdown: {target}")

    results: dict[str, list[Issue]] = {}
    for check in args.checks:
        if check == "markdown":
            results[check] = run_pymarkdown(files, config, root) + check_multiple_h1(files)
        elif check == "yaml":
            results[check] = check_yaml(files, root)
        elif check == "names":
            results[check] = check_names(files, root)
        elif check == "wikilinks":
            results[check] = check_wikilinks(files, root)
        elif check == "modules":
            results[check] = check_modules(root)

    issues = [issue for check in args.checks for issue in results[check]]
    print(f"Arquivos Markdown analisados: {len(files)}")
    print("Resumo:")
    for check in args.checks:
        status = "OK" if not results[check] else f"{len(results[check])} problema(s)"
        print(f"  {check}: {status}")

    if issues:
        print(f"\nProblemas (mostrando até {args.max_issues}):")
        for issue in issues[: args.max_issues]:
            print(issue.render(root))
        hidden = len(issues) - args.max_issues
        if hidden > 0:
            print(f"... {hidden} problema(s) adicional(is) omitido(s).")
        raise SystemExit(1)

    print("\nValidação concluída sem erros.")


if __name__ == "__main__":
    main()
