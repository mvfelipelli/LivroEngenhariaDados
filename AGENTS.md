# AGENTS.md

## Instruções Permanentes para Agentes de Inteligência Artificial

Este documento define as regras permanentes que qualquer agente de IA (OpenAI Codex, ChatGPT, Claude, Gemini, GitHub Copilot ou equivalente) deve seguir ao trabalhar neste repositório.

Estas regras têm prioridade sobre preferências implícitas do modelo sempre que não entrarem em conflito com instruções fornecidas diretamente pelo usuário.

---

## Objetivo do Projeto

Este repositório contém uma **Academia Completa de Engenharia de Dados**, escrita em português, organizada como um Vault do Obsidian.

O objetivo é produzir um material técnico de alta qualidade que funcione simultaneamente como:

* livro técnico;
* documentação;
* wiki;
* curso completo;
* laboratório prático;
* material para certificações;
* base permanente de conhecimento.

Todo conteúdo deve priorizar qualidade técnica, consistência editorial e facilidade de navegação.

---

## Papel do Agente

O agente deve atuar como um **autor técnico**, não apenas como um gerador de texto.

Sempre que produzir conteúdo, deve considerar:

* continuidade da coleção;
* consistência entre capítulos;
* manutenção dos Wikilinks;
* organização do Vault;
* experiência do leitor.

---

## Idioma

Todo o conteúdo deve ser produzido em:

**Português do Brasil**

Termos técnicos amplamente aceitos podem permanecer em inglês quando isso representar o padrão do mercado.

Exemplos:

* Data Lake
* Data Warehouse
* Cluster
* Commit
* Merge
* Hash Join

Evite traduções artificiais.

---

## Público-Alvo

Assuma que o leitor possui conhecimento técnico crescente.

Os capítulos devem atender simultaneamente:

* iniciantes;
* profissionais intermediários;
* engenheiros de dados experientes.

Sempre começar pelos fundamentos antes de avançar para detalhes mais complexos.

---

## Filosofia Editorial

Sempre priorizar:

1. conceitos;
2. fundamentos;
3. funcionamento interno;
4. aplicações práticas;
5. ferramentas.

Nunca inverter essa ordem.

Ferramentas mudam.

Fundamentos permanecem.

---

## Organização do Projeto

O Vault está organizado em diretórios numerados.

Nunca alterar essa organização sem solicitação explícita.

A estrutura principal inclui:

* 000-Atlas
* 001-Dashboard
* 005-Wiki
* 010-Biblioteca
* 020-Laboratorios
* 030-Projetos
* 040-Certificacoes
* 050-Templates
* 060-Assets
* 070-Anotacoes
* 080-Inbox
* 090-Arquivados
* 100-Volumes
* 999-Arquivos-Temporarios

---

## Organização dos Volumes

Cada volume contém diversos módulos.

Cada módulo possui um README e um conjunto padronizado de capítulos.

O agente nunca deve alterar essa estrutura sem autorização explícita.

---

## Estrutura Obrigatória dos Módulos

Cada módulo deve conter:

* README
* Objetivos
* Introdução
* Capítulos técnicos
* Estudo de Caso
* Resumo
* Perguntas de Entrevista
* Exercícios
* Gabarito
* Laboratório
* Solução
* Referências

Caso algum arquivo esteja ausente, o agente poderá criá-lo mantendo exatamente o padrão do projeto.

---

## Continuidade

Antes de criar novos arquivos, o agente deve:

1. localizar o último módulo concluído;
2. identificar o próximo módulo previsto;
3. verificar se já existe conteúdo parcial;
4. continuar exatamente do ponto onde o projeto foi interrompido.

Nunca duplicar capítulos.

Nunca reiniciar módulos.

Nunca alterar capítulos concluídos sem solicitação.

---

## Wikilinks

Sempre utilizar Wikilinks do Obsidian.

Exemplo:

```text
[[Data Lake]]

[[Apache Spark]]

[[Normalização]]
```

Nunca utilizar links relativos quando um Wikilink for possível.

---

## Mermaid

Sempre preferir diagramas Mermaid.

Diagramas devem ser compatíveis com Obsidian.

Utilizar principalmente:

* flowchart
* sequenceDiagram
* classDiagram
* stateDiagram
* erDiagram
* mindmap

Evitar sintaxes não suportadas pelo Obsidian.

---

## YAML Frontmatter

Todos os documentos principais devem iniciar com YAML.

Exemplo:

```yaml
---
title:
description:
tags:
aliases:
created:
updated:
---
```

Nunca omitir o frontmatter em novos documentos estruturados.

---

## Callouts

Sempre utilizar os callouts do Obsidian quando apropriado.

Exemplos:

* note
* tip
* warning
* info
* example
* quote

Evitar excesso de callouts.

Utilizá-los apenas quando agregarem valor.

---

## Exemplos

Sempre fornecer exemplos.

Sempre que possível incluir:

* SQL
* Python
* Bash
* Spark
* PostgreSQL
* Docker

Os exemplos devem ser executáveis.

Evitar pseudocódigo quando houver uma implementação simples.

---

## Estudos de Caso

Sempre que possível utilizar o cenário da empresa fictícia:

**DataRetail S.A.**

Isso garante continuidade entre todos os volumes.

---

## Exercícios

Os exercícios devem evoluir em dificuldade.

Preferir:

1. revisão conceitual;
2. interpretação;
3. aplicação prática;
4. desafios.

---

## Laboratórios

Laboratórios devem ser reproduzíveis.

Sempre informar:

* objetivo;
* pré-requisitos;
* ambiente;
* passos;
* validação;
* conclusão.

---

## Referências

Sempre priorizar:

1. documentação oficial;
2. RFCs;
3. livros;
4. artigos técnicos.

Evitar blogs sem reconhecimento técnico.

---

## Diagramas

Sempre que um conceito puder ser explicado visualmente, criar um diagrama.

Preferir diagramas simples.

Evitar diagramas excessivamente grandes.

---

## Estilo de Escrita

Escrever como um livro técnico.

Evitar:

* excesso de tópicos curtos;
* linguagem promocional;
* frases vagas;
* repetições.

Priorizar explicações completas.

---

## Atualizações

Quando novos arquivos forem criados:

* atualizar índices;
* preservar Wikilinks;
* verificar referências cruzadas;
* manter consistência da navegação.

---

## Arquivos de Governança

Antes de trabalhar no projeto, o agente deve ler:

1. README.md
2. AGENTS.md
3. EDITORIAL.md
4. ROADMAP.md
5. MEMORY.md

Esses documentos representam a fonte oficial de contexto do projeto.

---

## Alterações Arquiteturais

O agente não deve:

* reorganizar diretórios;
* renomear módulos;
* alterar a numeração dos volumes;
* modificar convenções;
* remover arquivos.

Essas ações somente podem ocorrer mediante solicitação explícita.

---

## Qualidade

Antes de considerar qualquer tarefa concluída, verificar:

* consistência técnica;
* coerência editorial;
* ortografia;
* Wikilinks;
* Mermaid;
* YAML;
* referências.

O objetivo é produzir conteúdo equivalente a um livro técnico profissional.

---

## Princípio Fundamental

Este projeto não é apenas uma coleção de arquivos Markdown.

Ele representa uma base de conhecimento viva, evolutiva e permanentemente organizada sobre Engenharia de Dados.

Toda contribuição deve preservar essa visão de longo prazo.
