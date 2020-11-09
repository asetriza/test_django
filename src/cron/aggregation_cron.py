import os
import sys

sys.path.append(os.getcwd())
from src.aggregation.processing import processing_flghts

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job("cron", day_of_week="mon-sun", hour=18, minute=16, second=1)
def scheduled_job():
    processing_flghts()
    print("This job processes flghts and sends to db every day at 00:00:01")


@sched.scheduled_job(
    "cron", month="jan-dec", day_of_week="mon", hour=18, minute=36, second=1
)
def scheduled_job():
    print("This job is run every weekday at 5pm.")


@sched.scheduled_job("interval", minutes="*")
def timed_job():
    print("This job is run every 1 minutes.")


sched.start()
