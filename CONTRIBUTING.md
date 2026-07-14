# CONTRIBUTING

Obrigado pelo interesse em contribuir com a **Formação em Engenharia de Dados**.

Este projeto tem como objetivo construir uma das mais completas referências abertas sobre Engenharia de Dados em língua portuguesa.

Toda contribuição é bem-vinda, desde que mantenha os padrões técnicos e editoriais da coleção.

---

## Antes de Contribuir

Leia obrigatoriamente os documentos de governança:

* README.md
* AGENTS.md
* EDITORIAL.md
* STYLE_GUIDE.md
* ARCHITECTURE.md
* ROADMAP.md
* MEMORY.md
* PROJECT_STATUS.md

Esses documentos definem como o projeto deve evoluir.

---

## Como Contribuir

Você pode contribuir com:

* correções técnicas;
* melhorias editoriais;
* novos diagramas;
* novos laboratórios;
* exercícios;
* estudos de caso;
* referências;
* correções ortográficas;
* exemplos de código.

---

## Fluxo de Trabalho

1. Faça um fork do repositório.
2. Crie uma branch específica para sua alteração.
3. Realize as modificações.
4. Revise o conteúdo.
5. Atualize o CHANGELOG quando necessário.
6. Abra um Pull Request.

---

## Convenções

Todo conteúdo deve seguir:

* Markdown
* YAML Frontmatter
* Wikilinks
* Mermaid
* Obsidian
* Português do Brasil

---

## Qualidade Técnica

Todo conteúdo deve:

* estar tecnicamente correto;
* possuir referências;
* evitar duplicações;
* utilizar exemplos executáveis;
* seguir o padrão editorial.

---

## Código

Sempre que possível utilizar exemplos reais.

Priorizar:

* SQL
* Python
* Bash
* Docker
* Spark
* PostgreSQL

Todo código deve ser executável.

---

## Diagramas

Utilizar Mermaid sempre que possível.

Evitar imagens quando um diagrama textual puder explicar o conceito.

---

## Estudos de Caso

Utilizar preferencialmente o cenário da empresa fictícia:

**DataRetail S.A.**

Evitar criar novos cenários sem necessidade.

---

## Inteligência Artificial

Contribuições produzidas com auxílio de IA são permitidas.

Entretanto:

* o autor continua responsável pelo conteúdo;
* todo material deve ser revisado tecnicamente;
* a IA não substitui a validação humana.

---

## Pull Requests

Um Pull Request deve conter:

* descrição clara;
* objetivo;
* impacto da alteração;
* arquivos modificados;
* referências quando aplicável.

---

## Checklist

Antes de enviar uma contribuição verifique:

* [ ] Ortografia
* [ ] Consistência técnica
* [ ] YAML
* [ ] Wikilinks
* [ ] Mermaid
* [ ] Referências
* [ ] Exemplos executáveis
* [ ] Atualização do CHANGELOG (quando necessário)

---

## Validação automatizada

Instale as dependências de desenvolvimento:

```bash
python -m pip install -r requirements-dev.txt
```

No Windows, execute a auditoria completa com:

```bat
tools\validate.cmd
```

Em qualquer sistema com Python, utilize:

```bash
python tools/validate_project.py
```

É possível executar categorias específicas:

```bash
python tools/validate_project.py --checks yaml,names,wikilinks
```

As verificações disponíveis são `markdown`, `yaml`, `names`, `wikilinks` e `modules`. Enquanto a dívida histórica estiver em correção, o CI bloqueia regressões de nomenclatura, frontmatter e templates, além de publicar a auditoria completa como diagnóstico não bloqueante.

---

## Código de Conduta

Esperamos que todos os colaboradores mantenham um ambiente respeitoso, colaborativo e construtivo.

Discussões técnicas são incentivadas.

Ataques pessoais, discriminação e comportamento ofensivo não serão tolerados.

---

## Obrigado

Obrigado por contribuir para a construção de uma referência aberta em Engenharia de Dados para a comunidade de língua portuguesa.
