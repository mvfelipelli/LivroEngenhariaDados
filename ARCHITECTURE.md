# ARCHITECTURE.md

## Arquitetura do Projeto

## Formação em Engenharia de Dados

---

## Objetivo

Este documento descreve a arquitetura da **Formação em Engenharia de Dados**.

Seu propósito é explicar como o conhecimento está organizado, quais decisões estruturais foram adotadas e quais princípios devem ser preservados durante a evolução do projeto.

Este documento é destinado tanto a colaboradores humanos quanto a agentes de Inteligência Artificial.

---

## Visão Geral

O projeto foi concebido como um **Vault do Obsidian**, funcionando simultaneamente como:

* livro técnico;
* wiki;
* base de conhecimento;
* ambiente de estudos;
* laboratório prático;
* documentação permanente.

Toda a arquitetura foi desenhada para favorecer:

* descoberta de conhecimento;
* reutilização de conteúdo;
* navegação por Wikilinks;
* evolução incremental;
* manutenção de longo prazo.

---

## Princípios Arquiteturais

A arquitetura segue cinco princípios fundamentais.

## 1. Conhecimento Organizado

Todo conteúdo possui um local específico dentro do Vault.

Evita-se duplicação de informações.

---

## 2. Navegação por Relacionamentos

O principal mecanismo de navegação são os **Wikilinks**.

A estrutura de diretórios organiza o conteúdo.

Os Wikilinks conectam o conhecimento.

---

## 3. Modularidade

Cada módulo é independente.

Pode ser estudado isoladamente.

Ao mesmo tempo faz parte de uma coleção maior.

---

## 4. Evolução Contínua

Nenhum capítulo é considerado definitivo.

Novas versões podem expandir exemplos, referências e laboratórios mantendo compatibilidade com os capítulos existentes.

---

## 5. Neutralidade Tecnológica

A estrutura do projeto privilegia conceitos.

Ferramentas são apresentadas como implementações dos conceitos.

---

## Organização do Vault

A raiz do projeto possui a seguinte estrutura.

```text id="6trqwp"
.
├── .obsidian
├── 000-Atlas
├── 001-Dashboard
├── 005-Wiki
├── 010-Biblioteca
├── 020-Laboratorios
├── 030-Projetos
├── 040-Certificacoes
├── 050-Templates
├── 060-Assets
├── 070-Anotacoes
├── 080-Inbox
├── 090-Arquivados
├── 100-Volumes
├── 999-Arquivos-Temporarios
└── tools
```

Cada diretório possui uma responsabilidade única.

---

## Camadas da Arquitetura

A arquitetura pode ser entendida em cinco camadas.

```text id="hhkg7x"
Governança

↓

Navegação

↓

Conteúdo

↓

Laboratórios

↓

Recursos
```

---

## Camada de Governança

Define as regras do projeto.

Arquivos:

```text id="xom52o"
README.md

AGENTS.md

EDITORIAL.md

STYLE_GUIDE.md

ARCHITECTURE.md

ROADMAP.md

MEMORY.md

CHANGELOG.md
```

Esses documentos são considerados a fonte oficial de governança.

Todo agente de IA deve lê-los antes de produzir conteúdo.

---

## Camada de Navegação

Responsável pela descoberta do conhecimento.

Inclui:

```text id="d3lyl9"
000-Atlas

001-Dashboard

005-Wiki
```

Esses diretórios concentram mapas, índices e páginas de navegação.

Eles não devem duplicar conteúdo técnico existente nos volumes.

---

## Camada de Conteúdo

O conhecimento principal está localizado em:

```text id="6vtvfh"
100-Volumes
```

Cada volume aborda um domínio específico da Engenharia de Dados.

---

## Camada de Laboratórios

Responsável pelo conteúdo prático.

```text id="twx25v"
020-Laboratorios

030-Projetos
```

Laboratórios podem ser reutilizados por diversos volumes.

Projetos integradores evoluem ao longo da formação.

---

## Camada de Recursos

Inclui materiais auxiliares.

```text id="gfvdr9"
010-Biblioteca

050-Templates

060-Assets
```

Essa camada fornece suporte ao conteúdo principal.

---

## Organização dos Volumes

Cada volume representa um domínio de conhecimento.

Estrutura oficial:

```text id="09vxr4"
00-Introducao

01-Fundamentos

02-Linux

03-Git-e-GitHub

04-SQL

05-Modelagem-de-Dados

06-Python

07-Apache-Spark

08-PostgreSQL

09-Lakehouse

10-Trino

11-Apache-Airflow

12-Qualidade-de-Dados

13-Observabilidade

14-Streaming

15-Cloud

16-DataOps-e-DevOps

17-Arquiteturas-Avancadas

18-Projeto-Integrador
```

Volumes não devem conter conhecimento duplicado.

Quando necessário utilizar Wikilinks.

Essa lista corresponde aos diretórios vigentes em `100-Volumes`. Ela é a referência arquitetural para nomes e numeração.

---

## Organização dos Módulos

Cada módulo segue exatamente a mesma estrutura.

```text id="jlwmvn"
README.md

01-Objetivos

02-Introducao

...

10-Estudo-de-Caso

11-Resumo

12-Perguntas-de-Entrevista

13-Exercicios

13-Gabarito

14-Laboratorio

14-Solucao

15-Referencias
```

Essa estrutura é obrigatória.

---

## Fluxo de Conhecimento

Todo conceito deve evoluir da seguinte maneira.

```text id="zqgq2t"
Conceito

↓

Explicação

↓

Diagrama

↓

Exemplo

↓

Laboratório

↓

Projeto Integrador
```

Essa progressão deve ser preservada.

---

## Wikilinks

Os Wikilinks representam as conexões entre os conceitos.

Sempre que um conceito já existir:

Utilizar:

```text id="5yx8fj"
[[Apache Spark]]
```

Em vez de repetir a definição.

---

## Diagramas

Diagramas são considerados parte da arquitetura do conhecimento.

Sempre que possível utilizar Mermaid.

Cada diagrama deve explicar apenas um conceito.

---

## Projeto Integrador

Toda a coleção utiliza a empresa fictícia:

**DataRetail S.A.**

Ela representa o fio condutor dos estudos de caso, laboratórios e projetos.

Novos cenários fictícios devem ser evitados, salvo necessidade didática claramente justificada.

---

## Dependências entre Volumes

Os volumes possuem dependências conceituais.

```text id="5pvjau"
Introdução

↓

Fundamentos

↓

Linux

↓

Git e GitHub

↓

SQL

↓

Modelagem de Dados

↓

Python

↓

Apache Spark

↓

PostgreSQL

↓

Lakehouse → Trino → Apache Airflow

↓

Qualidade → Observabilidade → Streaming

↓

Cloud → DataOps e DevOps → Arquiteturas Avançadas

↓

Projeto Integrador
```

O ROADMAP detalha a sequência completa.

---

## Evolução da Arquitetura

A arquitetura deve evoluir preservando:

* compatibilidade com Wikilinks existentes;
* organização dos diretórios;
* padrão editorial;
* convenções de nomenclatura;
* identidade da coleção.

Mudanças estruturais devem ser excepcionais e documentadas.

---

## Responsabilidades dos Agentes

Antes de criar novos arquivos, um agente de IA deve:

1. Ler os documentos de governança.
2. Identificar o estado atual do projeto.
3. Localizar o ponto de continuidade.
4. Verificar a existência de conteúdo relacionado.
5. Atualizar índices quando necessário.
6. Preservar todos os Wikilinks existentes.

---

## Princípios de Evolução

Toda nova contribuição deve buscar:

* aumentar a qualidade técnica;
* evitar duplicação;
* fortalecer as conexões entre capítulos;
* ampliar laboratórios;
* enriquecer referências;
* melhorar a navegabilidade do Vault.

---

## Visão de Longo Prazo

A Formação em Engenharia de Dados não deve ser encarada como uma sequência linear de documentos.

Ela constitui uma **base de conhecimento viva**, continuamente expandida, navegável por relacionamentos e preparada para ser utilizada por estudantes, profissionais e agentes de Inteligência Artificial.

A arquitetura do projeto existe para garantir que essa evolução permaneça organizada, consistente e sustentável ao longo dos anos.
