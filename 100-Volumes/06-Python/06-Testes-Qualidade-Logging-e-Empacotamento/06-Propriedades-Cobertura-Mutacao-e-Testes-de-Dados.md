---
title: Propriedades, Cobertura, Mutação e Testes de Dados
description: "Invariantes, efetividade e qualidade dos conjuntos."
tags: [python, propriedades, cobertura, dados]
aliases: [Testes de Propriedade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Propriedades, Cobertura, Mutação e Testes de Dados

Testes baseados em exemplos verificam casos escolhidos. Testes de propriedade geram muitos valores para desafiar invariantes, como idempotência, conservação e monotonicidade.

```python
def normalizar(ids: list[str]) -> list[str]:
    return sorted(set(ids))

amostras = [[], ["B", "A", "B"], ["A"]]
for entrada in amostras:
    assert normalizar(normalizar(entrada)) == normalizar(entrada)
```

Cobertura informa linhas ou ramos executados, não se as assertions são úteis. Mutação altera operadores e constantes para verificar se a suíte detecta o defeito.

Pipelines também testam dados: schema, unicidade, não nulidade, domínio, reconciliação e frescor. Fixtures devem incluir limites, duplicatas, Unicode, timestamps e registros tardios, sem copiar dados pessoais reais.
