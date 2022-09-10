import logging
from celery import Celery

app = Celery('tasks', broker='redis://redis:6379')
logger = logging.getLogger(__name__)

@app.task
def collector_task():
    logger.info("collector go on")
    # collector on mysql

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
   
    sender.add_periodic_task(10000, collector_task.s(), name='collector every 10 000 secs')
