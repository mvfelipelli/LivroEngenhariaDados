---
title: Preflight, Requisitos e Decisões de Instalação
description: "Verificações anteriores à instalação do ferramental."
tags: [preflight, requisitos, instalacao]
aliases: [Checklist de Preflight]
created: 2026-07-21
updated: 2026-07-21
---

# Preflight, Requisitos e Decisões de Instalação

Antes de instalar, registre sistema operacional, arquitetura do processador, memória, espaço livre e política de virtualização. Confirme permissões, proxy corporativo, DNS e portas que poderão ser usadas por serviços locais.

| Verificação | Comando indicativo | Resultado |
|---|---|---|
| Git | `git --version` | versão reconhecida |
| Python | `python --version` | runtime suportado |
| Java | `java -version` | versão compatível com Spark |
| Docker | `docker version` | cliente e daemon acessíveis |
| Porta 5432 | ferramenta do sistema | livre ou serviço conhecido |

Prefira gerenciadores oficiais e versões estáveis. Documente qualquer desvio de arquitetura, como WSL, máquina virtual ou execução remota.

Próximo: [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/04-Git-Editor-e-Obsidian|Git, Editor e Obsidian]].
