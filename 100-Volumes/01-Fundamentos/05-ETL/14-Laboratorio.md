---
title: Laboratório — ETL Incremental de Pedidos
aliases: [Laboratório ETL]
tags: [engenharia-de-dados, fundamentos, etl, laboratorio, python, sqlite]
type: laboratory
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "ETL incremental reproduzível com validação, quarentena, upsert, watermark e auditoria."
---

# 14 — Laboratório

## Objetivo

Processar pedidos CSV em SQLite com chave de negócio, validação, quarentena, upsert, cursor e auditoria.

## Pré-requisitos

- Python 3.11+;
- nenhuma dependência externa.

## Requisitos

1. gerar uma entrada com quatro eventos;
2. validar chave, status e total não negativo;
3. deduplicar pela maior versão;
4. colocar inválido em quarentena;
5. fazer upsert por `(source, order_id)`;
6. persistir watermark composto;
7. auditar extraídos, válidos e rejeitados;
8. repetir sem duplicar.

## Execução

```bash
python etl_lab.py
python etl_lab.py
```

## Resultado esperado

```text
extraidos=4
validos=2
rejeitados=1
pedidos=2
total_confirmado=150.00
watermark=2026-07-16T10:03:00Z|e4
idempotencia=ok
reconciliacao=ok
```

## Próximo Capítulo

➡️ [[14-Solucao|14 — Solução]]
