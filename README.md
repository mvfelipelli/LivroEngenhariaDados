# Engenharia de Dados

## Academia Completa de Engenharia de Dados em Português

> Um projeto open source para construir uma formação completa em Engenharia de Dados utilizando **Obsidian** como plataforma de conhecimento.

---

# Objetivo

Este projeto tem como objetivo construir uma **Academia de Engenharia de Dados** inteiramente em português, organizada como um Vault do Obsidian e estruturada como uma combinação de:

* Livro técnico
* Wiki
* Base de conhecimento
* Material para estudos
* Laboratórios práticos
* Projetos integradores
* Guia para certificações
* Repositório permanente de consulta

O conteúdo foi projetado para evoluir continuamente, permitindo que um estudante percorra desde os fundamentos até tópicos avançados da Engenharia de Dados.

---

# Filosofia do Projeto

Este projeto segue alguns princípios fundamentais.

## Aprendizado por fundamentos

O foco não é ensinar ferramentas específicas, mas os conceitos que permanecem válidos independentemente da tecnologia utilizada.

Ferramentas mudam.

Fundamentos permanecem.

---

## Vendor Neutral

Sempre que possível o conteúdo é independente de fornecedor.

Os conceitos são apresentados antes da implementação em ferramentas como:

* PostgreSQL
* SQL Server
* Oracle
* MySQL
* Hive
* Spark
* Trino
* Kafka
* Airflow
* dbt
* Databricks
* Snowflake
* AWS
* Azure
* Google Cloud

---

## Hands-on

Todo conceito importante possui atividades práticas.

Cada módulo contém:

* exemplos
* exercícios
* estudos de caso
* laboratórios
* projeto integrador

---

## Obsidian First

Todo o projeto é desenvolvido pensando no Obsidian.

São utilizados recursos como:

* Wikilinks
* Tags
* Callouts
* Mermaid
* Canvas
* Templates
* Backlinks

---

# Público-Alvo

Esta formação foi planejada para:

* iniciantes em Engenharia de Dados
* analistas de dados
* desenvolvedores
* DBAs
* cientistas de dados
* arquitetos de dados
* profissionais de BI
* estudantes
* profissionais em transição de carreira

---

# Estrutura do Projeto

O Vault é organizado da seguinte forma:

```text
000-Atlas/
001-Dashboard/
005-Wiki/

010-Biblioteca/
020-Laboratorios/
030-Projetos/
040-Certificacoes/

050-Templates/
060-Assets/
070-Anotacoes/
080-Inbox/
090-Arquivados/

100-Volumes/

999-Arquivos-Temporarios/

tools/
```

---

# Organização dos Volumes

Cada volume representa um grande domínio da Engenharia de Dados.

Exemplo:

```
100-Volumes/

00-Introducao

01-Fundamentos

02-Linux

03-SQL

04-Modelagem

05-Bancos-de-Dados

06-Data-Warehouse

...

20-Projeto-Final
```

Cada volume é dividido em módulos.

Cada módulo possui uma estrutura padronizada.

---

# Estrutura dos Módulos

Todos os módulos seguem exatamente a mesma organização.

```
README.md

01-Objetivos.md

02-Introducao.md

03...

04...

...

10-Estudo-de-Caso.md

11-Resumo.md

12-Perguntas-de-Entrevista.md

13-Exercicios.md

13-Gabarito.md

14-Laboratorio.md

14-Solucao.md

15-Referencias.md
```

Essa padronização permite uma experiência consistente durante toda a formação.

---

# Padrão Editorial

Todos os documentos seguem um padrão único.

Incluindo:

* YAML Frontmatter
* Wikilinks
* Mermaid
* Callouts
* Diagramas
* Tabelas
* Exemplos práticos
* Estudos de caso
* Exercícios
* Laboratórios

As regras completas encontram-se em:

* `EDITORIAL.md`

---

# Projeto Integrador

Durante toda a formação será utilizada uma empresa fictícia:

**DataRetail S.A.**

Todos os exemplos, estudos de caso, pipelines, bancos de dados e laboratórios serão desenvolvidos utilizando esse cenário, permitindo que o estudante acompanhe a evolução de um projeto real ao longo de toda a formação.

---

# Inteligência Artificial

Este projeto foi desenvolvido para funcionar em conjunto com agentes de IA.

O repositório possui documentação específica para orientar ferramentas como:

* OpenAI Codex
* ChatGPT
* Claude
* Gemini
* GitHub Copilot
* outros agentes compatíveis

As instruções encontram-se em:

* `AGENTS.md`
* `EDITORIAL.md`
* `MEMORY.md`

---

# Roadmap

O planejamento completo da formação está disponível em:

```
ROADMAP.md
```

Nele encontram-se:

* volumes planejados
* módulos
* progresso
* próximas entregas

---

# Estado Atual

O estado atual do projeto encontra-se em:

```
MEMORY.md
```

Esse documento registra:

* decisões arquiteturais
* convenções
* módulos concluídos
* próximos módulos
* histórico do projeto

---

# Como Utilizar

Clone o repositório:

```bash
git clone git@github.com:mvfelipelli/LivroEngenhariaDados.git
```

Abra a pasta diretamente no Obsidian.

Toda a navegação foi planejada para utilizar backlinks, wikilinks e gráficos de conhecimento.

---

# Contribuições

Contribuições são bem-vindas.

Antes de enviar alterações, recomenda-se:

* ler `AGENTS.md`;
* seguir `EDITORIAL.md`;
* manter o padrão de nomenclatura;
* preservar os Wikilinks;
* evitar duplicação de conteúdo;
* atualizar o `CHANGELOG.md` quando aplicável.

---

# Tecnologias Utilizadas

Entre as tecnologias abordadas ao longo da formação estão:

* SQL
* PostgreSQL
* Spark
* Hive
* Trino
* Kafka
* Airflow
* dbt
* Docker
* Linux
* Python
* Git
* MinIO
* Iceberg
* Delta Lake
* Parquet
* ORC
* Avro
* Cloud Computing
* Data Warehouse
* Data Lakehouse
* Data Mesh
* Data Fabric

---

# Licença

Este projeto é disponibilizado para fins educacionais.

A definição da licença oficial será publicada em versões futuras do repositório.

---

# Autor

**Marcello Felipelli**

Engenheiro de Dados • Arquiteto de Dados • Especialista em Analytics

LinkedIn:

https://www.linkedin.com/in/marcellofelipelli/

---

> **Missão:** construir a mais completa formação aberta em Engenharia de Dados em português, organizada como um livro técnico vivo, continuamente evoluído e suportado por Inteligência Artificial.
