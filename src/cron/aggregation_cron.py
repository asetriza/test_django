import os
import sys

sys.path.append(os.getcwd())
from src.aggregation.processing import processing_flghts
from src.cron.wakemydyno import wake_dyno

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job("cron", month="*", day_of_week="*", hour=3, minute=45, second=0)
def scheduled_job():
    processing_flghts()
    print("This job processes flghts and sends to db every day at 00:00:00 UTC 0")


@sched.scheduled_job("interval", minutes=1)
def timed_job():
    print(wake_dyno())
    print("This job is run every 1 minute.")


sched.start()
