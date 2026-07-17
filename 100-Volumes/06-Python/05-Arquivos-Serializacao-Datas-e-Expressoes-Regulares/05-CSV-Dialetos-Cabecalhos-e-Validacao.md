---
title: CSV, Dialetos, Cabeçalhos e Validação
description: "Leitura tabular robusta com a biblioteca padrão."
tags: [python, csv, validacao]
aliases: [CSV em Python]
created: 2026-07-17
updated: 2026-07-17
---

# CSV, Dialetos, Cabeçalhos e Validação

CSV é uma família de dialetos: delimitador, aspas, escape, newline e encoding fazem parte do contrato.

```python
import csv

with open("pedidos.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    if leitor.fieldnames != ["pedido_id", "valor_centavos"]:
        raise ValueError("cabeçalho inesperado")
    for linha in leitor:
        pedido_id = linha["pedido_id"]
```

Todos os campos lidos são strings até conversão explícita. Cabeçalhos duplicados podem sobrescrever valores em `DictReader`; valide unicidade e conjunto esperado.

Ao escrever, fixe `fieldnames`, `extrasaction` e terminador de linha se consumidores compararem bytes. Fórmulas iniciadas por `=`, `+`, `-` ou `@` podem causar CSV injection ao abrir em planilhas; sanitize conforme o destino.
