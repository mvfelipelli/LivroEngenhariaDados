---
title: Gabarito — Modelagem de Dados
aliases: [Gabarito de Modelagem]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, gabarito]
type: answer-key
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Respostas orientativas dos exercícios de Modelagem de Dados."
---

# 13 — Gabarito

> [!note]
> Respostas alternativas são válidas quando preservam as regras e justificam consequências.

1. Modelagem é descoberta, representação, validação e evolução; modelo é um artefato resultante.
2. Conceitual trata significado; lógico organiza por paradigma; físico implementa em tecnologia concreta.
3. Pedido é entidade; data é atributo; cliente realiza pedido é relacionamento.
4. Candidata é identificador mínimo; primária é a candidata escolhida; alternativa é outra candidata; estrangeira referencia uma chave.
5. Mínima indica participação opcional ou obrigatória; máxima limita uma ou muitas ocorrências.
6. `TELEFONE_CLIENTE` como entidade dependente com número, tipo, verificação e vigência, relacionada `1:N` ao cliente.
7. Cada duplicata recebe ID distinto. Uma chave de negócio ou regra de resolução continua necessária.
8. `pedido_id → pedido_data` e `produto_id → produto_nome`; ambas dependem de parte da chave.
9. Receita é aditiva; estoque é semiaditivo no tempo; margem percentual é não aditiva.
10. O `JOIN` produz até 12 combinações por pedido e multiplica valores. Modele fatos separadas ou agregue no grão compatível.
11. Deve representar cliente `1:N` pedido, pedido `1:N` item, produto `1:N` item e pedido `1:N` pagamento.
12. Chave natural `(loja_id, numero_pedido)` ou `(sistema_origem, id_origem)`, preservada mesmo com chave substituta.
13. `CLIENTE(cliente, nome_cliente)`, `PRODUTO(produto, nome_produto)`, `PEDIDO(pedido, data, cliente)` e `ITEM(pedido, produto, quantidade)`.
14. Uma linha por linha confirmada do pedido; quantidade, bruto, desconto e líquido, com fórmula e moeda declaradas.
15. Dimensão versionada com chave substituta, chave de negócio e vigência; fato aponta para a versão válida no evento.
16. `ENTREGA` e `ITEM_ENTREGA` referenciando `ITEM_PEDIDO`; soma entregue por linha menor ou igual à comprada, protegida transacionalmente.
17. Adicionar anulável, adaptar produtores, executar backfill, medir cobertura, migrar consumidores e aplicar `NOT NULL`.
18. Testes de duplicidade por chave, órfãos, contagem por grão e igualdade de totais elegíveis entre origem e destino.
19. Normalização protege escrita e fatos únicos; estrela facilita análise. O modelo analítico é derivado e reconciliado com o operacional.
20. Deve conter propósito, glossário, níveis, identidades, cardinalidades, invariantes, tempo, fatos/dimensões, contratos, migração e donos.

## Próximo Capítulo

➡️ [[14-Laboratorio|14 — Laboratório]]
