---
title: Laboratório — Correlação de Telemetria e SLO
aliases: [Laboratório de Observabilidade]
tags: [observabilidade, laboratorio, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Reconstrução de trace, avaliação de SLO e incidente idempotente."
---

# Laboratório — Correlação de Telemetria e SLO

## Objetivo

Reconstruir o caminho crítico do pipeline de pedidos da DataRetail S.A., correlacionar métricas de dados e registrar um incidente de freshness sem duplicação.

## Pré-requisitos

- Python 3.10 ou superior;
- biblioteca padrão;
- noções de traces, métricas e SLOs.

## Ambiente

Salve a solução como `observabilidade.py`. O programa usa SQLite temporário e remove o arquivo ao final.

## Passo a passo

1. Modele quatro spans sequenciais com o mesmo `trace_id`.
2. Some suas durações para obter o caminho crítico.
3. Converta a duração em freshness.
4. Compare freshness de oito minutos com SLO de cinco.
5. Verifique completude de 99,5% contra meta de 99%.
6. Abra incidente somente para os SLOs violados.
7. Persista duas vezes e confirme idempotência.

## Resultado esperado

```text
spans=4
caminho=extract>validate>transform>publish
caminho_critico_segundos=420
freshness_minutos=8.00
completude=99.50
alertas=1
incidente=INC-011
incidentes_persistidos=1
segunda_execucao=sem_duplicacao
observabilidade=ok
```

## Conclusão

O laboratório demonstra que trace explica latência, SLI determina impacto e uma chave estável evita alertas duplicados para o mesmo incidente.

Compare com [[14-Solucao]].
