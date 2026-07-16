---
title: Operação de Plataformas de Dados no Linux
description: "Práticas integradas para implantar e operar serviços de dados confiáveis no Linux."
tags: [linux, operacao, plataformas-de-dados, volume-02]
aliases: [Módulo 08 Linux, Operação de Dados Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Módulo 08 — Operação de Plataformas de Dados no Linux

Operar uma plataforma de dados significa preservar serviço, dados e evidências durante mudanças, picos e falhas. O host Linux é parte de um sistema que inclui workload, armazenamento, rede, identidade e processos humanos.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Requisitos-SLOs-Topologia-e-Modelo-Operacional|Requisitos, SLOs, Topologia e Modelo Operacional]]
4. [[04-Implantacao-Configuracao-e-Gestao-de-Servicos|Implantação, Configuração e Gestão de Serviços]]
5. [[05-Estado-Armazenamento-Backup-e-Recuperacao|Estado, Armazenamento, Backup e Recuperação]]
6. [[06-Automacao-Agendamento-Dependencias-e-Idempotencia|Automação, Agendamento, Dependências e Idempotência]]
7. [[07-Monitoramento-Saude-SLOs-e-Runbooks|Monitoramento, Saúde, SLOs e Runbooks]]
8. [[08-Incidentes-Continuidade-DR-e-Postmortems|Incidentes, Continuidade, DR e Postmortems]]
9. [[09-Capacidade-Mudancas-Custo-e-Melhoria-Continua|Capacidade, Mudanças, Custo e Melhoria Contínua]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    D["Design"] --> I["Implantação"]
    I --> O["Operação"]
    O --> R["Recuperação"]
    R --> M["Melhoria"]
    M --> D
```
