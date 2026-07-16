---
title: Sistema de Arquivos, Caminhos e Tipos
aliases: [Filesystem Linux]
tags: [linux, filesystem, caminhos, arquivos]
created: 2026-07-16
updated: 2026-07-16
description: "Hierarquia, caminhos, inodes, links e manipulação segura."
---

# Sistema de Arquivos, Caminhos e Tipos

O filesystem organiza nomes em uma árvore iniciada por `/`. Caminhos absolutos começam na raiz; relativos começam no diretório atual. `.` representa o diretório atual e `..`, o pai.

| Caminho | Uso comum |
|---|---|
| `/etc` | configuração do sistema |
| `/var` | dados variáveis, filas e logs |
| `/home` | diretórios de usuários |
| `/tmp` | temporários |
| `/proc` | visão de processos e kernel |
| `/dev` | dispositivos |

Um nome aponta para um inode com tipo, permissões, owner, timestamps e referências aos dados. Link físico referencia o mesmo inode; link simbólico armazena outro caminho.

```bash
pwd
ls -lah
find . -type f -name '*.csv'
file dados/pedidos.csv
```

Aspas protegem espaços e expansões. Use `--` antes de nomes que podem começar com hífen. Antes de remover ou mover recursivamente, confirme o caminho resolvido e o conteúdo.

> [!warning]
> Globs são expandidos pelo shell antes da execução. Uma variável vazia ou sem aspas pode mudar radicalmente o alvo.

Identidade e proteção são tratadas em [[06-Usuarios-Grupos-Permissoes-e-Sudo]].
