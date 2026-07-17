---
title: Hash Keys, Hashdiff, Canonicalização e Colisões
description: "Identificadores determinísticos e detecção de mudança."
tags: [hash-key, hashdiff, canonicalizacao]
aliases: [Hashes Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Hash Keys, Hashdiff, Canonicalização e Colisões

Hash key deriva business keys; hashdiff resume atributos de Satellite. A função só é determinística se a entrada for canônica.

## Contrato de canonicalização

- ordem fixa das colunas;
- conversão de tipo e formato estáveis;
- timezone e precisão definidos;
- Unicode e caixa tratados conscientemente;
- marcador inequívoco para `NULL`;
- delimitador escapado ou serialização com comprimento;
- algoritmo e versão registrados.

```text
SHA-256(canonical(cliente_bk))
SHA-256(canonical(nome, segmento, status))
```

Colisões são improváveis, não impossíveis. Mantenha business key, constraints e monitoramento; escolha algoritmo compatível com risco e plataforma.

> [!warning]
> `COALESCE(valor,'')` torna `NULL` indistinguível de string vazia e pode esconder mudanças.
