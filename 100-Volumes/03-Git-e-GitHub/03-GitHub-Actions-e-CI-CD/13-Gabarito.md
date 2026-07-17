---
title: Gabarito — GitHub Actions e CI/CD
description: "Respostas orientativas dos exercícios."
tags: [github-actions, ci-cd, gabarito]
aliases: [Gabarito GitHub Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Evento dispara workflow; jobs formam DAG; steps executam comandos/actions; action é unidade reutilizável.
2. Cache otimiza, artifact preserva arquivos, output transmite valor pequeno.
3. Matrix expande combinações, needs ordena DAG, concurrency limita sobreposição.
4. Secret é sensível, variable não; OIDC cria identidade curta; environment aplica contexto e gates.
5. Código não confiável pode exfiltrar segredo; remova acesso e separe contexto privilegiado.
6. Ambientes podem receber bytes diferentes; construa uma vez e promova por digest.
7. Use concurrency, lock da migration, idempotência, compatibilidade e aprovação.
8. Referência é mutável; fixe SHA completo validado.
9. Lint, unitário, contrato, SQL, integração, scans e build após gates.
10. Default sem escrita; conceda conteúdo, packages, id-token ou deployments apenas ao job necessário.
11. Build gera digest; staging testa; gate aprova; produção recebe o mesmo artefato.
12. Trust policy restringe issuer, audience, organização, repo, ref/environment.
13. Hospedado é efêmero gerenciado; self-hosted oferece controle e rede, com maior risco operacional.
14. Interface tipada, permissões mínimas, pinning, changelog, owners e compatibilidade.
15. O validador deve detectar que nem todos os jobs podem ser ordenados.
