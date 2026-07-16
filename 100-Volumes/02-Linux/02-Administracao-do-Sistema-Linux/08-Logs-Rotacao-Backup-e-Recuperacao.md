---
title: Logs, Rotação, Backup e Recuperação
aliases: [Backup Linux, Logrotate]
tags: [linux, logs, rotacao, backup, recuperacao]
created: 2026-07-16
updated: 2026-07-16
description: "Retenção de evidências e recuperação testada."
---

# Logs, Rotação, Backup e Recuperação

Logs precisam de formato, destino, owner, acesso, retenção e rotação. Rotação limita crescimento e pode comprimir históricos. Aplicações devem reabrir arquivo ou receber sinal adequado após rotação.

Backups protegem contra falhas, erro humano e corrupção, mas só a restauração testada demonstra recuperabilidade. Defina RPO, RTO, escopo, consistência, criptografia, retenção e cópia fora do domínio de falha.

```mermaid
flowchart LR
    A[Dados e configuração] --> B[Snapshot ou backup]
    B --> C[Verificação de integridade]
    C --> D[Cópia isolada]
    D --> E[Teste de restauração]
    E --> F[Evidência de RPO e RTO]
```

```bash
journalctl --disk-usage
logrotate --debug /etc/logrotate.conf
sha256sum backup.tar
```

RAID melhora disponibilidade de disco, mas não substitui backup. Snapshot rápido pode capturar estado inconsistente sem coordenação com a aplicação.

> [!warning]
> Não coloque o único backup no mesmo host, credencial e domínio de falha do original.

Operação sustentável é detalhada em [[09-Capacidade-Hardening-Manutencao-e-Automacao]].
