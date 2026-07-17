# MEMORY.md

## Memória do Projeto

## Formação em Engenharia de Dados

> Este documento representa o estado atual do projeto e funciona como a memória permanente da coleção. Deve ser atualizado sempre que um marco importante for alcançado, um módulo for concluído ou uma decisão arquitetural relevante for tomada.

---

## Objetivo

A **Formação em Engenharia de Dados** é um projeto de longo prazo que tem como objetivo construir uma academia completa de Engenharia de Dados em português, organizada como um Vault do Obsidian.

O projeto combina:

* Livro técnico
* Wiki
* Base de conhecimento
* Laboratórios
* Projetos integradores
* Material para certificações
* Documentação permanente

Todo o conteúdo é produzido seguindo padrões editoriais definidos em `EDITORIAL.md`.

---

## Visão de Longo Prazo

Ao final da coleção, o estudante deverá ser capaz de atuar como Engenheiro de Dados pleno ou sênior, dominando:

* Fundamentos
* Linux
* SQL
* Modelagem de Dados
* Bancos de Dados
* Data Warehouse
* Data Lake
* Lakehouse
* Apache Spark
* Streaming
* Kafka
* Airflow
* dbt
* Cloud Computing
* DataOps
* Arquitetura de Dados
* Engenharia de Machine Learning

A coleção deverá funcionar como referência permanente para consulta profissional.

---

## Estrutura do Vault

A estrutura oficial do projeto é composta pelos seguintes diretórios:

```text
.obsidian
000-Atlas
001-Dashboard
005-Wiki
010-Biblioteca
020-Laboratorios
030-Projetos
040-Certificacoes
050-Templates
060-Assets
070-Anotacoes
080-Inbox
090-Arquivados
100-Volumes
999-Arquivos-Temporarios
tools
```

Essa estrutura é considerada estável.

Alterações estruturais devem ser registradas no `CHANGELOG.md`.

Os diretórios existentes em `100-Volumes`, numerados de `00-Introducao` a `18-Projeto-Integrador`, são a fonte oficial para a sequência, a numeração e os nomes dos volumes. O `ROADMAP.md` deve sempre refletir essa estrutura.

---

## Projeto Integrador

Toda a coleção utiliza um único cenário de negócio.

Empresa:

**DataRetail S.A.**

Todos os exemplos, laboratórios e estudos de caso utilizam essa empresa fictícia para garantir continuidade entre os volumes.

---

## Padrão Editorial

O projeto adota os seguintes padrões permanentes:

* Obsidian First
* YAML Frontmatter
* Wikilinks
* Mermaid
* Callouts
* Markdown compatível com Obsidian
* Conteúdo orientado a fundamentos
* Linguagem técnica em Português do Brasil

---

## Estrutura Padrão dos Módulos

Todos os módulos seguem exatamente a mesma organização.

```text
README.md

01-Objetivos.md

02-Introducao.md

03...

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

Essa estrutura não deve ser modificada sem decisão explícita.

---

## Convenções Permanentes

As seguintes decisões fazem parte da arquitetura do projeto.

## Conteúdo

* Conceitos antes de ferramentas.
* Progressão do simples para o complexo.
* Exemplos executáveis.
* Laboratórios reproduzíveis.
* Referências oficiais.

---

## Navegação

A navegação principal utiliza:

* Wikilinks
* Índices
* Dashboards
* Atlas
* Backlinks do Obsidian

---

## Diagramas

Sempre utilizar Mermaid quando possível.

Evitar imagens para representar conceitos que possam ser descritos por diagramas textuais.

---

## Estado Atual

## Governança

Status:

🚧 Em implantação

Documentos existentes ou planejados:

* ✅ README.md
* ✅ AGENTS.md
* ✅ EDITORIAL.md
* ✅ STYLE_GUIDE.md
* ✅ ARCHITECTURE.md
* 🚧 ROADMAP.md
* ⏳ MEMORY.md
* ⏳ CHANGELOG.md

---

## Conteúdo

### Volume 00 — Introdução

Status:

🚧 Em desenvolvimento

O volume possui dez módulos estruturados. Há conteúdo parcial, especialmente em `01-O-que-e-Engenharia-de-Dados`; portanto, ele não deve ser classificado como não iniciado.

---

### Volume 01 — Fundamentos

Status:

✅ Concluído

#### Módulo 01 — Dados

Status:

✅ Concluído

#### Módulo 02 — Ciclo de Vida dos Dados

Status:

✅ Concluído

O módulo possui todos os capítulos técnicos e componentes obrigatórios concluídos.

#### Módulo 03 — Bancos de Dados

Status:

✅ Concluído

O módulo possui fundamentos, arquitetura interna, transações, concorrência, recuperação, índices, estudo de caso, exercícios e laboratório reproduzível com SQLite.

#### Módulo 04 — Modelagem

Status:

✅ Concluído

O módulo possui modelagem conceitual, lógica, física, relacional e analítica, normalização, evolução, estudo de caso e laboratório reproduzível.

#### Módulo 05 — ETL

Status:

✅ Concluído

O módulo possui extração, transformação, carga, incrementalidade, CDC, confiabilidade, testes, operação e laboratório reproduzível.

#### Módulo 06 — ELT

Status:

✅ Concluído

O módulo possui raw, staging, marts, SQL modular, materializações, testes, linhagem, governança e laboratório reproduzível.

#### Módulo 07 — Pipelines

Status:

✅ Concluído

O módulo possui DAGs, batch, streaming, orquestração, backfill, estado, idempotência, observabilidade, SLOs e laboratório reproduzível.

#### Módulo 08 — Arquiteturas

Status:

✅ Concluído

O módulo possui requisitos, trade-offs, estilos, eventos, Warehouse, Lake, Lakehouse, Data Mesh, Data Fabric, ADRs e laboratório reproduzível.

#### Módulo 09 — Qualidade

Status:

✅ Concluído

O módulo possui dimensões, profiling, contratos, testes, quality gates, SLOs, incidentes, responsabilidades e laboratório reproduzível.

#### Módulo 10 — Governança

Status:

✅ Concluído

O módulo possui princípios, modelo operacional, papéis, políticas, metadados, catálogo, linhagem, privacidade, retenção e laboratório reproduzível.

#### Módulo 11 — Observabilidade

Status:

✅ Concluído

O módulo possui logs, métricas, traces, saúde dos dados, linhagem operacional, SLOs, incidentes, runbooks e laboratório reproduzível.

#### Módulo 12 — Conceitos Modernos

Status:

✅ Concluído

O módulo possui produtos de dados, contratos, plataforma self-service, arquitetura evolutiva, Mesh, Fabric, Lakehouse, DataOps, FinOps, IA e laboratório reproduzível.

O Volume 01 — Fundamentos está concluído. O próximo trabalho é estruturar e iniciar o Volume 02 — Linux.

---

### Volume 02 — Linux

Status:

🚧 Em desenvolvimento

#### Módulo 01 — Fundamentos do Linux

Status:

✅ Concluído

O módulo possui arquitetura do sistema, filesystem, permissões, processos, serviços, terminal, pipes, segurança e laboratório Bash reproduzível.

#### Módulo 02 — Administração do Sistema Linux

Status:

✅ Concluído

O módulo possui pacotes, systemd, armazenamento, mounts, rede, logs, backup, capacidade, hardening e laboratório Bash reproduzível.

#### Módulo 03 — Shell Script e Automação

Status:

✅ Concluído

O módulo possui linguagem Bash, expansões, funções, tratamento de erros, idempotência, testes, segurança, operação e laboratório de ingestão reproduzível.

#### Módulo 04 — Redes e Conectividade no Linux

Status:

✅ Concluído

O módulo possui camadas, enlace, IP, roteamento, TCP, UDP, DNS, namespaces, firewall, diagnóstico e laboratório local reproduzível.

#### Módulo 05 — Contêineres e Isolamento no Linux

Status:

✅ Concluído

O módulo possui namespaces, cgroups, imagens OCI, runtimes, volumes, redes, segurança, supply chain e laboratório determinístico.

#### Módulo 06 — Desempenho, Troubleshooting e Observabilidade Linux

Status:

✅ Concluído

O módulo possui métodos USE e RED, CPU, memória, I/O, processos, profiling, tracing, incidentes, capacidade e laboratório reproduzível.

#### Módulo 07 — Segurança e Hardening Linux

Status:

✅ Concluído

O módulo possui risco, baselines, identidade, permissões, kernel, rede, criptografia, auditoria, incidentes e laboratório reproduzível.

#### Módulo 08 — Operação de Plataformas de Dados no Linux

Status:

✅ Concluído

O módulo integra SLOs, implantação, estado, backup, automação, observabilidade, incidentes, DR, capacidade e laboratório de prontidão.

O Volume 02 — Linux está concluído.

---

### Volume 03 — Git e GitHub

Status:

✅ Concluído

#### Módulo 01 — Fundamentos do Git

Status:

✅ Concluído

O módulo possui modelo distribuído, objetos, estados, branches, merges, remotos, recuperação, workflows e laboratório Git reproduzível.

#### Módulo 02 — Branches, Colaboração e GitHub

Status:

✅ Concluído

O módulo possui modelos colaborativos, estratégias de branch, pull requests, revisão, rulesets, CODEOWNERS, releases, segurança e laboratório distribuído.

#### Módulo 03 — GitHub Actions e CI/CD

Status:

✅ Concluído

O módulo possui workflows, runners, matrizes, cache, artefatos, OIDC, ambientes, CI, deploy, reuso, supply chain e laboratório reproduzível.

#### Módulo 04 — Releases, Versionamento e GitOps

Status:

✅ Concluído

O módulo possui SemVer, tags, releases, changelog, artefatos imutáveis, proveniência, promoção, rollback, reconciliação, drift, segurança e laboratório reproduzível.

O Volume 03 — Git e GitHub está concluído. O próximo trabalho é estruturar e iniciar o Volume 04 — SQL.

---

### Volume 04 — SQL

Status:

🚧 Em desenvolvimento

#### Módulo 01 — Fundamentos de SQL e Modelo Relacional

Status:

✅ Concluído

O módulo possui natureza declarativa, padrão SQL, modelo relacional, schemas, tipos, chaves, constraints, consultas fundamentais, lógica de `NULL`, joins, agregações e laboratório SQLite reproduzível.

#### Módulo 02 — Consultas, Joins e Subconsultas

Status:

✅ Concluído

O módulo possui grão, cardinalidade, joins internos e externos, semi-join, anti-join, fanout, subconsultas, conjuntos, CTEs, recursão e laboratório SQLite reproduzível.

#### Módulo 03 — Agregações, Funções de Janela e Análise

Status:

✅ Concluído

O módulo possui agregações, agrupamentos, métricas condicionais, rankings, partições, frames, comparações temporais, acumulados, médias móveis e laboratório SQLite reproduzível.

#### Módulo 04 — DML, Transações e Concorrência

Status:

✅ Concluído

O módulo possui mutações, upsert, idempotência, ACID, savepoints, isolamento, anomalias, MVCC, locks, deadlocks, retries, outbox e laboratório SQLite reproduzível.

#### Módulo 05 — DDL, Schemas e Evolução de Estruturas

Status:

✅ Concluído

O módulo possui objetos, schemas, tipos, constraints, dependências, locks de DDL, expand-contract, backfill, migrações versionadas e laboratório SQLite reproduzível.

#### Módulo 06 — Planos de Execução, Índices e Otimização

Status:

✅ Concluído

O módulo possui planos lógicos e físicos, cardinalidade, estatísticas, operadores, índices, algoritmos de join, EXPLAIN ANALYZE, SARGabilidade e laboratório SQLite reproduzível.

#### Módulo 07 — Views, Segurança e Governança SQL

Status:

✅ Concluído

O módulo possui views comuns e materializadas, roles, grants, ownership, menor privilégio, RLS, mascaramento, prevenção de SQL injection, auditoria, lineage e laboratório SQLite reproduzível.

#### Módulo 08 — SQL em Pipelines e Plataformas Analíticas

Status:

✅ Concluído

O módulo possui contratos de pipeline, staging, incrementalidade, watermarks, dados atrasados, deduplicação, upsert, modelagem dimensional, ELT, warehouses distribuídos e laboratório SQLite reproduzível.

#### Módulo 09 — Dados Temporais e Semiestruturados em SQL

Status:

✅ Concluído

O módulo possui instantes, timezones, intervalos, consultas as of, bitemporalidade, JSON, arrays, indexação, evolução de payload e laboratório SQLite reproduzível.

#### Módulo 10 — Testes, Qualidade e Observabilidade SQL

Status:

✅ Concluído

O módulo possui estratégia de testes, fixtures, constraints, contratos, reconciliação, propriedades, anomalias, métricas, SLOs e laboratório SQLite reproduzível.

O Volume 04 — SQL está concluído.

### Volume 05 — Modelagem de Dados

#### Módulo 01 — Fundamentos e Níveis de Modelagem

Status:

✅ Concluído

O módulo possui domínio, semântica, entidades, identidade, relacionamentos, níveis conceitual/lógico/físico, grão, cardinalidade, invariantes e laboratório SQLite reproduzível.

#### Módulo 02 — Modelagem Conceitual e Entidade-Relacionamento

Status:

✅ Concluído

O módulo possui entidades fortes e fracas, atributos, relacionamentos, cardinalidade, entidades associativas, hierarquias, notações e laboratório SQLite reproduzível.

O próximo trabalho é concluir o Módulo 03 — Modelagem Lógica Relacional e Normalização.

---

## Próximo Marco

Estruturar e iniciar:

**Volume 05 — Modelagem de Dados**

**Módulo 03 — Modelagem Lógica Relacional e Normalização**

Após sua conclusão:

1. Atualizar esta memória.
2. Atualizar o ROADMAP.
3. Registrar a entrega no CHANGELOG.
4. Iniciar o próximo módulo previsto.

---

## Decisões Arquiteturais

Até o momento foram adotadas as seguintes decisões permanentes.

## Organização

O projeto utiliza uma estrutura baseada em Volumes → Módulos → Capítulos.

A estrutura física de `100-Volumes` foi consolidada como referência oficial. Documentos de governança não devem propor sequências conflitantes com os diretórios existentes.

---

## Plataforma

O Obsidian é considerado a plataforma oficial de navegação e organização do conhecimento.

---

## Inteligência Artificial

O projeto foi estruturado para permitir colaboração entre autores humanos e agentes de IA.

Os agentes devem utilizar como contexto principal:

1. README.md
2. AGENTS.md
3. EDITORIAL.md
4. STYLE_GUIDE.md
5. ARCHITECTURE.md
6. ROADMAP.md
7. MEMORY.md

---

## Versionamento

Todo o projeto é mantido em um repositório Git.

Mudanças relevantes devem ser registradas no `CHANGELOG.md`.

---

## Regras para Atualização

Este documento deve ser atualizado quando ocorrer qualquer um dos eventos abaixo.

* Conclusão de um módulo.
* Criação de um novo volume.
* Alteração estrutural do Vault.
* Mudança no padrão editorial.
* Inclusão de novas convenções permanentes.
* Mudança no roteiro oficial da coleção.

Evitar registrar eventos pequenos ou alterações rotineiras.

---

## Continuidade para Agentes de IA

Antes de produzir qualquer novo conteúdo, um agente deve seguir a sequência abaixo.

1. Ler `README.md`.
2. Ler `AGENTS.md`.
3. Ler `EDITORIAL.md`.
4. Ler `STYLE_GUIDE.md`.
5. Ler `ARCHITECTURE.md`.
6. Ler `ROADMAP.md`.
7. Ler este documento (`MEMORY.md`).
8. Localizar o último módulo concluído.
9. Identificar o próximo arquivo a ser criado.
10. Continuar exatamente desse ponto.

Nunca reiniciar módulos já concluídos.

Nunca alterar a estrutura da coleção sem autorização explícita.

---

## Visão de Futuro

Este documento existe para preservar a continuidade do projeto ao longo dos anos.

Seu objetivo é garantir que qualquer colaborador — humano ou agente de Inteligência Artificial — consiga compreender rapidamente o estado atual da coleção, as decisões tomadas e o próximo passo a ser executado.

A memória do projeto deve representar sempre a verdade sobre o estado da coleção e servir como a principal referência para sua evolução contínua.
