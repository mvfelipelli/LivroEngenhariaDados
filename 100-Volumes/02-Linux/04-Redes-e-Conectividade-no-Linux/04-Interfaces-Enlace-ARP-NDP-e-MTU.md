---
title: Interfaces, Enlace, ARP, NDP e MTU
description: "Funcionamento do enlace local e interfaces Linux."
tags: [linux, redes, ethernet, mtu]
aliases: [Enlace Linux, Interfaces de Rede]
created: 2026-07-16
updated: 2026-07-16
---

# Interfaces, Enlace, ARP, NDP e MTU

Uma interface pode representar hardware, loopback, bridge, VLAN, túnel ou endpoint virtual. Seu estado administrativo (`UP`) não garante portadora, endereço válido ou caminho funcional.

## Rede local

Ethernet entrega quadros dentro de um domínio de camada 2. Para enviar a um IPv4 local, o host resolve o IP para MAC com ARP. No IPv6, Neighbor Discovery usa ICMPv6 e também descobre roteadores e alcançabilidade.

```bash
ip -details link show
ip neigh show
ip -s link show dev eth0
```

A tabela de vizinhos pode exibir `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `FAILED` ou `INCOMPLETE`. Estados incompletos sugerem problema local, VLAN incorreta, vizinho ausente ou filtro.

## MTU

MTU é o maior pacote que uma interface transmite sem fragmentação naquela camada. Túneis acrescentam cabeçalhos e reduzem a carga disponível. *Path MTU Discovery* tenta descobrir o menor limite do caminho; ICMP bloqueado pode produzir conexões que abrem, mas travam com mensagens maiores.

```bash
ip link show dev eth0
ping -M do -s 1472 192.0.2.10
```

O segundo exemplo testa 1500 bytes em IPv4 ao somar 20 bytes de IP e 8 de ICMP. Ajuste ao ambiente; não assuma que todos os caminhos usam Ethernet ou MTU 1500.

> [!tip]
> Contadores de `dropped`, `errors` e `overruns` ganham significado quando comparados em um intervalo, não como valor isolado desde o boot.

Continue em [[05-Enderecamento-IP-Sub-redes-e-Roteamento]].
