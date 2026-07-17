---
title: Resumo
description: "Síntese de SQL temporal e semiestruturado."
tags: [sql, resumo, temporal, json]
aliases: [Resumo SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Data civil, instante e duração possuem semânticas diferentes.
- UTC facilita comparação; timezone de negócio preserva regras civis.
- Intervalos semiabertos evitam ambiguidade em fronteiras.
- Consultas `as of` selecionam a versão válida em um instante.
- Bitemporalidade separa validade do domínio e conhecimento do sistema.
- Ausência, JSON `null`, texto e número não são equivalentes.
- JSON é adequado a flexibilidade controlada, não à fuga de modelagem.
- Expandir arrays altera o grão e pode provocar fanout.
- Índices de expressão, colunas geradas e índices invertidos atendem padrões distintos.
- Payloads precisam de versão, validação, evolução e quarentena.

O [[14-Laboratorio|laboratório]] combina consulta temporal e expansão tipada de itens JSON.
