---
title: Condicionais, Match, Loops e Compreensões
description: "Controle explícito do fluxo de transformação."
tags: [python, condicionais, loops, comprehensions]
aliases: [Controle de Fluxo Python]
created: 2026-07-17
updated: 2026-07-17
---

# Condicionais, Match, Loops e Compreensões

`if`, `elif` e `else` expressam decisões. `match` realiza casamento estrutural quando forma e conteúdo determinam o tratamento.

```python
def classificar(evento: dict[str, object]) -> str:
    match evento:
        case {"tipo": "pedido", "valor": int(valor)} if valor >= 0:
            return "valido"
        case {"tipo": "pedido"}:
            return "pedido_invalido"
        case _:
            return "desconhecido"
```

`for` consome iteráveis; `while` repete enquanto uma condição for verdadeira. `break` encerra, `continue` avança e o `else` do loop executa quando não houve `break`.

Comprehensions são adequadas a transformações curtas:

```python
ativos = {cliente["id"] for cliente in clientes if cliente["ativo"]}
```

Quando validação, efeitos ou múltiplas ramificações entram na expressão, um loop nomeado comunica melhor a intenção.
