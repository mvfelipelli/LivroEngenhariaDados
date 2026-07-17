---
title: Gabarito
description: "Respostas dos exercícios de SQL em pipelines."
tags: [sql, gabarito, pipelines]
aliases: [Gabarito SQL em Pipelines]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Grão: uma tentativa de pagamento; chave: `pagamento_id`; invariantes: chave única, pedido existente, valor positivo, moeda válida e estado pertencente ao domínio.

## 2

Dados incompletos ficam visíveis, falhas podem misturar versões e rollback exige distinguir linhas novas das anteriores. Staging cria fronteira de validação.

## 3

```sql
WHERE (atualizado_em, pedido_id) > (:ultimo_instante, :ultimo_id)
ORDER BY atualizado_em, pedido_id
```

O identificador desempata todas as linhas com o mesmo instante.

## 4

Capture limite superior no início, releia desde `watermark - 6 horas`, deduplique por chave/versão e avance o watermark somente após publicação confirmada.

## 5

```sql
WITH x AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY evento_id ORDER BY versao DESC, ingerido_em DESC
    ) AS rn
    FROM staging_eventos
)
SELECT * FROM x WHERE rn = 1;
```

## 6

Compare versão ou `atualizado_em` no ramo de update e mantenha constraint única sobre a chave lógica.

## 7

Fato registra evento no seu grão; snapshot registra estado por período; SCD Tipo 2 versiona atributos dimensionais por validade.

## 8

Divida por partição mensal, estime bytes, publique em destino versionado, reconcilie cada período, limite concorrência, registre progresso idempotente e troque a view apenas após validação global.
