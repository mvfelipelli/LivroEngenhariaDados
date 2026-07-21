---
title: Estudo de Caso — Primeiro Marco da DataRetail
description: "Definição do produto Pedidos Canônicos."
tags: [projeto-integrador, estudo-de-caso, dataretail]
aliases: [Caso Primeiro Marco DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Estudo de Caso — Primeiro Marco da DataRetail

O primeiro marco não constrói toda a plataforma. Ele gera pedidos sintéticos em CSV, valida contrato, separa quarentena e publica um resumo diário reproduzível.

```mermaid
flowchart LR
    G["Gerador com seed"] --> C["CSV bruto"]
    C --> V["Validação"]
    V --> Q["Quarentena"]
    V --> P["Pedidos válidos"]
    P --> R["Receita diária"]
    V --> M["Métricas"]
    R --> M
```

Critérios: mesma semente produz mesma entrada; válidos mais quarentena igualam entrada; soma de receita usa somente pagos válidos; repetir não duplica; nenhuma informação real é utilizada.

Esse marco será reimplementado com tecnologias diferentes sem mudar a semântica.
