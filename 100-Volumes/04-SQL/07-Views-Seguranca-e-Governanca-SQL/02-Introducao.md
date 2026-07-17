---
title: Introdução
description: "Do acesso técnico ao uso legítimo e governado dos dados."
tags: [sql, introducao, governanca]
aliases: [Introdução à Governança SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Conceder acesso a um banco não é uma decisão binária. É preciso responder **quem**, **por qual identidade**, **para qual finalidade**, **sobre quais dados**, **com quais operações**, **por quanto tempo** e **sob qual evidência**.

Views reduzem acoplamento e exposição; roles agrupam capacidades; políticas restringem linhas; parâmetros separam dados de código; auditoria registra eventos relevantes. Governança transforma esses mecanismos em um processo com responsáveis, revisão e expiração.

```mermaid
flowchart TD
    N["Necessidade legítima"] --> C["Classificação dos dados"]
    C --> M["Controle mínimo suficiente"]
    M --> E["Evidência de uso"]
    E --> R["Revisão e expiração"]
    R --> N
```

Na DataRetail S.A., um analista precisa de receita por loja, não necessariamente de nomes, e-mails ou leitura direta das tabelas transacionais. O contrato de acesso deve refletir essa finalidade.
