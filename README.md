# ✈️ AeroInsight — Previsão Inteligente de Atrasos de Voos

> **Sistema completo de Data Science & Machine Learning com foco em produção, integração via API e tomada de decisão baseada em risco.**

Este repositório apresenta um **projeto aplicado de previsão de atrasos de voos**, desenvolvido com base em **dados públicos oficiais**, utilizando práticas realistas de engenharia de dados, validação temporal e entrega de um **artefato único pronto para uso em produção**.

Embora desenvolvido no contexto de um hackathon educacional, o projeto **extrapola deliberadamente o escopo de um MVP simples**, priorizando arquitetura realista, robustez e integração com backend.

---

## 🎥 Demonstração em Vídeo

Uma demonstração resumida do projeto, apresentando o pipeline de dados, as decisões técnicas e a integração entre Data Science e Backend.

➡️ [Assistir vídeo de demonstração](https://drive.google.com/file/d/1ed7sWZXfKuD38DUxaAGuk-G_lvv6tygc/view?usp=sharing)

---

## 📌 Contexto Institucional

Este projeto foi desenvolvido no contexto do programa **Oracle Next Education (ONE)**.

- **Programa:** Oracle Next Education (ONE)
- **Turma:** G8
- **Hackathon:** Hackathon ONE II – Brasil
- **Equipe:** H12-25-B — Equipo 41 (Data Science)

O objetivo do hackathon foi criar uma solução aplicada de Ciência de Dados, integrando **modelagem preditiva**, **engenharia de dados** e **uso em produção**, seguindo boas práticas industriais.

---

## 🎯 Problema de Negócio

Atrasos de voos geram impactos significativos em:

- Custos operacionais de companhias aéreas  
- Logística aeroportuária e conexões  
- Planejamento de frota e tripulação  
- Experiência e satisfação do passageiro  

A pergunta central do projeto é:

> **“Dado um voo, qual é a probabilidade de ele sofrer um atraso relevante?”**

O foco do sistema **não é prever com 100% de acerto**, mas fornecer **probabilidades confiáveis de risco**, permitindo decisões antecipadas e mitigação de impacto operacional.

---

## 🧠 Formulação do Problema

O problema foi formulado como uma **classificação binária supervisionada**:

| Classe | Definição |
|------|----------|
| `0` | Voo sem atraso relevante |
| `1` | Voo com atraso ≥ 15 minutos |

O modelo retorna:

- a classe prevista  
- a **probabilidade associada**, utilizada por regras de negócio, alertas e sistemas externos  

---

## 📊 Fontes de Dados Oficiais

O projeto utiliza **exclusivamente dados públicos e confiáveis**, garantindo reprodutibilidade e validade analítica:

- **ANAC (Brasil)** — dados operacionais de voos comerciais  
- **Bureau of Transportation Statistics (EUA)** — dados oficiais do DOT  
- **ERA5 / ECMWF** — dados meteorológicos de reanálise climática  
- **OurAirports** — dados geográficos de aeroportos (IATA e ICAO)  

---

## 🧩 Arquitetura do Pipeline de Dados

O pipeline foi projetado seguindo princípios de **engenharia de dados moderna**, com foco em uso real em produção.

### 🔹 ETL Operacional

- Padronização e unificação de bases heterogêneas (ANAC + BTS)  
- Criação de features exclusivamente **pré-voo**  
- Definição consistente do target (`delay ≥ 15 min`)  

### 🔹 Enriquecimento Geográfico

- Associação espacial por latitude e longitude  
- Suporte simultâneo a códigos **ICAO e IATA**  

### 🔹 Enriquecimento Climático

- Integração com dados ERA5  
- Extração de variáveis em janelas de **1h e 3h antes do voo**  
- Variáveis: vento, chuva, nebulosidade e neve  
- Matching espacial por ponto geográfico mais próximo  

### 🔹 Enriquecimento Temporal

- Feriados nacionais (Brasil e EUA)  
- Vésperas, pós-feriados e finais de semana prolongados  
- Consideração do país do aeroporto de origem  

### 🔹 Histórico Operacional (Features Estatísticas)

- Taxas rolling de atraso (30 dias) por:  
  - rota  
  - aeroporto de origem  
  - companhia aérea  
- Janelas móveis com `closed="left"`  
  → **sem vazamento de informação temporal**  

### 🔹 Persistência

- Dataset final salvo em **Parquet**  
- Pipeline preparado para grandes volumes de dados  

---

## ⏱️ Validação Temporal e Disponibilidade de Dados

A estratégia de validação temporal utiliza **anos completos de 2023 e 2024 como conjunto de treino**, enquanto o conjunto de teste corresponde ao **ano de 2025 até o mês de setembro**.

Essa decisão reflete uma **limitação natural de disponibilidade de dados**, uma vez que o ano corrente ainda não estava totalmente consolidado no momento do desenvolvimento.

Essa abordagem simula um **cenário real de produção**, garantindo:

- ausência de *data leakage*  
- avaliação realista de generalização  
- alinhamento com práticas operacionais do mundo real  

---

## 🧠 Estratégia de Modelagem

- **Algoritmo:** Random Forest Classifier  

### Justificativas Técnicas

- Captura relações não lineares  
- Robustez a ruído e outliers  
- Baixa sensibilidade à multicolinearidade  
- Bom desempenho em dados heterogêneos  
- Estabilidade em produção  
- Serialização simples e confiável  

---

## ⚙️ Pipeline de Machine Learning

- `ColumnTransformer` para pré-processamento  
- Encoding categórico com `min_frequency`, `max_categories` e `handle_unknown="ignore"`  
- Pipeline único de **treino e inferência**  
- Artefato serializado contendo modelo + threshold  

---

## 📈 Avaliação e Estratégia de Decisão

A avaliação foi realizada exclusivamente em **dados futuros (2025 até setembro)**.

- Métricas: Precision, Recall, F1-score  
- Análise explícita de trade-off entre falsos positivos e falsos negativos  
- Ajuste manual de **threshold de decisão**  
- Priorização da **detecção preventiva de risco**  

O modelo é intencionalmente **probabilístico e conservador**.

---

## 📦 Entrega para Produção

O projeto entrega um **artefato único de inferência**, pronto para consumo por APIs e sistemas externos:

```python
artefato = {
    "pipeline": modelo_treinado,
    "threshold": 0.502
}
```

Esse formato garante:

- consistência entre treino e produção
- integração simples com backend
- previsões reproduzíveis

---

### 📦 Organização dos Releases

Os artefatos do projeto estão organizados em releases distintos:

- **Dataset**: contém os dados consolidados utilizados como base do projeto.
- **Data Processed**: contém todos os artefatos gerados ou obtidos via pipeline de código, incluindo dados climáticos (ERA5), arquivos processados intermediários, wrappers e modelos serializados.

Essa separação reflete práticas reais de projetos de dados, distinguindo dados de entrada e artefatos derivados.

---

## 🔌 Integração com Backend

O modelo foi projetado para ser consumido por uma API REST, que:

- valida o contrato de features
- garante ordem e tipo das variáveis
- retorna previsão (Pontual / Atrasado) e probabilidade associada

A integração evita dependência direta do notebook e simula um ambiente real de produção.

---

## 🧰 Stack Tecnológica

- Python 3.10+
- Pandas / NumPy
- Scikit-learn
- Xarray
- PyArrow / Parquet
- Joblib
- FastAPI

---

## 📌 Observações Importantes

Projeto desenvolvido ao longo de mais de 150 notebooks incrementais.

Este repositório consolida a versão final limpa e produtiva.

O vídeo de apresentação prioriza visão geral devido à limitação de tempo.

---

## 🏁 Conclusão

Este projeto demonstra a construção de um sistema completo de Data Science aplicado, abordando desafios reais de:

- dados heterogêneos
- validação temporal
- integração em produção
- tomada de decisão baseada em probabilidade

O trabalho foi desenvolvido com foco em empregabilidade, arquitetura realista e boas práticas industriais.
