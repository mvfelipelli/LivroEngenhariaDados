---
title: Terminal, Comandos, Documentação e Pipes
aliases: [Linha de Comando Linux]
tags: [linux, terminal, comandos, pipes, documentacao]
created: 2026-07-16
updated: 2026-07-16
description: "Composição de comandos, fluxos e interpretação de resultados."
---

# Terminal, Comandos, Documentação e Pipes

O shell separa argumentos, expande variáveis e globs, aplica redirecionamentos e inicia processos. Cada comando retorna código: zero indica sucesso por convenção; outro valor indica condição diferente.

```bash
command --help
man command
type command
printf '%s\n' "$?"
```

## Fluxos

Descritor `0` é stdin, `1` stdout e `2` stderr. `>` substitui arquivo, `>>` acrescenta e `2>` redireciona erro. O pipe conecta stdout de um processo ao stdin do próximo.

```bash
cut -d, -f4 pedidos.csv | sort | uniq -c
grep -E 'ERROR|WARN' pipeline.log | tail -n 20
```

Com `set -o pipefail`, um pipeline pode refletir falha de qualquer etapa, não apenas da última. Use formatos delimitados com cuidado: CSV completo não é analisado corretamente por divisão ingênua quando há aspas e vírgulas internas.

> [!tip]
> Construa o pipeline em etapas, inspecione amostras e preserve stderr para diagnóstico.

Práticas defensivas aparecem em [[09-Seguranca-Ambientes-e-Boas-Praticas]].
