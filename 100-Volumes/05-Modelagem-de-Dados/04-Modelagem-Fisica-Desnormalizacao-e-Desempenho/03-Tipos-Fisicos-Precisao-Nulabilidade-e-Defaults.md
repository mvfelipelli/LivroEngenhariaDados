---
title: Tipos Físicos, Precisão, Nulabilidade e Defaults
description: "Representação concreta de domínios e limites."
tags: [tipos, precisao, null, defaults]
aliases: [Tipos na Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Tipos Físicos, Precisão, Nulabilidade e Defaults

Tipo físico define representação, operações, intervalo, armazenamento e compatibilidade. Escolha pela semântica: centavos inteiros ou decimal exato para dinheiro; instante com timezone para eventos globais; `DATE` para conceitos civis.

## Decisões

- menor intervalo seguro, sem otimização prematura;
- precisão e escala explícitas;
- encoding e collation coerentes;
- `NOT NULL` quando ausência é estado inválido;
- `CHECK` para limites e domínio;
- default apenas quando há valor legítimo no momento da escrita.

```sql
valor_centavos BIGINT NOT NULL CHECK (valor_centavos >= 0),
ocorrido_em TIMESTAMPTZ NOT NULL,
moeda CHAR(3) NOT NULL
```

Default silencioso de zero ou data atual pode converter desconhecido em informação falsa. Tipos muito genéricos como texto deslocam validação e prejudicam estatísticas.

> [!warning]
> Alterar tipo pode exigir reescrita, lock ou conversão com perda. Planeje a evolução desde o contrato.
