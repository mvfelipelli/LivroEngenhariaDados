---
title: Python, Ambientes Virtuais e Dependências
description: "Instalação isolada e reproduzível do runtime Python."
tags: [python, venv, dependencias]
aliases: [Setup Python]
created: 2026-07-21
updated: 2026-07-21
---

# Python, Ambientes Virtuais e Dependências

Crie um ambiente por projeto. No PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -c "import sys; print(sys.executable)"
```

Em Bash, a ativação usa `source .venv/bin/activate`. Fixe dependências diretas em arquivo apropriado e use lockfile quando o gerenciador adotado oferecer esse recurso. Não versione `.venv`.

Valide importações e um teste simples antes de adicionar bibliotecas de dados pesadas. Isso separa falhas do runtime de falhas da aplicação.

Próximo: [[100-Volumes/00-Introducao/08-Preparacao-do-Ambiente/06-Java-Spark-e-Compatibilidade-de-Runtimes|Java e Spark]].
