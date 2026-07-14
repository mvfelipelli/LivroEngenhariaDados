---
title: Gabarito dos Exercícios
aliases:
  - Respostas dos Exercícios
volume: 01
module: 01
chapter: 13
type: answer-key
status: Em desenvolvimento
tags:
  - gabarito
  - exercícios
---

[[13-Exercicios|13 - Exercícios]] | [[14-Laboratorio|14 - Laboratório]]

---

# Gabarito dos Exercícios

> [!info]
> Este gabarito apresenta respostas de referência. Em muitos exercícios existem diversas soluções corretas. O mais importante é justificar tecnicamente as decisões.

---

# Exercício 1

## Defina

### Dado

Registro bruto de um fato, evento ou característica da realidade.

### Informação

Dados organizados e contextualizados.

### Conhecimento

Interpretação da informação para apoiar decisões.

---

# Exercício 2

## Diferença entre dado e informação

Um dado isolado possui pouco significado.

Exemplo:

```
350
```

Informação:

```
A loja vendeu 350 produtos ontem.
```

A informação acrescenta contexto ao dado.

---

# Exercício 3

| Conceito | Resposta esperada |
|-----------|------------------|
| Dado | Registro bruto |
| Informação | Dado contextualizado |
| Conhecimento | Interpretação da informação |

---

# Exercício 4

## Os 5 Vs

| V | Significado |
|---|-------------|
| Volume | Quantidade de dados |
| Velocidade | Frequência de geração |
| Variedade | Diferentes formatos |
| Veracidade | Confiabilidade |
| Valor | Utilidade para o negócio |

---

# Exercício 5

## Classificação

| Exemplo | Estruturado | Semiestruturado | Não Estruturado |
|----------|:-----------:|:---------------:|:---------------:|
| CSV | ✅ | | |
| JSON | | ✅ | |
| Foto | | | ✅ |
| XML | | ✅ | |
| PostgreSQL | ✅ | | |
| PDF | | | ✅ |
| Vídeo | | | ✅ |

---

# Exercício 6

## Schema-on-Write

O esquema é validado durante a gravação.

Exemplo:

- PostgreSQL
- SQL Server
- Oracle

### Vantagens

- maior consistência;
- consultas otimizadas.

---

## Schema-on-Read

O esquema é aplicado apenas durante a leitura.

Exemplos:

- Data Lake;
- Apache Spark;
- Hadoop.

### Vantagens

- maior flexibilidade;
- ingestão simplificada.

---

# Exercício 7

## Ciclo de Vida dos Dados

Ordem correta:

1. Geração
2. Coleta
3. Ingestão
4. Armazenamento
5. Processamento
6. Consumo
7. Arquivamento
8. Descarte

---

# Exercício 8

## Problemas encontrados

- CPF ausente;
- e-mail inválido;
- registros duplicados;
- cidades padronizadas incorretamente.

### Tratamento esperado

- validação de CPF;
- validação de e-mail;
- deduplicação;
- padronização dos municípios.

### Etapa recomendada

Durante a ingestão ou processamento do pipeline.

---

# Exercício 9

| Fonte | Classificação |
|--------|---------------|
| ERP | Estruturado |
| Aplicativo | Semiestruturado |
| Sensores IoT | Semiestruturado (eventos) |
| Imagens | Não Estruturado |
| Marketplace | Semiestruturado |

---

# Exercício 10

## Metadados esperados

Uma boa resposta deve conter:

- nome da tabela;
- descrição;
- origem;
- responsável;
- frequência;
- política de retenção;
- sensibilidade;
- regras de qualidade;
- data da última atualização.

---

# Exercício 11

## Inventário

A resposta deve incluir, para cada sistema:

- nome;
- responsável;
- tipo de dado;
- volume;
- frequência;
- sensibilidade.

Não existe resposta única.

O importante é justificar.

---

# Exercício 12

O aluno deve demonstrar capacidade de analisar dados do cotidiano.

Uma boa resposta identifica:

- classificação;
- metadados;
- ciclo de vida;
- riscos de qualidade.

---

# Exercício 13

## Arquitetura

Uma boa solução deve contemplar:

```text
Fontes

↓

Ingestão

↓

Armazenamento

↓

Processamento

↓

Consumo
```

Não é necessário citar tecnologias específicas.

Caso sejam utilizadas, exemplos válidos incluem:

- PostgreSQL;
- Spark;
- Trino;
- Iceberg;
- Airflow.

---

# Exercício 14

## Resposta esperada

### Dados

- CRM
- PostgreSQL

### Metadados

Todos os componentes possuem metadados.

### Validação

Principalmente entre:

- CSV
- Python
- PostgreSQL

### Monitoramento

Todo o pipeline deve ser monitorado.

---

# Desafio

Não existe resposta única.

Uma boa solução deve abordar:

- levantamento das fontes;
- inventário dos dados;
- classificação;
- requisitos do negócio;
- qualidade;
- governança;
- arquitetura inicial.

---

# Questões para Discussão

Essas questões têm caráter reflexivo.

O objetivo é avaliar a capacidade de argumentação.

Não existe resposta correta.

O importante é fundamentar tecnicamente as decisões.

---

# Critérios de Avaliação

| Critério | Excelente |
|----------|-----------|
| Conceitos | Explica corretamente |
| Justificativas | Fundamentadas |
| Arquitetura | Coerente |
| Qualidade | Identifica problemas relevantes |
| Metadados | Documentação completa |

---

# Autoavaliação

Considere que você domina este módulo quando consegue responder corretamente, sem consultar o material, pelo menos:

- 90% dos exercícios conceituais;
- 80% dos exercícios de aplicação;
- 100% do estudo de caso.

---

# Próximo passo

Após concluir este gabarito, realize o laboratório.

➡️ [[14-Laboratorio|14 - Laboratório]]

---

> [!success]
> O objetivo deste gabarito não é fornecer respostas prontas, mas orientar o raciocínio esperado de um Engenheiro de Dados. Em projetos reais, diferentes soluções podem ser corretas desde que estejam tecnicamente justificadas.