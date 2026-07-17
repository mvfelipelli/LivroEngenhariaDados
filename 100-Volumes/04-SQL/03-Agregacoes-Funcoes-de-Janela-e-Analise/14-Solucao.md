---
title: Solução — Métricas e Janelas da DataRetail
description: "Implementação SQLite validada do laboratório."
tags: [sql, sqlite, window-functions, solucao]
aliases: [Solução Laboratório Análise SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Métricas e Janelas da DataRetail

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE vendas (
        venda_id INTEGER PRIMARY KEY,
        dia TEXT NOT NULL,
        loja TEXT NOT NULL,
        valor NUMERIC NOT NULL
    );
    INSERT INTO vendas VALUES
        (1, '2026-07-01', 'A', 100),
        (2, '2026-07-01', 'B', 50),
        (3, '2026-07-02', 'A', 150),
        (4, '2026-07-03', 'B', 200),
        (5, '2026-07-04', 'A', 100);
    """
)

daily = db.execute(
    """
    WITH por_dia AS (
        SELECT dia, SUM(valor) AS receita
        FROM vendas GROUP BY dia
    )
    SELECT
        dia,
        receita,
        LAG(receita) OVER (ORDER BY dia) AS anterior,
        SUM(receita) OVER (
            ORDER BY dia
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS acumulado
    FROM por_dia
    ORDER BY dia
    """
).fetchall()

ranking = db.execute(
    """
    WITH por_loja AS (
        SELECT loja, SUM(valor) AS receita FROM vendas GROUP BY loja
    )
    SELECT loja, receita,
           ROW_NUMBER() OVER (ORDER BY receita DESC, loja) AS posicao
    FROM por_loja ORDER BY posicao
    """
).fetchall()

revenue = sum(float(row[1]) for row in daily)
changes = [float(row[1] - row[2]) for row in daily if row[2] is not None]

assert len(daily) == 4
assert revenue == 600.0
assert float(daily[-1][3]) == revenue
assert max(changes) == 50.0
assert ranking[0] == ("A", 350, 1)

print(f"dias={len(daily)}")
print(f"receita={revenue:.2f}")
print(f"top_loja={ranking[0][0]}")
print(f"ultimo_acumulado={float(daily[-1][3]):.2f}")
print(f"maior_variacao={max(changes):.2f}")
print("ranking=deterministico")
print("analise=ok")
db.close()
```

A consulta agrega antes de aplicar janelas. As assertions reconciliam detalhe, série diária, acumulado e ranking.
