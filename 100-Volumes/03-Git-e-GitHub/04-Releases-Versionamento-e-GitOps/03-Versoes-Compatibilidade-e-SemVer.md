---
title: Versões, Compatibilidade e SemVer
description: "Contratos públicos e significado das versões."
tags: [semver, compatibilidade, api]
aliases: [Versionamento Semântico]
created: 2026-07-17
updated: 2026-07-17
---

# Versões, Compatibilidade e SemVer

## Contrato antes do número

Uma versão só comunica algo quando existe uma API pública. Em dados, essa API pode incluir schemas, nomes de tabelas, eventos, parâmetros, formatos, semântica de campos e garantias operacionais.

SemVer usa `MAJOR.MINOR.PATCH`: major para incompatibilidade, minor para funcionalidade compatível e patch para correção compatível. Pré-releases, como `2.0.0-rc.1`, possuem precedência inferior à versão normal; metadados, como `+build.87`, não alteram precedência.

| Mudança | Exemplo | Incremento |
| --- | --- | --- |
| Correção preservando contrato | cálculo corrigido | patch |
| Capacidade retrocompatível | campo opcional | minor |
| Quebra do consumidor | campo removido | major |

```python
def proxima_versao(atual, mudanca):
    major, minor, patch = map(int, atual.split("."))
    if mudanca == "breaking":
        return f"{major + 1}.0.0"
    if mudanca == "feature":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"

assert proxima_versao("1.4.2", "feature") == "1.5.0"
```

> [!note]
> Antes de `1.0.0`, SemVer admite rápida evolução; a organização ainda deve documentar sua política de compatibilidade.

Erros comuns incluem versionar pela quantidade de commits, alterar conteúdo já publicado e chamar qualquer mudança de major. O próximo capítulo transforma a versão em referência Git e release.
