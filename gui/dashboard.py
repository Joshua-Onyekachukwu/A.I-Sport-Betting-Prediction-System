# gui/dashboard.py
import tkinter as tk
from tkinter import ttk, messagebox
from ml.predict import predict_match_outcome
import pandas as pd


class Dashboard:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        # Title
        ttk.Label(self.frame, text="Match Prediction Dashboard", font=("Arial", 16)).pack(pady=10)

        # Input fields
        ttk.Label(self.frame, text="Home Team Form:").pack()
        self.home_team_form = ttk.Entry(self.frame)
        self.home_team_form.pack()

        ttk.Label(self.frame, text="Away Team Form:").pack()
        self.away_team_form = ttk.Entry(self.frame)
        self.away_team_form.pack()

        ttk.Label(self.frame, text="Home Score:").pack()
        self.home_score = ttk.Entry(self.frame)
        self.home_score.pack()

        ttk.Label(self.frame, text="Away Score:").pack()
        self.away_score = ttk.Entry(self.frame)
        self.away_score.pack()

        # Predict button
        ttk.Button(self.frame, text="Predict", command=self.predict).pack(pady=10)

        # Result display
        self.result_label = ttk.Label(self.frame, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def predict(self):
        try:
            # Get input data
            data = {
                "home_team_form": float(self.home_team_form.get()),
                "away_team_form": float(self.away_team_form.get()),
                "home_score": int(self.home_score.get()),
                "away_score": int(self.away_score.get())
            }

            # Generate prediction
            prediction = predict_match_outcome(pd.DataFrame([data]))
            self.result_label.config(text=f"Prediction: {prediction}")
        except Exception as e:
            messagebox.showerror("Error", str(e))