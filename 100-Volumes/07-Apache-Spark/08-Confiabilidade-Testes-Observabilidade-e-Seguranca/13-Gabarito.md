---
title: Gabarito — Confiabilidade Spark
description: "Respostas dos exercícios do módulo."
tags: [apache-spark, confiabilidade, gabarito]
aliases: [Gabarito Confiabilidade Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Função DataFrame→DataFrame; adapters de leitura/escrita; entrypoint de coordenação.
2. Válido, ID nulo, valor negativo, duplicata, limite numérico e vazio.
3. `entrada = válidos + inválidos`; soma válida mais quarentena reconciliada conforme regra.
4. Aplicação, ambiente, status e etapa; não pedido, arquivo ou mensagem individual.
5. Uma unidade por data, staging versionado, validação e troca/publicação controlada.
6. Leitura das fontes necessárias, escrita em staging/destino/checkpoint e acesso a segredos específicos.
7. Shuffle, spill, cache, checkpoint, event log, staging, logs e dumps.
8. Injetar falha antes da troca de referência; confirmar destino anterior intacto e retry determinístico.
