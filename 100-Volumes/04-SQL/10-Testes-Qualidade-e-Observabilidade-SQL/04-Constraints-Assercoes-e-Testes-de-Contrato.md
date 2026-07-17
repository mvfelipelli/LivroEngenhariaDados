---
title: Constraints, Asserções e Testes de Contrato
description: "Defesas no armazenamento e nas fronteiras entre produtores e consumidores."
tags: [sql, constraints, contratos]
aliases: [Contratos de Qualidade SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Constraints, Asserções e Testes de Contrato

Constraints impedem estados inválidos no ponto de escrita. Testes consultivos verificam regras entre linhas, tabelas ou sistemas que não cabem em uma constraint simples.

```sql
CREATE TABLE pagamentos (
    pagamento_id BIGINT PRIMARY KEY,
    pedido_id BIGINT NOT NULL,
    valor_centavos BIGINT NOT NULL CHECK (valor_centavos > 0),
    status TEXT NOT NULL CHECK (status IN ('pendente', 'pago', 'falhou'))
);
```

Um contrato inclui nomes, tipos, nulabilidade, chaves, domínios, grão, semântica, freshness e compatibilidade. A validação deve ocorrer na entrada e antes da publicação.

```sql
-- O teste passa somente se não retornar linhas
SELECT pagamento_id
FROM pagamentos
WHERE status = 'pago' AND valor_centavos <= 0;
```

> [!warning]
> Aceitar tudo como texto desloca erro de contrato para consumidores e reduz a capacidade do banco de proteger o domínio.
