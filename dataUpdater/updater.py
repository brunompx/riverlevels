from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dataUpdater import apiClient

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apiClient.update_data(), 'interval', minutes=5)
    scheduler.start()