import os
import sys

sys.path.append(os.getcwd())
from src.aggregation.processing import processing_flghts

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job("cron", day_of_week="mon-sun", hour=18, minute=10, second=1)
def timed_job():
    processing_flghts()
    print("This job processes flghts and sends to db every day at 00:00:01")


sched.start()
