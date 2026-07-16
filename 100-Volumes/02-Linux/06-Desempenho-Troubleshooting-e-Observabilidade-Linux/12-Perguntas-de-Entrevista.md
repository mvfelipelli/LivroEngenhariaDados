---
title: Perguntas de Entrevista — Performance Linux
description: "Perguntas progressivas com respostas fundamentadas."
tags: [linux, desempenho, entrevista]
aliases: [Entrevista Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Perguntas de Entrevista

## 1. O que é método USE?

Para cada recurso, verificar utilização, saturação e erros, evitando pontos cegos.

## 2. O que é RED?

Taxa, erros e duração para cada serviço ou operação.

## 3. Load average é uso de CPU?

Não. Resume tarefas executáveis e algumas em espera ininterruptível; deve ser interpretado com CPU e estados.

## 4. CPU total baixa elimina gargalo de CPU?

Não. Uma thread pode saturar um núcleo, cgroup pode sofrer throttling ou lock pode serializar trabalho.

## 5. Memória free baixa é problema?

Não isoladamente. Linux usa cache. Analise `MemAvailable`, reclaim, PSI, swap e OOM.

## 6. RSS e PSS diferem em quê?

RSS conta páginas residentes por processo; PSS divide páginas compartilhadas proporcionalmente.

## 7. O que iowait significa?

Tempo em que uma CPU ficou ociosa enquanto havia I/O pendente; não mede diretamente utilização do disco.

## 8. Como analisar disco lento?

Correlacione latência, fila, throughput, IOPS, erros e padrão de acesso em todas as camadas.

## 9. Quando usar `strace`?

Para investigar syscalls, erros e espera, considerando overhead e volume de saída.

## 10. O que flame graph mostra?

Distribuição agregada de stacks amostradas. Largura representa frequência, não duração cronológica.

## 11. Por que percentis importam?

Médias ocultam cauda; p95 e p99 mostram a experiência de operações lentas, desde que haja amostra suficiente.

## 12. Como validar tuning?

Com hipótese, baseline, carga representativa, uma mudança, métricas de objetivo e efeitos colaterais, além de rollback.

## 13. Reiniciar é troubleshooting?

Pode conter impacto, mas não explica a causa e destrói evidências. Deve ser registrado e seguido de análise.

## 14. Como planejar capacidade?

Projete demanda, sazonalidade, crescimento, falhas e lead time; mantenha headroom baseado em SLO e risco.
