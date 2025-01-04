# data/preprocess.py
import pandas as pd
import os


def preprocess_data():
    raw_data_dir = "data/datasets/raw"
    processed_data_dir = "data/datasets/processed"

    # Load raw datasets
    match_data = pd.read_csv(os.path.join(raw_data_dir, "all_matches.csv"))
    player_data = pd.read_csv(os.path.join(raw_data_dir, "players.csv"))

    # Example preprocessing steps
    match_data['date'] = pd.to_datetime(match_data['date'])
    match_data['home_team'] = match_data.groupby('home_team')['home_score'].transform(
        lambda x: x.rolling(window=5, min_periods=1).mean())
    match_data['away_team'] = match_data.groupby('away_team')['away_score'].transform(
        lambda x: x.rolling(window=5, min_periods=1).mean())

    # Save processed data
    match_data.to_csv(os.path.join(processed_data_dir, "processed_matches.csv"), index=False)
    player_data.to_csv(os.path.join(processed_data_dir, "processed_players.csv"), index=False)
    print("Data preprocessing complete.")


if __name__ == "__main__":
    preprocess_data()