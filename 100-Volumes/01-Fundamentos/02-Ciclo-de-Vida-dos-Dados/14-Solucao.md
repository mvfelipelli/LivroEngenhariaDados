---
title: Solução — Pipeline do Ciclo de Vida
aliases: [Solução do Laboratório do Ciclo de Vida]
tags: [engenharia-de-dados, fundamentos, solucao, python, ciclo-de-vida]
type: solution
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Solução comentada do laboratório do pipeline do ciclo de vida."
---

# 14 — Solução do Laboratório

## Implementação

Salve como `pipeline.py`:

```python
from __future__ import annotations

import csv
import hashlib
import json
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
INPUT = ROOT / "input" / "pedidos.csv"
FIELDS = ["event_id", "order_id", "channel", "occurred_at", "total", "status"]
ALLOWED_STATUS = {"confirmed", "cancelled"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def validate(row: dict[str, str]) -> str | None:
    if any(not row.get(field) for field in FIELDS):
        return "required_field_missing"
    try:
        if float(row["total"]) < 0:
            return "negative_total"
    except ValueError:
        return "invalid_total"
    if row["status"] not in ALLOWED_STATUS:
        return "invalid_status"
    return None


def main() -> None:
    raw = ROOT / "raw" / INPUT.name
    raw.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(INPUT, raw)

    valid: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    seen: set[str] = set()

    with raw.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError("Schema incompatível")
        for row in reader:
            reason = validate(row)
            if reason:
                rejected.append({**row, "reason": reason})
            elif row["event_id"] not in seen:
                seen.add(row["event_id"])
                valid.append(row)

    write_csv(ROOT / "valid" / "eventos.csv", FIELDS, valid)
    write_csv(ROOT / "quarantine" / "rejeitados.csv", FIELDS + ["reason"], rejected)

    current: dict[str, dict[str, str]] = {}
    for row in sorted(valid, key=lambda item: item["occurred_at"]):
        current[row["order_id"]] = row
    current_rows = sorted(current.values(), key=lambda item: item["order_id"])
    write_csv(ROOT / "product" / "pedidos_atuais.csv", FIELDS, current_rows)

    totals: defaultdict[str, float] = defaultdict(float)
    for row in current_rows:
        if row["status"] == "confirmed":
            totals[row["channel"]] += float(row["total"])
    summary = [{"channel": channel, "total": f"{total:.2f}"}
               for channel, total in sorted(totals.items())]
    write_csv(ROOT / "product" / "resumo_canais.csv", ["channel", "total"], summary)

    manifest = {
        "input_sha256": sha256(raw),
        "input_rows": 6,
        "valid_unique_events": len(valid),
        "rejected_rows": len(rejected),
        "current_orders": len(current_rows),
        "confirmed_orders": sum(row["status"] == "confirmed" for row in current_rows),
    }
    manifest_path = ROOT / "product" / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    archive = ROOT / "archive"
    archive.mkdir(exist_ok=True)
    for source in [ROOT / "valid" / "eventos.csv", manifest_path]:
        target = archive / source.name
        shutil.copyfile(source, target)
        if sha256(source) != sha256(target):
            raise RuntimeError(f"Falha de integridade: {source.name}")

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
```

## Resultado esperado

```json
{
  "input_rows": 6,
  "valid_unique_events": 3,
  "rejected_rows": 2,
  "current_orders": 2,
  "confirmed_orders": 1
}
```

`input_sha256` varia apenas se a entrada mudar.

## Por que a solução é idempotente?

Os arquivos de saída são reescritos integralmente a partir da entrada preservada. Executar novamente não acrescenta linhas ao resultado.

## Limitações didáticas

- carrega tudo em memória;
- não implementa concorrência;
- aceita um arquivo;
- usa ordenação textual de timestamps ISO 8601 uniformes;
- não substitui armazenamento transacional;
- retenção é discutida, mas não automatizada.

Em produção, volume, atomicidade, catálogo, segredos, monitoramento e recuperação exigiriam componentes adicionais.

## Verificação final

- `valid/eventos.csv`: três eventos;
- `quarantine/rejeitados.csv`: dois registros;
- `product/pedidos_atuais.csv`: `p100` cancelado e `p101` confirmado;
- `product/resumo_canais.csv`: canal `store`, total `80.00`;
- `archive`: cópias verificadas.

## Próximo Capítulo

➡️ [[15-Referencias|15 — Referências]]
