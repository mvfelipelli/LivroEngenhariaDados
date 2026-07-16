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
