---
title: Solução — Contrato de Produto em Camadas
description: "Implementação validada de contrato e promoções."
tags: [modelagem-de-dados, python, data-product, solucao]
aliases: [Solução Laboratório Produto Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Contrato de Produto em Camadas

```python
contrato_v1 = {
    "evento_id": str,
    "pedido_id": int,
    "ocorrido_em": str,
    "itens": list,
}

bronze = [
    {"evento_id": "e1", "pedido_id": 100, "ocorrido_em": "2026-07-17T10:00:00Z",
     "itens": [{"numero": 1, "valor_centavos": 1000}, {"numero": 2, "valor_centavos": 1500}]},
    {"evento_id": "e2", "pedido_id": 200, "ocorrido_em": "2026-07-17T11:00:00Z",
     "itens": [{"numero": 1, "valor_centavos": 2000}]},
    {"evento_id": "e3", "pedido_id": "invalido", "ocorrido_em": "2026-07-17T12:00:00Z",
     "itens": []},
]

def valido(registro, contrato):
    return all(campo in registro and isinstance(registro[campo], tipo)
               for campo, tipo in contrato.items())

silver = {}
quarentena = []
for registro in bronze:
    if valido(registro, contrato_v1):
        silver[registro["evento_id"]] = registro
    else:
        quarentena.append(registro)

gold = []
for evento in silver.values():
    for item in evento["itens"]:
        gold.append({
            "pedido_id": evento["pedido_id"],
            "numero_item": item["numero"],
            "data_particao": evento["ocorrido_em"][:10],
            "valor_centavos": item["valor_centavos"],
        })

chaves = {(linha["pedido_id"], linha["numero_item"]) for linha in gold}
assert len(chaves) == len(gold) == 3
total = sum(linha["valor_centavos"] for linha in gold)
assert total == 4500 and len(silver) == 2 and len(quarentena) == 1

contrato_v2 = {**contrato_v1, "canal": (str, type(None))}
campos_v1 = set(contrato_v1)
campos_v2 = set(contrato_v2)
assert campos_v1 <= campos_v2 and "canal" in campos_v2 - campos_v1

print(f"bronze={len(bronze)}")
print(f"silver={len(silver)}")
print(f"quarentena={len(quarentena)}")
print(f"gold_itens={len(gold)}")
print(f"total_centavos={total}")
print("chaves_unicas=ok")
print("schema_v2=compativel")
print("produto=ok")
```

O exemplo mantém Bronze, separa quarentena, publica Silver deduplicado e Gold em grão explícito. A adição opcional preserva os campos de v1.
