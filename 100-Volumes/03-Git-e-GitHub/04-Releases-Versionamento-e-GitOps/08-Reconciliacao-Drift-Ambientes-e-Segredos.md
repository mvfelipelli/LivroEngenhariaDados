---
title: Reconciliação, Drift, Ambientes e Segredos
description: "Controle contínuo entre intenção e realidade operacional."
tags: [gitops, drift, ambientes, segredos]
aliases: [Reconciliação e Drift]
created: 2026-07-17
updated: 2026-07-17
---

# Reconciliação, Drift, Ambientes e Segredos

Cada ciclo lê o desejado, observa o atual, calcula diferença, aplica mudança e publica condição. A operação deve ser idempotente: repetir o ciclo não pode multiplicar efeitos.

```python
def reconciliar(desejado, atual):
    plano = {k: v for k, v in desejado.items() if atual.get(k) != v}
    return {**atual, **plano}, plano

estado, plano = reconciliar({"versao": "1.4.0", "replicas": 3}, {"versao": "1.3.2"})
assert estado["versao"] == "1.4.0" and plano["replicas"] == 3
```

Drift pode ser autocorrigido, apenas alertado ou temporariamente tolerado. Mudanças emergenciais diretas precisam de prazo e reconciliação reversa para que Git volte a representar a intenção.

Ambientes devem variar por overlays ou valores explícitos, sem copiar grandes manifestos. Promoção é uma mudança revisável na referência do artefato.

Segredos não devem aparecer em texto claro no Git. Opções incluem referências a secret managers, criptografia antes do commit e injeção por identidade de workload. Rotação e auditoria continuam necessárias.

> [!warning]
> Criptografia no repositório protege conteúdo, mas não corrige permissões excessivas do agente nem vazamento após descriptografia.
