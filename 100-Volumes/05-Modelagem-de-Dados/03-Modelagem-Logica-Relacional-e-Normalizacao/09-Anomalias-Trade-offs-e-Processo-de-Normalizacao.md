---
title: Anomalias, Trade-offs e Processo de Normalização
description: "Método prático para analisar e refinar relações."
tags: [anomalias, trade-offs, normalizacao]
aliases: [Processo de Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Anomalias, Trade-offs e Processo de Normalização

Anomalia de atualização permite versões conflitantes do mesmo fato; de inserção exige fato não relacionado; de exclusão remove informação adicional. Elas sinalizam dependências mal posicionadas.

## Processo

1. declare o grão da relação;
2. liste chaves candidatas;
3. registre dependências e sua origem semântica;
4. encontre dependências parciais, transitivas e determinantes não chave;
5. decomponha e prove junção sem perda;
6. verifique preservação das dependências;
7. implemente chaves e constraints;
8. teste inserção, atualização, exclusão e reconstrução.

Desnormalização pode reduzir custo de leitura, mas é decisão física posterior. Ela exige fonte canônica, sincronização, reconciliação e medição.

> [!tip]
> Comece pelas dependências, não pelo número da forma normal. O número resume uma propriedade; não substitui o raciocínio.
