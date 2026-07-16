---
title: Usuários, Grupos, Permissões e Sudo
aliases: [Permissões Linux]
tags: [linux, usuarios, grupos, permissoes, sudo]
created: 2026-07-16
updated: 2026-07-16
description: "Identidade, autorização e elevação de privilégio no Linux."
---

# Usuários, Grupos, Permissões e Sudo

Processos executam com UID e grupos. Arquivos possuem owner, grupo e bits para usuário, grupo e outros. Em arquivos, `r`, `w` e `x` significam ler, alterar e executar; em diretórios, listar nomes, alterar entradas e atravessar.

```text
-rwxr-x--- 1 dataeng analytics 2048 pipeline.sh
```

```bash
id
chmod 750 pipeline.sh
chgrp analytics pipeline.sh
umask 027
```

Permissão numérica soma leitura `4`, escrita `2` e execução `1`. `750` concede tudo ao owner, leitura e execução ao grupo e nada aos outros.

## Sudo

`sudo` executa comando segundo política, com auditoria e privilégio delimitado. Evite sessão root permanente. Serviços devem usar identidades próprias, sem login quando possível, e acesso mínimo aos diretórios necessários.

Bits especiais e ACLs ampliam o modelo, mas exigem uso consciente. O sticky bit em diretórios compartilhados restringe remoção de entradas por terceiros.

> [!tip]
> Defina `umask` antes de criar arquivos sensíveis; corrigir permissões depois pode deixar uma janela de exposição.

Processos são aprofundados em [[07-Processos-Sinais-Servicos-e-Recursos]].
