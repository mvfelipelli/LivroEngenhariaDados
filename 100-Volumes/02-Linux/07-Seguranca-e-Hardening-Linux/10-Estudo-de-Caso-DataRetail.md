---
title: Estudo de Caso — Hardening do Gateway da DataRetail
description: "Baseline baseado em risco para host de integração."
tags: [linux, seguranca, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Hardening]
created: 2026-07-16
updated: 2026-07-16
---

# Estudo de Caso — DataRetail S.A.

Um gateway transfere arquivos de parceiros para a DataRetail S.A. Ele é exposto a uma zona controlada, manipula dados comerciais e acessa armazenamento interno. A auditoria encontrou login SSH por senha, conta compartilhada, serviços desnecessários e logs apenas locais.

## Plano priorizado

| Risco | Controle | Evidência |
| --- | --- | --- |
| credencial reutilizada | chaves individuais, MFA e sem root remoto | configuração e teste |
| privilégio sem atribuição | sudo mínimo por identidade | regra e log |
| superfície excessiva | remover serviços e negar por padrão | listeners e firewall |
| movimento lateral | egress somente ao storage e DNS | policy e teste |
| adulteração local | logs remotos e integridade | recebimento externo |
| arquivo malicioso | quarentena, usuário isolado e scan | eventos do fluxo |

## Implantação

```mermaid
flowchart LR
    B["Baseline"] --> C["Canário"]
    C --> T["Teste funcional e de acesso"]
    T --> O["Onda de produção"]
    O --> D["Detecção de drift"]
```

A equipe manteve console fora de banda, testou `sshd -t`, abriu uma segunda sessão antes de fechar a primeira e validou transferência ponta a ponta. Uma exceção temporária de algoritmo legado recebeu parceiro responsável e data de expiração.

## Resultado

O host passou a ter identidade individual, menor exposição, logs externos e processo de patch mensurável. O sucesso não foi “100% no scanner”, mas redução de caminhos relevantes sem interromper a integração.

Pratique a verificação em [[14-Laboratorio]].
