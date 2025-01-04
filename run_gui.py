# run_gui.py
import streamlit.cli as stcli
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "gui/dashboard.py"]
    sys.exit(stcli.main())