Descrição do projeto

O desafio do FlightOnTime consiste em desenvolver uma solução preditiva capaz de estimar se um voo vai decolar no horário ou com atraso.

O time de Data Science criará um modelo que aprende padrões a partir de dados históricos de voos (companhia aérea, aeroporto, horário, dia da semana, etc.), e o time de Back-End construirá uma API que disponibiliza essa previsão em tempo real, permitindo que outros sistemas consultem facilmente se um voo tem risco de atraso.

Necessidade do cliente (explicação não técnica)

Todos que viajam de avião — e especialmente as companhias aéreas e aeroportos — sofrem com atrasos.

Esses atrasos causam insatisfação nos passageiros, custos extras para as empresas e problemas de logística (como conexões perdidas e remanejamentos de voos).

O cliente quer prever, com base em dados do voo (origem, destino, horário, companhia aérea, etc.), qual é a probabilidade de o voo atrasar para se preparar com antecedência:

Passageiros podem receber alertas antes de sair de casa.

Companhias aéreas podem ajustar a operação e minimizar o impacto.

Aeroportos podem planejar melhor o uso da infraestrutura.

Validação de mercado

Prever atrasos é uma aplicação real e valiosa de ciência de dados em transporte.

Companhias aéreas e startups do setor usam modelos preditivos semelhantes para:

melhorar a pontualidade e o planejamento de frota;

reduzir custos operacionais e reclamações;

aumentar a satisfação do cliente com informações mais transparentes.

Mesmo um modelo simples pode ser útil, pois ajuda a identificar horários ou aeroportos com maior risco de atraso — um diferencial para o setor aéreo.

Expectativa para este hackathon

Público: alunos iniciantes em tecnologia, sem experiência profissional na área, que já estudaram Back-end (Java, Spring, APIs REST, persistência) e Data Science (Python, Pandas, scikit-learn, modelagem supervisionada).

Objetivo: criar um MVP (produto mínimo viável) que recebe informações de um voo e retorna se ele provavelmente será Pontual ou Atrasado.

Escopo sugerido: classificação binária (0 = Pontual, 1 = Atrasado) usando um dataset simples e limpo.

Entregáveis desejados

Notebook (Jupyter/Colab) do time de Data Science, contendo:

Exploração e limpeza de dados (EDA);

Criação de variáveis relevantes (ex.: hora do voo, dia da semana, aeroporto de origem/destino, companhia aérea);

Treinamento de um modelo preditivo (ex.: Logistic Regression, Random Forest);

Avaliação do desempenho (Acurácia, Precisão, Recall, F1-score);

Exportação do modelo serializado (joblib/pickle).

Aplicação Back-End (API REST) desenvolvida em Java (Spring Boot), contendo:

Endpoint /predict que recebe informações de um voo e retorna a previsão;

Integração com o modelo de DS (direta ou via microserviço separado);

Tratamento de erros e respostas padronizadas em JSON.
