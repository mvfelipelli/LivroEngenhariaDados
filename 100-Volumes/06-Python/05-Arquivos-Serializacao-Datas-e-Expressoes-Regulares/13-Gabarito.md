---
title: Gabarito — Arquivos, Serialização, Datas e Regex
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, serializacao]
aliases: [Gabarito Arquivos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

`Path("dados") / "entrada" / "pedidos.jsonl"`.

## 2

O default varia por ambiente; bytes iguais podem decodificar diferentemente ou falhar.

## 3

Compare `fieldnames` com a lista contratada e aplique `int` dentro de tratamento específico.

## 4

Use `enumerate(arquivo, 1)` e capture `JSONDecodeError` apenas ao redor de `json.loads`.

## 5

`datetime.fromisoformat(texto).astimezone(timezone.utc)` resulta em 12:00 UTC.

## 6

`re.compile(r"^BR-[1-9]\d{0,9}$").fullmatch(valor)`.

## 7

Escreva no mesmo diretório, flush, opcionalmente fsync e substitua com `Path.replace` após sucesso.

## 8

Separe parse e validação por linha, normalize UTC, ordene registros, escreva temporário e só então publique.
