---
title: Gerenciamento de Pacotes e Atualizações
aliases: [Pacotes Linux]
tags: [linux, pacotes, atualizacoes, repositorios]
created: 2026-07-16
updated: 2026-07-16
description: "Repositórios, dependências, atualização e rollback de pacotes."
---

# Gerenciamento de Pacotes e Atualizações

Gerenciadores de pacotes resolvem dependências, verificam assinaturas, instalam arquivos e mantêm banco de estado. APT e DNF usam modelos semelhantes com comandos diferentes.

```bash
sudo apt update
apt list --upgradable
sudo apt install pacote
```

```bash
sudo dnf check-update
sudo dnf install pacote
```

Repositórios precisam de origem, chave e escopo controlados. Fixar versões melhora previsibilidade, mas exige processo de atualização. Correções de segurança devem respeitar criticidade, compatibilidade, janela e reboot necessário.

## Estratégia

Teste em lote pequeno, monitore, amplie gradualmente e preserve rollback. Registre versão anterior e arquivos de configuração. Remover pacote pode deixar dados ou dependências órfãs; revise explicitamente.

> [!warning]
> Executar script remoto diretamente no shell elimina inspeção, verificação de integridade e reprodutibilidade.

Serviços instalados são operados em [[05-Systemd-Servicos-Timers-e-Journal]].
