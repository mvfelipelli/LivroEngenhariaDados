---
title: Segurança por Linha, Coluna, Mascaramento e Privacidade
description: "Controles de exposição conforme identidade, finalidade e sensibilidade."
tags: [sql, rls, mascaramento, privacidade]
aliases: [Row Level Security e Mascaramento]
created: 2026-07-17
updated: 2026-07-17
---

# Segurança por Linha, Coluna, Mascaramento e Privacidade

Segurança por linha restringe quais tuplas uma identidade pode observar ou modificar. No PostgreSQL, Row-Level Security aplica políticas após ser habilitada:

```sql
ALTER TABLE core.pedidos ENABLE ROW LEVEL SECURITY;

CREATE POLICY pedidos_por_loja ON core.pedidos
FOR SELECT TO operador_loja
USING (loja_id = current_setting('app.loja_id')::bigint);
```

O contexto de sessão precisa ser definido por um componente confiável e não reutilizado incorretamente em pools. Proprietários, superusuários e roles com `BYPASSRLS` podem contornar políticas; teste com a identidade real da aplicação.

## Colunas e mascaramento

Views podem omitir ou transformar atributos:

```sql
CREATE VIEW atendimento.clientes AS
SELECT cliente_id,
       nome,
       CONCAT('***', RIGHT(telefone, 4)) AS telefone_mascarado
FROM core.clientes;
```

Mascaramento não é anonimização: combinações de atributos podem reidentificar pessoas. Hash sem segredo também pode ser revertido por dicionário. Tokenização, agregação, generalização e remoção devem ser escolhidas conforme ameaça e finalidade.

> [!important]
> Classificação orienta o controle: dados públicos, internos, confidenciais e restritos não devem receber o mesmo tratamento.
