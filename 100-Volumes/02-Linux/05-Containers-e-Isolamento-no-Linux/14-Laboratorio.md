---
title: Laboratório — Imagem em Camadas Determinística
description: "Construção didática de camadas, whiteout e manifesto por digest."
tags: [linux, containers, laboratorio, python]
aliases: [Laboratório Imagem OCI]
created: 2026-07-16
updated: 2026-07-16
---

# Laboratório — Imagem em Camadas Determinística

## Objetivo

Construir em memória duas camadas determinísticas, aplicar um whiteout, proteger contra caminhos inseguros e gerar um manifesto identificado por digest.

## Pré-requisitos

- Python 3.10 ou superior;
- somente biblioteca padrão;
- nenhum daemon, privilégio ou acesso à internet.

## Ambiente

O programa não extrai arquivos no disco. O root filesystem é representado por um dicionário e cada camada por um tar USTAR em memória.

## Passos

1. Salve [[14-Solucao|a solução]] como `imagem_didatica.py`.
2. Execute `python imagem_didatica.py`.
3. Confirme duas camadas, dois arquivos finais e um whiteout.
4. Execute novamente e compare o digest.
5. Adicione um caminho `../segredo` e confirme que a validação o rejeita.

## Resultado esperado

```text
camadas=2
arquivos=2
whiteouts=1
rootfs=app/config.ini,app/version.txt
digest_repetivel=sim
imagem=ok
```

## Validação

As seis linhas devem ser idênticas nas duas execuções e o processo deve retornar zero.

## Conclusão

O exercício demonstra endereçamento por conteúdo, aplicação ordenada de camadas, remoção lógica e importância de metadata reproduzível.
