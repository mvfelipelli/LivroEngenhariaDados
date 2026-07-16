---
title: Responsabilidade e Ciclo de Administração
aliases: [Ciclo de Administração Linux]
tags: [linux, administracao, mudancas, operacao]
created: 2026-07-16
updated: 2026-07-16
description: "Inventário, baseline, mudança, verificação e recuperação."
---

# Responsabilidade e Ciclo de Administração

O administrador preserva disponibilidade, integridade, confidencialidade e recuperabilidade. Isso exige inventário de hosts, owners, função, criticidade, versões, dependências e dados.

## Ciclo de mudança

1. definir resultado e risco;
2. registrar baseline;
3. validar backup e rollback;
4. aplicar em ambiente controlado;
5. verificar estado técnico e serviço;
6. observar período suficiente;
7. registrar evidências.

Mudanças emergenciais reduzem etapas formais, não controles essenciais. Comandos privilegiados devem entrar no log de mudança com motivo e resultado.

```bash
date --iso-8601=seconds
uname -r
systemctl --failed
df -h
```

> [!tip]
> Baseline útil é pequena e orientada ao serviço: versão, processos, portas, mounts, capacidade e SLO.

O primeiro domínio administrativo é [[04-Gerenciamento-de-Pacotes-e-Atualizacoes]].
