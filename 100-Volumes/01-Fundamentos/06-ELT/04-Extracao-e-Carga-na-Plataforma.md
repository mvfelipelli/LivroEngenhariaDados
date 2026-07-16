---
title: Extração e Carga na Plataforma
aliases: [ELT Extraction and Loading]
tags: [engenharia-de-dados, fundamentos, elt, raw, landing]
type: chapter
order: 04
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Landing, raw, metadados, evolução de schema e segurança na carga ELT."
---

# 04 — Extração e Carga na Plataforma

## Landing e raw

Landing recebe entregas; raw preserva registros carregados com metadados e política de retenção. A fronteira evita que arquivos parciais sejam tratados como dados disponíveis.

Metadados essenciais: origem, instante de ingestão, lote, arquivo, checksum, posição CDC e versão do schema.

## Append e imutabilidade

Raw é preferencialmente append-only. Correções entram como novas versões ou novos lotes, preservando evidência para auditoria e reprocessamento.

## Schema

Schema-on-write continua existindo: tipos podem ser flexíveis no raw, mas estrutura, versão e compatibilidade precisam ser registradas. Campos inesperados devem alertar; campos críticos ausentes podem bloquear o lote.

## Segurança antes da carga

Dados proibidos ou excessivos não devem ser carregados “para usar depois”. Minimize, tokenize ou masque antes da plataforma quando necessário. Raw exige acesso restrito, criptografia e retenção.

## Publicação do lote

Carregue em caminho ou tabela temporária, valide checksum e contagem e só então marque o lote como disponível.

## Próximo Capítulo

➡️ [[05-Transformacoes-no-Destino|05 — Transformações no Destino]]
