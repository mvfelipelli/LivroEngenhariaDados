---
title: Laboratório — Consultas Fundamentais da DataRetail
description: "Banco SQLite em memória com constraints e relatório relacional."
tags: [sql, sqlite, laboratorio, dataretail]
aliases: [Laboratório Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Consultas Fundamentais da DataRetail

## Objetivo

Criar um schema relacional em memória, carregar dados, validar constraints e produzir um relatório determinístico.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhuma dependência ou arquivo persistente.

## Passos

1. Copie o código de [[14-Solucao|Solução]] para `fundamentos_sql.py`.
2. Execute:

```bash
python fundamentos_sql.py
```

3. Inspecione a consulta com `LEFT JOIN`, `GROUP BY` e agregações.
4. Altere um pedido para valor negativo e confirme a falha da constraint.

## Resultado esperado

```text
clientes=3
pedidos=3
sem_pedidos=1
lider=Ana:350.00
integridade=ok
consulta=ok
```

## Validação

O programa deve terminar com código zero, produzir as seis linhas e comprovar que cliente sem pedido permanece no relatório.

## Conclusão

O laboratório conecta schema, integridade, ausência de correspondência, agregação e ordenação determinística.
