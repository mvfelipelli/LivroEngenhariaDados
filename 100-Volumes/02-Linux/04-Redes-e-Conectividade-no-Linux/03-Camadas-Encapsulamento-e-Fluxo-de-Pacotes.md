---
title: Camadas, Encapsulamento e Fluxo de Pacotes
description: "Modelos OSI e TCP/IP, encapsulamento e processamento no Linux."
tags: [linux, redes, tcp-ip]
aliases: [Camadas de Rede, Encapsulamento]
created: 2026-07-16
updated: 2026-07-16
---

# Camadas, Encapsulamento e Fluxo de Pacotes

Camadas separam responsabilidades e permitem substituir uma tecnologia sem reescrever todo o sistema. O modelo OSI é uma referência de sete camadas; o modelo TCP/IP agrupa funções em aplicação, transporte, internet e acesso à rede.

| Dados | Unidade | Identificação principal |
| --- | --- | --- |
| aplicação | mensagem | nome, URL ou protocolo |
| transporte | segmento/datagrama | portas |
| internet | pacote | endereço IP |
| enlace | quadro | endereço MAC |

## Encapsulamento

```mermaid
sequenceDiagram
    participant A as Aplicação
    participant T as TCP
    participant I as IP
    participant E as Ethernet
    A->>T: mensagem HTTP ou PostgreSQL
    T->>I: segmento com portas
    I->>E: pacote com IPs
    E->>E: quadro com MACs e verificação
```

No envio, cada camada acrescenta metadados. No recebimento, o kernel valida e remove cabeçalhos até entregar bytes ao socket do processo. Switches encaminham principalmente por enlace; roteadores, por IP; proxies podem interpretar a aplicação.

```bash
ip -brief link
ip -brief address
ip route show
ss -tn state established
```

Esses comandos observam, respectivamente, enlace, endereçamento, decisão de rota e transporte. Uma investigação eficiente registra horário, origem, destino e resultado em cada fronteira.

## Erros comuns

- tratar o modelo em camadas como implementação rígida;
- confundir pacote IP com quadro Ethernet;
- concluir que toda falha é “da rede” antes de testar o protocolo;
- capturar tráfego sem autorização ou proteção de dados.

Próximo: [[04-Interfaces-Enlace-ARP-NDP-e-MTU]].
