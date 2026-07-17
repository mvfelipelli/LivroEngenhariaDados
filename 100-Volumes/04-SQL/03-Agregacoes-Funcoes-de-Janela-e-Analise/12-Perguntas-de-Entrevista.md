---
title: Perguntas de Entrevista — Agregações e Janelas
description: "Questões práticas com respostas fundamentadas."
tags: [sql, entrevista, window-functions]
aliases: [Entrevista Análise SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. GROUP BY e função de janela diferem como?

O primeiro reduz linhas por grupo; a segunda preserva linhas e calcula sobre uma janela.

## 2. COUNT(*) e COUNT(coluna) diferem como?

O primeiro conta linhas; o segundo ignora valores nulos.

## 3. WHERE e HAVING diferem como?

`WHERE` filtra antes da agregação; `HAVING`, depois.

## 4. Por que média de médias pode estar errada?

Porque grupos com tamanhos distintos recebem o mesmo peso. Use soma e contagem ou média ponderada.

## 5. PARTITION BY e ORDER BY fazem o quê?

Partição separa conjuntos independentes; ordem define sequência dentro deles.

## 6. ROW_NUMBER, RANK e DENSE_RANK diferem como?

Sequência única; empates com lacunas; empates sem lacunas.

## 7. Como obter top N por grupo?

Calcule ranking em CTE ou subconsulta e filtre no nível externo.

## 8. Por que LAST_VALUE surpreende?

Porque o frame padrão com ordem termina no peer atual, não necessariamente no fim da partição.

## 9. ROWS e RANGE diferem como?

`ROWS` conta linhas posicionais; `RANGE` considera valores e peers da ordenação.

## 10. Como calcular acumulado determinístico?

Ordenação total e frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

## 11. Como comparar períodos ausentes?

Crie grade de calendário, agregue ao período e só então aplique `LAG`.

## 12. Como testar uma métrica de janela?

Reconcilie totais e cubra empates, limites, nulos, lacunas e partições pequenas.
