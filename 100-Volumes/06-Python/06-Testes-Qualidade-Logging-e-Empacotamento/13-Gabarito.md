---
title: Gabarito — Qualidade Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, qualidade]
aliases: [Gabarito Qualidade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Unitário para função; integração contra banco real; end-to-end para o fluxo completo e seus contratos.

## 2

Use `subTest` com pares de entrada e resultado ou parametrização equivalente no framework adotado.

## 3

Dict em memória implementa o port e torna testes rápidos, mas não verifica SQL, transação ou tipos do driver.

## 4

Para várias amostras, verifique `normalizar(normalizar(x)) == normalizar(x)`.

## 5

Teste chama função e não verifica retorno; a linha conta como coberta mesmo se o resultado estiver errado.

## 6

Timestamp, nível, evento, run_id, lote_id, registros, rejeitados e duração; nunca token ou payload completo.

## 7

Construa, crie novo venv, instale somente wheel, execute import, entry point e smoke test.

## 8

Separe validação e coordenação, injete destino, capture logs e afirme evento, contagem e ausência de segredo.
