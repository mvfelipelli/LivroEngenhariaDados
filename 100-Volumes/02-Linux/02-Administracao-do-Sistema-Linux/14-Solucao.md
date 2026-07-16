---
title: Solução — Auditoria de Prontidão Linux
aliases: [Solução Administração Linux]
tags: [linux, administracao, solucao, bash]
created: 2026-07-16
updated: 2026-07-16
description: "Solução Bash da auditoria administrativa idempotente."
---

# Solução — Auditoria de Prontidão Linux

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

root="$(mktemp -d)"
trap 'case "$root" in "${TMPDIR:-/tmp}"/*|/tmp/*) rm -rf -- "$root" ;; esac' EXIT
umask 027

prepare() {
    mkdir -p -- "$root/config" "$root/backup" "$root/report"
    printf '%s\n' 'service=dataretail-ingestion' 'owner=dataeng' 'environment=production' > "$root/config/service.env"
    printf '%s\n' '/data ext4 defaults,nodev' '/backup ext4 ro,nodev,nosuid' > "$root/config/mounts.tsv"
    printf '%s\n' 'configuration-backup-v1' > "$root/backup/config.tar"
    (cd -- "$root" && sha256sum -- backup/config.tar > backup/config.tar.sha256)
    chmod 640 -- "$root/config/service.env" "$root/config/mounts.tsv" "$root/backup/config.tar" "$root/backup/config.tar.sha256"
}

audit() {
    local approved=0
    grep -qx 'owner=dataeng' "$root/config/service.env" && ((approved += 1))
    grep -qx 'environment=production' "$root/config/service.env" && ((approved += 1))
    [[ "$(wc -l < "$root/config/mounts.tsv" | tr -d ' ')" == 2 ]] && ((approved += 1))
    grep -q 'nodev' "$root/config/mounts.tsv" && ((approved += 1))
    [[ -s "$root/backup/config.tar" ]] && ((approved += 1))
    (cd -- "$root" && sha256sum -c --status backup/config.tar.sha256) && ((approved += 1))
    [[ "$(stat -c '%a' "$root/config/service.env")" == 640 ]] && ((approved += 1))
    [[ -d "$root/backup" ]] && ((approved += 1))

    printf '%s\n' \
        'checks=8' \
        "aprovados=$approved" \
        'servicos=1' \
        'mounts=2' \
        'backup=ok' \
        'permissao_config=640' \
        > "$root/report/readiness.txt"
    [[ "$approved" == 8 ]]
}

prepare
audit
before="$(sha256sum -- "$root/report/readiness.txt")"
prepare
audit
after="$(sha256sum -- "$root/report/readiness.txt")"
[[ "$before" == "$after" ]]

cat -- "$root/report/readiness.txt"
printf '%s\n' 'segunda_execucao=sem_alteracoes' 'administracao=ok'
```

## Leitura da solução

O script cria somente estado temporário, aplica permissões, valida oito controles e compara hashes do relatório após a segunda execução. Em produção, cada check deve registrar host, versão e timestamp.

Finalize em [[15-Referencias]].
