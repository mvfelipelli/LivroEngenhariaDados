---
title: Gabarito dos Exercícios de Qualidade
aliases: [Gabarito do Módulo de Qualidade]
tags: [qualidade, gabarito, modulo-09]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios de qualidade de dados."
---

# Gabarito

1. Validade respeita domínio; acurácia representa a realidade; consistência verifica concordância entre valores ou sistemas.
2. Requisitos de latência, completude e precisão variam conforme a decisão e o risco.
3. Regra é condição; métrica agrega medida; teste avalia; incidente é falha com impacto e resposta coordenada.
4. Profiling resume estrutura e distribuição observadas; não conhece intenção semântica.
5. Testes de distribuição, unidade semântica e reconciliação financeira; o schema isolado não detectaria.
6. Quarentena preserva a maioria quando registros são independentes; bloqueio é adequado se o conjunto perde integridade ou há risco crítico.
7. A baseline ignora calendário e sazonalidade; deve comparar períodos equivalentes.
8. Investigar contrato, severidade e causa; corrigir regra ou sistema com decisão registrada, nunca silenciar informalmente.
9. Incluir identidade, tipo, versão, tempo, chave do pedido, valor, moeda, domínio de status, SLO, owner e evolução.
10. Definir numerador, denominador, população e janela para campos preenchidos, referências existentes, chaves únicas e entregas no prazo.
11. Testar regras SQL isoladas; contrato e integração com fontes; reconciliar totais com controle independente.
12. Exemplo: 99,9% das partições até 08h em 30 dias; bloquear a partição do dia se reconciliação financeira divergir.
13. Conter publicação, identificar intervalo e consumidores, deduplicar de modo idempotente, reconciliar, republicar e fortalecer chave na origem.
14. Domínio define semântica; plataforma fornece capacidades; consumidor explicita uso e impacto; owner decide risco e prioridade.
15. Tornar campo obrigatório na interface, validar endereço no cadastro e impedir avanço do processo, além de medir recorrência.
16. Com score de 83,33%, o gate reprova a execução a 90%; a decisão deve impedir publicação ou exigir política explícita de exceção.

> [!tip]
> Respostas devem explicitar o risco protegido e a ação associada à violação.

Continue em [[14-Laboratorio]].
