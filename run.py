# run.py
from gui.app import MainApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()