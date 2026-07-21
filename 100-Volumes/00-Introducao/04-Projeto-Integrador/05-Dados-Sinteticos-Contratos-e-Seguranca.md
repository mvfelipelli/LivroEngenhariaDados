---
title: Dados Sintéticos, Contratos e Segurança
description: "Datasets reproduzíveis sem exposição de informações reais."
tags: [dados-sinteticos, data-contracts, seguranca]
aliases: [Dados do Projeto DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Dados Sintéticos, Contratos e Segurança

Dados do projeto são sintéticos e gerados por semente fixa. Eles devem reproduzir distribuição, relacionamentos, atrasos, duplicatas e erros sem copiar registros reais.

Contratos descrevem `pedido_id`, versão, timestamps, moeda, valores, status, itens e referências. Casos inválidos são intencionais e documentados para testar qualidade.

```yaml
dataset: pedidos
grain: um registro por pedido e versão
primary_key: [pedido_id, versao]
classification: interno
owner: dominio-vendas
```

Não use nomes, e-mails ou documentos reais. Segredos nunca entram em fixtures. A geração registra versão, semente e parâmetros para que resultados sejam repetíveis.

> [!tip]
> Dado sintético útil preserva propriedades relevantes, não identidades.
