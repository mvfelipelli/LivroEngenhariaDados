---
title: Texto, Arquivos, Processos e Paralelismo
aliases: [Processamento de Texto no Bash, Paralelismo Bash]
tags: [linux, bash, texto, processos]
created: 2026-07-16
updated: 2026-07-16
description: "Composição segura de utilitários, arquivos e processos."
---

# Texto, Arquivos, Processos e Paralelismo

Pipelines Unix funcionam bem quando cada etapa possui um contrato textual simples. `grep` seleciona, `sed` transforma linhas, `awk` processa campos, `sort` ordena e `uniq` agrega adjacências. Antes da ferramenta, defina encoding, delimitador, cabeçalho e política para registros inválidos.

```bash
awk -F, 'NR > 1 && $2 == "confirmado" { soma += $3; n++ }
           END { printf "pedidos=%d valor=%.2f\n", n, soma }' pedidos.csv
```

Esse exemplo serve apenas para CSV simplificado, sem vírgulas ou quebras dentro de campos citados.

## Nomes de arquivo são dados

Não analise a saída de `ls`. Nomes podem conter espaços, curingas e quebras de linha. Use APIs delimitadas por byte nulo:

```bash
find entrada -type f -name '*.json' -print0 |
  while IFS= read -r -d '' arquivo; do
    processar "$arquivo"
  done
```

Com `xargs`, combine `find -print0` e `xargs -0`. Termine opções com `--` quando a ferramenta suporta, evitando que um nome iniciado por hífen seja interpretado como flag.

## Processos em segundo plano

```bash
pids=()
for particao in "${particoes[@]}"; do
  processar "$particao" &
  pids+=("$!")
done

falhas=0
for pid in "${pids[@]}"; do
  wait "$pid" || ((falhas++))
done
(( falhas == 0 ))
```

`&` inicia trabalho concorrente, `$!` identifica o processo e `wait` recolhe seu status. Limite a concorrência conforme CPU, memória, I/O e capacidade do serviço remoto. Paralelizar escrita no mesmo arquivo produz corrida; use saídas por partição e consolidação posterior.

> [!warning]
> Variáveis alteradas dentro de um pipeline podem estar em subshell e desaparecer. Prefira redirecionar o laço (`done < arquivo`) quando o estado precisa permanecer.

Continue em [[08-Testes-Debug-Lint-e-Qualidade]].
