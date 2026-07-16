---
title: Laboratório — Production Readiness Review
description: "Validação automatizada de dez gates operacionais."
tags: [linux, operacao, laboratorio, python]
aliases: [Laboratório Prontidão Operacional]
created: 2026-07-16
updated: 2026-07-16
---

# Laboratório — Production Readiness Review

## Objetivo

Avaliar dez gates da ingestão da DataRetail S.A. antes da liberação para produção.

## Pré-requisitos

- Python 3.10 ou superior;
- somente biblioteca padrão;
- nenhum privilégio ou acesso externo.

## Ambiente

Uma fixture representa evidências já coletadas. A política falha de modo determinístico quando um requisito não está pronto.

## Passos

1. Salve [[14-Solucao|a solução]] como `readiness_review.py`.
2. Execute `python readiness_review.py`.
3. Confirme dez gates aprovadas.
4. Altere `restore_tested` para falso e confirme reprovação.
5. Restaure e execute novamente.

## Resultado esperado

```text
gates=10
aprovadas=10
slo=definido
backup=restaurado
runbook=validado
rollback=pronto
producao=aprovada
operacao=ok
```

## Validação

As oito linhas devem se repetir e o status ser zero. Falhas devem nomear gates reprovadas.

## Conclusão

A review não elimina risco, mas torna lacunas explícitas e impede que operabilidade seja descoberta apenas durante incidentes.
