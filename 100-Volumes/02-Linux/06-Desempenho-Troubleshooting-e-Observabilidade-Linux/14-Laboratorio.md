---
title: Laboratório — Análise USE de um Batch
description: "Classificação reproduzível de métricas de CPU, memória e I/O."
tags: [linux, desempenho, laboratorio, python]
aliases: [Laboratório Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Laboratório — Análise USE de um Batch

## Objetivo

Analisar dois snapshots da DataRetail S.A., calcular deltas e identificar o recurso limitante com regras transparentes.

## Pré-requisitos

- Python 3.10 ou superior;
- somente biblioteca padrão;
- nenhum privilégio ou acesso externo.

## Ambiente

As métricas são fixtures determinísticas. Contadores estão em unidades acumuladas; gauges e PSI representam a janela final.

## Passos

1. Salve [[14-Solucao|a solução]] como `analisar_use.py`.
2. Execute `python analisar_use.py`.
3. Verifique os deltas de CPU e I/O.
4. Relacione PSI, swap, fila e latência à conclusão.
5. Execute novamente e compare a saída.

## Resultado esperado

```text
cpu_utilizacao=45.0%
cpu_saturacao=nao
memoria_pressao=sim
swap_delta_mb=768
io_fila=12.0
io_latencia_ms=42.0
recurso_limitante=memoria_e_io
analise=ok
```

## Validação

As oito linhas devem se repetir e o processo deve retornar zero.

## Conclusão

O laboratório mostra que CPU moderada pode coexistir com saturação em memória e armazenamento. Limiares reais devem derivar do SLO e baseline.
