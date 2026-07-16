---
title: Contêineres e Isolamento no Linux
description: "Fundamentos de namespaces, cgroups, imagens, runtimes e operação segura de contêineres."
tags: [linux, containers, isolamento, volume-02]
aliases: [Módulo 05 Linux, Contêineres Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Módulo 05 — Contêineres e Isolamento no Linux

Contêineres não são máquinas virtuais pequenas. São processos comuns executados com visões isoladas do sistema, limites de recursos, privilégios reduzidos e um filesystem preparado a partir de uma imagem.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Processos-Namespaces-e-Isolamento|Processos, Namespaces e Isolamento]]
4. [[04-Cgroups-Recursos-e-Qualidade-de-Servico|Cgroups, Recursos e Qualidade de Serviço]]
5. [[05-Imagens-OCI-Camadas-e-Root-Filesystem|Imagens OCI, Camadas e Root Filesystem]]
6. [[06-Runtimes-Ciclo-de-Vida-e-Estado|Runtimes, Ciclo de Vida e Estado]]
7. [[07-Armazenamento-Volumes-e-Persistencia|Armazenamento, Volumes e Persistência]]
8. [[08-Rede-de-Containers-e-Descoberta-de-Servicos|Rede de Contêineres e Descoberta de Serviços]]
9. [[09-Seguranca-Supply-Chain-Observabilidade-e-Operacao|Segurança, Supply Chain, Observabilidade e Operação]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    I["Imagem imutável"] --> R["Runtime"]
    R --> P["Processo isolado"]
    P --> C["cgroups e política"]
    P --> V["dados persistentes"]
```
