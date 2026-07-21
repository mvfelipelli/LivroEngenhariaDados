---
title: Produtores, Fontes e Domínios de Dados
description: "Origem, ownership e contratos na produção de dados."
tags: [fontes-de-dados, dominios, produtores]
aliases: [Produtores de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Produtores, Fontes e Domínios de Dados

Produtores incluem aplicações transacionais, dispositivos, parceiros, arquivos e pessoas. A fonte técnica não é necessariamente o owner semântico: o sistema registra, enquanto o domínio define significado e regras.

Tipos comuns:

- bancos relacionais e NoSQL;
- APIs e SaaS;
- logs e eventos;
- arquivos e object storage;
- streams e filas;
- dados externos adquiridos.

Cada fonte precisa de owner, contrato, frequência, volume, chave, retenção e política de mudança. Capturar diretamente tabelas internas sem coordenação acopla consumidores à implementação do produtor.

> [!warning]
> “Sistema de origem” deve ser definido por atributo e processo. Duas aplicações podem disputar autoridade sobre o mesmo conceito.
