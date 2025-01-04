# tasks/celery_tasks.py
from celery import Celery
from data.fetch_data import fetch_kaggle_datasets

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def fetch_data_task():
    fetch_kaggle_datasets()