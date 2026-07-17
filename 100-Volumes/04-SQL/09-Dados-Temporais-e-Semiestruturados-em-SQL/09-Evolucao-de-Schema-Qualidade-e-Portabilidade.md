---
title: Evolução de Schema, Qualidade e Portabilidade
description: "Contratos versionados para payloads e recursos específicos de SGBD."
tags: [sql, schema-evolution, qualidade, portabilidade]
aliases: [Evolução de JSON em SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Evolução de Schema, Qualidade e Portabilidade

Semiestruturado não significa sem schema; significa schema carregado junto aos dados ou aplicado na leitura. Inclua versão e mantenha leitores compatíveis durante a transição.

```sql
SELECT CASE json_extract(payload, '$.schema_version')
         WHEN 1 THEN json_extract(payload, '$.total') * 100
         WHEN 2 THEN json_extract(payload, '$.total_centavos')
       END AS total_centavos
FROM eventos;
```

O padrão expand-contract também se aplica: escritores passam a emitir o campo novo, leitores aceitam ambos, histórico é migrado quando necessário e o campo antigo é removido após observação.

## Qualidade

- JSON válido e versão reconhecida;
- campos obrigatórios presentes;
- tipos coerentes por caminho;
- datas em formato e timezone definidos;
- arrays dentro de limites;
- identidade e chave de deduplicação presentes;
- valores desconhecidos encaminhados à quarentena.

Funções, operadores, tipos JSON e recursos temporais variam amplamente. Isole SQL específico, crie testes de contrato por plataforma e evite assumir que representação textual preserva a mesma semântica.

> [!warning]
> Alterar o significado de um campo mantendo o mesmo nome e versão é quebra de contrato silenciosa.
