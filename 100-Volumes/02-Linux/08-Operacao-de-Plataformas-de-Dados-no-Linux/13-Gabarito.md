---
title: Gabarito — Operação de Plataformas de Dados no Linux
description: "Respostas orientativas dos exercícios operacionais."
tags: [linux, operacao, gabarito]
aliases: [Gabarito Operação Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Gabarito

1. Disponibilidade mantém acesso; durabilidade preserva dado; RPO limita perda; RTO limita retorno.
2. Artefato é programa imutável; configuração varia; segredo exige proteção; estado sobrevive à execução.
3. Health indica condição, readiness controla tráfego e SLO define resultado esperado na janela.
4. Backup é cópia recuperável; réplica serve disponibilidade; snapshot registra estado de volume em um ponto.
5. Falha do host ou domínio compartilhado derruba ambas; distribua por failure domains.
6. Falta prova de restauração íntegra dentro de RPO/RTO e validação do negócio.
7. Lock, timeout, política de sobreposição, idempotência, estado e monitoramento.
8. Migração incompatível tornou rollback assimétrico; use expand-contract e compatibilidade entre versões.
9. Exemplo: 99,5% até 30 minutos; alerte atraso e burn rate; runbook cobre fonte, worker e publicação.
10. Usuário sem login, artefato somente leitura, config em `/etc`, estado em `/var/lib`, logs em journal.
11. Escolha ponto, restaure isolado, valide hashes, schema, permissões, contagens e consulta de negócio.
12. Inclua owner, SLO, arquitetura, segurança, limites, telemetria, backup, restore, runbook e rollback.
13. Mantenha cópia isolada, infraestrutura e credenciais prontas, DNS, teste e autoridade de failover.
14. Modele pico, storage, fila, dependências e falha; teste carga e reserve headroom antes da campanha.
15. O script deve identificar a gate ausente e retornar status não zero.
