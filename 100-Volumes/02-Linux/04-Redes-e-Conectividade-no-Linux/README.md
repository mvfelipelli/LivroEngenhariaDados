---
title: Redes e Conectividade no Linux
description: "Fundamentos, configuração, segurança e diagnóstico de redes para plataformas de dados."
tags: [linux, redes, conectividade, volume-02]
aliases: [Módulo 04 Linux, Redes Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Módulo 04 — Redes e Conectividade no Linux

Redes conectam processos distribuídos. Para diagnosticar uma plataforma de dados, é preciso distinguir nome, endereço, rota, porta, sessão, protocolo e política de segurança.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Camadas-Encapsulamento-e-Fluxo-de-Pacotes|Camadas, Encapsulamento e Fluxo de Pacotes]]
4. [[04-Interfaces-Enlace-ARP-NDP-e-MTU|Interfaces, Enlace, ARP, NDP e MTU]]
5. [[05-Enderecamento-IP-Sub-redes-e-Roteamento|Endereçamento IP, Sub-redes e Roteamento]]
6. [[06-Transporte-Portas-Sockets-TCP-e-UDP|Transporte, Portas, Sockets, TCP e UDP]]
7. [[07-DNS-Resolucao-de-Nomes-e-Servicos|DNS, Resolução de Nomes e Serviços]]
8. [[08-Configuracao-Network-Namespaces-e-Firewall|Configuração, Network Namespaces e Firewall]]
9. [[09-Diagnostico-Seguranca-Desempenho-e-Observabilidade|Diagnóstico, Segurança, Desempenho e Observabilidade]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    N["Nome"] --> D["DNS"]
    D --> I["Endereço IP"]
    I --> R["Rota"]
    R --> P["Porta"]
    P --> A["Protocolo de aplicação"]
```
