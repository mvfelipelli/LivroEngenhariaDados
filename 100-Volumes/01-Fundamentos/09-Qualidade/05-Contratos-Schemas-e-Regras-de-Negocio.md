---
title: Contratos, Schemas e Regras de Negócio
aliases: [Contratos de Dados, Regras de Qualidade]
tags: [qualidade, contratos, schema, regras]
created: 2026-07-16
updated: 2026-07-16
description: "Formalização de expectativas técnicas, semânticas e operacionais."
---

# Contratos, Schemas e Regras de Negócio

Um contrato de dados estabelece compromissos entre produtor e consumidores. Ele pode incluir schema, semântica, chaves, granularidade, política de mudança, qualidade, freshness, segurança, proprietário e suporte.

## Níveis do contrato

- **Estrutural:** nomes, tipos, obrigatoriedade e compatibilidade.
- **Semântico:** significado, unidade, domínio e regras.
- **Operacional:** frequência, latência, disponibilidade e retenção.
- **Governança:** classificação, acesso, responsabilidade e evolução.

```yaml
produto: pedidos_confirmados
versao: 2
grao: um registro por pedido
chave: pedido_id
regras:
  - valor_total >= 0
  - status in [confirmado, cancelado]
slo_freshness_minutos: 5
```

## Compatibilidade

Adicionar campo opcional costuma ser compatível; remover, renomear ou mudar significado pode romper consumidores. Compatibilidade técnica não garante compatibilidade semântica: alterar reais para centavos mantendo o tipo numérico é uma ruptura grave.

## Regras executáveis

Uma regra deve ter identificador, descrição, população, severidade, proprietário, ação e versão. Invariantes críticos podem bloquear publicação; expectativas probabilísticas podem alertar ou consumir orçamento de erro.

> [!warning]
> Inferir contrato exclusivamente do schema observado transforma acidentes históricos em especificação.

Os contratos são verificados por [[06-Testes-de-Dados-e-Piramide-de-Qualidade]].
