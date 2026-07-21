---
title: Configuração, Ambientes, Segredos e Imagens
description: "Separação entre artefato e configuração operacional."
tags: [apache-spark, configuracao, containers]
aliases: [Configuração de Deploy Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Configuração, Ambientes, Segredos e Imagens

Um artefato imutável recebe configuração por argumentos, arquivos controlados e mecanismos da plataforma. Valores devem ser tipados, validados no início e registrados sem segredos.

Imagens fixam Java, Python, Spark e bibliotecas nativas. Use tag imutável ou digest, usuário não root, base mínima, scanner e política de atualização. Driver e executors precisam da mesma ABI para extensões nativas.

Segredos entram por volume, provider ou credencial temporária. Variáveis de ambiente são simples, mas podem aparecer em dumps e consoles; avalie o modelo de ameaça.

Configuração efetiva inclui origem e precedência: `SparkConf`, flags, defaults e propriedades da sessão podem se sobrepor.
