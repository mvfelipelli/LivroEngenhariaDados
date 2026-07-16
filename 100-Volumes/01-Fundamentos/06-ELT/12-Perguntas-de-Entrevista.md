---
title: Perguntas de Entrevista — ELT
aliases: [ELT Interview Questions]
tags: [engenharia-de-dados, fundamentos, elt, entrevistas]
type: interview
order: 12
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas para entrevistas sobre ELT."
---

# 12 — Perguntas de Entrevista

## Fundamentos e cenários

### 1. Diferencie ETL e ELT.

ETL transforma antes do destino final; ELT carrega raw e transforma na plataforma.

### 2. Raw é schema-less?

Não. Pode ser flexível, mas exige versão, metadados e política de evolução.

### 3. Por que usar staging?

Para padronizar fonte uma vez e oferecer contrato estável aos modelos seguintes.

### 4. View ou tabela?

View reduz armazenamento; tabela reduz compute de leitura. Escolha por uso e custo.

### 5. O que um incremental exige?

Chave única, filtro, merge, deletes, atrasos e full refresh.

### 6. Como testar ELT?

Schema, unicidade, relações, domínios, reconciliação, freshness e testes unitários.

### 7. O que é linhagem?

Relação rastreável entre fontes, modelos e consumidores.

### 8. Por que não expor raw?

Contém versões, dados sensíveis e semântica ainda não estabilizada.

### 9. Como controlar custo?

Medir scans e compute, atribuir por produto, definir orçamento e otimizar materializações.

### 10. Como tratar mudança de schema?

Detectar, avaliar compatibilidade, versionar contratos e migrar dependentes.

### 11. Full refresh ainda é necessário?

Sim, para reconstrução, correção e comparação com incrementais.

### 12. ELT elimina Engenharia de Dados?

Não. Move responsabilidades para modelagem, plataforma, testes, governança e operação.

### 13. Como evitar SQL duplicado?

Camadas, modelos intermediários reutilizáveis, macros controladas e revisão.

### 14. O que é produto oficial?

Interface governada com dono, contrato, SLO, testes e consumidores conhecidos.

### 15. Quando evitar ELT?

Quando dados não podem entrar brutos, o destino é limitado ou custo/latência favorece transformação anterior.

## Próximo Capítulo

➡️ [[13-Exercicios|13 — Exercícios]]
