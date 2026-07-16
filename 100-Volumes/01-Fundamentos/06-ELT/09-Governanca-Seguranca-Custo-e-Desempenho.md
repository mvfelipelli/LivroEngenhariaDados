---
title: Governança, Segurança, Custo e Desempenho
aliases: [ELT Governance Security Cost]
tags: [engenharia-de-dados, fundamentos, elt, governanca, seguranca, custo]
type: chapter
order: 09
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Controles operacionais para plataformas ELT."
---

# 09 — Governança, Segurança, Custo e Desempenho

## Governança

Defina dono por fonte e produto, convenções, contratos, revisão e depreciação. Self-service significa autonomia dentro de guardrails.

## Segurança

Raw recebe o maior risco. Aplique menor privilégio, separação por camadas, mascaramento, políticas por linha/coluna, auditoria e retenção. Transformar depois não autoriza carregar dados sem finalidade.

## Custo

Meça bytes lidos, tempo, slots/CPU, armazenamento e frequência. Atribua custo por domínio ou produto e estabeleça orçamento e alertas.

## Desempenho

- evite `SELECT *`;
- filtre cedo;
- particione e organize por acesso;
- materialize resultados caros e reutilizados;
- reduza scans repetidos;
- inspecione planos e cardinalidades;
- escolha full refresh por evidência.

## Operação

Monitore freshness, falhas, duração, custo, testes e consumidores afetados. Runbooks devem cobrir rebuild, rollback, atraso de fonte e quebra de schema.

## Próximo Capítulo

➡️ [[10-Estudo-de-Caso-DataRetail|10 — Estudo de Caso DataRetail]]
