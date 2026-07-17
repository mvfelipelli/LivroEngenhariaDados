---
title: Gabarito
description: "Respostas dos exercícios de otimização SQL."
tags: [sql, gabarito, otimizacao]
aliases: [Gabarito de Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Cardinalidade é o número de linhas; seletividade é a fração preservada pelo predicado; custo compara o trabalho previsto. Cardinalidade e seletividade alimentam custos dos operadores.

## 2

O índice acrescentaria acessos à estrutura e possivelmente buscas aleatórias na tabela. Ler páginas sequencialmente uma vez tende a ser mais econômico para 90% das linhas.

## 3

```sql
WHERE criado_em >= TIMESTAMP '2026-07-17 00:00:00'
  AND criado_em <  TIMESTAMP '2026-07-18 00:00:00'
```

## 4

```sql
CREATE INDEX idx_vendas_loja_data
ON vendas (loja_id, criado_em DESC)
INCLUDE (valor);
```

`INCLUDE` depende do SGBD e é dispensável se `valor` não precisar de cobertura.

## 5

Estatísticas desatualizadas, distribuição enviesada/parâmetro atípico e correlação entre colunas não representada. Expressões sem estatísticas também são candidatas.

## 6

Sem entrada pequena e busca interna seletiva, nested loop pode repetir trabalho em escala. Hash join costuma favorecer igualdade entre conjuntos grandes, desde que a construção caiba em memória ou tenha particionamento aceitável.

## 7

O filtro ocorre tarde ou não possui caminho seletivo. Teste um índice compatível ou uma reescrita SARGable e compare resultado, plano, leituras e latência.

## 8

Obtenha baseline; estime espaço e impacto; use mecanismo online quando disponível; monitore bloqueios, CPU, I/O e replicação; valide consultas e escrita; libere gradualmente; mantenha o índice anterior até estabilizar; remova a nova estrutura se houver regressão.
