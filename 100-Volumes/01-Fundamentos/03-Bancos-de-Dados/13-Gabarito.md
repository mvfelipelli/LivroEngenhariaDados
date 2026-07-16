---
title: Gabarito — Bancos de Dados
aliases: [Gabarito de Bancos de Dados]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, gabarito]
type: answer-key
order: 13
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Respostas orientativas dos exercícios de Bancos de Dados."
---

# 13 — Gabarito

> [!note]
> As respostas são orientativas. Soluções diferentes são válidas quando atendem aos requisitos e explicitam consequências.

## Parte I

1. Banco de Dados é a coleção organizada; SGBD é o software que a administra; schema define estrutura e regras; instância é o conteúdo em um momento.
2. Independência lógica reduz o impacto de mudanças no modelo lógico sobre visões e aplicações. Independência física permite alterar páginas, arquivos e índices sem mudar o modelo lógico.
3. Relacional favorece relações e integridade; documentos, agregados flexíveis; chave-valor, acesso direto; colunar, séries e agregações por colunas; grafos, travessias entre relações. Requisitos prevalecem sobre rótulos.
4. Páginas são unidades de I/O; o buffer pool mantém páginas em memória; o WAL registra mudanças antes das páginas e sustenta redo/undo na recuperação.
5. Atomicidade é tudo ou nada; consistência preserva regras declaradas; isolamento controla interferência; durabilidade preserva commits conforme a garantia contratada.

## Parte II

6. Uma resposta plausível: relacional para finanças; chave-valor para sessões; documentos para catálogo; grafos para fraude; colunar ou séries temporais para métricas. Volume, consultas, garantias e operação devem confirmar a escolha.
7. `PRIMARY KEY` no pedido, `FOREIGN KEY` para cliente, `CHECK (total >= 0)`, `NOT NULL` e `CHECK` ou tabela de domínio para status.
8. Como o log do commit foi persistido antes das páginas, a recuperação refaz operações confirmadas. Registros sem commit são desfeitos ou ignorados, conforme o mecanismo do SGBD.
9. Respectivamente: leitura não repetível, fantasma, write skew ou anomalia de decisão concorrente, leitura suja.
10. Um índice como `(customer_id, created_at)` atende igualdade pelo cliente e faixa temporal. A ordem inversa pode não atender tão bem ao primeiro filtro. O índice consome espaço e acrescenta manutenção a `INSERT`, `UPDATE` e `DELETE`.

## Parte III

11. Exemplo PostgreSQL:

```sql
BEGIN;

UPDATE products
SET stock = stock - 2
WHERE product_id = 10
  AND stock >= 2;

-- A aplicação exige uma linha afetada; caso contrário, executa ROLLBACK.
INSERT INTO orders (order_id, customer_id, status)
VALUES (501, 42, 'confirmed');

COMMIT;
```

12. Atualização condicional é simples e atômica; bloqueio pessimista serializa concorrentes, mas aumenta espera e risco de deadlock; controle otimista compara uma versão e repete quando há conflito. A carga define a escolha.
13. Obter plano estimado e real, comparar cardinalidades, verificar varredura e filtros, atualizar estatísticas quando necessário, medir I/O/CPU/locks, testar índice representativo e comparar novamente com a mesma carga.
14. Exemplo: RPO de cinco minutos e RTO de uma hora. Combinar backups completos, incrementais ou WAL arquivado, cópia isolada e restaurações periódicas. Réplicas podem propagar exclusão, corrupção e erro humano.
15. Pedidos em relacional; catálogo em documentos; sessões em chave-valor; eventos em log durável e armazenamento apropriado; relatórios em sistema analítico colunar. Cada tecnologia adiciona segurança, monitoramento, backup, integração e conhecimento operacional.

## Parte IV

16. Cada transação segura um recurso esperado pela outra. O SGBD detecta o ciclo e aborta uma vítima. Ordenar atualizações sempre por identificador e manter transações curtas reduz o risco; repetição com limite trata a vítima.
17. Fechamento pode exigir `SERIALIZABLE` ou snapshot consistente com validações; catálogo pode aceitar `READ COMMITTED`. Maior isolamento protege invariantes, mas pode elevar contenção e abortos, exigindo retry seguro.
18. Confirmar regressão e consulta, obter plano real, conferir cardinalidade e estatísticas, observar volume e distribuição, I/O, CPU, memória, locks e cache, avaliar mudanças de schema/configuração, testar correções e medir sob carga representativa.
19. Adicionar coluna inicialmente anulável, publicar contrato, adaptar produtores e consumidores, preencher histórico em lotes, validar cobertura, aplicar valor padrão quando legítimo e somente depois tornar `NOT NULL`.
20. Deve conter requisitos quantificados; modelo e chaves; invariantes no SGBD; limites transacionais; estratégia de concorrência; índices derivados de consultas; RPO/RTO e restauração testada; menor privilégio, criptografia e auditoria; métricas; testes de carga e falha.

## Próximo Capítulo

➡️ [[14-Laboratorio|14 — Laboratório]]
