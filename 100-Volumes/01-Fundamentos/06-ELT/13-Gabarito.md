---
title: Gabarito — ELT
aliases: [Gabarito de ELT]
tags: [engenharia-de-dados, fundamentos, elt, gabarito]
type: answer-key
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Respostas orientativas dos exercícios de ELT."
---

# 13 — Gabarito

1. A diferença é o local e momento da transformação; requisitos decidem.
2. Landing recebe, raw preserva, staging padroniza e mart publica semântica.
3. Origem, lote, ingestão, arquivo, checksum, schema e posição.
4. Raw contém versões, sensibilidade e regras não estabilizadas.
5. View calcula na leitura; tabela materializa; incremental atualiza mudanças.
6. Uma linha por item confirmado, com chave composta declarada.
7. Raw → staging → intermediários → marts; dependências unidirecionais.
8. Unicidade no grão, FKs lógicas, status aceitos e não nulos.
9. Reprocessar janela e fazer merge idempotente por chave/versão.
10. Comparar chaves, contagens e medidas entre incremental e rebuild.
11. Detectar, classificar compatibilidade, versionar e migrar dependentes.
12. Raw restrito; staging para engenharia; mart por domínio/consumidor.
13. Medir scans, filtrar, particionar, reutilizar intermediários e materializar.
14. Registrar fonte → raw → staging → mart → dashboard, incluindo versões.
15. Cópia diverge; intermediário centraliza regra testada.
16. Usar membro desconhecido ou retry e corrigir depois com métrica.
17. Compilar, lint, DAG, testes unitários e modelos afetados.
18. Adicionar substituta, migrar, medir uso, comunicar e remover após prazo.
19. Quando finalidade, privacidade ou regulação proíbem raw identificável.
20. Deve incluir ingestão, camadas, DAG, testes, materializações, segurança, custo e SLO.

## Próximo Capítulo

➡️ [[14-Laboratorio|14 — Laboratório]]
