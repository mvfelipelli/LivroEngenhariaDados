---
title: Referências do Módulo — Dados
aliases:
  - Referências do Módulo 01
  - Bibliografia sobre Dados
  - Leituras sobre Fundamentos de Dados
volume: 01
module: 01
chapter: 15
type: references
status: Concluído
tags:
  - referências
  - bibliografia
  - fundamentos
  - dados
  - qualidade-de-dados
  - metadados
description: "Capítulo técnico sobre Referências do Módulo — Dados na Formação em Engenharia de Dados."
created: "2026-07-14"
updated: "2026-07-14"
---

[[100-Volumes/01-Fundamentos/01-Dados/README]] | [[14-Laboratorio|14 - Laboratório]] | [[14-Solucao|14 - Solução]]

---

# Referências do Módulo — Dados

> [!quote]
> "Uma formação sólida combina conteúdo didático, documentação oficial, pesquisa acadêmica e experiência prática."

---

# Objetivo

Esta nota reúne as principais referências utilizadas para aprofundar os assuntos apresentados no **Módulo 01 — Dados**.

As referências foram organizadas por tema e nível de prioridade, permitindo que o estudante escolha entre:

- revisão rápida;
- aprofundamento conceitual;
- consulta técnica;
- pesquisa acadêmica;
- preparação para os próximos volumes.

---

# Como utilizar esta lista

Não é necessário ler todas as referências antes de avançar.

A sequência recomendada é:

1. concluir os capítulos do módulo;
2. executar o laboratório;
3. revisar o resumo;
4. consultar as referências essenciais;
5. utilizar as demais fontes conforme surgirem dúvidas;
6. registrar anotações em `070-Anotacoes`.

> [!tip]
> Ao estudar uma referência externa, crie uma nota própria com:
>
> - principais conceitos;
> - dúvidas;
> - exemplos;
> - relações com a Academia;
> - aplicações no Projeto Integrador.

---

# Prioridade de leitura

| Prioridade | Objetivo |
|---|---|
| Essencial | Consolidar os fundamentos do módulo |
| Recomendada | Aprofundar conceitos importantes |
| Avançada | Explorar arquitetura, pesquisa e governança |
| Consulta | Verificar detalhes técnicos específicos |

---

# Referências Essenciais

## Fundamentals of Data Engineering

**Autores:** Joe Reis e Matt Housley  
**Editora:** O’Reilly Media

### Temas relacionados

- ciclo de vida da Engenharia de Dados;
- geração;
- armazenamento;
- ingestão;
- transformação;
- disponibilização;
- segurança;
- governança;
- DataOps.

### Relação com o módulo

Esta obra ajuda a compreender como as características dos dados influenciam o desenho de uma plataforma.

### Notas relacionadas

- [[Ciclo de Vida dos Dados]]
- [[Pipeline-de-Dados|Pipeline de Dados]]
- [[Engenharia-de-Dados|Engenharia de Dados]]
- [[Arquiteturas]]

### Prioridade

**Essencial**

---

## Designing Data-Intensive Applications

**Autor:** Martin Kleppmann  
**Editora:** O’Reilly Media

### Temas relacionados

- confiabilidade;
- escalabilidade;
- manutenção;
- armazenamento;
- processamento distribuído;
- replicação;
- particionamento;
- sistemas de dados.

### Relação com o módulo

A obra demonstra como as propriedades e limitações dos dados influenciam a construção de sistemas confiáveis.

### Notas relacionadas

- [[Estruturação dos Dados]]
- [[Particionamento]]
- [[Arquitetura de Dados]]
- [[Sistemas Distribuídos]]

### Prioridade

**Essencial**, com leitura progressiva.

---

## DAMA-DMBOK

**Organização:** DAMA International  
**Título:** *DAMA-DMBOK: Data Management Body of Knowledge*

### Temas relacionados

- governança de dados;
- qualidade;
- metadados;
- arquitetura;
- modelagem;
- segurança;
- integração;
- gerenciamento do ciclo de vida.

### Relação com o módulo

É uma das principais referências para conceitos corporativos de gestão de dados.

### Notas relacionadas

- [[Governança de Dados]]
- [[Qualidade-de-Dados|Qualidade de Dados]]
- [[Metadados]]
- [[Catálogo de Dados]]
- [[Data Steward]]
- [[Data Owner]]

### Prioridade

**Essencial para governança e qualidade.**

---

# Dados, Informação e Conhecimento

## The Data–Information–Knowledge–Wisdom Hierarchy

A hierarquia DIKW é utilizada para representar a progressão entre:

```mermaid
flowchart LR
    DADOS["Dados"]
    INFORMACAO["Informação"]
    CONHECIMENTO["Conhecimento"]
    SABEDORIA["Sabedoria"]

    DADOS --> INFORMACAO
    INFORMACAO --> CONHECIMENTO
    CONHECIMENTO --> SABEDORIA
```

### Pontos de atenção

A DIKW é útil como modelo didático, mas não deve ser tratada como uma sequência automática.

Dados não se transformam em conhecimento apenas porque foram armazenados ou processados.

São necessários:

- contexto;
- interpretação;
- experiência;
- validação;
- compreensão do negócio.

### Notas relacionadas

- [[O que são Dados]]
- [[Informação]]
- [[Conhecimento]]
- [[Contexto]]

---

## Data and Information Quality

Obras e artigos sobre qualidade da informação ajudam a diferenciar:

- qualidade técnica;
- qualidade semântica;
- adequação ao uso;
- confiança do consumidor.

### Questão central

> O dado é adequado para a finalidade em que será utilizado?

Essa pergunta deve orientar toda avaliação de qualidade.

---

# Big Data e Características dos Dados

## Big Data: A Revolution That Will Transform How We Live, Work, and Think

**Autores:** Viktor Mayer-Schönberger e Kenneth Cukier

### Temas relacionados

- crescimento dos dados;
- análise em larga escala;
- impacto organizacional;
- tomada de decisão orientada por dados.

### Relação com o módulo

Ajuda a contextualizar por que volume, variedade e velocidade alteraram a forma como organizações utilizam dados.

### Notas relacionadas

- [[Big-Data|Big Data]]
- [[Características dos Dados]]
- [[Volume]]
- [[Velocidade]]
- [[Variedade]]

---

## Os Vs do Big Data

A formulação mais conhecida inclui:

- Volume;
- Velocidade;
- Variedade;
- Veracidade;
- Valor.

Outros modelos também adicionam características como:

- variabilidade;
- volatilidade;
- visualização;
- vulnerabilidade.

> [!important]
> A quantidade de Vs varia entre autores. Na Academia, os cinco primeiros são utilizados como modelo introdutório, sem serem tratados como uma definição formal e universal.

---

# Tipos e Estruturação dos Dados

## Database System Concepts

**Autores:** Abraham Silberschatz, Henry Korth e S. Sudarshan

### Temas relacionados

- bancos de dados;
- modelo relacional;
- armazenamento;
- transações;
- índices;
- organização física;
- consultas.

### Relação com o módulo

Fornece a base teórica para compreender dados estruturados e bancos relacionais.

### Notas relacionadas

- [[Dados Estruturados]]
- [[Banco de Dados]]
- [[Schema]]
- [[PostgreSQL]]

### Prioridade

**Recomendada**

---

## Database Design for Mere Mortals

**Autor:** Michael J. Hernandez

### Temas relacionados

- identificação de entidades;
- atributos;
- relacionamentos;
- regras de negócio;
- desenho lógico.

### Relação com o módulo

Ajuda a compreender como os dados são organizados antes da implementação física.

### Notas relacionadas

- [[Estrutura Lógica]]
- [[Modelagem de Dados]]
- [[Entidade]]
- [[Atributo]]

---

## Documentação do JSON

### Temas relacionados

- documentos;
- objetos;
- arrays;
- valores;
- estruturas semiestruturadas.

### Aplicações

- APIs;
- eventos;
- configuração;
- integrações;
- mensageria.

### Notas relacionadas

- [[JSON]]
- [[Dados Semiestruturados]]
- [[API REST]]
- [[Apache Kafka]]

---

## Especificação XML

### Temas relacionados

- documentos hierárquicos;
- elementos;
- atributos;
- namespaces;
- validação por schema.

### Notas relacionadas

- [[XML]]
- [[Dados Semiestruturados]]
- [[Schema]]

---

# Formatos de Dados

## Apache Parquet

Formato colunar utilizado em cargas analíticas.

### Características

- armazenamento por coluna;
- compressão;
- codificação eficiente;
- leitura seletiva;
- suporte a esquemas complexos.

### Aplicações futuras

- [[Apache-Spark|Apache Spark]];
- [[Trino]];
- [[Apache-Iceberg|Apache Iceberg]];
- [[Lakehouse]].

### Prioridade

**Consulta agora e aprofundamento no Volume 09.**

---

## Apache Avro

Formato de serialização orientado a linhas.

### Características

- esquema explícito;
- evolução de esquema;
- uso frequente em integração e streaming;
- representação binária compacta.

### Notas relacionadas

- [[Apache Avro]]
- [[Schema Evolution]]
- [[Streaming]]

---

## Apache ORC

Formato colunar utilizado em ecossistemas analíticos.

### Características

- compressão;
- índices internos;
- leitura seletiva;
- otimização para consultas.

### Notas relacionadas

- [[ORC]]
- [[Armazenamento Colunar]]
- [[Data-Lake|Data Lake]]

---

# Ciclo de Vida dos Dados

## Data Lifecycle Management

O gerenciamento do ciclo de vida considera:

- criação;
- captura;
- armazenamento;
- utilização;
- compartilhamento;
- arquivamento;
- retenção;
- descarte.

### Perguntas orientadoras

- Por quanto tempo os dados devem permanecer disponíveis?
- Quando devem ser movidos para armazenamento mais econômico?
- Quais obrigações legais precisam ser atendidas?
- Como realizar descarte seguro?
- O dado pode ser anonimizado em vez de eliminado?

### Notas relacionadas

- [[Ciclo de Vida dos Dados]]
- [[Retenção de Dados]]
- [[Arquivamento]]
- [[Descarte Seguro]]
- [[LGPD]]

---

## Records Management

Práticas de gestão de registros ajudam a definir:

- prazo de retenção;
- valor administrativo;
- valor fiscal;
- valor legal;
- valor histórico;
- critérios de descarte.

Esses conceitos são especialmente importantes para ambientes regulados.

---

# Qualidade dos Dados

## Data Quality: The Accuracy Dimension

**Autor:** Jack E. Olson

### Temas relacionados

- precisão;
- perfil dos dados;
- avaliação;
- regras de validação;
- melhoria da qualidade.

### Notas relacionadas

- [[Qualidade-de-Dados|Qualidade de Dados]]
- [[Precisão]]
- [[Data Profiling]]

---

## Executing Data Quality Projects

**Autor:** Danette McGilvray

### Temas relacionados

- projetos de qualidade;
- avaliação;
- priorização;
- melhoria contínua;
- monitoramento.

### Relação com o módulo

Ajuda a transformar dimensões abstratas de qualidade em um processo operacional.

---

## Data Quality Dimensions

As dimensões mais utilizadas na Academia são:

| Dimensão | Questão principal |
|---|---|
| Precisão | O dado representa corretamente a realidade? |
| Completude | Os valores necessários estão presentes? |
| Consistência | O dado é coerente entre sistemas? |
| Atualidade | O dado está disponível no momento necessário? |
| Unicidade | Existem registros duplicados? |
| Validade | O dado respeita as regras definidas? |

> [!note]
> Diferentes instituições podem utilizar nomes, agrupamentos e definições ligeiramente distintos.

---

## ISO 8000

Família de normas relacionada à qualidade de dados e dados mestres.

### Temas relacionados

- representação;
- intercâmbio;
- qualidade;
- dados mestres;
- terminologia.

### Prioridade

**Avançada**

---

## ISO/IEC 25012

Modelo de qualidade de dados que descreve características para avaliação de dados em sistemas computacionais.

### Utilidade

Pode ser usada como referência para estruturar critérios de avaliação mais formais.

### Prioridade

**Avançada**

---

# Metadados, Catálogo e Linhagem

## NISO — Understanding Metadata

Referência introdutória para compreender categorias e funções dos metadados.

### Temas relacionados

- metadados descritivos;
- estruturais;
- administrativos;
- preservação;
- descoberta.

### Relação com o módulo

Amplia a visão além dos metadados puramente técnicos.

---

## Data Catalog

Um catálogo de dados centraliza informações como:

- nome dos ativos;
- descrição;
- proprietário;
- responsável técnico;
- classificação;
- linhagem;
- qualidade;
- consumidores;
- políticas de acesso.

### Tecnologias relacionadas

- [[DataHub]];
- [[OpenMetadata]];
- [[Apache Atlas]];
- [[Microsoft Purview]].

---

## OpenLineage

Padrão aberto para coleta de metadados de execução e linhagem.

### Conceitos principais

- job;
- run;
- dataset;
- inputs;
- outputs;
- eventos de execução.

### Notas relacionadas

- [[Data Lineage]]
- [[OpenLineage]]
- [[Apache-Airflow|Apache Airflow]]
- [[Observabilidade de Dados]]

---

## Apache Atlas

Plataforma de metadados e governança associada ao ecossistema de dados.

### Recursos

- classificação;
- catálogo;
- linhagem;
- glossário de negócio;
- integração com tecnologias do ecossistema.

### Prioridade

**Consulta**

---

# Governança, Segurança e Privacidade

## Lei Geral de Proteção de Dados — LGPD

A LGPD estabelece princípios e obrigações para o tratamento de dados pessoais no Brasil.

### Assuntos relacionados ao módulo

- dados pessoais;
- dados pessoais sensíveis;
- finalidade;
- necessidade;
- segurança;
- retenção;
- anonimização;
- eliminação;
- direitos do titular.

### Notas relacionadas

- [[LGPD]]
- [[Dados Pessoais]]
- [[Dados Sensíveis]]
- [[Anonimização]]
- [[Retenção de Dados]]

> [!warning]
> O conteúdo da Academia não substitui orientação jurídica especializada.

---

## Privacy by Design

Princípio segundo o qual privacidade e proteção de dados devem ser consideradas desde o desenho da solução.

### Aplicações em Engenharia de Dados

- minimização;
- controle de acesso;
- mascaramento;
- criptografia;
- retenção limitada;
- auditoria;
- rastreabilidade.

---

## NIST Privacy Framework

Estrutura para gerenciamento de riscos relacionados à privacidade.

### Utilidade

Ajuda organizações a integrar proteção de dados aos processos de governança e segurança.

### Prioridade

**Avançada**

---

# Referências Técnicas para os Próximos Volumes

## PostgreSQL Documentation

Será utilizada para estudar:

- tipos de dados;
- schemas;
- restrições;
- índices;
- transações;
- particionamento;
- administração.

### Volume relacionado

[[100-Volumes/08-PostgreSQL/README|Volume 08 — PostgreSQL]]

---

## Apache Spark Documentation

Será utilizada para estudar:

- DataFrames;
- schemas;
- leitura de formatos;
- processamento distribuído;
- qualidade;
- particionamento.

### Volume relacionado

[[100-Volumes/07-Apache-Spark/README|Volume 07 — Apache Spark]]

---

## Apache Iceberg Documentation

Será utilizada para estudar:

- tabelas analíticas;
- snapshots;
- transações;
- evolução de esquema;
- evolução de particionamento;
- time travel.

### Volume relacionado

[[100-Volumes/09-Lakehouse/README|Volume 09 — Lakehouse]]

---

## Trino Documentation

Será utilizada para estudar:

- consultas distribuídas;
- catálogos;
- conectores;
- otimização;
- leitura de tabelas analíticas.

### Volume relacionado

[[100-Volumes/10-Trino/README|Volume 10 — Trino]]

---

## Apache Airflow Documentation

Será utilizada para estudar:

- DAGs;
- tarefas;
- dependências;
- agendamento;
- reprocessamento;
- monitoramento;
- metadados operacionais.

### Volume relacionado

[[100-Volumes/11-Apache-Airflow/README|Volume 11 — Apache Airflow]]

---

# Referências do Projeto Integrador

O Projeto Integrador utilizará as referências deste módulo para documentar:

- inventário de fontes;
- classificação dos dados;
- ciclo de vida;
- qualidade;
- metadados;
- sensibilidade;
- retenção;
- arquitetura inicial.

### Projeto relacionado

[[030-Projetos/DataRetail Platform/README|DataRetail Platform]]

### Entregáveis relacionados

- catálogo inicial de fontes;
- dicionário de dados;
- matriz de qualidade;
- classificação de sensibilidade;
- diagrama do ciclo de vida;
- arquitetura conceitual.

---

# Biblioteca da Academia

As referências principais deverão receber notas próprias na pasta:

```text
010-Biblioteca/
```

Estrutura recomendada:

```text
010-Biblioteca/
├── Livros/
├── Papers/
├── RFCs/
├── Documentacao Oficial/
├── Cheat Sheets/
├── Casos Reais/
└── Empresas/
```

## Notas prioritárias

- [[Fundamentals of Data Engineering]]
- [[Designing Data-Intensive Applications]]
- [[DAMA-DMBOK]]
- [[Apache Parquet Documentation]]
- [[Apache Spark Documentation]]
- [[PostgreSQL Documentation]]
- [[Apache Iceberg Documentation]]
- [[Trino Documentation]]
- [[Apache Airflow Documentation]]
- [[LGPD]]

---

# Modelo para registrar uma leitura

Ao estudar uma referência, utilize a seguinte estrutura:

```markdown
---
title:
type: reference
status: Em leitura
tags:
  - biblioteca
---

# Nome da Referência

## Informações bibliográficas

- Autor:
- Editora ou organização:
- Ano:
- Tipo:

## Objetivo

## Principais conceitos

## Relação com a Academia

## Aplicação na DataRetail S.A.

## Anotações

## Dúvidas

## Veja também
```

---

# Ordem Recomendada de Estudo

## Agora

1. [[Fundamentals of Data Engineering]]
2. [[DAMA-DMBOK]]
3. Referência introdutória sobre metadados
4. Material introdutório sobre LGPD

## Durante os volumes técnicos

1. documentação oficial da tecnologia;
2. capítulo correspondente da Academia;
3. laboratório;
4. aplicação no Projeto Integrador.

## Para aprofundamento

1. [[Designing Data-Intensive Applications]]
2. normas de qualidade;
3. padrões de metadados;
4. artigos acadêmicos;
5. casos reais de arquitetura.

---

# Critérios de Seleção das Referências

As referências incluídas na Academia devem atender a um ou mais dos seguintes critérios:

- documentação oficial;
- livro reconhecido;
- norma técnica;
- artigo acadêmico relevante;
- padrão aberto;
- legislação aplicável;
- caso real publicado por organização confiável.

Deve-se evitar utilizar como fonte principal:

- conteúdo sem autoria;
- publicações sem referências;
- tutoriais desatualizados;
- materiais excessivamente promocionais;
- respostas geradas sem validação;
- exemplos que não explicam suas limitações.

---

# Checklist de Referências do Módulo

- [ ] Consultei ao menos uma referência essencial.
- [ ] Registrei minhas anotações.
- [ ] Relacionei a leitura ao módulo.
- [ ] Identifiquei conceitos que precisam de revisão.
- [ ] Consultei documentação oficial quando necessário.
- [ ] Relacionei as referências ao Projeto Integrador.
- [ ] Evitei depender de uma única fonte.
- [ ] Verifiquei se o material está atualizado.

---

# Encerramento do Módulo

Com esta nota, o **Módulo 01 — Dados** possui a estrutura completa:

1. [[01-Objetivos|01 - Objetivos]]
2. [[02-Introducao|02 - Introdução]]
3. [[03-O-que-sao-Dados|03 - O que são Dados]]
4. [[04-Caracteristicas-dos-Dados|04 - Características dos Dados]]
5. [[05-Tipos-de-Dados|05 - Tipos de Dados]]
6. [[06-Estruturacao-dos-Dados|06 - Estruturação dos Dados]]
7. [[07-Ciclo-de-Vida-dos-Dados|07 - Ciclo de Vida dos Dados]]
8. [[08-Qualidade-dos-Dados|08 - Qualidade dos Dados]]
9. [[09-Metadados|09 - Metadados]]
10. [[10-Estudo-de-Caso|10 - Estudo de Caso]]
11. [[11-Resumo|11 - Resumo]]
12. [[12-Perguntas-de-Entrevista|12 - Perguntas de Entrevista]]
13. [[13-Exercicios|13 - Exercícios]]
14. [[13-Gabarito|13 - Gabarito]]
15. [[14-Laboratorio|14 - Laboratório]]
16. [[14-Solucao|14 - Solução]]
17. [[15-Referencias|15 - Referências]]

---

# Veja Também

## Módulo

- [[100-Volumes/01-Fundamentos/01-Dados/README]]
- [[11-Resumo|11 - Resumo]]
- [[14-Laboratorio|14 - Laboratório]]
- [[14-Solucao|14 - Solução]]

## Atlas

- [[000-Atlas/MOC]]
- [[000-Atlas/Arquiteturas]]
- [[000-Atlas/Tecnologias]]
- [[000-Atlas/Guia-Editorial|Guia Editorial]]

## Biblioteca

- [[010-Biblioteca/README]]

## Projeto

- [[030-Projetos/DataRetail Platform/README]]

---

> [!success]
> O **Módulo 01 — Dados** está completo. Ele estabelece a base conceitual necessária para compreender fontes, armazenamento, processamento, qualidade, metadados e governança ao longo de toda a Academia.

