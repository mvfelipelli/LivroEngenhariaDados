---
title: Resumo
description: "Síntese de histórico dimensional."
tags: [modelagem-de-dados, resumo, scd]
aliases: [Resumo Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Mudança real, correção e reclassificação exigem políticas diferentes.
- SCD0 preserva; SCD1 sobrescreve; SCD2 cria versões.
- SCD2 usa chave substituta e intervalo de validade.
- Fato histórico referencia a versão válida no evento.
- Snapshot periódico registra estado por intervalo.
- Snapshot acumulativo acompanha marcos de processo.
- Bridges representam relações multivaloradas.
- Pesos evitam duplicação quando medidas são alocadas.
- Hierarquias variáveis podem usar closure bridge.
- Dados tardios e correções exigem lookup temporal, lineage e testes.

O [[14-Laboratorio|laboratório]] implementa SCD2 e comprova resolução temporal dos fatos.
