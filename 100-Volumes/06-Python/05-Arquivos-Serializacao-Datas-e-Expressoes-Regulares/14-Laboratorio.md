---
title: Laboratório — JSONL para CSV Atômico
description: "Normalização temporal, rejeições e publicação segura."
tags: [python, laboratorio, jsonl, csv]
aliases: [Laboratório Serialização Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — JSONL para CSV Atômico

## Objetivo

Converter eventos JSONL em CSV ordenado, normalizando timestamps e isolando rejeições.

## Pré-requisitos

- Python 3.11 ou superior;
- [[04-Orientacao-a-Objetos-Dataclasses-e-Tipagem/README|Objetos, Dataclasses e Tipagem]];
- nenhuma dependência externa.

## Ambiente

Salve a solução como `converter.py`; ela cria os arquivos dentro de diretório temporário.

## Passos

1. Leia JSONL em UTF-8.
2. Valide ID `BR-N`, timestamp aware e centavos não negativos.
3. Converta o instante para UTC com sufixo `Z`.
4. Rejeite linha inválida com número e motivo.
5. Ordene por timestamp e ID.
6. Escreva CSV temporário e substitua o destino.
7. Execute duas vezes e compare bytes.

## Validação

Devem existir três registros, uma rejeição, total de `4500` centavos, timestamps UTC, bytes idênticos e ausência do temporário.

## Conclusão

O laboratório integra formato, validação, tempo e atomicidade em uma fronteira reproduzível.
