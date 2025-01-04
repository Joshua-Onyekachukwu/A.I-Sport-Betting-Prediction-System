# ml/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import accuracy_score
import joblib


def train_models():
    # Load processed data
    data = pd.read_csv("data/datasets/processed/processed_matches.csv")

    # Feature and target selection
    features = ["home_team_form", "away_team_form", "home_score", "away_score"]
    target = "result"  # Assuming 'result' is a column in the dataset
    X = data[features]
    y = data[target]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost model
    xgb_model = xgb.XGBClassifier()
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    print(f"XGBoost Accuracy: {accuracy_score(y_test, y_pred_xgb)}")
    joblib.dump(xgb_model, "ml/models/model_checkpoints/xgb_model.pkl")

    # Train LightGBM model
    lgb_model = lgb.LGBMClassifier()
    lgb_model.fit(X_train, y_train)
    y_pred_lgb = lgb_model.predict(X_test)
    print(f"LightGBM Accuracy: {accuracy_score(y_test, y_pred_lgb)}")
    joblib.dump(lgb_model, "ml/models/model_checkpoints/lgb_model.pkl")