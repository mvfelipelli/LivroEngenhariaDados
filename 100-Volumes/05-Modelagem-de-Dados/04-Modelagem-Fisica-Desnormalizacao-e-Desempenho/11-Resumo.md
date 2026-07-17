---
title: Resumo
description: "Síntese de modelagem física e desnormalização."
tags: [modelagem-de-dados, resumo, modelagem-fisica]
aliases: [Resumo Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Tipos físicos implementam domínios, precisão e limites.
- Defaults não devem inventar informação ausente.
- Estratégias de chave afetam geração, largura e localidade.
- Índices aceleram acesso e ampliam custo de escrita.
- Particionamento serve a pruning, manutenção e retenção.
- Distribuição precisa equilibrar dados e reduzir shuffle.
- Layout em linhas e colunas atende workloads distintos.
- Compressão depende de ordenação, cardinalidade e formato.
- Desnormalização exige fonte, atualização, reconciliação e rebuild.
- Toda decisão física é validada por workload e medição.

O [[14-Laboratorio|laboratório]] demonstra caminho indexado e projeção agregada reconciliável.
