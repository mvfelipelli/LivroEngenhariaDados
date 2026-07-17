---
title: Origens, Padrões e Natureza Declarativa do SQL
description: "Evolução, famílias de comandos e separação entre intenção e execução."
tags: [sql, padrao-sql, linguagem-declarativa]
aliases: [Natureza Declarativa do SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Origens, Padrões e Natureza Declarativa do SQL

SQL surgiu de pesquisas sobre o modelo relacional e tornou-se uma família de padrões ISO/IEC 9075. O padrão define framework, linguagem de fundação e extensões; nenhum produto precisa implementar tudo para ser útil.

| Família didática | Responsabilidade | Exemplos |
| --- | --- | --- |
| DDL | definir estruturas | `CREATE`, `ALTER` |
| DQL | consultar | `SELECT` |
| DML | modificar dados | `INSERT`, `UPDATE`, `DELETE` |
| DCL | controlar acesso | `GRANT`, `REVOKE` |
| TCL | controlar transações | `COMMIT`, `ROLLBACK` |

Essas siglas são convenções pedagógicas; o padrão organiza a linguagem de forma mais formal.

```sql
SELECT nome
FROM clientes
WHERE ativo = 1;
```

A sentença não determina loop, arquivo ou índice. Ela define projeção, fonte e predicado. O SGBD deriva um plano equivalente.

> [!warning]
> SQL declarativo não significa desempenho automático. Estatísticas, modelagem, seletividade e forma da consulta afetam o plano escolhido.

Palavras-chave geralmente não diferenciam maiúsculas de minúsculas; nomes e regras de quoting variam. Prefira estilo consistente e recursos portáveis quando não houver benefício claro em uma extensão.
