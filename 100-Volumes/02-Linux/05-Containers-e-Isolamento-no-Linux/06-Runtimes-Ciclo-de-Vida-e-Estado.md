---
title: Runtimes, Ciclo de Vida e Estado
description: "Papel de engines, runtimes OCI, processos e sinais."
tags: [linux, containers, runtime]
aliases: [Runtime OCI, Ciclo de Vida do Contêiner]
created: 2026-07-16
updated: 2026-07-16
---

# Runtimes, Ciclo de Vida e Estado

Uma engine gerencia imagens, rede, volumes e experiência do usuário. Um runtime de alto nível mantém ciclo de vida; um runtime OCI de baixo nível configura namespaces, cgroups, mounts, capabilities e executa o processo descrito no bundle.

```mermaid
sequenceDiagram
    participant U as Usuário ou orquestrador
    participant E as Engine ou runtime alto nível
    participant O as Runtime OCI
    participant K as Kernel
    U->>E: criar contêiner
    E->>O: bundle OCI
    O->>K: namespaces, cgroups e mounts
    O->>K: exec do processo
    K-->>E: estado e exit code
```

O contêiner permanece ativo enquanto seu processo principal vive. `exec` inicia processo adicional no mesmo contexto; não cria novo contêiner. Pausar normalmente congela tarefas; parar envia sinal e aguarda período de graça; matar encerra sem cooperação.

## Contrato do processo

```dockerfile
ENTRYPOINT ["/app/worker"]
CMD ["--config", "/etc/dataretail/config.yaml"]
```

A forma JSON evita shell intermediário e melhora sinais. A aplicação deve escrever logs em stdout/stderr, tratar `SIGTERM`, parar de aceitar trabalho, concluir ou devolver tarefas e sair com status significativo.

Health checks têm papéis distintos: *startup* protege inicialização lenta, *readiness* controla tráfego e *liveness* detecta travamento recuperável. Reiniciar não corrige dependência indisponível e pode criar tempestade.

> [!tip]
> Registre motivo de término, status, OOM, reinícios e duração; “Exited” descreve estado, não causa.

Próximo: [[07-Armazenamento-Volumes-e-Persistencia]].
