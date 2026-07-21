---
title: Ingestão, Contratos, Qualidade e Quarentena
description: "Fronteira de entrada auditável e reconciliada."
tags: [apache-spark, ingestao, qualidade-de-dados]
aliases: [Ingestão Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Ingestão, Contratos, Qualidade e Quarentena

Toda entrada recebe `source`, `ingestion_time`, `run_id`, identificador do arquivo/tópico e payload bruto quando permitido. O parser usa schema explícito e separa falha sintática de violação semântica.

Regras mínimas: ID obrigatório, versão não negativa, instante plausível, moeda aceita, valor dentro do domínio e itens não vazios. Dimensões são validadas quanto à unicidade antes de joins.

```text
entrada = válidos + quarentena
soma_entrada_aceita = soma_válidos + soma_quarentena_contabilizável
```

Limites de qualidade definem falha, alerta ou continuação. Amostras são mascaradas; payload sensível possui acesso e retenção restritos.
