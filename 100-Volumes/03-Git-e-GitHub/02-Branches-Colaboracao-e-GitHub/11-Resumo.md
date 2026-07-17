---
title: Resumo — Branches, Colaboração e GitHub
description: "Síntese do fluxo de colaboração protegido."
tags: [git, github, resumo]
aliases: [Resumo Colaboração GitHub]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

Colaboração eficaz reduz divergência, torna contexto visível e aplica política antes da integração. Branch, PR, revisão, check e ruleset têm responsabilidades diferentes.

```mermaid
mindmap
  root((Colaboração))
    Proposta
      issue
      branch curta
      pull request
    Verificação
      revisão
      CODEOWNERS
      CI e scans
    Integração
      merge ou squash
      rulesets
      merge queue
    Governança
      permissões
      release e deploy
      auditoria
```

## Regras essenciais

1. Use menor privilégio e equipes com owner.
2. Mantenha branches curtas e mudanças pequenas.
3. Explique impacto em dados, testes e rollback.
4. Proteja branch, workflows e CODEOWNERS.
5. Exija checks estáveis e revisões relevantes.
6. Trate código de fork como não confiável.
7. Fixe Actions por SHA completo e limite tokens.
8. Ligue issue, PR, commit, release e deploy.

Revise em [[12-Perguntas-de-Entrevista]] e [[13-Exercicios]].
