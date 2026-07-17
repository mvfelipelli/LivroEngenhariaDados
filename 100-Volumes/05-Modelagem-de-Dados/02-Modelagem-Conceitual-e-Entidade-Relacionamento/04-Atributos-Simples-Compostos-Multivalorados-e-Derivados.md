---
title: Atributos Simples, Compostos, Multivalorados e Derivados
description: "Propriedades e suas estruturas conceituais."
tags: [atributos, modelo-er]
aliases: [Atributos no Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Atributos Simples, Compostos, Multivalorados e Derivados

Atributo simples é tratado como valor indivisível para a finalidade; composto possui partes significativas; multivalorado admite várias ocorrências; derivado pode ser calculado.

| Tipo | Exemplo | Pergunta |
|---|---|---|
| simples | data de nascimento | é consultado como unidade? |
| composto | endereço postal | partes possuem significado? |
| multivalorado | telefones | ordem e tipo importam? |
| derivado | idade | deve ser persistido ou calculado? |

Idade muda com o tempo; data de nascimento é fato estável. Total do pedido pode ser derivado dos itens, mas persistência pode ser necessária para auditoria se a regra de cálculo variar.

Ausente, desconhecido e não aplicável são estados diferentes. Um atributo opcional precisa explicar por que pode faltar e em qual etapa se torna obrigatório.

> [!tip]
> Se um valor multivalorado possui atributos próprios, histórico ou identidade, ele é forte candidato a entidade relacionada.
