from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dataUpdater import updater

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updater.update_data, 'interval', minutes=60)
    scheduler.start()