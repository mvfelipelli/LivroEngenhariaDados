---
title: Laboratório — Gate de Qualidade SQL
description: "Validação reproduzível de unicidade, integridade e reconciliação."
tags: [sql, sqlite, laboratorio, qualidade]
aliases: [Laboratório Qualidade SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Gate de Qualidade SQL

## Objetivo

Construir um gate que rejeita staging inválido, corrige o lote e comprova publicação reconciliada e idempotente.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie clientes, staging e fato.
2. Carregue duplicata e referência inexistente.
3. Execute testes que retornam violações.
4. Confirme bloqueio da publicação.
5. corrija o staging e publique com upsert.
6. Reconcilie contagem e soma.
7. Reexecute e confirme estado idêntico.

## Validação esperada

```text
gate_inicial=bloqueado
duplicidades_detectadas=1
referencias_invalidas=1
gate_final=aprovado
pedidos=3
receita_centavos=6000
reexecucao=idempotente
qualidade=ok
```

Consulte [[14-Solucao|Solução]].
