# ml/hyperparameter_tuning.py
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
import joblib


def tune_hyperparameters():
    # Load processed data
    data = pd.read_csv("data/datasets/processed/processed_matches.csv")
    features = ["home_team_form", "away_team_form", "home_score", "away_score"]
    target = "result"
    X = data[features]
    y = data[target]

    # Define parameter grid
    param_grid = {
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.1, 0.2],
        "n_estimators": [100, 200, 300]
    }

    # Perform grid search
    xgb_model = xgb.XGBClassifier()
    grid_search = GridSearchCV(xgb_model, param_grid, cv=3, scoring="accuracy")
    grid_search.fit(X, y)

    # Save best model
    joblib.dump(grid_search.best_estimator_, "ml/models/model_checkpoints/xgb_tuned_model.pkl")
    print(f"Best Parameters: {grid_search.best_params_}")