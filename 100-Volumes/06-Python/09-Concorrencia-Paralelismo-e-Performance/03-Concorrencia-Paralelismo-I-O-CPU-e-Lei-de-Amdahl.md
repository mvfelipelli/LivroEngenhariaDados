---
title: Concorrência, Paralelismo, I/O, CPU e Lei de Amdahl
description: "Classificação da carga e limites de aceleração."
tags: [python, concorrencia, cpu, io]
aliases: [Lei de Amdahl Python]
created: 2026-07-17
updated: 2026-07-17
---

# Concorrência, Paralelismo, I/O, CPU e Lei de Amdahl

Carga I/O-bound passa grande parte do tempo aguardando rede ou disco; threads e asyncio podem sobrepor espera. Carga CPU-bound executa cálculo; processos ou código nativo que libera o GIL podem explorar núcleos.

Lei de Amdahl limita speedup pela fração serial. Se 20% é estritamente serial, paralelismo infinito não ultrapassa aceleração de 5x. Overhead de coordenação reduz ainda mais.

Throughput mede unidades por tempo; latência mede duração individual. Concorrência pode melhorar throughput e piorar p99 por contenção. Little relaciona trabalho em voo, taxa e tempo médio: mais latência mantém mais itens no sistema.

Antes de escolher modelo, identifique recurso saturado, tamanho das tarefas, custo de serialização, limites externos e requisito de ordenação.
