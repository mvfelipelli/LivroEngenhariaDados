---
title: Introdução
description: "Modelagem como investigação e contrato do domínio."
tags: [modelagem-de-dados, introducao]
aliases: [Introdução à Modelagem de Dados]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Modelagem não começa pela criação de tabelas. Começa por perguntas: o que existe no domínio, como é identificado, quais fatos podem ocorrer, que regras nunca podem ser violadas e que histórico precisa ser preservado.

```mermaid
flowchart TD
    D["Descobrir domínio"] --> C["Conceituar"]
    C --> L["Estruturar logicamente"]
    L --> F["Implementar fisicamente"]
    F --> V["Validar com exemplos"]
    V --> E["Evoluir"]
    E --> D
```

O modelo reduz ambiguidades entre negócio, software, dados e operação. Ele não é fotografia permanente: muda com o domínio, mas deve evoluir de forma explícita e compatível.
