---
title: Cache, Persistência e Reuso de Planos
description: "Materialização seletiva de resultados intermediários."
tags: [apache-spark, cache, persistencia]
aliases: [Cache DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Cache, Persistência e Reuso de Planos

Persistência compensa quando o mesmo resultado caro é consumido várias vezes. Ela não acelera um fluxo linear de uso único e pode piorá-lo ao competir por memória e materializar dados desnecessários.

```python
base = transformacao_cara.persist()
try:
    base.count()  # materialização controlada
    publicar_a(base)
    publicar_b(base)
finally:
    base.unpersist(blocking=False)
```

Compare custo de recomputação, tamanho materializado, frequência de reuso e nível de armazenamento. Cache de tabela e `persist` compartilham princípios, mas possuem interfaces distintas. Um checkpoint ou tabela intermediária pode ser melhor quando se deseja durabilidade, corte de linhagem ou reuso entre aplicações.
