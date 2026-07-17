---
title: BCNF, Quarta e Quinta Formas Normais
description: "Dependências determinantes, multivaloradas e de junção."
tags: [bcnf, 4fn, 5fn]
aliases: [Formas Normais Avançadas]
created: 2026-07-17
updated: 2026-07-17
---

# BCNF, Quarta e Quinta Formas Normais

BCNF exige que todo determinante de dependência funcional não trivial seja superchave. É mais estrita que 3FN e pode conflitar com preservação direta de dependências.

Quarta Forma Normal trata dependências multivaloradas independentes. Se professor possui vários idiomas e várias certificações sem relação entre elas, guardá-los juntos cria combinações artificiais.

```text
PROFESSOR_IDIOMA(professor_id, idioma)
PROFESSOR_CERTIFICACAO(professor_id, certificacao)
```

Quinta Forma Normal trata dependências de junção não implicadas por chaves. Ela aparece em relações complexas nas quais fatos ternários podem ser reconstruídos de projeções menores sob regra específica.

> [!warning]
> Formas avançadas não são licença para decompor tudo. A decomposição precisa ser sem perda e corresponder a independências reais do domínio.
