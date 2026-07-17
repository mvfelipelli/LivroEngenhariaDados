---
title: Introdução
description: "Otimização baseada em trabalho executado, não em intuição."
tags: [sql, introducao, otimizacao]
aliases: [Introdução à Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Uma consulta descreve **o resultado**, enquanto o banco decide **como obtê-lo**. Para a mesma expressão SQL, o otimizador pode ler uma tabela inteira, percorrer um índice, construir uma tabela hash ou ordenar conjuntos intermediários. A escolha depende do esquema, dos dados, das estatísticas, dos recursos e dos operadores disponíveis.

Tempo isolado é um sinal insuficiente: cache, concorrência e infraestrutura alteram a medição. Um diagnóstico robusto combina plano, linhas estimadas e reais, leituras, memória, temporários e repetição controlada.

```mermaid
flowchart TD
    B["Baseline reproduzível"] --> H["Hipótese sobre o gargalo"]
    H --> C["Uma mudança controlada"]
    C --> V["Validar resultado e plano"]
    V --> R{"Meta atingida?"}
    R -- não --> H
    R -- sim --> G["Observar regressões"]
```

Na DataRetail S.A., relatórios lentos não serão tratados com a regra simplista “adicione um índice”. O ponto de partida será o caminho crítico: quantas linhas entram em cada operador, quantas sobrevivem e onde ocorre I/O, CPU ou espera.
