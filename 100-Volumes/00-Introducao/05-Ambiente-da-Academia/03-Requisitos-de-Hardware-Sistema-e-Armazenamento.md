---
title: Requisitos de Hardware, Sistema e Armazenamento
description: "Capacidade local e alternativas para laboratórios."
tags: [hardware, sistema-operacional, armazenamento]
aliases: [Requisitos do Ambiente]
created: 2026-07-21
updated: 2026-07-21
---

# Requisitos de Hardware, Sistema e Armazenamento

Editor, Git, SQL e Python funcionam em máquinas modestas. Containers simultâneos, Spark e serviços de observabilidade exigem mais memória e disco. O requisito real depende do laboratório.

Referência confortável:

- CPU de 4 núcleos ou mais;
- 16 GB de RAM, com 8 GB para trilha básica;
- 40 GB livres para imagens, dados e ambientes;
- virtualização habilitada quando containers forem usados;
- conexão para baixar dependências, não para executar exemplos essenciais.

SSD reduz tempo de instalação e I/O. Monitore espaço usado por caches, imagens e logs. Quem possui menos recursos pode executar serviços por etapas, reduzir datasets ou usar ambiente remoto autorizado.

Backup protege notas e código; dados gerados devem ser recriáveis.
