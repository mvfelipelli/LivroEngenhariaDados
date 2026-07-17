---
title: Hubs, Business Keys, Identidade e Record Source
description: "Núcleo estável das entidades de negócio."
tags: [data-vault, hubs, business-key]
aliases: [Hubs Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Hubs, Business Keys, Identidade e Record Source

Hub registra uma business key estável e seu primeiro encontro. Não contém atributos descritivos.

```text
HUB_CLIENTE(cliente_hk, cliente_bk, load_ts, record_source)
```

Business key é identificador reconhecido pelo negócio dentro de um domínio. Quando fontes usam chaves distintas para a mesma pessoa, uma regra de matching ou hub de identidade corporativa precisa ser explícita.

`record_source` identifica proveniência; `load_ts` registra entrada no Vault. Hash key permite geração paralela determinística, desde que a canonicalização seja comum.

Hubs não devem ser criados para classificações sem identidade própria nem para toda tabela de origem.

> [!tip]
> Escreva a regra de unicidade e escopo da business key antes de escolher a expressão de hash.
