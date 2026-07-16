---
title: Resumo de Fundamentos do Linux
aliases: [Resumo do Módulo Linux]
tags: [linux, resumo, modulo-01]
created: 2026-07-16
updated: 2026-07-16
description: "Síntese dos fundamentos do sistema Linux."
---

# Resumo

- O kernel gerencia recursos; o shell coordena programas.
- Distribuições combinam kernel, utilitários, pacotes e políticas.
- Caminhos formam uma árvore iniciada em `/`.
- Inodes mantêm metadados; nomes referenciam inodes.
- Processos executam com identidade, grupos e ambiente.
- Permissões diferem em arquivos e diretórios.
- `sudo` aplica elevação delimitada e auditável.
- Sinais comunicam eventos a processos.
- stdout, stderr, códigos de saída e pipes sustentam composição.
- Aspas, validação de caminhos e menor privilégio evitam acidentes.
- Scripts idempotentes e evidências melhoram recuperação.

```mermaid
mindmap
  root((Linux))
    Sistema
      Kernel
      Shell
      Distribuição
    Recursos
      Arquivos
      Processos
      Memória
    Segurança
      Usuários
      Permissões
      Sudo
    Automação
      Pipes
      Scripts
      Códigos de saída
```

Continue em [[12-Perguntas-de-Entrevista]] e [[13-Exercicios]].
