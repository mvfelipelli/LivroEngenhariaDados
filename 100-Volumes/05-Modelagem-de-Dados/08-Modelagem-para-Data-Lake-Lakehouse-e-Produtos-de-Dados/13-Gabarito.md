---
title: Gabarito
description: "Respostas dos exercícios de lakehouse e produtos."
tags: [modelagem-de-dados, gabarito, lakehouse]
aliases: [Gabarito Modelagem Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Bronze preserva payload/fonte; Silver valida identidade, tipos e deduplica; Gold publica fatos financeiros reconciliados.

## 2

Avro para arquivo orientado a eventos e evolução; Parquet/ORC para mart com projeções e agregações.

## 3

Commit publica novos metadados apontando ao conjunto consistente de arquivos; leitores fixam um snapshot.

## 4

Particione por data em granularidade de volume adequada e faça clustering por cliente; evite partição por cliente.

## 5

Monitore quantidade/tamanho, compacte partições recentes em arquivos-alvo e coordene com writers e snapshots.

## 6

Adicionar campo novo, preencher ambos, adaptar leitores, backfill, medir uso e remover legado em versão major.

## 7

Finalidade, grão produto-loja-instante, chaves, medidas, tempo, SLO, owner, acesso, qualidade e evolução.

## 8

Defina `pedido_id` corporativo, eventos/tempos comuns, contratos versionados e produtos separados que compartilham chaves e lineage.
