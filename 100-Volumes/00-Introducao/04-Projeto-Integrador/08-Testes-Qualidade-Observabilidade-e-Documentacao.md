---
title: Testes, Qualidade, Observabilidade e Documentação
description: "Evidências obrigatórias em todas as etapas do projeto."
tags: [testes, qualidade-de-dados, observabilidade]
aliases: [Qualidade Projeto DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Testes, Qualidade, Observabilidade e Documentação

Testes evoluem com o projeto: funções, consultas, schemas, propriedades, conectores, replay e recuperação. Qualidade reconcilia entrada, válidos, quarentena e saída.

Observabilidade registra execução, versão, dataset, contagens, somas, duração, freshness e erros. Métricas técnicas sem métricas de dados não provam correção.

Documentação mínima:

- README com execução e arquitetura;
- contrato de cada dataset;
- ADRs para decisões relevantes;
- catálogo e lineage;
- runbooks de falha e backfill;
- changelog e limitações.

> [!note]
> Documentação deve ser validável: comandos funcionam, links resolvem e critérios correspondem aos testes.
