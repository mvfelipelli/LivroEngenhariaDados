---
title: Spark Submit, Client Mode e Cluster Mode
description: "Submissão e localização do driver."
tags: [apache-spark, spark-submit, deploy-mode]
aliases: [Spark Submit]
created: 2026-07-20
updated: 2026-07-20
---

# Spark Submit, Client Mode e Cluster Mode

`spark-submit` monta classpath, distribui artefatos, define master/deploy mode e inicia a aplicação. Argumentos após o arquivo principal pertencem à aplicação; opções Spark vêm antes.

```bash
spark-submit \
  --master k8s://https://cluster:443 \
  --deploy-mode cluster \
  --conf spark.executor.instances=4 \
  app.py --data-negocio 2026-07-20
```

Em client mode, o driver executa no processo de submissão e precisa de conectividade estável com executors. Em cluster mode, o driver executa dentro do cluster, adequado a jobs desacoplados do terminal.

Não fixe `.master()` no código de produção; a plataforma é responsável por essa decisão.
