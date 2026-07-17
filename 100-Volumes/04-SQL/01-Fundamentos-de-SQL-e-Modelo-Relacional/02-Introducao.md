---
title: Introdução aos Fundamentos de SQL
description: "Por que uma linguagem declarativa para dados relacionais."
tags: [sql, introducao, relacional]
aliases: [Introdução aos Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Sistemas de dados precisam responder perguntas sem obrigar o usuário a programar como percorrer páginas, índices ou arquivos. SQL resolve esse problema ao permitir declarar **qual relação resultante** se deseja.

```mermaid
flowchart TD
    S["Sentença SQL"] --> A["Análise sintática e semântica"]
    A --> O["Otimização"]
    O --> E["Execução"]
    E --> R["Relação resultante"]
```

O otimizador pode trocar a ordem de joins, selecionar índices e escolher algoritmos sem alterar a semântica. Essa separação entre intenção e mecanismo oferece produtividade, mas exige formular corretamente conjuntos, predicados e contratos.

SQL inclui sublinguagens para definição, consulta, manipulação, controle e transações. Este primeiro módulo concentra os fundamentos de definição e consulta.

> [!note]
> Produtos implementam dialetos. O padrão oferece uma base comum, enquanto tipos, funções e detalhes sintáticos podem variar.
