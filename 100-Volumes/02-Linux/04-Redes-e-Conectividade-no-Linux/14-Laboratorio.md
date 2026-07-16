---
title: Laboratório — Diagnóstico de Serviço em Loopback
description: "Teste reproduzível de DNS, TCP e HTTP sem acesso externo."
tags: [linux, redes, laboratorio, python]
aliases: [Laboratório Redes Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Laboratório — Diagnóstico de Serviço em Loopback

## Objetivo

Subir um serviço efêmero em `127.0.0.1`, resolver `localhost`, abrir um socket TCP, executar HTTP e validar as camadas de modo determinístico.

## Pré-requisitos

- Python 3.10 ou superior;
- permissão para abrir uma porta efêmera em loopback;
- Linux, macOS ou Windows para a parte reproduzível; comandos Linux para inspeção complementar.

## Ambiente

O programa usa apenas a biblioteca padrão, escolhe uma porta livre e encerra servidor e thread ao final. Não acessa internet nem grava arquivos.

## Passos

1. Salve o código de [[14-Solucao|Solução]] como `diagnostico_rede.py`.
2. Execute `python diagnostico_rede.py`.
3. Confirme resolução para loopback, conexão TCP e resposta HTTP 200.
4. Execute novamente e compare a saída.
5. Em Linux, enquanto adapta o servidor para aguardar, observe-o com `ss -lntp`.

## Resultado esperado

```text
nome=localhost
familia=IPv4
endereco=127.0.0.1
tcp=conectado
http_status=200
corpo=DataRetail OK
camadas=ok
```

## Validação

A execução deve terminar com status zero e repetir exatamente as sete linhas. A porta não aparece na saída porque é efêmera e não integra o contrato.

## Conclusão

O laboratório separa descoberta, transporte e aplicação. Em produção, repita o método a partir da origem real e inclua rota, firewall, TLS e métricas.
