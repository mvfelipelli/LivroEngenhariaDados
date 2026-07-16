---
title: Linhagem, Dependências e Análise de Impacto
aliases: [Linhagem Operacional, Análise de Impacto]
tags: [observabilidade, linhagem, dependencias, impacto]
created: 2026-07-16
updated: 2026-07-16
description: "Uso de grafos e metadados para diagnóstico e propagação de incidentes."
---

# Linhagem, Dependências e Análise de Impacto

Linhagem conecta fontes, transformações, datasets e consumidores. Dependência técnica mostra conexão; dependência operacional acrescenta versão, partição, run e estado efetivamente executados.

```mermaid
flowchart LR
    A[ERP pedidos] --> B[raw_pedidos]
    B --> C[stg_pedidos]
    C --> D[mart_vendas]
    C --> E[visao_operacional]
    D --> F[Dashboard financeiro]
    E --> G[Aplicação logística]
```

## Análise upstream e downstream

Upstream ajuda a procurar causas e mudanças de origem. Downstream identifica produtos, equipes e decisões afetadas. A travessia deve considerar tempo: uma tabela pode depender de uma versão antiga, não da execução mais recente.

## Granularidade

Linhagem por sistema é barata e ampla; por dataset é útil para impacto; por coluna explica propagação semântica; por registro costuma ser cara e reservada a requisitos específicos. Escolha segundo risco e pergunta.

## Correlação operacional

Associe nós e arestas a `run_id`, partição, código, schema e qualidade. Assim, um alerta de freshness pode localizar a tarefa lenta e enumerar consumidores dentro do SLO afetado.

> [!note]
> Linhagem declarada mostra intenção; linhagem capturada em execução mostra comportamento. Compare ambas para detectar caminhos inesperados.

Impacto orienta os objetivos de [[07-SLIs-SLOs-Alertas-e-Dashboards]].
