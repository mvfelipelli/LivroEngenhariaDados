---
title: Resumo — Arquivos, Serialização, Datas e Regex
description: "Síntese das fronteiras persistentes."
tags: [python, resumo, arquivos]
aliases: [Resumo Arquivos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Pathlib modela caminhos portavelmente.
- Arquivos texto exigem encoding e newline explícitos.
- CSV depende de dialeto e cabeçalho contratados.
- JSON não representa datetime, bytes ou Decimal diretamente.
- JSONL favorece processamento incremental e quarentena por linha.
- Datetime aware representa instante; timezone não é mero offset.
- UTC é uma forma adequada de intercâmbio, não substitui contexto civil.
- Regex deve ser ancorada, limitada e usada para a gramática certa.
- Compactação troca CPU por I/O e armazenamento.
- Escrita temporária e replace no mesmo filesystem evitam publicação parcial.

O próximo módulo institui testes, qualidade, logging e empacotamento profissional.
