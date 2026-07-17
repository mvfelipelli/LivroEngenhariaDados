---
title: Testes, Performance, Semântica e Governança Dimensional
description: "Controles para métricas e dimensões confiáveis."
tags: [testes, performance, governanca-dimensional]
aliases: [Qualidade Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Testes, Performance, Semântica e Governança Dimensional

Testes dimensionais protegem grão, referências, aditividade e conformidade.

- chave composta do grão é única;
- todas as chaves dimensionais resolvem;
- medidas respeitam domínio e sinal;
- fatos reconciliam com a origem;
- membros conformados têm mesmos códigos e definições;
- datas e moedas usam regras explícitas;
- métricas derivadas preservam numerador e denominador.

Performance depende de particionamento da fato, distribuição, ordenação, estatísticas e formatos colunares. Agregados devem ser derivados e reconciliados.

Camada semântica publica nomes, fórmulas, dimensões permitidas e filtros. Owner de negócio aprova significado; owner técnico responde por implementação e SLO.

> [!warning]
> Duas métricas chamadas “receita” com regras diferentes não são conformadas, mesmo no mesmo dashboard.
