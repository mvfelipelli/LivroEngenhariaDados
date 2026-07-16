---
title: Variáveis, Expansões, Arrays e Entrada
aliases: [Variáveis Bash, Expansões Bash]
tags: [linux, bash, variaveis, entrada]
created: 2026-07-16
updated: 2026-07-16
description: "Representação e validação de dados no Bash."
---

# Variáveis, Expansões, Arrays e Entrada

Bash armazena essencialmente strings. Uma variável local existe no shell; uma variável exportada compõe o ambiente recebido por processos filhos. Não inclua espaços ao redor de `=`.

## Quoting e expansão

```bash
arquivo='pedidos julho.csv'
printf '%s\n' "$arquivo"
printf 'ambiente=%s\n' "${AMBIENTE:-desenvolvimento}"
: "${TOKEN:?TOKEN é obrigatório}"
base=${arquivo%.csv}
```

Aspas simples preservam caracteres literalmente. Aspas duplas permitem expansões sem separação por espaços nem expansão de curingas. Uma expansão não citada passa por *word splitting* e *globbing*; quase sempre é um defeito.

| Forma | Efeito |
| --- | --- |
| `${x:-padrão}` | usa padrão se ausente ou vazio |
| `${x:=padrão}` | usa e atribui o padrão |
| `${x:?mensagem}` | interrompe se ausente ou vazio |
| `${x#prefixo}` | remove menor prefixo compatível |
| `${x%sufixo}` | remove menor sufixo compatível |

## Parâmetros e arrays

```bash
main() {
  local origem=${1:?informe a origem}
  shift
  local -a destinos=("$@")
  printf 'origem=%s destinos=%d\n' "$origem" "${#destinos[@]}"
  printf '%s\n' "${destinos[@]}"
}
main entrada.csv bronze prata
```

`$#` é a quantidade de parâmetros, `$@` preserva cada argumento quando escrito como `"$@"`, e `$*` os concatena. Arrays indexados são adequados a listas; arrays associativos (`declare -A`) representam mapas no Bash 4+.

## Entrada e opções

```bash
while getopts ':i:o:' opcao; do
  case $opcao in
    i) entrada=$OPTARG ;;
    o) saida=$OPTARG ;;
    *) exit 64 ;;
  esac
done

IFS=, read -r id status valor < linha.csv
```

`read -r` impede que barras invertidas sejam consumidas. Delimitadores simples não constituem um parser CSV completo: campos entre aspas, quebras de linha e vírgulas internas exigem biblioteca própria.

> [!warning]
> `resultado=$(comando)` remove quebras de linha finais e guarda toda a saída. Para streams grandes, use pipeline ou arquivo.

Continue em [[05-Condicionais-Lacos-Funcoes-e-Modularidade]].
