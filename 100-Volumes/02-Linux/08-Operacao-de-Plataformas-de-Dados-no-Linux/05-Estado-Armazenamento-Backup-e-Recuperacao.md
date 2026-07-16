---
title: Estado, Armazenamento, Backup e Recuperação
description: "Persistência, durabilidade, RPO, RTO e restauração."
tags: [linux, operacao, backup, recuperacao]
aliases: [Backup de Plataformas de Dados, Estado Operacional]
created: 2026-07-16
updated: 2026-07-16
---

# Estado, Armazenamento, Backup e Recuperação

Classifique arquivos em artefato, configuração, segredo, dado persistente, checkpoint, cache, temporário e log. Cada classe exige owner, permissão, retenção, backup e descarte.

## Backup como sistema

```mermaid
flowchart LR
    D["Dado consistente"] --> B["Backup"]
    B --> V["Verificação de integridade"]
    V --> C["Cópia isolada"]
    C --> R["Restauração testada"]
```

RPO limita perda aceitável; RTO limita tempo de retorno. Snapshot crash-consistent não garante consistência da aplicação. Coordene flush, logs transacionais ou mecanismo nativo.

```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
df -hT
df -i
lsblk -f
```

Implemente regra 3-2-1 quando compatível: múltiplas cópias, mídias ou domínios diferentes e uma cópia externa ou isolada. Proteja backups contra o mesmo comprometimento e teste credenciais de recuperação.

Restauração deve validar integridade, schema, permissões, dependências e consulta de negócio. Registre duração real e lacuna de dados.

> [!warning]
> Replicação propaga exclusão e corrupção; não substitui backup versionado.

Próximo: [[06-Automacao-Agendamento-Dependencias-e-Idempotencia]].
