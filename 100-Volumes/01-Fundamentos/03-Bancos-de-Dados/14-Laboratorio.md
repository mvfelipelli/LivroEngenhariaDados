---
title: Laboratório — Transações e Índices com SQLite
aliases: [Laboratório de Bancos de Dados]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, laboratorio, sqlite, python]
type: laboratory
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Laboratório reproduzível de integridade, transações, rollback, índices e planos de consulta."
---

# 14 — Laboratório

## Objetivo

Construir um Banco SQLite para pedidos da DataRetail S.A. e observar restrições, atomicidade, rollback, atualização condicional de estoque, índice composto e plano de consulta.

## Pré-requisitos

- Python 3.11 ou superior;
- terminal e editor de texto;
- nenhuma dependência externa.

## Ambiente

Crie uma pasta `lab-bancos-de-dados` e, dentro dela, o arquivo `database_lab.py`. O programa deverá criar `dataretail.db` do zero a cada execução.

## Requisitos

1. habilitar chaves estrangeiras;
2. criar `customers`, `products`, `orders` e `order_items`;
3. usar chaves primárias, estrangeiras, `NOT NULL` e `CHECK`;
4. cadastrar dois clientes e três produtos;
5. confirmar um pedido e baixar estoque na mesma transação;
6. tentar uma compra sem estoque e comprovar rollback;
7. criar índice composto em `orders(customer_id, created_at)`;
8. executar `EXPLAIN QUERY PLAN` antes e depois do índice;
9. validar totais, estoque e integridade referencial;
10. permitir reexecução determinística.

## Invariantes

- estoque nunca negativo;
- quantidade e preço unitário positivos;
- total do pedido não negativo;
- item sempre associado a pedido e produto existentes;
- compra sem estoque não deixa pedido parcial.

## Execução

```bash
python database_lab.py
```

## Resultado esperado

```text
pedido_confirmado=1001
compra_sem_estoque=rollback
pedidos=1
itens=1
estoque_produto_101=3
integridade=ok
indice_utilizado=sim
```

O texto exato do plano depende da versão do SQLite; ele deve mencionar o índice `idx_orders_customer_created` após sua criação.

## Questões de análise

1. Por que a verificação de estoque e sua atualização devem ocorrer atomicamente?
2. Qual estado incorreto surgiria sem rollback?
3. Por que o índice ajuda uma consulta e aumenta o custo das escritas?
4. O laboratório prova durabilidade diante de falha de energia? Justifique.
5. Que mecanismos adicionais seriam necessários em produção?

## Critérios de conclusão

- script executado sem dependências externas;
- todas as restrições criadas;
- pedido válido confirmado;
- compra inválida revertida integralmente;
- plano posterior usa o índice;
- validações automáticas aprovadas;
- segunda execução produz o mesmo resultado.

## Próximo Capítulo

➡️ [[14-Solucao|14 — Solução]]
