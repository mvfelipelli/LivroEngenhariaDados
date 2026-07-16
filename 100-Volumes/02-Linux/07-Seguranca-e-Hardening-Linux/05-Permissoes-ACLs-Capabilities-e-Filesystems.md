---
title: Permissões, ACLs, Capabilities e Filesystems
description: "Controle de acesso a arquivos, executáveis e mounts."
tags: [linux, seguranca, permissoes, capabilities]
aliases: [ACL Linux, Filesystem Hardening]
created: 2026-07-16
updated: 2026-07-16
---

# Permissões, ACLs, Capabilities e Filesystems

Permissões tradicionais avaliam owner, group e others. ACLs acrescentam entradas, mas a máscara limita permissões efetivas. Bits setuid/setgid e capabilities transferem poder ao executável e exigem inventário.

```bash
namei -l /opt/dataretail/config.yaml
getfacl /opt/dataretail/config.yaml
find / -xdev -perm /6000 -type f
getcap -r / 2>/dev/null
```

## Mounts e temporários

Opções `nodev`, `nosuid` e `noexec` reduzem classes de abuso, mas podem quebrar cargas legítimas. Diretórios compartilhados precisam de sticky bit; arquivos sensíveis devem nascer sob `umask` restritiva.

```bash
umask 027
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Capabilities dividem o poder de root. Remova conjuntos não usados e considere bounding, permitted, effective, inheritable e ambient. `CAP_SYS_ADMIN` é ampla e deve ser evitada.

```mermaid
flowchart LR
    U["UID e grupos"] --> D["DAC e ACL"]
    D --> L["LSM"]
    L --> M["mount e filesystem"]
    M --> A["acesso permitido"]
```

> [!note]
> Criptografia de disco protege mídia desligada; permissões protegem acesso durante execução. São controles distintos.

Próximo: [[06-Kernel-Sysctl-LSM-Seccomp-e-Modulos]].
