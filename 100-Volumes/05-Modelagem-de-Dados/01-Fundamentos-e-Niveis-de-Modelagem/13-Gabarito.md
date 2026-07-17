---
title: Gabarito
description: "Respostas dos exercícios de fundamentos de modelagem."
tags: [modelagem-de-dados, gabarito]
aliases: [Gabarito Fundamentos de Modelagem]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Exemplo: soma em centavos dos itens de pedidos pagos, no grão diário por loja, reconhecida no instante do pagamento, líquida de cancelamentos e na moeda da transação.

## 2

Livro/obra, exemplar, pessoa e empréstimo; retirada, devolução, reserva e multa são eventos candidatos.

## 3

ISBN identifica edição, não exemplar. Exemplar precisa identidade própria. Chave substituta pode implementar essa identidade sem substituir a regra do tombo patrimonial.

## 4

“Pedido contém itens” é conceitual; relações e chaves são lógicas; `BIGINT`, índice e partição são físicos.

## 5

Cliente 1:N Pedido; Pedido 1:N Item; Produto 1:N Item. Um cliente pode ter zero pedidos; pedido confirmado deve ter ao menos um item.

## 6

Identidade única, valor positivo, moeda válida, pedido existente e transição de status permitida.

## 7

O endereço praticado deve ser snapshot no pedido; alterações cadastrais posteriores não podem mudar a entrega histórica.

## 8

Reúna owners, liste identificadores e conflitos, use exemplos reais, defina regras de matching, golden record, consentimento, exceções e critérios de validação.
