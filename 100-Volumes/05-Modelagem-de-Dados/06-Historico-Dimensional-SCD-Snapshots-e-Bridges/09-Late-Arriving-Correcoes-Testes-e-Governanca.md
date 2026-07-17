---
title: Late Arriving, Correções, Testes e Governança
description: "Operação confiável de histórico dimensional."
tags: [late-arriving, correcoes, testes]
aliases: [Governança de Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Late Arriving, Correções, Testes e Governança

Dimensão tardia pode criar placeholder; fato tardio precisa resolver a versão válida no tempo do evento, não a atual. Correção retroativa pode dividir intervalos e exigir rekey de fatos afetados conforme contrato.

## Testes

- exatamente uma versão atual por chave natural;
- nenhum intervalo inválido ou sobreposto;
- cada fato encontra exatamente uma versão;
- peso da bridge soma 1 por grupo quando há alocação;
- snapshots não duplicam `(entidade, período)`;
- marcos acumulativos respeitam ordem possível;
- reprocessamento é idempotente.

Registre origem da mudança, instante de recepção, validade, versão do pipeline e motivo de correção. Backfills devem ser delimitados e reconciliados.

> [!important]
> Corrigir o histórico sem preservar lineage pode melhorar um relatório e destruir a auditabilidade.
