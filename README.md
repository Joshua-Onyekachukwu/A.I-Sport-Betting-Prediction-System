# AI Sports Betting Prediction System
DEVELOPED BY JOSHUA OSEMEKE ONYEKACHUKWU 

## Overview
This system provides highly accurate predictions for football match outcomes and betting opportunities using advanced machine learning models.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure Kaggle API: Place `kaggle.json` in `~/.kaggle/`
3. Initialize database: `python init_db.py`
4. Fetch data: `python data/fetch_data.py`
5. Preprocess data: `python data/preprocess.py`
6. Train models: `python ml/train_model.py`
7. Run backend: `python run.py`
8. Run dashboard: `python run_gui.py`