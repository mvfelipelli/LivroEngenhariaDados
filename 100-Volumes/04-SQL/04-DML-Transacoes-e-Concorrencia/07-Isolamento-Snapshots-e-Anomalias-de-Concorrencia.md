---
title: Isolamento, Snapshots e Anomalias de Concorrência
description: "Visibilidade de mudanças entre transações simultâneas."
tags: [sql, isolation, snapshots, anomalies]
aliases: [Níveis de Isolamento SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Isolamento, Snapshots e Anomalias de Concorrência

O padrão define níveis em termos de fenômenos permitidos. Implementações podem oferecer garantias mais fortes e nomes iguais com comportamentos diferentes.

| Fenômeno | Descrição |
| --- | --- |
| dirty read | lê mudança não confirmada |
| nonrepeatable read | mesma linha muda entre leituras |
| phantom | predicado encontra conjunto diferente |
| serialization anomaly | resultado impossível em ordem serial |

`READ COMMITTED` frequentemente cria snapshot por sentença. `REPEATABLE READ` tende a manter snapshot transacional. `SERIALIZABLE` exige efeito equivalente a alguma ordem serial e pode abortar uma transação.

```mermaid
sequenceDiagram
    participant T1
    participant T2
    T1->>T1: lê total
    T2->>T2: altera e COMMIT
    T1->>T1: relê conforme isolamento
```

Write skew ocorre quando transações leem o mesmo conjunto e atualizam linhas diferentes, violando um invariante conjunto. Locks adequados, constraint materializada ou serializable podem ser necessários.

> [!warning]
> A aplicação deve estar preparada para retry em níveis que detectam conflitos de serialização.
