---
title: Resumo — DDL e Evolução de Estruturas
description: "Síntese dos contratos e migrações do módulo."
tags: [sql, ddl, migrations, resumo]
aliases: [Resumo Evolução de Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- DDL gerencia objetos persistentes e seus contratos;
- schemas organizam namespaces e permissões;
- tipos, defaults e colunas geradas têm semânticas distintas;
- constraints protegem invariantes para qualquer escritor;
- dependências internas e externas precisam de inventário;
- `ALTER TABLE` pode exigir lock, scan ou reescrita;
- expand-contract preserva compatibilidade durante coexistência;
- backfills devem ser idempotentes, retomáveis e observáveis;
- rollback depende da compatibilidade dos dados novos;
- migrações aplicadas são imutáveis e recebem versão;
- testes devem cobrir instalação limpa, upgrade e volume realista;
- contração destrutiva ocorre somente após evidência de desuso.

```mermaid
mindmap
  root((Evolução de schema))
    Contrato
      Tipos
      Constraints
    Impacto
      Dependências
      Locks
    Processo
      Expand
      Backfill
      Contract
    Controle
      Versão
      Testes
      Métricas
```
