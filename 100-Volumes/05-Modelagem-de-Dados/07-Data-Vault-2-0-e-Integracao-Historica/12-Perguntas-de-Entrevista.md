---
title: Perguntas de Entrevista
description: "Perguntas sobre Data Vault 2.0."
tags: [modelagem-de-dados, entrevista, data-vault]
aliases: [Entrevista Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. O que Hub armazena?

Business key, hash key, primeiro load timestamp e record source; não atributos descritivos.

## 2. O que Link representa?

Associação no grão do conjunto de Hubs participantes.

## 3. O que Satellite contém?

Contexto descritivo historizado de Hub ou Link, com fonte e tempo de carga.

## 4. Raw e Business Vault diferem como?

Raw preserva conteúdo orientado à fonte; Business aplica regras derivadas.

## 5. Para que serve hashdiff?

Detectar mudança no conjunto canônico de atributos do Satellite.

## 6. Por que canonicalização importa?

Representações diferentes do mesmo valor gerariam hashes distintos ou estados diferentes indistinguíveis.

## 7. O que é Multi-Active Satellite?

Satellite com várias ocorrências simultaneamente ativas, discriminadas no grão.

## 8. O que PIT resolve?

Pré-resolve as versões de Satellites válidas em pontos de corte.

## 9. Data Vault substitui star schema?

Não. Vault integra e historiza; star schema normalmente atende consumo analítico.

## 10. Como tratar delete?

Registrar status, effectivity ou presença por lote, preservando histórico no Raw Vault.
