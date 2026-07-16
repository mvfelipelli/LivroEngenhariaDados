---
title: Gabarito — Shell Script e Automação
aliases: [Gabarito Bash]
tags: [linux, bash, gabarito]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas orientativas dos exercícios de shell script."
---

# Gabarito

1. O parser reconhece comando e palavras; `$HOME` é expandido dentro de aspas; `printf` recebe formato e um argumento sem divisão de palavras.
2. `"$@"` mantém argumentos; `"$*"` os une usando o primeiro caractere de `IFS`; `$@` sem aspas permite divisão e globbing.
3. O laço pode executar em subshell devido ao pipeline. Use `while ...; done < arquivo` ou outro mecanismo que mantenha o estado.
4. Idempotência preserva o resultado correto após repetição; atomicidade impede estados intermediários observáveis.
5. Há análise de `ls`, expansão não citada, comportamento ruim sem matches, nomes interpretados como opções e remoção sem validação. Use `find ... -print0`, leitura nula, aspas e `rm --` após checagens.
6. Ative `pipefail`, use `curl --fail-with-body`, temporário, valide JSON e publique por rename; preserve stderr e status.
7. Verifique usuário, `PATH`, diretório, shell, ambiente, permissões, arquivo de credenciais, locale e logs do agendador.
8. Exemplo: `case ${1:-} in dev|teste|prod) return 0;; *) return 64;; esac`.
9. Use `mktemp` no diretório do destino, trap de limpeza, `gerador >"$tmp"`, `test -s "$tmp"` e `mv -- "$tmp" "$destino"`.
10. Cubra lista vazia, um item, repetição adjacente e distante, caracteres válidos, ordem de saída e duas execuções.
11. Registre `timestamp`, `run_id`, etapa, status, duração e contagens; não registre payload, token ou identificador pessoal.
12. Classifique o status; para 429 respeite `Retry-After` ou backoff com jitter e limite. Para 400, falhe sem retentar.
13. Adquira `flock` antes da leitura; se ocupado, encerre com status documentado e métrica. Mantenha checksum para recuperação.
14. Preserve schema, códigos de saída, arquivos temporários, rename, estado, quarentena, logs e testes de contrato. Troque apenas o componente de parsing.
15. O hash de entrada deve mudar, os arquivos devem ser republicados uma vez e a terceira execução deve manter seus hashes.

> [!note]
> Soluções equivalentes são válidas quando explicitam seus contratos e preservam segurança, atomicidade e idempotência.
