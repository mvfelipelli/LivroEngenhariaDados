---
title: Gabarito
description: "Respostas dos exercícios de segurança e governança SQL."
tags: [sql, gabarito, seguranca]
aliases: [Gabarito de Segurança SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Grão, colunas e tipos, semântica das métricas, filtros, tratamento de `NULL`, owner, política de compatibilidade e frescor são exemplos válidos.

## 2

Materialize quando o custo repetido é alto e atraso controlado é aceitável. Surgem refresh, armazenamento, monitoramento, reconciliação e comunicação de frescor.

## 3

`analista_leitura` recebe views aprovadas; `app_leitura` recebe somente objetos do runtime; `migration_executor` recebe DDL e é usado apenas pelo pipeline de implantação.

## 4

`ALL` permite operações sem necessidade e amplia impacto de falha. Conceda `USAGE` no schema e apenas `SELECT`, `INSERT` ou outra ação indispensável nos objetos explícitos.

## 5

Usuário da loja A enxerga A; não enxerga B; contexto ausente falha fechado. Teste também pool de conexões e role privilegiada separadamente.

## 6

O restante do cadastro e o sufixo podem permitir correlação ou reidentificação. Mascaramento reduz exposição visual, não remove vínculo com a pessoa.

## 7

```python
cursor.execute(
    "SELECT cliente_id, email FROM clientes WHERE email = ?",
    (email,),
)
```

## 8

Exija incidente ou ticket, aprovação independente, role mínima, credencial curta, janela definida, gravação de comandos/eventos, revogação automática e revisão pós-incidente.
