---
title: Resumo
description: "Síntese do módulo de planos, índices e otimização."
tags: [sql, resumo, performance]
aliases: [Resumo Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- SQL especifica o resultado; o plano físico especifica o caminho.
- Estatísticas alimentam estimativas de cardinalidade e custo.
- Erros de estimativa alteram ordem de joins e escolha de operadores.
- Sequential scan pode ser correto quando grande parte da tabela será lida.
- Índices compostos devem refletir igualdade, intervalo e ordenação reais.
- Cobertura reduz acessos; índices parciais reduzem a estrutura ao subconjunto útil.
- Nested loop, hash e merge join têm cenários e riscos diferentes.
- `EXPLAIN ANALYZE` compara estimativa com execução, mas executa a instrução.
- SARGabilidade permite transformar predicados em caminhos de busca.
- Otimização profissional exige baseline, hipótese, validação semântica e observação de regressões.

O próximo passo é aplicar essas ideias no [[14-Laboratorio|laboratório]], comparando planos antes e depois de um índice alinhado à consulta.
