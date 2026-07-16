---
title: Processos, Namespaces e Isolamento
description: "Visões isoladas de PID, mount, rede, usuários e IPC."
tags: [linux, containers, namespaces]
aliases: [Namespaces Linux, Isolamento de Processos]
created: 2026-07-16
updated: 2026-07-16
---

# Processos, Namespaces e Isolamento

Um namespace limita o conjunto de recursos que processos enxergam. Ele não cria o recurso físico; cria uma visão e regras de pertencimento.

| Namespace | Isola principalmente |
| --- | --- |
| PID | identificadores e árvore de processos |
| mount | mounts e root filesystem |
| network | interfaces, rotas, portas e firewall |
| UTS | hostname e nome de domínio |
| IPC | filas, semáforos e memória compartilhada |
| user | IDs e capabilities |
| cgroup | visão da hierarquia de cgroups |
| time | alguns relógios do sistema |

```bash
lsns
readlink /proc/self/ns/pid
unshare --user --map-root-user --pid --fork --mount-proc sh
```

O PID 1 dentro do namespace recebe sinais e deve colher filhos órfãos. Uma aplicação que ignora `SIGTERM` força encerramento abrupto após o período de graça.

## User namespaces e privilégios

Um UID que parece 0 dentro do namespace pode mapear para usuário sem privilégio fora dele. Isso reduz impacto, mas depende de configuração do kernel, mounts, capabilities e políticas. *Rootless containers* combinam user namespaces e mecanismos sem daemon privilegiado.

## `chroot` não basta

`chroot` muda a raiz de resolução de caminhos, mas não isola processos, rede, IPC ou privilégios. Contêineres combinam mount namespace, `pivot_root`, políticas e limites.

> [!tip]
> Use `nsenter` e `/proc/<pid>/ns` para investigar o mesmo contexto do processo, sempre com autorização.

Continue em [[04-Cgroups-Recursos-e-Qualidade-de-Servico]].
