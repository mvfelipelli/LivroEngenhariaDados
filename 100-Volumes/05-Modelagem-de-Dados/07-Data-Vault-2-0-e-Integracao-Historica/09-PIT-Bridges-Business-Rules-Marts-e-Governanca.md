---
title: PIT, Bridges, Business Rules, Marts e Governança
description: "Estruturas de acesso e entrega a consumidores."
tags: [data-vault, pit, bridge, business-vault]
aliases: [Consumo do Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# PIT, Bridges, Business Rules, Marts e Governança

Point-in-Time table pré-resolve versões de Satellites para datas de corte. Bridge pré-calcula caminhos e associações. Ambas são estruturas derivadas, reconstruíveis e pertencem ao Business Vault.

Regras de negócio incluem cálculo, matching, survivorship, classificação e métricas. Devem ser versionadas e manter lineage até o Raw Vault.

Marts dimensionais convertem Hubs, Links e Satellites em fatos e dimensões amigáveis. Consumidores raramente devem juntar Raw Vault diretamente.

## Controles

- business key e record source documentados;
- canonicalização comum e testada;
- lineage de cada Satellite;
- lag e completude por fonte;
- PIT/Bridge reconstruíveis;
- regra e versão de cada mart.

> [!important]
> Flexibilidade estrutural não reduz a necessidade de produtos semânticos estáveis.
