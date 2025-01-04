# utils/helpers.py
import pandas as pd

def validate_data(data):
    if data.isnull().any().any():
        raise ValueError("Data contains missing values.")