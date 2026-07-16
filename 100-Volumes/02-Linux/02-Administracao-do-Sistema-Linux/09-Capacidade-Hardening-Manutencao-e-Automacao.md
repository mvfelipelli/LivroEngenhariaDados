---
title: Capacidade, Hardening, Manutenção e Automação
aliases: [Hardening Linux, Manutenção Linux]
tags: [linux, capacidade, hardening, manutencao, automacao]
created: 2026-07-16
updated: 2026-07-16
description: "Planejamento de capacidade e administração segura automatizada."
---

# Capacidade, Hardening, Manutenção e Automação

Capacidade deve considerar tendência, pico, margem e tempo de expansão. CPU, memória, swap, disco, inodes, I/O, rede, PIDs e descritores podem limitar serviços.

Hardening reduz superfície: remover serviços desnecessários, corrigir vulnerabilidades, limitar acesso, proteger boot e credenciais, aplicar MAC quando apropriado e auditar mudanças.

## Automação

Automação declarativa converge ao estado desejado; scripts imperativos precisam de idempotência e verificações. Separe planejamento de aplicação e ofereça modo dry-run quando possível.

```bash
ulimit -a
systemctl --failed
ss -lntup
find /etc -xdev -type f -perm -0002
```

```mermaid
flowchart LR
    A[Baseline] --> B[Detectar drift]
    B --> C[Planejar correção]
    C --> D[Aplicar em lote pequeno]
    D --> E[Verificar serviço e segurança]
    E -. atualizar baseline .-> A
```

> [!note]
> Hardening precisa respeitar função e ameaça. Controle que quebra recuperação ou observabilidade pode aumentar risco total.

Veja o caso integrado em [[10-Estudo-de-Caso-DataRetail]].
