---
title: Laboratório — Auditoria de Baseline de Segurança
description: "Avaliação reproduzível de dez controles de um gateway."
tags: [linux, seguranca, laboratorio, python]
aliases: [Laboratório Hardening Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Laboratório — Auditoria de Baseline de Segurança

## Objetivo

Avaliar dez controles declarativos do gateway DataRetail S.A., gerar evidência e falhar quando houver desvio.

## Pré-requisitos

- Python 3.10 ou superior;
- somente biblioteca padrão;
- nenhum privilégio ou alteração no host.

## Ambiente

A fixture representa o estado coletado. Em produção, coletores somente leitura devem alimentar o mesmo modelo.

## Passos

1. Salve [[14-Solucao|a solução]] como `auditar_baseline.py`.
2. Execute `python auditar_baseline.py`.
3. Confirme dez aprovações.
4. Altere `permit_root_login` para `True` e confirme falha.
5. Restaure e execute novamente.

## Resultado esperado

```text
checks=10
aprovados=10
ssh=ok
privilegios=ok
filesystem=ok
auditoria=ok
baseline=conforme
hardening=ok
```

## Validação

As oito linhas devem se repetir e o status ser zero. Qualquer desvio deve encerrar com mensagem que identifica o controle.

## Conclusão

Compliance automatizada é mais útil quando cada resultado é explícito, testável e ligado a política contextual.
