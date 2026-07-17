# CHANGELOG

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue o padrão **Keep a Changelog** e utiliza **Semantic Versioning**.

* [Keep a Changelog](https://keepachangelog.com/)
* [Semantic Versioning](https://semver.org/)

---

## Tipos de alteração

As alterações são classificadas nas seguintes categorias:

* **Added** — novos recursos
* **Changed** — alterações em funcionalidades existentes
* **Deprecated** — funcionalidades que serão removidas
* **Removed** — funcionalidades removidas
* **Fixed** — correções
* **Security** — melhorias de segurança

---

## [Unreleased]

### Added

* Módulo 09 do Volume 04 desenvolvido com tempo, validade, bitemporalidade, JSON e arrays.
* Estudo de caso, revisão, exercícios, gabarito e referências temporais e semiestruturadas adicionados.
* Laboratório reproduzível de consulta as of e expansão de JSON adicionado e validado.
* Módulo 08 do Volume 04 desenvolvido com staging, incrementalidade, idempotência, dimensional e ELT.
* Estudo de caso, revisão, exercícios, gabarito e referências de pipelines analíticos adicionados.
* Laboratório reproduzível de carga incremental com versão, upsert e watermark adicionado e validado.
* Módulo 07 do Volume 04 desenvolvido com views, roles, menor privilégio, RLS, privacidade e auditoria.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de segurança SQL adicionados.
* Laboratório reproduzível de view mínima, autorização e consulta parametrizada adicionado e validado.
* Módulo 06 do Volume 04 desenvolvido com planos, estatísticas, operadores, índices e algoritmos de join.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de otimização adicionados.
* Laboratório reproduzível de comparação de planos antes e depois da indexação adicionado e validado.
* Módulo 05 do Volume 04 desenvolvido com DDL, constraints, dependências e evolução de schema.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de migrações adicionados.
* Laboratório reproduzível de expand-contract e reconstrução de tabela adicionado e validado.
* Módulo 04 do Volume 04 desenvolvido com DML, transações, isolamento, locks, retries e outbox.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de concorrência adicionados.
* Laboratório reproduzível de transferência atômica e evento idempotente adicionado e validado.
* Módulo 03 do Volume 04 desenvolvido com agregações, rankings, frames, comparações e acumulados.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de análise SQL adicionados.
* Laboratório reproduzível de métricas e funções de janela adicionado e validado.
* Módulo 02 do Volume 04 desenvolvido com cardinalidade, joins, subconsultas, conjuntos, CTEs e recursão.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de consultas compostas adicionados.
* Laboratório reproduzível de composição sem fanout e anti-join adicionado e validado.
* Volume 04 — SQL iniciado com índice e identidade editorial.
* Módulo 01 desenvolvido com padrão SQL, modelo relacional, schemas, constraints e consultas fundamentais.
* Estudo de caso, revisão, exercícios, gabarito, referências e laboratório SQLite reproduzível adicionados.
* Módulo 04 do Volume 03 desenvolvido com SemVer, releases, artefatos, promoção, rollback e GitOps.
* Estudo de caso, revisão, exercícios, gabarito e referências oficiais de versionamento e GitOps adicionados.
* Laboratório reproduzível de reconciliação, drift e promoção imutável adicionado e validado.
* Módulo 03 do Volume 03 desenvolvido com workflows, runners, cache, artefatos, OIDC, ambientes, CI e deploy.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências oficiais de Actions adicionados.
* Laboratório reproduzível de validação de DAG e gates de CI/CD adicionado e validado.
* Módulo 02 do Volume 03 desenvolvido com colaboração, branches, PRs, revisão, rulesets, releases e segurança.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências oficiais do GitHub adicionados.
* Laboratório reproduzível com upstream bare, dois colaboradores, revisão e merge adicionado e validado.
* Volume 03 — Git e GitHub iniciado com índice e identidade editorial.
* Módulo 01 desenvolvido com modelo de objetos, estados, commits, branches, remotos, recuperação e workflows.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito, referências e laboratório Git reproduzível adicionados.
* Módulo 08 do Volume 02 desenvolvido com SLOs, implantação, backup, automação, monitoramento, DR e capacidade.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências operacionais adicionados.
* Laboratório reproduzível de production readiness review adicionado e validado.
* Módulo 07 do Volume 02 desenvolvido com risco, identidade, permissões, kernel, rede, criptografia, auditoria e incidentes.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências de hardening adicionados.
* Laboratório reproduzível de auditoria declarativa de baseline adicionado e validado.
* Módulo 06 do Volume 02 desenvolvido com USE, RED, CPU, memória, I/O, profiling, tracing, incidentes e capacidade.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências de performance adicionados.
* Laboratório reproduzível de análise de snapshots e classificação de gargalo adicionado e validado.
* Módulo 05 do Volume 02 desenvolvido com namespaces, cgroups, imagens OCI, runtimes, volumes, redes e segurança.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências de contêineres adicionados.
* Laboratório reproduzível de camadas, whiteout e manifesto por digest adicionado e validado.
* Módulo 04 do Volume 02 desenvolvido com camadas, enlace, IP, roteamento, transporte, DNS, namespaces, firewall e diagnóstico.
* Estudo de caso da DataRetail S.A., revisão, exercícios, gabarito e referências de redes adicionados.
* Laboratório reproduzível de resolução, socket TCP e HTTP em loopback adicionado e validado.
* Módulo 03 do Volume 02 desenvolvido com fundamentos de Bash, expansões, funções, erros, idempotência, testes, segurança e operação.
* Estudo de caso da DataRetail S.A., exercícios, gabarito e referências de Shell Script adicionados.
* Laboratório reproduzível de ingestão Bash com validação, deduplicação, quarentena e publicação atômica adicionado.

### Changed

* Continuidade movida para o Módulo 06 — Planos de Execução, Índices e Otimização.
* Continuidade movida para o Módulo 05 — DDL, Schemas e Evolução de Estruturas.
* Continuidade movida para o Módulo 04 — DML, Transações e Concorrência.
* Continuidade movida para o Módulo 03 — Agregações, Funções de Janela e Análise.
* Continuidade movida para o Módulo 02 — Consultas, Joins e Subconsultas.
* Volume 03 — Git e GitHub marcado como concluído e continuidade movida para o Volume 04 — SQL.
* Continuidade movida para o Módulo 04 — Releases, Versionamento e GitOps.
* Continuidade movida para o Módulo 03 — GitHub Actions e CI/CD.
* Continuidade movida para o Módulo 02 — Branches, Colaboração e GitHub.
* Volume 02 — Linux marcado como concluído e continuidade movida para o Volume 03 — Git e GitHub.
* Volume 02 atualizado para marcar Segurança e Hardening Linux como concluído e apontar o Módulo 08 como próximo marco.
* Volume 02 atualizado para marcar Desempenho e Observabilidade Linux como concluído e apontar o Módulo 07 como próximo marco.
* Volume 02 atualizado para marcar Contêineres e Isolamento no Linux como concluído e apontar o Módulo 06 como próximo marco.
* Volume 02 atualizado para marcar Redes e Conectividade no Linux como concluído e apontar o Módulo 05 como próximo marco.
* Volume 02 atualizado para marcar Shell Script e Automação como concluído e apontar o Módulo 04 como próximo marco.

## Changed

* Estrutura física de `100-Volumes` consolidada como fonte oficial para nomes e numeração dos volumes.
* ROADMAP sincronizado com os volumes `00-Introducao` a `18-Projeto-Integrador`.
* Status do Volume 00 corrigido para refletir o conteúdo parcial existente.
* README, ARCHITECTURE, MEMORY e PROJECT_STATUS alinhados à estrutura oficial.
* Nomes de 42 documentos editoriais normalizados para hífens, sem espaços ou acentos.
* Wikilinks relacionados atualizados com aliases para preservar o texto exibido no Obsidian.
* Convenção editorial diferenciada das nomenclaturas reservadas por ferramentas de infraestrutura.
* Templates de capítulo, estudo de caso, glossário, laboratório, projeto e tecnologia preenchidos e padronizados para o Obsidian.
* Validador integrado com verificações de Markdown, YAML, nomenclatura, Wikilinks e estrutura dos módulos.
* Workflow de CI adicionado para impor invariantes limpos e auditar, sem bloqueio temporário, a dívida histórica do Vault.
* Normalização de frontmatter automatizada para documentos editoriais, preservando metadados existentes.
* Validação de frontmatter promovida a etapa bloqueante do CI após eliminação das pendências de YAML.
* Validador de Wikilinks ajustado à resolução por caminhos abreviados do Obsidian e a blocos de código.
* Ferramenta adicionada para redirecionar Wikilinks a destinos existentes e remover vínculos sem página correspondente.
* Validação de Wikilinks promovida a etapa bloqueante do CI após eliminação dos links sem destino.
* Validador estrutural ajustado para exigir componentes obrigatórios somente de módulos declarados como concluídos.
* Status do Módulo 01 — Dados e de seus documentos alinhado ao ROADMAP como concluído.
* Validação estrutural de módulos concluídos promovida a etapa bloqueante do CI.
* PyMarkdown configurado com extensões compatíveis com YAML frontmatter, tabelas e listas de tarefas do Obsidian.
* Normalizadores Markdown ampliados para espaços finais, linhas excedentes, quebra final e hierarquia de títulos.
* Dívida histórica de Markdown eliminada nos documentos do Vault.
* Validação completa do Vault promovida a etapa bloqueante do CI.
* Capítulo `07-Processamento-de-Dados.md` do Módulo 02 desenvolvido com fundamentos de transformação, ETL, ELT, batch, streaming e confiabilidade operacional.
* Capítulo `08-Consumo-e-Compartilhamento.md` desenvolvido com produtos de dados, contratos, interfaces de consumo, níveis de serviço, segurança e privacidade.
* Capítulo `09-Arquivamento-e-Descarte-de-Dados.md` desenvolvido com retenção, recuperação, legal hold, exclusão segura, backups e evidências de descarte.
* Estudo de caso do Módulo 02 desenvolvido com o ciclo completo dos dados de pedidos da DataRetail S.A., incluindo requisitos, controles, incidente e critérios de aceite.
* Resumo do Módulo 02 adicionado com mapa conceitual, controles transversais, matriz de decisões, checklist e autoavaliação.
* Perguntas de entrevista do Módulo 02 adicionadas em níveis progressivos, com respostas fundamentadas e cenários de diagnóstico e arquitetura.
* Exercícios e gabarito do Módulo 02 adicionados com progressão conceitual, aplicação, incidentes e arquitetura.
* Laboratório reproduzível em Python adicionado para ingestão, validação, deduplicação, publicação, quarentena e arquivamento.
* Solução do laboratório validada quanto a contagens, integridade e idempotência.
* Referências oficiais e bibliográficas do Módulo 02 consolidadas.
* Módulo 02 — Ciclo de Vida dos Dados marcado como concluído.
* Módulo 03 — Bancos de Dados desenvolvido com fundamentos, modelos, armazenamento interno, transações, concorrência, recuperação, índices e desempenho.
* Estudo de caso da DataRetail S.A., resumo, perguntas de entrevista, exercícios e gabarito do Módulo 03 adicionados.
* Laboratório reproduzível com SQLite adicionado e solução validada quanto a integridade, rollback, estoque e uso de índice.
* Referências oficiais e bibliográficas do Módulo 03 consolidadas.
* Módulo 03 — Bancos de Dados marcado como concluído.
* Módulo 04 — Modelagem iniciado com índice, objetivos, mapa conceitual e introdução.
* Capítulo 03 do Módulo 04 desenvolvido com abstração, escopo, processo, participantes, validação e critérios de qualidade da Modelagem de Dados.
* Capítulo 04 do Módulo 04 desenvolvido com níveis conceitual, lógico e físico, transformação, rastreabilidade e exemplo SQL da DataRetail S.A.
* Capítulo 05 do Módulo 04 desenvolvido com entidades, atributos, relacionamentos, associações temporais e entregas parciais da DataRetail S.A.
* Capítulo 06 do Módulo 04 desenvolvido com chaves, resolução de identidade, cardinalidade, integridade referencial e invariantes em Bancos de Dados e pipelines.
* Capítulo 07 do Módulo 04 desenvolvido com dependências funcionais, formas normais, decomposição sem perda, preservação de dependências e desnormalização consciente.
* Capítulo 08 do Módulo 04 desenvolvido com diferenças entre OLTP e OLAP, grão, fatos, dimensões, aditividade e histórico.
* Capítulo 09 do Módulo 04 desenvolvido com compatibilidade, migração de schema, backfill, trade-offs e governança.
* Estudo de caso da DataRetail S.A. adicionado com modelos operacional e analítico, entregas parciais, invariantes e testes de aceite.
* Resumo e 28 perguntas de entrevista do Módulo 04 adicionados.
* Exercícios e gabarito do Módulo 04 adicionados com progressão conceitual e arquitetural.
* Laboratório reproduzível de modelo operacional e analítico adicionado com solução SQLite.
* Referências oficiais e bibliográficas do Módulo 04 consolidadas.
* Módulo 04 — Modelagem marcado como concluído.
* Módulo 05 — ETL desenvolvido com extração, transformação, carga, incrementalidade, CDC, idempotência, testes e operação.
* Estudo de caso, resumo, perguntas de entrevista, exercícios e gabarito do Módulo 05 adicionados.
* Laboratório incremental em Python e SQLite adicionado com watermark, quarentena, upsert, auditoria e idempotência.
* Referências do Módulo 05 consolidadas e módulo marcado como concluído.
* Módulo 06 — ELT desenvolvido com raw, staging, marts, SQL modular, materializações, testes, linhagem, governança e custo.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 06 adicionados.
* Laboratório ELT em Python e SQLite adicionado com deduplicação por versão, mart, testes e rebuild.
* Referências do Módulo 06 consolidadas e módulo marcado como concluído.
* Módulo 07 — Pipelines desenvolvido com DAGs, batch, streaming, orquestração, estado, confiabilidade e SLOs.
* Estudo de caso, resumo, entrevistas, exercícios e gabarito do Módulo 07 adicionados.
* Laboratório de pipeline em Python e SQLite adicionado com executor de DAG, quarentena, auditoria, upsert e reconciliação.
* Referências do Módulo 07 consolidadas e módulo marcado como concluído.
* Módulo 08 — Arquiteturas desenvolvido com requisitos, atributos de qualidade, estilos, eventos e arquiteturas analíticas.
* Data Warehouse, Data Lake, Lakehouse, Data Mesh, Data Fabric, ADRs e evolução arquitetural consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 08 adicionados.
* Laboratório em Python e SQLite adicionado com matriz ponderada, fitness functions e persistência idempotente de ADR.
* Referências do Módulo 08 consolidadas e módulo marcado como concluído.
* Módulo 09 — Qualidade desenvolvido com dimensões, profiling, contratos, regras, testes e quality gates.
* SLOs, incidentes, responsabilidades, governança da qualidade e melhoria contínua consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 09 adicionados.
* Laboratório em Python e SQLite adicionado com métricas, quarentena, gate e persistência idempotente.
* Referências do Módulo 09 consolidadas e módulo marcado como concluído.
* Módulo 10 — Governança desenvolvido com princípios, modelo operacional, ownership, domínios, políticas e controles.
* Metadados, catálogo, linhagem, privacidade, retenção, conformidade, maturidade e federação consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 10 adicionados.
* Laboratório em Python e SQLite adicionado com policy as code, avaliação de ativos e evidências idempotentes.
* Referências do Módulo 10 consolidadas e módulo marcado como concluído.
* Módulo 11 — Observabilidade desenvolvido com logs, métricas, traces, correlação e saúde operacional e dos dados.
* Linhagem operacional, SLOs, alertas, dashboards, incidentes, runbooks, segurança e maturidade consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 11 adicionados.
* Laboratório em Python e SQLite adicionado com correlação de spans, avaliação de SLO e incidente idempotente.
* Referências do Módulo 11 consolidadas e módulo marcado como concluído.
* Validador Markdown ajustado para processar arquivos em lotes e evitar o limite de linha de comando do Windows.
* Módulo 12 — Conceitos Modernos desenvolvido com produtos de dados, contratos, plataforma self-service e arquitetura evolutiva.
* Data Mesh, Data Fabric, Lakehouse, ativação, DataOps, FinOps, metadados ativos e IA responsável consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo 12 adicionados.
* Laboratório em Python e SQLite adicionado com guardrails de prontidão e evidências idempotentes.
* Módulo 12 e Volume 01 — Fundamentos marcados como concluídos.
* Volume 02 — Linux iniciado com README, sumário e histórico de alterações.
* Módulo 01 — Fundamentos do Linux desenvolvido com kernel, shell, filesystem, permissões, processos, serviços e terminal.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do primeiro módulo Linux adicionados.
* Laboratório Bash adicionado com workspace temporário, permissões, manifesto SHA-256 e idempotência.
* Módulo Linux 02 — Administração do Sistema desenvolvido com pacotes, systemd, armazenamento, rede e manutenção.
* Logs, backup, recuperação, capacidade, hardening e automação administrativa consolidados.
* Estudo de caso, revisão, entrevistas, exercícios e gabarito do Módulo Linux 02 adicionados.
* Laboratório Bash adicionado com auditoria idempotente de configuração, mounts, backup e permissões.

## Planned

* Conclusão do Volume 01
* Expansão dos laboratórios
* Construção dos dashboards do Obsidian
* Publicação da primeira versão da documentação

---

## [0.1.0] - 2026-07-14

## Added

### Governança do projeto

* README.md
* AGENTS.md
* EDITORIAL.md
* STYLE_GUIDE.md
* ARCHITECTURE.md
* ROADMAP.md
* MEMORY.md
* PROJECT_STATUS.md
* CONTRIBUTING.md
* CHANGELOG.md

### Estrutura do projeto

* Organização do Vault do Obsidian
* Estrutura dos volumes
* Estrutura dos módulos
* Padronização editorial
* Convenções de nomenclatura
* Arquitetura do projeto

### Conteúdo

* Início do Volume 01
* Módulo 01 — Dados concluído
* Módulo 02 — Ciclo de Vida dos Dados iniciado

---

## Versionamento

O projeto utiliza Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

Exemplos:

```text
1.0.0

1.1.0

1.1.1
```

---

## Política de Atualização

Este arquivo deve ser atualizado sempre que ocorrer:

* conclusão de um módulo;
* conclusão de um volume;
* mudança arquitetural;
* alteração da governança;
* inclusão de novos laboratórios;
* publicação de uma nova versão.

Correções editoriais pequenas não precisam ser registradas.

---

## Histórico

| Versão | Data       | Descrição                    |
| ------ | ---------- | ---------------------------- |
| 0.1.0  | 2026-07-14 | Estrutura inicial do projeto |
