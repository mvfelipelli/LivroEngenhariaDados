---
title: Laboratório — Domínio Imutável e Repositório Tipado
description: "Pedidos válidos, transições e port estrutural."
tags: [python, laboratorio, dataclasses]
aliases: [Laboratório Objetos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Domínio Imutável e Repositório Tipado

## Objetivo

Modelar pedidos válidos e persistência substituível sem acoplar o domínio ao armazenamento.

## Pré-requisitos

- Python 3.11 ou superior;
- [[03-Funcoes-Modulos-Excecoes-e-Iteradores/README|Funções, Módulos, Exceções e Iteradores]];
- nenhuma dependência externa.

## Ambiente

Salve a solução como `dominio.py` e execute no ambiente virtual.

## Passos

1. Crie `Dinheiro` e `Pedido` como dataclasses imutáveis.
2. Valide IDs, valor e status em runtime.
3. Implemente `cancelar()` sem mutar a instância.
4. Defina `Repositorio[T]` como Protocol.
5. Implemente repositório genérico em memória.
6. Salve, obtenha e atualize um pedido.
7. Confirme que o original continua aprovado.

## Validação

O programa deve confirmar `original=aprovado`, `atual=cancelado`, `total_centavos=4500`, `imutavel=ok` e `protocolo=ok`.

## Conclusão

O núcleo mantém invariantes e depende de comportamento, não de uma tecnologia de persistência.
