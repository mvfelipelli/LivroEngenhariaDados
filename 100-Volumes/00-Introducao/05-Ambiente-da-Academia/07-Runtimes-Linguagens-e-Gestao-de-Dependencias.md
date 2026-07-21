---
title: Runtimes, Linguagens e Gestão de Dependências
description: "Versões, ambientes e pacotes reproduzíveis."
tags: [runtime, dependencias, python]
aliases: [Runtimes da Academia]
created: 2026-07-21
updated: 2026-07-21
---

# Runtimes, Linguagens e Gestão de Dependências

Runtime executa programas; gerenciador instala pacotes; ambiente isola dependências; manifesto declara requisitos; lock registra resolução exata quando aplicável.

Python será a linguagem principal, SQL uma interface transversal e Java/JVM aparecerá em ferramentas como Spark. Versões suportadas devem ser verificadas em conjunto.

```bash
python --version
python -m pip --version
java -version
```

Use `python -m pip` para associar instalador ao interpretador correto. Ambientes virtuais evitam poluir a instalação global. Fixar todas as versões sem processo de atualização envelhece o projeto; não fixar nenhuma prejudica reprodutibilidade.

Dependências nativas também incluem bibliotecas do sistema, arquitetura e drivers.
