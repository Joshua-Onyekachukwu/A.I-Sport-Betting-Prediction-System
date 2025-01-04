# data/database.py
import sqlite3
import pandas as pd

def save_to_db(data, table_name):
    conn = sqlite3.connect("ai_sports_betting.db")
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def load_from_db(table_name):
    conn = sqlite3.connect("ai_sports_betting.db")
    data = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return data