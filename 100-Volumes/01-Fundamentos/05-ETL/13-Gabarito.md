---
title: Gabarito — ETL
aliases: [Gabarito de ETL]
tags: [engenharia-de-dados, fundamentos, etl, gabarito]
type: answer-key
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Respostas orientativas dos exercícios de ETL."
---

# 13 — Gabarito

1. Extrair captura; transformar aplica contrato; carregar publica com semântica definida.
2. Snapshot é simples e caro; watermark é eficiente e stateful; CDC captura operações, inclusive delete, com maior complexidade.
3. O ID desempata timestamps iguais e evita lacunas.
4. Fonte, schema, intervalo, cursor, execução, contagem e checksum.
5. Append acrescenta; upsert insere/atualiza por chave; replace substitui conjunto delimitado.
6. UTC explícito, decimal com arredondamento e motivo de ausência documentado.
7. CDC, tombstone, soft delete, auditoria ou reconciliação.
8. Extraídos = válidos carregados + rejeitados + filtros documentados.
9. Consultar efeito, repetir por chave única/upsert e avançar cursor só após confirmação.
10. `(source_system, source_order_id, line_number)`.
11. Fonte → raw → staging → transformação; inválidos → quarentena; válidos → publicação e auditoria.
12. Cursor composto, sobreposição e deduplicação com precedência da origem.
13. Schema, domínio, unicidade, referências, cardinalidade, contagem, somas e atualidade.
14. Congelar versão, processar partições, validar, reconciliar e trocar controladamente.
15. Medir cardinalidade e grão; agregar lados ou separar fatos antes do JOIN.
16. Atualidade até 7h, completude, rejeições, duração, cursor e tempo de recuperação.
17. Bloqueie quando compromete o produto; quarentene casos isolados rastreáveis conforme contrato.
18. Filtros indexados, lotes, réplica, limites, janela e monitoramento.
19. Permite auditoria, correção de regras e reconstrução.
20. Deve incluir contrato, chave, cursor, raw, regras, staging, carga, idempotência, reconciliação, métricas e runbook.

## Próximo Capítulo

➡️ [[14-Laboratorio|14 — Laboratório]]
