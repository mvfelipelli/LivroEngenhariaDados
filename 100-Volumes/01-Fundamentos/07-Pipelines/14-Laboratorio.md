---
title: Laboratório — Executor de DAG Idempotente
aliases: [Laboratório de Pipelines]
tags: [pipelines, laboratorio, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Construção de um pipeline com DAG, auditoria, quarentena e carga idempotente."
---

# Laboratório — Executor de DAG Idempotente

## Objetivo

Implementar um executor simples de DAG para o pipeline de pedidos da DataRetail S.A., registrando runs, isolando registros inválidos e demonstrando que a segunda execução não duplica pedidos.

## Pré-requisitos

- Python 3.10 ou superior;
- apenas módulos da biblioteca padrão;
- conhecimento básico de Python e SQL.

## Ambiente

Crie uma pasta vazia, salve a solução como `pipeline.py` e execute-a em um terminal. O programa criará um banco SQLite temporário no diretório do sistema.

## Etapas

1. Modele as tarefas `extract`, `validate`, `transform`, `load` e `reconcile`.
2. Declare as dependências como um DAG.
3. Calcule uma ordem topológica e rejeite ciclos.
4. Registre início e conclusão de cada tarefa por `run_id`.
5. Envie registros inválidos para quarentena.
6. Selecione a versão mais recente de cada pedido.
7. Faça upsert por `pedido_id` em uma transação.
8. Execute o pipeline duas vezes sobre a mesma entrada.
9. Valide contagem, valor reconciliado e ausência de duplicação.

```mermaid
flowchart LR
    A[extract] --> B[validate]
    B --> C[transform]
    C --> D[load]
    D --> E[reconcile]
```

## Critérios de validação

A saída deve conter:

```text
ordem=extract>validate>transform>load>reconcile
extraidos=4
validos=2
rejeitados=1
pedidos=2
total_confirmado=150.00
tarefas_auditadas=10
segunda_execucao=sem_duplicacao
pipeline=ok
```

## Conclusão

O laboratório demonstra que a topologia coordena o fluxo, enquanto idempotência, transação, quarentena, auditoria e reconciliação determinam sua confiabilidade.

Compare sua implementação com [[14-Solucao]].
