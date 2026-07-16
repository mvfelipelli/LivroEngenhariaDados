---
title: Extração de Dados
aliases: [Data Extraction]
tags: [engenharia-de-dados, fundamentos, etl, extracao]
type: chapter
order: 04
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Métodos, consistência, impacto e contratos de extração."
---

# 04 — Extração de Dados

## Objetivo

Extração captura um conjunto delimitado e reproduzível da fonte, com metadados suficientes para provar origem e completude.

## Métodos

| Método | Vantagem | Risco |
| --- | --- | --- |
| Snapshot completo | simples e reconstruível | volume e impacto |
| Watermark | eficiente | empates, atrasos e relógios |
| CDC por log | baixa latência e exclusões | ordenação e operação |
| Arquivos | desacoplamento | duplicação e chegada parcial |
| API | contrato explícito | paginação, limites e mutação |

## Consistência

Consultas longas podem observar estados de instantes diferentes. Snapshot transacional, réplica, exportação nativa ou partições imutáveis ajudam a definir o ponto de leitura.

## Paginação

Paginação por offset pode perder ou repetir registros quando a fonte muda. Cursor estável por `(updated_at, id)` é preferível. O watermark deve ser composto para desempatar timestamps iguais.

```sql
SELECT * FROM orders
WHERE (updated_at, order_id) > (:last_time, :last_id)
ORDER BY updated_at, order_id
LIMIT 1000;
```

## Metadados mínimos

- fonte e versão do schema;
- instante e intervalo extraídos;
- cursor inicial e final;
- contagem e checksum;
- identificador da execução;
- arquivo, partição ou query de origem.

## Proteção da fonte

Use índices compatíveis, limites, réplicas quando apropriado, janelas acordadas e monitoramento de CPU, I/O e locks. Extração não deve degradar o sistema operacional.

## Próximo Capítulo

➡️ [[05-Transformacao-de-Dados|05 — Transformação de Dados]]
