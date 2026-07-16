---
title: Exercícios
aliases:
  - Lista de Exercícios
volume: 01
module: 01
chapter: 13
type: exercises
status: Concluído
tags:
  - exercícios
  - revisão
description: "Capítulo técnico sobre Exercícios na Formação em Engenharia de Dados."
created: "2026-07-14"
updated: "2026-07-14"
---

[[100-Volumes/01-Fundamentos/01-Dados/README]] | [[12-Perguntas-de-Entrevista|12 - Perguntas de Entrevista]] | [[13-Gabarito|13 - Gabarito]] | [[14-Laboratorio|14 - Laboratório]]

---

# Exercícios

> [!quote]
> "Aprender não é apenas ler. É aplicar, analisar e resolver problemas."

---

## Objetivo

Este capítulo reúne exercícios para consolidar os conceitos estudados no módulo **Dados**.

Os exercícios foram organizados em níveis crescentes de dificuldade.

---

## Nível 1 — Fixação

### Exercício 1

Defina com suas próprias palavras:

- dado;
- informação;
- conhecimento.

---

### Exercício 2

Explique por que dados e informação não são sinônimos.

---

### Exercício 3

Complete a tabela.

| Conceito | Definição |
|-----------|-----------|
| Dado | |
| Informação | |
| Conhecimento | |

---

### Exercício 4

Quais são os cinco Vs do Big Data?

Explique cada um em uma frase.

---

## Nível 2 — Compreensão

### Exercício 5

Classifique os seguintes exemplos.

| Exemplo | Estruturado | Semiestruturado | Não Estruturado |
|----------|:-----------:|:---------------:|:---------------:|
| CSV | | | |
| JSON | | | |
| Foto | | | |
| XML | | | |
| PostgreSQL | | | |
| PDF | | | |
| Vídeo | | | |

---

### Exercício 6

Explique a diferença entre:

- Schema-on-Write
- Schema-on-Read

Quando cada abordagem costuma ser utilizada?

---

### Exercício 7

Descreva todas as etapas do ciclo de vida dos dados.

---

## Nível 3 — Aplicação

### Exercício 8

Você recebeu um arquivo contendo:

- CPF
- Nome
- Cidade
- E-mail

Existem:

- registros duplicados;
- e-mails inválidos;
- cidades em formatos diferentes;
- CPFs ausentes.

Responda:

1. Quais problemas de qualidade existem?
2. Como você os trataria?
3. Em qual etapa do pipeline faria essas validações?

---

### Exercício 9

Considere as seguintes fontes.

| Fonte | Tipo predominante |
|--------|-------------------|
| ERP | |
| Aplicativo | |
| Sensores IoT | |
| Imagens | |
| Marketplace | |

Preencha a tabela classificando os dados.

---

### Exercício 10

Explique quais metadados você registraria para uma tabela chamada:

```text
clientes
```

---

## Nível 4 — Projeto

### Exercício 11

Você foi contratado pela DataRetail S.A.

Sua missão é levantar todas as fontes de dados da empresa.

Elabore uma tabela contendo:

- sistema;
- tipo de dado;
- frequência de atualização;
- volume estimado;
- responsável;
- sensibilidade.

---

### Exercício 12

Escolha três conjuntos de dados do seu cotidiano.

Exemplos:

- aplicativo bancário;
- supermercado;
- hospital;
- escola;
- empresa.

Para cada conjunto responda:

- os dados são estruturados?
- possuem metadados?
- qual o ciclo de vida?
- quais riscos de qualidade existem?

---

## Nível 5 — Arquitetura

### Exercício 13

A empresa pretende armazenar:

- vídeos;
- imagens;
- JSON;
- vendas;
- pagamentos;
- sensores IoT.

Proponha uma arquitetura inicial.

Justifique:

- armazenamento;
- processamento;
- consulta.

Não se preocupe com ferramentas específicas.

Explique apenas seu raciocínio.

---

### Exercício 14

Analise o cenário.

```text
CRM

↓

CSV

↓

Python

↓

PostgreSQL

↓

Dashboard
```

Responda:

- Onde existem dados?
- Onde existem metadados?
- Onde deve haver validação?
- Onde deve haver monitoramento?

---

## Desafio

A DataRetail possui:

- ERP
- CRM
- Marketplace
- Aplicativo
- PDV
- Logística

Todos utilizam bancos diferentes.

Descreva:

1. quais seriam os primeiros passos de um Engenheiro de Dados;
2. quais informações precisariam ser levantadas;
3. quais riscos existem;
4. quais seriam suas prioridades.

---

## Questões para Discussão

Não existe resposta única.

Discuta com colegas ou registre sua opinião.

### Questão 1

Todo dado precisa ser armazenado?

---

### Questão 2

Vale a pena manter histórico infinito?

---

### Questão 3

É melhor corrigir dados na origem ou durante o pipeline?

---

### Questão 4

Qual dimensão da qualidade costuma gerar mais problemas nas empresas?

Justifique.

---

## Autoavaliação

Avalie seu nível de confiança.

| Tema | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
|------|:--:|:--:|:--:|:--:|:--:|
| Conceito de Dados | ☐ | ☐ | ☐ | ☐ | ☐ |
| Tipos de Dados | ☐ | ☐ | ☐ | ☐ | ☐ |
| Estruturação | ☐ | ☐ | ☐ | ☐ | ☐ |
| Ciclo de Vida | ☐ | ☐ | ☐ | ☐ | ☐ |
| Qualidade | ☐ | ☐ | ☐ | ☐ | ☐ |
| Metadados | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Critérios de Conclusão

Considere este módulo concluído quando você conseguir:

- explicar todos os conceitos sem consultar o material;
- responder às perguntas de entrevista;
- resolver os exercícios propostos;
- concluir o laboratório prático.

---

## Veja Também

➡️ [[14-Laboratorio|14 - Laboratório]]

➡️ [[11-Resumo|11 - Resumo]]

➡️ [[12-Perguntas-de-Entrevista|12 - Perguntas de Entrevista]]

---

> [!success]
> Os exercícios deste módulo foram elaborados para desenvolver não apenas conhecimento conceitual, mas também a capacidade de analisar problemas, justificar decisões e pensar como um Engenheiro de Dados.
