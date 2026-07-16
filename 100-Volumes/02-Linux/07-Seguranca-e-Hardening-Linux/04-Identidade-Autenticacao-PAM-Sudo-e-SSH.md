---
title: Identidade, Autenticação, PAM, Sudo e SSH
description: "Ciclo de contas, autenticação e administração privilegiada."
tags: [linux, seguranca, pam, sudo, ssh]
aliases: [Segurança SSH, PAM Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Identidade, Autenticação, PAM, Sudo e SSH

Toda ação privilegiada deve ser atribuível a uma identidade individual ou workload, autorizada pelo mínimo necessário e revogada no tempo correto.

## Contas e PAM

PAM compõe módulos para autenticação, conta, sessão e troca de credencial. Ordem e flags como `required`, `requisite` e `sufficient` alteram o resultado; mudanças exigem sessão de recuperação.

```bash
getent passwd
passwd -S usuario
chage -l usuario
sudo -l -U usuario
```

Contas de serviço devem ter shell e login compatíveis com sua função, credenciais rotacionadas e proprietário. Bloquear senha não necessariamente impede chave SSH, token ou sessão existente.

## Sudo e SSH

Prefira regras sudo por comando, usuário e host; edite com `visudo`. Evite curingas, editores, shells e comandos capazes de escapar para execução arbitrária.

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowGroups administradores
```

Essas opções são exemplos, não um arquivo universal. Valide com `sshd -t`, mantenha acesso alternativo e confirme include files. Proteja chaves privadas, use MFA ou certificados quando apropriado e registre acesso administrativo.

> [!warning]
> Não desative autenticação vigente antes de provar o novo caminho em outra sessão.

Continue em [[05-Permissoes-ACLs-Capabilities-e-Filesystems]].
