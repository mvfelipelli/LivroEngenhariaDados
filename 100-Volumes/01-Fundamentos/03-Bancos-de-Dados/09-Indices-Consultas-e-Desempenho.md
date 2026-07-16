---
title: Índices, Consultas e Desempenho
aliases: [Database Indexes, Query Optimization]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, indices, desempenho]
type: chapter
order: 09
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Estruturas de acesso, planos, estatísticas e custos de consulta."
---

# 09 — Índices, Consultas e Desempenho

## O problema da busca

Sem estrutura de acesso adequada, localizar registros pode exigir examinar todo o conjunto. Índices mantêm chaves associadas a localizações ou identificadores.

## B-tree

Árvores balanceadas mantêm chaves ordenadas e suportam igualdade, intervalos e ordenação.

```mermaid
flowchart TD
    A[20 | 50] --> B[5 | 10]
    A --> C[25 | 40]
    A --> D[60 | 80]
```

## Hash

Aplica uma função à chave para localizar buckets. Favorece igualdade; não preserva ordem para intervalos.

## Índices compostos

Contêm várias colunas. Ordem importa porque determina quais prefixos e ordenações podem ser usados. Seletividade e padrões de consulta orientam a escolha.

## Custo de índices

Índices consomem espaço e adicionam trabalho a inserções, atualizações e exclusões. Muitos índices podem degradar escrita e manutenção.

## Processamento de consulta

O otimizador transforma a consulta em operadores e estima custos. Decide entre varredura, acesso por índice, algoritmos de junção, agregação e ordenação.

```mermaid
flowchart LR
    A[SQL] --> B[Árvore lógica]
    B --> C[Planos candidatos]
    C --> D[Estimativa de custo]
    D --> E[Plano escolhido]
    E --> F[Execução]
```

## Estatísticas

Contagens, distribuição e valores frequentes ajudam a estimar cardinalidade. Estatísticas desatualizadas podem levar a um plano inadequado.

## SARGability

Predicados que permitem aproveitar estruturas de acesso são chamados de pesquisáveis. Aplicar funções à coluna indexada ou converter tipos implicitamente pode impedir acesso eficiente, dependendo do SGBD.

## Desempenho é sistêmico

Uma consulta lenta pode resultar de plano, dados, concorrência, I/O, memória, rede, locks ou expectativa incompatível. Otimizar exige medir.

## Exemplo

```sql
CREATE INDEX idx_pedidos_cliente_data
    ON pedidos (cliente_id, data_pedido);

SELECT pedido_id, data_pedido, total
FROM pedidos
WHERE cliente_id = 42
  AND data_pedido >= DATE '2026-07-01';
```

O índice pode favorecer o filtro, mas sua utilidade depende de volume, distribuição e plano real.

## Boas práticas

- Medir planos e tempos.
- Indexar consultas importantes, não todas as colunas.
- Manter estatísticas.
- Projetar paginação e limites.
- Revisar índices redundantes.

## Erros comuns

- acreditar que índice sempre melhora;
- ignorar custo de escrita;
- otimizar sem plano de execução;
- selecionar colunas desnecessárias;
- confundir tempo no cliente com tempo no SGBD.

## Resumo

Índices reduzem caminhos de busca, enquanto o otimizador escolhe como combinar operadores. Desempenho depende de dados, estatísticas, carga e recursos.

## Próximo Capítulo

➡️ [[10-Estudo-de-Caso-DataRetail|10 — Estudo de Caso: Bancos de Dados na DataRetail S.A.]]
