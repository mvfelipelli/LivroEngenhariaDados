---
title: Views, Contratos, Abstração e Dependências
description: "Views como interfaces relacionais estáveis e governadas."
tags: [sql, views, contratos]
aliases: [Views como Contratos]
created: 2026-07-17
updated: 2026-07-17
---

# Views, Contratos, Abstração e Dependências

Uma view nomeia uma consulta e apresenta seu resultado como relação. Ela pode ocultar complexidade, padronizar métricas, restringir colunas e desacoplar consumidores da estrutura física.

```sql
CREATE VIEW analytics.vw_receita_diaria AS
SELECT loja_id,
       CAST(criado_em AS DATE) AS data,
       SUM(valor) AS receita
FROM vendas.pedidos
WHERE status = 'pago'
GROUP BY loja_id, CAST(criado_em AS DATE);
```

O contrato inclui nomes, tipos, grão, significado, tratamento de `NULL`, filtros e política de atualização. `SELECT *` torna esse contrato vulnerável à adição ou reordenação de colunas; projeções explícitas são preferíveis.

## Atualizabilidade e barreiras

Views simples podem aceitar escrita, dependendo do SGBD. Agregações, joins e funções geralmente limitam a atualização. `WITH CHECK OPTION` impede que uma alteração via view produza linha fora de seu predicado:

```sql
CREATE VIEW app.pedidos_abertos AS
SELECT pedido_id, cliente_id, status
FROM core.pedidos
WHERE status = 'aberto'
WITH LOCAL CHECK OPTION;
```

Uma view não é automaticamente uma fronteira de segurança. Ownership, modo de execução, funções chamadas, permissões na base e recursos como `security_barrier` variam por produto.

> [!warning]
> Antes de alterar uma view, mapeie consumidores e dependências. A compatibilidade deve ser tratada como em [[08-Expand-Contract-Backfill-Compatibilidade-e-Rollback|expand-contract]].
