---
title: Gabarito dos Exercícios de Arquiteturas
aliases: [Gabarito do Módulo de Arquiteturas]
tags: [arquitetura, gabarito, modulo-08]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios de arquiteturas de dados."
---

# Gabarito

1. Arquitetura trata decisões estruturais significativas; design detalha a solução; diagrama representa uma visão de ambos.
2. É uma propriedade observável do sistema, como disponibilidade, latência ou auditabilidade.
3. Evento registra fato ocorrido; comando solicita uma ação a um responsável.
4. Warehouse privilegia análise modelada; Lake preserva múltiplos formatos; Lakehouse adiciona recursos de tabela transacional sobre armazenamento aberto.
5. Exemplo: “99% dos pedidos confirmados devem estar consultáveis em até cinco minutos, medidos mensalmente”.
6. Sem mudança de contrato ou responsabilidade, as camadas multiplicam custo, latência e pontos de falha.
7. Um destino pode aceitar e outro falhar, produzindo divergência. São necessários outbox, reconciliação, idempotência ou compensação.
8. Mesh exige propriedade por domínio, produto com SLO, plataforma self-service e governança federada.
9. Uma alternativa batch para BI com fluxo streaming separado para fraude; outra baseada em log de eventos com materializações e fechamento batch.
10. Critérios possíveis: latência, consistência, replay, custo e capacidade operacional; pesos devem refletir o contexto.
11. O ADR deve registrar necessidade de auditoria, alternativa escolhida, retenção, segurança, custo e consequências.
12. Verificar criptografia habilitada, p99 de freshness abaixo da meta e custo por unidade dentro do orçamento.
13. Selecionar um produto, replicar entradas, executar em paralelo, reconciliar, migrar consumidores e desativar o caminho antigo gradualmente.
14. A plataforma oferece identidade, execução, catálogo e observabilidade; domínios controlam semântica, qualidade e ciclo de vida dos produtos.
15. Criar e alterar tabelas em ambos os motores, testar tipos, snapshots, concorrência, schema evolution e rollback com a mesma suíte.
16. A análise deve relacionar novos pesos aos requisitos e verificar se a diferença entre alternativas é significativa.

> [!tip]
> Não existe um único gabarito para decisões arquiteturais. A resposta deve manter coerência entre contexto, medida, escolha e consequência.

Continue em [[14-Laboratorio]].
