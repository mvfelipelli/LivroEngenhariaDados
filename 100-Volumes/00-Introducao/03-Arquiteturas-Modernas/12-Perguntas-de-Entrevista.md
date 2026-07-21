---
title: Perguntas de Entrevista — Arquiteturas Modernas
description: "Questões comentadas sobre estilos arquiteturais."
tags: [arquitetura-de-dados, entrevista, sistemas]
aliases: [Entrevista Arquiteturas Modernas]
created: 2026-07-21
updated: 2026-07-21
---

# Perguntas de Entrevista

## Lakehouse substitui todo Warehouse?

Não necessariamente. Requisitos de consumo, governança, operação e ferramentas podem justificar coexistência.

## Lambda e Kappa diferem como?

Lambda mantém caminhos batch e rápido; Kappa busca um caminho streaming com replay do log.

## O que é Data Mesh?

Uma abordagem sociotécnica baseada em domínio, produto de dados, plataforma self-service e governança federada.

## Camadas Bronze, Silver e Gold garantem qualidade?

Não. É preciso definir contratos, testes, ownership e publicação em cada fronteira.

## Como escolher uma arquitetura?

Partir de requisitos mensuráveis, restrições, capacidades da equipe, custos e alternativas, registrando trade-offs.
