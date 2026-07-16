---
title: Perguntas de Entrevista — Bancos de Dados
aliases: [Database Interview Questions]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, entrevistas]
type: interview
order: 12
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas para entrevistas sobre Bancos de Dados."
---

# 12 — Perguntas de Entrevista

> [!tip]
> Responda primeiro em suas palavras. Uma resposta forte conecta conceito, mecanismo e trade-off.

## Fundamentos

### 1. Qual é a diferença entre Banco de Dados e SGBD?

Banco de Dados é a coleção organizada; SGBD é o software que define, consulta, protege, persiste e recupera essa coleção.

### 2. Qual é a diferença entre schema e instância?

Schema descreve estrutura e regras. Instância é o conteúdo existente em determinado momento.

### 3. O que é independência física de dados?

É a capacidade de alterar detalhes de armazenamento sem exigir mudanças equivalentes nas aplicações e no modelo lógico.

### 4. Por que usar restrições no Banco de Dados?

Elas preservam regras para todos os consumidores, mesmo quando diferentes aplicações acessam os mesmos dados.

## Modelos e arquitetura

### 5. Quando escolher um Banco de documentos?

Quando agregados hierárquicos são lidos juntos, variam de estrutura e não dependem de relações globais complexas. Flexibilidade ainda exige contrato e validação.

### 6. O que é persistência poliglota?

Uso de diferentes modelos por carga. Pode melhorar adequação, mas aumenta operação, integração e governança.

### 7. O que é uma página?

Unidade de armazenamento, leitura e cache do SGBD. Uma consulta a uma linha normalmente carrega a página que a contém.

### 8. Para que serve o buffer pool?

Mantém páginas em memória para reduzir I/O e gerencia leitura, substituição e gravação de páginas alteradas.

### 9. O que é WAL?

Write-Ahead Log registra informações de recuperação antes que a página de dados correspondente seja persistida.

## Transações e concorrência

### 10. Explique ACID.

Atomicidade aplica tudo ou nada; consistência preserva regras declaradas; isolamento controla interferência concorrente; durabilidade preserva commits segundo a garantia do sistema.

### 11. Consistência ACID garante que todo dado esteja correto?

Não. O SGBD protege regras declaradas; não conhece regras de negócio ausentes ou dados de origem incorretos.

### 12. O que é uma leitura não repetível?

A mesma linha retorna valores diferentes dentro de uma transação porque outra confirmou uma alteração entre as leituras.

### 13. O que é deadlock?

Espera circular por recursos. O SGBD aborta uma transação; a aplicação deve tratar e possivelmente repetir.

### 14. O que é MVCC?

Controle por múltiplas versões que permite snapshots de leitura e reduz alguns bloqueios. Não elimina conflitos nem manutenção de versões.

## Índices e desempenho

### 15. Índice sempre melhora desempenho?

Não. Acelera padrões específicos, mas consome espaço e aumenta custo de escrita e manutenção.

### 16. Por que a ordem de um índice composto importa?

Ela determina prefixos, filtros e ordenações que podem aproveitar a estrutura.

### 17. O que faz um otimizador?

Compara planos e estima custos de varreduras, junções, ordenações e agregações usando estatísticas.

### 18. Como investigar uma consulta lenta?

Confirmar requisito, obter plano real, comparar estimativas e linhas, observar I/O, CPU, locks e memória, revisar índices e medir novamente.

## Cenários

### 19. Duas compras disputam a última unidade. Como evitar estoque negativo?

Usar atualização condicional atômica ou bloqueio apropriado dentro de transação, verificar linhas afetadas e tratar a falha.

### 20. Relatórios degradam o checkout. O que avaliar?

Planos, índices, contenção e recursos; separar carga analítica por réplica ou produto derivado; confirmar atraso aceitável e recuperação.

### 21. Réplica substitui backup?

Não. Ela pode reproduzir exclusões e corrupção. Backup preserva pontos recuperáveis e precisa ser testado.

### 22. Como escolher um Banco de Dados?

Partir de modelo, consultas, garantias, volume, concorrência, latência, falhas, recuperação, segurança, retenção e capacidade operacional.

## Próximo Capítulo

➡️ [[13-Exercicios|13 — Exercícios]]
