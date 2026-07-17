---
title: Gabarito
description: "Respostas dos exercícios de modelagem ER."
tags: [modelagem-de-dados, gabarito, er]
aliases: [Gabarito Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Hotel e hóspede possuem identidade independente; quarto pode depender do hotel se o número só for único nele; reserva possui identidade e relaciona hotel/quarto/hóspede.

## 2

Endereço é composto; idade é derivada; telefones são multivalorados; saldo é derivado de lançamentos, salvo contrato de snapshot.

## 3

Relacionamento recursivo com papéis supervisor e subordinado, normalmente `0..1` supervisor e `0..N` subordinados.

## 4

Curso possui turmas; turma pertence a um curso; aluno participa de turmas por matrícula associativa, com situação e data.

## 5

`OFERTA` é associativa entre fornecedor e produto e contém preço, prazo e validade.

## 6

Quando a autorização de um fornecedor para uma peça depende de um projeto específico; pares isolados admitem combinações inexistentes.

## 7

Pagamento como supertipo; subtipos disjuntos com dados exclusivos. A especialização pode ser total se todo pagamento usa um desses meios.

## 8

Separe Assinatura, Plano, PeríodoAssinatura, Pausa e Cobrança; valide intervalos, uma versão ativa e relação entre cobrança e período praticado.
