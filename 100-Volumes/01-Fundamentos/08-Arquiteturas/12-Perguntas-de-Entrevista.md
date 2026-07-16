---
title: Perguntas de Entrevista sobre Arquiteturas de Dados
aliases: [Entrevista de Arquitetura de Dados]
tags: [arquitetura, entrevista, carreira]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e critérios de resposta sobre arquitetura de dados."
---

# Perguntas de Entrevista

## 1. O que torna uma decisão arquitetural?

Impacto amplo, influência em atributos de qualidade, alto custo de reversão ou restrição duradoura sobre decisões futuras.

## 2. Como você começa o desenho de uma arquitetura?

Pelo contexto, objetivos, stakeholders, restrições e cenários mensuráveis; depois compara alternativas e consequências.

## 3. Data Lake substitui Data Warehouse?

Não necessariamente. Eles atendem responsabilidades diferentes e podem coexistir; a resposta depende de consumo, governança, desempenho e operação.

## 4. Qual a diferença entre evento e comando?

Evento afirma um fato passado e pode ter vários consumidores. Comando expressa intenção direcionada a um responsável.

## 5. Quando streaming não é apropriado?

Quando a latência não justifica custo e complexidade de estado contínuo, ou quando equipe e requisitos favorecem batch simples e reproduzível.

## 6. O que é um ADR?

Registro conciso de contexto, decisão, alternativas, status e consequências, preservado como histórico.

## 7. Como validar uma arquitetura?

Com protótipos orientados a risco, testes de carga, cenários de falha, métricas e fitness functions ligadas aos requisitos.

## 8. Data Mesh é uma arquitetura tecnológica?

É uma abordagem sociotécnica de propriedade por domínio, produto de dados, plataforma self-service e governança federada.

## 9. Como evitar lock-in?

Separar contratos de implementações, adotar formatos e interfaces portáveis quando necessário e testar o custo real de substituição. Abstração total também tem custo.

## 10. Como migrar uma plataforma crítica?

Por fatias, com execução paralela, reconciliação, roteamento gradual, observabilidade, rollback e critérios explícitos de desativação.

Transforme as respostas em prática em [[13-Exercicios]].
