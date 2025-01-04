import os
import kaggle

# Set the path to your Kaggle JSON configuration file relative to the current directory
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(), '.kaggle')

def fetch_kaggle_datasets():
    datasets = [
        # "davidcariboo/player-scores",
        # "martj42/international-football-results-from-1872-to-2017",
        "felipefonseca1992/club-football-match-data-2000-2025",
        "adamgbor/club-football-match-data-2000-2025"
        "davidcariboo/transfermarkt-football-data"
    ]
    for dataset in datasets:
        print(f"Downloading dataset: {dataset}")
        kaggle.api.dataset_download_files(dataset, path="data/datasets/raw", unzip=True)
    print("All datasets downloaded and extracted.")

if __name__ == "__main__":
    fetch_kaggle_datasets()
