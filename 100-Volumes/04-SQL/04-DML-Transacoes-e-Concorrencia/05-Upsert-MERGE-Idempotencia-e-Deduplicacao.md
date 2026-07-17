---
title: Upsert, MERGE, Idempotência e Deduplicação
description: "Convergência segura diante de repetição e reprocessamento."
tags: [sql, upsert, merge, idempotencia]
aliases: [Upsert e MERGE]
created: 2026-07-17
updated: 2026-07-17
---

# Upsert, MERGE, Idempotência e Deduplicação

Upsert insere uma chave ausente ou atualiza a existente. A garantia depende de constraint única; “consultar e depois inserir” separadamente sofre corrida.

```sql
INSERT INTO saldos (cliente_id, valor, versao)
VALUES (101, 500, 3)
ON CONFLICT (cliente_id) DO UPDATE
SET valor = EXCLUDED.valor,
    versao = EXCLUDED.versao
WHERE saldos.versao < EXCLUDED.versao;
```

`MERGE` expressa ações condicionais entre fonte e alvo, mas semântica, concorrência e suporte variam. Deduplicate a fonte antes quando várias linhas puderem corresponder ao mesmo alvo.

```mermaid
flowchart LR
    E["Evento com chave idempotente"] --> U["Constraint UNIQUE"]
    U --> N["Novo: INSERT"]
    U --> R["Repetido: ignora ou atualiza"]
```

Idempotência significa que repetir a intenção produz o mesmo estado observável. Chave de evento, versão monotônica e hash de conteúdo são estratégias possíveis.

> [!note]
> Upsert não resolve ordenação de eventos atrasados. Uma versão ou timestamp de origem precisa impedir regressão do estado.
