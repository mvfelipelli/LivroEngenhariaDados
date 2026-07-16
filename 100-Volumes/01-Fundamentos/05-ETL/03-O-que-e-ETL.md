---
title: O que é ETL
aliases: [Extract Transform Load]
tags: [engenharia-de-dados, fundamentos, etl]
type: chapter
order: 03
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Definição, arquitetura, responsabilidades e trade-offs de ETL."
---

# 03 — O que é ETL

## Definição

**ETL** é um padrão em que dados são extraídos de fontes, transformados em uma área de processamento e carregados em um destino segundo um contrato.

| Etapa | Responsabilidade |
| --- | --- |
| Extract | obter dados e metadados com consistência e impacto controlado |
| Transform | validar, padronizar, integrar e derivar significado |
| Load | publicar no destino com atomicidade e semântica de escrita |

## Fronteiras

As etapas são fronteiras lógicas, não precisam ser programas separados. Transformações podem ocorrer em memória, em um engine distribuído ou em staging. O que define ETL é a transformação relevante antes da publicação no destino final.

## ETL, cópia e integração

Cópia replica representação. ETL altera contexto: mapeia chaves, tipos, unidades, regras e grãos. Por isso requer contratos de origem e destino, além de reconciliação.

## Batch e microbatch

ETL clássico processa lotes delimitados por arquivo, partição ou janela. Microbatches reduzem latência usando lotes menores. Streaming contínuo compartilha princípios de identidade, ordenação e idempotência, mas possui mecanismos próprios.

## Estado

Pipelines podem ser:

- **stateless**, quando cada registro é transformado isoladamente;
- **stateful**, quando dependem de watermark, histórico, deduplicação ou dimensões.

Estado precisa ser persistido e recuperável; mantê-lo apenas na memória torna retries inconsistentes.

## Critérios de sucesso

- completude e atualidade;
- unicidade no grão;
- integridade e qualidade;
- idempotência;
- rastreabilidade;
- capacidade de reprocessar;
- custo e duração previsíveis.

## Erros comuns

- misturar extração e exclusão da origem;
- transformar sem preservar entrada bruta;
- depender da ordem acidental dos registros;
- considerar “job verde” prova de dados corretos;
- carregar sem chave de negócio ou reconciliação.

## Próximo Capítulo

➡️ [[04-Extracao-de-Dados|04 — Extração de Dados]]
