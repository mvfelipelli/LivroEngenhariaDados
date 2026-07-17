---
title: Modelos Conceitual, Lógico e Físico
description: "Níveis de abstração e suas decisões."
tags: [modelo-conceitual, modelo-logico, modelo-fisico]
aliases: [Níveis de Modelagem]
created: 2026-07-17
updated: 2026-07-17
---

# Modelos Conceitual, Lógico e Físico

Os níveis respondem perguntas diferentes e evitam que limitações de tecnologia definam prematuramente o domínio.

| Nível | Foco | Exemplos de decisão |
|---|---|---|
| conceitual | significado do negócio | Pedido contém Item |
| lógico | estrutura independente de produto | relações, atributos, chaves |
| físico | implementação concreta | tipos, índices, partições |

```mermaid
flowchart LR
    C["Conceitual: o quê e por quê"] --> L["Lógico: como estruturar"]
    L --> F["Físico: como implementar"]
```

Uma decisão física pode retroalimentar o desenho, mas não deve alterar silenciosamente a semântica. Desnormalizar para leitura exige preservar a fonte de verdade e a regra de sincronização.

> [!note]
> “Modelo de dados” pode referir-se ao conjunto de conceitos de um paradigma ou ao modelo específico de uma organização; explicite o sentido.
