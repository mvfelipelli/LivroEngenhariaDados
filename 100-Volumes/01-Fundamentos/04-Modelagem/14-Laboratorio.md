---
title: Laboratório — Modelo Operacional e Analítico
aliases: [Laboratório de Modelagem de Dados]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, laboratorio, sqlite, python]
type: laboratory
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Laboratório reproduzível de modelo normalizado, estrela analítica, grão e reconciliação."
---

# 14 — Laboratório

## Objetivo

Implementar com Python e SQLite um núcleo normalizado de vendas da DataRetail e derivar uma fato analítica, validando chaves, integridade, grão, histórico e reconciliação.

## Pré-requisitos

- Python 3.11 ou superior;
- terminal e editor;
- nenhuma dependência externa.

## Ambiente

Crie `lab-modelagem/database_modeling_lab.py`. O script deverá recriar `dataretail_modeling.db` a cada execução.

## Requisitos

1. criar clientes, produtos, pedidos e itens normalizados;
2. preservar unicidade de `(source_system, source_order_id)`;
3. identificar item por `(order_id, line_number)`;
4. impedir quantidade não positiva e referências órfãs;
5. criar dimensão de produto versionada;
6. criar fato no grão de linha confirmada;
7. impedir duplicidade no grão;
8. reconciliar quantidade e valor líquido entre modelos;
9. comprovar que mudança de categoria não altera o fato histórico;
10. permitir duas execuções idênticas.

## Dados esperados

- dois pedidos, um confirmado e um cancelado;
- três linhas operacionais;
- duas linhas na fato, somente do pedido confirmado;
- quantidade analítica igual a `3`;
- valor líquido igual a `380.00`;
- categoria histórica igual a `Periféricos`.

## Execução

```bash
python database_modeling_lab.py
python database_modeling_lab.py
```

## Resultado esperado

```text
integridade=ok
duplicidade_bloqueada=sim
orfao_bloqueado=sim
fato_linhas=2
quantidade=3
valor_liquido=380.00
categoria_historica=Periféricos
reconciliacao=ok
```

## Questões

1. Por que a fato não recebe o pedido cancelado?
2. Qual é o grão operacional e o analítico?
3. Por que produto possui chave operacional e chave de dimensão?
4. Como a versão preserva a categoria histórica?
5. Quais regras dependeriam de transação em um cenário concorrente?

## Critérios de conclusão

- todas as restrições exercitadas;
- fato única no grão;
- histórico preservado;
- reconciliação aprovada;
- execução repetível.

## Próximo Capítulo

➡️ [[14-Solucao|14 — Solução]]
