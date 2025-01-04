# ml/explain.py
import shap
import lime
import joblib
import pandas as pd


def explain_prediction(match_data):
    # Load trained model
    model = joblib.load("ml/models/model_checkpoints/xgb_model.pkl")

    # SHAP explanation
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(match_data)
    shap.summary_plot(shap_values, match_data)

    # LIME explanation
    explainer = lime.lime_tabular.LimeTabularExplainer(match_data.values, feature_names=match_data.columns)
    exp = explainer.explain_instance(match_data.iloc[0], model.predict_proba)
    exp.show_in_notebook()