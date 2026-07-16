---
title: Exercícios — Bancos de Dados
aliases: [Exercícios de Bancos de Dados]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, exercicios]
type: exercises
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre fundamentos, transações, concorrência e desempenho em Bancos de Dados."
---

# 13 — Exercícios

> [!abstract]
> Resolva as atividades antes de consultar o [[13-Gabarito]]. Nas questões de arquitetura, explicite requisitos e trade-offs.

## Parte I — Revisão conceitual

1. Diferencie Banco de Dados, SGBD, schema e instância.
2. Explique independência lógica e independência física de dados.
3. Compare os modelos relacional, documentos, chave-valor, colunar e grafos.
4. Explique as funções de páginas, buffer pool e Write-Ahead Log (WAL).
5. Defina atomicidade, consistência, isolamento e durabilidade.

## Parte II — Interpretação

### 6. Modelo adequado

Indique um modelo inicial e justifique para: cadastro financeiro com relações fortes; sessão temporária; catálogo heterogêneo; rede de fraude; métricas por dispositivo e tempo.

### 7. Restrições

Uma tabela de pedidos aceita cliente inexistente, total negativo e status arbitrário. Proponha chaves e restrições que protejam o domínio.

### 8. Falha durante commit

Descreva como WAL e recuperação permitem tratar uma queda após o registro do commit, mas antes da gravação de todas as páginas de dados.

### 9. Anomalias

Classifique: uma linha muda entre duas leituras; novas linhas passam a satisfazer o mesmo predicado; duas transações leem saldo suficiente e ambas gastam; uma transação lê alteração ainda não confirmada.

### 10. Índices

Para consultas frequentes por `customer_id` e intervalo de `created_at`, proponha um índice. Explique a ordem das colunas e o custo sobre escritas.

## Parte III — Aplicação

### 11. Transação de pedido

Escreva SQL para criar um pedido e baixar estoque atomicamente. A atualização do estoque deve falhar quando a quantidade disponível for insuficiente.

### 12. Concorrência

Duas compras disputam a última unidade. Compare atualização condicional, bloqueio pessimista e controle otimista.

### 13. Plano de consulta

Uma consulta filtra uma tabela grande por coluna sem índice. Descreva como investigar com `EXPLAIN`, estatísticas e métricas de I/O.

### 14. Recuperação

Defina RPO e RTO para pedidos da DataRetail S.A. e proponha backup, restauração e testes. Explique por que réplica não substitui backup.

### 15. Persistência poliglota

Distribua pedidos, catálogo, sessões, eventos e relatórios entre categorias de Banco de Dados. Justifique também o custo operacional da decisão.

## Parte IV — Desafios

### 16. Deadlock

Duas transações atualizam os pedidos A e B em ordens inversas. Explique o ciclo de espera, a reação do SGBD e duas medidas preventivas.

### 17. Isolamento

Escolha um nível de isolamento para fechamento financeiro e outro para consulta de catálogo. Relacione correção, contenção e repetição de transações.

### 18. Diagnóstico

Após o crescimento da base, uma consulta passa de 100 ms para 12 s. Elabore uma investigação ordenada, sem assumir antecipadamente que falta um índice.

### 19. Evolução de schema

Planeje a inclusão obrigatória de `currency` em uma tabela de pedidos sem interromper consumidores antigos.

### 20. Projeto final

Produza uma decisão arquitetural para o Banco de pedidos da DataRetail S.A. contendo requisitos, modelo, invariantes, transações, índices, isolamento, recuperação, segurança, observabilidade e critérios de aceite.

## Critérios de avaliação

| Critério | Peso |
| --- | ---: |
| Correção conceitual | 30% |
| Justificativa e trade-offs | 25% |
| Consistência e concorrência | 20% |
| Operação e recuperação | 15% |
| Clareza | 10% |

## Próximo Capítulo

➡️ [[13-Gabarito|13 — Gabarito]]
