---
title: Mudança, Histórico, Validade e Tempo de Conhecimento
description: "Eixos temporais e políticas de correção."
tags: [validade, tempo-de-sistema, historico]
aliases: [Tempos no Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Mudança, Histórico, Validade e Tempo de Conhecimento

Tempo de validade indica quando um atributo vale no domínio. Tempo de conhecimento indica quando o warehouse recebeu ou acreditou nessa versão. Uma correção retroativa separa esses eixos.

## Categorias de mudança

- correção de erro: pode substituir ou exigir auditoria;
- mudança real: normalmente cria nova validade;
- reclassificação analítica: pode demandar visão “como era” e “como é hoje”;
- enriquecimento: preenche atributo antes desconhecido;
- fusão de identidades: exige regras de survivor e lineage.

Intervalos semiabertos `[desde, até)` evitam ambiguidades em fronteiras. `atual` é atributo derivável, mas pode acelerar lookup se mantido consistentemente.

> [!warning]
> Usar apenas `updated_at` não preserva o que mudou, quando passou a valer nem o que era conhecido antes.
