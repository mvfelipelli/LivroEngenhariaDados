---
title: Laboratório — CLI de Inspeção de Pedidos
description: "Construção de um ambiente isolado e uma CLI verificável."
tags: [python, laboratorio, cli]
aliases: [Laboratório Fundamentos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — CLI de Inspeção de Pedidos

## Objetivo

Construir uma CLI que valide um CSV de pedidos, conte registros e totalize valores em centavos.

## Pré-requisitos

- Python 3.11 ou superior;
- terminal com permissão de escrita;
- nenhuma dependência externa.

## Ambiente

Crie e ative `.venv`, depois confirme `sys.executable`. Salve a solução como `inspecionar.py`.

## Passos

1. Crie `pedidos.csv` com cabeçalho `pedido_id,valor_centavos` e três registros válidos.
2. Implemente argumentos `--entrada` e `--limite`.
3. Valide existência, cabeçalho, identificador não vazio e valor inteiro não negativo.
4. Produza `registros=N` e `total_centavos=T`.
5. Retorne código não zero para entrada inválida.
6. Execute o arquivo válido duas vezes e compare as saídas.

## Validação

```bash
python inspecionar.py --entrada pedidos.csv --limite 10
python inspecionar.py --entrada ausente.csv
```

A primeira execução deve retornar `0`; a segunda, código `2`. Execuções repetidas não alteram a entrada e produzem o mesmo resumo.

## Conclusão

O laboratório transforma ambiente, CLI, validação, saída e código de retorno em um contrato operacional mínimo.
