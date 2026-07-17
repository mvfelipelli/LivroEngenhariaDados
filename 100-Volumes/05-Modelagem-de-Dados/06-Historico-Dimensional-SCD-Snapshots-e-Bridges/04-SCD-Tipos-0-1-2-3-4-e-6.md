---
title: SCD Tipos 0, 1, 2, 3, 4 e 6
description: "Padrões de tratamento de mudanças dimensionais."
tags: [scd, slowly-changing-dimension]
aliases: [Tipos de SCD]
created: 2026-07-17
updated: 2026-07-17
---

# SCD Tipos 0, 1, 2, 3, 4 e 6

| Tipo | Estratégia | Uso |
|---|---|---|
| 0 | manter original | atributo imutável |
| 1 | sobrescrever | correção sem análise histórica |
| 2 | nova linha/versionamento | histórico completo por validade |
| 3 | colunas atual/anterior | uma mudança limitada |
| 4 | histórico separado | atual simples, histórico dedicado |
| 6 | híbrido 1+2+3 | visão histórica e atual combinadas |

O “tipo” não é propriedade da dimensão inteira; atributos diferentes podem ter políticas diferentes. Nome corrigido pode usar Tipo 1, enquanto segmento usa Tipo 2.

Tipo 3 preserva apenas quantidade limitada de versões. Tipo 6 aumenta complexidade e deve ser usado quando consultas justificam atributos atuais propagados pelas versões.

> [!tip]
> Documente política por atributo, evento que a aciona e impacto sobre fatos existentes.
