---
title: Objetos, Identidade, Tipos e Mutabilidade
description: "Modelo de objetos e efeitos de aliasing."
tags: [python, objetos, mutabilidade]
aliases: [Mutabilidade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Objetos, Identidade, Tipos e Mutabilidade

Em Python, nomes referenciam objetos. Atribuição não copia o valor; apenas associa outro nome ao mesmo objeto.

```python
origem = ["site"]
canais = origem
canais.append("loja")
assert origem == ["site", "loja"]
assert canais is origem
```

`is` compara identidade; `==` compara igualdade de valor. Use `is None`, mas não `is` para comparar strings ou números.

Listas, dicionários e conjuntos são mutáveis. Inteiros, strings, bytes, tuplas e frozensets são imutáveis. Uma tupla pode, contudo, referenciar um objeto interno mutável.

```python
config = {"fontes": ["erp"]}
copia_rasa = config.copy()
copia_rasa["fontes"].append("crm")
assert config["fontes"] == ["erp", "crm"]
```

Para dados aninhados independentes, modele uma reconstrução explícita ou use cópia profunda com critério; copiar indiscriminadamente pode ser caro e mascarar ownership confuso.
