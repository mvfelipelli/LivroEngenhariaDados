---
title: Rede, Nomes, Portas e Diagnóstico
aliases: [Rede Linux]
tags: [linux, rede, dns, portas, diagnostico]
created: 2026-07-16
updated: 2026-07-16
description: "Modelo de rede e diagnóstico sistemático em Linux."
---

# Rede, Nomes, Portas e Diagnóstico

Diagnóstico deve separar resolução de nomes, rota, conectividade, transporte, TLS e aplicação. “A rede caiu” é uma hipótese ampla demais.

```bash
ip address
ip route
getent hosts exemplo.internal
ss -lntp
curl -v --max-time 10 https://exemplo.internal/health
```

DNS traduz nomes segundo configuração e cache. Uma porta em `LISTEN` indica socket local, não acessibilidade externa. Firewall, bind address, rota e políticas intermediárias ainda importam.

```mermaid
flowchart LR
    A[Nome] --> B[DNS]
    B --> C[Rota]
    C --> D[Conexão TCP]
    D --> E[TLS]
    E --> F[Protocolo da aplicação]
```

Use `ping` apenas como um sinal; ICMP pode estar bloqueado. Capture tráfego somente com autorização, pois pacotes podem conter dados sensíveis.

> [!tip]
> Teste a partir do mesmo namespace de rede e identidade do serviço afetado.

Evidências e recuperação aparecem em [[08-Logs-Rotacao-Backup-e-Recuperacao]].
