---
title: Solução — Transações e Índices com SQLite
aliases: [Solução do Laboratório de Bancos de Dados]
tags: [engenharia-de-dados, fundamentos, bancos-de-dados, solucao, sqlite, python]
type: solution
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do laboratório de integridade, transações e índices."
---

# 14 — Solução

## Implementação

Crie `database_lab.py` com o conteúdo abaixo:

```python
from pathlib import Path
import sqlite3

DB_PATH = Path("dataretail.db")

def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA foreign_keys = ON;

        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC NOT NULL CHECK (price > 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        );

        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
            created_at TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('pending', 'confirmed', 'cancelled')),
            total NUMERIC NOT NULL CHECK (total >= 0)
        );

        CREATE TABLE order_items (
            order_id INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
            product_id INTEGER NOT NULL REFERENCES products(product_id),
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            unit_price NUMERIC NOT NULL CHECK (unit_price > 0),
            PRIMARY KEY (order_id, product_id)
        );
        """
    )

def seed(connection: sqlite3.Connection) -> None:
    connection.executemany(
        "INSERT INTO customers VALUES (?, ?)",
        [(1, "Ana"), (2, "Bruno")],
    )
    connection.executemany(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        [(101, "Teclado", 150.0, 5), (102, "Mouse", 80.0, 0), (103, "Monitor", 900.0, 2)],
    )
    connection.commit()

def place_order(
    connection: sqlite3.Connection,
    order_id: int,
    customer_id: int,
    product_id: int,
    quantity: int,
) -> bool:
    try:
        connection.execute("BEGIN IMMEDIATE")
        product = connection.execute(
            "SELECT price FROM products WHERE product_id = ?",
            (product_id,),
        ).fetchone()
        if product is None:
            raise ValueError("produto inexistente")

        updated = connection.execute(
            "UPDATE products SET stock = stock - ? "
            "WHERE product_id = ? AND stock >= ?",
            (quantity, product_id, quantity),
        )
        if updated.rowcount != 1:
            raise ValueError("estoque insuficiente")

        unit_price = product[0]
        connection.execute(
            "INSERT INTO orders VALUES (?, ?, ?, 'confirmed', ?)",
            (order_id, customer_id, "2026-07-16T10:00:00Z", unit_price * quantity),
        )
        connection.execute(
            "INSERT INTO order_items VALUES (?, ?, ?, ?)",
            (order_id, product_id, quantity, unit_price),
        )
        connection.commit()
        return True
    except (sqlite3.Error, ValueError):
        connection.rollback()
        return False

def main() -> None:
    DB_PATH.unlink(missing_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        create_schema(connection)
        seed(connection)

        valid = place_order(connection, 1001, 1, 101, 2)
        invalid = place_order(connection, 1002, 2, 102, 1)

        plan_before = connection.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM orders "
            "WHERE customer_id = 1 AND created_at >= '2026-07-01'"
        ).fetchall()
        connection.execute(
            "CREATE INDEX idx_orders_customer_created "
            "ON orders(customer_id, created_at)"
        )
        plan_after = connection.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM orders "
            "WHERE customer_id = 1 AND created_at >= '2026-07-01'"
        ).fetchall()

        orders = connection.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        items = connection.execute("SELECT COUNT(*) FROM order_items").fetchone()[0]
        stock = connection.execute(
            "SELECT stock FROM products WHERE product_id = 101"
        ).fetchone()[0]
        integrity = connection.execute("PRAGMA foreign_key_check").fetchall()
        uses_index = any("idx_orders_customer_created" in row[-1] for row in plan_after)

        assert valid and not invalid
        assert (orders, items, stock) == (1, 1, 3)
        assert not integrity
        assert uses_index

        print("plano_antes=", plan_before)
        print("plano_depois=", plan_after)
        print("pedido_confirmado=1001")
        print("compra_sem_estoque=rollback")
        print(f"pedidos={orders}")
        print(f"itens={items}")
        print(f"estoque_produto_101={stock}")
        print("integridade=ok")
        print("indice_utilizado=sim")

if __name__ == "__main__":
    main()
```

## O que a solução demonstra

`BEGIN IMMEDIATE` inicia a unidade transacional antes da disputa pelo estoque. A atualização condicional combina verificação e baixa em uma única instrução. Se nenhuma linha for alterada, o rollback impede pedido ou item parcial. As restrições funcionam como última linha de defesa da integridade.

O primeiro plano tende a realizar varredura de `orders`. Após a criação do índice composto, o plano deve pesquisar pelo cliente e pela faixa temporal usando `idx_orders_customer_created`.

> [!warning]
> SQLite é adequado ao laboratório, mas não reproduz todos os mecanismos de concorrência, recuperação e operação de um SGBD cliente-servidor. A decisão de produção exige testes no sistema escolhido.

## Respostas às questões

1. A atomicidade impede que duas compras aprovem a mesma unidade ou que estoque e pedido divirjam.
2. Sem rollback, poderia existir pedido sem item, item sem baixa coerente ou estoque alterado para uma compra rejeitada.
3. O índice reduz páginas examinadas em leituras compatíveis, mas precisa ser atualizado nas escritas.
4. Não. O script demonstra commit e rollback lógico, não simula falha física, configuração de sincronização ou recuperação após energia.
5. Backups restaurados em testes, observabilidade, controle de acesso, migrações, capacidade, alta disponibilidade e procedimentos de incidente.

## Próximo Capítulo

➡️ [[15-Referencias|15 — Referências]]
