---
title: Guia Editorial da Academia de Engenharia de Dados
aliases:
  - Guia Editorial
  - Padrão Editorial
type: guide
status: Oficial
version: 1.0
---

# Guia Editorial da Academia de Engenharia de Dados

> [!quote]
> "Consistência é mais importante do que velocidade. Um capítulo excelente vale mais do que dez capítulos inconsistentes."

---

# Objetivo

Este documento define os padrões editoriais utilizados em toda a Academia de Engenharia de Dados.

Seu objetivo é garantir:

- consistência;
- organização;
- navegabilidade;
- reutilização do conteúdo;
- facilidade de manutenção;
- compatibilidade com Obsidian.

Todo novo conteúdo deverá seguir este guia.

---

# Filosofia da Academia

A Academia foi construída sobre cinco pilares.

## 1. Fundamentos antes de ferramentas

Tecnologias mudam.

Princípios permanecem.

Sempre ensinaremos primeiro o conceito e somente depois a ferramenta.

---

## 2. Obsidian First

Todo o conteúdo é pensado para funcionar como uma Wiki.

Utilizamos:

- Wikilinks
- Backlinks
- MOCs
- Mermaid
- Callouts

---

## 3. Aprendizado progressivo

Cada volume reutiliza conceitos anteriores.

Nada é apresentado isoladamente.

---

## 4. Prática contínua

Todo conceito importante deve possuir:

- exemplo;
- laboratório;
- aplicação no Projeto Integrador.

---

## 5. Pensamento arquitetural

O objetivo não é ensinar ferramentas.

O objetivo é ensinar como tomar decisões.

---

# Estrutura da Academia

```text
Engenharia de Dados/

000-Atlas/

020-Laboratorios/

030-Projetos/

040-Certificacoes/

00-Introducao/

01-Fundamentos/

...

18-Projeto-Integrador/

050-Templates/

tools/
```

---

# Estrutura obrigatória de um capítulo

Todo capítulo deverá seguir esta ordem.

```text
Frontmatter

Navegação

Título

Citação

Visão Geral

Objetivos

Mapa do capítulo

Conteúdo

Diagramas

Exemplos

Estudo de Caso

Boas práticas

Erros comuns

Resumo

Conceitos-chave

Perguntas de entrevista

Exercícios

Leituras recomendadas

Veja também

Navegação
```

---

# Frontmatter

Todo capítulo utilizará YAML.

Exemplo.

```yaml
---
title:
aliases:
volume:
chapter:
section:
type:
status:
tags:
---
```

---

# Títulos

Utilizar sempre:

```markdown
# Nome do Capítulo
```

Nunca iniciar diretamente pelo texto.

---

# Visão Geral

Todo capítulo começa explicando:

- por que o assunto existe;
- onde ele será utilizado;
- relação com capítulos anteriores.

---

# Objetivos

Devem utilizar verbos observáveis.

Exemplos:

- compreender;
- implementar;
- comparar;
- analisar;
- construir;
- avaliar.

Evitar:

- conhecer um pouco;
- aprender sobre;
- entender melhor.

---

# Mapa do capítulo

Sempre apresentar os tópicos.

Exemplo.

```markdown
# 🗺️ Mapa do capítulo

1.

2.

3.
```

---

# Diagramas

Utilizar Mermaid compatível com Obsidian.

Priorizar:

- flowchart
- sequenceDiagram
- classDiagram
- erDiagram
- stateDiagram
- mindmap

Evitar recursos experimentais.

---

# Wikilinks

Sempre utilizar.

Exemplo.

```markdown
[[Apache Spark]]

[[Data Lake]]

[[Pipeline de Dados]]
```

Nunca utilizar texto simples quando existir uma nota correspondente.

---

# Callouts

Padronização oficial.

## Informação

```markdown
> [!info]
```

---

## Dica

```markdown
> [!tip]
```

---

## Importante

```markdown
> [!important]
```

---

## Atenção

```markdown
> [!warning]
```

---

## Exemplo

```markdown
> [!example]
```

---

## Resumo

```markdown
> [!summary]
```

---

## Exercício

```markdown
> [!question]
```

---

# Estudo de Caso

Sempre utilizar a empresa:

**DataRetail S.A.**

Ela evoluirá durante toda a Academia.

---

# Decisões Arquiteturais

Sempre que possível incluir.

Formato oficial.

```markdown
## 🏗️ Decisão de Arquitetura

Situação

Alternativas

Análise

Decisão

Consequências
```

---

# Comparações

Sempre utilizar tabelas.

Exemplo.

| Item | A | B |
|------|---|---|

---

# Código

Sempre utilizar blocos Markdown.

Nunca imagens de código.

---

# Laboratórios

Os laboratórios não ficarão dentro dos capítulos.

Serão referenciados.

Exemplo.

```markdown
[[Lab 012 - Apache Spark]]
```

---

# Projeto Integrador

Todo capítulo deverá indicar quando impactar o Projeto Integrador.

Utilizar.

```markdown
> [!success]
>
> Este conhecimento será aplicado no Projeto Integrador.
```

---

# Glossário

Sempre que surgir um conceito novo.

Criar um Wikilink.

Exemplo.

```markdown
[[Parquet]]

[[Apache Iceberg]]
```

Posteriormente será criada a nota correspondente.

---

# Mermaid

Preferir diagramas simples.

Pouco texto.

Sem cruzamentos desnecessários.

---

# Imagens

Preferencialmente SVG.

Caso contrário PNG.

Nome:

```text
figura-01.png
```

---

# Exercícios

Misturar:

- conceituais;
- arquitetura;
- implementação;
- pesquisa;
- estudo de caso.

---

# Perguntas de entrevista

Todo capítulo deverá possuir entre 5 e 15 perguntas.

---

# Leituras recomendadas

Priorizar:

- documentação oficial;
- livros clássicos;
- artigos acadêmicos.

---

# Nome dos arquivos

Utilizar.

```text
01 - Nome.md
```

Sempre dois dígitos.

---

# Convenção para laboratórios

```text
Lab 001

Lab 002

Lab 003
```

---

# Convenção para estudos de caso

Sempre:

```text
DataRetail S.A.
```

---

# Convenção para diagramas

Todo diagrama deve responder uma pergunta.

Nunca inserir diagramas apenas para preencher espaço.

---

# Revisão editorial

Antes de concluir um volume verificar:

- ortografia;
- Mermaid;
- Wikilinks;
- links quebrados;
- glossário;
- navegação;
- consistência.

---

# Definição de pronto

Um capítulo somente é considerado concluído quando:

- está consistente;
- possui exemplos;
- possui diagramas;
- possui estudo de caso;
- possui exercícios;
- possui perguntas de entrevista;
- possui resumo;
- possui conceitos-chave;
- possui navegação;
- possui Wikilinks válidos.

---

# Missão da Academia

A Academia de Engenharia de Dados tem como objetivo formar profissionais capazes de compreender, projetar, implementar e operar plataformas modernas de dados.

Mais do que ensinar ferramentas, busca desenvolver pensamento crítico, capacidade de tomada de decisão e visão arquitetural.

Todo conteúdo deverá contribuir para esse objetivo.
