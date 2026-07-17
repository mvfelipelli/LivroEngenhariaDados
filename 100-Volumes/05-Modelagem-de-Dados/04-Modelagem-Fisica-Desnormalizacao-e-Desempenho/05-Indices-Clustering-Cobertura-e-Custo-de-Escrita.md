---
title: Índices, Clustering, Cobertura e Custo de Escrita
description: "Caminhos de acesso e seus custos operacionais."
tags: [indices, clustering, cobertura]
aliases: [Índices no Modelo Físico]
created: 2026-07-17
updated: 2026-07-17
---

# Índices, Clustering, Cobertura e Custo de Escrita

Índice representa ordenação ou estrutura auxiliar. A sequência das colunas deve refletir igualdade, intervalo, ordenação e projeção das consultas críticas.

```sql
CREATE INDEX idx_pedido_cliente_data
ON pedido (cliente_id, criado_em DESC);
```

Clustering aproxima fisicamente valores correlatos, reduzindo I/O para faixas. Cobertura evita consultar a tabela quando o índice contém toda a projeção. Índices parciais concentram subconjuntos como itens pendentes.

Cada índice adiciona espaço, cache, manutenção e write amplification. Índices sobre colunas pouco seletivas ainda podem servir a ordenação ou cobertura, mas precisam de evidência.

> [!note]
> Foreign key nem sempre cria índice automaticamente no lado referenciador; ausência pode prejudicar joins e operações na chave pai.
