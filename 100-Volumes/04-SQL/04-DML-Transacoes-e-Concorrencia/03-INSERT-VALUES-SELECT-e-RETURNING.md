---
title: INSERT, VALUES, SELECT e RETURNING
description: "Criação de linhas, cargas derivadas e leitura dos resultados."
tags: [sql, insert, returning]
aliases: [INSERT SQL]
created: 2026-07-17
updated: 2026-07-17
---

# INSERT, VALUES, SELECT e RETURNING

`INSERT` cria linhas a partir de valores explícitos ou de uma consulta. Nomear colunas protege contra evolução e mudança de ordem física.

```sql
INSERT INTO clientes (cliente_id, nome, ativo)
VALUES (101, 'Ana', TRUE);
```

```sql
INSERT INTO clientes_ativos (cliente_id, nome)
SELECT cliente_id, nome
FROM staging_clientes
WHERE ativo = TRUE;
```

Inserções em lote reduzem viagens de rede, mas precisam de limites de memória, tamanho e rollback. Constraints continuam sendo a última barreira.

Em mecanismos que oferecem `RETURNING`, a aplicação obtém valores gerados e o estado realmente persistido:

```sql
INSERT INTO pedidos (cliente_id, valor)
VALUES (101, 250.00)
RETURNING pedido_id, criado_em;
```

```mermaid
flowchart LR
    F["Valores ou SELECT"] --> I["INSERT"]
    I --> C["Constraints e defaults"]
    C --> R["RETURNING"]
```

Evite inserir e depois buscar “o último identificador” por ordenação global: outra sessão pode escrever entre as sentenças. Use recurso transacional do mecanismo.
