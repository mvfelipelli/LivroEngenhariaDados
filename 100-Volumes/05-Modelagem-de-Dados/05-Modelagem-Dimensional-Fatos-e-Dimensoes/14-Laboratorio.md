---
title: Laboratório — Star Schema de Vendas
description: "Implementação e validação de grão dimensional no SQLite."
tags: [modelagem-de-dados, sqlite, laboratorio, dimensional]
aliases: [Laboratório Star Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Star Schema de Vendas

## Objetivo

Implementar dimensões Data, Produto e Loja, uma fato no grão de item vendido e validar agregações sem fanout.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie três dimensões com chaves substitutas.
2. Crie fato com chave única do grão.
3. Insira quatro itens de três pedidos.
4. Agregue receita por categoria e loja.
5. Valide total geral contra a soma das agregações.
6. Tente repetir o mesmo item.
7. Confirme rejeição da duplicidade.

## Validação esperada

```text
datas=2
produtos=2
lojas=2
itens_fato=4
quantidade=7
receita_centavos=7500
grao_duplicado=rejeitado
estrela=ok
```

Consulte [[14-Solucao|Solução]].
