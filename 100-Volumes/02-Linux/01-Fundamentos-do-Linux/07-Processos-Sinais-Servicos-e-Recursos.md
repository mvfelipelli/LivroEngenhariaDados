---
title: Processos, Sinais, Serviços e Recursos
aliases: [Processos Linux]
tags: [linux, processos, sinais, servicos, recursos]
created: 2026-07-16
updated: 2026-07-16
description: "Ciclo de vida de processos, sinais e inspeção de recursos."
---

# Processos, Sinais, Serviços e Recursos

Processo é uma instância de programa com PID, processo pai, credenciais, memória, descritores e estado. O kernel agenda threads e contabiliza recursos.

```bash
ps -ef
pgrep -a python
top
free -h
df -h
du -sh dados
```

## Sinais

`SIGTERM` solicita término e permite limpeza. `SIGKILL` encerra sem tratamento e deve ser último recurso. `SIGHUP` costuma indicar recarga, conforme a aplicação.

```bash
kill -TERM "$pid"
```

Serviços de longa duração são supervisionados por um init system, frequentemente systemd. A unidade define comando, dependências, identidade, reinício e limites. `systemctl status` mostra estado; `journalctl` consulta o journal quando disponível.

```mermaid
stateDiagram-v2
    [*] --> Criado
    Criado --> Executando
    Executando --> Suspenso
    Suspenso --> Executando
    Executando --> Encerrado
    Encerrado --> [*]
```

> [!warning]
> Disco livre e memória disponível não contam toda a história. Inodes, I/O, swap, limites e pressão também podem causar falhas.

O terminal conecta essas observações em [[08-Terminal-Comandos-Documentacao-e-Pipes]].
