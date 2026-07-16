---
title: Gabarito — Redes e Conectividade no Linux
description: "Respostas orientativas dos exercícios de redes."
tags: [linux, redes, gabarito]
aliases: [Gabarito Redes Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Gabarito

1. Enlace usa quadro; IP, pacote; TCP, segmento; UDP, datagrama; aplicação, mensagem.
2. `UP` é estado administrativo; portadora é enlace; conectividade ainda depende de endereço, rota, política e serviço.
3. Ambos resolvem vizinhos locais; ARP atende IPv4, NDP usa ICMPv6 e possui funções adicionais.
4. Socket é endpoint; porta identifica multiplexação; processo possui o descritor do socket.
5. Blocos `/27` têm 32 endereços: rede `172.20.8.128`, broadcast `.159`, hosts usuais `.129` a `.158`.
6. Vence `/16`, pois é o prefixo mais específico que contém o destino.
7. Considere rota, retorno, vizinhança, firewall, NAT, listener, bind, saturação e políticas intermediárias.
8. Confira bind com `ss`, endereço e rota, firewall IPv4/IPv6, namespace, NAT e teste a partir da origem real.
9. Exemplos: `ip -brief link`, `ip -brief address`, `ip route`, `ip neigh` e `ss -lntup`.
10. `getent` segue NSS e pode usar `/etc/hosts`; consulta DNS direta pode não retornar `localhost`.
11. Permitir TCP da origem ao IP e porta definidos, stateful para retorno, negar o restante e registrar metadados da exceção.
12. Correlacione RTT, perda e retransmissão com tempos de DNS, conexão, TLS, primeiro byte e processamento servidor.
13. Crie namespaces, par `veth`, associe uma ponta a cada domínio ou bridge, atribua IPs, ative links e defina rotas.
14. Suspeite de MTU/PMTUD, buffers ou aplicação; teste tamanhos, observe ICMP e capture nas duas extremidades.
15. O cliente deve receber recusa ou timeout conforme o destino e a política; a evidência local deve mostrar ausência do listener esperado.

> [!note]
> O gabarito orienta o raciocínio. Em diagnóstico real, conclusões exigem evidências do ambiente e da janela do incidente.
