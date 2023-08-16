from apscheduler.schedulers.blocking import BlockingScheduler
from mail import sendMail

sched = BlockingScheduler()

# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=19)
# def scheduled_job():
#     print('This job is run every weekday at 8 AM.')
#     sendMail()
# sched.start()


#For testing
@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every one minute.')
    sendMail()
sched.start()