---
title: Estudo de Caso — DataRetail S.A.
description: "Otimização do histórico de pedidos por cliente."
tags: [sql, estudo-de-caso, dataretail, indices]
aliases: [Caso DataRetail Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

O atendimento da DataRetail S.A. consulta os 20 pedidos mais recentes de um cliente. Com 180 milhões de pedidos, a latência p95 alcançou 4,8 segundos.

```sql
SELECT pedido_id, criado_em, valor, status
FROM pedidos
WHERE cliente_id = :cliente_id
ORDER BY criado_em DESC
LIMIT 20;
```

## Diagnóstico

O baseline revelou leitura extensa e ordenação temporária. A consulta retornava poucas linhas, mas o caminho disponível não combinava filtro e ordem. O índice existente começava por `status`, coluna ausente no predicado.

## Hipótese e intervenção

```sql
CREATE INDEX CONCURRENTLY idx_pedidos_cliente_criado
ON pedidos (cliente_id, criado_em DESC)
INCLUDE (valor, status);
```

O índice alinha igualdade, ordenação e projeção. Em PostgreSQL, `CONCURRENTLY` reduz bloqueios sobre escritas, embora demande mais trabalho e acompanhamento operacional.

## Validação

- conjunto de resultados comparado para clientes pequenos e grandes;
- plano passou a buscar a faixa do cliente e parar no limite;
- ordenação temporária desapareceu;
- latência p95 caiu para 38 ms no ensaio representativo;
- impacto na carga de escrita e tamanho do índice foi monitorado.

```mermaid
flowchart LR
    Q["Filtro por cliente"] --> I["Índice cliente + data"]
    I --> O["Ordem já disponível"]
    O --> L["Parada após 20 linhas"]
```

O ganho não veio de “usar índice” de modo abstrato, mas de evitar leitura, sort e processamento que não contribuíam para o resultado.
