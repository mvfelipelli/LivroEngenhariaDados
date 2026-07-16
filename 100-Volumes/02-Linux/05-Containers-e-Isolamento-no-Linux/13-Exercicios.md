---
title: Exercícios — Contêineres e Isolamento no Linux
description: "Exercícios progressivos sobre contêineres Linux."
tags: [linux, containers, exercicios]
aliases: [Exercícios Contêineres]
created: 2026-07-16
updated: 2026-07-16
---

# Exercícios

## Revisão

1. Relacione PID, mount, network e user namespace às suas visões.
2. Compare contêiner, `chroot` e máquina virtual.
3. Explique digest, manifesto, configuração e camada OCI.
4. Diferencie limite de CPU e limite de memória.

## Interpretação

5. Uma aplicação ignora `SIGTERM` e perde mensagens em rollout. Diagnostique.
6. Um arquivo secreto foi copiado e removido em instruções posteriores. Explique o risco.
7. Um serviço funciona dentro do contêiner, mas não pela porta publicada. Liste checks.
8. Um worker sofre OOM após aumentar concorrência. Proponha evidências.

## Aplicação

9. Desenhe execução com usuário não root, rootfs somente leitura, tmpfs e volume.
10. Defina requests, limits e métricas para um job de dados.
11. Modele health checks para API com migração inicial lenta.
12. Defina política de promoção por digest entre ambientes.

## Desafios

13. Compare rootful e rootless quanto a segurança e limitações.
14. Desenhe rede mínima para worker acessar DNS, broker e banco.
15. Execute [[14-Laboratorio]] e explique por que duas construções têm digest igual.

Consulte [[13-Gabarito]] após elaborar as respostas.
