---
title: Custo, Cardinalidade, Seletividade e Estatísticas
description: "Como estimativas orientam decisões do otimizador."
tags: [sql, custo, cardinalidade, estatisticas]
aliases: [Estimativas do Otimizador]
created: 2026-07-17
updated: 2026-07-17
---

# Custo, Cardinalidade, Seletividade e Estatísticas

**Cardinalidade** é a quantidade de linhas em uma relação ou saída intermediária. **Seletividade** é a fração que sobrevive a um predicado. Se um milhão de pedidos contém dez mil do segmento procurado, a seletividade aproximada é 1%.

O custo é uma unidade comparativa do otimizador, não necessariamente milissegundos. Ele modela componentes como páginas lidas, CPU por tupla, ordenação e comunicação. Uma decisão errada de cardinalidade propaga-se: o banco pode escolher nested loop para uma entrada que, na prática, contém milhões de linhas.

## Fontes de estimativa

- contagem de linhas e valores distintos;
- fração de `NULL`;
- histogramas e valores mais frequentes;
- correlação entre ordem física e valores;
- estatísticas multicoluna para dependências entre atributos.

Considere `estado = 'SP' AND cidade = 'São Paulo'`. Tratar os predicados como independentes subestima ou superestima a saída, pois cidade e estado são correlacionados. Estatísticas estendidas podem representar essa dependência.

```sql
-- PostgreSQL: atualizar estatísticas depois de uma carga relevante
ANALYZE pedidos;

-- Dependência entre colunas correlacionadas
CREATE STATISTICS st_localidade (dependencies)
ON estado, cidade FROM clientes;
ANALYZE clientes;
```

> [!tip]
> Compare `rows` estimadas com linhas reais em cada nível. A primeira divergência grande costuma explicar escolhas ruins acima dela.
