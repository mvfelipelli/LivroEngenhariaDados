---
title: Exercícios — Redes e Conectividade no Linux
description: "Exercícios progressivos de redes e diagnóstico."
tags: [linux, redes, exercicios]
aliases: [Exercícios Redes Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Exercícios

## Revisão

1. Relacione quadro, pacote, segmento e mensagem às camadas.
2. Diferencie interface `UP`, link ativo e conectividade funcional.
3. Explique ARP e Neighbor Discovery.
4. Diferencie socket, porta e processo.

## Interpretação

5. Calcule rede, broadcast e hosts usuais de `172.20.8.141/27`.
6. Explique a seleção entre rotas `10.0.0.0/8` e `10.20.0.0/16` para `10.20.30.40`.
7. Um nome resolve corretamente, mas a porta retorna timeout. Liste hipóteses por camada.
8. Um serviço funciona em `curl localhost`, mas não remotamente. Proponha uma sequência de checks.

## Aplicação

9. Colete, sem alterar estado, interfaces, endereços, rotas, vizinhos e listeners de um host Linux.
10. Compare a resolução de `localhost` por `getent` e por uma consulta DNS direta.
11. Desenhe uma regra mínima para pipeline `10.30.4.0/24` acessar PostgreSQL `10.50.2.10:5432`.
12. Defina métricas para distinguir perda de rede de lentidão da aplicação.

## Desafios

13. Modele dois namespaces conectados por `veth` e bridge, incluindo endereços e rotas.
14. Proponha investigação para conexões que funcionam com 100 bytes e travam com 10 KiB.
15. Execute [[14-Laboratorio]], altere a porta esperada e explique o erro observado.

Consulte [[13-Gabarito]] depois de registrar suas hipóteses.
