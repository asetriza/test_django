import os
import sys

sys.path.append(os.getcwd())
from src.aggregation.processing import processing_flghts

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job("cron", month="*", day_of_week="*", hour=0, minute=0, second=0)
def scheduled_job():
    processing_flghts()
    print("This job processes flghts and sends to db every day at 00:00:00 UTC 0")


@sched.scheduled_job("interval", minutes=30)
def timed_job():
    print("This job is run every 30 minutes.")


sched.start()
