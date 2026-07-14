---
title: "{{title}}"
description: "Laboratório reproduzível sobre o tema do módulo."
tags:
  - laboratorio
  - projeto-integrador
aliases: []
volume: "00"
module: "00"
chapter: "14"
type: laboratory
difficulty: iniciante
estimated_time: "60 minutos"
status: rascunho
created: "{{date:YYYY-MM-DD}}"
updated: "{{date:YYYY-MM-DD}}"
---

# {{title}}

## Objetivo

Declare o resultado observável que o leitor produzirá ao concluir o laboratório.

## Pré-requisitos

- Conhecimentos necessários.
- Software e versões mínimas.
- Recursos de máquina necessários.

## Ambiente

| Componente | Versão | Finalidade |
| ---------- | ------ | ---------- |
| Docker | Versão estável suportada | Execução reproduzível |

## Arquitetura do laboratório

```mermaid
flowchart LR
    A["Fonte"] --> B["Processamento"]
    B --> C["Destino"]
    C --> D["Validação"]
```

## Preparação

1. Crie um diretório exclusivo para o laboratório.
2. Confirme as versões das ferramentas.
3. Inicie apenas os serviços necessários.

```bash
docker --version
```

## Passo a passo

### Etapa 1 — Preparar os dados

Explique a ação, o comando e o resultado esperado.

### Etapa 2 — Executar o processamento

Inclua comandos executáveis e explique os parâmetros relevantes.

### Etapa 3 — Inspecionar o resultado

Mostre como verificar a saída sem depender apenas de inspeção visual.

## Validação

Execute verificações objetivas que comprovem a conclusão do laboratório.

```sql
SELECT 1 AS laboratorio_concluido;
```

## Resultado esperado

Descreva os arquivos, tabelas, métricas ou mensagens que devem existir ao final.

## Solução de problemas

| Sintoma | Causa provável | Correção |
| ------- | -------------- | -------- |
| Exemplo | Causa | Ação corretiva |

## Limpeza do ambiente

```bash
docker compose down
```

## Conclusão

Relacione o resultado prático aos fundamentos estudados no módulo.
