---
title: Proteções, Rulesets, CODEOWNERS e Merge Queue
description: "Políticas aplicáveis a branches, tags e integração."
tags: [github, rulesets, codeowners, merge-queue]
aliases: [Branch Protection, GitHub Rulesets]
created: 2026-07-17
updated: 2026-07-17
---

# Proteções, Rulesets, CODEOWNERS e Merge Queue

Proteções e rulesets transformam política em enforcement. Rulesets podem se acumular quando múltiplos conjuntos atingem a mesma ref e oferecem estados para avaliar uma regra antes de aplicá-la plenamente.

## Regras úteis

- exigir pull request e aprovações;
- invalidar aprovação após novos commits;
- exigir resolução de conversas;
- exigir status checks e base atualizada;
- bloquear force push e exclusão;
- exigir commits assinados ou deploy de staging;
- restringir caminhos, tamanho ou tipos de arquivo quando disponível.

`CODEOWNERS` solicita revisores por padrões. A proteção precisa exigir revisão de code owner para torná-la bloqueante. Coloque o arquivo em local suportado e proteja o próprio arquivo.

```text
*.sql              @dataretail/db
/infra/            @dataretail/platform
/.github/workflows/ @dataretail/security @dataretail/platform
```

Merge queue testa mudanças em combinação com a base mais recente, reduzindo a janela em que PRs individualmente verdes quebram juntas. Bypass deve ser raro, registrado e sujeito a revisão posterior.

> [!note]
> Disponibilidade de rulesets e regras específicas varia por visibilidade e plano. Confirme a documentação atual do GitHub.

Próximo: [[08-Issues-Projetos-Releases-e-Rastreabilidade]].
