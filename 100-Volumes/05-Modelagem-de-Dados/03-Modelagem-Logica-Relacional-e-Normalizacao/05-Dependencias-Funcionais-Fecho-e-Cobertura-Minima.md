---
title: Dependências Funcionais, Fecho e Cobertura Mínima
description: "Regras semânticas que determinam atributos."
tags: [dependencias-funcionais, fecho, cobertura-minima]
aliases: [Dependências Funcionais]
created: 2026-07-17
updated: 2026-07-17
---

# Dependências Funcionais, Fecho e Cobertura Mínima

`X → Y` significa que duas tuplas iguais em `X` devem ser iguais em `Y`. A dependência decorre da regra do domínio, não de coincidência nos dados atuais.

Exemplo:

```text
pedido_id → cliente_id, criado_em
(pedido_id, numero_item) → produto_id, quantidade, preco
produto_id → nome_produto
```

O fecho `X+` reúne atributos determinados por `X` sob um conjunto de dependências. Se o fecho contém todos os atributos, `X` é superchave. Axiomas de Armstrong — reflexividade, aumento e transitividade — derivam dependências válidas.

Cobertura mínima decompõe lados direitos, remove atributos excedentes e dependências redundantes. Ela apoia síntese em 3FN.

> [!tip]
> Escreva a frase de negócio que justifica cada dependência; isso revela regras falsas como `CEP → cidade` em contextos com exceções.
