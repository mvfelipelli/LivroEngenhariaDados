---
title: Produtos de Dados, Contratos, SLOs e Ownership
description: "Dados tratados como interface mantida para consumidores."
tags: [data-products, data-contracts, slo, ownership]
aliases: [Produtos e Contratos de Dados]
created: 2026-07-17
updated: 2026-07-17
---

# Produtos de Dados, Contratos, SLOs e Ownership

Produto de dados atende consumidores definidos e possui interface, documentação, qualidade, suporte e ciclo de vida. Dataset sem owner e compromisso é apenas ativo técnico.

## Contrato mínimo

- nome, finalidade e domínio;
- grão, chaves, schema e semântica;
- classificação e política de acesso;
- freshness, completude e disponibilidade;
- owner de negócio e técnico;
- interface e exemplos;
- versionamento, depreciação e suporte;
- lineage e dependências.

SLO deve refletir valor: “95% dos lotes disponíveis até 06:00” é mensurável; “dados rápidos” não é. Consumidores precisam ser comunicados antes de quebra.

> [!tip]
> Inclua consultas de exemplo e contraexemplos que esclareçam o grão e a aditividade.
