---
title: Laboratório — View Mínima e Consulta Parametrizada
description: "Demonstração reproduzível de exposição controlada no SQLite."
tags: [sql, sqlite, laboratorio, seguranca]
aliases: [Laboratório de Segurança SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — View Mínima e Consulta Parametrizada

## Objetivo

Publicar dados necessários por uma view, bloquear leitura direta da tabela com o autorizador do SQLite e demonstrar que entrada maliciosa permanece valor em uma consulta parametrizada.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie `pedidos` com identificador, cliente, e-mail, status e valor.
2. Publique `vw_pedidos_publicos` sem e-mail e apenas com pedidos pagos.
3. Configure `set_authorizer` para permitir leituras da tabela somente quando originadas pela view.
4. Consulte a view e valide sua projeção.
5. Confirme que a leitura direta é negada.
6. Use uma entrada semelhante a injection em predicado parametrizado.
7. Confirme que nenhuma linha indevida é retornada.

## Validação esperada

```text
linhas_view=2
colunas_sensiveis=omitidas
leitura_direta=negada
consulta_parametrizada=segura
resultado=ok
```

> [!note]
> O autorizador é um recurso da conexão SQLite usado para o experimento. Em produção, roles, grants, views e políticas do SGBD devem formar o controle persistente.

Consulte [[14-Solucao|Solução]].
