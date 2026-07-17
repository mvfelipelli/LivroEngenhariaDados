---
title: Perguntas de Entrevista — Qualidade Python
description: "Questões sobre testes, logging e distribuição."
tags: [python, entrevista, qualidade]
aliases: [Entrevista Qualidade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Unitário e integração diferem como?

O unitário isola uma regra pequena; integração verifica colaboração real entre componentes ou infraestrutura.

## 2. Fixture global mutável é problemática por quê?

Cria dependência de ordem e vazamento de estado entre testes.

## 3. Fake e mock diferem como?

Fake possui implementação funcional simplificada; mock verifica interações esperadas.

## 4. Cobertura de 100% prova correção?

Não. Linhas podem executar sem assertions relevantes e casos importantes podem faltar.

## 5. O que teste de mutação mede?

Se mudanças artificiais no código são detectadas pela suíte, aproximando a efetividade das assertions.

## 6. Biblioteca deve configurar logging global?

Não. Ela emite por logger nomeado; a aplicação define handlers, formato e destino.

## 7. Sdist e wheel diferem como?

Sdist contém fontes para build; wheel é distribuição construída e instalável.

## 8. Por que testar o wheel?

Para detectar metadados, arquivos e entry points ausentes que o checkout pode mascarar.
