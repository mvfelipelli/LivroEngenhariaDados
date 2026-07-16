---
title: Rede de Contêineres e Descoberta de Serviços
description: "Namespaces de rede, bridges, NAT, portas e DNS de serviços."
tags: [linux, containers, redes]
aliases: [Rede de Contêineres, Portas Publicadas]
created: 2026-07-16
updated: 2026-07-16
---

# Rede de Contêineres e Descoberta de Serviços

Um contêiner costuma receber network namespace próprio, uma ponta `veth`, endereço e rota. A outra ponta conecta-se a bridge ou dataplane do host. Publicar porta adiciona encaminhamento ou proxy; expor no metadata da imagem não cria acesso externo.

```mermaid
flowchart LR
    A["processo no contêiner"] --> V["veth"]
    V --> B["bridge ou dataplane"]
    B --> N["interface do host"]
    N --> X["rede externa"]
```

```bash
docker network inspect rede_dados
docker port api
nsenter -t "$PID" -n ip route
```

## Bind e publicação

Um serviço que escuta em `127.0.0.1` dentro do namespace não aceita tráfego destinado ao endereço do contêiner. Escutar em todas as interfaces pode ser necessário internamente, enquanto firewall e publicação limitam o acesso externo.

Descoberta de serviços traduz identidade lógica em endpoints. Clientes devem respeitar TTL, múltiplos endereços, conexões persistentes e mudanças de instância. IP de contêiner é efêmero; use nome ou serviço estável.

## Comunicação e política

Bridge, host networking, overlay e plugins CNI oferecem trade-offs. Host networking reduz isolamento e compartilha portas. Overlay atravessa nós com encapsulamento e MTU adicional. Network policies precisam controlar entrada e saída, DNS e dependências explícitas.

> [!note]
> `localhost` sempre referencia o namespace do processo. Em um contêiner, normalmente não é o host nem outro serviço.

Revise os fundamentos relacionados em [[04-Redes-e-Conectividade-no-Linux/README|Redes e Conectividade no Linux]] e avance para [[09-Seguranca-Supply-Chain-Observabilidade-e-Operacao]].
