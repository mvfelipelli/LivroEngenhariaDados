---
title: Perguntas de Entrevista
description: "Perguntas e respostas sobre segurança e governança SQL."
tags: [sql, entrevista, seguranca]
aliases: [Entrevista de Segurança SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Uma view melhora segurança automaticamente?

Não. Ela pode reduzir exposição, mas permissões, ownership, modo de execução e acesso às tabelas precisam formar a fronteira correta.

## 2. View comum e materializada: qual a diferença?

A comum executa a definição ao ser consultada; a materializada persiste resultado e precisa de refresh e contrato de frescor.

## 3. Por que usar roles funcionais?

Elas desacoplam pessoas de privilégios, facilitando aprovação, revisão, revogação e auditoria.

## 4. O que é menor privilégio?

Conceder apenas capacidades necessárias, sobre o escopo necessário e durante o tempo necessário.

## 5. O que RLS protege?

Quais linhas podem ser vistas ou alteradas conforme política e identidade. Não substitui controle de colunas nem criptografia.

## 6. Mascaramento anonimiza dados?

Não necessariamente. Dados mascarados podem continuar identificáveis isoladamente ou por combinação.

## 7. Como parâmetros evitam injection?

O driver transmite valores separadamente da estrutura SQL, impedindo que o valor seja interpretado como operador ou cláusula.

## 8. Como parametrizar um nome de coluna?

Não se usa placeholder de valor. Mapeia-se a opção solicitada para uma allowlist de identificadores conhecidos.

## 9. O que deve constar de uma auditoria?

Identidade, ação, objeto, instante, origem, resultado e correlação, evitando segredos e dados desnecessários.

## 10. Como governar um acesso temporário?

Com justificativa, aprovação, role restrita, expiração automática, auditoria e revisão posterior.
