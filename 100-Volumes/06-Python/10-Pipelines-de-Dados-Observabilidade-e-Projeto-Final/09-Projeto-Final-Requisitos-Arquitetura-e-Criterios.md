---
title: Projeto Final — Requisitos, Arquitetura e Critérios
description: "Especificação do projeto integrador do Volume 06."
tags: [python, projeto-final, requisitos]
aliases: [Especificação Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Projeto Final — Requisitos, Arquitetura e Critérios

## Cenário

Processar eventos versionados de pedidos da DataRetail S.A. para uma tabela SQLite de estado atual.

## Requisitos funcionais

- ler CSV incrementalmente por número de linha;
- validar ID, versão, status e centavos;
- aplicar maior versão por pedido;
- colocar registros inválidos em quarentena;
- atualizar checkpoint junto com os dados;
- suportar reexecução sem duplicidade.

## Requisitos operacionais

- configuração por argumentos;
- logging JSON com run_id;
- métricas reconciliadas;
- saída sem segredos;
- código de retorno não zero em falha sistêmica;
- laboratório autossuficiente.

## Critérios de aceite

O pipeline deve produzir três pedidos atuais, um registro em quarentena, total aprovado de `4500` centavos, checkpoint final correto e estado idêntico após a segunda execução.
