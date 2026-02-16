# file: scheduler_service.py
from apscheduler.schedulers.blocking import BlockingScheduler
from run_visuals import main as run_main

sched = BlockingScheduler(timezone="UTC")

@sched.scheduled_job("cron", hour=6, minute=0)
def daily_job():
    code = run_main()
    if code != 0:
        # send notification here
        pass

@sched.scheduled_job("interval", minutes=30)
def heartbeat():
    print("Service alive")

if __name__ == "__main__":
    sched.start()
