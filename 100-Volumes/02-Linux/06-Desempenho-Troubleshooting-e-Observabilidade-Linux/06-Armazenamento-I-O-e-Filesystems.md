---
title: Armazenamento, I/O e Filesystems
description: "Filas, latência, throughput, cache e integridade de armazenamento."
tags: [linux, desempenho, storage, io]
aliases: [I O Linux, Performance de Disco]
created: 2026-07-16
updated: 2026-07-16
---

# Armazenamento, I/O e Filesystems

I/O deve ser analisado pelo caminho completo: aplicação, syscall, filesystem, page cache, block layer, volume virtual e dispositivo. Uma métrica do disco físico pode não explicar throttling imposto acima dele.

```bash
iostat -xz 1
pidstat -d 1
cat /proc/diskstats
df -hT
df -i
```

## Quatro dimensões

| Dimensão | Pergunta |
| --- | --- |
| IOPS | quantas operações por segundo? |
| throughput | quantos bytes por segundo? |
| latência | quanto cada operação demora? |
| fila | quanto trabalho aguarda? |

Leitura aleatória pequena e escrita sequencial grande exigem capacidades diferentes. `fsync` inclui durabilidade e pode dominar latência. Page cache torna leituras rápidas, mas flush posterior pode concentrar escrita.

```mermaid
flowchart LR
    A["Aplicação"] --> F["Filesystem"]
    F --> C["Page cache"]
    C --> B["Block layer"]
    B --> D["Dispositivo ou volume"]
```

Espaço pode acabar por bytes, inodes, blocos reservados, snapshots ou arquivos removidos ainda abertos. Use `lsof +L1` com cuidado. Erros de kernel, resets e filesystem read-only exigem prioridade sobre tuning.

> [!warning]
> Benchmarks destrutivos ou que ignoram cache podem causar impacto. Use ambiente controlado, tamanho superior à cache quando apropriado e padrão semelhante à carga real.

Continue em [[07-Processos-Servicos-e-Rede]].
