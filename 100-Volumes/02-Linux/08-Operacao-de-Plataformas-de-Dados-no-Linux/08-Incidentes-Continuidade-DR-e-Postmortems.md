---
title: Incidentes, Continuidade, DR e Postmortems
description: "Resposta coordenada e recuperação de plataformas de dados."
tags: [linux, operacao, incidentes, disaster-recovery]
aliases: [DR de Dados, Incidentes Operacionais]
created: 2026-07-16
updated: 2026-07-16
---

# Incidentes, Continuidade, DR e Postmortems

Incidente é desvio que ameaça serviço ou dados e exige coordenação. Defina comandante, comunicação, especialistas e registro da linha do tempo. Separe mitigação imediata de investigação profunda.

## Continuidade e DR

Análise de impacto identifica processos críticos, dependências, RPO e RTO. O plano deve cobrir perda de host, zona, identidade, storage, rede e equipe. Failover só é útil se dados, DNS, credenciais e capacidade estiverem prontos.

```mermaid
sequenceDiagram
    participant M as Monitoramento
    participant I as Incidente
    participant R as Recuperação
    participant V as Validação
    M->>I: detecta impacto
    I->>R: decide failover ou restore
    R->>V: serviço e dados
    V-->>I: RPO, RTO e integridade
```

Exercícios de mesa validam decisões; testes técnicos validam execução. Registre tempo, lacuna, dependências e ações manuais.

Postmortem sem culpa descreve impacto, detecção, linha do tempo, fatores contribuintes, o que funcionou e ações com owner e prazo. “Erro humano” encerra investigação cedo demais.

> [!warning]
> Declare desastre apenas por autoridade definida. Failover precipitado pode criar split-brain ou perda adicional.

Continue em [[09-Capacidade-Mudancas-Custo-e-Melhoria-Continua]].
