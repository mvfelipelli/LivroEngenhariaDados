---
title: O que é Observabilidade de Dados
aliases: [Definição de Observabilidade de Dados]
tags: [observabilidade, fundamentos, telemetria]
created: 2026-07-16
updated: 2026-07-16
description: "Definição, escopo e perguntas centrais da observabilidade."
---

# O que é Observabilidade de Dados

Observabilidade é a capacidade de inferir e explicar estados internos a partir de saídas e evidências. Telemetria é a emissão e coleta dessas evidências. Monitoramento compara sinais com condições conhecidas. Diagnóstico interpreta sinais para testar hipóteses.

## Camadas observáveis

| Camada | Exemplos de perguntas |
|---|---|
| Infraestrutura | há saturação, perda ou limitação? |
| Aplicação | qual componente falhou ou ficou lento? |
| Pipeline | qual run, tarefa ou partição foi afetada? |
| Dados | houve atraso, ausência, desvio ou schema inesperado? |
| Produto | quais consumidores e decisões sofreram impacto? |

```mermaid
flowchart LR
    A[Emissão] --> B[Coleta]
    B --> C[Processamento]
    C --> D[Armazenamento]
    D --> E[Consulta e correlação]
    E --> F[Alerta, diagnóstico e aprendizado]
```

## Propriedades

Sinais precisam de cobertura, contexto, consistência temporal, granularidade e confiabilidade. A própria plataforma de observabilidade deve ser monitorada: perda de telemetria pode parecer ausência de falha.

> [!note]
> Observabilidade não elimina investigação. Ela reduz o espaço de hipóteses e preserva evidência para decisões melhores.

Os sinais fundamentais são detalhados em [[04-Logs-Metricas-Traces-e-Correlacao]].
