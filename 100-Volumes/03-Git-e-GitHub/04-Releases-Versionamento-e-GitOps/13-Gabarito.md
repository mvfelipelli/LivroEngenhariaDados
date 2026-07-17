---
title: Gabarito — Releases, Versionamento e GitOps
description: "Respostas orientadoras dos exercícios."
tags: [gabarito, releases, gitops]
aliases: [Gabarito Releases e GitOps]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Versão expressa compatibilidade; tag referencia Git; release publica; artefato é a unidade; deploy altera ambiente.
2. Declarativo, versionado e imutável, pulled automaticamente e continuamente reconciliado.
3. `2.4.0`, se o campo for realmente retrocompatível.
4. Pode produzir bytes distintos por dependências, toolchain ou tempo.
5. Drift: o reconciliador deve corrigir ou alertar conforme política.
6. Testes, contrato, digest, assinatura, SBOM, política, aprovação e SLO pós-deploy.
7. Tags anotadas e assinadas, SemVer, proteção contra alteração e release ligada ao digest.
8. Referências a um secret manager ou valores cifrados, com identidade mínima, rotação e auditoria.
9. Promover o mesmo digest a uma fração do tráfego; comparar erro, latência e saúde dos dados; pausar ou reverter ao exceder limites.
10. Autorizar por papel específico, limitar tempo e escopo, registrar comandos, abrir incidente e criar PR de reconciliação.

Respostas podem variar, mas devem preservar identidade imutável, separação de funções e retorno ao estado declarado.
