# gui/betting_tools.py
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


class BettingTools:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        # Title
        ttk.Label(self.frame, text="Betting Tools", font=("Arial", 16)).pack(pady=10)

        # Input fields
        ttk.Label(self.frame, text="Odds:").pack()
        self.odds = ttk.Entry(self.frame)
        self.odds.pack()

        ttk.Label(self.frame, text="Probability:").pack()
        self.probability = ttk.Entry(self.frame)
        self.probability.pack()

        # Calculate EV button
        ttk.Button(self.frame, text="Calculate Expected Value", command=self.calculate_ev).pack(pady=10)

        # Result display
        self.ev_label = ttk.Label(self.frame, text="", font=("Arial", 14))
        self.ev_label.pack(pady=10)

    def calculate_ev(self):
        try:
            odds = float(self.odds.get())
            probability = float(self.probability.get())
            ev = (odds * probability) - (1 - probability)
            self.ev_label.config(text=f"Expected Value: {ev:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))