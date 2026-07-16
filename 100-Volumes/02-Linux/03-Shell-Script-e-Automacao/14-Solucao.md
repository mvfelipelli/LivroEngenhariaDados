---
title: Solução — Ingestão Idempotente com Bash
aliases: [Solução Laboratório Shell Script]
tags: [linux, bash, laboratorio, solucao]
created: 2026-07-16
updated: 2026-07-16
description: "Implementação validada da automação de pedidos."
---

# Solução — Ingestão Idempotente com Bash

Salve como `automacao_pedidos.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
umask 027

raiz=$(mktemp -d)
cleanup() { rm -rf -- "$raiz"; }
trap cleanup EXIT

entrada="$raiz/pedidos.csv"
aprovados="$raiz/aprovados.tsv"
quarentena="$raiz/quarentena.tsv"
estado="$raiz/estado.txt"

cat >"$entrada" <<'CSV'
pedido_id,status,valor
p-100,confirmado,150.00
p-101,cancelado,40.00
p-102,desconhecido,10.00
p-100,confirmado,150.00
CSV

processar() {
  local hash_atual hash_anterior=''
  hash_atual=$(sha256sum "$entrada" | awk '{print $1}')
  if [[ -f $estado ]]; then
    hash_anterior=$(awk -F= '$1 == "input_hash" {print $2}' "$estado")
  fi
  [[ $hash_atual == "$hash_anterior" ]] && return 0

  local tmp_aprovados tmp_quarentena tmp_estado
  tmp_aprovados=$(mktemp "$raiz/aprovados.XXXXXX")
  tmp_quarentena=$(mktemp "$raiz/quarentena.XXXXXX")
  tmp_estado=$(mktemp "$raiz/estado.XXXXXX")

  printf 'pedido_id\tstatus\tvalor\n' >"$tmp_aprovados"
  printf 'pedido_id\tmotivo\tregistro\n' >"$tmp_quarentena"

  local linhas=0 ok=0 erros=0 duplicadas=0 invalidas=0
  local id status valor extra
  declare -A vistos=()

  while IFS=, read -r id status valor extra; do
    [[ $id == pedido_id ]] && continue
    ((linhas += 1))

    if [[ -n ${vistos[$id]+x} ]]; then
      printf '%s\tpedido_duplicado\t%s,%s,%s\n' \
        "$id" "$id" "$status" "$valor" >>"$tmp_quarentena"
      ((duplicadas += 1, erros += 1))
      continue
    fi
    vistos[$id]=1

    if [[ -n ${extra:-} || ! $id =~ ^p-[0-9]+$ ||
          ! $status =~ ^(confirmado|cancelado)$ ||
          ! $valor =~ ^[0-9]+([.][0-9]{2})?$ ]]; then
      printf '%s\tstatus_invalido\t%s,%s,%s\n' \
        "$id" "$id" "$status" "$valor" >>"$tmp_quarentena"
      ((invalidas += 1, erros += 1))
      continue
    fi

    printf '%s\t%s\t%s\n' "$id" "$status" "$valor" >>"$tmp_aprovados"
    ((ok += 1))
  done <"$entrada"

  {
    printf 'input_hash=%s\n' "$hash_atual"
    printf 'linhas=%d\n' "$linhas"
    printf 'aprovadas=%d\n' "$ok"
    printf 'quarentena=%d\n' "$erros"
    printf 'duplicadas=%d\n' "$duplicadas"
    printf 'invalidas=%d\n' "$invalidas"
    printf 'estado=publicado\n'
  } >"$tmp_estado"

  [[ -s $tmp_aprovados && -s $tmp_quarentena && -s $tmp_estado ]]
  mv -f -- "$tmp_aprovados" "$aprovados"
  mv -f -- "$tmp_quarentena" "$quarentena"
  mv -f -- "$tmp_estado" "$estado"
}

hash_publicacao() {
  sha256sum "$aprovados" "$quarentena" "$estado" | sha256sum | awk '{print $1}'
}

processar
antes=$(hash_publicacao)
processar
depois=$(hash_publicacao)
[[ $antes == "$depois" ]]

awk -F= '$1 != "input_hash" {print}' "$estado"
printf 'segunda_execucao=sem_alteracoes\n'
printf 'automacao=ok\n'
```

## Por que funciona

O checksum evita republicar a mesma entrada. Arquivos temporários recebem todo o conteúdo antes de `mv`. O array associativo detecta repetição e o estado registra contagens verificáveis. O hash composto prova que a segunda execução não alterou os três artefatos.

> [!note]
> A publicação de três arquivos não é uma transação indivisível. Sistemas reais podem publicar uma nova pasta versionada e trocar atomicamente um único ponteiro ou manifesto.
