---
title: Tempo de Evento, Sistema e Modelagem Bitemporal
description: "Histórico do negócio e histórico do conhecimento do sistema."
tags: [sql, bitemporal, event-time, system-time]
aliases: [Modelagem Bitemporal]
created: 2026-07-17
updated: 2026-07-17
---

# Tempo de Evento, Sistema e Modelagem Bitemporal

O tempo de validade responde “quando isso era verdadeiro no negócio?”. O tempo do sistema responde “quando o banco registrava essa versão como conhecida?”. Modelagem bitemporal preserva ambos.

| Eixo | Pergunta |
|---|---|
| validade | quando a condição vale no domínio? |
| sistema | quando essa versão esteve registrada? |

```sql
CREATE TABLE contrato_bitemporal (
    contrato_id BIGINT NOT NULL,
    valor NUMERIC NOT NULL,
    valido_desde TIMESTAMP NOT NULL,
    valido_ate TIMESTAMP,
    registrado_desde TIMESTAMP NOT NULL,
    registrado_ate TIMESTAMP,
    PRIMARY KEY (contrato_id, valido_desde, registrado_desde)
);
```

Uma correção retroativa encerra a versão no eixo do sistema e insere outra com validade no passado. Assim é possível responder tanto o estado corrigido quanto aquilo que era conhecido em uma data de auditoria.

```mermaid
flowchart LR
    R1["Registro original"] --> C["Correção recebida"]
    C --> F["Fechar tempo do sistema"]
    F --> R2["Nova versão com validade retroativa"]
```

> [!note]
> Bitemporalidade aumenta volume e complexidade. Use-a quando auditoria e correções históricas justificarem o custo.
