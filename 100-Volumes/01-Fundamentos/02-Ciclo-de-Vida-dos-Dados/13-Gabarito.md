---
title: Gabarito — Ciclo de Vida dos Dados
aliases: [Gabarito do Ciclo de Vida]
tags: [engenharia-de-dados, fundamentos, gabarito, ciclo-de-vida]
type: answer-key
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios sobre o Ciclo de Vida dos Dados."
---

# 13 — Gabarito

> [!note]
> Questões abertas admitem soluções diferentes. Compare o raciocínio, os controles e os trade-offs, não apenas os termos utilizados.

## Respostas — Parte I

1. É a jornada da geração ao descarte. É iterativa porque resultados podem ser armazenados novamente, reprocessados e gerar outros dados.
2. A compra gera o fato; a aplicação coleta seus atributos; o pipeline ingere o registro em um destino controlado.
3. Exemplos: qualidade verifica adequação; segurança protege; metadados explicam; observabilidade detecta anomalias; governança define decisões.
4. Ativos atendem usos frequentes; arquivados permanecem recuperáveis com menor acesso; descartados encerraram a retenção autorizada.
5. A marca lógica mantém o conteúdo armazenado. Eliminação pode exigir remoção de versões, réplicas e derivados.

## Respostas — Parte II

6. a) batch diário; b) streaming; c) batch; d) micro-batch ou streaming, conforme latência e complexidade. A justificativa deve partir do requisito.
7. Há risco de perda, impossibilidade de detectar reenvio e duplicidade. Persistir antes de confirmar, registrar identificador/checksum e publicar idempotentemente.
8. Exemplos: pedido não nulo; chave única; valor não negativo; total igual à soma dos itens; atualização dentro do SLO. Chaves e reconciliação podem bloquear; registros inválidos podem ir à quarentena; atraso pode alertar ou bloquear conforme criticidade.
9. Schema, semântica, chave, campos obrigatórios, versão, horário, origem, qualidade, segurança, compatibilidade, responsável e comunicação de mudanças.
10. Faltam evento inicial, finalidade, categoria, localizações, exceções, método de descarte, responsável e evidência.

## Respostas — Parte III

11. O diagrama deve conter o fluxo completo e um desvio para quarentena.
12. O dono aprova significado; produtor cumpre contrato; Engenharia opera; governança cataloga; segurança controla acessos; consumidor usa conforme finalidade.
13. Versionar regra, preservar entrada, dividir por período, executar em ambiente controlado, substituir partições idempotentemente, reconciliar e comunicar nova versão.
14. Entregar agregações por produto e região, sem identificadores pessoais, por canal seguro, com contrato, prazo e auditoria.
15. Verificar elegibilidade e exceções, gerar manifesto/checksum, copiar, validar integridade, testar restauração, restringir acesso e registrar evidências.

## Respostas — Parte IV

16. Confirmar métrica e filtros; comparar volumes por fonte; verificar ingestão, rejeições e atrasos; analisar transformações e joins; reconciliar; consultar linhagem; avaliar consumidores; corrigir e republicar com controle.
17. Eventos alimentam o produto intradiário; uma reconciliação batch fecha o dia. Ambos reutilizam definições e dados preservados.
18. Invalidar cache; revogar e eliminar exportação; limpar teste; restringir backup até expiração e reaplicar exclusão após restauração. Registrar escopo, execução, exceções e verificação.
19. Retenção ilimitada amplia reprocessamento, custo e exposição. Retenção limitada reduz risco e exige decidir o histórico realmente necessário.
20. A ficha deve ser verificável, atribuir responsabilidade e conectar produção, uso e destinação final.

## Rubrica

- **Excelente:** decisão justificada, riscos e controles conectados.
- **Adequada:** conceito correto e aplicação coerente.
- **Parcial:** enumera termos sem explicar mecanismos.
- **Insuficiente:** escolhe tecnologia sem requisitos ou ignora segurança e destinação.

## Próximo Capítulo

➡️ [[14-Laboratorio|14 — Laboratório]]
