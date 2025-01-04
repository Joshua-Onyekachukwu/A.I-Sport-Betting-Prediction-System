# tasks/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from tasks.celery_tasks import fetch_data_task

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_data_task, "interval", days=1)
scheduler.start()