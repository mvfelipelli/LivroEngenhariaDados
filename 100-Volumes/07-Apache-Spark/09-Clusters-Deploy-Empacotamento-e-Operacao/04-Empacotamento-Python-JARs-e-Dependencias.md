---
title: Empacotamento Python, JARs e Dependências
description: "Distribuição reprodutível de código e bibliotecas."
tags: [apache-spark, empacotamento, dependencias]
aliases: [Empacotamento PySpark]
created: 2026-07-20
updated: 2026-07-20
---

# Empacotamento Python, JARs e Dependências

`--py-files` distribui arquivos `.py`, `.zip` ou `.egg`, mas bibliotecas nativas exigem ambiente compatível ou imagem. `--jars` adiciona JARs; `--packages` resolve coordenadas Maven, sujeito a rede e repositórios.

Produção deve fixar versões e hashes, gerar SBOM e evitar download imprevisível no início do job. Imagem de container ou ambiente empacotado reduz divergência entre driver e executors.

```bash
spark-submit --py-files dist/dataretail.zip \
  --jars drivers/postgresql.jar app.py
```

O artefato inclui código, metadados de versão e manifesto, não segredos. Teste importação em executor, pois funcionar no driver não prova distribuição correta.
