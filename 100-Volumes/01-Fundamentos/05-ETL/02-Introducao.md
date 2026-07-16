---
title: Introdução ao ETL
aliases: [ETL Introduction]
tags: [engenharia-de-dados, fundamentos, etl, introducao]
type: chapter
order: 02
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Motivação, contexto e responsabilidades de processos ETL."
---

# 02 — Introdução

## Sistemas não compartilham contexto automaticamente

Pedidos, clientes e produtos podem existir em Bancos de Dados, APIs e arquivos, com chaves, tipos e ritmos distintos. Copiar bytes não basta: o consumidor precisa receber fatos interpretáveis, íntegros e atualizados.

ETL organiza essa passagem em três responsabilidades: extrair com impacto controlado, transformar segundo regras explícitas e carregar com semântica previsível.

```mermaid
flowchart LR
    A[Contexto da fonte] --> B[Contrato de extração]
    B --> C[Regras de transformação]
    C --> D[Contrato de destino]
    D --> E[Consumo]
```

## ETL como sistema

Um ETL profissional inclui mais que código de transformação:

- estado de execução;
- metadados e linhagem;
- staging e preservação de entrada;
- controles de qualidade;
- segurança e minimização;
- retries e reprocessamento;
- auditoria e observabilidade;
- reconciliação e acordos de serviço.

## Questões orientadoras

- qual fato e qual grão serão entregues?
- como mudanças e exclusões serão detectadas?
- qual atraso é aceitável?
- o que torna uma execução completa?
- como repetir sem duplicar?
- como reconstruir o destino?
- quem responde por regras e falhas?

## Próximo Capítulo

➡️ [[03-O-que-e-ETL|03 — O que é ETL]]
