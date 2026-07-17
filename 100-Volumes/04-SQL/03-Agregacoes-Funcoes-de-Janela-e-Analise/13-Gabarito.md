---
title: Gabarito — Agregações e Funções de Janela
description: "Respostas orientadoras dos exercícios."
tags: [sql, gabarito, window-functions]
aliases: [Gabarito Análise SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Agregação reduz o grão; janela preserva cada linha.
2. `WHERE` filtra entradas, `FILTER` entradas de uma agregação e `HAVING` grupos formados.
3. Ausência de linhas pode significar métrica desconhecida; zero é uma decisão do domínio.
4. Único e arbitrado; empate com lacuna; empate sem lacuna.
5. Com ordem, normalmente vai do início ao peer atual; declare até `UNBOUNDED FOLLOWING` para o último da partição.
6. Use `SUM(CASE...)` ou agregações com `FILTER`, agrupadas por loja.
7. `ROW_NUMBER` ou ranking em CTE, com desempate estável, seguido de filtro externo.
8. Agregue por dia e loja; use `LAG` e `SUM(...) OVER` com frame explícito.
9. Gere calendário, faça left join, trate ausência conforme contrato e aplique frame de seis anteriores mais atual.
10. Compare soma fonte, soma agrupada e último acumulado; teste empates, lacunas, nulos e partições unitárias.
