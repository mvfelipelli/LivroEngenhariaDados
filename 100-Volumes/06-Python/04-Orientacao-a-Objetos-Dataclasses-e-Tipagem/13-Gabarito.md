---
title: Gabarito — Objetos e Tipagem Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, tipagem]
aliases: [Gabarito Objetos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Valide no método antes de alterar `_valor` e exponha `@property` somente de leitura.

## 2

O classmethod recebe `cls`, converte texto com Decimal e constrói centavos com regra explícita.

## 3

Receba ambos no `__init__`; o método valida e só então chama o destino.

## 4

Use `@dataclass(frozen=True, slots=True)` com `loja_id` e `produto_id` não vazios.

## 5

Teste `if valor is None` antes de operar como string.

## 6

Declare `T`, `class Repositorio(Protocol[T])` e métodos com `T` e `T | None`.

## 7

Anotação não inspeciona o payload em runtime; é necessário validar chaves, tipos e domínio e então construir o objeto.

## 8

Use dataclasses frozen, método que devolve `dataclasses.replace`, Protocol genérico e dict privado no adaptador em memória.
