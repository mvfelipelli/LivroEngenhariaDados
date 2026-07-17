---
title: Doubles, Mocks, Contratos e Testabilidade
description: "Isolamento de efeitos e verificação de colaboração."
tags: [python, mocks, doubles, contratos]
aliases: [Mocks Python]
created: 2026-07-17
updated: 2026-07-17
---

# Doubles, Mocks, Contratos e Testabilidade

Dummy preenche parâmetro; stub devolve resposta controlada; fake implementa versão funcional simplificada; spy registra chamadas; mock inclui expectativas.

```python
from unittest.mock import Mock

destino = Mock()
publicar(destino, {"id": "P-1"})
destino.salvar.assert_called_once_with({"id": "P-1"})
```

Mocks testam interação e podem acoplar a implementação. Prefira fakes para interfaces estáveis e mocks nas bordas onde a interação é o comportamento relevante. Use `spec` ou `autospec` para detectar métodos inexistentes.

Patch deve ocorrer onde o nome é consultado, não necessariamente onde foi definido. Melhor ainda: receba relógio, cliente e repositório como dependências. Um double não prova compatibilidade com o serviço real; testes de contrato e integração completam a evidência.
