---
title: Privacidade, Criptografia, Auditoria e Governança
description: "Proteção e rastreabilidade de dados sensíveis."
tags: [apache-spark, privacidade, governanca]
aliases: [Privacidade no Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Privacidade, Criptografia, Auditoria e Governança

Classifique dados antes do processamento. Minimize colunas, retenção e cópias; tokenize ou masque identificadores quando o uso não exige o valor original. Criptografia deve cobrir trânsito e repouso, com chaves separadas dos dados.

Controle em nível de tabela ou coluna deve existir no catálogo e no destino, não apenas na aplicação. Resultados intermediários, shuffle, cache, checkpoint e logs também podem conter informação sensível.

Auditoria registra quem executou, qual versão, quais fontes acessou e o que publicou. Lineage e catálogo ligam evidência técnica a finalidade, proprietário e retenção.

Direitos de exclusão exigem estratégia para tabelas derivadas, backups e reprocessamento, respeitando legislação e política organizacional.
