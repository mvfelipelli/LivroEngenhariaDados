---
title: Perguntas de Entrevista — Shell Script e Automação
aliases: [Entrevista Bash]
tags: [linux, bash, entrevista]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas progressivas com respostas fundamentadas."
---

# Perguntas de Entrevista

## Fundamentos

### 1. Por que escrever `"$@"`?

Porque preserva cada parâmetro como um argumento separado, inclusive valores vazios ou com espaços. `$*` ou `$@` sem aspas podem alterar a fronteira dos argumentos.

### 2. Qual é a diferença entre variável e variável de ambiente?

Uma variável pertence ao shell atual. Após `export`, seu nome e valor são incluídos no ambiente de processos filhos; alterações no filho não retornam ao pai.

### 3. O que `pipefail` muda?

Sem ele, o status de um pipeline normalmente é o do último comando. Com ele, uma falha anterior pode tornar o pipeline malsucedido, evitando sucesso falso.

## Intermediário

### 4. `set -e` basta para tratamento de erros?

Não. Seu comportamento depende do contexto sintático e não faz rollback. Falhas esperadas devem ser tratadas e efeitos precisam de desenho transacional.

### 5. Como publicar um arquivo sem expor conteúdo parcial?

Gere um temporário no mesmo filesystem, valide, sincronize quando necessário e renomeie com `mv`. O rename é atômico no mesmo filesystem sob condições usuais.

### 6. Como processar nomes de arquivo arbitrários?

Use interfaces com byte nulo, como `find -print0`, `read -d ''` e `xargs -0`; cite expansões e evite analisar `ls`.

### 7. Qual é o papel de um trap `EXIT`?

Centralizar limpeza ou finalização independentemente do caminho de saída. Ele deve ser simples, tolerar estado parcial e preservar o status relevante.

## Avançado

### 8. Como projetar retentativas?

Somente para falhas transitórias e operações idempotentes, com timeout, limite, backoff, jitter quando aplicável e métricas por tentativa.

### 9. Como evitar duas execuções simultâneas?

Adquira lock atomicamente, por exemplo com `flock`; defina comportamento para disputa e recuperação de lock órfão. O lock complementa, mas não substitui idempotência.

### 10. Quando Bash deixou de ser a escolha adequada?

Quando parsing, estruturas complexas, concorrência, bibliotecas ou regras de domínio passam a dominar a orquestração. A migração deve preservar os contratos operacionais.

### 11. Como depuraria um script que funciona no terminal e falha no cron?

Compararia usuário, `PATH`, diretório, shell, locale, variáveis, permissões, limites e stdin; executaria com ambiente mínimo e consultaria stdout, stderr e status.

### 12. Como impedir injeção de comandos?

Não use `eval`; valide dados; represente comando e argumentos em array; cite expansões; separe dados de código e aplique menor privilégio.
