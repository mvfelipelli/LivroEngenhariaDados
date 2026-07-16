---
title: Atualizações, Integridade, Auditoria e Logs
description: "Gestão de vulnerabilidades, proveniência e evidências."
tags: [linux, seguranca, patches, auditoria]
aliases: [Auditoria Linux, Gestão de Patches]
created: 2026-07-16
updated: 2026-07-16
---

# Atualizações, Integridade, Auditoria e Logs

Vulnerabilidade deve ser priorizada por explorabilidade, exposição, privilégio, impacto e compensações, não apenas por severidade. Inventário de pacotes e kernel em execução é pré-requisito.

```bash
uname -a
systemd-detect-virt
rpm -qa --qf '%{NAME} %{VERSION}-%{RELEASE}\n' 2>/dev/null
dpkg-query -W 2>/dev/null
journalctl -p warning --since today
```

## Ciclo de patch

1. identificar ativos e advisories;
2. avaliar contexto e prazo;
3. testar compatibilidade, backup e rollback;
4. implantar em ondas;
5. confirmar versão carregada e saúde;
6. registrar evidência e exceção residual.

Atualizar pacote de kernel sem reiniciar pode deixar kernel antigo ativo. Bibliotecas já mapeadas por processos também podem exigir restart.

## Integridade e auditoria

Assinaturas de pacotes validam origem e integridade do artefato. File integrity monitoring detecta mudanças, mas requer baseline protegido. Auditd registra eventos selecionados; excesso de regras produz custo e ruído.

Logs de segurança devem ter relógio confiável, envio remoto, acesso restrito, retenção e proteção contra alteração. Nunca registre senha, token ou chave.

> [!note]
> Ausência de log pode significar ausência do evento, falha de coleta, filtro ou adulteração. Monitore o próprio pipeline de auditoria.

Continue em [[09-Resposta-a-Incidentes-Compliance-e-Automacao]].
