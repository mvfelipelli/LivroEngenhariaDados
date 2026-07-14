---
title: Geração e Coleta de Dados
aliases:
  - Geração de Dados
  - Coleta de Dados
tags:
  - engenharia-de-dados
  - fundamentos
  - ciclo-de-vida
  - data-generation
  - data-collection
type: chapter
order: 04
parent: "[[README]]"
created: 2026-07-14
updated: 2026-07-14
---

# 04 — Geração e Coleta de Dados

> [!abstract]
> Todo dado possui uma origem. Antes de ser armazenado, processado ou analisado, ele precisa ser produzido por algum evento e posteriormente capturado por um sistema. A geração e a coleta representam o início do Ciclo de Vida dos Dados e influenciam diretamente todas as etapas seguintes.

---

# Introdução

Nenhum dado surge espontaneamente.

Todo dado é consequência de um evento ocorrido no mundo real ou em um ambiente digital.

Uma compra.

Um clique.

Uma ligação telefônica.

Uma medição de temperatura.

Uma transferência bancária.

Uma consulta médica.

Uma leitura realizada por um sensor.

Cada um desses acontecimentos gera informações que podem ser registradas por um ou mais sistemas.

A Engenharia de Dados normalmente não controla a geração dessas informações, mas depende totalmente delas para construir plataformas analíticas confiáveis.

---

# O que significa gerar dados?

A geração de dados corresponde ao momento em que uma informação passa a existir de forma registrável.

Isso ocorre sempre que um evento produz informações que podem ser armazenadas.

> [!definition]
>
> **Geração de dados** é o processo pelo qual um evento, ação ou observação produz novas informações passíveis de registro e utilização por sistemas computacionais.

É importante observar que o evento ocorre primeiro.

O dado é apenas sua representação.

Por exemplo:

| Evento | Dado gerado |
|---------|-------------|
| Cliente realiza uma compra | Pedido, itens, valor, data, forma de pagamento |
| Sensor mede temperatura | Valor da temperatura, horário, localização |
| Usuário faz login | Usuário, horário, endereço IP, dispositivo |
| Veículo passa em um pedágio | Placa, cabine, horário, valor da tarifa |
| Médico registra um atendimento | Prontuário, exames, diagnóstico |

Os dados representam acontecimentos do mundo real.

Quanto melhor essa representação, maior será o valor produzido posteriormente.

---

# Dados não são o evento

Um erro comum é confundir o dado com o acontecimento.

Considere o exemplo abaixo.

```text
Evento:
João realizou uma compra às 14h35.

↓

Registro produzido:

Cliente: João
Produto: Notebook
Valor: R$ 5.000
Data/Hora: 14:35
Loja: São Paulo
```

A compra aconteceu apenas uma vez.

Entretanto, ela poderá gerar diversos registros diferentes em sistemas distintos.

Por exemplo:

- sistema de vendas;
- sistema financeiro;
- sistema fiscal;
- CRM;
- plataforma logística;
- Data Warehouse;
- Data Lake.

O evento é único.

Os registros podem ser muitos.

---

# Fontes de geração de dados

As organizações modernas produzem dados a partir de inúmeras fontes.

Entre as mais comuns destacam-se:

## Sistemas transacionais

São responsáveis pelas operações do negócio.

Exemplos:

- ERP;
- CRM;
- sistemas bancários;
- sistemas hospitalares;
- sistemas acadêmicos;
- plataformas de e-commerce.

Esses sistemas normalmente representam a principal fonte de dados corporativos.

---

## Aplicações Web

Sites e portais registram continuamente informações como:

- acessos;
- cliques;
- pesquisas;
- carrinhos de compra;
- páginas visitadas;
- tempo de navegação.

Esses dados são fundamentais para análises de comportamento dos usuários.

---

## Aplicativos móveis

Além das informações tradicionais, aplicativos podem registrar:

- localização;
- dispositivo;
- versão do aplicativo;
- notificações;
- uso de funcionalidades;
- tempo de utilização.

---

## Sensores (IoT)

Dispositivos conectados produzem grandes volumes de dados continuamente.

Exemplos:

- temperatura;
- umidade;
- pressão;
- vibração;
- velocidade;
- consumo de energia;
- posição geográfica.

Em muitos cenários esses dados são produzidos milhares de vezes por segundo.

---

## Equipamentos industriais

Máquinas industriais registram continuamente:

- produção;
- consumo;
- falhas;
- manutenção;
- desempenho.

Esses dados são utilizados para manutenção preditiva e otimização da produção.

---

## Redes sociais

Interações realizadas pelos usuários também geram dados.

Exemplos:

- curtidas;
- comentários;
- compartilhamentos;
- seguidores;
- mensagens;
- reações.

---

## Fontes externas

Nem todos os dados são produzidos pela própria empresa.

Também podem ser obtidos de:

- órgãos governamentais;
- parceiros;
- fornecedores;
- empresas especializadas;
- APIs públicas;
- serviços de terceiros.

Essas fontes costumam complementar os dados internos.

---

# Dados estruturados e não estruturados

As fontes produzem diferentes tipos de informação.

## Dados estruturados

Possuem organização previamente definida.

Exemplo:

| CPF | Nome | Salário |
|------|-------|----------|
| ... | ... | ... |

São facilmente armazenados em bancos relacionais.

---

## Dados semiestruturados

Possuem organização parcial.

Exemplos:

- JSON;
- XML;
- YAML.

Embora apresentem estrutura, ela pode variar entre registros.

---

## Dados não estruturados

Não seguem um esquema fixo.

Exemplos:

- imagens;
- vídeos;
- documentos;
- e-mails;
- gravações de áudio;
- arquivos PDF.

Esses dados normalmente exigem tratamentos específicos antes da análise.

---

# O que é coleta de dados?

Depois de produzidos, os dados precisam ser capturados.

Essa etapa recebe o nome de coleta.

> [!definition]
>
> **Coleta de dados** é o processo de captura das informações geradas em sua origem para que possam ser utilizadas por outros sistemas ou processos.

Enquanto a geração representa o nascimento do dado, a coleta representa sua primeira movimentação.

---

# Formas de coleta

Existem diferentes estratégias para capturar dados.

## Entrada manual

Uma pessoa informa os dados diretamente em um sistema.

Exemplos:

- cadastro de clientes;
- preenchimento de formulários;
- prontuários médicos;
- pesquisas.

Vantagem:

- validação humana.

Desvantagem:

- sujeito a erros de digitação.

---

## Captura automática

Os próprios sistemas registram os eventos.

Exemplos:

- logs;
- sensores;
- telemetria;
- APIs;
- sistemas embarcados.

É o modelo predominante em plataformas modernas.

---

## Importação

Dados produzidos anteriormente são incorporados ao ambiente.

Exemplos:

- planilhas;
- arquivos CSV;
- arquivos Parquet;
- backups;
- bases históricas.

---

## Integração entre sistemas

Os dados são enviados diretamente entre aplicações.

Pode ocorrer por:

- APIs;
- mensageria;
- filas;
- replicação;
- eventos.

Essa modalidade será aprofundada no módulo de Integração de Dados.

---

# Qualidade começa aqui

> [!warning]
> A qualidade dos dados não começa durante o processamento. Ela começa no momento em que os dados são gerados e coletados.

Problemas introduzidos nessa etapa costumam propagar-se por todo o restante do ciclo.

Alguns exemplos:

- CPF digitado incorretamente;
- data inválida;
- valores duplicados;
- unidades de medida diferentes;
- campos obrigatórios ausentes;
- horários inconsistentes.

Quanto mais cedo esses problemas forem identificados, menor será seu impacto.

---

# Boas práticas

Durante a geração e a coleta, algumas práticas são recomendadas.

- Registrar a origem de cada dado.
- Preservar o horário do evento.
- Utilizar identificadores únicos sempre que possível.
- Validar dados obrigatórios.
- Evitar duplicidades.
- Registrar metadados relevantes.
- Padronizar formatos.
- Documentar as fontes de dados.

Essas práticas facilitam as etapas seguintes do ciclo de vida.

---

# Erros comuns

> [!failure]
> Alguns dos problemas mais frequentes encontrados em projetos de Engenharia de Dados surgem logo nas primeiras etapas do ciclo.

Entre eles:

- ausência de identificação da origem;
- coleta duplicada;
- perda de eventos;
- dados incompletos;
- registros inconsistentes;
- falta de padronização;
- ausência de documentação das fontes;
- dependência excessiva de entrada manual.

Muitos desses problemas tornam-se difíceis — ou até impossíveis — de corrigir posteriormente.

---

# Estudo de caso — DataRetail S.A.

Considere a empresa fictícia **DataRetail S.A.**

Sempre que um cliente realiza uma compra em uma loja física, ocorre o seguinte:

```mermaid
flowchart LR

A[Cliente realiza compra]

B[Sistema PDV]

C[ERP]

D[Registro da Venda]

A --> B
B --> C
C --> D
```

O evento original é a compra.

Os dados produzidos incluem:

- identificação da venda;
- data e hora;
- loja;
- operador do caixa;
- produtos;
- quantidades;
- valores;
- forma de pagamento.

Essas informações serão utilizadas nas próximas etapas do ciclo de vida.

---

# Conexão com os próximos capítulos

Neste capítulo estudamos como os dados são produzidos e capturados.

No próximo veremos como essas informações deixam seus sistemas de origem e passam a integrar plataformas de dados por meio do processo de **ingestão**, etapa responsável por transportar os dados entre diferentes ambientes.

---

# Resumo

Neste capítulo aprendemos que:

- todo dado possui uma origem;
- dados representam eventos do mundo real;
- geração e coleta são processos distintos;
- existem diversas fontes produtoras de dados;
- a qualidade começa na origem;
- problemas iniciais tendem a propagar-se por todo o ciclo de vida.

Esses conceitos serão fundamentais para compreender a próxima etapa: a ingestão de dados.

---

# Próximo Capítulo

➡️ [[05-Ingestao-de-Dados]]
