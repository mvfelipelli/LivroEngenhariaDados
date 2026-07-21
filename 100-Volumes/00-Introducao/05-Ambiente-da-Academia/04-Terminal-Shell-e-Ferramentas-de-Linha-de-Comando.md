---
title: Terminal, Shell e Ferramentas de Linha de Comando
description: "Interface, automação e portabilidade de comandos."
tags: [terminal, shell, cli]
aliases: [Linha de Comando]
created: 2026-07-21
updated: 2026-07-21
---

# Terminal, Shell e Ferramentas de Linha de Comando

Terminal é a interface; shell interpreta comandos. Bash e PowerShell possuem sintaxe e modelos diferentes. Não copie comandos entre shells sem adaptação.

Competências iniciais:

- identificar diretório atual e listar arquivos;
- usar caminhos relativos e absolutos;
- criar, copiar e mover com segurança;
- inspecionar variáveis de ambiente;
- executar programas e interpretar código de saída;
- redirecionar e encadear dados conscientemente.

```powershell
Get-Location
Get-ChildItem -Force
Get-Command git
$LASTEXITCODE
```

Scripts transformam passos manuais em procedimentos repetíveis. Comandos destrutivos exigem validação do caminho e backup apropriado.
