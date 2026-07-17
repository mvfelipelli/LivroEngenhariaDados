---
title: Schema-on-Write, Schema-on-Read e Evolução
description: "Validação, flexibilidade e compatibilidade de contratos."
tags: [schema-on-write, schema-on-read, schema-evolution]
aliases: [Evolução de Schema Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Schema-on-Write, Schema-on-Read e Evolução

Schema-on-write valida antes de publicar; schema-on-read interpreta no consumo. Plataformas maduras combinam ambos: Bronze flexível e rastreável, Silver/Gold com contratos fortes.

Mudanças comuns:

- adicionar campo opcional com default semântico;
- tornar obrigatório depois de backfill;
- ampliar tipo sem perda;
- renomear preservando identidade de campo quando suportado;
- dividir campo com período de compatibilidade;
- remover somente após análise de consumidores.

Compatibilidade backward permite novo leitor ler dado antigo; forward permite leitor antigo lidar com dado novo. Registro de schema e testes de contrato bloqueiam mudanças incompatíveis.

> [!important]
> Compatibilidade sintática não garante compatibilidade semântica: mudar unidade de reais para centavos exige versão explícita.
