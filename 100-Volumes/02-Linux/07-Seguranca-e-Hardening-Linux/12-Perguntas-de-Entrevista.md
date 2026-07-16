---
title: Perguntas de Entrevista — Segurança Linux
description: "Perguntas progressivas com respostas fundamentadas."
tags: [linux, seguranca, entrevista]
aliases: [Entrevista Segurança Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Perguntas de Entrevista

## 1. O que é hardening?

Redução contextual de superfície e privilégio por configuração, remoção e controles verificáveis.

## 2. Por que benchmark não deve ser aplicado cegamente?

Porque função, ameaça, topologia e disponibilidade variam; um controle inadequado pode quebrar o serviço.

## 3. DAC e MAC diferem em quê?

DAC usa owner, grupos e ACLs; MAC aplica política obrigatória adicional por LSM.

## 4. Bloquear senha encerra todo acesso?

Não necessariamente. Chaves SSH, tokens, sessões e outros mecanismos podem continuar válidos.

## 5. Por que `sudo ALL` é problemático?

Concede privilégio amplo, reduz separação e permite múltiplos caminhos para shell root.

## 6. O que capabilities resolvem?

Dividem poderes de root em unidades menores, permitindo conceder apenas operações necessárias.

## 7. Seccomp e SELinux são equivalentes?

Não. Seccomp filtra syscalls; SELinux aplica controle de acesso obrigatório a objetos e domínios.

## 8. Criptografia de disco protege host ligado?

Protege principalmente mídia em repouso. Com chaves carregadas, permissões e identidade continuam essenciais.

## 9. Como alterar SSH com segurança?

Valide sintaxe, mantenha console ou sessão alternativa, teste nova sessão e preserve rollback.

## 10. Como priorizar patch?

Combine severidade, exploração, exposição, privilégio, impacto, compensações e prazo operacional.

## 11. O que é drift?

Desvio do estado real em relação ao baseline aprovado, causado por mudanças manuais, atualização ou falha.

## 12. Logs locais bastam?

Não para alta confiança: invasor pode alterá-los. Envio remoto e monitoramento do pipeline aumentam resiliência.

## 13. O que preservar em incidente?

Linha do tempo, estado volátil conforme plano, imagens ou artefatos, logs, hashes e cadeia de custódia.

## 14. Compliance prova segurança?

Não. Demonstra requisitos avaliados; risco real depende de ameaças, eficácia e mudanças contínuas.
