---
title: Perguntas de Entrevista
description: "Perguntas sobre modelagem conceitual e ER."
tags: [modelagem-de-dados, entrevista, er]
aliases: [Entrevista Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Entidade e tabela são sinônimos?

Não. Entidade é conceito do domínio; tabela é uma possível implementação lógica/física.

## 2. O que caracteriza entidade fraca?

Identidade e existência dependentes de entidade proprietária, complementadas por chave parcial.

## 3. Quando atributo multivalorado vira entidade?

Quando elementos possuem atributos, identidade, relacionamentos, ordem ou histórico relevantes.

## 4. O que é relacionamento recursivo?

Associação na qual a mesma entidade participa em papéis distintos.

## 5. Como ler `1..N`?

Participação obrigatória de ao menos uma ocorrência e possibilidade de várias.

## 6. Quando criar entidade associativa?

Quando uma relação N:N possui atributos, identidade, eventos ou ciclo de vida.

## 7. Especialização disjunta significa o quê?

Uma ocorrência do supertipo participa de no máximo um dos subtipos definidos.

## 8. Chen e Crow's Foot diferem como?

Chen explicita atributos e relacionamentos como formas; Crow's Foot compacta entidades e cardinalidades.

## 9. Como validar cardinalidade?

Pergunte mínimo e máximo nos dois sentidos, use estados intermediários e procure contraexemplos.

## 10. Qual o papel do glossário?

Definir termos e limites que o diagrama sozinho não comunica.
