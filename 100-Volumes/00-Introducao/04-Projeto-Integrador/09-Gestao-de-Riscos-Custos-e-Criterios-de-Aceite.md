---
title: Gestão de Riscos, Custos e Critérios de Aceite
description: "Priorização e aprovação de entregas do projeto."
tags: [riscos, custos, criterios-de-aceite]
aliases: [Riscos Projeto DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Gestão de Riscos, Custos e Critérios de Aceite

O registro de riscos contém probabilidade, impacto, owner, mitigação e gatilho. Riscos iniciais incluem schema instável, dados pessoais, duplicação, ambiente divergente e excesso de ferramentas.

Custo inclui infraestrutura, licenças, tempo de engenharia, suporte e complexidade. Cada componente novo deve resolver uma limitação demonstrada.

Critérios gerais:

- execução reproduzível;
- contrato e schema válidos;
- reconciliação completa;
- retry sem duplicação;
- testes aprovados;
- métricas e logs úteis;
- documentação e rollback;
- ausência de segredos.

Aceite é binário para invariantes críticas e baseado em limite para SLOs. Uma demonstração manual não substitui evidência automatizada.
