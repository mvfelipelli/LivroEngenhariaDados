---
title: Solução — Validação de Pipeline CI/CD
description: "Implementação validada do laboratório."
tags: [github-actions, ci-cd, laboratorio, solucao]
aliases: [Solução Laboratório CI CD]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Validação de Pipeline CI/CD

```python
pipeline = {
    "concurrency": "production",
    "jobs": {
        "test": {"needs": [], "permissions": {"contents": "read"}},
        "build": {
            "needs": ["test"],
            "permissions": {"contents": "read", "attestations": "write"},
            "artifact": "sha256:abc123",
        },
        "deploy": {
            "needs": ["build"],
            "permissions": {"contents": "read", "id-token": "write"},
            "artifact": "sha256:abc123",
            "environment": "production",
            "approval": True,
        },
    },
}


def ordenar(jobs):
    ordem, restantes = [], set(jobs)
    while restantes:
        prontos = sorted(
            nome for nome in restantes if set(jobs[nome]["needs"]) <= set(ordem)
        )
        if not prontos:
            raise ValueError("dependencia_ciclica")
        ordem.extend(prontos)
        restantes.difference_update(prontos)
    return ordem


ordem = ordenar(pipeline["jobs"])
jobs = pipeline["jobs"]
assert ordem == ["test", "build", "deploy"]
assert jobs["build"]["artifact"] == jobs["deploy"]["artifact"]
assert jobs["deploy"]["approval"] and jobs["deploy"]["environment"] == "production"
assert jobs["test"]["permissions"] == {"contents": "read"}
assert pipeline["concurrency"] == "production"

print(f"jobs={len(jobs)}")
print("ordem=" + ",".join(ordem))
print("permissoes=minimas")
print("artefato=unico")
print("ambiente=protegido")
print("concurrency=ativa")
print("pipeline=ok")
```

O algoritmo executa ordenação topológica e falha se não houver job pronto. Assertions representam gates de identidade, promoção e ambiente.
