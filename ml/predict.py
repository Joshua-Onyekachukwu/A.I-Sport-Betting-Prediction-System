# ml/predict.py
import joblib
import pandas as pd


def predict_match_outcome(match_data):
    # Load trained models
    xgb_model = joblib.load("ml/models/model_checkpoints/xgb_model.pkl")
    lgb_model = joblib.load("ml/models/model_checkpoints/lgb_model.pkl")

    # Generate predictions
    xgb_pred = xgb_model.predict(match_data)
    lgb_pred = lgb_model.predict(match_data)

    return {"xgb_prediction": xgb_pred, "lgb_prediction": lgb_pred}