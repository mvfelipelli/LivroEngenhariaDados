---
title: Strings, Bytes, Unicode e Formatação
description: "Texto, codificação e limites binários."
tags: [python, unicode, strings, bytes]
aliases: [Texto em Python]
created: 2026-07-17
updated: 2026-07-17
---

# Strings, Bytes, Unicode e Formatação

`str` contém texto Unicode; `bytes` contém octetos. Codificar transforma texto em bytes; decodificar realiza o inverso.

```python
texto = "São Paulo"
payload = texto.encode("utf-8")
assert payload.decode("utf-8") == texto
```

Defina o encoding nas fronteiras. Erros não devem ser silenciados com `errors="ignore"` sem uma política de perda documentada.

Unicode pode representar grafemas visualmente iguais por sequências diferentes. Normalização é relevante para comparação, mas não substitui regras de domínio:

```python
import unicodedata

normalizado = unicodedata.normalize("NFC", texto)
```

F-strings servem à apresentação e logs controlados. Não use interpolação para montar SQL. Strings são imutáveis; para juntar muitas partes, acumule-as e use `"".join(partes)`.
