---
title: Exercícios — Modelagem de Dados
aliases: [Exercícios de Modelagem]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, exercicios]
type: exercises
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre modelos, identidade, normalização, análise e evolução."
---

# 13 — Exercícios

> [!abstract]
> Resolva antes de consultar o [[13-Gabarito]]. Explicite pressupostos, grão e regras do domínio.

## Parte I — Revisão

1. Diferencie processo de modelagem e modelo de dados.
2. Compare os níveis conceitual, lógico e físico.
3. Diferencie entidade, atributo e relacionamento com um exemplo.
4. Explique chaves candidata, primária, alternativa e estrangeira.
5. Defina cardinalidade mínima e máxima.

## Parte II — Interpretação

6. Um cliente possui vários telefones, cada um com verificação e vigência. Modele o conceito.
7. Explique por que um ID gerado não impede clientes duplicados.
8. Uma relação `ITEM(pedido_id, produto_id, pedido_data, produto_nome, quantidade)` usa chave composta. Identifique dependências parciais.
9. Classifique as medidas receita, estoque diário e margem percentual quanto à aditividade.
10. Um relatório junta três itens, dois pagamentos e duas entregas do mesmo pedido. Explique o risco.

## Parte III — Aplicação

11. Modele em Mermaid clientes, pedidos, itens, produtos e pagamentos, com cardinalidades.
12. Proponha chaves para pedidos cujos números se repetem entre lojas.
13. Normalize até 3FN: `VENDA(pedido, data, cliente, nome_cliente, produto, nome_produto, quantidade)`.
14. Declare o grão e as medidas de uma fato de vendas por item.
15. Projete histórico de categoria de produto sem reclassificar vendas passadas.

## Parte IV — Desafios

16. Modele entregas parciais e a invariante que impede entregar acima do comprado.
17. Planeje tornar `currency` obrigatória sem interromper produtores antigos.
18. Defina testes para unicidade, integridade referencial, grão e reconciliação.
19. Compare normalização operacional e esquema estrela sem afirmar que um substitui o outro.
20. Produza uma decisão de modelagem da DataRetail com escopo, conceitos, chaves, regras, histórico, consumo, evolução e responsáveis.

## Critérios de avaliação

| Critério | Peso |
| --- | ---: |
| Correção semântica | 30% |
| Identidade e integridade | 25% |
| Grão e temporalidade | 20% |
| Trade-offs e evolução | 15% |
| Clareza | 10% |

## Próximo Capítulo

➡️ [[13-Gabarito|13 — Gabarito]]
