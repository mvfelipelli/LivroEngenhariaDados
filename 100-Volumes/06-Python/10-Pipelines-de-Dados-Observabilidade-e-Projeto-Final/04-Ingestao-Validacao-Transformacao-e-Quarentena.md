---
title: Ingestão, Validação, Transformação e Quarentena
description: "Fronteira de qualidade e isolamento de registros."
tags: [python, ingestao, validacao, quarentena]
aliases: [Quarentena de Dados Python]
created: 2026-07-20
updated: 2026-07-20
---

# Ingestão, Validação, Transformação e Quarentena

Ingestão preserva origem e metadados antes de normalizar. Validação ocorre em camadas: sintaxe, schema, domínio e relações.

Transformações devem tornar unidade e grão explícitos. Um registro inválido conhecido pode ir para quarentena; falha sistêmica, como banco indisponível, encerra o lote.

Quarentena registra source, posição, código de erro, versão do contrato e hash do payload. Payload sensível é protegido ou referenciado, não copiado para logs.

Defina limiar: poucas rejeições podem permitir publicação com alerta; taxa alta deve falhar o lote. Reprocessamento da quarentena usa versão conhecida da regra e deixa trilha de auditoria.

Nunca capture `Exception` por registro e continue silenciosamente: defeitos de código não são qualidade de dados.
