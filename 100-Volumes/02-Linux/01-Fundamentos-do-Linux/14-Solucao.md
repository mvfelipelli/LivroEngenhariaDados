---
title: Solução — Workspace Seguro de Ingestão
aliases: [Solução do Laboratório Linux]
tags: [linux, solucao, bash, seguranca]
created: 2026-07-16
updated: 2026-07-16
description: "Solução Bash reproduzível do laboratório de fundamentos Linux."
---

# Solução — Workspace Seguro de Ingestão

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

root="$(mktemp -d)"
trap 'case "$root" in "${TMPDIR:-/tmp}"/*|/tmp/*) rm -rf -- "$root" ;; esac' EXIT
umask 027

prepare_workspace() {
    local directories=(incoming processing quarantine archive logs)
    local directory
    for directory in "${directories[@]}"; do
        mkdir -p -- "$root/$directory"
        chmod 750 -- "$root/$directory"
    done

    local input="$root/incoming/pedidos.csv"
    if [[ ! -f "$input" ]]; then
        printf '%s\n' 'pedido_id,status,valor' 'p-100,confirmado,150.00' > "$input"
    fi
    chmod 640 -- "$input"

    (
        cd -- "$root"
        sha256sum -- incoming/pedidos.csv > manifest.sha256
    )
    chmod 640 -- "$root/manifest.sha256"
}

prepare_workspace
before="$(sha256sum -- "$root/incoming/pedidos.csv" "$root/manifest.sha256")"
prepare_workspace
after="$(sha256sum -- "$root/incoming/pedidos.csv" "$root/manifest.sha256")"

[[ "$before" == "$after" ]]
directories="$(find "$root" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
files="$(find "$root" -type f | wc -l | tr -d ' ')"
permission="$(stat -c '%a' "$root/incoming")"
manifest_entries="$(wc -l < "$root/manifest.sha256" | tr -d ' ')"

[[ "$directories" == 5 ]]
[[ "$files" == 2 ]]
[[ "$permission" == 750 ]]
[[ "$manifest_entries" == 1 ]]

printf '%s\n' \
    'workspace=ok' \
    "diretorios=$directories" \
    "arquivos=$files" \
    "permissao_diretorio=$permission" \
    "entradas_manifesto=$manifest_entries" \
    'segunda_execucao=sem_alteracoes' \
    'linux=ok'
```

## Leitura da solução

O diretório é exclusivo, a limpeza valida que o alvo está sob uma raiz temporária, `umask` reduz permissões padrão e a função pode ser repetida. O snapshot confirma que entrada e manifesto permanecem iguais.

Finalize em [[15-Referencias]].
