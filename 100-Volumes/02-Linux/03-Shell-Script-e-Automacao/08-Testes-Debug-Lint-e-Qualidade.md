---
title: Testes, Debug, Lint e Qualidade
aliases: [Testes Bash, Qualidade Shell Script]
tags: [linux, bash, testes, qualidade]
created: 2026-07-16
updated: 2026-07-16
description: "Estratégia de verificação de automações shell."
---

# Testes, Debug, Lint e Qualidade

Um script é verificável quando entradas, efeitos e saídas podem ser controlados. Testes não substituem revisão operacional; eles tornam regressões reproduzíveis.

## Pirâmide prática

1. análise sintática com `bash -n script.sh`;
2. análise estática com ShellCheck;
3. testes unitários de funções puras;
4. integração em diretório temporário;
5. teste de reexecução, falha e recuperação;
6. ensaio no ambiente equivalente à produção.

```bash
assert_eq() {
  local esperado=$1 obtido=$2 mensagem=$3
  [[ $esperado == "$obtido" ]] || {
    printf 'falha=%s esperado=%q obtido=%q\n' \
      "$mensagem" "$esperado" "$obtido" >&2
    return 1
  }
}
```

Fixtures devem ser pequenas e representar casos válidos, limites, duplicatas e erros. Um teste *golden* compara uma saída completa conhecida; use-o quando o formato faz parte do contrato, não para esconder expectativas.

## Depuração

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]:-main}: '
BASH_XTRACEFD=9
exec 9>trace.log
set -x
```

`set -x` revela comandos após expansões e pode vazar tokens. Habilite-o somente em contexto controlado, redirecione a trilha e desative antes de manipular segredos. Para inspecionar estruturas, use `declare -p variavel`.

## Critérios de revisão

- todas as expansões que representam um argumento estão citadas;
- falhas esperadas são tratadas e status são significativos;
- temporários, locks e sinais possuem ciclo de vida;
- stdout contém dados; stderr, diagnóstico;
- entradas externas são validadas antes de compor comandos;
- o script é testado no Bash mínimo declarado;
- reexecução e concorrência fazem parte dos testes.

> [!tip]
> Formatação consistente reduz ruído na revisão. Ela não corrige semântica; combine formatador, ShellCheck e testes.

Próximo: [[09-Seguranca-Portabilidade-Agendamento-e-Operacao]].
