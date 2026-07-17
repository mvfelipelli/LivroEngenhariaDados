---
title: Datetime, Timezones, DST e ISO 8601
description: "Instantes, tempo civil e normalização temporal."
tags: [python, datetime, timezone, iso-8601]
aliases: [Datas Python]
created: 2026-07-17
updated: 2026-07-17
---

# Datetime, Timezones, DST e ISO 8601

Datetime naive não possui timezone; aware possui `tzinfo`. Eventos distribuídos devem representar instantes aware e normalmente ser persistidos em UTC.

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

local = datetime(2026, 7, 17, 9, tzinfo=ZoneInfo("America/Sao_Paulo"))
utc = local.astimezone(timezone.utc)
texto = utc.isoformat().replace("+00:00", "Z")
```

Timezone é conjunto histórico de regras, não apenas offset. Mudanças de DST criam horários inexistentes ou ambíguos; `fold` distingue a segunda ocorrência em sobreposição.

`timedelta(days=1)` representa 24 horas, que pode diferir de “mesmo horário civil amanhã”. Defina se a regra é duração ou calendário. Parseie apenas formatos documentados e rejeite timestamp sem offset quando a origem não tiver timezone contratual.
