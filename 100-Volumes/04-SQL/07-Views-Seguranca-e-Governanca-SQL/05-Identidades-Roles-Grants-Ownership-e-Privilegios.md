---
title: Identidades, Roles, Grants, Ownership e Privilégios
description: "Modelo de autorização e responsabilidade sobre objetos SQL."
tags: [sql, roles, grants, ownership]
aliases: [Autorização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Identidades, Roles, Grants, Ownership e Privilégios

**Autenticação** confirma uma identidade; **autorização** decide o que ela pode fazer. Contas humanas, aplicações, pipelines e administradores devem possuir identidades distintas, preferencialmente federadas ou com credenciais curtas.

Roles representam funções, não pessoas. O PostgreSQL permite compor roles e conceder privilégios em objetos:

```sql
CREATE ROLE relatorio_leitura NOLOGIN;
GRANT USAGE ON SCHEMA analytics TO relatorio_leitura;
GRANT SELECT ON analytics.vw_receita_diaria TO relatorio_leitura;
GRANT relatorio_leitura TO analista_ana;
```

`USAGE` no schema não concede `SELECT` nas relações. Ownership é mais poderoso que privilégios comuns: o proprietário pode alterar ou remover o objeto e normalmente administrar concessões. Objetos não devem pertencer a contas pessoais.

## Privilégios futuros

```sql
ALTER DEFAULT PRIVILEGES FOR ROLE owner_analytics
IN SCHEMA analytics
GRANT SELECT ON TABLES TO relatorio_leitura;
```

Default privileges dependem do role criador e não corrigem objetos existentes. É necessário testar o caminho completo de criação.

> [!warning]
> Evite contas compartilhadas e grants diretamente a indivíduos; ambos dificultam revogação, atribuição e auditoria.
