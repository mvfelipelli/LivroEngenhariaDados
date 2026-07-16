---
title: Introdução a Desempenho, Troubleshooting e Observabilidade
description: "Modelo causal para investigar comportamento de sistemas."
tags: [linux, desempenho, introducao]
aliases: [Introdução Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Introdução

“O servidor está lento” não é um diagnóstico. É preciso definir operação, população afetada, janela, latência, taxa de erros, carga e expectativa. O mesmo uso de CPU pode ser saudável em um batch e crítico em uma API.

## Três disciplinas

| Disciplina | Pergunta |
| --- | --- |
| performance analysis | qual recurso ou caminho limita o objetivo? |
| troubleshooting | qual hipótese explica o desvio observado? |
| observabilidade | quais sinais permitem explicar o estado interno? |

```mermaid
flowchart TD
    U["Usuário percebe latência"] --> A["serviço e dependências"]
    A --> K["kernel e recursos"]
    K --> H["hardware ou infraestrutura"]
    A --> T["telemetria correlacionada"]
```

Mude uma variável por vez, registre antes e depois, preserve relógios e compare com período saudável. Reiniciar pode restaurar serviço, mas também apagar estado necessário para descobrir a causa.

> [!warning]
> Correlação não prova causalidade. CPU alta durante lentidão pode ser causa, consequência ou trabalho útil.

Comece em [[03-Metodo-Baselines-USE-e-RED]].
