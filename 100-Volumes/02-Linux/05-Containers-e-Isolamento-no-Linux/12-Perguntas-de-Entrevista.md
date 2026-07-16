---
title: Perguntas de Entrevista — Contêineres Linux
description: "Perguntas progressivas com respostas fundamentadas."
tags: [linux, containers, entrevista]
aliases: [Entrevista Contêineres]
created: 2026-07-16
updated: 2026-07-16
---

# Perguntas de Entrevista

## 1. Contêiner é uma máquina virtual?

Não. É um conjunto de processos que compartilha o kernel do host e recebe isolamento e limites por primitivas do kernel.

## 2. Namespaces e cgroups diferem em quê?

Namespaces restringem visibilidade e identidade de recursos; cgroups contabilizam e controlam consumo.

## 3. Por que PID 1 é especial?

Ele recebe sinais no namespace, adota órfãos e deve colher filhos. Sua semântica influencia término gracioso e processos zumbis.

## 4. Tag e digest são equivalentes?

Não. Tag é referência mutável; digest deriva do conteúdo e fornece identidade verificável.

## 5. O que é uma camada?

Um blob, normalmente tar compactado, aplicado em ordem ao root filesystem. Whiteouts representam remoções de camadas anteriores.

## 6. Por que apagar segredo em outra camada não resolve?

Porque a camada original continua armazenada e recuperável. É necessário revogar e reconstruir sem o segredo.

## 7. Volume e camada gravável diferem em quê?

O volume possui ciclo independente e persistência definida; a camada acompanha a instância e costuma ser descartável.

## 8. O que acontece no limite de memória?

Reclaim e pressão antecedem o limite; se insuficientes, o OOM killer pode encerrar processos do cgroup.

## 9. `EXPOSE` publica uma porta?

Não. É metadata. Publicação exige configuração do runtime ou orquestrador.

## 10. Por que usar forma JSON no entrypoint?

Evita shell intermediário, preserva argumentos e facilita entrega de sinais ao processo correto.

## 11. Readiness e liveness diferem em quê?

Readiness controla recebimento de tráfego; liveness decide recuperação por reinício. Confundi-las pode criar cascatas.

## 12. Contêiner root equivale a root no host?

Nem sempre, devido a user namespaces e capabilities, mas pode manter grande poder. Deve ser evitado e avaliado no contexto.

## 13. Como reduzir risco da supply chain?

Fixar fontes, builds isolados, SBOM, scan contextual, assinatura, proveniência, admissão e promoção pelo mesmo digest.

## 14. Como diagnosticar reinício frequente?

Correlacione exit code, sinal, OOM, probe, eventos, logs anteriores, pressão de recursos, configuração e dependências.
