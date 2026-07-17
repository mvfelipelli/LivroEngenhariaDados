---
title: Modelos de Colaboração, Permissões e Forks
description: "Repositório compartilhado, fork, acesso e responsabilidade."
tags: [git, github, forks, permissoes]
aliases: [Fork Workflow, Permissões GitHub]
created: 2026-07-17
updated: 2026-07-17
---

# Modelos de Colaboração, Permissões e Forks

No modelo compartilhado, colaboradores criam branches no mesmo repositório. No modelo fork, cada pessoa propõe mudanças a partir de outro repositório. Fork reduz necessidade de escrita no upstream e é comum em open source.

| Modelo | Vantagem | Atenção |
| --- | --- | --- |
| branch compartilhada | CI e colaboração simples | usuários com escrita e branches não confiáveis |
| fork | isolamento de contribuição | segredos e workflows de código externo |
| espelho | redundância ou migração | direção de sincronização |

Permissões devem refletir função: leitura, triagem, escrita, manutenção e administração possuem impactos diferentes. Prefira equipes a concessões individuais, acesso temporário e revisão periódica.

```bash
git remote add upstream https://github.com/org/projeto.git
git fetch upstream
git switch -c feature upstream/main
```

Pull requests de forks são entrada não confiável. Workflows não devem expor segredos ao código proposto. O contexto `pull_request_target` exige desenho especialmente cuidadoso porque executa no contexto do repositório base.

> [!tip]
> Separe identidade humana, bot e GitHub App; cada uma precisa de escopo, owner e rotação.

Próximo: [[04-Estrategias-de-Branches-e-Ciclo-de-Vida]].
