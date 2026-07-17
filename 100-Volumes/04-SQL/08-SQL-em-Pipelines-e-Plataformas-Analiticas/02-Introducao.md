---
title: Introdução
description: "Da consulta correta à transformação operacionalmente confiável."
tags: [sql, introducao, elt]
aliases: [Introdução ao SQL em Pipelines]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Uma consulta interativa é avaliada pelo resultado imediato. Em um pipeline, o mesmo SQL participa de agenda, dependências, retries, backfills, contratos e custos. Falhas podem ocorrer entre leitura, escrita e avanço do estado; dados podem chegar atrasados ou repetidos.

```mermaid
flowchart TD
    C["Contrato de entrada"] --> X["Transformação determinística"]
    X --> Q["Testes de qualidade"]
    Q --> A["Commit de dados e estado"]
    A --> O["Observabilidade"]
    O --> R["Retry ou backfill"]
    R --> X
```

A solução exige quatro propriedades: transformação determinística, chave estável, fronteira transacional e estado de progresso recuperável. Na DataRetail S.A., pedidos reenviados não podem duplicar receita, enquanto correções tardias precisam atualizar o fato já publicado.
