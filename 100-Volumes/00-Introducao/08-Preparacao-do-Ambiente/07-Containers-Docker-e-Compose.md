---
title: Containers, Docker e Compose
description: "Execução isolada de serviços locais."
tags: [docker, containers, compose]
aliases: [Setup de Containers]
created: 2026-07-21
updated: 2026-07-21
---

# Containers, Docker e Compose

Uma imagem empacota o ambiente; um container é uma instância; um volume preserva dados; uma rede conecta serviços. Compose declara o conjunto necessário ao laboratório.

```bash
docker version
docker compose version
docker run --rm hello-world
```

Fixe tags de imagem, use healthchecks, nomes claros e limites de recursos. Variáveis sensíveis devem vir do ambiente ou de um arquivo local ignorado pelo Git. `docker compose down` remove containers e rede; volumes somente devem ser removidos com intenção explícita.

Próximo: [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/08-PostgreSQL-Servicos-Rede-e-Persistencia|PostgreSQL]].
