---
title: Referências — Ciclo de Vida dos Dados
aliases: [Referências do Ciclo de Vida]
tags: [engenharia-de-dados, fundamentos, referencias, ciclo-de-vida]
type: references
order: 15
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Fontes oficiais e bibliográficas do Módulo 02 — Ciclo de Vida dos Dados."
---

# 15 — Referências

## Livros essenciais

### Fundamentals of Data Engineering

Joe Reis e Matt Housley. O’Reilly Media, 2022. Referência para geração, ingestão, armazenamento, transformação, disponibilização, segurança e DataOps.

### Designing Data-Intensive Applications

Martin Kleppmann. O’Reilly Media, 2017. Referência para confiabilidade, armazenamento, processamento batch e streaming, replicação e particionamento.

### DAMA-DMBOK

DAMA International. Referência para governança, qualidade, metadados, segurança e gerenciamento do ciclo de vida.

## Legislação e privacidade

### Lei Geral de Proteção de Dados Pessoais

Lei nº 13.709/2018. Aplique ao módulo os princípios de finalidade, necessidade, segurança, prevenção e término do tratamento. Consulte o [texto compilado oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm).

> [!warning]
> Este material é educacional e não substitui orientação jurídica.

### NIST Privacy Framework

O [NIST Privacy Framework](https://www.nist.gov/privacy-framework) apoia a identificação e o gerenciamento de riscos de privacidade.

### NIST SP 800-88

As [Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r1/final) apresentam fundamentos para sanitização e destinação de mídias.

## Padrões e documentação técnica

- [Python — módulo csv](https://docs.python.org/3/library/csv.html), utilizado no laboratório.
- [Python — hashlib](https://docs.python.org/3/library/hashlib.html), utilizado para integridade.
- [PostgreSQL — COPY](https://www.postgresql.org/docs/current/sql-copy.html), referência futura para movimentação tabular.
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/), referência para eventos e streaming.
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/), referência para processamento distribuído.
- [OpenLineage](https://openlineage.io/docs/), referência para metadados de execução e linhagem.

## Relação com os capítulos

| Tema | Capítulo |
| --- | --- |
| Conceito geral | [[03-O-que-e-o-Ciclo-de-Vida-dos-Dados]] |
| Origem | [[04-Geracao-e-Coleta-de-Dados]] |
| Transporte | [[05-Ingestao-de-Dados]] |
| Persistência | [[06-Armazenamento-de-Dados]] |
| Transformação | [[07-Processamento-de-Dados]] |
| Disponibilização | [[08-Consumo-e-Compartilhamento]] |
| Destinação | [[09-Arquivamento-e-Descarte-de-Dados]] |
| Aplicação integrada | [[10-Estudo-de-Caso-DataRetail]] |

## Critérios para novas fontes

Priorize documentação oficial, normas, legislação, livros reconhecidos e artigos acadêmicos. Registre edição, data de consulta quando necessário, escopo e limitações. Evite usar conteúdo promocional ou sem autoria como fundamento principal.

## Encerramento do módulo

O Módulo 02 agora contém objetivos, introdução, capítulos técnicos, estudo de caso, resumo, perguntas de entrevista, exercícios, gabarito, laboratório, solução e referências.

> [!success]
> O módulo apresenta o ciclo completo: os dados nascem com propósito, circulam com confiabilidade, geram valor sob controle e recebem destinação adequada.
