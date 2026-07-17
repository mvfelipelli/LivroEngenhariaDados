---
title: Satellites, Contexto, Histórico e Rate of Change
description: "Atributos descritivos historizados por fonte e ritmo."
tags: [data-vault, satellites, historico]
aliases: [Satellites Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Satellites, Contexto, Histórico e Rate of Change

Satellite contém contexto de Hub ou Link e cria linha quando atributos rastreados mudam.

```text
SAT_CLIENTE_CRM(cliente_hk, load_ts, hashdiff,
                nome, segmento, record_source)
```

Chave típica combina parent hash key e load timestamp. Satellites são separados por fonte, classificação de segurança, frequência de mudança e grupo semântico coerente.

Separar atributos rápidos de lentos reduz linhas e I/O. Não fragmente cada atributo isoladamente; o grupo deve ter significado operacional.

End dating pode ser calculado com `LEAD(load_ts)` ou materializado em Business Vault. O Raw Vault preserva inserções, evitando updates quando possível.

> [!note]
> O timestamp de carga não é necessariamente o tempo de validade do negócio; preserve ambos quando disponíveis.
