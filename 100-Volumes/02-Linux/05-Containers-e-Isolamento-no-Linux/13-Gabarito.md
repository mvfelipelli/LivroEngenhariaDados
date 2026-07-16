---
title: Gabarito — Contêineres e Isolamento no Linux
description: "Respostas orientativas dos exercícios de contêineres."
tags: [linux, containers, gabarito]
aliases: [Gabarito Contêineres]
created: 2026-07-16
updated: 2026-07-16
---

# Gabarito

1. PID isola árvore; mount, mounts; network, interfaces e sockets; user, IDs e capabilities.
2. `chroot` muda caminhos; contêiner combina mecanismos; VM possui kernel convidado e fronteira do hipervisor.
3. Digest identifica blob; manifesto referencia config e camadas; config descreve execução; camada altera rootfs.
4. CPU causa throttling ao exceder quota; memória pode resultar em OOM kill quando reclaim não basta.
5. Entregue sinais diretamente, implemente drain, readiness false, ack ou devolução e período de graça compatível.
6. O blob anterior retém o segredo. Revogue-o, remova-o do contexto e reconstrua o histórico.
7. Verifique bind, namespace, listener, mapeamento, firewall, protocolo, IPv4/IPv6 e rota de retorno.
8. Observe working set, cache, heap, memória nativa, eventos OOM, limite, concorrência e tamanho dos registros.
9. Use UID dedicado, `read-only`, tmpfs limitado para temporários e volume com permissões mínimas para estado.
10. Requests devem refletir demanda normal; limits, pico testado. Monitore throttling, pressão, OOM, latência e fila.
11. Startup tolera migração; readiness só libera tráfego após dependências essenciais; liveness detecta travamento interno.
12. Build único produz digest assinado; testes promovem o mesmo digest, com configuração externa por ambiente.
13. Rootless reduz poder do daemon e mapeia IDs, mas pode ter restrições de portas, rede, storage e cgroups.
14. Permita somente resolvedor aprovado e destinos/portas do broker e banco, incluindo retorno stateful.
15. Conteúdo, ordem, metadata e serialização são normalizados; portanto, os bytes e digests se repetem.
