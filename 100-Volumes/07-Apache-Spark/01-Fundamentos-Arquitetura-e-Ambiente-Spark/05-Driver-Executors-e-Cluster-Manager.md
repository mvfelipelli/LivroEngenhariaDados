---
title: Driver, Executors e Cluster Manager
description: "Responsabilidades dos processos e da gestão de recursos."
tags: [apache-spark, driver, executor, cluster]
aliases: [Arquitetura Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Driver, Executors e Cluster Manager

O driver executa o programa principal, constrói planos e coordena tasks. Executors executam tasks, mantêm partições em cache e devolvem resultados. O cluster manager aloca recursos; ele não interpreta o plano de dados.

```mermaid
flowchart TB
    U["Aplicação"] --> DR["Driver"]
    DR --> CM["Cluster manager"]
    CM --> E1["Executor A"]
    CM --> E2["Executor B"]
    DR <--> E1
    DR <--> E2
```

`collect()` move dados ao driver e pode esgotar sua memória. Variáveis locais também não são compartilhadas: executors são processos distintos.
