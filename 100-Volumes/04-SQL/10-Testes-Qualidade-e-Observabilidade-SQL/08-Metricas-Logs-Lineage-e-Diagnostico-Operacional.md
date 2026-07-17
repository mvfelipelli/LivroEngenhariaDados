---
title: Métricas, Logs, Lineage e Diagnóstico Operacional
description: "Contexto necessário para explicar a produção de um dado."
tags: [sql, metricas, logs, lineage]
aliases: [Observabilidade Operacional SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Métricas, Logs, Lineage e Diagnóstico Operacional

Uma execução deve registrar `run_id`, versão do código, parâmetros, janela, watermark, linhas lidas/inseridas/atualizadas/rejeitadas, duração e resultado dos testes.

```sql
INSERT INTO controle_execucao (
    run_id, modelo, iniciado_em, linhas_lidas, status
) VALUES (:run_id, :modelo, CURRENT_TIMESTAMP, :linhas, 'executando');
```

Logs explicam eventos; métricas mostram tendência; lineage conecta dependências. Nenhum deles substitui os outros. Propague o mesmo identificador entre orquestrador, consulta e alerta.

## Diagnóstico

1. delimite consumidores e período afetados;
2. encontre primeira transformação divergente;
3. compare entradas, versões e parâmetros;
4. separe atraso, perda, duplicação e corrupção;
5. restaure serviço com ação reversível;
6. preserve evidências para causa raiz.

> [!warning]
> Não registre dados pessoais ou credenciais apenas para facilitar depuração. Metadados e fingerprints costumam ser suficientes.
