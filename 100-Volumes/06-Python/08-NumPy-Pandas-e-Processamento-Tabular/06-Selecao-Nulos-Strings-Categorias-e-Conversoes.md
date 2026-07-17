---
title: Seleção, Nulos, Strings, Categorias e Conversões
description: "Manipulação explícita de colunas e ausência."
tags: [python, pandas, nulos, conversoes]
aliases: [Nulos Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Seleção, Nulos, Strings, Categorias e Conversões

Use `.loc` para rótulos e `.iloc` para posições. Atribua com `.loc` em uma única operação para evitar chained assignment e ambiguidades entre view e cópia.

```python
mascara = pedidos["valor_centavos"].notna() & pedidos["status"].eq("aprovado")
aprovados = pedidos.loc[mascara, ["pedido_id", "valor_centavos"]].copy()
```

Ausência pode ser `pd.NA`, `NaN`, `NaT` ou `None` conforme dtype. Use `isna` e `notna`, não igualdade. Antes de `fillna`, defina se zero é realmente equivalente a ausência.

Métodos `.str` operam sobre Series string. `pd.to_numeric(..., errors="raise")` e `pd.to_datetime(..., errors="raise", utc=True)` falham explicitamente; `errors="coerce"` só é correto quando a contagem de coerções vira métrica e quarentena.
