# model_wrapper.py
"""
Wrapper de inferência para o modelo de previsão de atraso de voos.

Este módulo encapsula:
- carregamento do artefato treinado (joblib)
- execução do pipeline de Machine Learning
- aplicação do threshold de decisão

O backend deve interagir EXCLUSIVAMENTE com a função `predict_voo`.
"""

import joblib
import pandas as pd
from pathlib import Path

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
    Executa inferência do modelo de atraso de voos.

    Retorna:
        prediction (int): 0 = sem atraso | 1 = com atraso
        probability (float): probabilidade da classe 1
    """

    X_novo = pd.DataFrame([novo_voo])

    proba = modelo.predict_proba(X_novo)[:, 1][0]
    prediction = int(proba >= threshold)

    return {
        "prediction": prediction,
        "probability": float(proba)
    }
