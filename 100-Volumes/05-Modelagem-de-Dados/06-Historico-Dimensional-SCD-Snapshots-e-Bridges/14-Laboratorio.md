---
title: Laboratório — SCD Tipo 2 e Lookup Temporal
description: "Histórico de segmento e resolução de fatos no SQLite."
tags: [modelagem-de-dados, sqlite, laboratorio, scd2]
aliases: [Laboratório SCD Tipo 2]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — SCD Tipo 2 e Lookup Temporal

## Objetivo

Criar duas versões de cliente, carregar fatos antes e depois da mudança e comprovar que cada venda referencia o segmento válido.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie dimensão cliente SCD2.
2. Insira versão Bronze válida desde 1º de julho.
3. Feche-a em 10 de julho e insira versão Ouro.
4. Carregue vendas em 5 e 12 de julho por lookup temporal.
5. Confirme chaves substitutas diferentes.
6. Valide uma versão atual e ausência de overlap.
7. Agregue receita por segmento histórico.

## Validação esperada

```text
versoes=2
versoes_atuais=1
fatos=2
bronze_centavos=1000
ouro_centavos=2000
overlaps=0
lookup_temporal=ok
scd2=ok
```

Consulte [[14-Solucao|Solução]].
