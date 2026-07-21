---
title: Operações Stateful e State Store
description: "Persistência incremental de agregações e estado por chave."
tags: [apache-spark, state-store, stateful]
aliases: [State Store Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Operações Stateful e State Store

Agregações, deduplicação, joins stream-stream e funções por chave mantêm informações entre lotes. O state store organiza esse estado por partição e versão; checkpoint preserva metadados necessários à recuperação.

Estado sem limite cresce até pressionar memória, disco e latência. Limites vêm de watermark, timeout e condições temporais. Monitore `numRowsTotal`, `numRowsUpdated`, memória, arquivos do state store e tempo de commit.

Reparticionar ou alterar operadores stateful pode ser incompatível com checkpoint existente. Trate topologia, schema de estado e número de partições como parte da versão da aplicação.

Backends disponíveis variam por versão e distribuição; escolha com testes de recuperação e carga.
