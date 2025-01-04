# gui/main.py
import tkinter as tk
from tkinter import ttk
from gui.dashboard import Dashboard
from gui.betting_tools import BettingTools


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Sports Betting Prediction System")
        self.root.geometry("1200x800")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs
        self.dashboard_tab = Dashboard(self.notebook)
        self.betting_tools_tab = BettingTools(self.notebook)

        self.notebook.add(self.dashboard_tab.frame, text="Dashboard")
        self.notebook.add(self.betting_tools_tab.frame, text="Betting Tools")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()