---
title: Estratégias de Release, Promoção e Rollback
description: "Separação entre publicar, promover, implantar e recuperar."
tags: [release, deploy, promocao, rollback]
aliases: [Promoção e Rollback]
created: 2026-07-17
updated: 2026-07-17
---

# Estratégias de Release, Promoção e Rollback

Release é disponibilidade de uma versão; deploy altera um ambiente; ativação expõe comportamento. Separar esses eventos reduz o raio de impacto.

| Estratégia | Mecanismo | Principal trade-off |
| --- | --- | --- |
| rolling | substituição gradual | versões coexistem |
| blue-green | troca de ambiente | custo duplicado |
| canary | tráfego progressivo | exige métricas confiáveis |
| feature flag | ativação lógica | dívida de flags |

```mermaid
sequenceDiagram
    participant C as CI
    participant R as Registry
    participant G as Repositório de ambiente
    participant A as Agente
    C->>R: publica digest D
    C->>G: propõe D para homologação
    G->>A: mudança aprovada
    A->>A: reconcilia e valida
```

Rollback restaura uma declaração anterior; roll-forward publica uma correção. Bancos e dados tornam reversão difícil: prefira mudanças expand-contract, backups testados e compatibilidade entre versões adjacentes.

Promoção deve mover referência ao mesmo digest, com gates específicos por ambiente. Copiar ou recompilar artefatos quebra a cadeia de custódia.
