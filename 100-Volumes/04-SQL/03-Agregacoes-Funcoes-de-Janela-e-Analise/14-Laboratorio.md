---
title: Laboratório — Métricas e Janelas da DataRetail
description: "Receita diária, ranking, variação e acumulado em SQLite."
tags: [sql, sqlite, window-functions, laboratorio]
aliases: [Laboratório Análise SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Métricas e Janelas da DataRetail

## Objetivo

Calcular métricas diárias, ranking por loja, variação e acumulado com frames determinísticos.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- `sqlite3` da biblioteca padrão;
- nenhuma dependência externa.

## Passos

1. Copie [[14-Solucao|a solução]] para `analise_sql.py`.
2. Execute:

```bash
python analise_sql.py
```

3. Remova o desempate do ranking e analise a estabilidade.
4. Troque o frame `ROWS` pelo padrão e compare peers.

## Resultado esperado

```text
dias=4
receita=600.00
top_loja=A
ultimo_acumulado=600.00
maior_variacao=50.00
ranking=deterministico
analise=ok
```

## Validação

O programa deve terminar com código zero e reconciliar receita agregada, último acumulado, variação e ranking.

## Conclusão

O laboratório prova que métricas analíticas são contratos testáveis de população, ordem e frame.
