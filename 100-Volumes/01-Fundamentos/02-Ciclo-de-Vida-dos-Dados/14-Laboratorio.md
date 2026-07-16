---
title: Laboratório — Pipeline do Ciclo de Vida
aliases: [Laboratório do Ciclo de Vida]
tags: [engenharia-de-dados, fundamentos, laboratorio, python, ciclo-de-vida]
type: laboratory
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Laboratório reproduzível de ingestão, validação, processamento, publicação e arquivamento."
---

# 14 — Laboratório

## Objetivo

Construir com Python e sua biblioteca padrão um pipeline local para pedidos da DataRetail S.A., incluindo entrada bruta, validação, deduplicação, produto de consumo, quarentena, manifesto e arquivo.

## Pré-requisitos

- Python 3.11 ou superior;
- terminal;
- editor de texto;
- conhecimento básico de CSV e Python.

## Ambiente

Crie uma pasta `lab-ciclo-vida` com:

```text
lab-ciclo-vida/
├── input/
├── raw/
├── valid/
├── quarantine/
├── product/
├── archive/
└── pipeline.py
```

## Dados de entrada

Crie `input/pedidos.csv`:

```csv
event_id,order_id,channel,occurred_at,total,status
e1,p100,web,2026-07-15T10:00:00Z,120.50,confirmed
e2,p101,store,2026-07-15T10:05:00Z,80.00,confirmed
e2,p101,store,2026-07-15T10:05:00Z,80.00,confirmed
e3,p102,app,2026-07-15T10:10:00Z,-15.00,confirmed
e4,,web,2026-07-15T10:15:00Z,30.00,confirmed
e5,p100,web,2026-07-15T11:00:00Z,120.50,cancelled
```

## Requisitos

Implemente `pipeline.py` para:

1. copiar a entrada para `raw` sem alterá-la;
2. calcular SHA-256 da cópia;
3. validar campos obrigatórios, total não negativo e status permitido;
4. deduplicar por `event_id`;
5. gravar rejeições com o motivo em `quarantine`;
6. gravar eventos válidos em `valid`;
7. produzir `product/pedidos_atuais.csv`, mantendo o último estado por pedido;
8. produzir `product/resumo_canais.csv` somente com pedidos confirmados;
9. criar `product/manifest.json` com contagens e checksum;
10. copiar os artefatos válidos para `archive` e verificar sua integridade;
11. permitir nova execução sem duplicar resultados.

## Regras esperadas

- `e2` deve aparecer uma vez;
- `e3` e `e4` devem ir para quarentena;
- `p100` deve terminar cancelado;
- somente `p101` deve compor o resumo confirmado;
- a segunda execução deve produzir os mesmos resultados.

## Validação

Execute duas vezes:

```bash
python pipeline.py
python pipeline.py
```

Verifique:

```bash
python -c "import csv; print(list(csv.DictReader(open('product/pedidos_atuais.csv', encoding='utf-8'))))"
python -c "import json; print(json.load(open('product/manifest.json', encoding='utf-8')))"
```

## Critérios de conclusão

- estrutura criada;
- entrada bruta preservada;
- dois registros em quarentena;
- três eventos válidos únicos;
- dois pedidos atuais;
- um pedido confirmado no resumo;
- checksums verificados;
- reexecução idempotente.

## Desafios adicionais

- detectar mudança de schema;
- aceitar múltiplos arquivos;
- simular evento atrasado;
- implementar retenção por data;
- produzir métricas por execução.

## Próximo Capítulo

➡️ [[14-Solucao|14 — Solução]]
