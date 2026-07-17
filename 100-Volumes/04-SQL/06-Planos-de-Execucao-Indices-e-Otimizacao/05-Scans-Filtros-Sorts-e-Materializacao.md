---
title: Scans, Filtros, Sorts e Materialização
description: "Operadores fundamentais de acesso e transformação."
tags: [sql, scan, sort, materializacao]
aliases: [Operadores de Plano SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Scans, Filtros, Sorts e Materialização

Um plano é uma árvore: nós inferiores produzem linhas consumidas pelos nós superiores. O nome varia por produto, mas o trabalho fundamental é recorrente.

| Operador | Função | Sinal de atenção |
|---|---|---|
| Sequential/Table Scan | lê a relação | muitas linhas descartadas por filtro |
| Index Scan/Seek | localiza faixas no índice | muitos acessos aleatórios à tabela |
| Bitmap Scan | combina referências e lê páginas em lote | bitmap grande ou perda de precisão |
| Filter | aplica predicado | filtro tardio e baixa sobrevivência |
| Sort | ordena linhas | spill para disco |
| Hash Aggregate | agrupa em hash | lotes ou spill |
| Materialize | guarda saída reutilizável | intermediário volumoso |

Sequential scan não é defeito: para ler grande parcela de uma tabela, a leitura sequencial pode superar milhares de acessos aleatórios. Índice é vantajoso quando reduz trabalho suficiente.

## Ordenação evitável

```sql
SELECT pedido_id, criado_em, valor
FROM pedidos
WHERE cliente_id = 42
ORDER BY criado_em DESC
LIMIT 20;
```

Um índice iniciado por `(cliente_id, criado_em DESC)` pode filtrar e entregar a ordem pedida, permitindo parar cedo. Sem ele, o mecanismo pode filtrar e construir uma estrutura temporária para ordenar.

> [!note]
> Um operador caro no topo pode apenas acumular o custo dos filhos. Leia o plano de baixo para cima e observe o fluxo de linhas.
