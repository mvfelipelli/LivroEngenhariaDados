---
title: Perguntas de Entrevista — ETL
aliases: [ETL Interview Questions]
tags: [engenharia-de-dados, fundamentos, etl, entrevistas]
type: interview
order: 12
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas para entrevistas sobre ETL."
---

# 12 — Perguntas de Entrevista

## Fundamentos e cenários

### 1. O que é ETL?

Extração consistente, transformação por regras e carga em contrato de destino.

### 2. Full load ou incremental?

Full simplifica reconstrução; incremental reduz custo, mas exige cursor, deletes, atrasos e idempotência.

### 3. O que é watermark?

Estado que delimita mudanças confirmadas. Deve desempatar valores iguais e avançar após commit.

### 4. Como detectar deletes?

CDC, tombstone, exclusão lógica, auditoria ou reconciliação completa periódica.

### 5. O que é idempotência?

Repetir a mesma entrada mantém o mesmo estado observável.

### 6. Por que usar staging?

Isola carga, permite validação e publicação atômica.

### 7. Append ou upsert?

Append para eventos imutáveis; upsert para estado mutável com chave e precedência.

### 8. Como tratar inválidos?

Bloquear o lote quando crítico ou quarentenar com motivo e linhagem; nunca descartar silenciosamente.

### 9. Como provar completude?

Reconciliar extraídos, carregados, rejeitados e filtros, além de chaves e somas de controle.

### 10. Como evitar JOIN multiplicativo?

Declarar grãos, testar cardinalidade e agregar antes de unir quando necessário.

### 11. Exactly-once é garantido pelo job?

Não sozinho. Exige garantia fim a fim; efeitos idempotentes são abordagem prática.

### 12. Como fazer backfill?

Preservar raw e versão, processar partições isoladas, validar, reconciliar e publicar controladamente.

### 13. O que monitorar?

Contagens, rejeições, duração, atraso, cursor, bytes, chaves, qualidade e versão.

### 14. Timeout significa falha sem efeito?

Não. O destino pode ter confirmado. Consulte estado e use idempotência antes de retry.

### 15. Como reduzir impacto na fonte?

Filtros indexados, paginação estável, lotes, réplica, limites e janela acordada.

### 16. O que torna transformação reprodutível?

Entrada imutável, regras versionadas, determinismo e estado persistido.

### 17. Como tratar evento atrasado?

Janela sobreposta, deduplicação e comparação de versão/tempo da origem.

### 18. Pipeline verde prova qualidade?

Não. Prova execução técnica; dados exigem testes e reconciliação.

## Próximo Capítulo

➡️ [[13-Exercicios|13 — Exercícios]]
