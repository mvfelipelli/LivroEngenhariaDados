---
title: Perguntas de Entrevista — Redes no Linux
description: "Perguntas progressivas com respostas fundamentadas."
tags: [linux, redes, entrevista]
aliases: [Entrevista Redes Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Perguntas de Entrevista

## 1. Qual a diferença entre MAC, IP e porta?

MAC identifica enlace local, IP identifica interface e permite roteamento, e porta multiplexa o transporte entre processos.

## 2. O que significa `/24`?

Que os primeiros 24 bits formam o prefixo. Em IPv4 restam 8 bits, totalizando 256 endereços no bloco.

## 3. Como o Linux escolhe uma rota?

Aplica regras de política e consulta tabelas, priorizando o prefixo mais específico; métricas resolvem alternativas conforme configuração.

## 4. TCP e UDP diferem em quê?

TCP oferece fluxo confiável e ordenado com estado e congestionamento. UDP entrega datagramas sem essas garantias.

## 5. `0.0.0.0:5432` e `127.0.0.1:5432` significam o quê?

O primeiro bind aceita endereços IPv4 locais; o segundo apenas loopback. Firewall e aplicação ainda controlam acesso.

## 6. Por que `ping` não valida um banco?

Ele testa ICMP e parte do caminho. Não testa listener, TCP, TLS, autenticação nem protocolo SQL.

## 7. Quando usar `getent` em vez de `dig`?

Quando se deseja reproduzir o resolvedor da aplicação, incluindo NSS e `/etc/hosts`. `dig` investiga DNS diretamente.

## 8. O que causa `connection refused`?

Resposta ativa sem listener compatível ou rejeição explícita. É diferente de timeout, embora middleboxes possam alterar sinais.

## 9. O que é MTU black hole?

Pacotes pequenos funcionam, mas maiores somem porque excedem o caminho e mensagens necessárias ao Path MTU Discovery são filtradas.

## 10. NAT é firewall?

Não. NAT traduz endereços ou portas; firewall decide permitir ou negar. Podem coexistir no mesmo mecanismo.

## 11. Como diagnosticar lentidão?

Separe DNS, conexão, TLS e resposta; meça RTT, perda, retransmissão, filas, throughput e tempo da aplicação, comparando origens.

## 12. O que um network namespace isola?

Interfaces, rotas, sockets, regras e outros objetos da pilha de rede, permitindo topologias virtuais por processo ou contêiner.

## 13. Como capturar pacotes com segurança?

Com autorização, filtro mínimo, duração curta, armazenamento protegido, revisão de dados sensíveis e descarte controlado.

## 14. Como provar que o problema está no firewall?

Correlacione tentativa, rota, captura na origem e destino, contadores ou logs da regra e teste controlado. Ausência de resposta isolada não prova a causa.
