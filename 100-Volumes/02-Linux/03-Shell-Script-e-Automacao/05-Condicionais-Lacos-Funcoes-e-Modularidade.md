---
title: Condicionais, Laços, Funções e Modularidade
aliases: [Controle de Fluxo Bash, Funções Bash]
tags: [linux, bash, funcoes]
created: 2026-07-16
updated: 2026-07-16
description: "Controle de fluxo e decomposição de scripts Bash."
---

# Condicionais, Laços, Funções e Modularidade

Controle de fluxo deve expressar decisões do domínio, não esconder falhas. Separe validação, transformação e efeitos externos em funções pequenas.

## Testes e decisões

```bash
if [[ -f $entrada && -r $entrada ]]; then
  processar "$entrada"
elif [[ -e $entrada ]]; then
  printf 'entrada sem leitura: %s\n' "$entrada" >&2
  exit 66
else
  exit 66
fi

case ${AMBIENTE:-} in
  dev|teste) nivel=DEBUG ;;
  prod) nivel=INFO ;;
  *) printf '%s\n' 'ambiente inválido' >&2; exit 64 ;;
esac
```

O comando condicional estendido do Bash evita várias armadilhas de divisão de palavras e oferece regex com `=~`. Use o comando aritmético do Bash para cálculos inteiros.

## Laços

```bash
for arquivo in "$diretorio"/*.json; do
  [[ -e $arquivo ]] || continue
  validar "$arquivo" || { quarentenar "$arquivo"; continue; }
  publicar "$arquivo"
done

while IFS= read -r linha; do
  consumir "$linha"
done < eventos.txt
```

Nunca use `for x in $(cat arquivo)`: espaços, curingas e quebras alteram registros.

## Funções como contratos

```bash
log() { printf '%s level=%s msg=%s\n' "$(date -u +%FT%TZ)" "$1" "$2" >&2; }

validar_id() {
  local id=${1:-}
  [[ $id =~ ^[a-z0-9-]+$ ]]
}
```

Uma função retorna status por `return`; dados podem sair por stdout. Não misture logs com dados no mesmo fluxo. Declare temporários com `local` e passe dependências por argumentos quando possível.

## Modularidade

Organize `bin/` para executáveis, `lib/` para funções e `test/` para fixtures e testes. Bibliotecas não devem chamar `exit`, alterar opções globais silenciosamente nem executar trabalho ao serem carregadas.

```bash
main() { validar_config; adquirir_lock; executar_pipeline; }
if [[ ${BASH_SOURCE[0]} == "$0" ]]; then main "$@"; fi
```

Esse guard permite carregar funções em testes. Avance para [[06-Erros-Sinais-Traps-e-Idempotencia]].
