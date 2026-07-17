---
title: Perguntas de Entrevista — Objetos e Tipagem Python
description: "Questões sobre classes, dataclasses e typing."
tags: [python, entrevista, tipagem]
aliases: [Entrevista Objetos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Atributo de classe e de instância diferem como?

O primeiro pertence à classe e é compartilhado na busca; o segundo fica no estado da instância.

## 2. Python possui atributos privados?

Há convenção `_nome` e name mangling com `__nome`, mas não isolamento de segurança absoluto.

## 3. Quando preferir composição?

Quando componentes têm ciclos de vida ou políticas independentes e não existe relação de substituição.

## 4. O que é MRO?

A ordem linearizada usada para buscar métodos em hierarquias, especialmente com herança múltipla.

## 5. Frozen dataclass é profundamente imutável?

Não. Ela bloqueia reatribuição de campos, mas objetos mutáveis referenciados continuam mutáveis.

## 6. Type hints alteram execução?

Em geral, não aplicam o contrato; ferramentas estáticas os interpretam e o runtime os armazena.

## 7. Protocol e ABC diferem como?

Protocol permite compatibilidade estrutural; ABC normalmente define relação nominal e pode fornecer implementação.

## 8. `cast` valida um valor?

Não. Ele apenas instrui o analisador e retorna o mesmo objeto em runtime.
