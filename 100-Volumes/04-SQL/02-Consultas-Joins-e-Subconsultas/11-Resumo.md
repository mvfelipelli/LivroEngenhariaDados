---
title: Resumo — Consultas, Joins e Subconsultas
description: "Síntese das técnicas de composição relacional."
tags: [sql, joins, subconsultas, resumo]
aliases: [Resumo Consultas e Joins]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- toda consulta deve declarar seu grão esperado;
- chaves e multiplicidades permitem prever cardinalidade;
- `INNER JOIN` mantém correspondências e `CROSS JOIN` combina tudo;
- outer joins preservam ausência, desde que filtros não a eliminem;
- `EXISTS` e `NOT EXISTS` expressam semi-join e anti-join;
- múltiplas relações 1:N podem causar fanout;
- subconsultas podem ser escalares, derivadas ou correlacionadas;
- operações de conjunto compõem resultados verticalmente;
- CTEs nomeiam etapas e CTEs recursivas percorrem hierarquias;
- materialização é decisão dependente do mecanismo;
- contagem, unicidade e totais de controle testam a semântica.

```mermaid
mindmap
  root((Composição SQL))
    Cardinalidade
      Grão
      Chaves
      Fanout
    Joins
      Interno
      Externo
      Existência
    Subconsultas
      Escalar
      Derivada
      Correlacionada
    CTE
      Comum
      Recursiva
```
