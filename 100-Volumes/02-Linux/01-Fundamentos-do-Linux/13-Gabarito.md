---
title: Gabarito dos Exercícios de Fundamentos do Linux
aliases: [Gabarito do Módulo Linux]
tags: [linux, gabarito, modulo-01]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios de Linux."
---

# Gabarito

1. Kernel gerencia recursos; shell interpreta comandos; distribuição integra kernel, utilitários e pacotes.
2. Absoluto inicia em `/`; relativo parte do diretório atual; `.` é atual e `..` é pai.
3. Owner lê e escreve; grupo lê; outros não acessam.
4. Programa é código, processo é instância em execução e serviço é processo supervisionado de longa duração.
5. Pode listar nomes, mas não atravessar para acessar metadados ou conteúdo das entradas.
6. Confirmar PID e impacto, enviar SIGTERM, aguardar e diagnosticar; SIGKILL somente se necessário.
7. stdout e stderr são fluxos distintos; é preciso redirecionar ou preservar o descritor 2 explicitamente.
8. Divisão em argumentos, expansão de glob e alvo inesperado, inclusive operação fora do diretório pretendido.
9. `mkdir -p workspace/{incoming,processing,quarantine,archive,logs}`.
10. `chmod 750` nos diretórios, combinado com grupo correto e `umask 027`.
11. `cut -d, -f4 arquivo.csv | sort | uniq -c`, para CSV simples sem campos escapados.
12. `ps`, `top`, `free`, `df`, `du` e ferramentas equivalentes.
13. `mkdir -p`, escrita condicional ou atômica e verificações de pós-condição.
14. Criar com `mktemp -d` e registrar `trap 'rm -rf -- "$tmp"' EXIT` após validar origem do caminho.
15. `sha256sum incoming/* > manifest.sha256`, controlando ausência de arquivos e expansão.
16. Conferir que arquivos novos não concedem permissões a outros e que a configuração esperada permanece ativa.

Continue em [[14-Laboratorio]].
