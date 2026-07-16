---
title: Perguntas de Entrevista
aliases:
  - Interview Questions
  - Revisão para Entrevistas
volume: 01
module: 01
chapter: 12
type: interview
status: Concluído
tags:
  - entrevistas
  - revisão
description: "Capítulo técnico sobre Perguntas de Entrevista na Formação em Engenharia de Dados."
created: "2026-07-14"
updated: "2026-07-14"
---

[[100-Volumes/01-Fundamentos/01-Dados/README]] | [[11-Resumo|11 - Resumo]] | [[13-Exercicios|13 - Exercícios]]

---

# Perguntas de Entrevista

> [!quote]
> "Saber fazer é importante. Saber explicar demonstra domínio."

---

# Objetivo

Este capítulo reúne perguntas frequentemente utilizadas em entrevistas para vagas de Engenharia de Dados, Analytics e Ciência de Dados.

O objetivo não é decorar respostas, mas verificar se você consegue explicar os conceitos de forma clara, objetiva e tecnicamente correta.

> [!tip]
> Antes de consultar as respostas, tente responder com suas próprias palavras.

---

# Nível 1 — Fundamentos

## 1. O que é um dado?

### O entrevistador deseja avaliar

- compreensão do conceito de dado;
- capacidade de diferenciar dado de informação.

### Resposta esperada

Um dado é o registro de um fato, evento ou característica da realidade. Isoladamente, possui pouco significado. Quando contextualizado e interpretado, pode gerar informação e conhecimento.

---

## 2. Qual a diferença entre dado e informação?

### O entrevistador deseja avaliar

Se o candidato compreende a transformação dos dados em valor.

### Resposta esperada

Dados são registros brutos.

Informação é o resultado da organização e contextualização desses dados.

Exemplo:

Dado:

```text
350
```

Informação:

```text
A loja vendeu 350 produtos ontem.
```

---

## 3. O que é Engenharia de Dados?

### Resposta esperada

É a disciplina responsável por projetar, construir e manter plataformas capazes de coletar, armazenar, transformar e disponibilizar dados para consumo por aplicações, análises e modelos de inteligência artificial.

---

# Nível 2 — Características dos Dados

## 4. Quais são os 5 Vs do Big Data?

### Resposta esperada

- Volume
- Velocidade
- Variedade
- Veracidade
- Valor

### Pergunta complementar

Qual deles costuma representar o maior desafio na sua experiência?

---

## 5. Por que a variedade dos dados aumenta a complexidade da plataforma?

### Resposta esperada

Porque diferentes formatos exigem diferentes mecanismos de armazenamento, processamento e consulta.

---

# Nível 3 — Tipos de Dados

## 6. Qual a diferença entre dados estruturados e semiestruturados?

### Resposta esperada

Dados estruturados seguem um esquema rígido.

Dados semiestruturados possuem organização parcial, permitindo maior flexibilidade.

---

## 7. Cite exemplos de dados não estruturados.

Exemplos esperados:

- imagens;
- vídeos;
- documentos;
- áudios;
- e-mails.

---

# Nível 4 — Estruturação

## 8. O que é um schema?

### Resposta esperada

É a definição da estrutura dos dados, incluindo campos, tipos, restrições e relacionamentos.

---

## 9. Explique Schema-on-Write e Schema-on-Read.

### Resposta esperada

Schema-on-Write valida os dados antes da gravação.

Schema-on-Read interpreta o esquema apenas durante a leitura.

---

# Nível 5 — Ciclo de Vida

## 10. Quais são as etapas do ciclo de vida dos dados?

Resposta esperada:

- geração;
- coleta;
- ingestão;
- armazenamento;
- processamento;
- consumo;
- arquivamento;
- descarte.

---

## 11. Em qual etapa a Engenharia de Dados atua mais fortemente?

Resposta esperada

Embora participe de todas as etapas, a Engenharia de Dados concentra grande parte de seu trabalho na ingestão, armazenamento, processamento e disponibilização dos dados.

---

# Nível 6 — Qualidade

## 12. O que significa qualidade dos dados?

Resposta esperada

É o conjunto de características que tornam os dados adequados para seu propósito.

---

## 13. Cite pelo menos quatro dimensões da qualidade.

Exemplos:

- Precisão
- Completude
- Consistência
- Atualidade
- Unicidade
- Validade

---

## 14. Como você trataria registros duplicados?

O entrevistador deseja avaliar raciocínio.

Uma boa resposta deve mencionar:

- identificação das duplicidades;
- definição da chave de negócio;
- deduplicação;
- validação da origem do problema;
- prevenção de novas duplicidades.

---

# Nível 7 — Metadados

## 15. O que são metadados?

Resposta esperada

São informações que descrevem os próprios dados.

---

## 16. Qual a importância dos metadados?

Resposta esperada

Facilitam:

- descoberta;
- governança;
- documentação;
- auditoria;
- linhagem;
- rastreabilidade.

---

# Perguntas de Cenário

## 17. Você recebeu um arquivo CSV com 15 milhões de registros.

O que avaliaria antes de carregá-lo?

Uma boa resposta pode incluir:

- formato;
- codificação;
- qualidade;
- tamanho;
- colunas;
- tipos;
- duplicidades;
- valores nulos;
- regras de negócio;
- estratégia de carga.

---

## 18. Um dashboard apresenta números diferentes do ERP.

Como investigaria?

O entrevistador espera um raciocínio estruturado.

Exemplo:

1. verificar origem dos dados;
2. validar pipelines;
3. comparar regras de negócio;
4. analisar transformações;
5. verificar qualidade;
6. confirmar atualização das cargas.

---

## 19. Como decidir entre PostgreSQL e Data Lake?

Resposta esperada

Depende das características dos dados.

Dados estruturados e transacionais costumam ser armazenados em bancos relacionais.

Grandes volumes heterogêneos normalmente utilizam Data Lakes.

---

## 20. O que você faria primeiro ao iniciar um projeto de Engenharia de Dados?

Uma boa resposta deve mencionar:

- entendimento do negócio;
- levantamento das fontes;
- caracterização dos dados;
- requisitos;
- arquitetura;
- qualidade;
- governança.

---

# Perguntas Avançadas

Essas perguntas costumam aparecer em vagas Pleno e Sênior.

- Como garantir qualidade em pipelines distribuídos?
- Como controlar evolução de schema?
- Como tratar dados históricos?
- Quando utilizar particionamento?
- Como documentar uma plataforma de dados?
- Como controlar custos de armazenamento?

---

# Autoavaliação

Marque as perguntas que você consegue responder sem consultar o material.

| Pergunta | Sei responder |
|-----------|:-------------:|
| O que é um dado? | ☐ |
| O que é informação? | ☐ |
| Quais são os 5 Vs? | ☐ |
| O que é Schema? | ☐ |
| O que é Schema-on-Read? | ☐ |
| O que é qualidade? | ☐ |
| O que são metadados? | ☐ |
| Como funciona o ciclo de vida? | ☐ |

---

# Dicas para entrevistas

> [!tip]
>
> Em entrevistas técnicas:
>
> - responda de forma objetiva;
> - use exemplos práticos;
> - demonstre raciocínio;
> - admita quando não souber algo;
> - relacione conceitos com experiências reais.

---

# Veja Também

## Próximo capítulo

➡️ [[13-Exercicios|13 - Exercícios]]

## Revisão

- [[11-Resumo|11 - Resumo]]
- [[03-O-que-sao-Dados|03 - O que são Dados]]
- [[08-Qualidade-dos-Dados|08 - Qualidade dos Dados]]
- [[09-Metadados|09 - Metadados]]

---

> [!success]
> Se você consegue responder corretamente à maior parte das perguntas deste capítulo sem consultar o material, provavelmente já possui uma base sólida dos fundamentos de Engenharia de Dados e está preparado para avançar para os próximos módulos da Academia.
