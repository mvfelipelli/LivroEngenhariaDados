# EDITORIAL.md

# Manual Editorial

## Formação em Engenharia de Dados

---

# Objetivo

Este documento estabelece o padrão editorial oficial da coleção **Formação em Engenharia de Dados**.

Seu objetivo é garantir que todos os documentos produzidos durante a evolução do projeto mantenham o mesmo nível de qualidade, profundidade técnica, organização e identidade visual.

Todas as contribuições devem seguir estas regras.

---

# Filosofia Editorial

A coleção deve ser escrita como um livro técnico profissional.

Ela não deve parecer:

* documentação de software;
* apostila;
* conjunto de anotações;
* blog;
* tutorial isolado.

O leitor deve perceber que todos os capítulos pertencem à mesma obra.

---

# Princípios Fundamentais

Todo conteúdo deve seguir os princípios abaixo.

## Clareza

Explique conceitos complexos utilizando linguagem simples.

Evite frases longas quando não agregarem valor.

---

## Precisão

Toda afirmação técnica deve ser correta.

Quando houver simplificações, elas devem ser explicitadas.

---

## Progressão

Os assuntos devem evoluir gradualmente.

Nunca assumir conhecimento que ainda não foi apresentado.

---

## Consistência

A mesma terminologia deve ser utilizada durante toda a coleção.

Evite alternar nomes para o mesmo conceito.

---

## Neutralidade Tecnológica

Sempre ensinar primeiro o conceito.

Depois apresentar implementações em ferramentas.

---

# Idioma

Todo o conteúdo deve ser produzido em Português do Brasil.

Termos técnicos amplamente consolidados podem permanecer em inglês.

Exemplos:

* Data Lake
* Data Warehouse
* Commit
* Merge
* Cluster
* Namespace
* Schema
* Broadcast Join

Evitar traduções artificiais.

---

# Público-Alvo

Os capítulos devem atender simultaneamente três perfis.

## Iniciante

Necessita compreender conceitos.

---

## Intermediário

Deseja aprofundamento técnico.

---

## Avançado

Busca compreender funcionamento interno, arquitetura e boas práticas.

---

# Estrutura de um Capítulo

Todo capítulo técnico deve seguir a seguinte sequência.

1. Objetivos

2. Introdução

3. Motivação

4. Conceitos Fundamentais

5. Desenvolvimento Técnico

6. Diagramas

7. Exemplos

8. Boas Práticas

9. Erros Comuns

10. Resumo

11. Próximo Capítulo

---

# Objetivos

Todo capítulo inicia informando claramente o que será aprendido.

Os objetivos devem utilizar verbos de ação.

Exemplos:

* compreender;
* implementar;
* comparar;
* projetar;
* analisar.

---

# Introdução

A introdução deve responder:

* por que este assunto existe;
* qual problema resolve;
* onde é utilizado.

Nunca iniciar diretamente com definições.

---

# Desenvolvimento

O desenvolvimento deve seguir esta ordem:

Conceito

↓

Funcionamento

↓

Arquitetura

↓

Exemplo

↓

Caso real

↓

Resumo

---

# Diagramas

Sempre que possível incluir diagramas Mermaid.

Diagramas devem explicar.

Não decorar.

Priorizar:

* flowchart
* sequenceDiagram
* classDiagram
* stateDiagram
* erDiagram
* mindmap

---

# Código

Todo código deve ser válido.

Sempre informar a linguagem.

Exemplos:

```sql
SELECT *
FROM clientes;
```

```python
df.show()
```

```bash
docker compose up
```

Evitar pseudocódigo.

---

# Exemplos

Todo conceito importante deve possuir exemplos.

Preferencialmente:

* exemplo simples;
* exemplo intermediário;
* exemplo real.

---

# Tabelas

Utilizar tabelas quando melhorarem a compreensão.

Evitar tabelas excessivamente grandes.

---

# Callouts

Utilizar callouts apenas quando necessários.

Exemplos:

```text
> [!note]

> [!tip]

> [!warning]

> [!example]
```

Evitar excesso.

---

# Wikilinks

Sempre utilizar Wikilinks do Obsidian.

Exemplo:

```text
[[Apache Spark]]

[[SQL]]

[[Particionamento]]
```

Nunca criar links quebrados.

---

# YAML Frontmatter

Todos os documentos estruturados devem iniciar com:

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

---

# Convenção de Arquivos

Os arquivos devem possuir nomes claros.

Exemplo:

```text
01-Objetivos.md

02-Introducao.md

03-Arquitetura-do-Data-Lake.md
```

Evitar espaços.

Evitar caracteres especiais.

---

# Convenção de Títulos

Utilizar:

```markdown
# Capítulo

## Seção

### Subseção
```

Evitar níveis maiores que quatro.

---

# Estudos de Caso

Sempre utilizar o cenário da empresa fictícia:

**DataRetail S.A.**

O cenário deve evoluir durante toda a coleção.

Evitar criar empresas fictícias diferentes.

---

# Laboratórios

Todo laboratório deve conter:

Objetivo

Pré-requisitos

Ambiente

Passo a passo

Resultado esperado

Validação

Conclusão

---

# Exercícios

Organizar por dificuldade.

1. Revisão

2. Conceitos

3. Aplicação

4. Desafio

---

# Perguntas de Entrevista

Priorizar perguntas utilizadas em processos seletivos reais.

Evitar perguntas puramente acadêmicas.

Sempre fornecer respostas fundamentadas no capítulo.

---

# Referências

Prioridade:

1. Documentação oficial

2. RFC

3. Livros

4. Artigos técnicos

5. White Papers

Evitar blogs desconhecidos.

---

# Estilo de Escrita

Escrever como um autor técnico.

Não escrever como um chatbot.

Evitar:

* frases motivacionais;
* marketing;
* autopromoção;
* linguagem excessivamente informal.

---

# Profundidade

Sempre responder:

O que é?

Por que existe?

Como funciona?

Quando utilizar?

Quando evitar?

Como implementar?

Quais limitações?

Quais alternativas?

---

# Repetições

Evitar repetir definições em diversos capítulos.

Quando necessário, utilizar Wikilinks.

---

# Consistência

Antes de finalizar um documento verificar:

* nomenclatura;
* ortografia;
* diagramas;
* exemplos;
* links;
* referências.

---

# Checklist Editorial

Todo documento deve responder positivamente às perguntas abaixo.

* O objetivo do capítulo está claro?
* Existe uma introdução?
* O conceito foi apresentado antes da implementação?
* Há pelo menos um diagrama?
* Existem exemplos executáveis?
* Há boas práticas?
* Foram apresentados erros comuns?
* Existe um resumo?
* Existem links para capítulos relacionados?
* O YAML está presente?
* Os Wikilinks funcionam?
* As referências foram incluídas?

Somente após esse checklist o documento pode ser considerado concluído.

---

# Identidade da Coleção

A **Formação em Engenharia de Dados** deve transmitir a sensação de uma obra única e contínua.

Independentemente de quem produza um capítulo, o leitor deve perceber a mesma organização, o mesmo estilo de escrita e o mesmo nível de qualidade em toda a coleção.

A consistência editorial é considerada um requisito técnico do projeto, e não apenas um aspecto estético.
