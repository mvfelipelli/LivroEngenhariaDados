---
title: Perguntas de Entrevista
description: "Perguntas e respostas sobre desempenho e planos SQL."
tags: [sql, entrevista, performance]
aliases: [Entrevista sobre Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Sequential scan é sempre ruim?

Não. Ele pode ser o caminho mais barato quando a consulta lê grande fração da tabela, a relação é pequena ou acessos aleatórios via índice seriam mais caros.

## 2. Qual a diferença entre custo e tempo?

Custo é uma estimativa interna comparativa baseada no modelo do otimizador. Tempo é uma medição afetada por cache, concorrência, hardware e esperas.

## 3. Por que a cardinalidade importa?

Ela dimensiona o trabalho dos operadores seguintes. Erros grandes podem selecionar join, ordem e memória inadequados.

## 4. Como escolher a ordem de um índice composto?

Partindo dos padrões de consulta: colunas de igualdade, depois intervalo ou ordenação, considerando seletividade, projeção e reutilização por outras consultas.

## 5. O que é índice de cobertura?

É um índice que contém as colunas necessárias para localizar e retornar o resultado, potencialmente evitando acesso à tabela.

## 6. Quando nested loop funciona bem?

Quando a entrada externa é pequena e cada busca interna é barata, normalmente por chave indexada.

## 7. O que significa spill?

Um operador excedeu a memória disponível e usou armazenamento temporário, elevando I/O e latência.

## 8. O que torna um predicado não SARGable?

Uma forma que impede usar diretamente a coluna como chave/faixa de busca, como função sobre a coluna ou conversão incompatível.

## 9. Que risco existe em EXPLAIN ANALYZE?

A instrução é realmente executada; operações de escrita e funções com efeitos colaterais podem alterar estado.

## 10. Como provar que uma otimização é válida?

Compare resultados, planos e métricas sob carga representativa, documente contexto e rollback e acompanhe regressões após a implantação.
