---
title: Laboratório — Pipeline Incremental Observável
description: "Projeto final CSV para SQLite com estado e quarentena."
tags: [python, laboratorio, pipelines, sqlite]
aliases: [Laboratório Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Pipeline Incremental Observável

## Objetivo

Construir um pipeline incremental de pedidos versionados com checkpoint, quarentena e métricas reconciliadas.

## Pré-requisitos

- Python 3.11 ou superior;
- todos os módulos anteriores do Volume 06;
- nenhuma dependência externa.

## Ambiente

Salve a solução como `pipeline_final.py`. Ela usa diretório temporário e SQLite local.

## Passos

1. Crie CSV append-only com cabeçalho e cinco eventos.
2. Inicialize tabelas de pedidos, quarentena e checkpoint.
3. Leia somente linhas posteriores ao checkpoint.
4. Valide ID, versão, status e centavos.
5. Aplique upsert somente para versão maior.
6. Registre rejeição e motivo.
7. Atualize checkpoint na mesma transação.
8. Emita evento JSON com métricas.
9. Execute duas vezes e compare o estado.

## Validação

Primeira execução: cinco lidos, quatro aceitos, um rejeitado. Estado final: três pedidos, total aprovado `4500` e checkpoint `6`. Segunda execução: zero lidos e estado idêntico.

## Conclusão

O laboratório reúne a linguagem, I/O, banco, testes, estado e observabilidade em um pipeline operável.
