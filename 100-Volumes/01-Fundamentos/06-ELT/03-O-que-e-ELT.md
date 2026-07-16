---
title: O que é ELT
aliases: [Extract Load Transform]
tags: [engenharia-de-dados, fundamentos, elt]
type: chapter
order: 03
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Definição, comparação com ETL e critérios de adoção de ELT."
---

# 03 — O que é ELT

**ELT** extrai dados, carrega uma representação próxima da fonte na plataforma de destino e executa transformações ali.

| Aspecto | ETL | ELT |
| --- | --- | --- |
| Transformação | antes do destino final | dentro da plataforma |
| Raw no destino | opcional | central ao reprocessamento |
| Compute | engine intermediário | engine do destino |
| Latência de disponibilidade bruta | maior | menor |
| Governança | no pipeline e destino | fortemente na plataforma |

Nenhum padrão é universalmente superior. ELT é adequado quando a plataforma suporta isolamento, escala, SQL e governança; ETL pode ser necessário para mascarar dados antes da carga, reduzir volume ou atender destinos limitados.

## Princípios

- carregamento não significa publicação;
- raw preserva evidência, não é produto pronto;
- transformações são código versionado;
- modelos formam um grafo de dependências;
- cada camada tem contrato e dono;
- testes e reconciliação autorizam consumo.

## Anti-padrões

- conceder acesso amplo ao raw;
- transformar diretamente em dashboards sem staging;
- usar `SELECT *` como contrato permanente;
- copiar SQL entre produtos;
- reconstruir tudo sem controle de custo;
- confundir flexibilidade com ausência de schema.

## Próximo Capítulo

➡️ [[04-Extracao-e-Carga-na-Plataforma|04 — Extração e Carga na Plataforma]]
