---
title: Kernel, Sysctl, LSM, Seccomp e Módulos
description: "Controles do kernel e redução de superfície de execução."
tags: [linux, seguranca, kernel, lsm, seccomp]
aliases: [Kernel Hardening, LSM Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Kernel, Sysctl, LSM, Seccomp e Módulos

O kernel é uma fronteira compartilhada de alto impacto. Hardening combina atualização, configuração, políticas obrigatórias e redução de interfaces disponíveis.

## Sysctl

```bash
sysctl kernel.randomize_va_space
sysctl kernel.kptr_restrict
sysctl fs.protected_hardlinks
sysctl net.ipv4.conf.all.rp_filter
```

Parâmetros dependem da função, kernel e topologia. Reverse path filtering estrito, por exemplo, pode quebrar roteamento assimétrico. Registre valor atual, persistência e rollback antes de mudar.

## LSM e seccomp

SELinux e AppArmor implementam controle de acesso obrigatório além de DAC. Modo permissivo ajuda a construir política, mas não bloqueia. Não desative o LSM para resolver negação: investigue contexto e regra.

Seccomp filtra syscalls por processo. Uma allowlist reduz superfície, mas precisa acompanhar arquitetura, runtime e comportamento real.

```bash
getenforce 2>/dev/null || aa-status
cat /proc/self/status | grep -E 'Seccomp|NoNewPrivs'
```

## Módulos e boot

Carregamento de módulos, parâmetros de boot, Secure Boot e assinatura do kernel formam uma cadeia. Bloqueie módulos apenas após inventariar dependências e plano de recuperação. Restringir acesso a `dmesg`, BPF e interfaces de debug pode reduzir vazamento e abuso.

> [!warning]
> Um sysctl copiado de benchmark pode reduzir disponibilidade ou observabilidade. Controle eficaz é contextual e testado.

Continue em [[07-Rede-Servicos-Criptografia-e-Segredos]].
