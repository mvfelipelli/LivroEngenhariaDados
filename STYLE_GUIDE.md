# STYLE_GUIDE.md

# Guia de Estilo

## Formação em Engenharia de Dados

---

# Objetivo

Este documento define o padrão de escrita utilizado em toda a coleção **Formação em Engenharia de Dados**.

Seu objetivo é garantir que todos os capítulos apresentem a mesma identidade visual, terminologia, nomenclatura e organização, independentemente de quem produza o conteúdo.

Este guia complementa o `EDITORIAL.md`.

---

# Princípios

Todo conteúdo deve ser:

* consistente;
* técnico;
* objetivo;
* legível;
* reutilizável;
* atemporal.

---

# Idioma

Todo o conteúdo deve ser produzido em:

**Português do Brasil**

Entretanto, termos técnicos consolidados na indústria permanecem em inglês.

Exemplos:

* Data Lake
* Data Warehouse
* Data Lakehouse
* Data Mesh
* Data Fabric
* Streaming
* Batch
* Cluster
* Commit
* Merge
* Pull Request
* Namespace
* Schema
* Broadcast Join

Evitar traduções literais.

---

# Capitalização

Utilizar maiúsculas apenas quando fizerem parte do nome oficial.

Exemplos corretos:

* Apache Spark
* PostgreSQL
* Microsoft SQL Server
* Amazon S3
* Google Cloud Storage

Exemplos incorretos:

* apache spark
* Postgre Sql
* Sql Server

---

# Siglas

Na primeira ocorrência:

```text
Apache Airflow (Airflow)

Change Data Capture (CDC)

Extract, Transform and Load (ETL)
```

Após isso utilizar apenas a sigla quando apropriado.

---

# Terminologia Oficial

Sempre utilizar os mesmos termos.

| Preferencial   | Evitar                                         |
| -------------- | ---------------------------------------------- |
| Banco de Dados | Base de Dados                                  |
| Data Lake      | Lago de Dados                                  |
| Pipeline       | Fluxo                                          |
| Cluster        | Agrupamento                                    |
| Schema         | Esquema (quando se referir ao objeto do banco) |
| Namespace      | Espaço de nomes                                |
| Commit         | Gravação                                       |
| Merge          | Mesclagem (quando se referir ao Git)           |

---

# Nomes de Arquivos

Utilizar:

* números de dois dígitos;
* palavras separadas por hífen;
* sem acentos;
* sem espaços.

Exemplos:

```text
01-Objetivos.md

02-Introducao.md

03-Arquitetura-Data-Lake.md

14-Laboratorio.md
```

Nunca utilizar:

```text
Introdução.md

Meu Arquivo.md

capitulo1.md
```

---

# Diretórios

Os diretórios devem utilizar:

```text
01-Fundamentos

02-Linux

03-SQL

04-Modelagem
```

Nunca:

```text
fundamentos

SQL

Modulo1
```

---

# Títulos

Sempre utilizar:

```markdown
# Capítulo

## Seção

### Subseção

#### Detalhamento
```

Evitar níveis superiores a quatro.

---

# Parágrafos

Priorizar parágrafos curtos.

Cada parágrafo deve transmitir apenas uma ideia principal.

Evitar blocos longos de texto.

---

# Listas

Preferir listas quando:

* houver enumeração;
* comparação;
* sequência de passos.

Evitar listas excessivamente longas.

---

# Ênfase

Utilizar:

**negrito**

para:

* conceitos importantes;
* definições;
* palavras-chave.

Utilizar:

*itálico*

para:

* termos estrangeiros;
* livros;
* publicações.

Evitar sublinhado.

---

# Código

Todo código deve indicar a linguagem.

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

```yaml
version: "3"
```

---

# SQL

Palavras reservadas sempre em maiúsculas.

Exemplo:

```sql
SELECT
    nome,
    idade
FROM clientes
WHERE idade > 18
ORDER BY idade;
```

---

# Python

Seguir PEP 8.

Sempre utilizar:

* nomes descritivos;
* snake_case;
* funções pequenas.

---

# Bash

Sempre utilizar:

```bash
set -euo pipefail
```

quando aplicável.

Explicar comandos destrutivos.

---

# YAML

Sempre utilizar:

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

No início dos documentos estruturados.

---

# Markdown

Utilizar apenas recursos compatíveis com Obsidian.

Evitar HTML.

---

# Wikilinks

Sempre utilizar:

```text
[[Apache Spark]]

[[Data Warehouse]]

[[PostgreSQL]]
```

Nunca utilizar caminhos relativos quando existir um Wikilink equivalente.

---

# Callouts

Preferir:

```text
> [!note]

> [!tip]

> [!warning]

> [!important]

> [!example]
```

Utilizar apenas quando agregarem valor.

---

# Diagramas

Utilizar Mermaid.

Priorizar:

* flowchart
* sequenceDiagram
* classDiagram
* erDiagram
* stateDiagram
* journey
* mindmap

Diagramas devem ser simples.

Cada diagrama deve explicar apenas um conceito.

---

# Tabelas

Utilizar tabelas apenas quando melhorarem a compreensão.

Evitar tabelas com excesso de colunas.

---

# Exemplos

Sempre que possível apresentar três níveis.

## Básico

Introdução ao conceito.

## Intermediário

Aplicação prática.

## Avançado

Cenário de produção.

---

# Boas Práticas

Ao final de capítulos técnicos incluir seção:

## Boas Práticas

Com recomendações objetivas.

---

# Erros Comuns

Sempre incluir seção:

## Erros Comuns

Apresentando problemas frequentes encontrados em projetos reais.

---

# Estudos de Caso

Todos os estudos de caso devem utilizar a empresa fictícia:

**DataRetail S.A.**

Evitar criar novos cenários fictícios.

---

# Laboratórios

Os laboratórios devem seguir a estrutura:

1. Objetivo
2. Cenário
3. Pré-requisitos
4. Ambiente
5. Passo a passo
6. Validação
7. Resultado esperado
8. Desafios adicionais

---

# Referências

Prioridade das fontes:

1. Documentação oficial
2. RFCs
3. Livros
4. White Papers
5. Artigos técnicos
6. Publicações acadêmicas

Evitar referências sem autoria identificada.

---

# Emojis

Não utilizar emojis em títulos.

Emojis podem ser utilizados apenas em dashboards, índices ou páginas de navegação, quando melhorarem a experiência do leitor.

---

# Linguagem

Evitar:

* "simplesmente"
* "obviamente"
* "é fácil perceber"
* "como todos sabem"
* "basta"

Essas expressões presumem conhecimento prévio do leitor.

---

# Consistência

Sempre utilizar a mesma nomenclatura ao longo de toda a coleção.

Se um conceito foi denominado "Data Lake", nunca alternar para "Lago de Dados" em outro capítulo.

---

# Revisão Final

Antes de concluir qualquer documento verificar:

* ortografia;
* gramática;
* consistência técnica;
* nomenclatura;
* títulos;
* Wikilinks;
* diagramas;
* exemplos;
* YAML Frontmatter;
* referências.

---

# Princípio Final

O leitor deve conseguir abrir qualquer capítulo da coleção e reconhecer imediatamente que ele pertence à mesma obra.

A consistência de estilo é considerada um requisito técnico do projeto e deve ser preservada em todas as futuras contribuições.
