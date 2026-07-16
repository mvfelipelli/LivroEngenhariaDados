---
title: Solução — Decisão Arquitetural Executável
aliases: [Solução do Laboratório de Arquitetura]
tags: [arquitetura, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável para matriz de decisão, fitness functions e ADR."
---

# Solução — Decisão Arquitetural Executável

```python
from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path


WEIGHTS = {
    "latencia": 0.25,
    "governanca": 0.25,
    "replay": 0.20,
    "custo": 0.15,
    "autonomia": 0.15,
}

SCORES = {
    "warehouse_centralizado": {
        "latencia": 2, "governanca": 5, "replay": 2, "custo": 4, "autonomia": 2,
    },
    "lakehouse_hibrido": {
        "latencia": 4, "governanca": 4, "replay": 5, "custo": 4, "autonomia": 3,
    },
    "orientada_a_eventos": {
        "latencia": 5, "governanca": 3, "replay": 4, "custo": 2, "autonomia": 4,
    },
}

CONFIGURATIONS = {
    "warehouse_centralizado": {
        "raw_imutavel": False,
        "retencao_dias": 365,
        "criptografia": True,
        "freshness_p99_minutos": 1440,
    },
    "lakehouse_hibrido": {
        "raw_imutavel": True,
        "retencao_dias": 2555,
        "criptografia": True,
        "freshness_p99_minutos": 5,
    },
    "orientada_a_eventos": {
        "raw_imutavel": True,
        "retencao_dias": 730,
        "criptografia": True,
        "freshness_p99_minutos": 1,
    },
}


def rank_alternatives() -> dict[str, float]:
    if round(sum(WEIGHTS.values()), 10) != 1.0:
        raise ValueError("Os pesos devem somar 1.0")
    ranking = {}
    for alternative, scores in SCORES.items():
        if set(scores) != set(WEIGHTS):
            raise ValueError(f"Critérios incompletos: {alternative}")
        if any(score < 1 or score > 5 for score in scores.values()):
            raise ValueError(f"Nota fora do intervalo: {alternative}")
        ranking[alternative] = sum(scores[item] * weight for item, weight in WEIGHTS.items())
    return ranking


def select(ranking: dict[str, float]) -> str:
    return sorted(ranking, key=lambda item: (-ranking[item], item))[0]


def apply_fitness_functions(configuration: dict) -> None:
    assert configuration["raw_imutavel"] is True, "A origem precisa permitir replay"
    assert configuration["retencao_dias"] >= 2555, "A retenção deve cobrir sete anos"
    assert configuration["criptografia"] is True, "Criptografia é obrigatória"
    assert configuration["freshness_p99_minutos"] <= 5, "O p99 deve ser de até cinco minutos"


def prepare(connection: sqlite3.Connection) -> None:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS adr (
            adr_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            alternativa TEXT NOT NULL,
            contexto TEXT NOT NULL,
            consequencias TEXT NOT NULL
        )
    """)
    connection.commit()


def persist_adr(connection: sqlite3.Connection, alternative: str) -> None:
    consequences = {
        "beneficios": ["replay", "baixa latencia", "interoperabilidade"],
        "custos": ["metadados", "operacao hibrida", "governanca"],
    }
    with connection:
        connection.execute("""
            INSERT INTO adr VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(adr_id) DO UPDATE SET
                status = excluded.status,
                alternativa = excluded.alternativa,
                contexto = excluded.contexto,
                consequencias = excluded.consequencias
        """, (
            "ADR-008",
            "aceito",
            alternative,
            "BI diário, operação em cinco minutos e replay por sete anos",
            json.dumps(consequences, ensure_ascii=False, sort_keys=True),
        ))


def main() -> None:
    ranking = rank_alternatives()
    alternative = select(ranking)
    apply_fitness_functions(CONFIGURATIONS[alternative])

    database = Path(tempfile.gettempdir()) / "dataretail_architecture.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare(connection)
        persist_adr(connection, alternative)
        persist_adr(connection, alternative)
        count = connection.execute("SELECT COUNT(*) FROM adr").fetchone()[0]
        assert count == 1

        for name in SCORES:
            print(f"{name}={ranking[name]:.2f}")
        print(f"alternativa={alternative}")
        print("fitness_functions=aprovadas")
        print(f"adrs_persistidos={count}")
        print("segunda_execucao=sem_duplicacao")
        print("arquitetura=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

## Leitura da solução

A matriz torna os critérios discutíveis e reproduzíveis. O ranking escolhe a maior pontuação e usa o nome como desempate estável. Em seguida, fitness functions aplicam restrições inegociáveis. O ADR é persistido duas vezes com upsert, demonstrando idempotência.

> [!warning]
> Pontuação não substitui experimentos, análise de risco ou responsabilidade. Notas frágeis devem motivar um protótipo, não falsa precisão.

Finalize em [[15-Referencias]].
