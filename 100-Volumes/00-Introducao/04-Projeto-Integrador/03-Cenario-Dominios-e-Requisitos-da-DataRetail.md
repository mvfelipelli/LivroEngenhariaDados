---
title: Cenário, Domínios e Requisitos da DataRetail
description: "Contexto empresarial e primeiras necessidades do projeto."
tags: [dataretail, dominios, requisitos]
aliases: [Cenário DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Cenário, Domínios e Requisitos da DataRetail

A DataRetail opera lojas físicas e e-commerce. Seus domínios iniciais são Vendas, Clientes, Catálogo, Estoque, Pagamentos e Logística. Fontes incluem ERP, CRM, plataforma web, gateway e WMS.

Problemas prioritários:

- receita divergente entre áreas;
- atraso na consolidação de pedidos;
- dificuldade para rastrear estoque e entrega;
- dados de clientes sem classificação uniforme;
- reprocessamentos manuais e pouco auditáveis.

O primeiro produto é Pedidos Canônicos; dele derivam Receita Diária e Indicadores de Entrega. Requisitos devem declarar granularidade, chave, SLA, retenção, acesso e owner. “Dashboard único” não é requisito suficiente.
