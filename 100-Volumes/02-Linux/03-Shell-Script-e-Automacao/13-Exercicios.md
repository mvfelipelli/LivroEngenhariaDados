---
title: Exercícios — Shell Script e Automação
aliases: [Exercícios Bash]
tags: [linux, bash, exercicios]
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre automação shell confiável."
---

# Exercícios

## Revisão conceitual

1. Explique parsing, expansão e execução de `printf '%s\n' "$HOME"`.
2. Compare `"$@"`, `"$*"` e `$@`.
3. Explique por que `cat arquivo | while read linha; do total=$((total+1)); done` pode não alterar `total` no shell atual.
4. Diferencie idempotência de atomicidade.

## Interpretação

5. Identifique os defeitos:

```bash
for f in $(ls $DIR/*.csv); do
  rm $f
done
```

6. Uma rotina `curl ... | jq ... > destino.json` retorna zero mesmo com falha do `curl`. Diagnostique e proponha controles.
7. Um script chamado pelo cron não encontra `psql`. Liste cinco verificações.

## Aplicação

8. Escreva `validar_ambiente` que aceite somente `dev`, `teste` ou `prod`.
9. Escreva uma função que crie temporário, execute uma geração recebida como função e publique com `mv` somente se a saída não estiver vazia.
10. Projete testes para uma função que deduplica identificadores.
11. Modele logs para início, fim, falha e contagens sem registrar dados pessoais.

## Desafios

12. Desenhe retentativa para uma API sujeita a HTTP 429, sem repetir erros 400.
13. Adicione um lock ao desenho da ingestão da DataRetail S.A. e defina a resposta quando outra execução estiver ativa.
14. Explique como migraria o parser do [[10-Estudo-de-Caso-DataRetail|estudo de caso]] para Python sem perder suas garantias.
15. Execute [[14-Laboratorio]], altere uma linha da entrada e prove que uma nova publicação ocorre exatamente uma vez.

As respostas orientativas estão em [[13-Gabarito]].
