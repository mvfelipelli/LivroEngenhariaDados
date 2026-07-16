---
title: Introdução à Modelagem de Dados
aliases: [Data Modeling Introduction]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, introducao]
type: chapter
order: 02
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Motivação, propósito e processo fundamental da Modelagem de Dados."
---

# 02 — Introdução

## Antes das tabelas

Uma organização fala em clientes, contratos, pedidos, produtos e entregas. Um sistema precisa transformar esses conceitos em estruturas persistentes. Essa passagem não é automática: palavras podem ter significados diferentes, regras podem estar implícitas e o mesmo fato pode servir a processos distintos.

Modelagem de Dados é a disciplina que torna essas decisões explícitas. Ela identifica os conceitos relevantes, suas propriedades, relações, regras e necessidades de uso antes de escolher detalhes de implementação.

## O problema que a modelagem resolve

Considere a frase: “um cliente realiza pedidos”. Ela ainda não responde:

- um pedido pode existir sem cliente identificado?
- uma pessoa pode representar mais de um cliente?
- o endereço pertence ao cliente ou ao pedido?
- o preço deve refletir o catálogo atual ou o momento da compra?
- cancelamento remove o pedido ou altera seu estado?

Cada resposta muda o modelo. Quando essas decisões ficam apenas no código ou na memória das pessoas, diferentes sistemas passam a representar o mesmo domínio de formas incompatíveis.

> [!note]
> Um modelo não é uma fotografia neutra da realidade. Ele é uma abstração construída para um propósito, com limites e escolhas que devem ser documentados.

## Modelagem como processo

O trabalho começa com o domínio, progride por diferentes níveis de abstração e retorna ao negócio para validação.

```mermaid
flowchart LR
    A[Descobrir o domínio] --> B[Identificar conceitos e regras]
    B --> C[Construir o modelo]
    C --> D[Validar com cenários]
    D --> E[Implementar]
    E --> F[Observar o uso]
    F --> A
```

Modelos evoluem porque regras, produtos e padrões de acesso também evoluem. Por isso, modelagem não é uma atividade executada apenas no início de um projeto.

## Três perspectivas complementares

| Perspectiva | Pergunta principal | Evita antecipar |
| --- | --- | --- |
| Conceitual | Quais conceitos e regras existem no domínio? | tabelas e tipos físicos |
| Lógica | Como os dados serão organizados em um modelo? | detalhes de um produto específico |
| Física | Como o modelo será implementado e acessado? | abstrações sem restrições reais |

A separação ajuda a preservar o significado enquanto decisões técnicas são acrescentadas gradualmente.

## O mesmo domínio, modelos diferentes

O processamento de pedidos pode exigir uma estrutura normalizada para registrar transações e um modelo dimensional para analisar vendas por tempo, produto e região. As duas representações podem ser corretas porque respondem a propósitos diferentes.

Esse princípio evita duas simplificações comuns: procurar um único modelo universal e copiar diretamente o schema operacional para todas as cargas analíticas.

## Modelagem na Engenharia de Dados

Engenheiros de Dados usam modelos para:

- interpretar schemas de origem;
- preservar chaves e significado em pipelines;
- projetar contratos e produtos de dados;
- integrar domínios com definições distintas;
- organizar fatos, dimensões e históricos;
- avaliar compatibilidade durante evoluções;
- implementar testes de integridade e qualidade.

## Perguntas orientadoras

- Qual processo ou decisão o modelo deve apoiar?
- Quais conceitos possuem identidade própria?
- Quais fatos precisam ser preservados historicamente?
- Quais regras nunca podem ser violadas?
- Quem produz e quem consome os dados?
- Quais consultas e mudanças são esperadas?
- Que informação ficou deliberadamente fora do modelo?

## Erros comuns na primeira abordagem

- iniciar pelas tabelas sem compreender o domínio;
- confundir nomes iguais com conceitos iguais;
- armazenar múltiplos fatos em um único atributo;
- usar identificadores sem definir sua estabilidade;
- representar estado atual quando o requisito exige histórico;
- desnormalizar antes de medir uma necessidade;
- tratar o diagrama como documentação imutável.

## Síntese

Modelagem conecta linguagem de negócio, estrutura de dados e comportamento dos sistemas. Um bom modelo não elimina a complexidade do domínio; ele a torna visível, discutível e verificável.

## Próximo Capítulo

➡️ **03 — O que é Modelagem de Dados**
