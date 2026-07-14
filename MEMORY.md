# MEMORY.md

# Memória do Projeto

## Formação em Engenharia de Dados

> Este documento representa o estado atual do projeto e funciona como a memória permanente da coleção. Deve ser atualizado sempre que um marco importante for alcançado, um módulo for concluído ou uma decisão arquitetural relevante for tomada.

---

# Objetivo

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

# Visão de Longo Prazo

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

# Estrutura do Vault

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

---

# Projeto Integrador

Toda a coleção utiliza um único cenário de negócio.

Empresa:

**DataRetail S.A.**

Todos os exemplos, laboratórios e estudos de caso utilizam essa empresa fictícia para garantir continuidade entre os volumes.

---

# Padrão Editorial

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

# Estrutura Padrão dos Módulos

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

# Convenções Permanentes

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

# Estado Atual

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

### Volume 00

Status:

⏳ Planejado

---

### Volume 01 — Fundamentos

Status:

🚧 Em desenvolvimento

#### Módulo 01 — Dados

Status:

✅ Concluído

#### Módulo 02 — Ciclo de Vida dos Dados

Status:

🚧 Em desenvolvimento

Os capítulos iniciais já foram produzidos.

O módulo ainda não foi concluído.

---

# Próximo Marco

Concluir integralmente:

**Volume 01 — Fundamentos**

**Módulo 02 — Ciclo de Vida dos Dados**

Após sua conclusão:

1. Atualizar esta memória.
2. Atualizar o ROADMAP.
3. Registrar a entrega no CHANGELOG.
4. Iniciar o próximo módulo previsto.

---

# Decisões Arquiteturais

Até o momento foram adotadas as seguintes decisões permanentes.

## Organização

O projeto utiliza uma estrutura baseada em Volumes → Módulos → Capítulos.

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

# Regras para Atualização

Este documento deve ser atualizado quando ocorrer qualquer um dos eventos abaixo.

* Conclusão de um módulo.
* Criação de um novo volume.
* Alteração estrutural do Vault.
* Mudança no padrão editorial.
* Inclusão de novas convenções permanentes.
* Mudança no roteiro oficial da coleção.

Evitar registrar eventos pequenos ou alterações rotineiras.

---

# Continuidade para Agentes de IA

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

# Visão de Futuro

Este documento existe para preservar a continuidade do projeto ao longo dos anos.

Seu objetivo é garantir que qualquer colaborador — humano ou agente de Inteligência Artificial — consiga compreender rapidamente o estado atual da coleção, as decisões tomadas e o próximo passo a ser executado.

A memória do projeto deve representar sempre a verdade sobre o estado da coleção e servir como a principal referência para sua evolução contínua.

