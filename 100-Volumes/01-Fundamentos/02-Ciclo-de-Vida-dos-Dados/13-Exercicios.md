---
title: Exercícios — Ciclo de Vida dos Dados
aliases: [Exercícios do Ciclo de Vida]
tags: [engenharia-de-dados, fundamentos, exercicios, ciclo-de-vida]
type: exercises
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre o Ciclo de Vida dos Dados."
---

# 13 — Exercícios

> [!abstract]
> Resolva as atividades antes de consultar o [[13-Gabarito]]. Justifique decisões e explicite pressupostos quando o enunciado não fornecer todos os requisitos.

## Parte I — Revisão conceitual

1. Defina Ciclo de Vida dos Dados e explique por que ele não é estritamente linear.
2. Diferencie geração, coleta e ingestão usando uma venda no e-commerce.
3. Liste quatro controles transversais e explique sua função.
4. Compare dados ativos, arquivados e descartados.
5. Explique por que exclusão lógica não comprova descarte físico.

## Parte II — Interpretação

### 6. Batch ou streaming?

Classifique e justifique:

a. fechamento financeiro disponível às 7h;
b. alerta de fraude em poucos segundos;
c. relatório semanal de fornecedores;
d. atualização de estoque a cada 15 minutos.

### 7. Identificação de riscos

Um pipeline confirma o recebimento antes de persistir, não registra checksum e acrescenta linhas ao destino em toda retentativa. Identifique três riscos e proponha controles.

### 8. Qualidade

Para um produto de pedidos, defina um teste para completude, unicidade, validade, consistência e atualidade. Indique se cada falha deve alertar, segregar ou bloquear a publicação.

### 9. Contrato de dados

Liste ao menos oito elementos de um contrato para eventos de pedidos.

### 10. Retenção

Explique por que a regra “guardar vendas por cinco anos” está incompleta.

## Parte III — Aplicação

### 11. Mapeamento do ciclo

Desenhe em Mermaid o ciclo de dados de entregas, incluindo fonte, ingestão, armazenamento, processamento, consumidor, arquivo, descarte e quarentena.

### 12. Matriz de responsabilidades

Defina responsabilidades para dono do domínio, sistema produtor, Engenharia de Dados, governança, segurança e consumidor.

### 13. Reprocessamento

Uma regra de receita mudou e os últimos seis meses precisam ser recalculados. Elabore um plano com entrada, particionamento, idempotência, validação, publicação e comunicação.

### 14. Compartilhamento externo

Um fornecedor solicita transações com nome, CPF e endereço para prever demanda regional. Proponha uma entrega que respeite finalidade e minimização.

### 15. Arquivamento

Crie um checklist para arquivar uma partição anual e demonstrar que ela continua recuperável.

## Parte IV — Desafios

### 16. Incidente

O dashboard mostra 30% menos pedidos, embora o pipeline esteja verde. Escreva uma investigação ordenada da fonte ao consumo.

### 17. Arquitetura

Projete o ciclo de vida de pedidos da DataRetail S.A. para dois consumidores: reposição em 15 minutos e finanças no dia seguinte. Explique onde batch e streaming coexistem.

### 18. Descarte distribuído

Um cliente foi removido da tabela principal, mas permanece em cache, exportação, ambiente de teste e backup. Defina o tratamento de cada cópia e as evidências esperadas.

### 19. Trade-off

Compare preservar toda entrada bruta indefinidamente com aplicar retenção limitada. Discuta capacidade de reprocessamento, custo, privacidade e risco.

### 20. Projeto final

Produza uma ficha de um produto de dados contendo propósito, produtores, consumidores, schema resumido, qualidade, nível de serviço, segurança, linhagem, retenção e responsável.

## Critérios de avaliação

| Critério | Peso |
| --- | ---: |
| Correção conceitual | 30% |
| Justificativa e trade-offs | 25% |
| Controles de confiabilidade | 20% |
| Segurança e governança | 15% |
| Clareza | 10% |

## Próximo Capítulo

➡️ [[13-Gabarito|13 — Gabarito]]
