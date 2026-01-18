# model_wrapper.py
"""
Wrapper de inferência para o modelo de previsão de atraso de voos.

Este módulo encapsula:
- carregamento do artefato treinado (joblib)
- execução do pipeline de Machine Learning
- aplicação do threshold de decisão

O backend deve interagir EXCLUSIVAMENTE com a função `predict_voo`.
"""
from pathlib import Path
import joblib
import pandas as pd


# ============================================================
# Carregamento do artefato
# ============================================================

ARTEFATO_PATH = Path("artefato_atraso_voos_rf.joblib")

artefato = joblib.load(ARTEFATO_PATH)
modelo = artefato["pipeline"]
threshold = artefato["threshold"]

# ============================================================
# Função de inferência
# ============================================================

def previsao_voo(novo_voo: dict) -> dict:
    """
    Retorna a classe mais provável (0 = No horário, 1 = Atrasado)
    e a probabilidade associada em percentual.
    """

    entrada_voo = pd.DataFrame([novo_voo])

    prob_no_horario, prob_atrasado = modelo.predict_proba(entrada_voo)[0]

    if prob_atrasado > prob_no_horario:
        classe_prevista = 1
        probabilidade = prob_atrasado
    else:
        classe_prevista = 0
        probabilidade = prob_no_horario

    return {
        "prediction": classe_prevista,
        "probability": float(round(probabilidade * 100,2))
    }



