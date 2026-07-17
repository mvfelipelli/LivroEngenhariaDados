---
title: Introdução
description: "Da semântica conceitual às relações consistentes."
tags: [modelagem-de-dados, introducao, relacional]
aliases: [Introdução à Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Uma planilha que repete nome de cliente em cada pedido parece prática, mas permite atualizar apenas algumas linhas, impede cadastrar cliente sem pedido e perde cadastro ao apagar a última venda. São anomalias de atualização, inserção e exclusão.

```mermaid
flowchart TD
    S["Regras do domínio"] --> F["Dependências funcionais"]
    F --> K["Chaves candidatas"]
    K --> N["Formas normais"]
    N --> T["Relações e constraints"]
    T --> V["Consultas de validação"]
```

Normalizar não significa criar o maior número de tabelas. O objetivo é representar cada fato uma vez, no lugar em que sua identidade e dependências possam ser protegidas.
