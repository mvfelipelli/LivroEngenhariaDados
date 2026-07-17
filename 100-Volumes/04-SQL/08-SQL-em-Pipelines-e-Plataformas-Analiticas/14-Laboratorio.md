---
title: Laboratório — Carga Incremental Idempotente
description: "Pipeline SQLite com staging, versão, upsert e watermark."
tags: [sql, sqlite, laboratorio, incremental]
aliases: [Laboratório de Pipeline SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Carga Incremental Idempotente

## Objetivo

Processar dois lotes, aplicar correção mais recente, ignorar versão antiga e comprovar que repetir o segundo lote não altera o destino.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie origem, staging, fato e tabela de controle.
2. Insira o lote inicial com três pedidos.
3. Carregue staging após o watermark e faça upsert por versão.
4. Adicione uma correção, um pedido novo e uma versão antiga atrasada.
5. Execute novamente com sobreposição.
6. Repita o mesmo processamento.
7. Compare snapshot, contagem, soma e watermark.

## Validação esperada

```text
pedidos=4
total_centavos=4250
correcao=aplicada
versao_antiga=ignorada
reexecucao=idempotente
watermark=6
pipeline=ok
```

> [!note]
> O número sequencial representa o cursor de ingestão. A versão de negócio decide qual estado vence por pedido.

Consulte [[14-Solucao|Solução]].
