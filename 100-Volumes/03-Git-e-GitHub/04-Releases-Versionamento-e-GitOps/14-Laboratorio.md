---
title: Laboratório — Reconciliador GitOps Determinístico
description: "Validação local de versão, promoção, drift e reconciliação."
tags: [laboratorio, gitops, python]
aliases: [Laboratório Reconciliador GitOps]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Reconciliador GitOps Determinístico

## Objetivo

Validar uma release SemVer, promover o mesmo digest e reconciliar drift sem dependências externas.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- terminal local;
- apenas biblioteca padrão.

## Passos

1. Copie o código de [[14-Solucao|Solução]] para `reconcile.py`.
2. Execute:

```bash
python reconcile.py
```

3. Altere o digest desejado ou remova a assinatura e observe a falha de política.
4. Mude réplicas no estado atual e confirme a detecção de drift.

## Resultado esperado

```text
release=1.4.0
digest=verificado
promocao=imutavel
drift=2
reconciliacao=ok
estado=convergente
```

## Validação

O programa deve terminar com código zero e imprimir exatamente os seis invariantes. Uma assinatura ausente, versão inválida ou troca de digest durante a promoção deve interromper a execução.

## Conclusão

O exercício demonstra o núcleo de GitOps: uma intenção válida, comparação determinística e convergência idempotente.
