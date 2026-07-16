---
title: Resumo — Bancos de Dados
aliases: [Resumo de Bancos de Dados]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, resumo]
type: summary
order: 11
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Síntese dos fundamentos de Bancos de Dados."
---

# 11 — Resumo

## Mapa do módulo

```mermaid
mindmap
  root((Bancos de Dados))
    Organização
      Schema
      Instância
      Catálogo
    SGBD
      Consultas
      Armazenamento
      Transações
      Recuperação
    Modelos
      Relacional
      Documento
      Chave-valor
      Grafo
      Temporal
    Internos
      Páginas
      Buffers
      WAL
    Concorrência
      Locks
      MVCC
      Isolamento
    Desempenho
      Índices
      Estatísticas
      Planos
```

## Conceitos essenciais

- Banco de Dados é a coleção persistente e organizada; SGBD é o software gerenciador.
- Schema define estrutura; instância representa valores em um momento.
- Catálogo contém metadados usados por pessoas e pelo próprio sistema.
- Abstração separa visões externas, modelo lógico e armazenamento físico.
- Modelos diferentes atendem padrões de acesso diferentes.
- Páginas são unidades de I/O e buffers aproximam dados da CPU.
- WAL registra alterações antes das páginas correspondentes.
- ACID reúne atomicidade, consistência, isolamento e durabilidade.
- Locks, versões e validação coordenam concorrência.
- Índices aceleram acessos específicos ao custo de espaço e escrita.
- O otimizador escolhe planos usando estimativas e estatísticas.

## Matriz de decisões

| Questão | Efeito no desenho |
| --- | --- |
| Relações e integridade fortes? | favorece modelo relacional |
| Acesso somente por chave? | chave-valor pode ser adequado |
| Agregado hierárquico variável? | documento pode reduzir reconstrução |
| Travessias profundas? | grafo pode favorecer consultas |
| Eventos ordenados pelo tempo? | temporal pode otimizar retenção |
| Escrita intensa? | limitar índices e medir contenção |
| RPO/RTO rigorosos? | reforçar log, backup, réplica e testes |

## Checklist

- [ ] Domínio e padrões de acesso conhecidos.
- [ ] Garantias de consistência explícitas.
- [ ] Schema, chaves e restrições definidos.
- [ ] Fronteiras transacionais documentadas.
- [ ] Isolamento escolhido pelas anomalias intoleráveis.
- [ ] Índices justificados por planos reais.
- [ ] Crescimento e retenção planejados.
- [ ] Backup e restauração testados.
- [ ] Segurança e observabilidade implementadas.
- [ ] Complexidade operacional aceita pela equipe.

## Síntese

> [!summary]
> Bancos de Dados são sistemas de compromissos. Nenhum modelo maximiza simultaneamente flexibilidade, integridade, latência, escala e simplicidade. Engenharia começa por requisitos e valida as decisões por comportamento observável.

## Próximo Capítulo

➡️ [[12-Perguntas-de-Entrevista|12 — Perguntas de Entrevista]]
