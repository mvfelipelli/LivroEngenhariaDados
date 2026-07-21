---
title: Gabarito — Projeto Final Spark
description: "Respostas orientadoras dos exercícios integradores."
tags: [apache-spark, projeto-final, gabarito]
aliases: [Gabarito Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Exemplo: 99% dos pedidos válidos disponíveis em até cinco minutos, medido em janela mensal.
2. Bronze preserva payload/metadados; Silver tipa e deduplica; Gold agrega por contrato de consumo.
3. Entrada reconciliada, chave única, soma monetária, órfãos limitados e freshness.
4. `pedido_id` + versão, maior versão e desempate por ingestão/ID; batch corrige sob a mesma regra.
5. A capacidade total precisa processar chegada corrente mais duas vezes a taxa média acumulada no backlog.
6. Mesma entrada, saída isolada, comparação de schema/contagem/soma/distribuição e promoção reversível.
7. Confirmar destino anterior, invalidar staging incompleto, repetir run idempotente e reconciliar antes do commit.
8. Nova versão de contrato, leitura dual, backfill, consumidores migrados, shadow e retirada controlada.
