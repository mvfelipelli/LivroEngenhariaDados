---
title: Perguntas de Entrevista — Fundamentos Python
description: "Questões sobre runtime, ambientes e ferramentas."
tags: [python, entrevista]
aliases: [Entrevista Fundamentos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Python é compilado ou interpretado?

Ambos os termos descrevem partes do processo: CPython compila fonte para bytecode e interpreta esse bytecode em sua máquina virtual.

## 2. O que um ambiente virtual isola?

O prefixo do runtime e os pacotes Python instalados. Ele não isola kernel, serviços, drivers ou bibliotecas externas do sistema.

## 3. Por que usar `python -m pip`?

Para executar o `pip` associado ao interpretador selecionado e evitar instalar no ambiente errado.

## 4. Restrição e lock são iguais?

Não. A restrição declara versões aceitáveis; o lock registra uma resolução exata, frequentemente incluindo dependências transitivas e hashes.

## 5. Qual é a função do bloco `if __name__ == "__main__"`?

Executar o ponto de entrada apenas quando o módulo é iniciado como programa, sem dispará-lo durante importação.

## 6. Tipagem estática valida JSON recebido?

Não por si só. Dados externos exigem parsing e validação em runtime.

## 7. Por que retornar códigos de saída?

Para que shell, CI e orquestradores distingam sucesso de falha automaticamente.

## 8. Como tratar segredos?

Fornecer por mecanismo seguro do ambiente, limitar privilégios, rotacionar e impedir sua inclusão em logs e Git.
