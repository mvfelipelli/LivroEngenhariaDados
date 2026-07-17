---
title: Resumo
description: "Síntese de fatos e dimensões."
tags: [modelagem-de-dados, resumo, dimensional]
aliases: [Resumo Modelagem Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- O desenho dimensional começa pelo processo e pelo grão.
- Bus matrix coordena processos e dimensões conformadas.
- Fatos podem ser transacionais, snapshots ou factless.
- Aditividade define eixos seguros de soma.
- Dimensões fornecem contexto descritivo e hierarquias.
- Chave substituta identifica a versão dimensional.
- Dimensões degeneradas e junk atendem padrões específicos.
- Estrela privilegia simplicidade; snowflake normaliza hierarquias.
- Late arriving exige unknown, inferência, quarentena ou retry.
- Testes protegem unicidade do grão, referências e reconciliação.

O [[14-Laboratorio|laboratório]] implementa uma estrela de vendas e comprova agregação sem fanout.
