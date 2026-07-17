---
title: Laboratório — Serviço Testado com Logging JSON
description: "Suíte unittest, fake e eventos estruturados."
tags: [python, laboratorio, unittest, logging]
aliases: [Laboratório Qualidade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Serviço Testado com Logging JSON

## Objetivo

Implementar e testar um serviço de publicação de lotes com repositório fake e logs JSON seguros.

## Pré-requisitos

- Python 3.11 ou superior;
- [[05-Arquivos-Serializacao-Datas-e-Expressoes-Regulares/README|Arquivos e Serialização]];
- nenhuma dependência externa.

## Ambiente

Salve a solução como `qualidade.py` e execute-a diretamente.

## Passos

1. Defina evento imutável e port de destino.
2. Valide ID e centavos não negativos.
3. Implemente fake em memória.
4. Emita JSON com campos permitidos.
5. Teste sucesso, entrada inválida, idempotência e ausência de segredo.
6. Execute a suíte duas vezes.

## Validação

Quatro testes devem passar; o serviço deve salvar dois IDs únicos, totalizar `2000` centavos e emitir evento `lote_concluido` sem o token fornecido.

## Conclusão

O laboratório conecta contrato de domínio, double, assertions e diagnóstico operacional seguro.
