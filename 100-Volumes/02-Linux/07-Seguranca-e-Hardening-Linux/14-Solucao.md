---
title: Solução — Auditoria de Baseline de Segurança
description: "Implementação validada do laboratório de hardening."
tags: [linux, seguranca, laboratorio, solucao]
aliases: [Solução Laboratório Hardening]
created: 2026-07-16
updated: 2026-07-16
---

# Solução — Auditoria de Baseline de Segurança

Salve como `auditar_baseline.py`:

```python
estado = {
    "permit_root_login": False,
    "password_authentication": False,
    "admin_group_required": True,
    "sudo_least_privilege": True,
    "umask": "027",
    "rootfs_nodev_tmp": True,
    "lsm_enforcing": True,
    "firewall_default_deny": True,
    "remote_audit_logs": True,
    "automatic_security_inventory": True,
}

politica = {
    "ssh_root_bloqueado": lambda s: not s["permit_root_login"],
    "ssh_senha_bloqueada": lambda s: not s["password_authentication"],
    "grupo_admin": lambda s: s["admin_group_required"],
    "sudo_minimo": lambda s: s["sudo_least_privilege"],
    "umask_restritiva": lambda s: s["umask"] == "027",
    "tmp_nodev": lambda s: s["rootfs_nodev_tmp"],
    "lsm_enforcing": lambda s: s["lsm_enforcing"],
    "firewall_deny": lambda s: s["firewall_default_deny"],
    "logs_remotos": lambda s: s["remote_audit_logs"],
    "inventario": lambda s: s["automatic_security_inventory"],
}

resultados = {nome: check(estado) for nome, check in politica.items()}
falhas = sorted(nome for nome, aprovado in resultados.items() if not aprovado)
if falhas:
    raise SystemExit("controles_reprovados=" + ",".join(falhas))

print(f"checks={len(resultados)}")
print(f"aprovados={sum(resultados.values())}")
print("ssh=ok")
print("privilegios=ok")
print("filesystem=ok")
print("auditoria=ok")
print("baseline=conforme")
print("hardening=ok")
```

## Leitura da solução

Estado e política são separados. Cada regra tem nome estável e retorna booleano; falhas são ordenadas para produzir evidência determinística. O laboratório não afirma que dez checks bastam para um host real.

> [!tip]
> Em produção, inclua origem da evidência, horário, host, versão da política, exceção e assinatura do relatório.
