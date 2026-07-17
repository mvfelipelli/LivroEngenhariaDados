---
title: Permissões, Segredos, OIDC e Ambientes
description: "Identidade efêmera e proteção de deployments."
tags: [github-actions, oidc, secrets, environments]
aliases: [OIDC GitHub Actions, Environments Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Permissões, Segredos, OIDC e Ambientes

Declare `permissions`; ao especificar algumas permissões, as não listadas ficam sem acesso. Jobs devem receber somente o necessário.

```yaml
permissions:
  contents: read

jobs:
  deploy:
    permissions:
      contents: read
      id-token: write
    environment: production
```

OIDC permite trocar token assinado e curto por credencial cloud, evitando chave estática. A política cloud deve validar claims como organização, repositório, ref ou environment.

Environments podem controlar reviewers, espera, regras customizadas e segredos. Segredos de environment só ficam disponíveis ao job que o referencia e após proteções aplicáveis.

Mascaramento de logs não substitui prevenção. Não passe segredo em argumento, output, artefato ou cache. Rotacione após suspeita.

> [!warning]
> Recursos de environment variam por plano e visibilidade. Self-hosted runner não se torna isolado por usar environment.

Continue em [[07-Integracao-Continua-Testes-Qualidade-e-Feedback]].
