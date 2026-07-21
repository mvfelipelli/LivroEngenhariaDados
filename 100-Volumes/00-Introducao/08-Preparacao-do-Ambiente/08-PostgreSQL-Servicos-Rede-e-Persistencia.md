---
title: PostgreSQL, Serviços, Rede e Persistência
description: "Configuração de um banco local seguro e verificável."
tags: [postgresql, rede, persistencia]
aliases: [Setup PostgreSQL]
created: 2026-07-21
updated: 2026-07-21
---

# PostgreSQL, Serviços, Rede e Persistência

Execute PostgreSQL nativamente ou em container, mas documente versão, host, porta, banco e usuário. Separe credenciais administrativas das usadas pela aplicação.

```bash
psql --host localhost --port 5432 --username dataretail --dbname dataretail
```

O teste mínimo cria uma tabela temporária, insere uma linha, consulta e encerra. Para containers, use volume nomeado e healthcheck com `pg_isready`. Evite publicar a porta em interfaces externas quando o laboratório só precisa de acesso local.

Backup e persistência são conceitos diferentes: volume preserva estado entre reinícios; backup permite restauração independente desse volume.

Próximo: [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/09-Testes-de-Fumaca-Diagnostico-e-Limpeza|Testes de Fumaça]].
