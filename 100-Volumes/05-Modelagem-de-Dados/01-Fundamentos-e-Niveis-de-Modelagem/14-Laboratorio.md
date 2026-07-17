---
title: Laboratório — Do Domínio ao Esquema Validado
description: "Tradução de regras de pedidos para constraints SQLite."
tags: [modelagem-de-dados, sqlite, laboratorio]
aliases: [Laboratório Fundamentos de Modelagem]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Do Domínio ao Esquema Validado

## Objetivo

Transformar entidades e invariantes de pedidos em esquema físico e provar identidade, cardinalidade e integridade com testes executáveis.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Modele cliente, pedido e item.
2. Defina chaves naturais e substitutas.
3. Aplique referências, unicidade e checks.
4. Insira um pedido válido com dois itens.
5. Tente quantidade zero, item duplicado e cliente inexistente.
6. Confirme que as três violações são rejeitadas.
7. Valide o grão e o total do pedido.

## Validação esperada

```text
clientes=1
pedidos=1
itens=2
total_centavos=3500
quantidade_invalida=rejeitada
item_duplicado=rejeitado
referencia_invalida=rejeitada
modelo=ok
```

Consulte [[14-Solucao|Solução]].
