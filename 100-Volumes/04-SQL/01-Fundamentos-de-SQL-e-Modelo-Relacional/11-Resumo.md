---
title: Resumo — Fundamentos de SQL
description: "Síntese do módulo introdutório de SQL."
tags: [sql, resumo, modelo-relacional]
aliases: [Resumo Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- SQL declara resultados e permite ao SGBD escolher mecanismos;
- o padrão fornece uma base, mas produtos possuem dialetos;
- relação, tupla, atributo e domínio sustentam o raciocínio;
- tabelas SQL podem conter duplicatas e não têm ordem implícita;
- tipos, chaves e constraints preservam invariantes;
- `FROM` e `WHERE` são logicamente avaliados antes de `SELECT`;
- `NULL` introduz o valor lógico desconhecido;
- `DISTINCT` remove duplicatas, enquanto `ORDER BY` define ordem;
- expressões derivam valores e conversões devem ser explícitas;
- joins combinam relações e agregações resumem grupos;
- portabilidade exige disciplina e testes.

```mermaid
mindmap
  root((SQL))
    Modelo relacional
      Relação
      Tupla
      Domínio
    Estrutura
      Tipos
      Chaves
      Constraints
    Consulta
      Projeção
      Filtro
      Composição
      Ordenação
```

O próximo passo é consolidar tudo no [[14-Laboratorio|laboratório reproduzível]].
