---
title: Segurança, Autenticação, Autorização e Segredos
description: "Identidade, menor privilégio e proteção de credenciais."
tags: [apache-spark, seguranca, segredos]
aliases: [Segurança Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Segurança, Autenticação, Autorização e Segredos

Autenticação prova identidade; autorização define ações permitidas. Aplicações usam identidade de serviço exclusiva por ambiente, com menor privilégio em fontes, checkpoints, event logs e destinos.

Credenciais não entram em código, argumentos visíveis, notebooks, logs ou arquivos versionados. Secret manager injeta valores de curta duração; rotação deve ocorrer sem reconstruir a aplicação.

Spark authentication protege comunicação interna quando configurada; TLS protege tráfego. Plataformas como Kerberos, IAM ou Kubernetes adicionam seus próprios controles. Exposição da Spark UI e History Server precisa de autenticação e rede restrita.

Dependências e imagens devem ser fixadas, verificadas e atualizadas por processo de vulnerabilidades.
