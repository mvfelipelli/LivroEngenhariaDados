---
title: Integração, Conflitos, Rebase, Squash e Cherry-pick
description: "Estratégias de integração e seus efeitos no grafo."
tags: [git, merge, rebase, squash]
aliases: [Estratégias de Merge, Cherry Pick]
created: 2026-07-17
updated: 2026-07-17
---

# Integração, Conflitos, Rebase, Squash e Cherry-pick

Merge commit preserva topologia; squash cria um novo commit consolidado; rebase reaplica commits sobre nova base; cherry-pick copia a mudança de commits selecionados.

| Estratégia | História | Uso típico |
| --- | --- | --- |
| merge | preserva branch e múltiplos pais | contexto de integração |
| squash | um commit na base | PR com commits intermediários |
| rebase | linha reescrita | atualizar branch privada |
| cherry-pick | copia commit específico | backport controlado |

Conflito precisa considerar versões, schema e ordem de migrations, não apenas remover marcadores. Após rebase ou atualização da base, aprovações podem ficar obsoletas conforme regra.

```bash
git fetch origin
git rebase origin/main
git range-diff origin/main...feature-antiga origin/main...feature-nova
```

`range-diff` ajuda a revisar alterações entre séries reescritas. Cherry-pick duplicará identidade do patch com novo commit; documente origem com `-x` em backports.

> [!warning]
> Não use rebase para apagar autoria, revisão ou incidentes. Histórico é ferramenta de colaboração, não estética isolada.

Continue em [[07-Protecoes-Rulesets-CODEOWNERS-e-Merge-Queue]].
