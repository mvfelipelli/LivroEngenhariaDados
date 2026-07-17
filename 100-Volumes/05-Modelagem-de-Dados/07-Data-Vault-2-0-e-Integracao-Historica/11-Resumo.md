---
title: Resumo
description: "Síntese de Data Vault 2.0."
tags: [modelagem-de-dados, resumo, data-vault]
aliases: [Resumo Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Raw Vault preserva dados orientados à fonte e auditáveis.
- Business Vault aplica regras derivadas e estruturas de acesso.
- Hub registra business key; Link registra associação.
- Satellite historiza contexto por fonte e ritmo.
- Hash keys permitem identidade determinística e carga paralela.
- Hashdiff detecta mudança sob canonicalização estável.
- Multi-active representa valores simultâneos no grão correto.
- Deletes são historizados, não propagados fisicamente ao Raw Vault.
- PIT e Bridges aceleram consultas e são reconstruíveis.
- Marts publicam semântica adequada ao consumidor.

O [[14-Laboratorio|laboratório]] carrega um mini-Vault e comprova idempotência.
