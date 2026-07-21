---
title: Solução do Laboratório — Auditoria do Ambiente
description: "Modelo de evidências para validar a estação."
tags: [laboratorio, solucao, ambiente]
aliases: [Solução da Auditoria do Ambiente]
created: 2026-07-21
updated: 2026-07-21
---

# Solução do Laboratório — Auditoria do Ambiente

Use uma matriz como esta:

| Componente | Comando | Esperado | Estado |
|---|---|---|---|
| Git | `git --version` | versão suportada | aprovado |
| Python | `python --version` | versão documentada | aprovado |
| Docker | `docker version` | daemon acessível | aprovado |
| PostgreSQL | `pg_isready` | accepting connections | aprovado |

Para cada falha, registre sintoma, hipótese, teste e correção. A solução é aceita quando outra pessoa consegue repetir a validação sem conhecer detalhes não documentados.

Próximo: [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/15-Referencias|Referências]].
