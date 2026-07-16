---
title: Modelo de Execução e Sintaxe do Shell
aliases: [Execução Bash, Sintaxe Bash]
tags: [linux, bash, shell]
created: 2026-07-16
updated: 2026-07-16
description: "Parsing, expansões, pipelines, subshells e códigos de saída."
---

# Modelo de Execução e Sintaxe do Shell

O shell primeiro reconhece operadores e palavras, realiza expansões e redirecionamentos e só então executa builtins, funções ou programas. Entender essa ordem evita tratar uma linha Bash como se fosse apenas texto.

## Programa executável

```bash
#!/usr/bin/env bash
printf 'shell=%s\n' "$BASH_VERSION"
exit 0
```

O *shebang* seleciona o interpretador quando o arquivo é executado. `bash script.sh` ignora o shebang e usa o Bash chamado. Permissão de execução e um shebang válido são contratos diferentes.

## Status e composição

Todo comando retorna um inteiro entre 0 e 255; zero representa sucesso por convenção. `$?` contém o status mais recente, mas deve ser capturado imediatamente.

```bash
if grep -q '^READY$' status.txt; then
  printf '%s\n' 'pronto'
else
  rc=$?
  printf 'não pronto: rc=%d\n' "$rc" >&2
fi

mkdir -p saida && printf '%s\n' ok >saida/status
test -s saida/status || exit 1
```

`&&` executa à direita após sucesso; `||`, após falha; `;` não condiciona. Em `a | b`, processos são conectados e, sem `pipefail`, o status costuma ser o de `b`.

## Ambiente, agrupamento e carregamento

```bash
export AMBIENTE=teste
( cd /tmp && printf 'subshell=%s\n' "$PWD" )
{ printf '%s\n' linha1; printf '%s\n' linha2; } >relatorio.txt
source ./lib/log.sh
```

Parênteses criam subshell: mudanças de diretório ou variável não retornam ao processo pai. Chaves agrupam no shell atual e exigem espaços e `;` antes de `}`. `source` executa no contexto atual; carregue somente código confiável.

## Redirecionamentos

`>` substitui, `>>` acrescenta, `<` fornece entrada e `2>` redireciona erro. A ordem importa: `cmd >arquivo 2>&1` reúne ambos no arquivo; `cmd 2>&1 >arquivo` deixa o erro apontando para o destino anterior.

> [!tip]
> Use `printf` em automações: seu formato é previsível e não depende das variações de `echo`.

Próximo: [[04-Variaveis-Expansoes-Arrays-e-Entrada]].
