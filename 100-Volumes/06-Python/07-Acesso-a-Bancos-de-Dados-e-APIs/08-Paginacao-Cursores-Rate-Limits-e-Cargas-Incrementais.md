---
title: Paginação, Cursores, Rate Limits e Cargas Incrementais
description: "Consumo completo e retomável de coleções remotas."
tags: [python, paginacao, rate-limit, incremental]
aliases: [Paginação de APIs Python]
created: 2026-07-17
updated: 2026-07-17
---

# Paginação, Cursores, Rate Limits e Cargas Incrementais

Offset/limit é simples, mas inserções e remoções durante a leitura podem duplicar ou omitir itens. Cursor opaco ou keyset oferece continuidade mais estável quando a API implementa snapshot ou ordenação consistente.

```python
cursor = None
while True:
    pagina = cliente.listar(cursor=cursor, limite=100)
    persistir(pagina.itens)
    cursor = pagina.proximo_cursor
    if cursor is None:
        break
```

O cursor deve ser tratado como opaco. Persista-o somente após commit dos itens. Detecte cursor repetido e limite páginas para evitar loop infinito.

Rate limits podem ser globais, por token ou rota. Observe headers documentados, reduza concorrência e aguarde `Retry-After`. Incremental por `updated_at` precisa de desempate por ID e sobreposição controlada para dados tardios.
