---
title: Chaves, Identidade, Referências e Localidade
description: "Impacto físico da estratégia de identidade."
tags: [chaves, identidade, localidade]
aliases: [Chaves na Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Chaves, Identidade, Referências e Localidade

Chaves largas aumentam índices e referências. Chaves sequenciais favorecem localidade, mas podem concentrar escrita; UUIDs distribuem identidade, porém versões aleatórias fragmentam B-trees em alguns mecanismos.

| Estratégia | Benefício | Risco |
|---|---|---|
| natural | significado e deduplicação | mutabilidade ou largura |
| sequência | compacta e local | coordenação e hot spot |
| UUID aleatório | geração distribuída | tamanho e dispersão |
| UUID ordenável | distribuição com localidade temporal | suporte e exposição de tempo |

A chave física deve coexistir com `UNIQUE` sobre identificadores de negócio. Em sistemas distribuídos, a chave de distribuição influencia colocalização de joins e balanceamento.

> [!tip]
> Escolha identidade por requisitos de geração, merge, privacidade, localidade e ciclo de vida, não por moda.
