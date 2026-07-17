---
title: Funções, Assinaturas, Parâmetros e Retornos
description: "Contratos de chamada e desenho de funções."
tags: [python, funcoes, parametros]
aliases: [Assinaturas Python]
created: 2026-07-17
updated: 2026-07-17
---

# Funções, Assinaturas, Parâmetros e Retornos

Funções são objetos. Sua assinatura deve tornar obrigatório o que é essencial e nomeável o que exige clareza.

```python
def calcular_total(valores: list[int], /, *, incluir_zeros: bool = True) -> int:
    selecionados = valores if incluir_zeros else [v for v in valores if v]
    return sum(selecionados)
```

Antes de `/`, argumentos são posicionais; após `*`, somente nomeados. `*args` e `**kwargs` ajudam em adaptadores, mas podem esconder contratos.

Defaults são avaliados uma vez. Evite coleções mutáveis:

```python
def registrar(item: str, itens: list[str] | None = None) -> list[str]:
    resultado = [] if itens is None else itens
    resultado.append(item)
    return resultado
```

Prefira uma forma de sucesso estável. Retornar `None`, `False` ou lista conforme o caminho transfere ambiguidade ao chamador.
