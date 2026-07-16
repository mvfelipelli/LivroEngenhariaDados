---
title: Objetivos — Contêineres e Isolamento no Linux
description: "Resultados de aprendizagem sobre contêineres Linux."
tags: [linux, containers, objetivos]
aliases: [Objetivos Contêineres Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Objetivos

Ao concluir este módulo, você será capaz de:

- explicar por que contêiner é processo isolado, não virtualização completa;
- distinguir namespaces, cgroups, capabilities, seccomp e LSM;
- interpretar imagens OCI, manifestos, camadas, digests e tags;
- compreender o ciclo entre engine, runtime de alto e baixo nível;
- projetar persistência sem gravar estado importante na camada gravável;
- explicar redes de contêineres, portas publicadas e descoberta;
- limitar CPU, memória, PIDs e I/O com critérios operacionais;
- reduzir privilégios e riscos da cadeia de suprimentos;
- observar saúde, logs, sinais e encerramento gracioso;
- validar uma imagem determinística no laboratório.

## Critério de conclusão

O leitor deve conseguir revisar uma carga conteinerizada, identificar fronteiras de isolamento e executar [[14-Laboratorio|o laboratório]] duas vezes com o mesmo digest.
