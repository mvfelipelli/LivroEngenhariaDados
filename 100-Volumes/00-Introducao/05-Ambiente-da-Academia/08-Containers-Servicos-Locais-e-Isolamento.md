---
title: Containers, Serviços Locais e Isolamento
description: "Ambientes descartáveis para bancos e plataformas."
tags: [containers, docker, isolamento]
aliases: [Containers na Academia]
created: 2026-07-21
updated: 2026-07-21
---

# Containers, Serviços Locais e Isolamento

Container empacota processo e dependências sobre o kernel do host. Imagem é o artefato; container é uma instância; volume persiste dados; rede conecta serviços.

Containers facilitam PostgreSQL, Trino, Airflow e observabilidade sem instalação direta, mas não eliminam consumo de recursos ou diferenças de arquitetura.

```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: academia
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```

Nunca publique portas ou credenciais além do necessário. Fixe imagens, use healthchecks e saiba remover/recriar o ambiente. Dados importantes precisam de backup, não apenas volume local.
