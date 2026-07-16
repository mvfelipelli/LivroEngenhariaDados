---
title: Gabarito — Segurança e Hardening Linux
description: "Respostas orientativas dos exercícios de segurança."
tags: [linux, seguranca, gabarito]
aliases: [Gabarito Hardening Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Gabarito

1. Ameaça pode causar dano; vulnerabilidade permite exploração; risco combina chance e impacto; controle reduz risco.
2. Camadas cobrem falhas diferentes; menor privilégio limita capacidades ao necessário.
3. DAC e ACL controlam arquivos, capabilities dividem root, LSM impõe MAC e seccomp filtra syscalls.
4. Prevenção dificulta, detecção revela, recuperação restaura e limita impacto.
5. Registre não aplicabilidade, evidência funcional e controles alternativos; não desative protocolo necessário.
6. Use shell não interativo se possível, sudo por comandos, identidade própria, rotação e logs.
7. Revogar e rotacionar; apagar histórico não invalida cópias já obtidas.
8. O pacote pode exigir reboot; confirme kernel em execução, bootloader e saúde após reinício planejado.
9. Identidade individual, chaves, sem root, porta limitada, chroot ou isolamento, logs remotos, patch e egress mínimo.
10. Valide `sshd -t`, abra acesso alternativo, teste segunda sessão e só então encerre o método antigo.
11. Registre identidade, comando, alvo, horário e resultado em coletor protegido, sem segredos.
12. Inclua razão, escopo, dono, prazo, aprovação, risco residual e compensação monitorada.
13. Classifique dados, exposição, atores, impacto, caminhos e controles para priorizar risco residual.
14. Revogue, rotacione dependências, investigue uso, preserve evidência, notifique e corrija origem do vazamento.
15. A auditoria deve listar o controle reprovado e terminar com status não zero.
