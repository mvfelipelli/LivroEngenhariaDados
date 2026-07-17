---
title: Migrações Versionadas, Testes, Observabilidade e Governança
description: "Processo repetível e auditável para evolução estrutural."
tags: [sql, migrations, testing, governance]
aliases: [Governança de Migrações]
created: 2026-07-17
updated: 2026-07-17
---

# Migrações Versionadas, Testes, Observabilidade e Governança

Cada migração precisa de identificador único, ordem, descrição, checksum e estado aplicado. Arquivos já executados não devem ser editados; correções entram como nova migração.

```text
V001__cria_pedidos.sql
V002__adiciona_canal.sql
V003__valida_canal.sql
```

Teste em banco vazio, upgrade a partir da versão anterior e cópia com volume representativo. Valide schema, dados, constraints, dependências e compatibilidade da aplicação.

```mermaid
flowchart LR
    G["Migração no Git"] --> T["Testes"]
    T --> H["Homologação"]
    H --> P["Produção"]
    P --> O["Observabilidade"]
```

Durante execução, monitore lock wait, duração, throughput, erros, lag de réplica e espaço. Defina critérios objetivos de pausa.

Revisão deve incluir proprietário, impacto, janela, plano de backfill, rollback/roll-forward e evidências. Migração destrutiva requer confirmação de que nenhum consumidor usa o objeto.

> [!tip]
> O melhor rollback para muitas mudanças de schema é parar, manter a expansão compatível e corrigir por roll-forward.
