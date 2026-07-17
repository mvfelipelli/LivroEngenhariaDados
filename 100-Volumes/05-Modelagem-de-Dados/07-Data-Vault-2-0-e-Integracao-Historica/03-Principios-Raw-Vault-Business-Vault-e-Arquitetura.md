---
title: Princípios, Raw Vault, Business Vault e Arquitetura
description: "Camadas e responsabilidades do Data Vault."
tags: [raw-vault, business-vault, arquitetura]
aliases: [Arquitetura Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Princípios, Raw Vault, Business Vault e Arquitetura

Princípios centrais incluem integração por business key, historização, rastreabilidade até a fonte, carga incremental e separação de regras.

| Camada | Responsabilidade |
|---|---|
| staging | padronização técnica e metadados de lote |
| Raw Vault | identidades, relações e contexto historizado da fonte |
| Business Vault | regras, cálculos, survivorship e estruturas auxiliares |
| mart | apresentação por processo e consumidor |

Raw não significa bytes intocados: tipos, encoding, trimming e canonicalização necessários à carga são transformações técnicas documentadas. Regras de negócio que reinterpretam conteúdo ficam fora dele.

> [!warning]
> Misturar regras voláteis no Raw Vault reduz auditabilidade e exige reconstrução quando a regra muda.
