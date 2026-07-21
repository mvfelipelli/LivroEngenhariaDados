---
title: Requisitos, Trade-offs e Atributos de Qualidade
description: "Critérios que orientam decisões arquiteturais."
tags: [arquitetura-de-dados, requisitos, atributos-de-qualidade]
aliases: [Atributos de Qualidade de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Requisitos, Trade-offs e Atributos de Qualidade

Requisitos funcionais descrevem capacidades; atributos de qualidade definem como o sistema deve se comportar. Exemplos: disponibilidade, latência, throughput, durabilidade, consistência, segurança, auditabilidade, evolutividade e custo.

“Tempo real” é vago. Transforme-o em cenário: sob pico de 20 mil eventos/s, 99% dos eventos válidos devem estar consultáveis em até dois minutos, com recuperação de uma hora de backlog em 30 minutos.

Trade-offs precisam de contexto e evidência. Consistência forte pode aumentar latência; retenção longa eleva custo; múltiplos motores ampliam flexibilidade e operação.

Registre decisão, alternativas, consequência e gatilho de revisão em um Architecture Decision Record.
