---
title: Referências — Contêineres e Isolamento no Linux
description: "Especificações, documentação oficial e bibliografia."
tags: [linux, containers, referencias]
aliases: [Referências Contêineres Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Referências

## Especificações e kernel

- Open Container Initiative. *Image Specification*, *Runtime Specification* e *Distribution Specification*.
- Linux Kernel Documentation. *Control Group v2* e documentação de namespaces.
- Linux man-pages: `namespaces(7)`, `cgroups(7)`, `capabilities(7)`, `seccomp(2)`, `user_namespaces(7)` e `overlayfs`.
- freedesktop.org. *systemd.resource-control*.

## Projetos oficiais

- Moby Project e Docker Docs: imagens, volumes, redes, segurança e build.
- Podman Docs: execução rootless e pods.
- containerd e CRI-O: arquitetura e ciclo de vida.
- runc: implementação de runtime OCI.
- Kubernetes Documentation: recursos, probes, segurança e ciclo de pods.
- Sigstore e SLSA: assinatura, identidade e proveniência de software.

## Livros

- BURNS, Brendan. *Designing Distributed Systems*.
- RICE, Liz. *Container Security*.
- POULTON, Nigel. *The Kubernetes Book*.

> [!tip]
> Consulte versões compatíveis entre kernel, runtime e orquestrador. Segurança e formatos de artefato evoluem continuamente.
