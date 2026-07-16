---
title: Perguntas de Entrevista — Modelagem de Dados
aliases: [Data Modeling Interview Questions]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, entrevistas]
type: interview
order: 12
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas para entrevistas sobre Modelagem de Dados."
---

# 12 — Perguntas de Entrevista

> [!tip]
> Uma resposta forte conecta regra do domínio, estrutura, mecanismo de integridade e trade-off.

## Fundamentos

### 1. O que é Modelagem de Dados?

É o processo de descobrir, representar, validar e evoluir conceitos, fatos, relações e regras de um domínio para um propósito. O modelo é um artefato desse processo.

### 2. Qual é a diferença entre modelo conceitual, lógico e físico?

O conceitual representa significado; o lógico organiza segundo um paradigma; o físico implementa em uma tecnologia concreta com tipos, índices e armazenamento.

### 3. Entidade e tabela são sinônimos?

Não. Entidade é conceito do domínio. Uma entidade pode exigir várias tabelas, e uma tabela pode materializar múltiplos conceitos por decisão física.

### 4. Como decidir entre entidade e atributo?

Avaliar identidade, ciclo de vida, relacionamentos, estrutura interna e histórico. Um conceito referenciado ou alterado independentemente tende a ser entidade.

## Chaves e relacionamentos

### 5. O que é uma chave candidata?

Uma superchave mínima: identifica unicamente sem atributos desnecessários. As candidatas não escolhidas como primária continuam exigindo unicidade.

### 6. Chave substituta elimina a chave natural?

Não. Ela fornece identidade técnica estável, mas a unicidade de negócio deve ser preservada quando válida.

### 7. Como representar um relacionamento muitos-para-muitos?

No modelo relacional, por uma relação associativa com chaves para ambos os lados e atributos próprios da associação.

### 8. Uma chave estrangeira implementa toda a cardinalidade?

Não. Ela protege existência do alvo. Limites `1:1` exigem unicidade, e mínimos como “todo pedido possui item” podem exigir validação adicional.

### 9. Como evitar explosão de linhas em um JOIN?

Declarar o grão de ambos os lados, medir cardinalidade, garantir unicidade das chaves de junção e agregar previamente quando os grãos diferirem.

## Normalização

### 10. Por que normalizar?

Para localizar fatos conforme dependências, reduzindo redundância problemática e anomalias de inserção, atualização e exclusão.

### 11. O que é dependência funcional?

`X → Y` significa que valores iguais de `X` determinam valores iguais de `Y` em toda instância válida. É regra do domínio, não coincidência da amostra.

### 12. Diferencie 2FN e 3FN.

2FN elimina dependências parciais de chave composta. 3FN trata dependências transitivas inadequadas entre atributos não chave.

### 13. 3FN e BCNF são iguais?

Não. BCNF exige que todo determinante de dependência não trivial seja superchave e é mais restritiva.

### 14. O que é decomposição sem perda?

É aquela cuja junção reconstrói exatamente os fatos originais, sem perder linhas ou criar combinações espúrias.

### 15. Quando desnormalizar?

Quando medição demonstra necessidade e existem fonte de verdade, sincronização ou reconstrução, testes de consistência e justificativa documentada.

## Modelagem analítica

### 16. O que é o grão de uma tabela fato?

É a definição exata do que cada linha representa. Deve ser declarado antes de dimensões e medidas.

### 17. Diferencie fato e dimensão.

Fato registra evento, medição ou snapshot; dimensão fornece contexto descritivo para filtrar, agrupar e interpretar.

### 18. O que é uma medida semiaditiva?

Pode ser somada em algumas dimensões, mas não em todas. Estoque pode ser somado por loja e produto, mas não ao longo dos dias indiscriminadamente.

### 19. O que é dimensão conformada?

Dimensão com significado e chaves compatíveis entre fatos, permitindo analisar processos como vendas e devoluções de modo consistente.

### 20. Como preservar mudança de categoria de produto?

Se o histórico importa, criar nova versão da dimensão e associar fatos à versão válida no instante do evento.

## Evolução e cenários

### 21. Como tornar uma coluna obrigatória sem interromper produtores?

Adicionar anulável, adaptar produtores, preencher histórico, medir cobertura, migrar consumidores e somente então aplicar `NOT NULL`.

### 22. O que é expandir-migrar-contrair?

Criar a nova estrutura mantendo a antiga, migrar dados e consumidores com reconciliação e remover o legado após a depreciação.

### 23. Como tratar uma mudança na definição de receita?

Versionar a métrica, documentar a quebra, recalcular histórico quando possível e manter definições paralelas durante a transição.

### 24. Pedidos possuem itens, pagamentos e entregas. Como evitar duplicar receita?

Modelar cada processo em fato própria, não juntar fatos diretamente e reconciliar medidas no grão correto por dimensões conformadas.

### 25. Como modelar entregas parciais?

Criar entrega com identidade própria e uma associação entre entrega e item do pedido contendo quantidade; validar que a soma entregue não exceda a comprada.

### 26. O que deve acompanhar um diagrama?

Glossário, regras, chaves, cardinalidades, pressupostos, temporalidade, decisões, contratos, exemplos e testes. O desenho sozinho é insuficiente.

### 27. Como validar um modelo?

Usar cenários normais, limites e exceções; testar identidades, estados inválidos, concorrência, histórico, consultas e evolução.

### 28. Qual é o papel da governança na modelagem?

Definir significado, donos, políticas, classificação, linhagem, contratos e processo de mudança para manter modelos e sistemas coerentes.

## Próximo Capítulo

➡️ **13 — Exercícios**
