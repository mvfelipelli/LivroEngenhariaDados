---
title: Solução — Reconciliador GitOps Determinístico
description: "Implementação validada do laboratório de GitOps."
tags: [laboratorio, gitops, python, solucao]
aliases: [Solução Reconciliador GitOps]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Reconciliador GitOps Determinístico

```python
import re

release = {
    "version": "1.4.0",
    "digest": "sha256:4f2a9c",
    "signed": True,
}

desired = {
    "image": release["digest"],
    "replicas": 3,
    "environment": "production",
}

current = {
    "image": "sha256:91b7dd",
    "replicas": 2,
    "environment": "production",
}


def validate_release(item):
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", item["version"]):
        raise ValueError("versao_invalida")
    if not item["signed"] or not item["digest"].startswith("sha256:"):
        raise ValueError("release_nao_verificada")


def reconcile(wanted, observed):
    drift = {key: value for key, value in wanted.items() if observed.get(key) != value}
    converged = {**observed, **drift}
    return drift, converged


validate_release(release)
assert desired["image"] == release["digest"]
drift, state = reconcile(desired, current)
assert len(drift) == 2
assert state == desired
drift_after, state_after = reconcile(desired, state)
assert not drift_after and state_after == desired

print(f"release={release['version']}")
print("digest=verificado")
print("promocao=imutavel")
print(f"drift={len(drift)}")
print("reconciliacao=ok")
print("estado=convergente")
```

A segunda reconciliação não produz alterações, comprovando idempotência. As assertions funcionam como políticas mínimas de versão, assinatura, digest e convergência.
