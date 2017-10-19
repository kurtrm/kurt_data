"""Scheduler pending use for pulling data."""
import schedule
import time

schedule.every().day.at("05:45").do()

while True:
    schedule.run_pending()
    time.sleep(1)
