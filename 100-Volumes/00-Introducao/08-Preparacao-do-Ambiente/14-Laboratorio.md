---
title: Laboratório — Auditoria do Ambiente
description: "Checklist reproduzível da estação de trabalho."
tags: [laboratorio, ambiente]
aliases: [Lab de Preparação]
created: 2026-07-21
updated: 2026-07-21
---

# Laboratório — Auditoria do Ambiente

## Objetivo

Produzir evidência de que a estação está pronta para os primeiros volumes.

## Pré-requisitos e ambiente

Terminal, Git e acesso ao Vault. Python, Java e Docker podem ser marcados como pendentes quando não forem exigidos pela trilha imediata.

## Passos

1. Crie uma tabela de componentes, comandos de versão e estado.
2. Confirme que o Vault abre e renderiza Wikilinks e Mermaid.
3. Crie e descarte com segurança um ambiente virtual de teste.
4. Inicie um serviço PostgreSQL de laboratório e aguarde o healthcheck.
5. Execute uma consulta simples e registre o resultado.
6. Pare o serviço sem remover o volume.
7. Documente duas falhas simuladas e seus diagnósticos.

## Validação

Nenhum segredo foi registrado; os comandos são repetíveis; cada estado possui evidência.

Veja [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/14-Solucao|Solução]].
