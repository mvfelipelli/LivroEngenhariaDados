---
title: Perguntas de Entrevista sobre Administração Linux
aliases: [Entrevista Administração Linux]
tags: [linux, administracao, entrevista]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas sobre administração do sistema Linux."
---

# Perguntas de Entrevista

## 1. `enable` e `start` diferem como?

`enable` configura ativação futura, normalmente no boot; `start` inicia agora.

## 2. Como investigar serviço que não inicia?

Status, journal, unidade, dependências, identidade, permissões, portas, configuração e recursos.

## 3. O que é mount?

Associação de um filesystem a um diretório da árvore.

## 4. Por que usar UUID no fstab?

Nomes de dispositivos podem mudar; UUID identifica o filesystem de forma mais estável.

## 5. Porta em LISTEN garante acesso?

Não. Bind, firewall, rota e políticas externas ainda podem bloquear.

## 6. RPO e RTO significam o quê?

Perda temporal tolerada e tempo-alvo de recuperação.

## 7. RAID substitui backup?

Não; não protege contra exclusão, corrupção lógica, ataque ou falha compartilhada.

## 8. Como controlar atualização?

Inventário, teste, lote pequeno, observação, rollout, rollback e evidência.

## 9. O que é drift?

Divergência entre estado real e estado desejado.

## 10. Como planejar capacidade?

Medir tendência e pico, definir margem, conhecer limites e tempo de expansão.

Pratique em [[13-Exercicios]].
