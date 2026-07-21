---
title: Requisitos, Escopo e Critérios de Aceite
description: "Definição verificável do sistema a construir."
tags: [apache-spark, requisitos, criterios-de-aceite]
aliases: [Requisitos Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Requisitos, Escopo e Critérios de Aceite

O sistema recebe pedidos, clientes, lojas e pagamentos. Publica pedidos canônicos, receita diária por loja e indicadores de atraso. O volume inicial é 2 TB/dia, pico de 150 mil eventos/s e retenção curada de cinco anos.

Critérios:

- 100% da entrada reconciliada entre válidos e quarentena;
- unicidade por `pedido_id` e versão;
- soma monetária preservada após joins;
- batch diário em até 60 minutos;
- streaming com 99% dos eventos publicados em até cinco minutos;
- replay sem duplicação;
- recuperação documentada e testada;
- nenhum segredo ou dado pessoal em logs.

Ficam fora do escopo serving transacional, BI e treinamento de modelos.
