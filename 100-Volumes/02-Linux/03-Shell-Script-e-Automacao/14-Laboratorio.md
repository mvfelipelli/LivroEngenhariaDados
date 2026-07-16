---
title: Laboratório — Ingestão Idempotente com Bash
aliases: [Laboratório Shell Script]
tags: [linux, bash, laboratorio, automacao]
created: 2026-07-16
updated: 2026-07-16
description: "Ingestão reproduzível com validação, quarentena e publicação atômica."
---

# Laboratório — Ingestão Idempotente com Bash

## Objetivo

Construir para a DataRetail S.A. uma automação que valide quatro pedidos, deduplique identificadores, separe erros e prove que a segunda execução não altera o resultado.

## Pré-requisitos

- Bash 4 ou superior;
- `awk`, `sha256sum`, `mktemp` e `mv`;
- diretório descartável, Linux ou Git Bash.

## Ambiente

O script cria todo o workspace com `mktemp -d` e o remove ao terminar. Não exige privilégios. O CSV é deliberadamente simplificado: três campos separados por vírgula, sem aspas ou vírgulas internas.

## Passos

1. Crie `automacao_pedidos.sh` a partir de [[14-Solucao|Solução]].
2. Valide a sintaxe com `bash -n automacao_pedidos.sh`.
3. Execute `bash automacao_pedidos.sh`.
4. Confirme duas aprovações, duas quarentenas e os motivos `status_invalido` e `pedido_duplicado`.
5. Confirme que os hashes de aprovados, quarentena e estado permanecem iguais após a segunda chamada.
6. Execute todo o script novamente para testar independência entre execuções.

## Resultado esperado

```text
linhas=4
aprovadas=2
quarentena=2
duplicadas=1
invalidas=1
estado=publicado
segunda_execucao=sem_alteracoes
automacao=ok
```

## Validação

O laboratório é aprovado quando a saída coincide, o status é zero e duas execuções completas apresentam o mesmo resultado. Altere uma entrada para verificar que um novo checksum provoca nova publicação.

## Conclusão

A solução demonstra que automação confiável combina contrato de entrada, validação, estado, temporários, publicação atômica e teste de reexecução.

> [!warning]
> Em produção, acrescente lock entre processos, retenção de evidências e um parser compatível com o formato real.
