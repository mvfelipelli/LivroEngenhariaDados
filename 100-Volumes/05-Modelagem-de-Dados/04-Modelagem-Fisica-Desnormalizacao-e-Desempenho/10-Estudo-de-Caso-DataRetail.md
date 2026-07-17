---
title: Estudo de Caso — DataRetail S.A.
description: "Modelo físico do histórico de pedidos por cliente."
tags: [modelagem-de-dados, estudo-de-caso, dataretail, desempenho]
aliases: [Caso DataRetail Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

O atendimento da DataRetail consulta os 20 pedidos recentes de um cliente; o financeiro agrega receita mensal; a operação escreve milhares de pedidos por minuto.

## Decisões

- chaves `BIGINT` internas e unicidade dos identificadores de origem;
- valores em centavos e instantes com timezone;
- índice `(cliente_id, criado_em DESC)` para atendimento;
- particionamento mensal do histórico para retenção;
- fato colunar separado para analytics;
- resumo diário derivado, com reconstrução a partir dos pedidos;
- métricas de custo de escrita e tamanho dos índices.

```mermaid
flowchart LR
    P["Pedidos normalizados"] --> I["Índice por cliente e data"]
    P --> CDC["Mudanças"]
    CDC --> F["Fato colunar particionado"]
    F --> R["Resumo diário"]
```

O desenho não força um único armazenamento a atender workloads incompatíveis. Identidade e regras permanecem comuns; projeções são reconciliáveis.
