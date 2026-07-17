---
title: Processos de Negócio, Bus Matrix e Declaração do Grão
description: "Ponto de partida do desenho dimensional."
tags: [processos, bus-matrix, grao]
aliases: [Bus Matrix e Grão]
created: 2026-07-17
updated: 2026-07-17
---

# Processos de Negócio, Bus Matrix e Declaração do Grão

Processo de negócio é atividade mensurável: venda, pagamento, entrega ou estoque diário. Bus matrix cruza processos com dimensões conformadas e orienta entregas incrementais integráveis.

| Processo | Data | Produto | Cliente | Loja |
|---|---:|---:|---:|---:|
| Vendas | ✓ | ✓ | ✓ | ✓ |
| Estoque diário | ✓ | ✓ |  | ✓ |
| Entregas | ✓ |  | ✓ | ✓ |

Declaração de grão deve ser frase concreta: “uma linha por item vendido, no instante da confirmação, por pedido”. Só depois são escolhidas dimensões e fatos.

Grão atômico preserva capacidade de responder perguntas futuras. Agregados podem ser derivados, enquanto detalhe ausente não pode ser recuperado.

> [!warning]
> “Uma linha por venda” é ambíguo: pedido, item, pagamento e remessa são grãos diferentes.
