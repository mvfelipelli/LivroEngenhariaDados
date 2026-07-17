---
title: Escopos, Closures, Decorators e Funções de Alta Ordem
description: "Estado lexical e composição de comportamento."
tags: [python, closures, decorators, escopo]
aliases: [Closures Python]
created: 2026-07-17
updated: 2026-07-17
---

# Escopos, Closures, Decorators e Funções de Alta Ordem

A resolução de nomes segue escopos local, enclosing, global e built-in. `global` e `nonlocal` permitem reatribuir nomes externos, mas estado compartilhado dificulta testes.

```python
def acima_de(limite: int):
    def predicado(valor: int) -> bool:
        return valor > limite
    return predicado
```

Closures preservam referências do escopo criador. Funções de alta ordem recebem ou retornam funções. Decorators envolvem uma função; `functools.wraps` preserva metadados.

Use decorators para políticas estáveis e visíveis, não para esconder I/O, retries ou transações inesperadas. Funções pequenas com dependências recebidas por parâmetro são mais simples de testar do que closures com estado mutável.
