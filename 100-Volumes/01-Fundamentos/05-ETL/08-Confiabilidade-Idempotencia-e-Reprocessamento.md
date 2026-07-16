---
title: Confiabilidade, Idempotência e Reprocessamento
aliases: [Reliable ETL, Idempotent ETL]
tags: [engenharia-de-dados, fundamentos, etl, idempotencia, reprocessamento]
type: chapter
order: 08
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Garantias de execução, retries, checkpoints e recuperação de ETL."
---

# 08 — Confiabilidade, Idempotência e Reprocessamento

## Falhas são parte do sistema

Rede, fonte, código e destino podem falhar depois de efeitos parciais. O design deve permitir retry sem duplicar e distinguir execução de publicação.

## Idempotência

Aplicar a mesma entrada novamente produz o mesmo estado observável. Mecanismos:

- chaves determinísticas e `UNIQUE`;
- upsert com precedência;
- partições substituíveis;
- tabela de lotes processados;
- escrita temporária e commit atômico.

## Exactly-once

“Exatamente uma vez” é uma propriedade fim a fim difícil. Na prática, combine entrega ao menos uma vez com efeitos idempotentes e reconciliação.

## Checkpoints

Persistem cursor, lote, versão de regra e status. Só avance checkpoint após o destino confirmar. Checkpoint antecipado perde dados; tardio exige idempotência.

## Reprocessamento

Preserve raw imutável, versões de código e contratos. Defina intervalo, partições afetadas, isolamento do resultado, validação e troca controlada.

## Poison records

Registros que sempre falham não devem bloquear indefinidamente. Quarentena, limite de tentativas e alerta preservam progresso sem ocultar perda.

## Próximo Capítulo

➡️ [[09-Testes-Desempenho-e-Operacao|09 — Testes, Desempenho e Operação]]
