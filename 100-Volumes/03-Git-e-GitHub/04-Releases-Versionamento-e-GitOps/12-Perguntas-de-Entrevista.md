---
title: Perguntas de Entrevista — Releases e GitOps
description: "Questões práticas com respostas fundamentadas."
tags: [entrevista, releases, gitops]
aliases: [Entrevista Releases e GitOps]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Tag e release são iguais?

Não. Tag é uma referência Git; release é uma publicação associada a uma tag, com notas, ativos e metadados.

## 2. Quando incrementar major?

Quando uma mudança quebra a API pública definida. A decisão depende do contrato, não do tamanho da alteração.

## 3. Por que construir uma vez?

Para promover os mesmos bytes e eliminar diferenças introduzidas por reconstruções entre ambientes.

## 4. Digest e assinatura resolvem o mesmo problema?

Não. Digest prova identidade do conteúdo; assinatura liga conteúdo a uma identidade verificável.

## 5. Quais são os princípios de GitOps?

Estado declarativo, versionado e imutável, obtido automaticamente e continuamente reconciliado.

## 6. Push CD e pull GitOps diferem como?

No push, o pipeline chama o ambiente. No pull, um agente observa a fonte e aplica a intenção, reduzindo a distribuição de credenciais externas.

## 7. O que é drift?

Diferença entre estado desejado e observado, causada por mudança manual, falha parcial ou comportamento externo.

## 8. Como tratar segredos?

Com referência a secret manager ou conteúdo cifrado, identidade mínima, rotação e auditoria; nunca em texto claro.

## 9. Rollback sempre é seguro?

Não. Mudanças irreversíveis de schema ou dados podem exigir roll-forward e estratégias expand-contract.

## 10. Como medir GitOps?

Tempo e sucesso de reconciliação, idade de drift e métricas de entrega, conectadas a SLOs e decisões operacionais.

## 11. Qual o papel do CI?

Testar, construir e produzir evidências. O reconciliador é responsável por convergir o ambiente.

## 12. Como fazer uma mudança emergencial?

Usar break-glass auditado, com escopo e expiração, e registrar imediatamente a intenção no Git para encerrar o drift.
