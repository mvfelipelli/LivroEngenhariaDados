---
title: Processos, IPC, ProcessPoolExecutor e Custos
description: "Paralelismo de CPU com isolamento de memória."
tags: [python, multiprocessing, ipc, cpu]
aliases: [Processos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Processos, IPC, ProcessPoolExecutor e Custos

Processos possuem memória e interpretador separados, permitindo paralelismo de CPU. Argumentos e retornos atravessam IPC e normalmente precisam ser serializados.

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as executor:
    totais = list(executor.map(calcular_particao, caminhos, chunksize=4))
```

Funções e dados precisam ser importáveis e serializáveis. Proteja o entry point com `if __name__ == "__main__"`, especialmente em plataformas que iniciam processos por spawn.

Processos têm startup, memória e cópia de dados. Agrupe tarefas pequenas, envie referências ou blocos compactos e devolva resultados reduzidos. Não compartilhe conexão de banco criada antes do fork; cada processo cria e encerra seus recursos.
