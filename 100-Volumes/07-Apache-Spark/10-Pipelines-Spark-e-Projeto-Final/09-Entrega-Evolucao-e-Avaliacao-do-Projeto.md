---
title: Entrega, Evolução e Avaliação do Projeto
description: "Artefatos, rubrica e manutenção do sistema."
tags: [apache-spark, entrega, avaliacao]
aliases: [Avaliação Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Entrega, Evolução e Avaliação do Projeto

A entrega contém arquitetura, código empacotável, configuração de exemplo, schemas, testes, dados sintéticos, comandos, dashboards, runbooks e registro de decisões.

Rubrica de 100 pontos:

| Critério | Pontos |
|---|---:|
| Correção e reconciliação | 25 |
| Arquitetura e idempotência | 20 |
| Performance e capacidade | 15 |
| Testes e qualidade | 15 |
| Observabilidade e operação | 15 |
| Segurança e documentação | 10 |

Falha em reconciliação, exposição de segredo ou impossibilidade de replay impede aprovação. Evoluções passam por compatibilidade de schema, shadow e plano de migração/rollback.
